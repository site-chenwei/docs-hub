---
title: "构建HSP模块时报错“Ohos BundleTool [Error]: hsp has home ability;Ohos BundleTool [Error]: CompressEntrance::main exit, verify failed.”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-180"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "构建HSP模块时报错“Ohos BundleTool [Error]: hsp has home ability;Ohos BundleTool [Error]: CompressEntrance::main exit, verify failed.”"
captured_at: "2026-04-17T02:03:23.289Z"
---

# 构建HSP模块时报错“Ohos BundleTool \[Error\]: hsp has home ability;Ohos BundleTool \[Error\]: CompressEntrance::main exit, verify failed.”

**问题现象**

构建HSP模块时出现以下错误：Ohos BundleTool \[Error\]: hsp 包含 home 能力；Ohos BundleTool \[Error\]: CompressEntrance::main 校验失败。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/HyHns878TUChL1p3LSTiwQ/zh-cn_image_0000002229758781.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=7C17FBDD4B3EFECD2020BE9879F7E770AE1F2D6269F956C4BD41C05910FE730E)

**问题原因**

1.  从DevEco Studio 5.0.2 Beta1版本开始，HSP支持配置UIAbility组件，除入口Ability外。
2.  构建过程中，HSP模块会将依赖的HAR中的Ability与其自身配置合并。因此，HSP不支持依赖带有入口Ability的HAR。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/AHDSIXBNSw25TVY1q82NJA/zh-cn_image_0000002229604285.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=9BE977BFF902DC31F7EC8917EF761459A4D7A15718B91EBFA31DF3E997F26DB3)

**解决措施**

1.  排查当前构建的HSP模块的module.json5，删除入口Ability中多余的skills配置，然后重新构建。
2.  排查HSP模块依赖的HAR模块的module.json5文件。如果入口Ability配置了HAR，则：
    1.  若为本地源码依赖，删除上述配置后重新构建，或移除HSP中对该模块的依赖。
    2.  若为第三方包依赖，需删除对应配置并重新发布，更新依赖版本后重新构建。
    3.  如果第三方包依赖无法重新发布，可以通过Hvigor自定义插件在HSP模块中增加自定义任务，删除build/${productName}/intermediates/package/${targetName}/module.json中的入口 Ability 相关配置，然后重新构建。
        
        // HSP module hvigorfile.ts
        import { hspTasks,OhosPluginId, Target } from '@ohos/hvigor-ohos-plugin';
        import { hvigor, HvigorNode, HvigorPlugin,FileUtil } from '@ohos/hvigor';
        export function customPlugin():HvigorPlugin {
            return {
                pluginId: 'customPlugin',
                context() {
                    return {
                        data: 'customPlugin xxx'
                    };
                },
                apply(currentNode:HvigorNode): Promise<void> {
                    hvigor.nodesEvaluated(async () => {
                        hspTask(currentNode);
                    });
                }
            }
        }
        function hspTask(currentNode: HvigorNode) {
            // Obtain contextual information of the HSP module
            const hspContext = currentNode.getContext(OhosPluginId.OHOS\_HSP\_PLUGIN) as OhosHspContext;
            hspContext?.targets((target: Target) => {
                const targetName = target.getTargetName();
                const outputPath = target.getBuildTargetOutputPath();
                const task = currentNode.getTaskByName(\`${targetName}@GeneratePkgModuleJson\`);
                currentNode.registerTask({
                    // TASK
                    name: \`${targetName}@changeModuleJson\`,
                    // Task execution logic entity function
                    run() {
                        const moduleJson = FileUtil.readJson5(outputPath+"/../../intermediates/package/"+targetName+"/module.json");
                        const abilities = moduleJson\['module'\]\['abilities'\];
                        abilities.forEach((ability)=>{
                            delete ability\['skills'\];
                        })
                        console.log('begin to rewrite module.json file.');
                        moduleJson\['module'\]\['abilities'\] = abilities
                        FileUtil.writeFileSync(outputPath+"/../../intermediates/package/"+targetName+"/module.json",JSON.stringify(moduleJson));
                    },
                    // Configure prerequisite task dependencies
                    dependencies: \[\`${targetName}@GeneratePkgModuleJson\`\],
                    // Post task dependencies for configuring tasks
                    postDependencies: \[\`${targetName}@PackageSharedHar\`\]
                });
            });
        }
        export default {
            system: hspTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
            plugins:\[customPlugin()\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
        }

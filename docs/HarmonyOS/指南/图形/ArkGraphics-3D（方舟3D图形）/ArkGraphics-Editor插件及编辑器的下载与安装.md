---
title: "ArkGraphics Editor插件及编辑器的下载与安装"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkgraphics-editor"
menu_path:
  - "指南"
  - "图形"
  - "ArkGraphics 3D（方舟3D图形）"
  - "ArkGraphics Editor插件及编辑器的下载与安装"
captured_at: "2026-04-17T01:36:09.253Z"
---

# ArkGraphics Editor插件及编辑器的下载与安装

3D编辑器ArkGraphics Editor提供3D模型、动画、ShaderGraph等核心编辑能力，可供设计师、开发者快速接入使用。支持通过拖拽等操作，利用3D编辑器可视化能力，完成3D场景开发，3D设计效果所见即所得。无需代码编写，支持从PC到移动端设备的快速流转， 可大幅提升3D应用开发效率。

#### 主要功能

ArkGraphics Editor编辑器当前主要支持功能如下：

-   编辑器工程的新建、打开、保存功能。
    
-   支持导入gltf格式的3D模型和image图片。
    
-   支持相机新增、修改、删除。
    
-   支持3D场景里模型的缩放、移动、旋转等拖动操作。
    
-   支持3D场景节点新增、修改、删除功能。
    
-   支持3D场景节点的属性设置，包括位置、颜色，旋转、缩放功能。
    
-   支持3D模型的动画新增、修改、删除功能。
    
-   支持3D模型的材质新增、修改、删除功能。
    
-   支持3D模型的ShaderGraph新增、修改、删除功能。
    
-   支持环境光的添加和设置。
    

ArkGraphics Editor插件支持的主要功能如下：

-   支持在DevEco中预览3D场景文件(.Scene)。
    
-   可点击“Open ArkGraphicsEditor”打开编辑器程序编辑3D资源。
    

#### 插件的安装及编辑器的使用

1.  前往[下载中心](https://developer.huawei.com/consumer/cn/download/)下载最新版本ArkGraphics Editor插件。
    
2.  点击DevEco Studio菜单项的File，选择Settings，选择左边列表的Plugins。
    
3.  点击Plugins窗口的顶部设置按钮，选择Install Plugin from Disk...。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/2vTHUfPoTHC14RfpycU8gg/zh-cn_image_0000002538019650.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=805FA297AE06111E9F2BCC06ABF88DCF0505881DBDA3BD60C87DDD4419D22148)
    
4.  选择下载的插件，进行安装。
    
5.  安装成功后，关闭DevEco Studio，再重新打开，选择3D工程里的\*.scene文件，可在DevEco Studio里打开显示3D场景内容。
    
6.  前往[下载中心](https://developer.huawei.com/consumer/cn/download/)下载最新版本ArkGraphics Editor编辑器，并进行安装。
    
    插件主要用来预览，当开发者需要进行3D编辑开发时，可点击“Open Ark Graphics Editor”打开3D编辑器对3D模型进行编辑。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/tztl0rbASVyzB_QCSbbBgw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=17BD79280ED7126A34004B84155F4C6C259EBB4EB9CEE57EA465D64EAB803EB1)
    
    -   要使用ArkGraphics Editor编辑器，需要满足以下条件：
        
        -   对应设备已安装Visual Studio 2022 Community。
            
        -   Visual Studio 2022 Community已安装使用C++ 进行桌面开发的选项。
            
    -   编辑器生成的3D资源文件，目前只支持在HarmonyOS 6.0.0及以上版本的设备上加载呈现。
        
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/zLcQVTVqQKqfzhpRnX1b4g/zh-cn_image_0000002538179580.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=89F335AFF827BBE54E3DFEB4A676BB6CFB80A6F810314DD5639F817A7F2246F2)
    

#### 创建使用3D编辑器资源的工程

1.  创建一个新工程或在已有工程下，右键工程名，选择New，选择Ark Graphics Editor Project。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/wg2-C2R3Rc250z1XwE3q0Q/zh-cn_image_0000002569019367.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=F480464BE9F5B001562B70BC8A24B809DB1D42A37C6D3A083ADBD8DC5BB66392)
    
2.  输入3D资源工程名。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/rzS7MQ1OQkyH_BkDuNGgNA/zh-cn_image_0000002568899359.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=CBB5911B762C94376976A20F5FFB7A7280EC167EACBFA0BCF0853C77E30A2FA6)
    
3.  双击default.scene，可显示创建的3D场景资源。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/RfNZ5wWCTnaQIq2QQDY9Yw/zh-cn_image_0000002538019652.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=91E69DFC44E68ACB82EF2A5138164841EFFD16132233ACC7F31F46441760CFE2)
    
4.  点击右下角Editor，可打开编辑器编辑3D资源，编辑保存后，可显示编辑后的资源。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/vogK4MeqRfOqj3uF05BbuQ/zh-cn_image_0000002538179582.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=C7EB619A1E9160205D29463E000E399A4706B0023B9D9E3DD61DD17E8559B1C5)
    
5.  修改复制资源脚本文件。
    
    脚本文件路径：xxx/MyApplication/entry/hvigorfile.ts
    
    运行工程时会执行该脚本将3D资源复制到assets目录下。
    
    ```ts
    // entry/hvigorfile.ts
    import { hapTasks } from '@ohos/hvigor-ohos-plugin';
     
    import { getNode } from '@ohos/hvigor';
    import * as MyEditorProject  from '../ArkGraphics/package-assets';
    MyEditorProject.packageAssetsToModule(getNode(__filename));
     
    export default {
        system: hapTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
        plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
    }
    ```
    
6.  修改Index.ets，加载3D资源。
    
    注意Index.ets代码内容中加载的目录名与3D资源工程名保持一致。
    
    ```ts
    // Index.ets
    import * as scene3d from '@ohos.graphics.scene'
     
    @Entry
    @Component
    struct Index {
      scene: scene3d.Scene | null = null;
      cam: scene3d.Camera | null = null;
      @State sceneOpts: SceneOptions | null = null;
      @State statusText: string = "";
     
      onPageShow(): void {
        this.Init();
      }
     
      Init(): void {
        if (this.scene == null) {
          this.statusText = 'Loading scene. Please wait.'
          const resource = $rawfile('ArkGraphics/assets/default.scene');
     
          scene3d.Scene.load(resource).then(async (scene: Scene) => {
            this.scene = scene;
     
            this.cam = this.scene.root?.getNodeByPath("Perspective Camera") as scene3d.Camera;
            this.cam.enabled = true;
     
            this.sceneOpts = { scene: this.scene, modelType: ModelType.SURFACE };
            this.statusText = 'Done.'
          }).catch(() => {
            this.statusText = 'Failed to load scene.'
          })
        }
      }
     
      build() {
        Row() {
          Column() {
            Text('Ark Graphics Scene Example 3')
            if (this.sceneOpts) {
              Component3D(this.sceneOpts).width('70%').height('70%')
            }
            if (this.statusText) {
              Text(this.statusText)
            }
          }.width('100%')
        }
        .height('100%')
      }
    }
    ```
    
7.  完成以上操作后，可在真机运行工程，观察3D资源加载效果。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/-mcvuUz9Qw2i_a2cSkWe0A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013609Z&HW-CC-Expire=86400&HW-CC-Sign=5D9BDBC6A83BA49060F4CE202538BC71619C5C443FF65F13E100E5A72BA78009)
    
    编辑器生成的3D资源文件，目前只支持在HarmonyOS 6.0.0及以上版本的设备上加载呈现。

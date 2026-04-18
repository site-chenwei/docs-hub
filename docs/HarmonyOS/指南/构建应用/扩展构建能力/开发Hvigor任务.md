---
title: "开发Hvigor任务"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-task"
menu_path:
  - "指南"
  - "构建应用"
  - "扩展构建能力"
  - "开发Hvigor任务"
captured_at: "2026-04-17T01:36:51.147Z"
---

# 开发Hvigor任务

#### 了解任务

任务是Hvigor构建过程中的基本执行单元，通常包含一段可执行代码；一个任务可以依赖其他多个任务。Hvigor任务调度执行时通过解析依赖关系确定任务执行时序。

UP-TO-DATE

任务标识，表示任务未实际执行。Hvigor任务增量跳过机制，在二次执行任务时检测任务输入输出条件未发生变化，则任务跳过执行提高构建效率。

示例：

\> hvigor UP-TO-DATE ::PackageApp...

Finished

任务执行完成标识，表示任务已执行完成。

示例：

\> hvigor Finished ::PackageApp... after 310 ms

#### 注册任务

使用HvigorNode节点对象注册任务。

1.  编辑工程下hvigorfile.ts文件。
    
    // 导入模块
    import { getNode, HvigorNode, HvigorTask } from '@ohos/hvigor';
    
2.  编写任务代码。
    
    // 获取当前hvigorNode节点对象
    const node: HvigorNode \= getNode(\_\_filename);
    
    // 注册Task
    node.registerTask({
      name: 'customTask',
      run() {
        console.log('this is Task');
      }
    });
    
3.  执行任务。
    
    使用hvigor命令行工具执行任务：
    
    hvigorw customTask
    
4.  查看任务执行结果。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/DL1ktIscSMiCJZex910Y0A/zh-cn_image_0000002561753201.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=8C5761AD6BD5668A311B956AAA458131E4F0254E263BDC4DB92B782A3FBA558A "点击放大")

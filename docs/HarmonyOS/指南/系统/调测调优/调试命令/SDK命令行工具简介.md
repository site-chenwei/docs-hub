---
title: "SDK命令行工具简介"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/command-line-tools-overview"
menu_path:
  - "指南"
  - "系统"
  - "调测调优"
  - "调试命令"
  - "SDK命令行工具简介"
captured_at: "2026-04-17T01:36:02.857Z"
---

# SDK命令行工具简介

当前SDK中包含了开发者在开发应用过程中需要使用的多种工具，可以实现日志查看、应用安装、启动测试等功能。

#### 命令行工具获取

-   通过SDK获取相关工具。其中SDK已嵌入[DevEco Studio](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-software-install)中，无需额外下载配置。SDK位于DevEco Studio的安装位置下的sdk目录中。
    
-   通过[Command Line Tools](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-commandline-get)工具中的sdk文件夹获取相关工具。
    

如需获取最新版本工具，请更新DevEco Studio或Command Line Tools。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/ao6dYIRVR_2blHd7VCyGrg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013602Z&HW-CC-Expire=86400&HW-CC-Sign=F25E5022CAF141DB90542A21E40B51D12353738A03715073737692F2AC696206)

各命令行工具存放位置有差异，详见各工具文档介绍。

#### 常用工具列表

| 命令 | 说明 |
| :-- | :-- |
| [hdc](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hdc) | 用于与设备进行交互调试、数据传输、查看日志等操作。 |
| [aa](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/aa-tool) | Ability助手用于启动应用和测试用例，提供应用调试和测试功能，如启动组件、强制停止进程、打印组件信息等。 |
| [bm](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/bm-tool) | 实现应用安装、卸载、更新、查询，提供基本的安装包调试能力。 |
| [hilog](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hilog) | 用于打印日志，记录用户操作和系统运行状态。 |
| [打包工具](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/packing-tool) | 用于在程序编译完成后，对编译出的文件等进行打包，以供安装发布。 |
| [拆包工具](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/unpacking-tool) | 支持通过命令行方式将HAP、HSP、App等文件解压成文件夹。提供Java接口对HAP、HSP、App等文件进行解析。 |

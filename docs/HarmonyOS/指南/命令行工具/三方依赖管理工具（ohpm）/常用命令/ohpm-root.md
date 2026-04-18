---
title: "ohpm root"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-root"
menu_path:
  - "指南"
  - "命令行工具"
  - "三方依赖管理工具（ohpm）"
  - "常用命令"
  - "ohpm root"
captured_at: "2026-04-17T01:36:52.373Z"
---

# ohpm root

在标准输出中打印有效的 oh\_modules 目录路径信息。

从ohpm 6.0.2.636版本开始，命令后支持配置log\_level和debug参数，用于查看日志级别和指定执行当前命令的日志级别。

#### 命令格式

ohpm root

#### 功能描述

可以在模块的任意子目录下执行，用于打印命令工作路径下所在包的有效 oh\_modules 目录路径信息。

#### Options

#### \[h2\]prefix

-   默认值：""
-   类型： string

可以在 root 命令后面配置 --prefix <string> 参数，用来指定包的根目录，该目录下必须存在 oh-package.json5 文件，将会打印该根目录中有效的 oh\_modules 目录路径信息。

#### \[h2\]log\_level

-   默认值：无
-   类型： String

可以在 root 命令后配置--log\_level <string>参数，指定执行当前命令的日志级别（info、debug、warn、error），如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

#### \[h2\]debug

-   默认值：false
-   类型： Boolean

可以在命令后配置--debug参数，指定执行当前命令的日志级别为debug，该配置仅在当前命令行生效，不修改.ohpmrc中的日志级别，如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

#### 示例

项目结构为：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/iPwy7jJpTeeSycYZpurf_A/zh-cn_image_0000002561752639.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=062F7DDD4410D3DC52C00D446EE0CC21CA5C71446B4BF09277BBF21D25940AFB)

在entry模块的src目录下执行：

ohpm root

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/yGAONdGMRXOUktXXCFT3fw/zh-cn_image_0000002530752698.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=53BC9DCE633A22970CCB45D7A6771999225D6D3DDACBBF7394E12249A5478DE1)

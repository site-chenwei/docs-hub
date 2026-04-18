---
title: "ohpm prepublish"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-prepublish"
menu_path:
  - "指南"
  - "命令行工具"
  - "三方依赖管理工具（ohpm）"
  - "常用命令"
  - "ohpm prepublish"
captured_at: "2026-04-17T01:36:52.454Z"
---

# ohpm prepublish

预发布一个三方库。

从ohpm 6.0.2.636版本开始，命令后支持配置log\_level和debug参数，用于查看日志级别和指定执行当前命令的日志级别。

#### 命令格式

ohpm prepublish \[options\] <har\_or\_tgz\_file>

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/vpN-5JdHSSymSXLe-UvdGg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=562776105D1E46C71EC6F8D6B78EB7ADED107C880A9F45409342B6D5F50BB139)

-   har\_or\_tgz\_file：压缩包路径，可以是 .har 包格式和由 hsp 模块打包出来的 .tgz 包格式，必选参数。
-   ohpm v1.8.0 版本开始支持prepublish命令。

#### 功能描述

-   拥有publish命令的所有内容校验规则，可以在发布前检测待发布的三方库能否通过ohpm客户端校验。
-   只校验待发布三方库内容，不对publish\_registry、publish\_id、key\_path等做校验。
-   包的格式、结构及具体校验规则可参考[publish命令说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-publish)。

#### Options

无。

#### \[h2\]log\_level

-   默认值：无
-   类型： String

可以在 prepublish 命令后配置--log\_level <string>参数，指定执行当前命令的日志级别（info、debug、warn、error），如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

#### \[h2\]debug

-   默认值：false
-   类型： Boolean

可以在命令后配置--debug参数，指定执行当前命令的日志级别为debug，该配置仅在当前命令行生效，不修改.ohpmrc中的日志级别，如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

#### 示例

预发布工作目录下的三方库，执行以下命令：

ohpm prepublish publish\_test.har

结果示例：

C:\\Program Files\\Huawei\\DevEco Studio\\tools\\ohpm\\bin> ohpm prepublish D:\\publish\_test.har
prepublish publish\_test 1.0.0 succeed.

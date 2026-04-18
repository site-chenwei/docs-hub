---
title: "ohpm init"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-init"
menu_path:
  - "指南"
  - "命令行工具"
  - "三方依赖管理工具（ohpm）"
  - "常用命令"
  - "ohpm init"
captured_at: "2026-04-17T01:36:52.266Z"
---

# ohpm init

创建 oh-package.json5 文件。

从ohpm 6.0.2.636版本开始，命令后支持配置log\_level和debug参数，用于查看日志级别和指定执行当前命令的日志级别。

#### 命令格式

ohpm init \[options\]

#### 功能描述

在工作目录下，生成一个新的 oh-package.json5 文件，初始化一个 package。

执行命令时，命令行会出现交互界面，可填写一系列关于三方库的基本信息，例如：三方库名称、版本等。ohpm 会根据现有字段、依赖项和所选选项做出合理的猜测，它会保留已设置的任何字段和值，在工作目录下创建一个 oh-package.json5 文件。

#### Options

#### \[h2\]yes

-   默认值：null
-   类型：null 或 Boolean
-   别名：y

可以在 init 命令后面指定 -y或者--yes 参数，命令行将会完全跳过交互界面，创建默认的 oh-package.json5 文件。

默认内容如下：

{
    "name": "work\_dir",
    "version": "1.0.0",
    "description": "",
    "main": "Index.ets",
    "author": "",
    "license": "ISC",
    "dependencies": {}
  }

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/lINkfv0zRF2kUixNkMgiMw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=9B51DC36FA1820F36BDAE003F3A931D31B977578E063068FE4D282AC7FBCBCDE)

若当前工作目录下不存在 oh-package.json5 文件，则文件中 name 字段默认为当前工作目录名称；若当前工作目录下已存在 oh-package.json5 文件，则新文件中 name 字段复用已存在文件中的 name 字段，并且最后覆盖原有oh-package.json5文件。

#### \[h2\]group

-   默认值：当前项目的命名空间 或 ""
-   类型：String
-   别名：g

可以在 init 命令后面配置 -g <group\_name> 或者 --group <group\_name>参数，创建一个 oh-package.json5 文件，其中 name 字段的命名空间为 @group\_name。

#### \[h2\]log\_level

-   默认值：无
-   类型： string

可以在 init 命令后配置--log\_level <string>参数，指定执行当前命令的日志级别（info、debug、warn、error），如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

#### \[h2\]debug

-   默认值：false
-   类型： Boolean

可以在命令后配置--debug参数，指定执行当前命令的日志级别为debug，该配置仅在当前命令行生效，不修改.ohpmrc中的日志级别，如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

#### 示例

-   当前工作目录下不存在 oh-package.json5 文件。
    
    在" D:\\demo " 路径下，执行如下命令：
    
    ohpm init -y
    
    执行结果为：
    
    Wrote to D:\\demo\\oh-package.json5:
    
    {
        "name": "demo",
        "version": "1.0.0",
        "description": "",
        "main": "Index.ets",
        "author": "",
        "license": "ISC",
        "dependencies": {}
    }
    
-   当前工作目录下已存在其中 name 字段为 demo\_name 的 oh-package.json5 文件。
    
    在" D:\\demo " 路径下，执行如下命令：
    
    ohpm init -y
    
    执行结果为：
    
    Wrote to D:\\demo\\oh-package.json5:
    
    {
        "name": "demo\_name",
        "version": "1.0.0",
        "description": "",
        "main": "Index.ets",
        "author": "",
        "license": "ISC",
        "dependencies": {}
    }
    
-   创建一个 oh-package.json5 文件，其中参数 name 字段为 "@group\_name/demo" ，而不是仅为 "demo"。
    
    ohpm init -g group\_name
    
    执行结果为：示例中 name 字段自动显示为 @group\_name/demo。
    
    package name: (@group\_name/demo)

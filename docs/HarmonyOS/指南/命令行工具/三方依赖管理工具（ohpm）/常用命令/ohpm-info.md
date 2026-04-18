---
title: "ohpm info"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-info"
menu_path:
  - "指南"
  - "命令行工具"
  - "三方依赖管理工具（ohpm）"
  - "常用命令"
  - "ohpm info"
captured_at: "2026-04-17T01:36:52.255Z"
---

# ohpm info

查询指定三方库的具体信息。

从ohpm 6.21.0版本开始，支持通过field查看三方库中元数据的属性，属性包括：keywords、dependencies、tags、versions、license、author、repository、dist、latest，具体请参考[Field](#section1068917464119)。

从ohpm 6.0.2.636版本开始，命令后支持配置log\_level和debug参数，用于查看日志级别和指定执行当前命令的日志级别。

#### 命令格式

ohpm info \[options\] \[<@group>/\]<pkg>\[@<version> | @tag:<tag>\] \[field\]

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/jElP87qSR_aWMWGPXNXlGA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=524D791CD0E4E16D3DADE1C34E57B0A3AF6D0698B9C84556573B1EA089788CDE)

-   @group：三方库的命名空间，可选。
-   pkg：三方库名称，必选。
-   version：三方库的版本号，可选。
-   tag：三方库的标签，标签会标记三方库的某个版本号，可选。

#### 功能描述

用于调用云端查询接口，查看指定包的详细信息，并将结果进行标准输出。

#### Options

#### \[h2\]registry

-   默认值：""
-   类型：URL

可以在 info 命令后面配置 --registry <registry> 参数，指定仓库地址；如果没有指定，默认从配置中获取仓库地址。

#### \[h2\]fetch\_timeout

-   默认值：60000
-   类型： Number
-   别名：ft

可以在 info 命令后面配置 --ft <number> 或者 --fetch\_timeout <number> 参数，用以设置操作的超时时间，如果没有指定，默认超时时间为60000ms。

#### \[h2\]strict\_ssl

-   默认值：true
-   类型： Boolean

可以在 info 命令后面配置 --strict\_ssl true 参数，校验 https 证书；配置 --strict\_ssl false 参数，不校验https证书。

#### \[h2\]pageNum

-   默认值：1
-   类型： Number

当field设置为versions时生效，可以在field后面配置 --pageNum <number> 参数，取值范围：\[1, 10000\]，表示在版本以列表分页展示时的页码数，可与pageSize一起使用。

#### \[h2\]pageSize

-   默认值：100
-   类型： Number

当field设置为versions时生效，可以在field后面配置 --pageSize <number> 参数，取值范围：\[1, 500\]，表示在版本以列表形式分页展示时每页的版本数量，可与pageNum一起使用。

#### \[h2\]debug

-   默认值：false
-   类型： Boolean

可以在命令后配置--debug参数，指定执行当前命令的日志级别为debug，该配置仅在当前命令行生效，不修改.ohpmrc中的日志级别，如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

#### \[h2\]log\_level

-   默认值：无
-   类型： string

可以在 info 命令后配置--log\_level <string>参数，指定执行当前命令的日志级别（info、debug、warn、error），如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/ioHW4qOpQTOuMbIKntJ8Fg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=D3ECA819A6F60ADB325505AB233003242CCF3AB6E7C8DF6A91BE87ADFFAA264E)

上述选项中配置的registry，fetch\_timeout和strict\_ssl，仅在执行当前info命令时生效，不会修改项目级或者用户级的配置文件。

#### Field

-   keywords：查看三方库的关键词。
-   dependencies：查看三方库的子依赖配置。
-   tags：查看三方库的tag列表。
-   versions：查看三方库版本列表，查询结果按照发布时间升序排列，以列表形式进行分页展示。可通过Options中[pageNum](#section12987141924519)和[pageSize](#section7425335114510)设置页码和每页数量，命令配置为versions --pageNum <number> --pageSize <number>。
-   license：查看三方库的许可证。
-   author：查看三方库的作者， 包括name 字段、 email 、url字段。
-   repository：查看三方库的源码地址。
-   dist：查看三方库的完整性字符串和.har包/.tgz包的下载地址。
-   latest：查看三方库最新发布的版本。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/Dkj7tJTdTuyBFmmDwqeQpA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=46405D70EF3F4CA14DF7669549B299F9B22C12D0BDDB3DF4FD92913AA6E665CA)

-   tags：展示三方库的所有tag列表，不支持在依赖名称后通过@拼接具体version或tag实现过滤，如'ohpm info @ohos/lottie tags'等同于'ohpm info @ohos/lottie@latest tags'、'ohpm info @ohos/lottie tags'等同于'ohpm info @ohos/lottie@1.0.0 tags'。
-   versions：分页展示三方库的版本列表，不支持在依赖名称后通过@拼接具体version或tag实现过滤。

#### 示例

#### \[h2\]示例1

命令：

ohpm info @ohos/lottie --registry https://ohpm.openharmony.cn/ohpm

结果：

➜ ohpm info @ohos/lottie --registry https://ohpm.openharmony.cn/ohpm

@ohos/lottie@2.0.10-rc.1 | MIT | deps: none | versions: 15
lottie是一个适用于OpenHarmony的动画库，它可以使用Bodymovin解析以json格式导出的Adobe After Effects动画，并在移动设备上进行本地渲染

keywords: OpenHarmony, HarmonyOS, Lottie

dist
.tarball: https://repo.harmonyos.com/ohpm/@ohos/lottie/-/lottie-2.0.10-rc.1.har
.integrity: sha512-fjdc1qJeEax+4/wA1eHdjvtLBOFxRGeU4J2F9Q1b+yRYjmZnzL6GCA241Ku5iyzG5j2RUZi6tyBa0rpyQnjhPg==

dist-tags:
latest: 2.0.10-rc.1

published 15 hours ago by ohos\_tpc

#### \[h2\]示例2

命令：

ohpm info @ohos/imageknife --registry https://ohpm.openharmony.cn/ohpm/ keywords

结果：

OpenHarmony, ImageKnife, glide, HarmonyOS

#### \[h2\]示例3

命令：

ohpm info @ohos/lottie --registry https://ohpm.openharmony.cn/ohpm versions --pageNum 1 --pageSize 500

结果：

current page num: 1, total pages: 88
2.0.0        2.0.1        2.0.10       2.0.10-rc.0  2.0.10-rc.1  2.0.10-rc.2  2.0.10-rc.3  2.0.10-rc.4  2.0.11       
2.0.11-rc.0  2.0.11-rc.1  2.0.11-rc.2  2.0.11-rc.3  2.0.11-rc.4  2.0.11-rc.5  2.0.11-rc.6  2.0.11-rc.7  ......

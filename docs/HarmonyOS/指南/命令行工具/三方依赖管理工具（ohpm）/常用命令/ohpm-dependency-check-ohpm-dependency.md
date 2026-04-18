---
title: "ohpm dependency"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-dependency-check"
menu_path:
  - "指南"
  - "命令行工具"
  - "三方依赖管理工具（ohpm）"
  - "常用命令"
  - "ohpm dependency-check"
captured_at: "2026-04-17T01:36:52.492Z"
---

# ohpm dependency-check

从ohpm 6.1.0.xxx版本开始，ohpm命令支持查询三方库的版本更新信息。

#### 命令格式

ohpm dependency-check \[options\] \[<@group>/<pkg>\]

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/H_goq1NBSgKqZgn19XqCoQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=9B0C5FBEE748D3EDE912D75B064482ADD6276607C3F64E42E9414DF8D7901949)

-   @group：三方库的命名空间，可选。
-   pkg：三方库名称，可选。

#### 功能描述

用于检查当前引入的三方库版本的更新信息。

#### Options

#### \[h2\]registry

-   默认值：""
-   类型：URL

可以在 dependency-check 命令后面配置 --registry <registry> 参数，指定仓库地址。如果不配置该参数，从配置中获取仓库地址。

#### \[h2\]fetch\_timeout

-   默认值：60000
-   类型： Number
-   别名：ft

可以在 dependency-check 命令后面配置 --ft <number> 或者 --fetch\_timeout <number> 参数，用以设置查询操作的超时时间，单位为ms。如果不配置该参数，超时时间为60000ms。

#### \[h2\]strict\_ssl

-   默认值：true
-   类型： Boolean

可以在 dependency-check 命令后面配置--strict\_ssl true参数，校验 https 证书。配置为--strict\_ssl false，不校验https证书。

#### \[h2\]retry\_times

-   默认值：1
-   类型： Number
-   别名：rt

可以在 dependency-check 命令后面配置 --rt <number> 或者 --retry\_times <number> 参数，设置失败时的重试次数。如果不配置该参数，默认重试1次。

#### \[h2\]retry\_interval

-   默认值：1000
-   类型： Number
-   别名：ri

可以在 dependency-check 命令后面配置 --ri <number> 或者 --retry\_interval <number> 参数，设置重试的间隔时间，单位为ms。如果不配置该参数，默认等待时间为1000ms。

#### \[h2\]all-modules

-   默认值：true
-   类型： Boolean
-   别名：all

可以在 dependency-check 命令后面配置 --all 或者 --all-modules 参数，获取所有模块（包括工程根目录）下的三方库版本的更新信息。

#### \[h2\]modules

-   默认值：""
-   类型： String
-   别名：m

可以在 dependency-check 命令后面配置 -m <string> 或者 --modules<string> 参数，string可以是一个或多个模块名称，多个模块时使用英文逗号隔开，用来获取模块下三方库版本的更新信息。

#### \[h2\]project

-   默认值：true
-   类型： Boolean
-   别名：p

可以在 dependency-check 命令后面配置 -p 或者 --project 参数，获取工程级目录下三方库版本的更新信息。

#### \[h2\]dev

-   默认值：true
-   类型： Boolean
-   别名：d

可以在 dependency-check 命令后面配置 -d 或者 --dev 参数，获取 oh-package.json5 文件的 devDependencies 中的三方库更新版本的信息。默认获取 oh-package.json5 文件的 dependencies 中的三方库版本的更新信息。

#### \[h2\]json

-   默认值：true
-   类型： Boolean
-   别名：j

可以在 dependency-check 命令后面配置 -j 或者 --json 参数，获取的三方库版本更新信息以json格式输出在控制台，且会输出到工程级目录下的 dependency-check-output.json 文件中。不配置此参数时，以表格形式输出在控制台或者dependency-check-output.txt文件中。

#### \[h2\]long

-   默认值：true
-   类型： Boolean
-   别名：l

可以在 dependency-check 命令后面配置 -l 或者 --long 参数，获取三方库版本的详细更新信息。不配置此参数时，获取三方库版本的简要更新信息。详细更新信息和简要更新信息展示的内容可参考[示例](#section1495275683016)。

#### \[h2\]console

-   默认值：true
-   类型： Boolean
-   别名：c

可以在 dependency-check 命令后面配置 -c 或者 --console 参数，默认会将获取到的三方库更新信息输出到工程级目录下的 dependency-check-output.txt 文件中，配置此参数可以将获取到的三方库更新信息同时输出到控制台。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/cTIUIdgLRU-J76jZn1isBQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=3984774533DCCC51CC65BD54958A300C31C64AC32020F387E01BE68BDE7CBAE0)

查询三方库的版本更新信息规则如下：

-   指定全部模块查询时，如果指定了三方库名称pkg，则查询全部模块（包括工程根目录）下该三方库更新信息。如果没有指定三方库名称，则查询全部模块（包括工程根目录）下所有三方库更新信息。
-   指定模块查询时，如果指定了三方库名称pkg，则查询指定模块下该三方库更新信息。如果没有指定三方库名称，则查询指定模块下所有三方库更新信息。
-   指定工程查询时，如果指定了三方库的名称pkg，则查询指定工程下该三方库更新信息。如果没有指定三方库名称，则查询指定工程下所有三方库更新信息。
-   当同时配置all-modules、modules、project命令时，按照all-modules > modules > project的优先级查询三方库更新信息。当均不配置时，以project范围查询三方库版本更新信息。

#### 示例

#### \[h2\]示例1

查询三方库的版本详细更新信息，执行一下命令。

ohpm dc --all -c -l

结果示例如下：

package                installed   wanted      latest  type   description     dependedBy  dependencyType  homepage                                                 
----------------------------------------------------------------------------------------------------------------------
checkupdate\_pkgc3      1.2.0       1.2.0       1.2.0   match  update to date  library     prod            http://a.c
checkupdate\_pkgc5      0.1.1       0.1.1       0.1.2   match  update to date  library     prod            http://a.c
checkupdate\_pkgc2      2.0.0       2.0.0       2.0.0   match  update to date  library     prod            http://a.c
checkupdate\_pkgea4     1.0.0       1.0.0       1.0.0   match  update to date  project     prod
@js-joda/core          5.5.2       5.5.2       5.6.0   match  update to date  project     prod            https://c.d
test-check-update      3.8.9-beta  3.8.9-beta  4.0.0   match  update to date  project     prod            https://a.y
Here are the recommended replacement packages for the following dependent packages :
checkupdate\_pkgea4->checkupdate\_test@2.0.0-beta, 三方测试库
checkupdate\_pkgea4->@fdddd/test@1.1.5, 三方测试库
@js-joda/core->checkupdate\_test@2.0.0-beta, 三方测试库
@js-joda/core->@fdddd/test@1.1.5, 三方测试库
test-check-update->checkupdate\_test@2.0.0, 三方测试库
Here is the security update information: 2 package container 2 vulnerabilities，2 malwares
checkupdate\_pkgea4@1.0.0, CVE-xxxx-xxxx test 跨站脚本漏洞,
checkupdate\_pkgea4@1.0.0, asfasdf
test-check-update@3.8.9-beta, CVE-xxxx-xxxxx test 跨站脚本漏洞
test-check-update@3.8.9-beta, virusxxx

#### \[h2\]示例2

查询三方库的版本简要更新信息，执行一下命令。

ohpm dc --all -c

结果示例如下：

package                installed   wanted      latest  type     dependedBy                                                   
----------------------------------------------------------------------------
checkupdate\_pkgc3      1.2.0       1.2.0       1.2.0   match    library     
checkupdate\_pkgc5      0.1.1       0.1.1       0.1.2   match    library     
checkupdate\_pkgc2      2.0.0       2.0.0       2.0.0   match    library     
checkupdate\_pkgea4     1.0.0       1.0.0       1.0.0   match    project     
@js-joda/core          5.5.2       5.5.2       5.6.0   match    project     
test-check-update      3.8.9-beta  3.8.9-beta  4.0.0   match    project     
Here are the recommended replacement packages for the following dependent packages :
checkupdate\_pkgea4->checkupdate\_test@2.0.0-beta, 三方测试库
checkupdate\_pkgea4->@fdddd/test@1.1.5, 三方测试库
@js-joda/core->checkupdate\_test@2.0.0-beta, 三方测试库
@js-joda/core->@fdddd/test@1.1.5, 三方测试库
test-check-update->checkupdate\_test@2.0.0, 三方测试库
Here is the security update information: 2 package container 2 vulnerabilities，2 malwares
checkupdate\_pkgea4@1.0.0, CVE-xxxx-xxxx test 跨站脚本漏洞,
checkupdate\_pkgea4@1.0.0, asfasdf
test-check-update@3.8.9-beta, CVE-xxxx-xxxxx test 跨站脚本漏洞
test-check-update@3.8.9-beta, virusxxx

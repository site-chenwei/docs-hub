---
title: "ohpm convert"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-convert"
menu_path:
  - "指南"
  - "命令行工具"
  - "三方依赖管理工具（ohpm）"
  - "常用命令"
  - "ohpm convert"
captured_at: "2026-04-17T01:36:52.485Z"
---

# ohpm convert

将npm三方库转换为ohpm三方库。因为语法差异，转换时仅对文件进行格式转换，不修改原npm包的代码逻辑。若HAR包在转换后出现代码不兼容的报错，开发者需修改原npm包的代码做适配。

从ohpm 6.0.2.636版本开始，命令后支持配置log\_level和debug参数，用于查看日志级别和指定执行当前命令的日志级别。

#### 命令格式

ohpm convert \[\[<@group>/\]<pkg>\[@<version> | @tag:<tag>\]\] --registry <string> \[--publish\]
ohpm convert <node\_modules\_path> \[--publish\]

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/1tHiek6_Q129_2HdNtWyhw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=72920F446A138E2AD7B23F20B485EE09CDA4E1D92145BD61A07712A32C09BBEF)

-   @group：三方库的命名空间，可选。
-   pkg：三方库名称，必选。
-   version：三方库的版本号，可选。
-   tag：三方库的标签，标签会标记三方库的某个版本号，可选。

#### 功能描述

将指定npm仓库中的某个包或者本地node\_modules目录下的包转换成满足ohpm格式要求的HAR包，并保存至当前工作目录，转换后的包将支持上传至ohpm-repo私仓或OpenHarmony三方库中心仓。

-   ohpm convert @group/pkg@version --registry <npm仓库地址>
    
    下载指定仓库中的某个包及其所有依赖项，并且将该包及其依赖转换为满足ohpm格式要求的HAR包。
    
-   ohpm convert <node\_modules\_path>
    
    转换本地node\_modules中的所有包为满足ohpm格式要求的HAR包，<node\_modules\_path>必须为npm执行install命令后生成的node\_modules目录。
    
    示例：
    
    ohpm convert ./xxxx/node\_modules
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/LvjXx1mTRpO1muEHLDSsVw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=95C61842B8CBA745C8989A06444B2FAADE8158B06D5AC30DD0E2E00B683205F3)

ohpm convert命令仅保留npm包中package.json配置文件中的name、version、main、types、license、description、author、keywords、homepage、repository、artifactType、dependencies、devDependencies、dynamicDependencies、overrides、scripts、hooks，module、packageType、typesVersions、exports和jsnext:main字段，具体字段说明请参考[oh-package.json5 字段说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-oh-package-json5#zh-cn_topic_0000001792256137_oh-packagejson5-字段说明)。

#### Options

#### \[h2\]registry

-   默认值：无
-   类型：URL

可以在convert命令后面配置 --registry <registry> 参数，指定仓库地址。如果指定了--registry，convert命令将从远程仓库地址下载指定的包及其依赖后，进行转换处理。如果没有指定--registry，convert命令将从本地node\_modules目录进行转换处理。

#### \[h2\]publish

-   默认值：false
-   类型： Boolean

可以在 convert命令后面配置 --publish 参数 ，若指定该参数，执行convert命令前请确认.ohpmrc推包相关配置无误，当所有包转换完成后将根据.ohpmrc中的配置依次进行推包。

#### \[h2\]log\_level

-   默认值：无
-   类型： String

可以在convert命令后配置--log\_level <string>参数，指定执行当前命令的日志级别（info、debug、warn、error），如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

#### \[h2\]debug

-   默认值：false
-   类型： Boolean

可以在命令后配置--debug参数，指定执行当前命令的日志级别为debug，该配置仅在当前命令行生效，不修改.ohpmrc中的日志级别，如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

#### 示例

**转换远程npm三方库中的包**

转换npm三方库中的axios包，执行以下命令：

ohpm convert axios --registry https://registry.npmjs.org/

结果示例：

PS C:\\Users\\xxxxx\\Desktop> ohpm convert axios --registry https://registry.npmjs.org
...
ohpm INFO: > start convert package: asynckit@0.4.0
ohpm INFO: > start convert package: axios@1.6.8
ohpm INFO: > start convert package: combined-stream@1.0.8
...
ohpm INFO: A total of 9 packets are converted successfully.
ohpm INFO: Converted packages are saved to the "C:\\Users\\xxxxx\\Desktop\\convert\_1712127991590" directory.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/GavkPAROSX24YBQ1dJ_aYA/zh-cn_image_0000002561833683.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=26D321AF10F15C4AAE867BEFFA8E0FFB28438529297F9EC5D4F68A751B8FC697 "点击放大")

**转换本地node\_modules目录中的包**

执行npm install uuid后，转换本地node\_modules目录中的包，执行以下命令：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/46KuaPWfR9S6xE20RqQdfw/zh-cn_image_0000002561753703.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=149B1C821F8E507627969449B38FA3BA79E301DA3113543862CEDEEDEA4D9D4E)

ohpm convert C:\\Users\\xxxxx\\Desktop\\uuidInstallDir\\node\_modules

结果示例：

PS C:\\Users\\xxxxx\\Desktop> ohpm convert C:\\Users\\xxxxx\\Desktop\\uuidInstallDir\\node\_modules
ohpm INFO: > start convert package: uuid
...
ohpm INFO: A total of 1 package(s) are converted successfully.
ohpm INFO: Converted packages are saved to the "C:\\Users\\xxxxx\\Desktop\\convert\_1712128912583" directory.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/C1Zt5QCmR3GErB45_SbTOQ/zh-cn_image_0000002530913760.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=A49F796485FEC05AAC471B6DD7B98A5C9510CFDD690E4EB0C698653341E242D2)

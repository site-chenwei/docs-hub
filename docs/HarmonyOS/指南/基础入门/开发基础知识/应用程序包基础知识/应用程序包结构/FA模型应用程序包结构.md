---
title: "FA模型应用程序包结构"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-package-structure-fa"
menu_path:
  - "指南"
  - "基础入门"
  - "开发基础知识"
  - "应用程序包基础知识"
  - "应用程序包结构"
  - "FA模型应用程序包结构"
captured_at: "2026-04-17T01:35:30.651Z"
---

# FA模型应用程序包结构

基于[FA模型](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-configuration-file-overview-fa)开发的应用，其应用程序包结构如下图应用程序包结构（FA模型）所示。开发者需要熟悉应用程序包结构相关的基本概念。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/AqkA_0QgTYqHFAO6WjeuUg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013531Z&HW-CC-Expire=86400&HW-CC-Sign=C4D2E644FBDE96C1C0F1CD4DF69CB5D05BCB524941412B8A5E18FE7B35F4A164)

API version 8及更早的版本支持的应用模型，FA模型已经不再主流。建议使用新的Stage模型进行开发。

FA模型与Stage模型的内部文件的存放位置不同。FA模型中，所有资源文件、库文件和代码文件都存放在assets文件夹中，并在文件夹内部进一步区分，Stage模型的内部文件的存放位置请参考[Stage模型应用程序包结构](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-package-structure-stage)。

-   config.json是应用配置文件，DevEco Studio会自动生成部分模块代码，开发者按需修改其中的配置。详细字段请参见[应用配置文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-configuration-file-overview-fa#配置文件的内部结构)。
    
-   assets是HAP所有的资源文件、库文件和代码文件的集合，内部可以分为entry和js文件夹。entry文件夹中存放的是resources目录和resources.index文件。
    
-   resources目录用于存放应用的资源文件（字符串、图片等），便于开发者使用和维护，详见[资源文件的使用](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/resource-categories-and-access)。
    
-   resources.index是资源索引表，由DevEco Studio调用SDK工具生成。
    
-   js文件夹中存放的是编译后的代码文件。
    
-   pack.info 是 Bundle 中用于描述每个 HAP 属性的文件，包含应用的 bundleName 和 versionCode 信息、模块的 name、type 和 abilities 等信息。该文件由 DevEco Studio 工具在构建 Bundle 包时自动生成。
    

**图1** 应用程序包结构（FA模型）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/jOnunkW2SxaNLG9DrVcrvQ/zh-cn_image_0000002569018105.png?HW-CC-KV=V1&HW-CC-Date=20260417T013531Z&HW-CC-Expire=86400&HW-CC-Sign=D9F55E1FC74D878D9C0D7EF607EDAADA6D1C198E42936D21C36400300EC4A61D)

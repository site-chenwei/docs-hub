---
title: "编译报错“The local dependency below in module %s is invalid”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-143"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "编译报错“The local dependency below in module %s is invalid”"
captured_at: "2026-04-17T02:03:22.872Z"
---

# 编译报错“The local dependency below in module %s is invalid”

**错误描述**

模块内添加本地依赖项无效。

**可能原因**

当设置"harLocalDependencyCheck": true时，若har模块添加模块外依赖，将触发该编译报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/Mzqp-2jxTpygLCr2vtqasQ/zh-cn_image_0000002194158324.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=9C8860AF5E9E789A390B3D14504845625C93F8127605D03D5D962A3325351A79)

**解决措施**

设置"harLocalDependencyCheck": true时，确保模块的oh-package.json5文件中，在dependencies和dynamicDependencies下指定的本地依赖都在当前模块目录下。

---
title: "编译报错“The metadata field in FormExtensionAbility cannot be left blank or as an empty array”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-164"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "编译报错“The metadata field in FormExtensionAbility cannot be left blank or as an empty array”"
captured_at: "2026-04-17T02:03:23.192Z"
---

# 编译报错“The metadata field in FormExtensionAbility cannot be left blank or as an empty array”

**错误描述**

FormExtensionAbility中的metadata字段必须非空且不为数组。

**可能原因**

在module.json5文件中，当ExtensionAbility的type为form时，metadata字段可以是空对象或空数组。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/OTu2rDtpTEOVnN4jIy2imQ/zh-cn_image_0000002194158712.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=B4200289DCC8F006EDE29033903849A47FD616D31E9749D593E9BEC534FF962D)

**解决措施**

在module.json5中type为form的ExtensionAbility中配置metadata字段，具体配置方式参考[配置ArkTS卡片的配置文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-configuration)。

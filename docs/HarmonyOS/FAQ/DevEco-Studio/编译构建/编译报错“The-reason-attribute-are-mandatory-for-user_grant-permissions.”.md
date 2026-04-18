---
title: "编译报错“The reason attribute are mandatory for user_grant permissions.”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-159"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "编译报错“The reason attribute are mandatory for user_grant permissions.”"
captured_at: "2026-04-17T02:03:23.098Z"
---

# 编译报错“The reason attribute are mandatory for user\_grant permissions.”

**错误描述**

针对Har和Hsp模块，配置user\_grant权限时必须包含reason属性。

**可能原因**

在module.json5文件中配置user\_grant类型的权限时，必须包含reason属性。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/o7QVoRnpQcuBh_WwUO6wCQ/zh-cn_image_0000002229758313.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=90F5FE0953E206C4D8572C8C48455576749369B9F3BBC755FEED687B727E179C)

**解决措施**

hap模块的module.json5文件中添加reason和usedScene字段。

在module.json5文件的requestPermissions中添加reason字段，用于har/hsp模块。

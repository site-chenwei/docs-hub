---
title: "编译报错“The reason and usedScene attributes are mandatory for user_grant permissions.”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-158"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "编译报错“The reason and usedScene attributes are mandatory for user_grant permissions.”"
captured_at: "2026-04-17T02:03:23.096Z"
---

# 编译报错“The reason and usedScene attributes are mandatory for user\_grant permissions.”

**错误描述**

针对Hap模块，配置user\_grant权限时必须包含reason和usedScene属性。

**可能原因**

在module.json5文件中配置user\_grant类型的权限时，必须包含reason和usedScene属性。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/TaIagfGvTQeT9LwgMqDlkw/zh-cn_image_0000002194158708.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=B74A34378857AAF496414E3F24CE3633EAAF7943FD44CE1E7FA1C6C0A5A9EB37)

**解决措施**

对于Hap模块，在module.json5文件的requestPermissions中添加reason和usedScene字段。

对于Har/Hsp模块，在module.json5文件的requestPermissions中添加reason字段。

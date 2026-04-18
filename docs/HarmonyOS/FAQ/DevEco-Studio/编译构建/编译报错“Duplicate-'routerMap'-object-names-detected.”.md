---
title: "编译报错“Duplicate 'routerMap' object names detected.”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-161"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "编译报错“Duplicate 'routerMap' object names detected.”"
captured_at: "2026-04-17T02:03:23.098Z"
---

# 编译报错“Duplicate 'routerMap' object names detected.”

**错误描述**

routerMap配置中存在重复名称。

**可能原因**

当前模块的router\_map.json文件中存在name重复的routerMap配置，或者当前模块与依赖模块之间存在name重复的routerMap配置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/Pbf7riRXRiSwKTbP8LJuOg/zh-cn_image_0000002229603813.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=1A23FBF6C61EDA5FD9F64CC3DF6D25C7160A8E70728AEF5CC0A47495C77347CE)

**解决措施**

修改router\_map.json文件中的name字段，确保其值唯一。

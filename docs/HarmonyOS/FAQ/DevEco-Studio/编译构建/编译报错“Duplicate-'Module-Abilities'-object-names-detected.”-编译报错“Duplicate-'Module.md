---
title: "编译报错“Duplicate 'Module"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-167"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "编译报错“Duplicate 'Module-Abilities' object names detected.”"
captured_at: "2026-04-17T02:03:23.235Z"
---

# 编译报错“Duplicate 'Module-Abilities' object names detected.”

**错误描述**

Module-Abilities对象名称重复。

**可能原因**

依赖的HAR模块中module.json5的abilities数组中存在重复的ability对象名称。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/EI8F-lJUQNiqHSU1bxdorw/zh-cn_image_0000002194158504.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=3FD96030392910F7965C7C20106D50231B110E2E5D90A4CEFDAB4E870D2FC49F)

**解决措施**

检查依赖的HAR模块在module.json5文件中的abilities字段，确保每个ability的name唯一。

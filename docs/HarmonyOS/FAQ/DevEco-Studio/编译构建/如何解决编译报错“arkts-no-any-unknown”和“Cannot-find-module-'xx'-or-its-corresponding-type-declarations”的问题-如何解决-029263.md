---
title: "如何解决编译报错“arkts"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-129"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "如何解决编译报错“arkts-no-any-unknown”和“Cannot find module 'xx' or its corresponding type declarations”的问题"
captured_at: "2026-04-17T02:03:22.640Z"
---

# 如何解决编译报错“arkts-no-any-unknown”和“Cannot find module 'xx' or its corresponding type declarations”的问题

**问题现象**

编译报错“arkts-no-any-unknown”和“Cannot find module 'xx' or its corresponding type declarations”。

**问题****原因**

大小写敏感导致模块无法找到。常见于图片中两种错误同时出现，且仅在Linux系统中出现，Windows和Mac系统不会报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/SCwjY9EAT8qO86lL6YpCZw/zh-cn_image_0000002194158772.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=37DEF61AC28583F5A344900302528075877B2176F2ACA3032DD2D04950FED1E2)

**解决方案**

解决引用中的大小写问题。

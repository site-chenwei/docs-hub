---
title: "如何解决编译报错“Declaration merging is not supported(arkts"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-127"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "如何解决编译报错“Declaration merging is not supported(arkts-no-decl-merging)” 或 “Cannot redeclare block-scoped variable 'xxx'”的问题"
captured_at: "2026-04-17T02:03:22.645Z"
---

# 如何解决编译报错“Declaration merging is not supported(arkts-no-decl-merging)” 或 “Cannot redeclare block-scoped variable 'xxx'”的问题

**问题现象**

在不同的文件中声明相同变量、interface、enum等类型，DevEco Studio不报错，但编译时会报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/XRk5XDOkQ6CkkziLANfYXw/zh-cn_image_0000002229604153.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=BE38D8708EB8A4BD9CF9FC785E518A7A426373CF4282FB51C62E1C33A175A359)

**解决方案**

如果文件中不包含export关键字，该文件将视为全局命名空间的一部分。

---
title: "如何获取BuildProfile中的值"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-72"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "如何获取BuildProfile中的值"
captured_at: "2026-04-17T02:03:21.935Z"
---

# 如何获取BuildProfile中的值

生成 BuildProfile 文件后，可以通过相对路径在代码中引入该文件。例如，在 HAR 模块的 Index.ets 文件中使用该文件：

import BuildProfile from './BuildProfile';

获取 BuildProfile 类中的值：

const HAR\_VERSION: string = BuildProfile.HAR\_VERSION;
const BUILD\_MODE\_NAME: string = BuildProfile.BUILD\_MODE\_NAME;
const DEBUG: boolean = BuildProfile.DEBUG;

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/PgD8vtqDTZSEGv5qJaI5NA/zh-cn_image_0000002229604169.png?HW-CC-KV=V1&HW-CC-Date=20260417T020322Z&HW-CC-Expire=86400&HW-CC-Sign=4A1D4707BD4C73E7C8B7E0F735674E55B669E6ECBF35FF001961A7248E9C5C70 "点击放大")

**参考链接**

[HAR运行时获取编译构建参数](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-get-build-profile-para-guide#section68146594553)

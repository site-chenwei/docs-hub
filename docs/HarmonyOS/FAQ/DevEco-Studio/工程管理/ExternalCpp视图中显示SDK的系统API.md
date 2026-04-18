---
title: "ExternalCpp视图中显示SDK的系统API"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-25"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "工程管理"
  - "ExternalCpp视图中显示SDK的系统API"
captured_at: "2026-04-17T02:03:20.653Z"
---

# ExternalCpp视图中显示SDK的系统API

**问题现象**

ExternalCpp视图中显示SDK的系统API。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/acKT6obVTFOUVdCRQkJI4A/zh-cn_image_0000002194158908.png?HW-CC-KV=V1&HW-CC-Date=20260417T020320Z&HW-CC-Expire=86400&HW-CC-Sign=4E7E98E538C36B645B1BEF9A32B327405E00547CCC53B57DFE1BD5163246028C)

**可能原因**

在本地存在多个DevEco Studio（包括Command Line Tools）打开同一个工程，并且使用daemon模式构建该工程。

**解决措施**

关闭多余的DevEco Studio（包括Command Line Tools）或者使用--no-daemon模式构建工程。

**参考链接**

[守护进程](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-daemon)

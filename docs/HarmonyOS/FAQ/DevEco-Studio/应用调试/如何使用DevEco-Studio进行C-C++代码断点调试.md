---
title: "如何使用DevEco Studio进行C/C++代码断点调试"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-26"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "应用调试"
  - "如何使用DevEco Studio进行C/C++代码断点调试"
captured_at: "2026-04-17T02:03:24.666Z"
---

# 如何使用DevEco Studio进行C/C++代码断点调试

**问题现象**

在DevEco Studio上的C/C++代码处打断点，调试运行时断点不生效。

**可能原因**

DevEco Studio进行ArkTS/JS + Native混合调试时需要配置DevEco Studio的调试模式。

**解决措施**

选择配置项：Run/Debug Configurations > Debugger > Dual(ArkTS/JS + Native)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/yzTopVGBRy6TfdlU7RFrEQ/zh-cn_image_0000002229604041.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=E6197F0801E1C15A24BCF29770E4F1153E699A13A409EECFF9B253D3FC73C14E "点击放大")

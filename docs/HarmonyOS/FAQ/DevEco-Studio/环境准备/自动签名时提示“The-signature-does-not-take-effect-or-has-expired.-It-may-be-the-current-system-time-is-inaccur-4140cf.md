---
title: "自动签名时提示“The signature does not take effect or has expired. It may be the current system time is inaccurate, please calibrate the system time and sign again”错误"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-14"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "环境准备"
  - "自动签名时提示“The signature does not take effect or has expired. It may be the current system time is inaccurate, please calibrate the system time and sign again”错误"
captured_at: "2026-04-17T02:03:20.295Z"
---

# 自动签名时提示“The signature does not take effect or has expired. It may be the current system time is inaccurate, please calibrate the system time and sign again”错误

**问题描述**

自动生成签名失败。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/Vx-Szi8HRk2z0NrMZwdOuw/zh-cn_image_0000002229604309.png?HW-CC-KV=V1&HW-CC-Date=20260417T020320Z&HW-CC-Expire=86400&HW-CC-Sign=24B879718D5C421A52B9AAD542151073DC8072EA2E795D6FEB1A709E478559B3)

**解决方案**

报错原因：本地PC和服务器时间不一致。请将本地PC时间与北京时间进行对比，精确到秒。

DevEco Studio签名提示系统时间不正确，请在设置中选择“时间和语言”>“日期和时间”，开启自动设置时间功能，确保时间精确到1-2秒。

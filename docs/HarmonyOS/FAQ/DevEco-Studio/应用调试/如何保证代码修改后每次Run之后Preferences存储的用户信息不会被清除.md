---
title: "如何保证代码修改后每次Run之后Preferences存储的用户信息不会被清除"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-58"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "应用调试"
  - "如何保证代码修改后每次Run之后Preferences存储的用户信息不会被清除"
captured_at: "2026-04-17T02:03:24.824Z"
---

# 如何保证代码修改后每次Run之后Preferences存储的用户信息不会被清除

如果需要在运行后保留存储在Preferences中的用户信息，可以在DevEco Studio中进行如下设置：点击“Run”->“Edit Configurations...”，进入“Debug Configurations”->“General”->“Installation Options”，勾选“Keep Application Data”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/H9KBzq3eRyui2Wh1b_645Q/zh-cn_image_0000002229758741.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=1EA8C1E4DA3A7B43E134C0FA00990584465C578F095A0B2BEF62EB675FCF4785)

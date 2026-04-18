---
title: "指标检测值无法点击拉起profiler"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-17"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "性能分析"
  - "指标检测值无法点击拉起profiler"
captured_at: "2026-04-17T02:03:25.190Z"
---

# 指标检测值无法点击拉起profiler

**问题现象**

报告详情页，指标检测值无法点击，如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/d190xrxISBKB0nz6r-SC7A/zh-cn_image_0000002527522192.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=714EEF7A13945AADDE6AEDAFA8C19955F6C59696D591651A4EEE447B1563BCB4)

预期是可以点击指标检测值并拉起profiler，如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/rUZfhjnbSVOiuZ4bkmea5Q/zh-cn_image_0000002558681913.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=ACCC4224CF4A53A0099029E43856873FD9748925046DBAEC72E9C15D88E600C6)

**问题原因**

体检卡片勾选冷启动场景，但在录制开始时未重启应用，导致堆栈抓取失败。

**解决措施**

1、建议冷启动场景，使用“手动性能冷启动体检”卡片进行检测。

2、如果是自定义卡片场景勾选“冷启动”场景，需要在录制开始时，强制重启应用，之后再进行体检。

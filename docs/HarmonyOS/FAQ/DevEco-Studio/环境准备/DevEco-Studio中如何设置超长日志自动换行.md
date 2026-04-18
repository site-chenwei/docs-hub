---
title: "DevEco Studio中如何设置超长日志自动换行"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-15"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "环境准备"
  - "DevEco Studio中如何设置超长日志自动换行"
captured_at: "2026-04-17T02:03:20.284Z"
---

# DevEco Studio中如何设置超长日志自动换行

启用Soft-Wrap功能以实现日志消息的自动换行。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/uEfbw134SeiwVZZq0ODVog/zh-cn_image_0000002194158840.png?HW-CC-KV=V1&HW-CC-Date=20260417T020320Z&HW-CC-Expire=86400&HW-CC-Sign=63756CE43B393710D15EAC6C1E1AC00E2E3150AD0EFEEE2521D55A09809C920B "点击放大")

日志单条打印的最大长度为4096个字符。建议在应用的日志框架中，对日志长度进行判断，若超过该长度则分段打印，以避免日志丢失。

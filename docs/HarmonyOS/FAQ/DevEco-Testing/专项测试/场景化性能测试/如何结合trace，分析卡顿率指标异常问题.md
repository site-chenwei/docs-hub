---
title: "如何结合trace，分析卡顿率指标异常问题"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-scenario-based-performance-test-12"
menu_path:
  - "FAQ"
  - "DevEco Testing"
  - "专项测试"
  - "场景化性能测试"
  - "如何结合trace，分析卡顿率指标异常问题"
captured_at: "2026-04-17T02:03:26.298Z"
---

# 如何结合trace，分析卡顿率指标异常问题

下载并打开trace后，通过上报的Present ID字段搜索，可快速定位问题点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/ZsvJ-3W_T3umBN0hRp5DJA/zh-cn_image_0000002229758405.png?HW-CC-KV=V1&HW-CC-Date=20260417T020327Z&HW-CC-Expire=86400&HW-CC-Sign=8FA72F7D3499D98A5148279CF7AFA5A19D4DDD1B162524C9467F50233326FFE7 "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/0oT8LmkhQluZw28mwvMBzw/zh-cn_image_0000002194318144.png?HW-CC-KV=V1&HW-CC-Date=20260417T020327Z&HW-CC-Expire=86400&HW-CC-Sign=C9A9CB1846A8903DA04C7993EBD204E536FF459865242A9484D987F3102F1112 "点击放大")

上图中，99009这一帧在屏幕上持续了33ms，超出应持续的16.6ms，被统计为丢1帧。

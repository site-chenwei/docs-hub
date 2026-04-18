---
title: "Profiler录制Launch，详情中Load ETS Files和TOP Redundant页签无数据"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-8"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "性能分析"
  - "Profiler录制Launch，详情中Load ETS Files和TOP Redundant页签无数据"
captured_at: "2026-04-17T02:03:25.037Z"
---

# Profiler录制Launch，详情中Load ETS Files和TOP Redundant页签无数据

**问题现象**

Profiler录制Launch，将ETS文件监控时长配置为20000，录制成功后，详情中Load ETS Files和TOP Redundant页签无数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/dE76SL-sTnOv2aWY2LxKZA/zh-cn_image_0000002314311052.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=D2A30965D1B5B5F3F71CFC7C3DC428A9D9ED8E69E266B138F780529B6B999187 "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/OtPkh_swSSqAdrrjFW6aBw/zh-cn_image_0000002314151220.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=EA7D8E0029FF9BB4F405B678D3431B89D9E2315AA31DA1001031663064D70077 "点击放大")

**问题原因**

ETS文件监控时长配置为20000，需要在拉起应用20000ms之后，才能生成对应的ETS冗余打点文件。

**解决措施**

将ETS文件监控时长配置为20000后，录制时长一定要大于配置时长。

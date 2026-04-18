---
title: "Profiler录制Allocation没有Native信息"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-5"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "性能分析"
  - "Profiler录制Allocation没有Native信息"
captured_at: "2026-04-17T02:03:24.941Z"
---

# Profiler录制Allocation没有Native信息

**解决措施**

取消勾选Run > Edit Configurations > Diagnostics 内的Address Sanitizer、Thread Sanitizer、Hardware-Assisted Address Sanitizer选项重新运行应用录制即可。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/BTxnPeIsRiyZY3X0Xe3X3g/zh-cn_image_0000002269366576.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=ED86F6CC48A6DB00D68E6B82757CB51B13F69BFDCA04FDDB9C758886E384DCCC)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/vTCjTET7Tsibdtbeq2SWCA/zh-cn_image_0000002304120341.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=A9C8B54D0A93EC87380B49CFAE183A9FF140A0BD5CC90F42400D7FA43C42AEA8)

---
title: "PC设备录制Allocation模板时，Graphic Memory泳道中OpenGL ES子泳道无数据"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-14"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "性能分析"
  - "PC设备录制Allocation模板时，Graphic Memory泳道中OpenGL ES子泳道无数据"
captured_at: "2026-04-17T02:03:25.131Z"
---

# PC设备录制Allocation模板时，Graphic Memory泳道中OpenGL ES子泳道无数据

**问题现象**

在使用PC设备时，通过FP回栈模式录制Allocation模板，Graphic Memory泳道中的OpenGL ES子泳道无数据。

**可能原因**

GPU底层库不支持FP回栈模式。

**解决措施**

开始录制前，单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/8rot7pn6SQSildiE5xNxDA/zh-cn_image_0000002538356035.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=50ED16AA553775F3B2D4882A1322F8ACB020F89BE0C4B5C5A8A06BD3FF1EB549 "点击放大")按钮，设置内存分配栈回栈模式为DWARF。使用DWARF回栈模式采集数据时，性能开销较大，因此在录制Graphic Memory泳道时，建议不同时录制Native Allocation泳道。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/NGGid0EnQd21urHgUaHmNQ/zh-cn_image_0000002506636162.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=11842F4B74604121767014A290CE08B771F0A391229FFEF580AF3CC95A3919D3 "点击放大")

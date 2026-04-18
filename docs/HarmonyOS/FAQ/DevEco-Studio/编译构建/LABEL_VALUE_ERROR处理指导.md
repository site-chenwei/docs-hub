---
title: "LABEL_VALUE_ERROR处理指导"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-15"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "LABEL_VALUE_ERROR处理指导"
captured_at: "2026-04-17T02:03:21.234Z"
---

# LABEL\_VALUE\_ERROR处理指导

**问题现象**

在工程同步、编译构建过程中，提示**LABEL\_VALUE\_ERROR**错误信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/-4hYDkESSoi4qHVLJyMBwA/zh-cn_image_0000002229758717.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=1E5F3D1F06576DFDA0694A6ADC850C30799D169965A7045943B1F17E5DBA97BB)

**解决措施**

该问题由config.json文件的资源引用规则变更引起，需将“label”字段的取值修改为资源引用方式。

1.  在**resources > base > element**中的string.json中添加对应的字符串信息。
2.  在config.json中重新引用该字符串资源。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/K3Bq6NbxTUCdt1XmTj10bQ/zh-cn_image_0000002194158844.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=4EA12B1D58EA17636247E4792FF801D8E1AF5591BA4BC70095B790CA54A68C41)

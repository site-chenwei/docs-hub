---
title: "AI框架算子适配概述"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-overview-of-ai-framework-operator"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "自定义算子开发"
  - "算子部署"
  - "AI框架算子适配"
  - "AI框架算子适配概述"
captured_at: "2026-04-17T01:36:25.061Z"
---

# AI框架算子适配概述

本章节内容介绍AI框架调用自定义算子的方法。如下图所示，PyTorch和TensorFlow仅支持图模式。

AI框架调用时，除了需要提供DDK框架调用时需要的代码实现文件，还需要对插件进行适配开发。下文仅展示通过ONNX框架进行算子适配，TensorFlow框架开发流程与ONNX框架开发流程一致。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/f6lgO51MS_yaqjjN95S8Zw/zh-cn_image_0000002538180122.png?HW-CC-KV=V1&HW-CC-Date=20260417T013627Z&HW-CC-Expire=86400&HW-CC-Sign=7F3E1969903D0AE2BE0A222F59B38BF5FFC507A6E5C11AFA7D2CC9E3C07604E6)

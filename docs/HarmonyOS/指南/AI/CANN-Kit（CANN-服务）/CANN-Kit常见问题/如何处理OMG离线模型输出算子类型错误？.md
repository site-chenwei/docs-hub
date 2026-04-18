---
title: "如何处理OMG离线模型输出算子类型错误？"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-faqs-4"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "CANN Kit常见问题"
  - "如何处理OMG离线模型输出算子类型错误？"
captured_at: "2026-04-17T01:36:38.774Z"
---

# 如何处理OMG离线模型输出算子类型错误？

Caffe网络中具有相同类型名但计算功能不同的层。比如DetectionOutput层，需要使用算子映射指明为FSRDetectionOutput、SSDDetectionOutput等检测算子类型，否则OMG生成离线模型会执行失败。为了避免出现错误，以下两种方案二选一即可。

-   方案1：可以在OMG命令中加入--op\_name\_map参数，参考[OMG参数](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-overall-parameter)中op\_name\_map参数设置。
    
-   方案2：可以在原始网络proto模型文件中将输出算子类型指定为SSDDetectionOutput等算子类型，如下图所示。
    
    **图1** 输出算子类型修改前（左）和修改后（右）
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/KLnTVvm1QfyC8T-xxFl89w/zh-cn_image_0000002538020236.png?HW-CC-KV=V1&HW-CC-Date=20260417T013638Z&HW-CC-Expire=86400&HW-CC-Sign=005271361D6839CF235A7DD5C65DCE82468870FC61C05F4D16A50CB16487722B)

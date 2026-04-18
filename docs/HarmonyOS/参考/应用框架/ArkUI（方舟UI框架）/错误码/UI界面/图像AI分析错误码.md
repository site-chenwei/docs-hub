---
title: "图像AI分析错误码"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-image-analyzer"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "错误码"
  - "UI界面"
  - "图像AI分析错误码"
captured_at: "2026-04-17T01:48:10.982Z"
---

# 图像AI分析错误码

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/ULRKSvRNQhS9HXY7jc0Q2A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014811Z&HW-CC-Expire=86400&HW-CC-Sign=6FBF83243D14699634931ECF00E67AD0540FFDA10476289346BFAC2C63B1D9F8)

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

#### 110001 AI图像分析功能不支持

**错误信息**

Image analysis feature is unsupported.

**错误描述**

当开发者调用startImageAnalyzer()接口时，若当前不支持AI分析功能，会抛出此错误码。

**可能原因**

调用不支持的功能接口。

**处理步骤**

NA

#### 110002 AI图像分析正在进行中

**错误信息**

Image analysis is currently being executed.

**错误描述**

当开发者调用startImageAnalyzer()接口时，若上一次的分析还没有结束，会抛出此错误码。

**可能原因**

调用接口时机错误。

**处理步骤**

NA

#### 110003 AI图像分析已停止

**错误信息**

Image analysis is stopped.

**错误描述**

当开发者调用startImageAnalyzer()接口，当前分析未完成时调用了stopImageAnalyzer()接口，会抛出此错误码。

**可能原因**

调用接口时机错误。

**处理步骤**

NA

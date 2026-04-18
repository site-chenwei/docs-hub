---
title: "ArkTS API错误码"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/natural-language-error-code"
menu_path:
  - "参考"
  - "AI"
  - "Natural Language Kit（自然语言理解服务）"
  - "ArkTS API错误码"
captured_at: "2026-04-17T01:49:05.191Z"
---

# ArkTS API错误码

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/VfKGSQlrTSO2wkO4LQZFwg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014905Z&HW-CC-Expire=86400&HW-CC-Sign=A58FB5EDABC56E9D07B6106B5597E7B9E4E7F3F75FADEEFA5143084B1B178454)

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

#### 200 运行超时

**错误信息**

Run timed out, please try again later.

**错误描述**

运行超时，请重试。

**可能原因**

当前存在大量的请求，无法及时处理。

**处理步骤**

过一段时间重试，并做好相关的逻辑判断。

#### 1011200001 运行失败

**错误信息**

Failed to run, please try again.

**错误描述**

运行失败，请重试。

**可能原因**

输入不符合要求，或服务存在异常。

**处理步骤**

过一段时间重试，并做好相关的逻辑判断。

#### 1011200002 服务异常

**错误信息**

The service is abnormal.

**错误描述**

服务异常时，系统会产生此错误码。

**可能原因**

服务异常。

**处理步骤**

系统异常，建议重启设备重试。

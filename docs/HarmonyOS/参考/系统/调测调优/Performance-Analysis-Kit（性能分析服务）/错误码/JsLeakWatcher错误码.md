---
title: "JsLeakWatcher错误码"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-jsleakwatcher"
menu_path:
  - "参考"
  - "系统"
  - "调测调优"
  - "Performance Analysis Kit（性能分析服务）"
  - "错误码"
  - "JsLeakWatcher错误码"
captured_at: "2026-04-17T01:48:35.403Z"
---

# JsLeakWatcher错误码

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/WJKbwixpQ0Cn2MD-B0TRSw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=4048DB96A398417EA4579FA670F1B4150EB40FED67583618C87ADD3C7792F0B1)

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

#### 10801001 参数isEnabled无效

**错误信息**

The parameter isEnabled is invalid.

**错误描述**

在调用接口函数enableLeakWatcher时，传入无效参数isEnabled。

**可能原因**

1.传入参数isEnabled的类型错误。

2.必填参数未指定。

**处理步骤**

确保传入参数isEnabled的类型正确。

#### 10801002 参数config无效

**错误信息**

The parameter config is invalid.

**错误描述**

在调用接口函数enableLeakWatcher时，传入无效参数config。

**可能原因**

1.传入参数config的类型错误。

2.必填参数未指定。

3.参数校验失败。该参数为字符串类型数组，数组元素必须包含：XComponent，NodeContainer，Window，Custom Component和Ability中一个或者多个。

**处理步骤**

确保传入参数config的类型正确。

#### 10801003 参数callback无效

**错误信息**

The parameter callback is invalid.

**错误描述**

在调用接口函数enableLeakWatcher时，传入无效参数callback。

**可能原因**

1.传入参数callback的类型错误。

2.必填参数未指定。

3.参数校验失败。校验callback回调函数入参是一个包含两个元素字符串类型数组。

**处理步骤**

确保传入参数callback的类型正确。callback是一个回调函数，该回调函数入参是一个包含两个元素字符串类型数组。

索引0为泄露列表文件名，后缀为.jsleaklist；索引1为虚拟机内存快照文件名，后缀为.rawheap。

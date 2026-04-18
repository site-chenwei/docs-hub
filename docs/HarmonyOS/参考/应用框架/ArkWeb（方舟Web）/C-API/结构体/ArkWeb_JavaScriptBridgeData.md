---
title: "ArkWeb_JavaScriptBridgeData"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-javascriptbridgedata"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkWeb（方舟Web）"
  - "C API"
  - "结构体"
  - "ArkWeb_JavaScriptBridgeData"
captured_at: "2026-04-17T01:48:13.078Z"
---

# ArkWeb\_JavaScriptBridgeData

```c
typedef struct {...} ArkWeb_JavaScriptBridgeData
```

#### 概述

定义JavaScript Bridge数据的基础结构。

**起始版本：** 12

**相关模块：** [Web](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web)

**所在头文件：** [arkweb\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| const uint8\_t\* buffer | 指向传输数据的指针。仅支持前端传入String和ArrayBuffer类型，其余类型会被json序列化后，以String类型传递。 |
| size\_t size | 传输数据的长度。 |

---
title: "Hid_EmitItem"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-emititem"
menu_path:
  - "参考"
  - "系统"
  - "硬件"
  - "Driver Development Kit（驱动开发服务）"
  - "C API"
  - "结构体"
  - "Hid_EmitItem"
captured_at: "2026-04-17T01:48:32.707Z"
---

# Hid\_EmitItem

```c
typedef struct Hid_EmitItem {...} Hid_EmitItem
```

#### 概述

事件信息。

**起始版本：** 11

**相关模块：** [HidDdk](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk)

**所在头文件：** [hid\_ddk\_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hid-ddk-types-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint16\_t type | 事件类型 |
| uint16\_t code | 事件编码 |
| uint32\_t value | 事件值 |

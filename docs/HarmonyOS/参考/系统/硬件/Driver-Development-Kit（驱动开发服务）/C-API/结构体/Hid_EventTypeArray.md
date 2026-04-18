---
title: "Hid_EventTypeArray"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-eventtypearray"
menu_path:
  - "参考"
  - "系统"
  - "硬件"
  - "Driver Development Kit（驱动开发服务）"
  - "C API"
  - "结构体"
  - "Hid_EventTypeArray"
captured_at: "2026-04-17T01:48:32.798Z"
---

# Hid\_EventTypeArray

```c
typedef struct Hid_EventTypeArray {...} Hid_EventTypeArray
```

#### 概述

事件类型编码数组。

**起始版本：** 11

**相关模块：** [HidDdk](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk)

**所在头文件：** [hid\_ddk\_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hid-ddk-types-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| Hid\_EventType\* hidEventType | 事件类型编码 |
| uint16\_t length | 数组的有效长度 |

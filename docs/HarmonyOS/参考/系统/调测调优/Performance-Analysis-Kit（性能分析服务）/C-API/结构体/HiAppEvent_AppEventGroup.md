---
title: "HiAppEvent_AppEventGroup"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-hiappevent-appeventgroup"
menu_path:
  - "参考"
  - "系统"
  - "调测调优"
  - "Performance Analysis Kit（性能分析服务）"
  - "C API"
  - "结构体"
  - "HiAppEvent_AppEventGroup"
captured_at: "2026-04-17T01:48:35.003Z"
---

# HiAppEvent\_AppEventGroup

```c
typedef struct HiAppEvent_AppEventGroup {...} HiAppEvent_AppEventGroup
```

#### 概述

一组事件信息，包含事件组的名称，按名称分组的单个事件信息数组，事件数组的长度。

**起始版本：** 12

**相关模块：** [HiAppEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent)

**所在头文件：** [hiappevent.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| const char\* name | 事件数组中相同的事件名称。 |
| const struct HiAppEvent\_AppEventInfo\* appEventInfos | 具有相同事件名称的事件数组。 |
| uint32\_t infoLen | 具有相同事件名称的事件数组的长度。 |

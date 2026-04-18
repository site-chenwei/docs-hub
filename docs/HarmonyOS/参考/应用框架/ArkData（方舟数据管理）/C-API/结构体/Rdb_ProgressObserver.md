---
title: "Rdb_ProgressObserver"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-progressobserver"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkData（方舟数据管理）"
  - "C API"
  - "结构体"
  - "Rdb_ProgressObserver"
captured_at: "2026-04-17T01:47:50.646Z"
---

# Rdb\_ProgressObserver

```c
typedef struct Rdb_ProgressObserver {...} Rdb_ProgressObserver
```

#### 概述

端云同步进度观察者。

**起始版本：** 11

**相关模块：** [RDB](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb)

**所在头文件：** [relational\_store.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-relational-store-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| void\* context | 端云同步进度观察者的上下文。 |
| [Rdb\_ProgressCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-relational-store-h#rdb_progresscallback) callback | 端云同步进度观察者的回调函数。 |

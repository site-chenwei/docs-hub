---
title: "Rdb_DataObserver"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-dataobserver"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkData（方舟数据管理）"
  - "C API"
  - "结构体"
  - "Rdb_DataObserver"
captured_at: "2026-04-17T01:47:50.560Z"
---

# Rdb\_DataObserver

```c
typedef struct Rdb_DataObserver {...} Rdb_DataObserver
```

#### 概述

表示数据观察者。

**起始版本：** 11

**相关模块：** [RDB](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb)

**所在头文件：** [relational\_store.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-relational-store-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| void\* context | 表示数据观察者的上下文。 |
| [Rdb\_SubscribeCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-subscribecallback) callback | 数据观察者的回调。 |

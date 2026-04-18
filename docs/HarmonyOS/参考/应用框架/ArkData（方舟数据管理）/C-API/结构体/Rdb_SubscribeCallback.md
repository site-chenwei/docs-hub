---
title: "Rdb_SubscribeCallback"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-subscribecallback"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkData（方舟数据管理）"
  - "C API"
  - "结构体"
  - "Rdb_SubscribeCallback"
captured_at: "2026-04-17T01:47:50.564Z"
---

# Rdb\_SubscribeCallback

```c
typedef union Rdb_SubscribeCallback {...} Rdb_SubscribeCallback
```

#### 概述

表示回调函数。

**起始版本：** 11

**相关模块：** [RDB](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb)

**所在头文件：** [relational\_store.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-relational-store-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [Rdb\_DetailsObserver](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-relational-store-h#rdb_detailsobserver) detailsObserver | 端云数据更改事件的细节的回调函数。 |
| [Rdb\_BriefObserver](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-relational-store-h#rdb_briefobserver) briefObserver | 端云数据更改事件的回调函数。 |

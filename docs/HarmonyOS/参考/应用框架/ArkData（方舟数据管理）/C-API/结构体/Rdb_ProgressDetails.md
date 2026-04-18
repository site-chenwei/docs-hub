---
title: "Rdb_ProgressDetails"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-progressdetails"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkData（方舟数据管理）"
  - "C API"
  - "结构体"
  - "Rdb_ProgressDetails"
captured_at: "2026-04-17T01:47:50.640Z"
---

# Rdb\_ProgressDetails

```c
typedef struct Rdb_ProgressDetails {...} Rdb_ProgressDetails
```

#### 概述

描述数据库整体执行端云同步任务上传和下载的统计信息。

**起始版本：** 11

**相关模块：** [RDB](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb)

**所在头文件：** [relational\_store.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-relational-store-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int version | 用于唯一标识OH\_TableDetails结构的版本。 |
| int schedule | 表示端云同步过程。 |
| int code | 表示端云同步过程的状态。 |
| int32\_t tableLength | 表示端云同步的表的数量。 |

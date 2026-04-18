---
title: "Rdb_Statistic"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-statistic"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkData（方舟数据管理）"
  - "C API"
  - "结构体"
  - "Rdb_Statistic"
captured_at: "2026-04-17T01:47:50.571Z"
---

# Rdb\_Statistic

```c
typedef struct Rdb_Statistic {...} Rdb_Statistic
```

#### 概述

描述数据库表的端云同步过程的统计信息。

**起始版本：** 11

**相关模块：** [RDB](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb)

**所在头文件：** [relational\_store.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-relational-store-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int total | 表示数据库表中需要端云同步的总行数。 |
| int successful | 表示数据库表中端云同步成功的行数。 |
| int failed | 表示数据库表中端云同步失败的行数。 |
| int remained | 表示数据库表中端云同步剩余未执行的行数。 |

---
title: "Rdb_KeyInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-keyinfo"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkData（方舟数据管理）"
  - "C API"
  - "结构体"
  - "Rdb_KeyInfo"
captured_at: "2026-04-17T01:47:50.490Z"
---

# Rdb\_KeyInfo

```c
typedef struct {...} Rdb_KeyInfo
```

#### 概述

描述发生变化的行的主键或者行号。

**起始版本：** 11

**相关模块：** [RDB](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb)

**所在头文件：** [relational\_store.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-relational-store-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int count | 表示发生变化的主键或者行号的数量。 |
| int type | 表示主键的类型[OH\_ColumnType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-data-value-h#oh_columntype)。 |
| [Rdb\_KeyData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-rdb-keydata)\* data | 存放变化的具体数据 |

---
title: "OH_Rdb_Config"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-rdb-config"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkData（方舟数据管理）"
  - "C API"
  - "结构体"
  - "OH_Rdb_Config"
captured_at: "2026-04-17T01:47:50.473Z"
---

# OH\_Rdb\_Config

```c
typedef struct  {...} OH_Rdb_Config
```

#### 概述

管理关系数据库配置。

**起始版本：** 10

**相关模块：** [RDB](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb)

**所在头文件：** [relational\_store.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-relational-store-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int selfSize | 该结构体的大小。 |
| const char\* dataBaseDir | 数据库文件路径。 |
| const char\* storeName | 数据库名称。 |
| const char\* bundleName | 应用包名。 |
| const char\* moduleName | 应用模块名。 |
| bool isEncrypt | 指定数据库是否加密。true表示加密，false表示不加密。 |
| int securityLevel | 设置数据库安全级别[OH\_Rdb\_SecurityLevel](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-relational-store-h#oh_rdb_securitylevel)。 |
| int area | 
设置数据库安全区域等级[Rdb\_SecurityArea](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-relational-store-h#rdb_securityarea)

**起始版本：** 11

 |

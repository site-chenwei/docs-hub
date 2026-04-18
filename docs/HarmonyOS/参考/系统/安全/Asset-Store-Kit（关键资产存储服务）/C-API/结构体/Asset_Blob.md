---
title: "Asset_Blob"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-assettype-asset-blob"
menu_path:
  - "参考"
  - "系统"
  - "安全"
  - "Asset Store Kit（关键资产存储服务）"
  - "C API"
  - "结构体"
  - "Asset_Blob"
captured_at: "2026-04-17T01:48:17.388Z"
---

# Asset\_Blob

```c
typedef struct {...} Asset_Blob
```

#### 概述

二进制数组类型，即不定长的字节数组。

**起始版本：** 11

**相关模块：** [AssetType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-assettype)

**所在头文件：** [asset\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-asset-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t size | 表示字节数组的大小。 |
| uint8\_t \*data | 指向字节数组的指针。 |

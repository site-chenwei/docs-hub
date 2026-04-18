---
title: "Asset_Value"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-assettype-asset-value"
menu_path:
  - "参考"
  - "系统"
  - "安全"
  - "Asset Store Kit（关键资产存储服务）"
  - "C API"
  - "结构体"
  - "Asset_Value"
captured_at: "2026-04-17T01:48:17.388Z"
---

# Asset\_Value

```c
typedef union {...} Asset_Value
```

#### 概述

关键资产属性内容。

**起始版本：** 11

**相关模块：** [AssetType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-assettype)

**所在头文件：** [asset\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-asset-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| bool boolean | 该字段用于传入bool类型的关键资产。 |
| uint32\_t u32 | 该字段用于传入uint32类型的关键资产。 |
| [Asset\_Blob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-assettype-asset-blob) blob | 该字段用于传入bytes类型的关键资产。 |

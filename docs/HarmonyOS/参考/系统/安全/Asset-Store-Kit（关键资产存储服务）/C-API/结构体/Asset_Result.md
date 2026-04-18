---
title: "Asset_Result"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-assettype-asset-result"
menu_path:
  - "参考"
  - "系统"
  - "安全"
  - "Asset Store Kit（关键资产存储服务）"
  - "C API"
  - "结构体"
  - "Asset_Result"
captured_at: "2026-04-17T01:48:17.426Z"
---

# Asset\_Result

```c
typedef struct {...} Asset_Result
```

#### 概述

关键资产查询结果，用于定义一条关键资产。

**起始版本：** 11

**相关模块：** [AssetType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-assettype)

**所在头文件：** [asset\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-asset-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t count | 关键资产属性的个数。 |
| [Asset\_Attr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-assettype-asset-attr) \*attrs | 指向关键资产属性数组的指针。 |

---
title: "Asset_SyncResult"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-assettype-asset-syncresult"
menu_path:
  - "参考"
  - "系统"
  - "安全"
  - "Asset Store Kit（关键资产存储服务）"
  - "C API"
  - "结构体"
  - "Asset_SyncResult"
captured_at: "2026-04-17T01:48:17.489Z"
---

# Asset\_SyncResult

```c
typedef struct {...} Asset_SyncResult
```

#### 概述

关键资产同步结果。

**起始版本：** 20

**相关模块：** [AssetType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-assettype)

**所在头文件：** [asset\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-asset-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int32\_t resultCode | 关键资产同步的结果码。 |
| uint32\_t totalCount | 触发同步的关键资产总数。 |
| uint32\_t failedCount | 关键资产同步失败的数量。 |

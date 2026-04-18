---
title: "NetworkBoost_MultiPathQuota"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-multipath_quota"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Network Boost Kit（网络加速服务）"
  - "C API"
  - "结构体"
  - "NetworkBoost_MultiPathQuota"
captured_at: "2026-04-17T01:48:24.921Z"
---

# NetworkBoost\_MultiPathQuota

#### 概述

应用配额信息，包含应用已使用配额信息和剩余配额信息。

**起始版本：** 6.0.2(22)

**相关模块：** [NetworkBoost](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-overview)

**所在头文件：** [network\_boost\_handover.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-files-handover)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [NetworkBoost\_MultiPathQuotaInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-multipath_quotainfo) [used](#used) | 应用已使用配额信息。 |
| [NetworkBoost\_MultiPathQuotaInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-multipath_quotainfo) [remaining](#remaining) | 应用剩余使用配额信息。 |

#### 结构体成员变量说明

#### used

```c
NetworkBoost_MultiPathQuotaInfo NetworkBoost_MultiPathQuota::used
```

**描述**

表明应用已使用配额信息。

#### remaining

```c
NetworkBoost_MultiPathQuotaInfo NetworkBoost_MultiPathQuota::remaining
```

**描述**

应用剩余使用配额信息。

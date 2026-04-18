---
title: "NetworkBoost_MultiPathQuotaInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-multipath_quotainfo"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Network Boost Kit（网络加速服务）"
  - "C API"
  - "结构体"
  - "NetworkBoost_MultiPathQuotaInfo"
captured_at: "2026-04-17T01:48:24.970Z"
---

# NetworkBoost\_MultiPathQuotaInfo

#### 概述

多网配额信息，包含配额次数信息和时长信息。

**起始版本：** 6.0.2(22)

**相关模块：** [NetworkBoost](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-overview)

**所在头文件：** [network\_boost\_handover.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-files-handover)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint16\_t [count](#count) | 配额次数信息。 |
| uint16\_t [duration](#duration) | 配额时长信息，单位为s。 |

#### 结构体成员变量说明

#### count

```c
uint16_t NetworkBoost_MultiPathQuotaInfo::count
```

**描述**

配额次数信息。

#### duration

```c
uint16_t NetworkBoost_MultiPathQuotaInfo::duration
```

**描述**

配额时长信息，单位为s。

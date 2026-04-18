---
title: "NetworkBoost_HandoverStart"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-handover_start"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Network Boost Kit（网络加速服务）"
  - "C API"
  - "结构体"
  - "NetworkBoost_HandoverStart"
captured_at: "2026-04-17T01:48:24.658Z"
---

# NetworkBoost\_HandoverStart

#### 概述

连接迁移开始信息。

**起始版本：** 5.1.0(18)

**相关模块：** [NetworkBoost](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-overview)

**所在头文件：** [network\_boost\_handover.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-files-handover)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t [expires](#expires) | 连接迁移全流程的超时时间，单位为s，取值为任意正整数或者0。 |
| [NetworkBoost\_DataSpeedAction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-data_speed_action) [dataSpeedAction](#dataspeedaction) | 老链路的发包建议。 |

#### 结构体成员变量说明

#### \[h2\]dataSpeedAction

```c
NetworkBoost_DataSpeedAction NetworkBoost_HandoverStart::dataSpeedAction
```

**描述**

老链路的发包建议。

#### \[h2\]expires

```c
uint32_t NetworkBoost_HandoverStart::expires
```

**描述**

连接迁移全流程的超时时间，单位为s，取值为任意正整数或者0。

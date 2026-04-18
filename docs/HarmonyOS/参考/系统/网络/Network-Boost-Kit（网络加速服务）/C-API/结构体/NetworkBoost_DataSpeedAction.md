---
title: "NetworkBoost_DataSpeedAction"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-data_speed_action"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Network Boost Kit（网络加速服务）"
  - "C API"
  - "结构体"
  - "NetworkBoost_DataSpeedAction"
captured_at: "2026-04-17T01:48:24.530Z"
---

# NetworkBoost\_DataSpeedAction

#### 概述

发包速率建议。

**起始版本：** 5.1.0(18)

**相关模块：** [NetworkBoost](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-overview)

**所在头文件：** [network\_boost\_quality.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-files-quality)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [NetworkBoost\_DataSpeedSimpleAction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-overview#networkboost_dataspeedsimpleaction-1) [dataSpeedSimpleAction](#dataspeedsimpleaction) | 应用发包策略的简单建议。 |
| uint64\_t [linkUpBandwidth](#linkupbandwidth) | 上行带宽。 |
| uint64\_t [linkDownBandwidth](#linkdownbandwidth) | 下行带宽。 |

#### 结构体成员变量说明

#### \[h2\]dataSpeedSimpleAction

```c
NetworkBoost_DataSpeedSimpleAction NetworkBoost_DataSpeedAction::dataSpeedSimpleAction
```

**描述**

应用发包策略的简单建议。

#### \[h2\]linkDownBandwidth

```c
uint64_t NetworkBoost_DataSpeedAction::linkDownBandwidth
```

**描述**

下行带宽。

#### \[h2\]linkUpBandwidth

```c
uint64_t NetworkBoost_DataSpeedAction::linkUpBandwidth
```

**描述**

上行带宽。

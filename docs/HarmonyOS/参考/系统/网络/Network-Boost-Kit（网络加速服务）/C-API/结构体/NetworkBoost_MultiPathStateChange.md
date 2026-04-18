---
title: "NetworkBoost_MultiPathStateChange"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-multipath_statechange"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Network Boost Kit（网络加速服务）"
  - "C API"
  - "结构体"
  - "NetworkBoost_MultiPathStateChange"
captured_at: "2026-04-17T01:48:25.189Z"
---

# NetworkBoost\_MultiPathStateChange

#### 概述

多网状态信息，用于注册多网状态变化事件回调后，系统多网状态发生变化的事件通知。

**起始版本：** 6.0.2(22)

**相关模块：** [NetworkBoost](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-overview)

**所在头文件：** [network\_boost\_handover.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-files-handover)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [NetworkBoost\_MultiPathState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-overview#networkboost_multipathstate) [multiPathState](#multipathstate) | 多网状态。 |
| [NetworkBoost\_MultiPathChangeCause](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-overview#networkboost_multipathchangecause) [changeCause](#changecause) | 多网状态变化原因。 |
| [NetworkBoost\_NetHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-overview#networkboost_nethandle) [netHandle](#nethandle) | 多网链路的netHandle。 |
| [NetworkBoost\_PathState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-overview#networkboost_pathstate) [pathState](#pathstate) | 多网链路状态。 |
| [NetworkBoost\_PathType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-overview#networkboost_pathtype) [pathType](#pathtype) | 多网链路类型。 |

#### 结构体成员变量说明

#### multiPathState

```c
NetworkBoost_MultiPathState NetworkBoost_MultiPathStateChange::multiPathState
```

**描述**

多网状态，可以通过该信息获取当前多网所处状态，包含空闲态、建立中、已建立和释放中四种状态。

#### changeCause

```c
NetworkBoost_MultiPathChangeCause NetworkBoost_MultiPathStateChange::changeCause
```

**描述**

多网状态变化原因，在多网状态发生变化时，通过该信息可以获取发生多网状态发生变化的原因。

#### netHandle

```c
NetworkBoost_NetHandle NetworkBoost_MultiPathStateChange::netHandle
```

**描述**

多网链路的netHandle。

#### pathState

```c
NetworkBoost_PathState NetworkBoost_MultiPathStateChange::pathState
```

**描述**

多网链路状态。

#### pathType

```c
NetworkBoost_PathType NetworkBoost_MultiPathStateChange::pathType
```

**描述**

多网链路类型。

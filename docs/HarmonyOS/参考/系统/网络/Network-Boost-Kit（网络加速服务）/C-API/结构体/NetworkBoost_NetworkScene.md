---
title: "NetworkBoost_NetworkScene"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-network_scene"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Network Boost Kit（网络加速服务）"
  - "C API"
  - "结构体"
  - "NetworkBoost_NetworkScene"
captured_at: "2026-04-17T01:48:24.776Z"
---

# NetworkBoost\_NetworkScene

#### 概述

网络场景状态变更回调信息。

**起始版本：** 5.1.0(18)

**相关模块：** [NetworkBoost](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-overview)

**所在头文件：** [network\_boost\_quality.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-files-quality)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [NetworkBoost\_PathType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-overview#networkboost_pathtype-1) [pathType](#pathtype) | 表明相应的数据路径上的网络场景信息。 |
| [NetworkBoost\_Scene](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-overview#networkboost_scene-1) [scene](#scene) | 网络场景类型。 |
| [NetworkBoost\_RecommendedAction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-overview#networkboost_recommendedaction-1) [recommendedAction](#recommendedaction) | 建议的数传策略。 |
| [NetworkBoost\_WeakSignalPrediction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-weak_signal_prediction) [weakSignalPrediction](#weaksignalprediction) | 弱信号预测相关信息。 |

#### 结构体成员变量说明

#### \[h2\]pathType

```c
NetworkBoost_PathType NetworkBoost_NetworkScene::pathType
```

**描述**

表明相应的数据路径上的网络场景信息。

#### \[h2\]recommendedAction

```c
NetworkBoost_RecommendedAction NetworkBoost_NetworkScene::recommendedAction
```

**描述**

建议的数传策略。

#### \[h2\]scene

```c
NetworkBoost_Scene NetworkBoost_NetworkScene::scene
```

**描述**

网络场景类型。

#### \[h2\]weakSignalPrediction

```c
NetworkBoost_WeakSignalPrediction NetworkBoost_NetworkScene::weakSignalPrediction
```

**描述**

弱信号预测相关信息。

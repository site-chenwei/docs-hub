---
title: "NetworkBoost_WeakSignalPrediction"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-weak_signal_prediction"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Network Boost Kit（网络加速服务）"
  - "C API"
  - "结构体"
  - "NetworkBoost_WeakSignalPrediction"
captured_at: "2026-04-17T01:48:24.923Z"
---

# NetworkBoost\_WeakSignalPrediction

#### 概述

弱信号预测相关信息。

**起始版本：** 5.1.0(18)

**相关模块：** [NetworkBoost](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-overview)

**所在头文件：** [network\_boost\_quality.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-files-quality)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| bool [isLastPredictionValid](#islastpredictionvalid) | 最近一次的弱信号预测是否有效，true表示最近一次的弱信号预测依旧有效，false表示最近一次的弱信号预测失效，此时startTime和duration参数忽略。 |
| uint32\_t [startTime](#starttime) | 预计多长时间进入弱信号（单位：s），取值范围为0和任意正数。 |
| uint32\_t [duration](#duration) | 预计在弱信号区域停留时长（单位：s），取任意正数。取值0，此次预测结果无效。 |

#### 结构体成员变量说明

#### \[h2\]duration

```c
uint32_t NetworkBoost_WeakSignalPrediction::duration
```

**描述**

预计在弱信号区域停留时长（单位：s），取任意正数。取值0，此次预测结果无效。

#### \[h2\]isLastPredictionValid

```c
bool NetworkBoost_WeakSignalPrediction::isLastPredictionValid
```

**描述**

最近一次的弱信号预测是否有效，true表示最近一次的弱信号预测依旧有效，false表示最近一次的弱信号预测失效，此时startTime和duration参数忽略。

#### \[h2\]startTime

```c
uint32_t NetworkBoost_WeakSignalPrediction::startTime
```

**描述**

预计多长时间进入弱信号（单位：s），取值范围为0和任意正数。

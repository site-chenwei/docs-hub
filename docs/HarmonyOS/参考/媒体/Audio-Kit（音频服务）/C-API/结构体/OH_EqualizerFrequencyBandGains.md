---
title: "OH_EqualizerFrequencyBandGains"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudiosuite-oh-equalizerfrequencybandgains"
menu_path:
  - "参考"
  - "媒体"
  - "Audio Kit（音频服务）"
  - "C API"
  - "结构体"
  - "OH_EqualizerFrequencyBandGains"
captured_at: "2026-04-17T01:48:36.782Z"
---

# OH\_EqualizerFrequencyBandGains

```c
typedef struct {...} OH_EqualizerFrequencyBandGains
```

#### 概述

定义音频编创均衡器效果节点配置参数。

**起始版本：** 22

**相关模块：** [OHAudioSuite](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudiosuite)

**所在头文件：** [native\_audio\_suite\_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-suite-base-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int32\_t gains\[EQUALIZER\_BAND\_NUM\] | 
均衡器频带增益配置，EQUALIZER\_BAND\_NUM为10，输入范围为\[-10, 10\]，单位为dB（分贝）。

频带：31Hz、62Hz、125Hz、250Hz、500Hz、1kHz、2kHz、4kHz、8kHz、16kHz。

**起始版本：** 22

 |

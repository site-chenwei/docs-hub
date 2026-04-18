---
title: "OH_LowPowerAudioSinkCallback"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-lowpoweraudiosink-oh-lowpoweraudiosinkcallback"
menu_path:
  - "参考"
  - "媒体"
  - "Media Kit（媒体服务）"
  - "C API"
  - "结构体"
  - "OH_LowPowerAudioSinkCallback"
captured_at: "2026-04-17T01:48:44.639Z"
---

# OH\_LowPowerAudioSinkCallback

```c
typedef struct OH_LowPowerAudioSinkCallback OH_LowPowerAudioSinkCallback
```

#### 概述

包含了LowPowerAudioSink回调函数指针的集合。

应用需注册此实例结构体到[OH\_LowPowerAudioSink](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-lowpoweraudiosink-oh-lowpoweraudiosink)实例中，并对回调上报的信息进行处理，保证LowPowerAudioSink的正常运行。

**起始版本：** 20

**相关模块：** [LowPowerAudioSink](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-lowpoweraudiosink)

**所在头文件：** [lowpower\_audio\_sink\_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-lowpower-audio-sink-base-h)

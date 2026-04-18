---
title: "OH_AudioBuffer"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-audiobuffer"
menu_path:
  - "参考"
  - "媒体"
  - "Media Kit（媒体服务）"
  - "C API"
  - "结构体"
  - "OH_AudioBuffer"
captured_at: "2026-04-17T01:48:44.536Z"
---

# OH\_AudioBuffer

```c
typedef struct OH_AudioBuffer {...} OH_AudioBuffer
```

#### 概述

定义了音频数据的大小、类型、时间戳等配置信息。

**起始版本：** 10

**相关模块：** [AVScreenCapture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture)

**所在头文件：** [native\_avscreen\_capture\_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avscreen-capture-base-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint8\_t\* buf | 音频buffer内存。 |
| int32\_t size | 音频buffer内存大小。 |
| int64\_t timestamp | 音频buffer时间戳。 |
| [OH\_AudioCaptureSourceType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avscreen-capture-base-h#oh_audiocapturesourcetype) type | 音频录制源类型。 |

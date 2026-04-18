---
title: "OH_AudioInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-audioinfo"
menu_path:
  - "参考"
  - "媒体"
  - "Media Kit（媒体服务）"
  - "C API"
  - "结构体"
  - "OH_AudioInfo"
captured_at: "2026-04-17T01:48:44.426Z"
---

# OH\_AudioInfo

```c
typedef struct OH_AudioInfo {...} OH_AudioInfo
```

#### 概述

音频信息。

同时采集音频麦克风和音频内录数据时，两路音频的audioSampleRate和audioChannels采样参数需要相同。

**起始版本：** 10

**相关模块：** [AVScreenCapture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture)

**所在头文件：** [native\_avscreen\_capture\_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avscreen-capture-base-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [OH\_AudioCaptureInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-audiocaptureinfo) micCapInfo | 音频麦克风采样信息。 |
| [OH\_AudioCaptureInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-audiocaptureinfo) innerCapInfo | 音频内录采样信息。 |
| [OH\_AudioEncInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-audioencinfo) audioEncInfo | 音频编码信息，原始码流时不需要设置。 |

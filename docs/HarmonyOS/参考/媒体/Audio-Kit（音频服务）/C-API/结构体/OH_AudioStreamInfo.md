---
title: "OH_AudioStreamInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio-oh-audiostreaminfo"
menu_path:
  - "参考"
  - "媒体"
  - "Audio Kit（音频服务）"
  - "C API"
  - "结构体"
  - "OH_AudioStreamInfo"
captured_at: "2026-04-17T01:48:36.668Z"
---

# OH\_AudioStreamInfo

```c
typedef struct OH_AudioStreamInfo {...} OH_AudioStreamInfo
```

#### 概述

定义音频流信息，用于描述基本音频格式。

**起始版本：** 19

**相关模块：** [OHAudio](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio)

**所在头文件：** [native\_audiostream\_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audiostream-base-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int32\_t samplingRate | 音频流采样率。 |
| [OH\_AudioChannelLayout](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-channel-layout-h#oh_audiochannellayout) channelLayout | 音频流声道布局。 |
| [OH\_AudioStream\_EncodingType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audiostream-base-h#oh_audiostream_encodingtype) encodingType | 音频流编码类型。 |
| [OH\_AudioStream\_SampleFormat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audiostream-base-h#oh_audiostream_sampleformat) sampleFormat | 音频流采样格式。 |

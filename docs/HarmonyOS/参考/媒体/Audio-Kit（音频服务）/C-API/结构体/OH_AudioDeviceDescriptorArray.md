---
title: "OH_AudioDeviceDescriptorArray"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio-oh-audiodevicedescriptorarray"
menu_path:
  - "参考"
  - "媒体"
  - "Audio Kit（音频服务）"
  - "C API"
  - "结构体"
  - "OH_AudioDeviceDescriptorArray"
captured_at: "2026-04-17T01:48:36.597Z"
---

# OH\_AudioDeviceDescriptorArray

```c
typedef struct OH_AudioDeviceDescriptorArray {...} OH_AudioDeviceDescriptorArray
```

#### 概述

声明音频设备描述符数组。

**起始版本：** 12

**相关模块：** [OHAudio](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio)

**所在头文件：** [native\_audio\_device\_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-device-base-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t size | 音频设备描述符数组大小。 |
| [OH\_AudioDeviceDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio-oh-audiodevicedescriptor)\*\* descriptors | 音频设备描述符数组。 |

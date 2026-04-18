---
title: "OH_AudioDataArray"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudiosuite-oh-audiodataarray"
menu_path:
  - "参考"
  - "媒体"
  - "Audio Kit（音频服务）"
  - "C API"
  - "结构体"
  - "OH_AudioDataArray"
captured_at: "2026-04-17T01:48:36.768Z"
---

# OH\_AudioDataArray

```c
typedef struct {...} OH_AudioDataArray
```

#### 概述

定义多路输出渲染接口的输入数据描述。当管线中存在多输出效果节点时，通过多输出渲染接口获取处理过后的音频数据。

**起始版本：** 22

**相关模块：** [OHAudioSuite](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudiosuite)

**所在头文件：** [native\_audio\_suite\_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-suite-base-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| void \*\*audioDataArray | 需要输出的音频数据地址。 |
| int32\_t arraySize | 音频数组大小。 |
| int32\_t requestFrameSize | audioDataArray数组中地址的内存大小（单位为字节），应确保每个地址均具有requestFrameSize字节个大小。 |

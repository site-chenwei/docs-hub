---
title: "OH_AVCodecBufferAttr"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-core-oh-avcodecbufferattr"
menu_path:
  - "参考"
  - "媒体"
  - "AVCodec Kit（音视频编解码服务）"
  - "C API"
  - "结构体"
  - "OH_AVCodecBufferAttr"
captured_at: "2026-04-17T01:48:37.529Z"
---

# OH\_AVCodecBufferAttr

```c
typedef struct OH_AVCodecBufferAttr {...} OH_AVCodecBufferAttr
```

#### 概述

定义OH\_AVCodec的缓冲区描述信息。

**起始版本：** 9

**相关模块：** [Core](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-core)

**所在头文件：** [native\_avbuffer\_info.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avbuffer-info-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int64\_t pts | 此缓冲区的显示时间戳（以微秒为单位）。 |
| int32\_t size | 缓冲区中包含的数据的大小（以字节为单位）。 |
| int32\_t offset | 此缓冲区中有效数据的起始偏移量。 |
| uint32\_t flags | 此缓冲区具有的标志，请参阅[OH\_AVCodecBufferFlags](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avbuffer-info-h#oh_avcodecbufferflags)。 |

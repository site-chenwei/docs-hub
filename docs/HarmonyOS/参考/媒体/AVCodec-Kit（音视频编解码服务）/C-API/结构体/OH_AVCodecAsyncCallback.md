---
title: "OH_AVCodecAsyncCallback"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-codecbase-oh-avcodecasynccallback"
menu_path:
  - "参考"
  - "媒体"
  - "AVCodec Kit（音视频编解码服务）"
  - "C API"
  - "结构体"
  - "OH_AVCodecAsyncCallback"
captured_at: "2026-04-17T01:48:37.425Z"
---

# OH\_AVCodecAsyncCallback

```c
typedef struct OH_AVCodecAsyncCallback {...} OH_AVCodecAsyncCallback
```

#### 概述

OH\_AVCodec中所有异步回调函数指针的集合。将该结构体的实例注册到OH\_AVCodec实例中，并处理回调上报的信息，以保证OH\_AVCodec的正常运行。

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [OH\_AVCodecCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-codecbase-oh-avcodeccallback)

**相关模块：** [CodecBase](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-codecbase)

**所在头文件：** [native\_avcodec\_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avcodec-base-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [OH\_AVCodecOnError](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avcodec-base-h#oh_avcodeconerror) onError | 监控编解码器操作错误。 |
| [OH\_AVCodecOnStreamChanged](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avcodec-base-h#oh_avcodeconstreamchanged) onStreamChanged | 监控编解码器流变化。 |
| [OH\_AVCodecOnNeedInputData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avcodec-base-h#oh_avcodeconneedinputdata) onNeedInputData | 监控编解码器需要输入数据。 |
| [OH\_AVCodecOnNewOutputData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avcodec-base-h#oh_avcodeconnewoutputdata) onNeedOutputData | 监控编解码器已生成输出数据。 |

---
title: "OH_AVMetadataExtractor_FrameInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/metadataextractor-oh-avmetadataextractor-frameinfo"
menu_path:
  - "参考"
  - "媒体"
  - "Media Kit（媒体服务）"
  - "C API"
  - "结构体"
  - "OH_AVMetadataExtractor_FrameInfo"
captured_at: "2026-04-17T01:48:44.891Z"
---

# OH\_AVMetadataExtractor\_FrameInfo

```c
typedef struct {...} OH_AVMetadataExtractor_FrameInfo
```

#### 概述

定义从视频中提取出的帧的信息。

**起始版本：** 23

**相关模块：** [AVMetadataExtractor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avmetadataextractor)

**所在头文件：** [avmetadata\_extractor\_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avmetadata-extractor-base-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int64\_t requestTimeUs | 用户传入的请求时间。 |
| int64\_t actualTimeUs | 实际提取到的帧的时间；若提取失败，则为-1。 |
| [OH\_PixelmapNative\*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-pixelmapnative) image | 从视频中提取出的帧图像；若提取失败，则为空指针。 |
| [OH\_AVMetadataExtractor\_FetchState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avmetadata-extractor-base-h#oh_avmetadataextractor_fetchstate) result | 本次帧提取操作的结果状态。 |

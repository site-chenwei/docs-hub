---
title: "VideoProcessing_ColorSpaceInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-videoprocessing-videoprocessing-colorspaceinfo"
menu_path:
  - "参考"
  - "媒体"
  - "Media Kit（媒体服务）"
  - "C API"
  - "结构体"
  - "VideoProcessing_ColorSpaceInfo"
captured_at: "2026-04-17T01:48:44.740Z"
---

# VideoProcessing\_ColorSpaceInfo

```c
typedef struct VideoProcessing_ColorSpaceInfo {...} VideoProcessing_ColorSpaceInfo
```

#### 概述

视频颜色空间信息数据结构。

**参考：** [OH\_VideoProcessing\_IsColorSpaceConversionSupported](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-video-processing-h#oh_videoprocessing_iscolorspaceconversionsupported)

**起始版本：** 12

**相关模块：** [VideoProcessing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-videoprocessing)

**所在头文件：** [video\_processing\_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-video-processing-types-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int32\_t metadataType | 视频元数据类型，参考[OH\_NativeBuffer\_MetadataType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-buffer-common-h#oh_nativebuffer_metadatatype)。 |
| int32\_t colorSpace | 视频颜色空间类型，参考[OH\_NativeBuffer\_ColorSpace](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-buffer-common-h#oh_nativebuffer_colorspace)。 |
| int32\_t pixelFormat | 视频像素格式，参考[OH\_NativeBuffer\_Format](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-buffer-common-h#oh_nativebuffer_format)。 |

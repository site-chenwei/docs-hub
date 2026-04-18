---
title: "ImageProcessing_ColorSpaceInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-imageprocessing-imageprocessing-colorspaceinfo"
menu_path:
  - "参考"
  - "媒体"
  - "Image Kit（图片处理服务）"
  - "C API"
  - "结构体"
  - "ImageProcessing_ColorSpaceInfo"
captured_at: "2026-04-17T01:48:42.859Z"
---

# ImageProcessing\_ColorSpaceInfo

```c
typedef struct ImageProcessing_ColorSpaceInfo {...} ImageProcessing_ColorSpaceInfo
```

#### 概述

色彩空间信息，用于色彩空间转换能力查询。

**参考：**

[OH\_ImageProcessing\_IsColorSpaceConversionSupported](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-processing-h#oh_imageprocessing_iscolorspaceconversionsupported), [OH\_ImageProcessing\_IsCompositionSupported](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-processing-h#oh_imageprocessing_iscompositionsupported), [OH\_ImageProcessing\_IsDecompositionSupported](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-processing-h#oh_imageprocessing_isdecompositionsupported)

**起始版本：** 13

**相关模块：** [ImageProcessing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-imageprocessing)

**所在头文件：** [image\_processing\_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-processing-types-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int32\_t metadataType | 定义元数据类型，参考[OH\_Pixelmap\_HdrMetadataKey](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pixelmap-native-h#oh_pixelmap_hdrmetadatakey)。 |
| int32\_t colorSpace | 定义色彩空间，参考[ColorSpaceName](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-color-space-manager-h#colorspacename)。 |
| int32\_t pixelFormat | 定义像素格式，参考[PIXEL\_FORMAT](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pixelmap-native-h#pixel_format)。 |

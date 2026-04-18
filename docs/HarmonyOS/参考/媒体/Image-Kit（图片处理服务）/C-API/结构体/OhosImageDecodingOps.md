---
title: "OhosImageDecodingOps"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagedecodingops"
menu_path:
  - "参考"
  - "媒体"
  - "Image Kit（图片处理服务）"
  - "C API"
  - "结构体"
  - "OhosImageDecodingOps"
captured_at: "2026-04-17T01:48:42.643Z"
---

# OhosImageDecodingOps

```c
struct OhosImageDecodingOps {...}
```

#### 概述

定义图像源解码选项。此选项给[OH\_ImageSource\_CreatePixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-mdk-h#oh_imagesource_createpixelmap)和[OH\_ImageSource\_CreatePixelMapList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-mdk-h#oh_imagesource_createpixelmaplist)接口使用。

**起始版本：** 10

**相关模块：** [Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image)

**所在头文件：** [image\_source\_mdk.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-mdk-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int8\_t editable | 定义输出的像素位图是否可编辑。 |
| int32\_t pixelFormat | 定义输出的像素格式。 |
| int32\_t fitDensity | 定义解码目标的像素密度。 |
| uint32\_t index | 定义ImageSource解码索引。 |
| uint32\_t sampleSize | 定义解码样本大小选项。 |
| uint32\_t rotate | 定义解码旋转选项。 |
| struct [OhosImageSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagesize) size | 定义解码目标像素宽高的大小。 |
| struct [OhosImageRegion](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimageregion) region | 定义ImageSource解码的像素范围。 |

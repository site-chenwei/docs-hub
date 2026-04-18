---
title: "OhosImageComponent"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagecomponent"
menu_path:
  - "参考"
  - "媒体"
  - "Image Kit（图片处理服务）"
  - "C API"
  - "结构体"
  - "OhosImageComponent"
captured_at: "2026-04-17T01:48:42.427Z"
---

# OhosImageComponent

```c
struct OhosImageComponent {...}
```

#### 概述

定义图像组成信息。

**起始版本：** 10

**相关模块：** [Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image)

**所在头文件：** [image\_mdk.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-mdk-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint8\_t\* byteBuffer | 像素数据地址。 |
| size\_t size | 内存中的像素数据大小。 |
| int32\_t componentType | 
像素数据类型。

1：OHOS\_IMAGE\_COMPONENT\_FORMAT\_YUV\_Y 亮度信息。

2：OHOS\_IMAGE\_COMPONENT\_FORMAT\_YUV\_U 色度信息。

3：OHOS\_IMAGE\_COMPONENT\_FORMAT\_YUV\_V 色差值信息。

4：OHOS\_IMAGE\_COMPONENT\_FORMAT\_JPEG JPEG格式。

 |
| int32\_t rowStride | 像素数据行宽。读取相机预览流数据时，需要考虑按stride进行读取，具体用法见[C/C++预览流二次处理示例](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-preview-imagereceiver)。 |
| int32\_t pixelStride | 像素数据的像素大小。 |

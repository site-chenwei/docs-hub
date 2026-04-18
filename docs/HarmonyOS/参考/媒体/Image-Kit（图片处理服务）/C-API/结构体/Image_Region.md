---
title: "Image_Region"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-image-region"
menu_path:
  - "参考"
  - "媒体"
  - "Image Kit（图片处理服务）"
  - "C API"
  - "结构体"
  - "Image_Region"
captured_at: "2026-04-17T01:48:42.140Z"
---

# Image\_Region

```c
struct Image_Region {...}
```

#### 概述

待解码的图像源区域结构体。

**起始版本：** 12

**相关模块：** [Image\_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule)

**所在头文件：** [image\_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-common-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t x | 区域横坐标，不能大于原图的宽度。 |
| uint32\_t y | 区域纵坐标，不能大于原图的高度。 |
| uint32\_t width | 输出图片的宽，单位：像素。 |
| uint32\_t height | 输出图片的高，单位：像素。 |

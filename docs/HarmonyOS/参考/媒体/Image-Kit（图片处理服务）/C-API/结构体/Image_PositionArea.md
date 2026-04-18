---
title: "Image_PositionArea"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-image-positionarea"
menu_path:
  - "参考"
  - "媒体"
  - "Image Kit（图片处理服务）"
  - "C API"
  - "结构体"
  - "Image_PositionArea"
captured_at: "2026-04-17T01:48:42.932Z"
---

# Image\_PositionArea

```c
typedef struct Image_PositionArea {...} Image_PositionArea
```

#### 概述

要读取或写入的图像像素区域。

**起始版本：** 22

**相关模块：** [Image\_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule)

**所在头文件：** [image\_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-common-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint8\_t \*pixels | 读取或写入的图像像素数据。仅支持BRGA\_8888格式的数据。 |
| size\_t pixelsSize | 图像像素数据的长度（单位：字节）。 |
| uint32\_t offset | 数据读取或写入的偏移量（单位：字节）。 |
| uint32\_t stride | 区域的跨距，即区域中每行像素所占的空间（单位：字节）。stride >= region.size.width \* 4。 |
| [Image\_Region](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-image-region) region | 读取或写入的区域。区域宽度加X坐标不能大于原图的宽度，区域高度加Y坐标不能大于原图的高度。 |

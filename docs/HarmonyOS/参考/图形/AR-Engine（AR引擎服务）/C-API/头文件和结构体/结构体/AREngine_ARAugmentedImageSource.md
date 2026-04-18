---
title: "AREngine_ARAugmentedImageSource"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-struct-araugmentedimagesource"
menu_path:
  - "参考"
  - "图形"
  - "AR Engine（AR引擎服务）"
  - "C API"
  - "头文件和结构体"
  - "结构体"
  - "AREngine_ARAugmentedImageSource"
captured_at: "2026-04-17T01:48:46.195Z"
---

# AREngine\_ARAugmentedImageSource

#### 概述

图像数据。

**起始版本：** 5.1.0(18)

**相关模块：** [AR Engine](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine)

**所在头文件：** [ar\_engine\_core.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-header-file)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| const char \*[imageName](#imagename) | 图像名，不允许为空，255个字符以内，超过255个的字符将会被丢弃。 |
| const uint8\_t \*[imageData](#imagedata) | 灰度图像元素数组地址。 |
| int32\_t [pixelWidth](#pixelwidth) | 图像像素宽度。 |
| int32\_t [pixelHeight](#pixelheight) | 图像像素高度。 |
| int32\_t [stride](#stride) | 图像步幅。 |
| float [realWidthInMeters](#realwidthinmeters) | 图像中对象的实际物理宽度。无限制，默认值为A4纸张尺寸。 |

#### 结构体成员变量说明

#### \[h2\]imageName

```cpp
const char* AREngine_ARAugmentedImageSource::imageName
```

**描述**

图像名，不允许为空，255个字符以内，超过255个的字符将会被丢弃。

#### \[h2\]imageData

```cpp
const uint8_t* AREngine_ARAugmentedImageSource::imageData
```

**描述**

灰度图像元素数组地址。

#### \[h2\]pixelWidth

```cpp
int32_t AREngine_ARAugmentedImageSource::pixelWidth
```

**描述**

图像像素宽度。

#### \[h2\]pixelHeight

```cpp
int32_t AREngine_ARAugmentedImageSource::pixelHeight
```

**描述**

图像像素高度。

#### \[h2\]stride

```cpp
int32_t AREngine_ARAugmentedImageSource::stride
```

**描述**

图像步幅。

#### \[h2\]realWidthInMeters

```cpp
float AREngine_ARAugmentedImageSource::realWidthInMeters
```

**描述**

图像中对象的实际物理宽度。无限制，默认值为A4纸张尺寸。

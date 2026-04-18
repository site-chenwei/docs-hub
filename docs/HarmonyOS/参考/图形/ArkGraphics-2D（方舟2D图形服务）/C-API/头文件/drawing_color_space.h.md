---
title: "drawing_color_space.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-color-space-h"
menu_path:
  - "参考"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "C API"
  - "头文件"
  - "drawing_color_space.h"
captured_at: "2026-04-17T01:48:47.539Z"
---

# drawing\_color\_space.h

#### 概述

文件中定义了与颜色空间相关的功能函数。

**引用文件：** <native\_drawing/drawing\_color\_space.h>

**库：** libnative\_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**相关模块：** [Drawing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing)

#### 汇总

#### \[h2\]函数

| 名称 | 描述 |
| :-- | :-- |
| [OH\_Drawing\_ColorSpace\* OH\_Drawing\_ColorSpaceCreateSrgb(void)](#oh_drawing_colorspacecreatesrgb) | 创建一个标准颜色空间。 |
| [OH\_Drawing\_ColorSpace\* OH\_Drawing\_ColorSpaceCreateSrgbLinear(void)](#oh_drawing_colorspacecreatesrgblinear) | 创建一个Gamma 1.0空间上的颜色空间。 |
| [void OH\_Drawing\_ColorSpaceDestroy(OH\_Drawing\_ColorSpace\* colorSpace)](#oh_drawing_colorspacedestroy) | 销毁颜色空间对象，并回收该对象占用内存。 |

#### 函数说明

#### \[h2\]OH\_Drawing\_ColorSpaceCreateSrgb()

```c
OH_Drawing_ColorSpace* OH_Drawing_ColorSpaceCreateSrgb(void)
```

**描述**

创建一个标准颜色空间。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [OH\_Drawing\_ColorSpace](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-colorspace)\* | 函数返回一个指针，指针指向创建的颜色空间对象[OH\_Drawing\_ColorSpace](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-colorspace)。 |

#### \[h2\]OH\_Drawing\_ColorSpaceCreateSrgbLinear()

```c
OH_Drawing_ColorSpace* OH_Drawing_ColorSpaceCreateSrgbLinear(void)
```

**描述**

创建一个Gamma 1.0空间上的颜色空间。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [OH\_Drawing\_ColorSpace](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-colorspace)\* | 函数返回一个指针，指针指向创建的颜色空间对象[OH\_Drawing\_ColorSpace](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-colorspace)。 |

#### \[h2\]OH\_Drawing\_ColorSpaceDestroy()

```c
void OH_Drawing_ColorSpaceDestroy(OH_Drawing_ColorSpace* colorSpace)
```

**描述**

销毁颜色空间对象，并回收该对象占用的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_Drawing\_ColorSpace](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-colorspace)\* colorSpace | 指向颜色空间对象[OH\_Drawing\_ColorSpace](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-colorspace)的指针。 |

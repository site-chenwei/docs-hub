---
title: "drawing_point.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-point-h"
menu_path:
  - "参考"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "C API"
  - "头文件"
  - "drawing_point.h"
captured_at: "2026-04-17T01:48:48.777Z"
---

# drawing\_point.h

#### 概述

文件中定义了与坐标点相关的功能函数。

**引用文件：** <native\_drawing/drawing\_point.h>

**库：** libnative\_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**相关模块：** [Drawing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing)

#### 汇总

#### \[h2\]函数

| 名称 | 描述 |
| :-- | :-- |
| [OH\_Drawing\_Point\* OH\_Drawing\_PointCreate(float x, float y)](#oh_drawing_pointcreate) | 用于创建一个坐标点对象。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PointGetX(const OH\_Drawing\_Point\* point, float\* x)](#oh_drawing_pointgetx) | 用于获取点的x轴坐标。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PointGetY(const OH\_Drawing\_Point\* point, float\* y)](#oh_drawing_pointgety) | 用于获取点的y轴坐标。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_PointSet(OH\_Drawing\_Point\* point, float x, float y)](#oh_drawing_pointset) | 用于设置点的x轴和y轴坐标。 |
| [void OH\_Drawing\_PointDestroy(OH\_Drawing\_Point\* point)](#oh_drawing_pointdestroy) | 用于销毁坐标点对象并回收该对象占有的内存。 |

#### 函数说明

#### \[h2\]OH\_Drawing\_PointCreate()

```c
OH_Drawing_Point* OH_Drawing_PointCreate(float x, float y)
```

**描述**

用于创建一个坐标点对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| float x | X轴坐标。 |
| float y | Y轴坐标。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [OH\_Drawing\_Point](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-point)\* | 函数会返回一个指针，指针指向创建的坐标点对象。 |

#### \[h2\]OH\_Drawing\_PointGetX()

```c
OH_Drawing_ErrorCode OH_Drawing_PointGetX(const OH_Drawing_Point* point, float* x)
```

**描述**

用于获取点的x轴坐标。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const [OH\_Drawing\_Point](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-point)\* point | 指向坐标点对象[OH\_Drawing\_Point](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-point)的指针。 |
| float\* x | 表示点的x轴坐标。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-error-code-h#oh_drawing_errorcode) | 
函数返回执行错误码。

返回OH\_DRAWING\_SUCCESS，表示执行成功。

返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数point或者x为空。

 |

#### \[h2\]OH\_Drawing\_PointGetY()

```c
OH_Drawing_ErrorCode OH_Drawing_PointGetY(const OH_Drawing_Point* point, float* y)
```

**描述**

用于获取点的y轴坐标。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const [OH\_Drawing\_Point](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-point)\* point | 指向坐标点对象[OH\_Drawing\_Point](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-point)的指针。 |
| float\* y | 表示点的y轴坐标。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-error-code-h#oh_drawing_errorcode) | 
函数返回执行错误码。

返回OH\_DRAWING\_SUCCESS，表示执行成功。

返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数point或者y为空。

 |

#### \[h2\]OH\_Drawing\_PointSet()

```c
OH_Drawing_ErrorCode OH_Drawing_PointSet(OH_Drawing_Point* point, float x, float y)
```

**描述**

用于设置点的x轴和y轴坐标。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_Drawing\_Point](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-point)\* point | 指向坐标点对象[OH\_Drawing\_Point](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-point)的指针。 |
| float x | 表示点的x轴坐标。 |
| float y | 表示点的y轴坐标。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-error-code-h#oh_drawing_errorcode) | 
函数返回执行错误码。

返回OH\_DRAWING\_SUCCESS，表示执行成功。

返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数point为空。

 |

#### \[h2\]OH\_Drawing\_PointDestroy()

```c
void OH_Drawing_PointDestroy(OH_Drawing_Point* point)
```

**描述**

用于销毁坐标点对象并回收该对象占有的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_Drawing\_Point](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-point)\* point | 指向坐标点对象的指针。 |

---
title: "drawing_surface.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-surface-h"
menu_path:
  - "参考"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "C API"
  - "头文件"
  - "drawing_surface.h"
captured_at: "2026-04-17T01:48:49.305Z"
---

# drawing\_surface.h

#### 概述

文件中定义与surface相关的功能函数，包括surface的创建、销毁和使用等。

**引用文件：** <native\_drawing/drawing\_surface.h>

**库：** libnative\_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**相关模块：** [Drawing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing)

#### 汇总

#### \[h2\]函数

| 名称 | 描述 |
| :-- | :-- |
| [OH\_Drawing\_Surface\* OH\_Drawing\_SurfaceCreateFromGpuContext(OH\_Drawing\_GpuContext\* gpuContext, bool flag, OH\_Drawing\_Image\_Info imageInfo)](#oh_drawing_surfacecreatefromgpucontext) | 
使用图形处理器上下文创建一个surface对象，用于管理画布绘制的内容。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-error-code-h#oh_drawing_errorcodeget)查看错误码的取值。

gpuContext为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

 |
| [OH\_Drawing\_Surface\* OH\_Drawing\_SurfaceCreateOnScreen(OH\_Drawing\_GpuContext\* gpuContext, OH\_Drawing\_Image\_Info imageInfo, void\* window)](#oh_drawing_surfacecreateonscreen) | 

使用图形处理器上下文创建一个与屏幕窗口绑定的surface对象，用于管理画布绘制的内容。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-error-code-h#oh_drawing_errorcodeget)查看错误码的取值。

gpuContext或window为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

 |
| [OH\_Drawing\_Canvas\* OH\_Drawing\_SurfaceGetCanvas(OH\_Drawing\_Surface\* surface)](#oh_drawing_surfacegetcanvas) | 

通过surface对象获取画布对象。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-error-code-h#oh_drawing_errorcodeget)查看错误码的取值。

surface为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_SurfaceFlush(OH\_Drawing\_Surface\* surface)](#oh_drawing_surfaceflush) | 将surface对象上的画布绘制内容提交给GPU处理，完成绘制内容上屏显示。 |
| [void OH\_Drawing\_SurfaceDestroy(OH\_Drawing\_Surface\* surface)](#oh_drawing_surfacedestroy) | 销毁surface对象并回收该对象占用的内存。 |

#### 函数说明

#### \[h2\]OH\_Drawing\_SurfaceCreateFromGpuContext()

```c
OH_Drawing_Surface* OH_Drawing_SurfaceCreateFromGpuContext(OH_Drawing_GpuContext* gpuContext, bool flag, OH_Drawing_Image_Info imageInfo)
```

**描述**

使用图形处理器上下文创建一个surface对象，用于管理画布绘制的内容。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-error-code-h#oh_drawing_errorcodeget)查看错误码的取值。

gpuContext为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_Drawing\_GpuContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-gpucontext)\* gpuContext | 指向图形处理器上下文对象的指针[OH\_Drawing\_GpuContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-gpucontext)。 |
| bool flag | 用于控制内存分配是否计入缓存预算。true则计入高速缓存预算，false则不计入高速缓存预算。 |
| [OH\_Drawing\_Image\_Info](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-image-info) imageInfo | 图片信息[OH\_Drawing\_Image\_Info](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-image-info)结构体。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [OH\_Drawing\_Surface](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-surface)\* | 返回一个指针，指针指向创建的surface对象[OH\_Drawing\_Surface](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-surface)。 |

#### \[h2\]OH\_Drawing\_SurfaceCreateOnScreen()

```c
OH_Drawing_Surface* OH_Drawing_SurfaceCreateOnScreen(OH_Drawing_GpuContext* gpuContext, OH_Drawing_Image_Info imageInfo, void* window)
```

**描述**

使用图形处理器上下文创建一个与屏幕窗口绑定的surface对象，用于管理画布绘制的内容。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-error-code-h#oh_drawing_errorcodeget)查看错误码的取值。

gpuContext或window为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

imageInfo的宽高和window的宽高需保持一致。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 16

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_Drawing\_GpuContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-gpucontext)\* gpuContext | 
指向图形处理器上下文对象的指针[OH\_Drawing\_GpuContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-gpucontext)。

该图形处理器上下文对象必须由[OH\_Drawing\_GpuContextCreate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-gpu-context-h#oh_drawing_gpucontextcreate)创建，否则surface对象会创建失败。

 |
| [OH\_Drawing\_Image\_Info](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-image-info) imageInfo | 图片信息[OH\_Drawing\_Image\_Info](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-image-info)结构体。 |
| void\* window | 指向屏幕窗口对象的指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [OH\_Drawing\_Surface](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-surface)\* | 返回一个指针，指针指向创建的surface对象[OH\_Drawing\_Surface](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-surface)。 |

#### \[h2\]OH\_Drawing\_SurfaceGetCanvas()

```c
OH_Drawing_Canvas* OH_Drawing_SurfaceGetCanvas(OH_Drawing_Surface* surface)
```

**描述**

通过surface对象获取画布对象。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-error-code-h#oh_drawing_errorcodeget)查看错误码的取值。

surface为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_Drawing\_Surface](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-surface)\* surface | 指向创建的surface对象的指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [OH\_Drawing\_Canvas](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-canvas)\* | 返回一个指针，指针指向创建的画布对象[OH\_Drawing\_Canvas](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-canvas)。返回的指针不需要由调用者管理。 |

#### \[h2\]OH\_Drawing\_SurfaceFlush()

```c
OH_Drawing_ErrorCode OH_Drawing_SurfaceFlush(OH_Drawing_Surface* surface)
```

**描述**

将surface对象上的画布绘制内容提交给GPU处理，完成绘制内容上屏显示。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 16

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_Drawing\_Surface](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-surface)\* surface | 指向创建的surface对象的指针[OH\_Drawing\_Surface](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-surface)。该surface对象必须由[OH\_Drawing\_SurfaceCreateOnScreen](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-surface-h#oh_drawing_surfacecreateonscreen)创建，否则该接口调用将没有任何效果。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [OH\_Drawing\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-error-code-h#oh_drawing_errorcode) | 
函数返回执行错误码。

返回OH\_DRAWING\_SUCCESS，表示执行成功。

返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数surface为空。

 |

#### \[h2\]OH\_Drawing\_SurfaceDestroy()

```c
void OH_Drawing_SurfaceDestroy(OH_Drawing_Surface* surface)
```

**描述**

销毁surface对象并回收该对象占用的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_Drawing\_Surface](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-surface)\* surface | 指向创建的surface对象的指针。 |

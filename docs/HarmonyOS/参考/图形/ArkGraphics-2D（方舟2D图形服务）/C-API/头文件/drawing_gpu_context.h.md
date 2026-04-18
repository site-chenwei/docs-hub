---
title: "drawing_gpu_context.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-gpu-context-h"
menu_path:
  - "参考"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "C API"
  - "头文件"
  - "drawing_gpu_context.h"
captured_at: "2026-04-17T01:48:47.960Z"
---

# drawing\_gpu\_context.h

#### 概述

声明与绘图模块中的图形处理器上下文对象相关的函数。

**引用文件：** <native\_drawing/drawing\_gpu\_context.h>

**库：** libnative\_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**相关模块：** [Drawing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing)

#### 汇总

#### \[h2\]结构体

| 名称 | typedef关键字 | 描述 |
| :-- | :-- | :-- |
| [OH\_Drawing\_GpuContextOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-gpucontextoptions) | OH\_Drawing\_GpuContextOptions | 定义有关图形处理器上下文的选项。 |

#### \[h2\]函数

| 名称 | 描述 |
| :-- | :-- |
| [OH\_Drawing\_GpuContext\* OH\_Drawing\_GpuContextCreateFromGL(OH\_Drawing\_GpuContextOptions gpuContextOptions)](#oh_drawing_gpucontextcreatefromgl) | 用于创建一个使用OpenGL作为后端接口的图形处理器上下文对象。 |
| [OH\_Drawing\_GpuContext\* OH\_Drawing\_GpuContextCreate(void)](#oh_drawing_gpucontextcreate) | 用于创建一个图形处理器上下文对象, 使用的后端类型取决于运行设备。 |
| [void OH\_Drawing\_GpuContextDestroy(OH\_Drawing\_GpuContext\* gpuContext)](#oh_drawing_gpucontextdestroy) | 用于销毁图形处理器上下文对象并回收该对象占用的内存。 |

#### 函数说明

#### \[h2\]OH\_Drawing\_GpuContextCreateFromGL()

```c
OH_Drawing_GpuContext* OH_Drawing_GpuContextCreateFromGL(OH_Drawing_GpuContextOptions gpuContextOptions)
```

**描述**

用于创建一个使用OpenGL作为后端接口的图形处理器上下文对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**废弃版本：** 18

**替代接口：** OH\_Drawing\_GpuContextCreate

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_Drawing\_GpuContextOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-gpucontextoptions) gpuContextOptions | 图形处理器上下文选项[OH\_Drawing\_GpuContextOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-gpucontextoptions)。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [OH\_Drawing\_GpuContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-gpucontext)\* | 返回一个指针，指针指向创建的图形处理器上下文对象[OH\_Drawing\_GpuContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-gpucontext)。 |

#### \[h2\]OH\_Drawing\_GpuContextCreate()

```c
OH_Drawing_GpuContext* OH_Drawing_GpuContextCreate(void)
```

**描述**

用于创建一个图形处理器上下文对象, 使用的后端类型取决于运行设备。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 16

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [OH\_Drawing\_GpuContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-gpucontext)\* | 返回一个指针，指针指向创建的图形处理器上下文对象[OH\_Drawing\_GpuContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-gpucontext)。 |

#### \[h2\]OH\_Drawing\_GpuContextDestroy()

```c
void OH_Drawing_GpuContextDestroy(OH_Drawing_GpuContext* gpuContext)
```

**描述**

用于销毁图形处理器上下文对象并回收该对象占用的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_Drawing\_GpuContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-gpucontext)\* gpuContext | 指向图形处理器上下文对象的指针[OH\_Drawing\_GpuContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-gpucontext)。 |

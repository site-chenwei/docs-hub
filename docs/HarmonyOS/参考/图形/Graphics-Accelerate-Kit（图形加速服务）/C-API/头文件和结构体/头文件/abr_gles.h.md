---
title: "abr_gles.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/abr__gles_8h"
menu_path:
  - "参考"
  - "图形"
  - "Graphics Accelerate Kit（图形加速服务）"
  - "C API"
  - "头文件和结构体"
  - "头文件"
  - "abr_gles.h"
captured_at: "2026-04-17T01:48:51.615Z"
---

# abr\_gles.h

#### 概述

声明OpenGL ES图形API平台的ABR接口。

**引用文件：** <graphics\_game\_sdk/abr\_gles.h>

**库：** libabr.so

**系统能力：** SystemCapability.GraphicsGame.RenderAccelerate

**起始版本：** 5.0.0(12)

**相关模块：** [GraphicsAccelerate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate)

#### 汇总

#### \[h2\]函数

| 名称 | 描述 |
| :-- | :-- |
| [ABR\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#abr_errorcode-1) [HMS\_ABR\_MarkFrameBuffer\_GLES](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#hms_abr_markframebuffer_gles)([ABR\_Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#abr_context)\* context) | 标记ABR进行自适应渲染处理的GLES Buffer，需要在GLES Buffer开始渲染前调用此接口。 |
| [ABR\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#abr_errorcode-1) [HMS\_ABR\_GetScaledTexture\_GLES](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#hms_abr_getscaledtexture_gles)([ABR\_Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#abr_context)\* context, uint32\_t originTexture, uint32\_t\* scaledTexture) | 根据原始GLES纹理获取ABR渲染后的GLES纹理。 |

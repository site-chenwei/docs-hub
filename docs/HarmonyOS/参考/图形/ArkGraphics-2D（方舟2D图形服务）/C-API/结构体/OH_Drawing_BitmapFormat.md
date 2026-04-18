---
title: "OH_Drawing_BitmapFormat"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-bitmapformat"
menu_path:
  - "参考"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "C API"
  - "结构体"
  - "OH_Drawing_BitmapFormat"
captured_at: "2026-04-17T01:48:49.904Z"
---

# OH\_Drawing\_BitmapFormat

```c
typedef struct {...} OH_Drawing_BitmapFormat
```

#### 概述

结构体用于描述位图像素的格式，包括颜色类型和透明度类型。

**起始版本：** 8

**相关模块：** [Drawing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing)

**所在头文件：** [drawing\_bitmap.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-bitmap-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| OH\_Drawing\_ColorFormat colorFormat | 描述位图像素的存储格式。 |
| OH\_Drawing\_AlphaFormat alphaFormat | 描述位图像素的透明度分量。 |

---
title: "OH_Drawing_Image_Info"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-image-info"
menu_path:
  - "参考"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "C API"
  - "结构体"
  - "OH_Drawing_Image_Info"
captured_at: "2026-04-17T01:48:50.247Z"
---

# OH\_Drawing\_Image\_Info

```c
typedef struct {...} OH_Drawing_Image_Info
```

#### 概述

定义图片信息结构体。

**起始版本：** 12

**相关模块：** [Drawing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing)

**所在头文件：** [drawing\_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-types-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int32\_t width | 宽度，单位为像素。 |
| int32\_t height | 高度，单位为像素。 |
| [OH\_Drawing\_ColorFormat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-types-h#oh_drawing_colorformat) colorType | 颜色类型[OH\_Drawing\_ColorFormat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-types-h#oh_drawing_colorformat)。 |
| [OH\_Drawing\_AlphaFormat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-types-h#oh_drawing_alphaformat) alphaType | 透明度类型[OH\_Drawing\_AlphaFormat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-types-h#oh_drawing_alphaformat)。 |

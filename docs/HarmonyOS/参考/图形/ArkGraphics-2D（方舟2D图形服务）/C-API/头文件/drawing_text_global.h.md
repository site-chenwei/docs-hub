---
title: "drawing_text_global.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-text-global-h"
menu_path:
  - "参考"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "C API"
  - "头文件"
  - "drawing_text_global.h"
captured_at: "2026-04-17T01:48:49.394Z"
---

# drawing\_text\_global.h

#### 概述

提供文本全局信息的相关接口，比如设置文本渲染高对比度模式等。

**引用文件：** <native\_drawing/drawing\_text\_global.h>

**库：** libnative\_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**相关模块：** [Drawing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing)

#### 汇总

#### \[h2\]枚举

| 名称 | typedef关键字 | 描述 |
| :-- | :-- | :-- |
| [OH\_Drawing\_TextHighContrast](#oh_drawing_texthighcontrast) | OH\_Drawing\_TextHighContrast | 文本渲染高对比度模式枚举。 |
| [OH\_Drawing\_TextUndefinedGlyphDisplay](#oh_drawing_textundefinedglyphdisplay) | OH\_Drawing\_TextUndefinedGlyphDisplay | 显示未定义字形的方式。 |

#### \[h2\]函数

| 名称 | 描述 |
| :-- | :-- |
| [void OH\_Drawing\_SetTextHighContrast(OH\_Drawing\_TextHighContrast action)](#oh_drawing_settexthighcontrast) | 设置文本渲染高对比度模式。 |
| [void OH\_Drawing\_SetTextUndefinedGlyphDisplay(OH\_Drawing\_TextUndefinedGlyphDisplay undefinedGlyphDisplay)](#oh_drawing_settextundefinedglyphdisplay) | 控制未定义字形的呈现方式，影响此后渲染的所有文本。 |

#### 枚举类型说明

#### \[h2\]OH\_Drawing\_TextHighContrast

```c
enum OH_Drawing_TextHighContrast
```

**描述**

文本渲染高对比度模式枚举。

**起始版本：** 20

| 枚举项 | 描述 |
| :-- | :-- |
| TEXT\_FOLLOW\_SYSTEM\_HIGH\_CONTRAST | 跟随系统设置中的高对比度文字配置。 |
| TEXT\_APP\_DISABLE\_HIGH\_CONTRAST | 关闭APP的文本渲染高对比度配置，该模式的优先级要高于系统设置中的高对比度文字配置。 |
| TEXT\_APP\_ENABLE\_HIGH\_CONTRAST | 开启APP的文本渲染高对比度配置，该模式的优先级要高于系统设置中的高对比度文字配置。 |

#### \[h2\]OH\_Drawing\_TextUndefinedGlyphDisplay

```c
enum OH_Drawing_TextUndefinedGlyphDisplay
```

**描述**

显示未定义字形的方式。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

| 枚举项 | 描述 |
| :-- | :-- |
| TEXT\_NO\_GLYPH\_USE\_DEFAULT = 0 | 使用字体文件中定义的默认字形（可能是空框、空白或自定义符号等）。 |
| TEXT\_NO\_GLYPH\_USE\_TOFU = 1 | 始终使用豆腐块显示缺失的字形。 |

#### 函数说明

#### \[h2\]OH\_Drawing\_SetTextHighContrast()

```c
void OH_Drawing_SetTextHighContrast(OH_Drawing_TextHighContrast action)
```

**描述**

设置文本渲染高对比度模式。

该接口设置后整个进程都会生效，进程内所有页面共用相同模式。

可调用此接口设置，也可通过系统设置界面中高对比度文字配置开关进行开启/关闭。使用此接口设置开启/关闭文本渲染高对比度配置的优先级高于系统开关设置。

该接口针对应用的文字自绘制场景不生效。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_Drawing\_TextHighContrast](#oh_drawing_texthighcontrast) action | 表示文本渲染高对比度模式，为[OH\_Drawing\_TextHighContrast](#oh_drawing_texthighcontrast)类型的枚举值。 |

#### \[h2\]OH\_Drawing\_SetTextUndefinedGlyphDisplay()

```c
void OH_Drawing_SetTextUndefinedGlyphDisplay(OH_Drawing_TextUndefinedGlyphDisplay undefinedGlyphDisplay)
```

**描述**

控制未定义字形的呈现方式，影响此后渲染的所有文本。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_Drawing\_TextUndefinedGlyphDisplay](#oh_drawing_textundefinedglyphdisplay) undefinedGlyphDisplay | 表示显示未定义字形的方式，为[OH\_Drawing\_TextUndefinedGlyphDisplay](#oh_drawing_textundefinedglyphdisplay)类型的枚举值。 |

---
title: "drawing_font_collection.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-font-collection-h"
menu_path:
  - "参考"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "C API"
  - "头文件"
  - "drawing_font_collection.h"
captured_at: "2026-04-17T01:48:47.714Z"
---

# drawing\_font\_collection.h

#### 概述

定义绘制模块中与字体集合相关的函数。

**引用文件：** <native\_drawing/drawing\_font\_collection.h>

**库：** libnative\_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**相关模块：** [Drawing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing)

#### 汇总

#### \[h2\]函数

| 名称 | 描述 |
| :-- | :-- |
| [OH\_Drawing\_FontCollection\* OH\_Drawing\_CreateFontCollection(void)](#oh_drawing_createfontcollection) | 创建字体集对象[OH\_Drawing\_FontCollection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontcollection)。 |
| [void OH\_Drawing\_DestroyFontCollection(OH\_Drawing\_FontCollection\* fontCollection)](#oh_drawing_destroyfontcollection) | 释放被字体集对象占据的内存。 |
| [void OH\_Drawing\_DisableFontCollectionFallback(OH\_Drawing\_FontCollection\* fontCollection)](#oh_drawing_disablefontcollectionfallback) | 禁用系统字体。 |
| [void OH\_Drawing\_DisableFontCollectionSystemFont(OH\_Drawing\_FontCollection\* fontCollection)](#oh_drawing_disablefontcollectionsystemfont) | 禁用系统字体。 |
| [OH\_Drawing\_FontCollection\* OH\_Drawing\_CreateSharedFontCollection(void)](#oh_drawing_createsharedfontcollection) | 创建可共享的字体集对象[OH\_Drawing\_FontCollection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontcollection)。 |
| [void OH\_Drawing\_ClearFontCaches(OH\_Drawing\_FontCollection\* fontCollection)](#oh_drawing_clearfontcaches) | 清理字体排版缓存（字体排版缓存本身设有内存上限和清理机制，所占内存有限，如无内存要求，不建议清理）。 |
| [OH\_Drawing\_FontCollection\* OH\_Drawing\_GetFontCollectionGlobalInstance(void)](#oh_drawing_getfontcollectionglobalinstance) | 获取全局字体集对象[OH\_Drawing\_FontCollection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontcollection)，可感知主题字信息，禁止释放该对象。 |

#### 函数说明

#### \[h2\]OH\_Drawing\_CreateFontCollection()

```c
OH_Drawing_FontCollection* OH_Drawing_CreateFontCollection(void)
```

**描述**

创建字体集对象[OH\_Drawing\_FontCollection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontcollection)。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [OH\_Drawing\_FontCollection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontcollection)\* | 指向创建的字体集对象的指针。该函数创建的字体集指针对象OH\_Drawing\_FontCollection只能被一个[OH\_Drawing\_TypographyCreate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-typographycreate)对象使用，无法被多个OH\_Drawing\_TypographyCreate对象共享使用。如需在多个OH\_Drawing\_TypographyCreate对象间共享同一个OH\_Drawing\_FontCollection，请使用[OH\_Drawing\_CreateSharedFontCollection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-font-collection-h#oh_drawing_createsharedfontcollection)函数创建OH\_Drawing\_FontCollection对象。 |

#### \[h2\]OH\_Drawing\_DestroyFontCollection()

```c
void OH_Drawing_DestroyFontCollection(OH_Drawing_FontCollection* fontCollection)
```

**描述**

释放被字体集对象占据的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_Drawing\_FontCollection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontcollection)\* fontCollection | 指向字体集对象的指针。 |

#### \[h2\]OH\_Drawing\_DisableFontCollectionFallback()

```c
void OH_Drawing_DisableFontCollectionFallback(OH_Drawing_FontCollection* fontCollection)
```

**描述**

禁用系统字体。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**废弃版本：** 18

**替代接口：** [OH\_Drawing\_DisableFontCollectionSystemFont()](#oh_drawing_disablefontcollectionsystemfont)

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_Drawing\_FontCollection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontcollection)\* fontCollection | 指向字体集对象[OH\_Drawing\_FontCollection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontcollection)的指针。 |

#### \[h2\]OH\_Drawing\_DisableFontCollectionSystemFont()

```c
void OH_Drawing_DisableFontCollectionSystemFont(OH_Drawing_FontCollection* fontCollection)
```

**描述**

禁用系统字体。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_Drawing\_FontCollection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontcollection)\* fontCollection | 指向字体集对象[OH\_Drawing\_FontCollection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontcollection)的指针。 |

#### \[h2\]OH\_Drawing\_CreateSharedFontCollection()

```c
OH_Drawing_FontCollection* OH_Drawing_CreateSharedFontCollection(void)
```

**描述**

创建可共享的字体集对象[OH\_Drawing\_FontCollection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontcollection)。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [OH\_Drawing\_FontCollection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontcollection)\* | 指向创建的字体集对象的指针。 |

#### \[h2\]OH\_Drawing\_ClearFontCaches()

```c
void OH_Drawing_ClearFontCaches(OH_Drawing_FontCollection* fontCollection)
```

**描述**

清理字体排版缓存（字体排版缓存本身设有内存上限和清理机制，所占内存有限，如无内存要求，不建议清理）。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_Drawing\_FontCollection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontcollection)\* fontCollection | 指向字体集对象[OH\_Drawing\_FontCollection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontcollection)的指针。 |

#### \[h2\]OH\_Drawing\_GetFontCollectionGlobalInstance()

```c
OH_Drawing_FontCollection* OH_Drawing_GetFontCollectionGlobalInstance(void)
```

**描述**

获取全局字体集对象[OH\_Drawing\_FontCollection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontcollection)，可感知主题字信息，禁止释放该对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 14

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [OH\_Drawing\_FontCollection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontcollection)\* | 指向全局字体集对象的指针。 |

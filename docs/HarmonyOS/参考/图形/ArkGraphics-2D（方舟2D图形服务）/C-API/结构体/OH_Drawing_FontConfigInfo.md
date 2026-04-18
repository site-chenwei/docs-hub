---
title: "OH_Drawing_FontConfigInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontconfiginfo"
menu_path:
  - "参考"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "C API"
  - "结构体"
  - "OH_Drawing_FontConfigInfo"
captured_at: "2026-04-17T01:48:50.112Z"
---

# OH\_Drawing\_FontConfigInfo

```c
typedef struct OH_Drawing_FontConfigInfo {...} OH_Drawing_FontConfigInfo
```

#### 概述

系统字体配置信息结构体。

**起始版本：** 12

**相关模块：** [Drawing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing)

**所在头文件：** [drawing\_text\_typography.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-text-typography-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| size\_t fontDirSize | 系统字体文件路径数量。 |
| size\_t fontGenericInfoSize | 通用字体集列表数量。 |
| size\_t fallbackGroupSize | 备用字体集列表数量。 |
| char\*\* fontDirSet | 系统字体文件路径列表。 |
| [OH\_Drawing\_FontGenericInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontgenericinfo)\* fontGenericInfoSet | 通用字体集列表。 |
| [OH\_Drawing\_FontFallbackGroup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontfallbackgroup)\* fallbackGroupSet | 备用字体集列表。 |

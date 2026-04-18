---
title: "OH_Drawing_FontFallbackInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontfallbackinfo"
menu_path:
  - "参考"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "C API"
  - "结构体"
  - "OH_Drawing_FontFallbackInfo"
captured_at: "2026-04-17T01:48:50.025Z"
---

# OH\_Drawing\_FontFallbackInfo

```c
typedef struct OH_Drawing_FontFallbackInfo {...} OH_Drawing_FontFallbackInfo
```

#### 概述

备用字体信息结构体。

**起始版本：** 12

**相关模块：** [Drawing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing)

**所在头文件：** [drawing\_text\_typography.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-text-typography-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| char\* language | 字体集所支持的语言类型，语言格式为bcp47。 |
| char\* familyName | 字体家族名。 |

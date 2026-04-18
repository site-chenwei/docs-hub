---
title: "OH_Drawing_FontAdjustInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontadjustinfo"
menu_path:
  - "参考"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "C API"
  - "结构体"
  - "OH_Drawing_FontAdjustInfo"
captured_at: "2026-04-17T01:48:50.096Z"
---

# OH\_Drawing\_FontAdjustInfo

```c
typedef struct OH_Drawing_FontAdjustInfo {...} OH_Drawing_FontAdjustInfo
```

#### 概述

字重映射信息结构体。

**起始版本：** 12

**相关模块：** [Drawing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing)

**所在头文件：** [drawing\_text\_typography.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-text-typography-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int weight | 字体原本的字重值。 |
| int to | 字体在应用中显示的字重值。 |

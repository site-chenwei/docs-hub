---
title: "OH_Drawing_RunBuffer"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-runbuffer"
menu_path:
  - "参考"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "C API"
  - "结构体"
  - "OH_Drawing_RunBuffer"
captured_at: "2026-04-17T01:48:49.997Z"
---

# OH\_Drawing\_RunBuffer

```c
typedef struct {...} OH_Drawing_RunBuffer
```

#### 概述

结构体用于描述一块内存，描述文字和位置信息。

**起始版本：** 11

**相关模块：** [Drawing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing)

**所在头文件：** [drawing\_text\_blob.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-text-blob-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint16\_t\* glyphs | 存储文字索引。 |
| float\* pos | 存储文字的位置。 |
| char\* utf8text | 存储文字UTF-8编码。 |
| uint32\_t\* clusters | 存储文字簇UTF-8编码（簇指的是集合）。 |

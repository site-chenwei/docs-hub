---
title: "OH_Drawing_String"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-string"
menu_path:
  - "参考"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "C API"
  - "结构体"
  - "OH_Drawing_String"
captured_at: "2026-04-17T01:48:50.244Z"
---

# OH\_Drawing\_String

```c
typedef struct {...} OH_Drawing_String
```

#### 概述

采用UTF-16编码的字符串信息结构体。

**起始版本：** 14

**相关模块：** [Drawing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing)

**所在头文件：** [drawing\_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-types-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint8\_t\* strData | 指向包含UTF-16编码的字节数组的指针。 |
| uint32\_t strLen | strData指向的字符串的实际长度，单位为字节。 |

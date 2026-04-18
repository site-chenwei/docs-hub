---
title: "OH_Drawing_FontGenericInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontgenericinfo"
menu_path:
  - "参考"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "C API"
  - "结构体"
  - "OH_Drawing_FontGenericInfo"
captured_at: "2026-04-17T01:48:50.098Z"
---

# OH\_Drawing\_FontGenericInfo

```c
typedef struct OH_Drawing_FontGenericInfo {...} OH_Drawing_FontGenericInfo
```

#### 概述

系统所支持的通用字体集信息结构体。

**起始版本：** 12

**相关模块：** [Drawing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing)

**所在头文件：** [drawing\_text\_typography.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-text-typography-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| char\* familyName | 字体家族名。 |
| size\_t aliasInfoSize | 别名字体列表的数量。 |
| size\_t adjustInfoSize | 字重映射列表的数量。 |
| [OH\_Drawing\_FontAliasInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontaliasinfo)\* aliasInfoSet | 别名字体列表。 |
| [OH\_Drawing\_FontAdjustInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontadjustinfo)\* adjustInfoSet | 字重映射列表。 |

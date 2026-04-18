---
title: "ArkUI_GridItemSize"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-griditemsize"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "C API"
  - "结构体"
  - "ArkUI_GridItemSize"
captured_at: "2026-04-17T01:48:10.607Z"
---

# ArkUI\_GridItemSize

```c
typedef struct {...} ArkUI_GridItemSize
```

#### 概述

定义Grid布局选项onGetIrregularSizeByIndex回调返回值结构体。

**起始版本：** 22

**相关模块：** [ArkUI\_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)

**所在头文件：** [native\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h)

**相关示例：** [native\_type\_sample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeTypeSample)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t rowSpan | GridItem占用的行数。 |
| uint32\_t columnSpan | GridItem占用的列数。 |

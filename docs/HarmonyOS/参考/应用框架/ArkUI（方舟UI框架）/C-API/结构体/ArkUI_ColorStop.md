---
title: "ArkUI_ColorStop"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-colorstop"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "C API"
  - "结构体"
  - "ArkUI_ColorStop"
captured_at: "2026-04-17T01:48:09.414Z"
---

# ArkUI\_ColorStop

```c
typedef struct {...} ArkUI_ColorStop
```

#### 概述

定义渐变色结构。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)

**所在头文件：** [native\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| const uint32\_t\* colors | 颜色数组。 |
| float\* stops | 位置数组。 |
| int size | 数组长度。 |

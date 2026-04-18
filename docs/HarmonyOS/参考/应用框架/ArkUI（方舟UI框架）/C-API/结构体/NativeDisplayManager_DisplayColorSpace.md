---
title: "NativeDisplayManager_DisplayColorSpace"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-displaycolorspace"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "C API"
  - "结构体"
  - "NativeDisplayManager_DisplayColorSpace"
captured_at: "2026-04-17T01:48:10.300Z"
---

# NativeDisplayManager\_DisplayColorSpace

```c
typedef struct {...} NativeDisplayManager_DisplayColorSpace
```

#### 概述

显示设备支持的所有色域类型。

**起始版本：** 14

**相关模块：** [OH\_DisplayManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-displaymanager)

**所在头文件：** [oh\_display\_info.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t colorSpaceLength | 显示设备的色域长度。 |
| uint32\_t\* colorSpaces | 显示设备的色域数据。 |

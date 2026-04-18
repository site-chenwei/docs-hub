---
title: "NativeDisplayManager_DisplayHdrFormat"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-displayhdrformat"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "C API"
  - "结构体"
  - "NativeDisplayManager_DisplayHdrFormat"
captured_at: "2026-04-17T01:48:10.281Z"
---

# NativeDisplayManager\_DisplayHdrFormat

```c
typedef struct {...} NativeDisplayManager_DisplayHdrFormat
```

#### 概述

显示设备支持的所有HDR格式。

**起始版本：** 14

**相关模块：** [OH\_DisplayManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-displaymanager)

**所在头文件：** [oh\_display\_info.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t hdrFormatLength | 显示设备的HDR格式长度。 |
| uint32\_t\* hdrFormats | 显示设备的HDR格式数据。 |

---
title: "NativeDisplayManager_DisplaysInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-displaysinfo"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "C API"
  - "结构体"
  - "NativeDisplayManager_DisplaysInfo"
captured_at: "2026-04-17T01:48:10.298Z"
---

# NativeDisplayManager\_DisplaysInfo

```c
typedef struct {...} NativeDisplayManager_DisplaysInfo
```

#### 概述

多显示设备的Display对象。

**起始版本：** 14

**相关模块：** [OH\_DisplayManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-displaymanager)

**所在头文件：** [oh\_display\_info.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t displaysLength | 多显示设备Display对象的长度。 |
| [NativeDisplayManager\_DisplayInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-displayinfo)\* displaysInfo | 多显示设备Display对象的属性。 |

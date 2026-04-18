---
title: "NativeDisplayManager_CutoutInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-cutoutinfo"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "C API"
  - "结构体"
  - "NativeDisplayManager_CutoutInfo"
captured_at: "2026-04-17T01:48:10.279Z"
---

# NativeDisplayManager\_CutoutInfo

```c
typedef struct {...} NativeDisplayManager_CutoutInfo
```

#### 概述

挖孔屏、刘海屏、瀑布屏等不可用屏幕区域信息。

**起始版本：** 12

**相关模块：** [OH\_DisplayManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-displaymanager)

**所在头文件：** [oh\_display\_info.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int32\_t boundingRectsLength | 挖孔屏、刘海屏不可用屏幕区域长度。 |
| [NativeDisplayManager\_Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-rect)\* boundingRects | 挖孔屏、刘海屏等区域的边界矩形。 |
| [NativeDisplayManager\_WaterfallDisplayAreaRects](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-nativedisplaymanager-waterfalldisplayarearects) waterfallDisplayAreaRects | 瀑布屏曲面部分显示区域。 |

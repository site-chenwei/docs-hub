---
title: "OH_Rect"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-rect"
menu_path:
  - "参考"
  - "媒体"
  - "Media Kit（媒体服务）"
  - "C API"
  - "结构体"
  - "OH_Rect"
captured_at: "2026-04-17T01:48:44.516Z"
---

# OH\_Rect

```c
typedef struct OH_Rect {...} OH_Rect
```

#### 概述

定义录屏界面的宽高以及画面信息。

**起始版本：** 10

**相关模块：** [AVScreenCapture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture)

**所在头文件：** [native\_avscreen\_capture\_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avscreen-capture-base-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int32\_t x | 录屏界面的X坐标。 |
| int32\_t y | 录屏界面的Y坐标。 |
| int32\_t width | 录屏界面的宽度，单位px。 |
| int32\_t height | 录屏界面的高度，单位px。 |

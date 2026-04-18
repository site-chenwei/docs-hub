---
title: "WindowManager_Rect"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-windowmanager-rect"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "C API"
  - "结构体"
  - "WindowManager_Rect"
captured_at: "2026-04-17T01:48:10.173Z"
---

# WindowManager\_Rect

```c
typedef struct {...} WindowManager_Rect
```

#### 概述

定义窗口矩形结构体，包含窗口位置和宽高信息。

**起始版本：** 15

**相关模块：** [WindowManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-windowmanager)

**所在头文件：** [oh\_window\_comm.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-window-comm-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int32\_t posX | 窗口的x轴，单位为px，该参数为整数。 |
| int32\_t posY | 窗口的y轴，单位为px，该参数为整数。 |
| uint32\_t width | 窗口的宽度，单位为px，该参数为整数。 |
| uint32\_t height | 窗口的高度，单位为px，该参数为整数。 |

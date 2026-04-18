---
title: "WindowManager_MainWindowInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-windowmanager-windowmanager-mainwindowinfo"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "C API"
  - "结构体"
  - "WindowManager_MainWindowInfo"
captured_at: "2026-04-17T01:48:10.198Z"
---

# WindowManager\_MainWindowInfo

```c
typedef struct {...} WindowManager_MainWindowInfo
```

#### 概述

主窗口信息。

**起始版本：** 21

**相关模块：** [WindowManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-windowmanager)

**所在头文件：** [oh\_window\_comm.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-window-comm-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint64\_t displayId | 主窗口所在的屏幕ID。 |
| int32\_t windowId | 主窗口ID。 |
| bool showing | 主窗口的前后台状态。true表示主窗口在前台，false表示主窗口不在前台。 |
| const char\* label | 主窗口任务名称。 |

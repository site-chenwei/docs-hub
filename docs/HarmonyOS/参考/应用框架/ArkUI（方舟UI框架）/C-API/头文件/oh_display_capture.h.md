---
title: "oh_display_capture.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-capture-h"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "C API"
  - "头文件"
  - "oh_display_capture.h"
captured_at: "2026-04-17T01:48:07.835Z"
---

# oh\_display\_capture.h

#### 概述

提供屏幕截屏的能力。

**引用文件：** <window\_manager/oh\_display\_capture.h>

**库：** libnative\_display\_manager.so

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 14

**相关模块：** [OH\_DisplayManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-displaymanager)

#### 汇总

#### \[h2\]函数

| 名称 | 描述 |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_CaptureScreenPixelmap(uint32\_t displayId,OH\_PixelmapNative \*\*pixelMap)](#oh_nativedisplaymanager_capturescreenpixelmap) | 获取屏幕全屏截图，可以通过设置不同的屏幕id号截取不同屏幕的截图。 |

#### 函数说明

#### \[h2\]OH\_NativeDisplayManager\_CaptureScreenPixelmap()

```c
NativeDisplayManager_ErrorCode OH_NativeDisplayManager_CaptureScreenPixelmap(uint32_t displayId,OH_PixelmapNative **pixelMap)
```

**描述**

获取屏幕全屏截图，可以通过设置不同的屏幕id号截取不同屏幕的截图。

**需要权限：** ohos.permission.CUSTOM\_SCREEN\_CAPTURE

**起始版本：** 14

**设备行为差异：** 在API version 21之前，该接口在2in1设备、Tablet设备中可正常调用，在其他设备中返回801错误码。从API version 21开始，该接口在Phone设备、2in1设备、Tablet设备中可正常调用，在其他设备中返回801错误码。

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| uint32\_t displayId | 需要截屏的屏幕id号，该值为非负整数。 |
| [OH\_PixelmapNative](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-pixelmapnative) \*\*pixelMap | 创建指定屏幕id的OH\_PixelmapNative对象，此处作为出参返回。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode) | 返回屏幕管理接口的通用状态码，具体可见[NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode)。 |

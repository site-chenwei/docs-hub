---
title: "oh_display_manager.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-manager-h"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "C API"
  - "头文件"
  - "oh_display_manager.h"
captured_at: "2026-04-17T01:48:08.194Z"
---

# oh\_display\_manager.h

#### 概述

提供屏幕管理的一些基础能力，包括获取默认显示设备的信息，以及监听显示设备的旋转、折叠、展开等状态变化的能力。

**引用文件：** <window\_manager/oh\_display\_manager.h>

**库：** libnative\_display\_manager.so

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

**相关模块：** [OH\_DisplayManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-displaymanager)

#### 汇总

#### \[h2\]函数

| 名称 | typedef关键字 | 描述 |
| :-- | :-- | :-- |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDefaultDisplayId(uint64\_t \*displayId)](#oh_nativedisplaymanager_getdefaultdisplayid) | \- | 获取默认屏幕的id号。 |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDefaultDisplayWidth(int32\_t \*displayWidth)](#oh_nativedisplaymanager_getdefaultdisplaywidth) | \- | 获取默认屏幕的宽度。 |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDefaultDisplayHeight(int32\_t \*displayHeight)](#oh_nativedisplaymanager_getdefaultdisplayheight) | \- | 获取默认屏幕的高度。 |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDefaultDisplayRotation(NativeDisplayManager\_Rotation \*displayRotation)](#oh_nativedisplaymanager_getdefaultdisplayrotation) | \- | 获取默认屏幕的顺时针旋转角度。 |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDefaultDisplayOrientation(NativeDisplayManager\_Orientation \*displayOrientation)](#oh_nativedisplaymanager_getdefaultdisplayorientation) | \- | 获取默认屏幕的旋转方向。 |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDefaultDisplayVirtualPixelRatio(float \*virtualPixels)](#oh_nativedisplaymanager_getdefaultdisplayvirtualpixelratio) | \- | 获取默认屏幕的虚拟像素密度。 |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDefaultDisplayRefreshRate(uint32\_t \*refreshRate)](#oh_nativedisplaymanager_getdefaultdisplayrefreshrate) | \- | 获取默认屏幕的刷新率。 |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDefaultDisplayDensityDpi(int32\_t \*densityDpi)](#oh_nativedisplaymanager_getdefaultdisplaydensitydpi) | \- | 获取屏幕的物理像素密度。 |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDefaultDisplayDensityPixels(float \*densityPixels)](#oh_nativedisplaymanager_getdefaultdisplaydensitypixels) | \- | 获取屏幕逻辑像素的密度。 |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDefaultDisplayScaledDensity(float \*scaledDensity)](#oh_nativedisplaymanager_getdefaultdisplayscaleddensity) | \- | 获取屏幕显示字体的缩放因子。 |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDefaultDisplayDensityXdpi(float \*xDpi)](#oh_nativedisplaymanager_getdefaultdisplaydensityxdpi) | \- | 获取屏幕X方向中每英寸屏幕的物理像素值。 |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDefaultDisplayDensityYdpi(float \*yDpi)](#oh_nativedisplaymanager_getdefaultdisplaydensityydpi) | \- | 获取Y方向中每英寸屏幕的物理像素值。 |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_CreateDefaultDisplayCutoutInfo(NativeDisplayManager\_CutoutInfo \*\*cutoutInfo)](#oh_nativedisplaymanager_createdefaultdisplaycutoutinfo) | \- | 获取挖孔屏、刘海屏、瀑布屏等不可用屏幕区域信息。 |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_DestroyDefaultDisplayCutoutInfo(NativeDisplayManager\_CutoutInfo \*cutoutInfo)](#oh_nativedisplaymanager_destroydefaultdisplaycutoutinfo) | \- | 销毁挖孔屏、刘海屏、瀑布屏等不可用屏幕区域信息。 |
| [bool OH\_NativeDisplayManager\_IsFoldable()](#oh_nativedisplaymanager_isfoldable) | \- | 查询设备是否可折叠。 |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetFoldDisplayMode(NativeDisplayManager\_FoldDisplayMode \*displayMode)](#oh_nativedisplaymanager_getfolddisplaymode) | \- | 获取可折叠设备的显示模式。 |
| [typedef void (\*OH\_NativeDisplayManager\_DisplayChangeCallback)(uint64\_t displayId)](#oh_nativedisplaymanager_displaychangecallback) | OH\_NativeDisplayManager\_DisplayChangeCallback | 注册屏幕状态变化的回调函数。 |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_RegisterDisplayChangeListener(OH\_NativeDisplayManager\_DisplayChangeCallback displayChangeCallback, uint32\_t \*listenerIndex)](#oh_nativedisplaymanager_registerdisplaychangelistener) | \- | 注册屏幕状态变化监听（如旋转变化、刷新率、DPI、分辨率等变化）。 |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_UnregisterDisplayChangeListener(uint32\_t listenerIndex)](#oh_nativedisplaymanager_unregisterdisplaychangelistener) | \- | 取消屏幕状态变化的监听。 |
| [typedef void (\*OH\_NativeDisplayManager\_FoldDisplayModeChangeCallback)(NativeDisplayManager\_FoldDisplayMode displayMode)](#oh_nativedisplaymanager_folddisplaymodechangecallback) | OH\_NativeDisplayManager\_FoldDisplayModeChangeCallback | 注册屏幕展开、折叠状态变化的回调函数。 |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_RegisterFoldDisplayModeChangeListener(OH\_NativeDisplayManager\_FoldDisplayModeChangeCallback displayModeChangeCallback, uint32\_t \*listenerIndex)](#oh_nativedisplaymanager_registerfolddisplaymodechangelistener) | \- | 注册屏幕展开、折叠状态变化的监听。 |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_UnregisterFoldDisplayModeChangeListener(uint32\_t listenerIndex)](#oh_nativedisplaymanager_unregisterfolddisplaymodechangelistener) | \- | 取消屏幕展开、折叠状态变化的监听。 |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_CreateAllDisplays(NativeDisplayManager\_DisplaysInfo \*\*allDisplays)](#oh_nativedisplaymanager_createalldisplays) | \- | 获取当前所有屏幕信息对象。 |
| [void OH\_NativeDisplayManager\_DestroyAllDisplays(NativeDisplayManager\_DisplaysInfo \*allDisplays)](#oh_nativedisplaymanager_destroyalldisplays) | \- | 销毁所有屏幕的信息对象。 |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_CreateDisplayById(uint32\_t displayId,NativeDisplayManager\_DisplayInfo \*\*displayInfo)](#oh_nativedisplaymanager_createdisplaybyid) | \- | 获取指定屏幕的信息对象。 |
| [void OH\_NativeDisplayManager\_DestroyDisplay(NativeDisplayManager\_DisplayInfo \*displayInfo)](#oh_nativedisplaymanager_destroydisplay) | \- | 销毁指定屏幕的信息对象。 |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_CreatePrimaryDisplay(NativeDisplayManager\_DisplayInfo \*\*displayInfo)](#oh_nativedisplaymanager_createprimarydisplay) | \- | 获取主屏信息对象。除2in1之外的设备获取的是设备自带屏幕的屏幕信息；2in1设备外接屏幕时获取的是当前主屏幕的屏幕信息；2in1设备没有外接屏幕时获取的是自带屏幕的屏幕信息。 |
| [typedef void (\*OH\_NativeDisplayManager\_AvailableAreaChangeCallback)(uint64\_t displayId)](#oh_nativedisplaymanager_availableareachangecallback) | OH\_NativeDisplayManager\_AvailableAreaChangeCallback | 注册屏幕可用区域变化的回调函数。 |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_RegisterAvailableAreaChangeListener(OH\_NativeDisplayManager\_AvailableAreaChangeCallback availableAreaChangeCallback, uint32\_t \*listenerIndex)](#oh_nativedisplaymanager_registeravailableareachangelistener) | \- | 注册屏幕可用区域变化监听。 |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_UnregisterAvailableAreaChangeListener(uint32\_t listenerIndex)](#oh_nativedisplaymanager_unregisteravailableareachangelistener) | \- | 取消屏幕可用区域变化的监听。 |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_CreateAvailableArea(uint64\_t displayId, NativeDisplayManager\_Rect \*\*availableArea)](#oh_nativedisplaymanager_createavailablearea) | \- | 获取屏幕的可用区域。 |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_DestroyAvailableArea(NativeDisplayManager\_Rect \*availableArea)](#oh_nativedisplaymanager_destroyavailablearea) | \- | 销毁屏幕的可用区域。 |
| [typedef void (\*OH\_NativeDisplayManager\_DisplayAddCallback)(uint64\_t displayId)](#oh_nativedisplaymanager_displayaddcallback) | OH\_NativeDisplayManager\_DisplayAddCallback | 注册屏幕连接的回调函数。 |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_RegisterDisplayAddListener(OH\_NativeDisplayManager\_DisplayAddCallback displayAddCallback, uint32\_t \*listenerIndex)](#oh_nativedisplaymanager_registerdisplayaddlistener) | \- | 注册屏幕连接变化监听（如插入显示器）。 |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_UnregisterDisplayAddListener(uint32\_t listenerIndex)](#oh_nativedisplaymanager_unregisterdisplayaddlistener) | \- | 取消屏幕连接的监听。 |
| [typedef void (\*OH\_NativeDisplayManager\_DisplayRemoveCallback)(uint64\_t displayId)](#oh_nativedisplaymanager_displayremovecallback) | OH\_NativeDisplayManager\_DisplayRemoveCallback | 注册屏幕移除的回调函数。 |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_RegisterDisplayRemoveListener(OH\_NativeDisplayManager\_DisplayRemoveCallback displayRemoveCallback, uint32\_t \*listenerIndex)](#oh_nativedisplaymanager_registerdisplayremovelistener) | \- | 注册屏幕移除变化监听（如移除显示器）。 |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_UnregisterDisplayRemoveListener(uint32\_t listenerIndex)](#oh_nativedisplaymanager_unregisterdisplayremovelistener) | \- | 取消屏幕移除的监听。 |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDisplaySourceMode(uint64\_t displayId, NativeDisplayManager\_SourceMode \*sourceMode)](#oh_nativedisplaymanager_getdisplaysourcemode) | \- | 获取屏幕的显示模式。 |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_GetDisplayPosition(uint64\_t displayId, int32\_t \*x, int32\_t \*y)](#oh_nativedisplaymanager_getdisplayposition) | \- | 获取屏幕的位置信息。 |

#### 函数说明

#### \[h2\]OH\_NativeDisplayManager\_GetDefaultDisplayId()

```c
NativeDisplayManager_ErrorCode OH_NativeDisplayManager_GetDefaultDisplayId(uint64_t *displayId)
```

**描述**

获取默认屏幕的id号。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| uint64\_t \*displayId | 默认屏幕的id号，非负整数，此处作为出参返回。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode) | 返回屏幕管理接口的通用状态码，具体可见[NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode)。 |

#### \[h2\]OH\_NativeDisplayManager\_GetDefaultDisplayWidth()

```c
NativeDisplayManager_ErrorCode OH_NativeDisplayManager_GetDefaultDisplayWidth(int32_t *displayWidth)
```

**描述**

获取默认屏幕的宽度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| int32\_t \*displayWidth | 默认屏幕的宽度，单位为px，该参数应为整数，此处作为出参返回。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode) | 返回屏幕管理接口的通用状态码，具体可见[NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode)。 |

#### \[h2\]OH\_NativeDisplayManager\_GetDefaultDisplayHeight()

```c
NativeDisplayManager_ErrorCode OH_NativeDisplayManager_GetDefaultDisplayHeight(int32_t *displayHeight)
```

**描述**

获取默认屏幕的高度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| int32\_t \*displayHeight | 默认屏幕的高度，单位为px，该参数应为整数，此处作为出参返回。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode) | 返回屏幕管理接口的通用状态码，具体可见[NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode)。 |

#### \[h2\]OH\_NativeDisplayManager\_GetDefaultDisplayRotation()

```c
NativeDisplayManager_ErrorCode OH_NativeDisplayManager_GetDefaultDisplayRotation(NativeDisplayManager_Rotation *displayRotation)
```

**描述**

获取默认屏幕的顺时针旋转角度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [NativeDisplayManager\_Rotation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_rotation) \*displayRotation | 默认屏幕的顺时针旋转角度，具体可见[NativeDisplayManager\_Rotation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_rotation)，此处作为出参返回。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode) | 返回屏幕管理接口的通用状态码，具体可见[NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode)。 |

#### \[h2\]OH\_NativeDisplayManager\_GetDefaultDisplayOrientation()

```c
NativeDisplayManager_ErrorCode OH_NativeDisplayManager_GetDefaultDisplayOrientation(NativeDisplayManager_Orientation *displayOrientation)
```

**描述**

获取默认屏幕的旋转方向。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [NativeDisplayManager\_Orientation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_orientation) \*displayOrientation | 屏幕当前显示的方向，具体可见[NativeDisplayManager\_Orientation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_orientation)，此处作为出参返回。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode) | 返回屏幕管理接口的通用状态码，具体可见[NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode)。 |

#### \[h2\]OH\_NativeDisplayManager\_GetDefaultDisplayVirtualPixelRatio()

```c
NativeDisplayManager_ErrorCode OH_NativeDisplayManager_GetDefaultDisplayVirtualPixelRatio(float *virtualPixels)
```

**描述**

获取默认屏幕的虚拟像素密度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| float \*virtualPixels | 屏幕的虚拟像素密度，该参数为浮点数，通常与densityPixels相同，此处作为出参返回。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode) | 返回屏幕管理接口的通用状态码，具体可见[NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode)。 |

#### \[h2\]OH\_NativeDisplayManager\_GetDefaultDisplayRefreshRate()

```c
NativeDisplayManager_ErrorCode OH_NativeDisplayManager_GetDefaultDisplayRefreshRate(uint32_t *refreshRate)
```

**描述**

获取默认屏幕的刷新率。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| uint32\_t \*refreshRate | 屏幕的刷新率，该参数应为整数，单位为Hz，此处作为出参返回。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode) | 返回屏幕管理接口的通用状态码，具体可见[NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode)。 |

#### \[h2\]OH\_NativeDisplayManager\_GetDefaultDisplayDensityDpi()

```c
NativeDisplayManager_ErrorCode OH_NativeDisplayManager_GetDefaultDisplayDensityDpi(int32_t *densityDpi)
```

**描述**

获取屏幕的物理像素密度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| int32\_t \*densityDpi | 屏幕的物理像素密度，表示每英寸上的像素点数。该参数为整数，单位为px，实际能取到的值取决于不同设备设置里提供的可选值。此处作为出参返回。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode) | 返回屏幕管理接口的通用状态码，具体可见[NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode)。 |

#### \[h2\]OH\_NativeDisplayManager\_GetDefaultDisplayDensityPixels()

```c
NativeDisplayManager_ErrorCode OH_NativeDisplayManager_GetDefaultDisplayDensityPixels(float *densityPixels)
```

**描述**

获取屏幕逻辑像素的密度。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| float \*densityPixels | 设备逻辑像素的密度，代表物理像素与逻辑像素的缩放系数，该参数为浮点数，受densityDPI范围限制，取值范围在\[0.5，4.0\]。一般取值1.0、3.0等，实际取值取决于不同设备提供的densityDpi。此处作为出参返回。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode) | 返回屏幕管理接口的通用状态码，具体可见[NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode)。 |

#### \[h2\]OH\_NativeDisplayManager\_GetDefaultDisplayScaledDensity()

```c
NativeDisplayManager_ErrorCode OH_NativeDisplayManager_GetDefaultDisplayScaledDensity(float *scaledDensity)
```

**描述**

获取屏幕显示字体的缩放因子。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| float \*scaledDensity | 显示字体的缩放因子，该参数为浮点数，通常与densityPixels相同，此处作为出参返回。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode) | 返回屏幕管理接口的通用状态码，具体可见[NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode)。 |

#### \[h2\]OH\_NativeDisplayManager\_GetDefaultDisplayDensityXdpi()

```c
NativeDisplayManager_ErrorCode OH_NativeDisplayManager_GetDefaultDisplayDensityXdpi(float *xDpi)
```

**描述**

获取屏幕X方向中每英寸屏幕的物理像素值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| float \*xDpi | X方向中每英寸屏幕的物理像素值，该参数为浮点数，此处作为出参返回。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode) | 返回屏幕管理接口的通用状态码，具体可见[NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode)。 |

#### \[h2\]OH\_NativeDisplayManager\_GetDefaultDisplayDensityYdpi()

```c
NativeDisplayManager_ErrorCode OH_NativeDisplayManager_GetDefaultDisplayDensityYdpi(float *yDpi)
```

**描述**

获取Y方向中每英寸屏幕的物理像素值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| float \*yDpi | 获取Y方向中每英寸屏幕的物理像素值，该参数为浮点数，此处作为出参返回。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode) | 返回屏幕管理接口的通用状态码，具体可见[NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode)。 |

#### \[h2\]OH\_NativeDisplayManager\_CreateDefaultDisplayCutoutInfo()

```c
NativeDisplayManager_ErrorCode OH_NativeDisplayManager_CreateDefaultDisplayCutoutInfo(NativeDisplayManager_CutoutInfo **cutoutInfo)
```

**描述**

获取挖孔屏、刘海屏、瀑布屏等不可用屏幕区域信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [NativeDisplayManager\_CutoutInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-cutoutinfo) \*\*cutoutInfo | 挖孔屏、刘海屏、瀑布屏等不可用屏幕区域信息，具体可见[NativeDisplayManager\_CutoutInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-cutoutinfo)，此处作为出参返回。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode) | 返回屏幕管理接口的通用状态码，具体可见[NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode)。 |

#### \[h2\]OH\_NativeDisplayManager\_DestroyDefaultDisplayCutoutInfo()

```c
NativeDisplayManager_ErrorCode OH_NativeDisplayManager_DestroyDefaultDisplayCutoutInfo(NativeDisplayManager_CutoutInfo *cutoutInfo)
```

**描述**

销毁挖孔屏、刘海屏、瀑布屏等不可用屏幕区域信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [NativeDisplayManager\_CutoutInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-cutoutinfo) \*cutoutInfo | 销毁通过[OH\_NativeDisplayManager\_CreateDefaultDisplayCutoutInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-manager-h#oh_nativedisplaymanager_createdefaultdisplaycutoutinfo)接口获取的挖孔屏、刘海屏、瀑布屏等不可用屏幕区域信息对象，具体可见[NativeDisplayManager\_CutoutInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-cutoutinfo)。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode) | 返回屏幕管理接口的通用状态码，具体可见[NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode)。 |

#### \[h2\]OH\_NativeDisplayManager\_IsFoldable()

```c
bool OH_NativeDisplayManager_IsFoldable()
```

**描述**

查询设备是否可折叠。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| bool | 返回查询设备是否可折叠的结果。true表示设备可折叠，false表示设备不可折叠。 |

#### \[h2\]OH\_NativeDisplayManager\_GetFoldDisplayMode()

```c
NativeDisplayManager_ErrorCode OH_NativeDisplayManager_GetFoldDisplayMode(NativeDisplayManager_FoldDisplayMode *displayMode)
```

**描述**

获取可折叠设备的显示模式。

**起始版本：** 12

**设备行为差异：** 该接口在2in1设备、非折叠设备中返回0，在其他设备中可正常调用。

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [NativeDisplayManager\_FoldDisplayMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_folddisplaymode) \*displayMode | 折叠设备当前的显示模式，具体可见[NativeDisplayManager\_FoldDisplayMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_folddisplaymode)，此处作为出参返回。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode) | 返回屏幕管理接口的通用状态码，具体可见[NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode)。 |

#### \[h2\]OH\_NativeDisplayManager\_DisplayChangeCallback()

```c
typedef void (*OH_NativeDisplayManager_DisplayChangeCallback)(uint64_t displayId)
```

**描述**

注册屏幕状态变化的回调函数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| uint64\_t displayId | 屏幕状态发生变化的编号。 |

#### \[h2\]OH\_NativeDisplayManager\_RegisterDisplayChangeListener()

```c
NativeDisplayManager_ErrorCode OH_NativeDisplayManager_RegisterDisplayChangeListener(OH_NativeDisplayManager_DisplayChangeCallback displayChangeCallback, uint32_t *listenerIndex)
```

**描述**

注册屏幕状态变化监听（如旋转变化、刷新率、DPI、分辨率等变化）。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_NativeDisplayManager\_DisplayChangeCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-manager-h#oh_nativedisplaymanager_displaychangecallback) displayChangeCallback | 屏幕状态变化后触发的回调函数，回调函数定义见[OH\_NativeDisplayManager\_DisplayChangeCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-manager-h#oh_nativedisplaymanager_displaychangecallback)。 |
| uint32\_t \*listenerIndex | 注册成功后返回的监听编号，调用取消注册函数[OH\_NativeDisplayManager\_UnregisterDisplayChangeListener](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-manager-h#oh_nativedisplaymanager_unregisterdisplaychangelistener)时作为入参使用，此处作为出参返回。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode) | 返回屏幕管理接口的通用状态码，具体可见[NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode)。 |

#### \[h2\]OH\_NativeDisplayManager\_UnregisterDisplayChangeListener()

```c
NativeDisplayManager_ErrorCode OH_NativeDisplayManager_UnregisterDisplayChangeListener(uint32_t listenerIndex)
```

**描述**

取消屏幕状态变化的监听。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| uint32\_t listenerIndex | 调用注册函数[OH\_NativeDisplayManager\_RegisterDisplayChangeListener](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-manager-h#oh_nativedisplaymanager_registerdisplaychangelistener)时获取到的监听编号。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode) | 返回屏幕管理接口的通用状态码，具体可见[NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode)。 |

#### \[h2\]OH\_NativeDisplayManager\_FoldDisplayModeChangeCallback()

```c
typedef void (*OH_NativeDisplayManager_FoldDisplayModeChangeCallback)(NativeDisplayManager_FoldDisplayMode displayMode)
```

**描述**

注册屏幕展开、折叠状态变化的回调函数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [NativeDisplayManager\_FoldDisplayMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_folddisplaymode) displayMode | 折叠/展开动作执行后屏幕的状态，具体可见[NativeDisplayManager\_FoldDisplayMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_folddisplaymode)。 |

#### \[h2\]OH\_NativeDisplayManager\_RegisterFoldDisplayModeChangeListener()

```c
NativeDisplayManager_ErrorCode OH_NativeDisplayManager_RegisterFoldDisplayModeChangeListener(OH_NativeDisplayManager_FoldDisplayModeChangeCallback displayModeChangeCallback, uint32_t *listenerIndex)
```

**描述**

注册屏幕展开、折叠状态变化的监听。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_NativeDisplayManager\_FoldDisplayModeChangeCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-manager-h#oh_nativedisplaymanager_folddisplaymodechangecallback) displayModeChangeCallback | 屏幕展开和折叠变化后触发的回调函数，回调函数定义见[OH\_NativeDisplayManager\_FoldDisplayModeChangeCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-manager-h#oh_nativedisplaymanager_folddisplaymodechangecallback)。 |
| uint32\_t \*listenerIndex | 注册成功后返回的监听编号，调用取消注册函数[OH\_NativeDisplayManager\_UnregisterFoldDisplayModeChangeListener](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-manager-h#oh_nativedisplaymanager_unregisterfolddisplaymodechangelistener)时作为入参使用，此处作为出参返回。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode) | 返回屏幕管理接口的通用状态码，具体可见[NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode)。 |

#### \[h2\]OH\_NativeDisplayManager\_UnregisterFoldDisplayModeChangeListener()

```c
NativeDisplayManager_ErrorCode OH_NativeDisplayManager_UnregisterFoldDisplayModeChangeListener(uint32_t listenerIndex)
```

**描述**

取消屏幕展开、折叠状态变化的监听。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| uint32\_t listenerIndex | 调用注册函数[OH\_NativeDisplayManager\_RegisterFoldDisplayModeChangeListener](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-manager-h#oh_nativedisplaymanager_registerfolddisplaymodechangelistener)时获取到的监听编号。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode) | 返回屏幕管理接口的通用状态码，具体可见[NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode)。 |

#### \[h2\]OH\_NativeDisplayManager\_CreateAllDisplays()

```c
NativeDisplayManager_ErrorCode OH_NativeDisplayManager_CreateAllDisplays(NativeDisplayManager_DisplaysInfo **allDisplays)
```

**描述**

获取当前所有屏幕信息对象。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [NativeDisplayManager\_DisplaysInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-displaysinfo) \*\*allDisplays | 当前所有的屏幕信息，具体可见[NativeDisplayManager\_DisplaysInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-displaysinfo)，此处作为出参返回。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode) | 返回屏幕管理接口的通用状态码，具体可见[NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode)。 |

#### \[h2\]OH\_NativeDisplayManager\_DestroyAllDisplays()

```c
void OH_NativeDisplayManager_DestroyAllDisplays(NativeDisplayManager_DisplaysInfo *allDisplays)
```

**描述**

销毁所有屏幕的信息对象。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [NativeDisplayManager\_DisplaysInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-displaysinfo) \*allDisplays | 销毁通过[OH\_NativeDisplayManager\_CreateAllDisplays](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-manager-h#oh_nativedisplaymanager_createalldisplays)接口获取的所有的屏幕信息，具体可见[NativeDisplayManager\_DisplaysInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-displaysinfo)。 |

#### \[h2\]OH\_NativeDisplayManager\_CreateDisplayById()

```c
NativeDisplayManager_ErrorCode OH_NativeDisplayManager_CreateDisplayById(uint32_t displayId,NativeDisplayManager_DisplayInfo **displayInfo)
```

**描述**

获取指定屏幕的信息对象。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| uint32\_t displayId | 指定屏幕的id编号，该值为非负整数。 |
| [NativeDisplayManager\_DisplayInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-displayinfo) \*\*displayInfo | 指定的屏幕信息对象，具体可见[NativeDisplayManager\_DisplayInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-displayinfo)，此处作为出参返回。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode) | 返回屏幕管理接口的通用状态码，具体可见[NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode)。 |

#### \[h2\]OH\_NativeDisplayManager\_DestroyDisplay()

```c
void OH_NativeDisplayManager_DestroyDisplay(NativeDisplayManager_DisplayInfo *displayInfo)
```

**描述**

销毁指定屏幕的信息对象。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [NativeDisplayManager\_DisplayInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-displayinfo) \*displayInfo | 销毁通过[OH\_NativeDisplayManager\_CreateDisplayById](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-manager-h#oh_nativedisplaymanager_createdisplaybyid)或者[OH\_NativeDisplayManager\_CreatePrimaryDisplay](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-manager-h#oh_nativedisplaymanager_createprimarydisplay)接口获取到的屏幕信息，具体可见[NativeDisplayManager\_DisplayInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-displayinfo)。 |

#### \[h2\]OH\_NativeDisplayManager\_CreatePrimaryDisplay()

```c
NativeDisplayManager_ErrorCode OH_NativeDisplayManager_CreatePrimaryDisplay(NativeDisplayManager_DisplayInfo **displayInfo)
```

**描述**

获取主屏信息对象。除2in1之外的设备获取的是设备自带屏幕的屏幕信息；2in1设备外接屏幕时获取的是当前主屏幕的屏幕信息；2in1设备没有外接屏幕时获取的是自带屏幕的屏幕信息。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [NativeDisplayManager\_DisplayInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-displayinfo) \*\*displayInfo | 主屏的屏幕信息对象，具体可见[NativeDisplayManager\_DisplayInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-displayinfo)，此处作为出参返回。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode) | 返回屏幕管理接口的通用状态码，具体可见[NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode)。 |

#### \[h2\]OH\_NativeDisplayManager\_AvailableAreaChangeCallback()

```c
typedef void (*OH_NativeDisplayManager_AvailableAreaChangeCallback)(uint64_t displayId)
```

**描述**

注册屏幕可用区域变化的回调函数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| uint64\_t displayId | 屏幕的id号，非负整数。 |

#### \[h2\]OH\_NativeDisplayManager\_RegisterAvailableAreaChangeListener()

```c
NativeDisplayManager_ErrorCode OH_NativeDisplayManager_RegisterAvailableAreaChangeListener(OH_NativeDisplayManager_AvailableAreaChangeCallback availableAreaChangeCallback, uint32_t *listenerIndex)
```

**描述**

注册屏幕可用区域变化监听。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_NativeDisplayManager\_AvailableAreaChangeCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-manager-h#oh_nativedisplaymanager_availableareachangecallback) availableAreaChangeCallback | 
屏幕可用区域变化后触发的回调函数，

回调函数定义见[OH\_NativeDisplayManager\_AvailableAreaChangeCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-manager-h#oh_nativedisplaymanager_availableareachangecallback)。

 |
| uint32\_t \*listenerIndex | 

注册成功后返回的监听编号，

调用取消注册函数[OH\_NativeDisplayManager\_UnregisterAvailableAreaChangeListener](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-manager-h#oh_nativedisplaymanager_unregisteravailableareachangelistener)时作为入参使用，此处作为出参返回。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode) | 返回屏幕管理接口的通用状态码，具体可见[NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode)。 |

#### \[h2\]OH\_NativeDisplayManager\_UnregisterAvailableAreaChangeListener()

```c
NativeDisplayManager_ErrorCode OH_NativeDisplayManager_UnregisterAvailableAreaChangeListener(uint32_t listenerIndex)
```

**描述**

取消屏幕可用区域变化的监听。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| uint32\_t listenerIndex | 
调用注册函数

[OH\_NativeDisplayManager\_RegisterAvailableAreaChangeListener](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-manager-h#oh_nativedisplaymanager_registeravailableareachangelistener)时获取到的监听编号。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode) | 返回屏幕管理接口的通用状态码，具体可见[NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode)。 |

#### \[h2\]OH\_NativeDisplayManager\_CreateAvailableArea()

```c
NativeDisplayManager_ErrorCode OH_NativeDisplayManager_CreateAvailableArea(uint64_t displayId, NativeDisplayManager_Rect **availableArea)
```

**描述**

获取屏幕的可用区域。

**起始版本：** 20

**设备行为差异：** 该接口在2in1设备、Tablet设备中可正常调用；在其他设备中不可用，请通过[OH\_NativeDisplayManager\_GetDefaultDisplayWidth()](#oh_nativedisplaymanager_getdefaultdisplaywidth)、[OH\_NativeDisplayManager\_GetDefaultDisplayHeight()](#oh_nativedisplaymanager_getdefaultdisplayheight)获取当前设备屏幕的可用区域。

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| uint64\_t displayId | 查询屏幕的id号，非负整数。 |
| [NativeDisplayManager\_Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-rect) \*\*availableArea | 屏幕可用区域，具体可见[NativeDisplayManager\_Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-rect)，此处作为出参返回。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode) | 返回屏幕管理接口的通用状态码，具体可见[NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode)。 |

#### \[h2\]OH\_NativeDisplayManager\_DestroyAvailableArea()

```c
NativeDisplayManager_ErrorCode OH_NativeDisplayManager_DestroyAvailableArea(NativeDisplayManager_Rect *availableArea)
```

**描述**

销毁屏幕的可用区域。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [NativeDisplayManager\_Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-rect) \*availableArea | 
销毁通过[OH\_NativeDisplayManager\_CreateAvailableArea](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-manager-h#oh_nativedisplaymanager_createavailablearea)获取的屏幕可用区域，

可用区域定义具体可见[NativeDisplayManager\_Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-rect)。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode) | 返回屏幕管理接口的通用状态码，具体可见[NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode)。 |

#### \[h2\]OH\_NativeDisplayManager\_DisplayAddCallback()

```c
typedef void (*OH_NativeDisplayManager_DisplayAddCallback)(uint64_t displayId)
```

**描述**

注册屏幕连接的回调函数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| uint64\_t displayId | 新增屏幕的id号，非负整数。 |

#### \[h2\]OH\_NativeDisplayManager\_RegisterDisplayAddListener()

```c
NativeDisplayManager_ErrorCode OH_NativeDisplayManager_RegisterDisplayAddListener(OH_NativeDisplayManager_DisplayAddCallback displayAddCallback, uint32_t *listenerIndex)
```

**描述**

注册屏幕连接变化监听（如插入显示器）。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_NativeDisplayManager\_DisplayAddCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-manager-h#oh_nativedisplaymanager_displayaddcallback) displayAddCallback | 屏幕连接后触发的回调函数，回调函数定义见[OH\_NativeDisplayManager\_DisplayAddCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-manager-h#oh_nativedisplaymanager_displayaddcallback)。 |
| uint32\_t \*listenerIndex | 
注册成功后返回的监听编号，

调用取消注册函数[OH\_NativeDisplayManager\_UnregisterDisplayAddListener](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-manager-h#oh_nativedisplaymanager_unregisterdisplayaddlistener)时作为入参使用，此处作为出参返回。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode) | 返回屏幕管理接口的通用状态码，具体可见[NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode)。 |

#### \[h2\]OH\_NativeDisplayManager\_UnregisterDisplayAddListener()

```c
NativeDisplayManager_ErrorCode OH_NativeDisplayManager_UnregisterDisplayAddListener(uint32_t listenerIndex)
```

**描述**

取消屏幕连接的监听。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| uint32\_t listenerIndex | 调用注册函数[OH\_NativeDisplayManager\_RegisterDisplayAddListener](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-manager-h#oh_nativedisplaymanager_registerdisplayaddlistener)时获取到的监听编号。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode) | 返回屏幕管理接口的通用状态码，具体可见[NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode)。 |

#### \[h2\]OH\_NativeDisplayManager\_DisplayRemoveCallback()

```c
typedef void (*OH_NativeDisplayManager_DisplayRemoveCallback)(uint64_t displayId)
```

**描述**

注册屏幕移除的回调函数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| uint64\_t displayId | 被移除屏幕的id号，非负整数。 |

#### \[h2\]OH\_NativeDisplayManager\_RegisterDisplayRemoveListener()

```c
NativeDisplayManager_ErrorCode OH_NativeDisplayManager_RegisterDisplayRemoveListener(OH_NativeDisplayManager_DisplayRemoveCallback displayRemoveCallback, uint32_t *listenerIndex)
```

**描述**

注册屏幕移除变化监听（如移除显示器）。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_NativeDisplayManager\_DisplayRemoveCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-manager-h#oh_nativedisplaymanager_displayremovecallback) displayRemoveCallback | 屏幕移除后触发的回调函数，回调函数定义见[OH\_NativeDisplayManager\_DisplayRemoveCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-manager-h#oh_nativedisplaymanager_displayremovecallback)。 |
| uint32\_t \*listenerIndex | 
注册成功后返回的监听编号，

调用取消注册函数[OH\_NativeDisplayManager\_UnregisterDisplayRemoveListener](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-manager-h#oh_nativedisplaymanager_unregisterdisplayremovelistener)时作为入参使用，此处作为出参返回。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode) | 返回屏幕管理接口的通用状态码，具体可见[NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode)。 |

#### \[h2\]OH\_NativeDisplayManager\_UnregisterDisplayRemoveListener()

```c
NativeDisplayManager_ErrorCode OH_NativeDisplayManager_UnregisterDisplayRemoveListener(uint32_t listenerIndex)
```

**描述**

取消屏幕移除的监听。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| uint32\_t listenerIndex | 调用注册函数[OH\_NativeDisplayManager\_RegisterDisplayRemoveListener](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-manager-h#oh_nativedisplaymanager_registerdisplayremovelistener)时获取到的监听编号。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode) | 返回屏幕管理接口的通用状态码，具体可见[NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode)。 |

#### \[h2\]OH\_NativeDisplayManager\_GetDisplaySourceMode()

```c
NativeDisplayManager_ErrorCode OH_NativeDisplayManager_GetDisplaySourceMode(uint64_t displayId, NativeDisplayManager_SourceMode *sourceMode)
```

**描述**

获取屏幕的显示模式。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| uint64\_t displayId | 查询屏幕的id号，非负整数。 |
| [NativeDisplayManager\_SourceMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_sourcemode) \*sourceMode | 屏幕当前的显示模式，具体可见[NativeDisplayManager\_SourceMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_sourcemode)，此处作为出参返回。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode) | 返回屏幕管理接口的通用状态码，具体可见[NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode)。 |

#### \[h2\]OH\_NativeDisplayManager\_GetDisplayPosition()

```c
NativeDisplayManager_ErrorCode OH_NativeDisplayManager_GetDisplayPosition(uint64_t displayId, int32_t *x, int32_t *y)
```

**描述**

获取屏幕的位置信息。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| uint64\_t displayId | 查询屏幕的id号，非负整数。 |
| int32\_t \*x | 相对于主屏左上角的x方向坐标，此处作为出参返回。 |
| int32\_t \*y | 相对于主屏左上角的y方向坐标，此处作为出参返回。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode) | 
返回屏幕管理接口的通用状态码，具体可见[NativeDisplayManager\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h#nativedisplaymanager_errorcode)。

当前仅支持主屏幕和扩展屏幕查询屏幕位置信息，其他屏幕查询会返回DISPLAY\_MANAGER\_ERROR\_ILLEGAL\_PARAM。

 |

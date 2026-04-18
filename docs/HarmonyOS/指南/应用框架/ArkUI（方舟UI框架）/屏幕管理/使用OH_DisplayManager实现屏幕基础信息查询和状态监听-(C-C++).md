---
title: "使用OH_DisplayManager实现屏幕基础信息查询和状态监听 (C/C++)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-display-manager"
menu_path:
  - "指南"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "屏幕管理"
  - "使用OH_DisplayManager实现屏幕基础信息查询和状态监听 (C/C++)"
captured_at: "2026-04-17T01:35:41.845Z"
---

# 使用OH\_DisplayManager实现屏幕基础信息查询和状态监听 (C/C++)

#### 场景介绍

[OH\_DisplayManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-displaymanager)屏幕管理模块用于提供屏幕的信息查询、屏幕状态变化监听、折叠设备的折叠状态变化监听等能力，应用可根据对应的屏幕信息、屏幕状态变化、屏幕折叠状态适配不同的UI界面显示。

-   支持查询的屏幕信息，包括屏幕的分辨率、物理像素密度、逻辑像素密度、刷新率、屏幕尺寸、屏幕旋转方向、屏幕旋转角度等。
    
-   支持屏幕状态变化的监听，包括屏幕旋转变化，屏幕分辨率变化、屏幕刷新率变化等。
    
-   支持查询当前设备是否为可折叠设备，同时支持折叠状态（展开/折叠）变化的监听。
    

#### 基本概念

-   屏幕的物理像素密度(densityDPI)：代表每英寸屏幕所拥有的物理像素点数。
    
-   屏幕的逻辑像素的密度(densityPixels)：代表物理像素与逻辑像素的缩放系数比，计算方法为物理像素密度除以160。
    

#### 接口说明

常用接口如下表所示。更多API说明请参考[OH\_DisplayManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-displaymanager)。

| 接口名 | 描述 |
| :-- | :-- |
| OH\_NativeDisplayManager\_GetDefaultDisplayRotation(NativeDisplayManager\_Rotation \*displayRotation) | 获取默认屏幕的旋转角度。 |
| OH\_NativeDisplayManager\_CreateDefaultDisplayCutoutInfo(NativeDisplayManager\_CutoutInfo \*\*cutoutInfo) | 获取挖孔屏、刘海屏、瀑布屏等不可用屏幕区域信息。 |
| OH\_NativeDisplayManager\_DestroyDefaultDisplayCutoutInfo(NativeDisplayManager\_CutoutInfo \*cutoutInfo) | 销毁挖孔屏、刘海屏、瀑布屏等不可用屏幕区域信息。 |
| OH\_NativeDisplayManager\_IsFoldable() | 查询设备是否可折叠。 |
| OH\_NativeDisplayManager\_RegisterDisplayChangeListener( OH\_NativeDisplayManager\_DisplayChangeCallback displayChangeCallback, uint32\_t \*listenerIndex) | 注册屏幕状态变化监听（如旋转变化、刷新率、DPI、分辨率等）。 |
| OH\_NativeDisplayManager\_UnregisterDisplayChangeListener(uint32\_t listenerIndex) | 取消屏幕状态变化监听。 |
| OH\_NativeDisplayManager\_RegisterFoldDisplayModeChangeListener( OH\_NativeDisplayManager\_FoldDisplayModeChangeCallback displayModeChangeCallback, uint32\_t \*listenerIndex) | 注册屏幕展开、折叠状态变化监听。 |
| OH\_NativeDisplayManager\_UnregisterFoldDisplayModeChangeListener(uint32\_t listenerIndex) | 取消屏幕展开、折叠状态变化监听。 |

#### 在CMake脚本中链接动态库

```text
target_link_libraries(entry PUBLIC libhilog_ndk.z.so)
target_link_libraries(entry PUBLIC libnative_display_manager.so )
```

#### 添加头文件

#include <window\_manager/oh\_display\_info.h>
#include <window\_manager/oh\_display\_manager.h>
#include <hilog/log.h>

#### 获取屏幕状态

1.  可以通过OH\_NativeDisplayManager\_GetDefaultDisplayRotation获取默认屏幕的旋转角度。
    
    static napi\_value GetDefaultDisplayRotation(napi\_env env, napi\_callback\_info info)
    {
        NativeDisplayManager\_Rotation displayRotation;
        NativeDisplayManager\_ErrorCode errCode = OH\_NativeDisplayManager\_GetDefaultDisplayRotation(&displayRotation);
        if (errCode == NativeDisplayManager\_ErrorCode::DISPLAY\_MANAGER\_OK) {
            napi\_value rotation;
            napi\_create\_int32(env, displayRotation, &rotation);
            OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "DMSTest", "rotation=%{public}d", displayRotation);
            return rotation;
        } else {
            napi\_value errorCode;
            napi\_create\_int32(env, errCode, &errorCode);
            OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "DMSTest",
                "GetDefaultDisplayRotation errCode=%{public}d", errCode);
            return errorCode;
        }
    }
    
2.  可以通过OH\_NativeDisplayManager\_CreateDefaultDisplayCutoutInfo获取挖孔屏、刘海屏、瀑布屏等不可用屏幕区域信息。 可通过OH\_NativeDisplayManager\_DestroyDefaultDisplayCutoutInfo销毁挖孔屏、刘海屏、瀑布屏等不可用屏幕区域信息。
    
    static napi\_value CreateDefaultDisplayCutoutInfo(napi\_env env, napi\_callback\_info info)
    {
        NativeDisplayManager\_CutoutInfo \*cutOutInfo = NULL;
        NativeDisplayManager\_ErrorCode errCode = OH\_NativeDisplayManager\_CreateDefaultDisplayCutoutInfo(&cutOutInfo);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "DMSTest", "GetDefaultCutoutInfo errCode=%{public}d", errCode);
        if (errCode == NativeDisplayManager\_ErrorCode::DISPLAY\_MANAGER\_OK) {
            if (cutOutInfo != NULL && cutOutInfo->boundingRectsLength != 0) {
                OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "DMSTest",
                    "GetDefaultCutoutInfo cutOutInfo length=%{public}d", cutOutInfo->boundingRectsLength);
                for (int i = 0; i < cutOutInfo->boundingRectsLength; i++) {
                    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "DMSTest",
                        "cutOutInfo\[%{public}d\]=\[%{public}d %{public}d %{public}d %{public}d\]",
                        i, cutOutInfo->boundingRects\[i\].left, cutOutInfo->boundingRects\[i\].top,
                        cutOutInfo->boundingRects\[i\].width, cutOutInfo->boundingRects\[i\].height);
                }
                OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "DMSTest",
                    "cutOutInfo waterfall left rect=\[%{public}d %{public}d %{public}d %{public}d\]",
                    cutOutInfo->waterfallDisplayAreaRects.left.left, cutOutInfo->waterfallDisplayAreaRects.left.top,
                    cutOutInfo->waterfallDisplayAreaRects.left.width, cutOutInfo->waterfallDisplayAreaRects.left.height);
                OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "DMSTest",
                    "cutOutInfo waterfall top rect=\[%{public}d %{public}d %{public}d %{public}d\]",
                    cutOutInfo->waterfallDisplayAreaRects.top.left, cutOutInfo->waterfallDisplayAreaRects.top.top,
                    cutOutInfo->waterfallDisplayAreaRects.top.width, cutOutInfo->waterfallDisplayAreaRects.top.height);
                OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "DMSTest",
                    "cutOutInfo waterfall right rect=\[%{public}d %{public}d %{public}d %{public}d\]",
                    cutOutInfo->waterfallDisplayAreaRects.right.left, cutOutInfo->waterfallDisplayAreaRects.right.top,
                    cutOutInfo->waterfallDisplayAreaRects.right.width, cutOutInfo->waterfallDisplayAreaRects.right.height);
                OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "DMSTest",
                    "cutOutInfo waterfall bottom rect=\[%{public}d %{public}d %{public}d %{public}d\]",
                    cutOutInfo->waterfallDisplayAreaRects.bottom.left,
                    cutOutInfo->waterfallDisplayAreaRects.bottom.top,
                    cutOutInfo->waterfallDisplayAreaRects.bottom.width,
                    cutOutInfo->waterfallDisplayAreaRects.bottom.height);
            }
            napi\_value boundingRectsLength;
            napi\_create\_int32(env, cutOutInfo->boundingRectsLength, &boundingRectsLength);
            OH\_NativeDisplayManager\_DestroyDefaultDisplayCutoutInfo(cutOutInfo);
            return boundingRectsLength;
        } else {
            napi\_value errorCode;
            napi\_create\_int32(env, errCode, &errorCode);
            return errorCode;
        }
    }
    

#### 监听屏幕状态变化

可以通过OH\_NativeDisplayManager\_RegisterDisplayChangeListener接口注册屏幕变化的监听，包括屏幕旋转、分辨率变化、刷新率变化、DPI变化等。 通过OH\_NativeDisplayManager\_UnregisterDisplayChangeListener接口取消屏幕状态变化的监听。

void DisplayChangeCallback(uint64\_t displayId)
{
    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "DMSTest",
        "DisplayChangeCallback displayId=%{public}lu.", displayId);
}

static napi\_value RegisterDisplayChangeListener(napi\_env env, napi\_callback\_info info)
{
    uint32\_t listenerIndex;
    NativeDisplayManager\_ErrorCode errCode = OH\_NativeDisplayManager\_RegisterDisplayChangeListener(
        DisplayChangeCallback, &listenerIndex);
    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "DMSTest",
        "RegisterDisplayChangeListener listenerIndex =%{public}d errCode=%{public}d.", listenerIndex, errCode);
    if (errCode == NativeDisplayManager\_ErrorCode::DISPLAY\_MANAGER\_OK) {
        napi\_value registerIndex;
        napi\_create\_int32(env, listenerIndex, &registerIndex);
        return registerIndex;
    } else {
        napi\_value errorCode;
        napi\_create\_int32(env, errCode, &errorCode);
        return errorCode;
    }
}

static napi\_value UnregisterDisplayChangeListener(napi\_env env, napi\_callback\_info info)
{
    size\_t argc = 1;
    napi\_value args\[1\] = { nullptr };

    uint32\_t listenerIndex;
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    napi\_get\_value\_uint32(env, args\[0\], &listenerIndex);
    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "DMSTest",
        "UnregisterDisplayChangeListener listenerIndex =%{public}d.", listenerIndex);
    NativeDisplayManager\_ErrorCode errCode = OH\_NativeDisplayManager\_UnregisterDisplayChangeListener(listenerIndex);
    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "DMSTest",
        "UnregisterDisplayChangeListener errCode=%{public}d.", errCode);
    napi\_value errorCode;
    napi\_create\_int32(env, errCode, &errorCode);
    return errorCode;
}

#### 监听折叠设备状态变化

1.  可以通过OH\_NativeDisplayManager\_IsFoldable接口查询设备是不是折叠设备。
    
    static napi\_value IsFoldable(napi\_env env, napi\_callback\_info info)
    {
        bool isFoldDevice = OH\_NativeDisplayManager\_IsFoldable();
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "DMSTest", "IsFoldable isFoldDevice =%{public}d.", isFoldDevice);
        napi\_value isFold;
        napi\_get\_boolean(env, isFoldDevice, &isFold);
        return isFold;
    }
    
2.  可以通过OH\_NativeDisplayManager\_RegisterFoldDisplayModeChangeListener注册屏幕展开/折叠状态变化的监听。 通过OH\_NativeDisplayManager\_UnregisterFoldDisplayModeChangeListener接口取消屏幕展开/折叠状态变化的监听。
    
    void FoldDisplayModeChangeCallback(NativeDisplayManager\_FoldDisplayMode displayMode)
    {
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "DMSTest", "displayMode=%{public}d.", displayMode);
    }
    
    static napi\_value RegisterFoldDisplayModeChangeListener(napi\_env env, napi\_callback\_info info)
    {
        uint32\_t listenerIndex = 0;
        NativeDisplayManager\_ErrorCode errCode = OH\_NativeDisplayManager\_RegisterFoldDisplayModeChangeListener(
            FoldDisplayModeChangeCallback, &listenerIndex);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "DMSTest", "listenerIndex =%{public}d errCode=%{public}d.",
            listenerIndex, errCode);
        if (errCode == NativeDisplayManager\_ErrorCode::DISPLAY\_MANAGER\_OK) {
            napi\_value registerIndex;
            napi\_create\_int32(env, listenerIndex, &registerIndex);
            return registerIndex;
        } else {
            napi\_value errorCode;
            napi\_create\_int32(env, errCode, &errorCode);
            return errorCode;
        }
    }
    
    static napi\_value UnregisterFoldDisplayModeChangeListener(napi\_env env, napi\_callback\_info info)
    {
        size\_t argc = 1;
        napi\_value args\[1\] = { nullptr };
        uint32\_t listenerIndex;
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
        napi\_get\_value\_uint32(env, args\[0\], &listenerIndex);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "DMSTest", "listenerIndex =%{public}d.", listenerIndex);
        NativeDisplayManager\_ErrorCode errCode =
            OH\_NativeDisplayManager\_UnregisterFoldDisplayModeChangeListener(listenerIndex);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "DMSTest", "errorCode=%{public}d", errCode);
        napi\_value errorCode;
        napi\_create\_int32(env, errCode, &errorCode);
        return errorCode;
    }
    

#### 注册函数

EXTERN\_C\_START
static napi\_value Init(napi\_env env, napi\_value exports)
{
    napi\_property\_descriptor desc\[\] = {
        {"getDisplayRotation", nullptr, GetDefaultDisplayRotation, nullptr, nullptr, nullptr, napi\_default, nullptr},
        {"getCutoutInfo", nullptr, CreateDefaultDisplayCutoutInfo, nullptr, nullptr, nullptr, napi\_default, nullptr},
        {"registerDisplayChange", nullptr, RegisterDisplayChangeListener,
            nullptr, nullptr, nullptr, napi\_default, nullptr},
        {"unregisterDisplayChange", nullptr, UnregisterDisplayChangeListener,
            nullptr, nullptr, nullptr, napi\_default, nullptr},
        {"checkIsFoldDevice", nullptr, IsFoldable, nullptr, nullptr, nullptr, napi\_default, nullptr},
        {"registerFoldDisplayModeChange", nullptr, RegisterFoldDisplayModeChangeListener,
            nullptr, nullptr, nullptr, napi\_default, nullptr},
        {"unregisterFoldDisplayModeChange", nullptr, UnregisterFoldDisplayModeChangeListener,
            nullptr, nullptr, nullptr, napi\_default, nullptr},
    };
    napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
    return exports;
}
EXTERN\_C\_END

#### 注册模块

static napi\_module displayModule = {
    .nm\_version = 1,
    .nm\_flags = 0,
    .nm\_filename = nullptr,
    .nm\_register\_func = Init,
    .nm\_modname = "nativedisplay",
    .nm\_priv = ((void\*)0),
    .reserved = { 0 },
};

extern "C" \_\_attribute\_\_((constructor)) void RegisterEntryModule(void)
{
    napi\_module\_register(&displayModule);
}

```
static napi_module displayModule = {
    .nm_version = 1,
    .nm_flags = 0,
    .nm_filename = nullptr,
    .nm_register_func = Init,
    .nm_modname = "nativedisplay",
    .nm_priv = ((void*)0),
    .reserved = { 0 },
};

extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
{
    napi_module_register(&displayModule);
}
```

#### 在Index.ets文件中调用函数

private callGetDisplayRotation(): void {
  this.promptAction.openToast({ message: '调用getDisplayRotation方法' }).catch((error: Error) => {
    console.error(\`callGetDisplayRotation error ${JSON.stringify(error)}\`);
  }).then(() => {
    console.info(\`get rotation value is: ${displayNapi.getDisplayRotation()}\`);
  });
}

private callFoldableCallback(): void {
  this.promptAction.openToast({ message: '调用register displayMode方法' }).catch((error: Error) => {
    console.error(\`callFoldableCallback error ${JSON.stringify(error)}\`);
  }).then(() => {
    let registerIndex = displayNapi.registerFoldDisplayModeChange();
    console.info(\`register foldable value is: ${registerIndex}\`);
    console.info(\`unregister foldable value is: ${displayNapi.unregisterFoldDisplayModeChange(registerIndex)}\`);
  });
}

private callGetCutoutInfo(): void {
  this.promptAction.openToast({ message: '调用getCutoutInfo方法' }).catch((error: Error) => {
    console.error(\`callGetCutoutInfo error ${JSON.stringify(error)}\`);
  }).then(() => {
    console.info(\`cutoutInfo length is: ${displayNapi.getCutoutInfo()}\`);
  });
}

private callDealListenCallback(): void {
  this.promptAction.openToast({ message: '调用register change方法' }).catch((error: Error) => {
    console.error(\`callDealListenCallback error ${JSON.stringify(error)}\`);
  }).then(() => {
    let registerIndex = displayNapi.registerDisplayChange();
    console.info(\`register display change value is: ${registerIndex}\`);
    console.info(\`unregister display change value is: ${displayNapi.unregisterDisplayChange(registerIndex)}\`);
  });
}

private callDealFoldableDevice(): void {
  this.promptAction.openToast({ message: '调用dealFoldableDevice方法' }).catch((error: Error) => {
    console.error(\`callDealFoldableDevice error ${JSON.stringify(error)}\`);
  }).then(() => {
    console.info(\`fold device is: ${displayNapi.checkIsFoldDevice()}\`);
  });
}

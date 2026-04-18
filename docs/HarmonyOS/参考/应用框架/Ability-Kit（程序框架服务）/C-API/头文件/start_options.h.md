---
title: "start_options.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-start-options-h"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "C API"
  - "头文件"
  - "start_options.h"
captured_at: "2026-04-17T01:47:48.633Z"
---

# start\_options.h

#### 概述

提供应用启动参数数据结构[AbilityRuntime\_StartOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-startoptions)以及设置和获取相关函数。

**引用文件：** <AbilityKit/ability\_runtime/start\_options.h>

**库：** libability\_runtime.so

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 17

**相关模块：** [AbilityRuntime](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime)

#### 汇总

#### \[h2\]结构体

| 名称 | typedef关键字 | 描述 |
| :-- | :-- | :-- |
| [AbilityRuntime\_StartOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-startoptions) | AbilityRuntime\_StartOptions | StartOptions数据结构。 |

#### \[h2\]函数

| 名称 | 描述 |
| :-- | :-- |
| [AbilityRuntime\_StartOptions\* OH\_AbilityRuntime\_CreateStartOptions(void)](#oh_abilityruntime_createstartoptions) | 创建AbilityRuntime\_StartOptions对象。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_DestroyStartOptions(AbilityRuntime\_StartOptions \*\*startOptions)](#oh_abilityruntime_destroystartoptions) | 销毁AbilityRuntime\_StartOptions对象。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsWindowMode(AbilityRuntime\_StartOptions \*startOptions,AbilityRuntime\_WindowMode windowMode)](#oh_abilityruntime_setstartoptionswindowmode) | 设置启动Ability时的窗口模式。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsWindowMode(AbilityRuntime\_StartOptions \*startOptions,AbilityRuntime\_WindowMode &windowMode)](#oh_abilityruntime_getstartoptionswindowmode) | 获取启动Ability时的窗口模式。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsDisplayId(AbilityRuntime\_StartOptions \*startOptions,int32\_t displayId)](#oh_abilityruntime_setstartoptionsdisplayid) | 设置启动Ability时窗口所在的屏幕ID。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsDisplayId(AbilityRuntime\_StartOptions \*startOptions,int32\_t &displayId)](#oh_abilityruntime_getstartoptionsdisplayid) | 获取启动Ability时窗口所在的屏幕ID。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsWithAnimation(AbilityRuntime\_StartOptions \*startOptions,bool withAnimation)](#oh_abilityruntime_setstartoptionswithanimation) | 设置启动Ability时是否具有动画效果。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsWithAnimation(AbilityRuntime\_StartOptions \*startOptions,bool &withAnimation)](#oh_abilityruntime_getstartoptionswithanimation) | 获取启动Ability时是否具有动画效果。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsWindowLeft(AbilityRuntime\_StartOptions \*startOptions,int32\_t windowLeft)](#oh_abilityruntime_setstartoptionswindowleft) | 设置启动Ability时的窗口左侧位置，单位为px。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsWindowLeft(AbilityRuntime\_StartOptions \*startOptions,int32\_t &windowLeft)](#oh_abilityruntime_getstartoptionswindowleft) | 获取启动Ability时的窗口左侧位置，单位为px。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsWindowTop(AbilityRuntime\_StartOptions \*startOptions,int32\_t windowTop)](#oh_abilityruntime_setstartoptionswindowtop) | 设置启动Ability时的窗口顶部位置，单位为px。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsWindowTop(AbilityRuntime\_StartOptions \*startOptions,int32\_t &windowTop)](#oh_abilityruntime_getstartoptionswindowtop) | 获取启动Ability时的窗口顶部位置，单位为px。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsWindowHeight(AbilityRuntime\_StartOptions \*startOptions,int32\_t windowHeight)](#oh_abilityruntime_setstartoptionswindowheight) | 设置启动Ability时的窗口高度，单位为px。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsWindowHeight(AbilityRuntime\_StartOptions \*startOptions,int32\_t &windowHeight)](#oh_abilityruntime_getstartoptionswindowheight) | 获取启动Ability时的窗口高度，单位为px。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsWindowWidth(AbilityRuntime\_StartOptions \*startOptions,int32\_t windowWidth)](#oh_abilityruntime_setstartoptionswindowwidth) | 设置启动Ability时的窗口宽度，单位为px。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsWindowWidth(AbilityRuntime\_StartOptions \*startOptions,int32\_t &windowWidth)](#oh_abilityruntime_getstartoptionswindowwidth) | 获取启动Ability时的窗口宽度，单位为px。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsStartVisibility(AbilityRuntime\_StartOptions \*startOptions,AbilityRuntime\_StartVisibility startVisibility)](#oh_abilityruntime_setstartoptionsstartvisibility) | 设置启动Ability时窗口和dock栏图标的显示模式。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsStartVisibility(AbilityRuntime\_StartOptions \*startOptions,AbilityRuntime\_StartVisibility &startVisibility)](#oh_abilityruntime_getstartoptionsstartvisibility) | 获取启动Ability时窗口和dock栏图标的显示模式。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsStartWindowIcon(AbilityRuntime\_StartOptions \*startOptions,OH\_PixelmapNative \*startWindowIcon)](#oh_abilityruntime_setstartoptionsstartwindowicon) | 设置启动Ability时的窗口启动图标。图片数据大小限制为600M。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsStartWindowIcon(AbilityRuntime\_StartOptions \*startOptions,OH\_PixelmapNative \*\*startWindowIcon)](#oh_abilityruntime_getstartoptionsstartwindowicon) | 获取启动Ability时的窗口启动图标。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsStartWindowBackgroundColor(AbilityRuntime\_StartOptions \*startOptions, const char \*startWindowBackgroundColor)](#oh_abilityruntime_setstartoptionsstartwindowbackgroundcolor) | 设置启动Ability时的窗口背景颜色。如果未设置该字段，则默认采用module.json5配置文件中abilities标签的startWindowBackground字段的配置。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsStartWindowBackgroundColor(AbilityRuntime\_StartOptions \*startOptions, char \*\*startWindowBackgroundColor, size\_t &size)](#oh_abilityruntime_getstartoptionsstartwindowbackgroundcolor) | 获取启动Ability时的窗口背景颜色。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsSupportedWindowModes(AbilityRuntime\_StartOptions \*startOptions, AbilityRuntime\_SupportedWindowMode \*supportedWindowModes,size\_t size)](#oh_abilityruntime_setstartoptionssupportedwindowmodes) | 设置启动Ability时的组件所支持的窗口模式。如果未配置该字段，则默认采用该UIAbility对应的module.json5配置文件中abilities标签的supportWindowMode字段取值。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsSupportedWindowModes(AbilityRuntime\_StartOptions \*startOptions, AbilityRuntime\_SupportedWindowMode \*\*supportedWindowModes,size\_t &size)](#oh_abilityruntime_getstartoptionssupportedwindowmodes) | 获取启动Ability时的组件所支持的窗口模式。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsMinWindowWidth(AbilityRuntime\_StartOptions \*startOptions, int32\_t minWindowWidth)](#oh_abilityruntime_setstartoptionsminwindowwidth) | 设置启动Ability时的窗口最小宽度，单位为vp。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsMinWindowWidth(AbilityRuntime\_StartOptions \*startOptions, int32\_t &minWindowWidth)](#oh_abilityruntime_getstartoptionsminwindowwidth) | 获取启动Ability时的窗口最小宽度，单位为vp。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsMaxWindowWidth(AbilityRuntime\_StartOptions \*startOptions, int32\_t maxWindowWidth)](#oh_abilityruntime_setstartoptionsmaxwindowwidth) | 设置启动Ability时的窗口最大宽度，单位为vp。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsMaxWindowWidth(AbilityRuntime\_StartOptions \*startOptions, int32\_t &maxWindowWidth)](#oh_abilityruntime_getstartoptionsmaxwindowwidth) | 获取启动Ability时的窗口最大宽度，单位为vp。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsMinWindowHeight(AbilityRuntime\_StartOptions \*startOptions, int32\_t minWindowHeight)](#oh_abilityruntime_setstartoptionsminwindowheight) | 设置启动Ability时的窗口最小高度，单位为vp。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsMinWindowHeight(AbilityRuntime\_StartOptions \*startOptions, int32\_t &minWindowHeight)](#oh_abilityruntime_getstartoptionsminwindowheight) | 获取启动Ability时的窗口最小高度，单位为vp。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_SetStartOptionsMaxWindowHeight(AbilityRuntime\_StartOptions \*startOptions, int32\_t maxWindowHeight)](#oh_abilityruntime_setstartoptionsmaxwindowheight) | 设置启动Ability时的窗口最大高度，单位为vp。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetStartOptionsMaxWindowHeight(AbilityRuntime\_StartOptions \*startOptions, int32\_t &maxWindowHeight)](#oh_abilityruntime_getstartoptionsmaxwindowheight) | 获取启动Ability时的窗口最大高度，单位为vp。 |

#### 函数说明

#### \[h2\]OH\_AbilityRuntime\_CreateStartOptions()

```c
AbilityRuntime_StartOptions* OH_AbilityRuntime_CreateStartOptions(void)
```

**描述**

创建[AbilityRuntime\_StartOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-startoptions)对象。

**起始版本：** 17

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-startoptions)\* | 返回指针类型AbilityRuntime\_StartOptions对象。 |

**示例代码：**

```cpp
#include <AbilityKit/ability_runtime/start_options.h>

void createStartOptionsTest()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### \[h2\]OH\_AbilityRuntime\_DestroyStartOptions()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_DestroyStartOptions(AbilityRuntime_StartOptions **startOptions)
```

**描述**

销毁[AbilityRuntime\_StartOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-startoptions)对象。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-startoptions) \*\*startOptions | 需要销毁的AbilityRuntime\_StartOptions对象。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-runtime-common-h#abilityruntime_errorcode) | 
在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。

在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。

 |

**示例代码：**

```cpp
#include <AbilityKit/ability_runtime/start_options.h>

void destroyStartOptionsTest()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### \[h2\]OH\_AbilityRuntime\_SetStartOptionsWindowMode()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsWindowMode(AbilityRuntime_StartOptions *startOptions,AbilityRuntime_WindowMode windowMode)
```

**描述**

设置启动Ability时的窗口模式。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-startoptions) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| [AbilityRuntime\_WindowMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-context-constant-h#abilityruntime_windowmode) windowMode | 启动Ability时的窗口模式。取值范围参见AbilityRuntime\_WindowMode。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-runtime-common-h#abilityruntime_errorcode) | 
在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。

在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空或者WindowMode无效。

 |

**示例代码：**

```cpp
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsWindowMode(options,
        ABILITY_RUNTIME_WINDOW_MODE_FULL_SCREEN);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### \[h2\]OH\_AbilityRuntime\_GetStartOptionsWindowMode()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsWindowMode(AbilityRuntime_StartOptions *startOptions,AbilityRuntime_WindowMode &windowMode)
```

**描述**

获取启动Ability时的窗口模式。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-startoptions) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| [AbilityRuntime\_WindowMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-context-constant-h#abilityruntime_windowmode) windowMode | 启动Ability时的窗口模式。取值范围参见AbilityRuntime\_WindowMode。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-runtime-common-h#abilityruntime_errorcode) | 
在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。

在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。

 |

**示例代码：**

```cpp
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    AbilityRuntime_WindowMode windowMode = ABILITY_RUNTIME_WINDOW_MODE_UNDEFINED;
    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsWindowMode(options, windowMode);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### \[h2\]OH\_AbilityRuntime\_SetStartOptionsDisplayId()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsDisplayId(AbilityRuntime_StartOptions *startOptions,int32_t displayId)
```

**描述**

设置启动Ability时窗口所在的屏幕ID。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-startoptions) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| int32\_t displayId | 启动Ability时窗口所在的屏幕ID。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-runtime-common-h#abilityruntime_errorcode) | 
在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。

在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。

 |

**示例代码：**

```cpp
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsDisplayId(options, 1);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### \[h2\]OH\_AbilityRuntime\_GetStartOptionsDisplayId()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsDisplayId(AbilityRuntime_StartOptions *startOptions,int32_t &displayId)
```

**描述**

获取启动Ability时窗口所在的屏幕ID。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-startoptions) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| int32\_t &displayId | 启动Ability时窗口所在的屏幕ID。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-runtime-common-h#abilityruntime_errorcode) | 
在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。

在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。

 |

**示例代码：**

```cpp
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    int32_t displayId = 0;
    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsDisplayId(options, displayId);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### \[h2\]OH\_AbilityRuntime\_SetStartOptionsWithAnimation()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsWithAnimation(AbilityRuntime_StartOptions *startOptions,bool withAnimation)
```

**描述**

设置启动Ability时是否具有动画效果。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-startoptions) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| bool withAnimation | 
启动Ability时是否具有动画效果。

true表示启动Ability时具有动画效果；false表示启动Ability时不具有动画效果。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-runtime-common-h#abilityruntime_errorcode) | 
在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。

在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。

 |

**示例代码：**

```cpp
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsWithAnimation(options, true);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### \[h2\]OH\_AbilityRuntime\_GetStartOptionsWithAnimation()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsWithAnimation(AbilityRuntime_StartOptions *startOptions,bool &withAnimation)
```

**描述**

获取启动Ability时是否具有动画效果。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-startoptions) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| bool &withAnimation | 
启动Ability时是否具有动画效果。

true表示启动Ability时具有动画效果；false表示启动Ability时不具有动画效果。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-runtime-common-h#abilityruntime_errorcode) | 
在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。

在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。

 |

**示例代码：**

```cpp
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    bool withAnimation = false;
    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsWithAnimation(options, withAnimation);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### \[h2\]OH\_AbilityRuntime\_SetStartOptionsWindowLeft()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsWindowLeft(AbilityRuntime_StartOptions *startOptions,int32_t windowLeft)
```

**描述**

设置启动Ability时的窗口左侧位置，单位为px。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-startoptions) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| int32\_t windowLeft | 启动Ability时的窗口左侧位置，单位为px。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-runtime-common-h#abilityruntime_errorcode) | 
在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。

在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。

 |

**示例代码：**

```cpp
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsWindowLeft(options, 200);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### \[h2\]OH\_AbilityRuntime\_GetStartOptionsWindowLeft()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsWindowLeft(AbilityRuntime_StartOptions *startOptions,int32_t &windowLeft)
```

**描述**

获取启动Ability时的窗口左侧位置，单位为px。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-startoptions) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| int32\_t &windowLeft | 启动Ability时的窗口左侧位置，单位为px。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-runtime-common-h#abilityruntime_errorcode) | 
在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。

在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。

 |

**示例代码：**

```cpp
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    int32_t windowLeft = 0;
    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsWindowLeft(options, windowLeft);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### \[h2\]OH\_AbilityRuntime\_SetStartOptionsWindowTop()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsWindowTop(AbilityRuntime_StartOptions *startOptions,int32_t windowTop)
```

**描述**

设置启动Ability时的窗口顶部位置，单位为px。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-startoptions) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| int32\_t windowTop | 启动Ability时的窗口顶部位置，单位为px。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-runtime-common-h#abilityruntime_errorcode) | 
在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。

在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。

 |

**示例代码：**

```cpp
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsWindowTop(options, 500);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### \[h2\]OH\_AbilityRuntime\_GetStartOptionsWindowTop()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsWindowTop(AbilityRuntime_StartOptions *startOptions,int32_t &windowTop)
```

**描述**

获取启动Ability时的窗口顶部位置，单位为px。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-startoptions) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| int32\_t &windowTop | 启动Ability时的窗口顶部位置，单位为px。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-runtime-common-h#abilityruntime_errorcode) | 
在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。

在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。

 |

**示例代码：**

```cpp
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    int32_t windowTop = 0;
    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsWindowTop(options, windowTop);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### \[h2\]OH\_AbilityRuntime\_SetStartOptionsWindowHeight()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsWindowHeight(AbilityRuntime_StartOptions *startOptions,int32_t windowHeight)
```

**描述**

设置启动Ability时的窗口高度，单位为px。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-startoptions) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| int32\_t windowHeight | 启动Ability时的窗口高度，单位为px。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-runtime-common-h#abilityruntime_errorcode) | 
在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。

在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。

 |

**示例代码：**

```cpp
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsWindowHeight(options, 500);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### \[h2\]OH\_AbilityRuntime\_GetStartOptionsWindowHeight()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsWindowHeight(AbilityRuntime_StartOptions *startOptions,int32_t &windowHeight)
```

**描述**

获取启动Ability时的窗口高度，单位为px。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-startoptions) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| int32\_t &windowHeight | 启动Ability时的窗口高度，单位为px。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-runtime-common-h#abilityruntime_errorcode) | 
在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。

在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。

 |

**示例代码：**

```cpp
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    int32_t windowHeight = 0;
    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsWindowHeight(options, windowHeight);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### \[h2\]OH\_AbilityRuntime\_SetStartOptionsWindowWidth()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsWindowWidth(AbilityRuntime_StartOptions *startOptions,int32_t windowWidth)
```

**描述**

设置启动Ability时的窗口宽度，单位为px。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-startoptions) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| int32\_t windowWidth | 启动Ability时的窗口宽度，单位为px。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-runtime-common-h#abilityruntime_errorcode) | 
在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。

在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。

 |

**示例代码：**

```cpp
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsWindowWidth(options, 500);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### \[h2\]OH\_AbilityRuntime\_GetStartOptionsWindowWidth()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsWindowWidth(AbilityRuntime_StartOptions *startOptions,int32_t &windowWidth)
```

**描述**

获取启动Ability时的窗口宽度，单位为px。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-startoptions) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| int32\_t &windowWidth | 启动Ability时的窗口宽度，单位为px。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-runtime-common-h#abilityruntime_errorcode) | 
在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。

在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。

 |

**示例代码：**

```cpp
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    int32_t windowWidth = 0;
    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsWindowWidth(options, windowWidth);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### \[h2\]OH\_AbilityRuntime\_SetStartOptionsStartVisibility()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsStartVisibility(AbilityRuntime_StartOptions *startOptions,AbilityRuntime_StartVisibility startVisibility)
```

**描述**

设置启动Ability时窗口和dock栏图标的显示模式。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-startoptions) \*startOptions | StartOptions结构体。 |
| [AbilityRuntime\_StartVisibility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-context-constant-h#abilityruntime_startvisibility) startVisibility | 需要设置的显示模式。取值范围参见AbilityRuntime\_StartVisibility。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-runtime-common-h#abilityruntime_errorcode) | 
在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示设置成功。

在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空，或startVisibility取值不在枚举类AbilityRuntime\_StartVisibility中。

 |

**示例代码：**

```cpp
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    AbilityRuntime_StartVisibility visibility = AbilityRuntime_StartVisibility::ABILITY_RUNTIME_SHOW_UPON_START;
    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsStartVisibility(options, visibility);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### \[h2\]OH\_AbilityRuntime\_GetStartOptionsStartVisibility()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsStartVisibility(AbilityRuntime_StartOptions *startOptions,AbilityRuntime_StartVisibility &startVisibility)
```

**描述**

获取启动Ability时窗口和dock栏图标的显示模式。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-startoptions) \*startOptions | StartOptions结构体。 |
| [AbilityRuntime\_StartVisibility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-context-constant-h#abilityruntime_startvisibility) &startVisibility | 获取到的显示模式。取值范围参见AbilityRuntime\_StartVisibility。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-runtime-common-h#abilityruntime_errorcode) | 
在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示获取成功。

在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空，或startVisibility未被设置。

 |

**示例代码：**

```cpp
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    AbilityRuntime_StartVisibility visibility;
    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsStartVisibility(options, visibility);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### \[h2\]OH\_AbilityRuntime\_SetStartOptionsStartWindowIcon()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsStartWindowIcon(AbilityRuntime_StartOptions *startOptions,OH_PixelmapNative *startWindowIcon)
```

**描述**

设置启动Ability时的窗口启动图标。图片数据大小限制为600M。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-startoptions) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| OH\_PixelmapNative \*startWindowIcon | 启动Ability时的窗口启动图标。图片数据大小限制为600M。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-runtime-common-h#abilityruntime_errorcode) | 
在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。

在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空，或者OH\_PixelmapNative没有置为空指针。

 |

**示例代码：**

```cpp
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    uint8_t data[96];
    size_t dataSize = 96;
    for (int i = 0; i < dataSize; i++) {
        data[i] = i + 1;
    }

    // 创建参数结构体实例，并设置参数
    OH_Pixelmap_InitializationOptions *createOpts = nullptr;
    OH_PixelmapInitializationOptions_Create(&createOpts);
    OH_PixelmapInitializationOptions_SetWidth(createOpts, 6);
    OH_PixelmapInitializationOptions_SetHeight(createOpts, 4);
    OH_PixelmapInitializationOptions_SetPixelFormat(createOpts, PIXEL_FORMAT_RGBA_8888);
    OH_PixelmapInitializationOptions_SetAlphaType(createOpts, PIXELMAP_ALPHA_TYPE_UNKNOWN);

    // 创建Pixelmap实例
    OH_PixelmapNative *startWindowIcon = nullptr;
    Image_ErrorCode errCode = OH_PixelmapNative_CreatePixelmap(data, dataSize, createOpts, &startWindowIcon);
    if (errCode != IMAGE_SUCCESS) {
        // 记录错误日志以及其他业务处理

        // 销毁createOpts，防止内存泄漏
        OH_PixelmapInitializationOptions_Release(createOpts);
        return;
    }

    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理

        // 销毁createOpts，防止内存泄漏
        OH_PixelmapInitializationOptions_Release(createOpts);

        // 销毁startWindowIcon，防止内存泄漏
        OH_PixelmapNative_Release(startWindowIcon);
        return;
    }

    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsStartWindowIcon(options, startWindowIcon);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 销毁createOpts，防止内存泄漏
    OH_PixelmapInitializationOptions_Release(createOpts);

    // 销毁startWindowIcon，防止内存泄漏
    OH_PixelmapNative_Release(startWindowIcon);

    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### \[h2\]OH\_AbilityRuntime\_GetStartOptionsStartWindowIcon()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsStartWindowIcon(AbilityRuntime_StartOptions *startOptions,OH_PixelmapNative **startWindowIcon)
```

**描述**

获取启动Ability时的窗口启动图标。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-startoptions) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| OH\_PixelmapNative \*\*startWindowIcon | 启动Ability时的窗口启动图标。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-runtime-common-h#abilityruntime_errorcode) | 
在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。

在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions或者StartWindowBackgroundColor为空。

 |

**示例代码：**

```cpp
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    OH_PixelmapNative *startWindowIcon = nullptr;
    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsStartWindowIcon(options, &startWindowIcon);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }

    // 销毁startWindowIcon，防止内存泄漏
    OH_PixelmapNative_Release(startWindowIcon);

    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### \[h2\]OH\_AbilityRuntime\_SetStartOptionsStartWindowBackgroundColor()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsStartWindowBackgroundColor(AbilityRuntime_StartOptions *startOptions, const char *startWindowBackgroundColor)
```

**描述**

设置启动Ability时的窗口背景颜色。启动UIAbility时，启动页所显示的背景颜色如果未设置该字段，则默认采用[module.json5配置文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)中[abilities标签](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file#abilities标签)的startWindowBackground字段的配置。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-startoptions) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| const char \*startWindowBackgroundColor | 启动Ability时的窗口背景颜色。固定为ARGB格式, 如：#E5FFFFFF。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-runtime-common-h#abilityruntime_errorcode) | 
在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。

在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空，或者StartWindowBackgroundColor没有置为空指针。

 |

**示例代码：**

```cpp
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsStartWindowBackgroundColor(options, "#00000000");
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }

    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### \[h2\]OH\_AbilityRuntime\_GetStartOptionsStartWindowBackgroundColor()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsStartWindowBackgroundColor(AbilityRuntime_StartOptions *startOptions, char **startWindowBackgroundColor, size_t &size)
```

**描述**

获取启动Ability时的窗口背景颜色。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-startoptions) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| char \*\*startWindowBackgroundColor | 启动Ability时的窗口背景颜色。固定为ARGB格式, 如：#E5FFFFFF。 |
| size\_t &size | 获取到的窗口背景颜色的大小。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-runtime-common-h#abilityruntime_errorcode) | 
在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。

在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions或者SupportedWindowModes为空，或者Size为0。

在返回ABILITY\_RUNTIME\_ERROR\_CODE\_INTERNAL时，表示开发者无法恢复的内部错误，比如内部调用malloc错误，或者字符串拷贝函数出错。

 |

**示例代码：**

```cpp
#include <cstdlib>

#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    char *startWindowBackgroundColor = nullptr;
    size_t size = 0;
    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsStartWindowBackgroundColor(options,
        &startWindowBackgroundColor, size);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }

    if (startWindowBackgroundColor != nullptr) {
        // 销毁startWindowBackgroundColor，防止内存泄漏
        free(startWindowBackgroundColor);
        startWindowBackgroundColor = nullptr;
    }

    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### \[h2\]OH\_AbilityRuntime\_SetStartOptionsSupportedWindowModes()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsSupportedWindowModes(AbilityRuntime_StartOptions *startOptions, AbilityRuntime_SupportedWindowMode *supportedWindowModes,size_t size)
```

**描述**

设置启动Ability时的组件所支持的窗口模式。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-startoptions) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| [AbilityRuntime\_SupportedWindowMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-context-constant-h#abilityruntime_supportedwindowmode) \*supportedWindowModes | 启动Ability时的组件所支持的窗口模式。取值范围参见AbilityRuntime\_SupportedWindowMode。 |
| size\_t size | 组件所支持的窗口模式大小。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-runtime-common-h#abilityruntime_errorcode) | 
在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。

在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions或者SupportedWindowModes为空，或者Size为0。

 |

**示例代码：**

```cpp
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    size_t supportedWindowModesSize = 3;
    AbilityRuntime_SupportedWindowMode supportedWindowModes[3] = {
        ABILITY_RUNTIME_SUPPORTED_WINDOW_MODE_FULL_SCREEN,
        ABILITY_RUNTIME_SUPPORTED_WINDOW_MODE_SPLIT,
        ABILITY_RUNTIME_SUPPORTED_WINDOW_MODE_FLOATING,
    };
    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsSupportedWindowModes(options,
        supportedWindowModes, supportedWindowModesSize);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }

    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### \[h2\]OH\_AbilityRuntime\_GetStartOptionsSupportedWindowModes()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsSupportedWindowModes(AbilityRuntime_StartOptions *startOptions, AbilityRuntime_SupportedWindowMode **supportedWindowModes,size_t &size)
```

**描述**

获取启动Ability时的组件所支持的窗口模式。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-startoptions) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| [AbilityRuntime\_SupportedWindowMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-context-constant-h#abilityruntime_supportedwindowmode) \*\*supportedWindowModes | 启动Ability时的组件所支持的窗口模式。取值范围参见AbilityRuntime\_SupportedWindowMode。 |
| size | 组件所支持的窗口模式大小。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-runtime-common-h#abilityruntime_errorcode) | 
在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。

在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空，或者SupportWindowMode没有置为空指针。

在返回ABILITY\_RUNTIME\_ERROR\_CODE\_INTERNAL时，表示开发者无法恢复的内部错误，比如内部调用malloc错误。

 |

**示例代码：**

```cpp
#include <cstdlib>

#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    AbilityRuntime_SupportedWindowMode *supportedWindowModes = nullptr;
    size_t size = 0;
    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsSupportedWindowModes(options,
        &supportedWindowModes, size);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }

    if (supportedWindowModes != nullptr) {
        // 销毁supportedWindowModes，防止内存泄漏
        free(supportedWindowModes);
    }

    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### \[h2\]OH\_AbilityRuntime\_SetStartOptionsMinWindowWidth()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsMinWindowWidth(AbilityRuntime_StartOptions *startOptions, int32_t minWindowWidth)
```

**描述**

设置启动Ability时的窗口最小宽度，单位为vp。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-startoptions) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| int32\_t minWindowWidth | 启动Ability时的窗口最小宽度，单位为vp。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-runtime-common-h#abilityruntime_errorcode) | 
在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。

在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。

 |

**示例代码：**

```cpp
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsMinWindowWidth(options, 100);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }

    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### \[h2\]OH\_AbilityRuntime\_GetStartOptionsMinWindowWidth()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsMinWindowWidth(AbilityRuntime_StartOptions *startOptions, int32_t &minWindowWidth)
```

**描述**

获取启动Ability时的窗口最小宽度，单位为vp。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-startoptions) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| int32\_t &minWindowWidth | 启动Ability时的窗口最小宽度，单位为vp。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-runtime-common-h#abilityruntime_errorcode) | 
在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。

在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。

 |

**示例代码：**

```cpp
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    int32_t minWindowWidth = 0;
    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsMinWindowWidth(options, minWindowWidth);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }

    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### \[h2\]OH\_AbilityRuntime\_SetStartOptionsMaxWindowWidth()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsMaxWindowWidth(AbilityRuntime_StartOptions *startOptions, int32_t maxWindowWidth)
```

**描述**

设置启动Ability时的窗口最大宽度，单位为vp。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-startoptions) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| int32\_t maxWindowWidth | 启动Ability时的窗口最大宽度，单位为vp。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-runtime-common-h#abilityruntime_errorcode) | 
在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。

在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。

 |

**示例代码：**

```cpp
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsMaxWindowWidth(options, 100);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }

    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### \[h2\]OH\_AbilityRuntime\_GetStartOptionsMaxWindowWidth()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsMaxWindowWidth(AbilityRuntime_StartOptions *startOptions, int32_t &maxWindowWidth)
```

**描述**

获取启动Ability时的窗口最大宽度，单位为vp。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-startoptions) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| int32\_t &maxWindowWidth | 启动Ability时的窗口最大宽度，单位为vp。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-runtime-common-h#abilityruntime_errorcode) | 
在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。

在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。

 |

**示例代码：**

```cpp
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    int32_t maxWindowWidth = 0;
    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsMaxWindowWidth(options, maxWindowWidth);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }

    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### \[h2\]OH\_AbilityRuntime\_SetStartOptionsMinWindowHeight()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsMinWindowHeight(AbilityRuntime_StartOptions *startOptions, int32_t minWindowHeight)
```

**描述**

设置启动Ability时的窗口最小高度，单位为vp。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-startoptions) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| int32\_t minWindowHeight | 启动Ability时的窗口最小高度，单位为vp。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-runtime-common-h#abilityruntime_errorcode) | 
在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。

在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。

 |

**示例代码：**

```cpp
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsMinWindowHeight(options, 100);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }

    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### \[h2\]OH\_AbilityRuntime\_GetStartOptionsMinWindowHeight()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsMinWindowHeight(AbilityRuntime_StartOptions *startOptions, int32_t &minWindowHeight)
```

**描述**

获取启动Ability时的窗口最小高度，单位为vp。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-startoptions) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| int32\_t &minWindowHeight | 启动Ability时的窗口最小高度，单位为vp。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-runtime-common-h#abilityruntime_errorcode) | 
在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。

在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。

 |

**示例代码：**

```cpp
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    int32_t minWindowHeight = 0;
    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsMinWindowHeight(options, minWindowHeight);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }

    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### \[h2\]OH\_AbilityRuntime\_SetStartOptionsMaxWindowHeight()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_SetStartOptionsMaxWindowHeight(AbilityRuntime_StartOptions *startOptions, int32_t maxWindowHeight)
```

**描述**

设置启动Ability时的窗口最大高度，单位为vp。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-startoptions) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| int32\_t maxWindowHeight | 启动Ability时的窗口最大高度，单位为vp。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-runtime-common-h#abilityruntime_errorcode) | 
在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。

在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。

 |

**示例代码：**

```cpp
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_SetStartOptionsMaxWindowHeight(options, 100);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }

    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

#### \[h2\]OH\_AbilityRuntime\_GetStartOptionsMaxWindowHeight()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_GetStartOptionsMaxWindowHeight(AbilityRuntime_StartOptions *startOptions, int32_t &maxWindowHeight)
```

**描述**

获取启动Ability时的窗口最大高度，单位为vp。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [AbilityRuntime\_StartOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-startoptions) \*startOptions | AbilityRuntime\_StartOptions对象。 |
| int32\_t &maxWindowHeight | 启动Ability时的窗口最大高度，单位为vp。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-runtime-common-h#abilityruntime_errorcode) | 
在返回ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR时，表示接口调用成功。

在返回ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID时，表示StartOptions为空。

 |

**示例代码：**

```cpp
#include <AbilityKit/ability_runtime/start_options.h>

void demo()
{
    AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
    if (options == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    int32_t maxWindowHeight = 0;
    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetStartOptionsMaxWindowHeight(options, maxWindowHeight);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }

    // 销毁options，防止内存泄漏
    OH_AbilityRuntime_DestroyStartOptions(&options);
}
```

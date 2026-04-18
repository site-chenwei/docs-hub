---
title: "ArkUI_NativeDialogAPI_2"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-2"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "C API"
  - "结构体"
  - "ArkUI_NativeDialogAPI_2"
captured_at: "2026-04-17T01:48:08.682Z"
---

# ArkUI\_NativeDialogAPI\_2

```c
typedef struct {...} ArkUI_NativeDialogAPI_2
```

#### 概述

ArkUI提供的Native侧自定义弹窗接口集合。

**起始版本：** 15

**相关模块：** [ArkUI\_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)

**所在头文件：** [native\_dialog.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-dialog-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogAPI\_1](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1) nativeDialogAPI1 | 
ArkUI提供的Native侧自定义弹窗接口集合，范围是[ArkUI\_NativeDialogAPI\_1](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1)。

**起始版本：** 15

 |

#### \[h2\]成员函数

| 名称 | 描述 |
| :-- | :-- |
| [int32\_t (\*setKeyboardAvoidDistance)(ArkUI\_NativeDialogHandle handle, float distance, ArkUI\_LengthMetricUnit unit)](#setkeyboardavoiddistance) | 弹窗避让键盘后，和键盘之间距离。 |
| [int32\_t (\*setLevelMode)(ArkUI\_NativeDialogHandle handle, ArkUI\_LevelMode levelMode)](#setlevelmode) | 设置弹窗的显示层级。 |
| [int32\_t (\*setLevelUniqueId)(ArkUI\_NativeDialogHandle handle, int32\_t uniqueId)](#setleveluniqueid) | 设置弹窗显示层级页面下的节点id。 |
| [int32\_t (\*setImmersiveMode)(ArkUI\_NativeDialogHandle handle, ArkUI\_ImmersiveMode immersiveMode)](#setimmersivemode) | 设置嵌入式弹窗蒙层的显示区域。 |

#### 成员函数说明

#### \[h2\]setKeyboardAvoidDistance()

```c
int32_t (*setKeyboardAvoidDistance)(ArkUI_NativeDialogHandle handle, float distance, ArkUI_LengthMetricUnit unit)
```

**描述：**

弹窗避让键盘后，和键盘之间距离。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/rcNKHQv8QS-36qTycZpqLw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014808Z&HW-CC-Expire=86400&HW-CC-Sign=55AA540B7CDAAC61D2DDA0E112170F5BE17FDBC6E028F959E93354B7DB95923A)

setKeyboardAvoidDistance方法需要在调用[show](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1#show)方法之前调用。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) handle | 指向自定义弹窗控制器的指针。 |
| float distance | 避让键盘的距离，单位为vp。 |
| [ArkUI\_LengthMetricUnit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_lengthmetricunit) unit | 避让距离的单位，参数类型[ArkUI\_LengthMetricUnit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_lengthmetricunit)。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 接口初始化错误。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]setLevelMode()

```c
int32_t (*setLevelMode)(ArkUI_NativeDialogHandle handle, ArkUI_LevelMode levelMode)
```

**描述：**

设置弹窗的显示层级。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/Q6ggKvpDRkuKGoN8H-NEcQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014808Z&HW-CC-Expire=86400&HW-CC-Sign=4527C4F844F429E63B2E3BBE520BB39EE9F2BF708A4EFFB29F7627FE631AF072)

setLevelMode方法需要在调用[show](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1#show)方法之前调用。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) handle | 指向自定义弹窗控制器的指针。 |
| [ArkUI\_LevelMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-dialog-h#arkui_levelmode) levelMode | 显示层级的枚举值， 类型为[ArkUI\_LevelMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-dialog-h#arkui_levelmode)。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]setLevelUniqueId()

```c
int32_t (*setLevelUniqueId)(ArkUI_NativeDialogHandle handle, int32_t uniqueId)
```

**描述：**

设置弹窗显示层级页面下的节点id。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/qcLn5K7eRIC4HyZ_5VXX7w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014808Z&HW-CC-Expire=86400&HW-CC-Sign=30ADC9B1F7DCB6AC4BCAA8B9D80A6E8C4B65B168B0C97C4EF9FD5D73AD77E4E5)

setLevelUniqueId方法需要在调用[setLevelMode](#setlevelmode)方法之前调用。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) handle | 指向自定义弹窗控制器的指针。 |
| int32\_t uniqueId | 指定节点id，会查找该节点所在页面，并将弹窗显示在该页面下。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]setImmersiveMode()

```c
int32_t (*setImmersiveMode)(ArkUI_NativeDialogHandle handle, ArkUI_ImmersiveMode immersiveMode)
```

**描述：**

设置嵌入式弹窗蒙层的显示区域。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/VfPhrPxGR6uEo_uQQTk-3Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014808Z&HW-CC-Expire=86400&HW-CC-Sign=C4A0CA67B45ABB1CC5578F2D07F56D79DE085AA069CCB2CD8E7E9842D28EBCFF)

setImmersiveMode方法需要在调用[show](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1#show)方法之前调用。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) handle | 指向自定义弹窗控制器的指针。 |
| [ArkUI\_ImmersiveMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-dialog-h#arkui_immersivemode) immersiveMode | 显示区域类型的枚举值， 类型为[ArkUI\_ImmersiveMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-dialog-h#arkui_immersivemode)。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

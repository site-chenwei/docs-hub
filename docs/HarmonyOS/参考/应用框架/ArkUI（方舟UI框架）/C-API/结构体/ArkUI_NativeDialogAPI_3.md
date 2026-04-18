---
title: "ArkUI_NativeDialogAPI_3"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-3"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "C API"
  - "结构体"
  - "ArkUI_NativeDialogAPI_3"
captured_at: "2026-04-17T01:48:08.730Z"
---

# ArkUI\_NativeDialogAPI\_3

```c
typedef struct {...} ArkUI_NativeDialogAPI_3
```

#### 概述

ArkUI提供的Native侧自定义弹窗接口集合。

**起始版本：** 19

**相关模块：** [ArkUI\_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)

**所在头文件：** [native\_dialog.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-dialog-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogAPI\_1](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1) nativeDialogAPI1 | 
ArkUI提供的Native侧自定义弹窗接口集合，范围是[ArkUI\_NativeDialogAPI\_1](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1)。

**起始版本：** 19

 |
| [ArkUI\_NativeDialogAPI\_2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-2) nativeDialogAPI2 | 

ArkUI提供的Native侧自定义弹窗接口集合，范围是[ArkUI\_NativeDialogAPI\_2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-2)。

**起始版本：** 19

 |

#### \[h2\]成员函数

| 名称 | 描述 |
| :-- | :-- |
| [int32\_t (\*setLevelOrder)(ArkUI\_NativeDialogHandle handle, double levelOrder)](#setlevelorder) | 设置自定义弹窗显示的顺序。 |
| [int32\_t (\*registerOnWillAppear)(ArkUI\_NativeDialogHandle handle, void\* userData, void (\*callback)(void\* userData))](#registeronwillappear) | 注册自定义弹窗显示之前的回调函数。 |
| [int32\_t (\*registerOnDidAppear)(ArkUI\_NativeDialogHandle handle, void\* userData, void (\*callback)(void\* userData))](#registerondidappear) | 注册自定义弹窗显示之后的回调函数。 |
| [int32\_t (\*registerOnWillDisappear)(ArkUI\_NativeDialogHandle handle, void\* userData, void (\*callback)(void\* userData))](#registeronwilldisappear) | 注册自定义弹窗关闭之前的回调函数。 |
| [int32\_t (\*registerOnDidDisappear)(ArkUI\_NativeDialogHandle handle, void\* userData, void (\*callback)(void\* userData))](#registerondiddisappear) | 注册自定义弹窗关闭之后的回调函数。 |
| [int32\_t (\*setBorderWidth)(ArkUI\_NativeDialogHandle handle, float top, float right, float bottom, float left, ArkUI\_LengthMetricUnit unit)](#setborderwidth) | 设置自定义弹窗的边框宽度。 |
| [int32\_t (\*setBorderColor)(ArkUI\_NativeDialogHandle handle, uint32\_t top, uint32\_t right, uint32\_t bottom, uint32\_t left)](#setbordercolor) | 设置自定义弹窗的边框颜色。 |
| [int32\_t (\*setBorderStyle)(ArkUI\_NativeDialogHandle handle, int32\_t top, int32\_t right, int32\_t bottom, int32\_t left)](#setborderstyle) | 设置自定义弹窗的边框样式。 |
| [int32\_t (\*setWidth)(ArkUI\_NativeDialogHandle handle, float width, ArkUI\_LengthMetricUnit unit)](#setwidth) | 设置自定义弹窗的背板宽度。 |
| [int32\_t (\*setHeight)(ArkUI\_NativeDialogHandle handle, float height, ArkUI\_LengthMetricUnit unit)](#setheight) | 设置自定义弹窗的背板高度。 |
| [int32\_t (\*setShadow)(ArkUI\_NativeDialogHandle handle, ArkUI\_ShadowStyle shadow)](#setshadow) | 设置自定义弹窗的背板阴影。 |
| [int32\_t (\*setCustomShadow)(ArkUI\_NativeDialogHandle handle, const ArkUI\_AttributeItem\* customShadow)](#setcustomshadow) | 设置自定义弹窗的背板阴影。 |
| [int32\_t (\*setBackgroundBlurStyle)(ArkUI\_NativeDialogHandle handle, ArkUI\_BlurStyle blurStyle)](#setbackgroundblurstyle) | 设置自定义弹窗的背板模糊材质。 |
| [int32\_t (\*setKeyboardAvoidMode)(ArkUI\_NativeDialogHandle handle, ArkUI\_KeyboardAvoidMode keyboardAvoidMode)](#setkeyboardavoidmode) | 设置自定义弹窗避让键盘模式。 |
| [int32\_t (\*enableHoverMode)(ArkUI\_NativeDialogHandle handle, bool enableHoverMode)](#enablehovermode) | 设置自定义弹窗是否响应悬停态。 |
| [int32\_t (\*setHoverModeArea)(ArkUI\_NativeDialogHandle handle, ArkUI\_HoverModeAreaType hoverModeAreaType)](#sethovermodearea) | 设置悬停态下自定义弹窗默认展示区域。 |
| [int32\_t (\*setFocusable)(ArkUI\_NativeDialogHandle handle, bool focusable)](#setfocusable) | 设置自定义弹窗是否获取焦点。 |
| [int32\_t (\*setBackgroundBlurStyleOptions)(ArkUI\_NativeDialogHandle handle, const ArkUI\_AttributeItem\* backgroundBlurStyleOptions)](#setbackgroundblurstyleoptions) | 设置自定义弹窗的背景模糊效果。 |
| [int32\_t (\*setBackgroundEffect)(ArkUI\_NativeDialogHandle handle, const ArkUI\_AttributeItem\* backgroundEffect)](#setbackgroundeffect) | 设置自定义弹窗的背景效果参数。 |

#### 成员函数说明

#### \[h2\]setLevelOrder()

```c
int32_t (*setLevelOrder)(ArkUI_NativeDialogHandle handle, double levelOrder)
```

**描述：**

设置自定义弹窗显示的顺序。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/jEzmRdiUQgOsg2WLqjtHoQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014808Z&HW-CC-Expire=86400&HW-CC-Sign=0ADCF1BBB36B97069A77814B26176235A7D478BEC568098925B24E6ABDE5B1C3)

setLevelOrder方法需要在调用[show](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1#show)之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) handle | 指向自定义弹窗控制器的指针。 |
| double levelOrder | 
自定义弹窗显示的顺序。

默认值：0，取值范围：\[-100000.0, 100000.0\]。超出取值范围属性不生效。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]registerOnWillAppear()

```c
int32_t (*registerOnWillAppear)(ArkUI_NativeDialogHandle handle, void* userData, void (*callback)(void* userData))
```

**描述：**

注册自定义弹窗显示之前的回调函数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/gdwZ03xyTWaxeDn1bC33gw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014808Z&HW-CC-Expire=86400&HW-CC-Sign=EDF78C79529CC90C1E96BD787CFD15DB653B5B5841C566B296E6E26EB4210E53)

registerOnWillAppear方法需要在调用[show](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1#show)之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) handle | 指向自定义弹窗控制器的指针。 |
| void\* userData | 用户自定义数据。 |
| callback | 自定义弹窗显示之前的回调函数。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]registerOnDidAppear()

```c
int32_t (*registerOnDidAppear)(ArkUI_NativeDialogHandle handle, void* userData, void (*callback)(void* userData))
```

**描述：**

注册自定义弹窗显示之后的回调函数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/8IfmoOTcRUe928YvItUtYA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014808Z&HW-CC-Expire=86400&HW-CC-Sign=B95EAA202B60CD7F53EC344510345E368B1E795884CBEBCFFFE4716C413EA5FD)

registerOnDidAppear方法需要在调用[show](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1#show)之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) handle | 指向自定义弹窗控制器的指针。 |
| void\* userData | 用户自定义数据。 |
| callback | 自定义弹窗显示之后的回调函数。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]registerOnWillDisappear()

```c
int32_t (*registerOnWillDisappear)(ArkUI_NativeDialogHandle handle, void* userData, void (*callback)(void* userData))
```

**描述：**

注册自定义弹窗关闭之前的回调函数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/HJphCb0QTiqPVvOmURu26w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014808Z&HW-CC-Expire=86400&HW-CC-Sign=766C6FF492A6BA6D09A26082EA7DD2F26757E3B9A73093A3205A48DB3D6E4416)

registerOnWillDisappear方法需要在调用[show](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1#show)之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) handle | 指向自定义弹窗控制器的指针。 |
| void\* userData | 用户自定义数据。 |
| callback | 自定义弹窗关闭之前的回调函数。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]registerOnDidDisappear()

```c
int32_t (*registerOnDidDisappear)(ArkUI_NativeDialogHandle handle, void* userData, void (*callback)(void* userData))
```

**描述：**

注册自定义弹窗关闭之后的回调函数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/KALyp6_4R-eg_A6VV1JY4w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014808Z&HW-CC-Expire=86400&HW-CC-Sign=47F9E5AF39A9171335B83E3211388ADD86D3C417CA5AE3845C40A8FF7FE04A41)

registerOnDidDisappear方法需要在调用[show](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1#show)之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) handle | 指向自定义弹窗控制器的指针。 |
| void\* userData | 用户自定义数据。 |
| callback | 自定义弹窗关闭之后的回调函数。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]setBorderWidth()

```c
int32_t (*setBorderWidth)(ArkUI_NativeDialogHandle handle, float top, float right, float bottom, float left, ArkUI_LengthMetricUnit unit)
```

**描述：**

设置自定义弹窗的边框宽度。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/Om-Ow6brQaKMetx-eEQvYg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014808Z&HW-CC-Expire=86400&HW-CC-Sign=98BD9BE4E6C93E4BC6B20899FCE56540FE7A31D14DDE5AC3EB9F7410C8E2742A)

setBorderWidth方法需要在调用[show](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1#show)之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) handle | 指向自定义弹窗控制器的指针。 |
| float top | 上边框的宽度。 |
| float right | 右边框的宽度。 |
| float bottom | 下边框的宽度。 |
| float left | 左边框的宽度。 |
| [ArkUI\_LengthMetricUnit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_lengthmetricunit) unit | 指定宽度单位，默认为vp。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]setBorderColor()

```c
int32_t (*setBorderColor)(ArkUI_NativeDialogHandle handle, uint32_t top, uint32_t right, uint32_t bottom, uint32_t left)
```

**描述：**

设置自定义弹窗的边框颜色。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/FH6vVlpYT7CJHbh3rSUDVA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014808Z&HW-CC-Expire=86400&HW-CC-Sign=5243FA681AA5DAFB8CD05194876AF248C82620E22FC6B265D7BD8854E31DF51F)

setBorderColor方法需要在调用[show](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1#show)之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) handle | 指向自定义弹窗控制器的指针。 |
| uint32\_t top | 上边框的颜色。 |
| uint32\_t right | 右边框的颜色。 |
| uint32\_t bottom | 下边框的颜色。 |
| uint32\_t left | 左边框的颜色。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]setBorderStyle()

```c
int32_t (*setBorderStyle)(ArkUI_NativeDialogHandle handle, int32_t top, int32_t right, int32_t bottom, int32_t left)
```

**描述：**

设置自定义弹窗的边框样式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/pZOzSPiyT-mvj9uSDj2eTw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014808Z&HW-CC-Expire=86400&HW-CC-Sign=A6CDFC19D89E8C9380216C2DB9635D77EFF08A0CD6936C45A84FC0FD0FCFC86B)

setBorderStyle方法需要在调用[show](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1#show)之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) handle | 指向自定义弹窗控制器的指针。 |
| int32\_t top | 上边框的样式。参数类型[ArkUI\_BorderStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_borderstyle)，默认值为ARKUI\_BORDER\_STYLE\_SOLID。 |
| int32\_t right | 右边框的样式。参数类型[ArkUI\_BorderStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_borderstyle)，默认值为ARKUI\_BORDER\_STYLE\_SOLID。 |
| int32\_t bottom | 下边框的样式。参数类型[ArkUI\_BorderStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_borderstyle)，默认值为ARKUI\_BORDER\_STYLE\_SOLID。 |
| int32\_t left | 左边框的样式。参数类型[ArkUI\_BorderStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_borderstyle)，默认值为ARKUI\_BORDER\_STYLE\_SOLID。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]setWidth()

```c
int32_t (*setWidth)(ArkUI_NativeDialogHandle handle, float width, ArkUI_LengthMetricUnit unit)
```

**描述：**

设置自定义弹窗的背板宽度。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/OEhPJpaXQkeFaOXFCYAHkw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014808Z&HW-CC-Expire=86400&HW-CC-Sign=9C9434EF5CA6B27F4169C048FDB7735F1AAA6805056DA82CE70A91A86C5B1795)

setWidth方法需要在调用[show](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1#show)之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) handle | 指向自定义弹窗控制器的指针。 |
| float width | 背板宽度。 |
| [ArkUI\_LengthMetricUnit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_lengthmetricunit) unit | 指定宽度的单位，默认为vp。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]setHeight()

```c
int32_t (*setHeight)(ArkUI_NativeDialogHandle handle, float height, ArkUI_LengthMetricUnit unit)
```

**描述：**

设置自定义弹窗的背板高度。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/pKCqn9L8SQKp48ml_ROIDQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014808Z&HW-CC-Expire=86400&HW-CC-Sign=E5CBD1D5B622BDF5BD3DAA2E121A39CAF0C081CD781EB9BB14D17099D82AD5F8)

setHeight方法需要在调用[show](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1#show)之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) handle | 指向自定义弹窗控制器的指针。 |
| float height | 背板高度。 |
| [ArkUI\_LengthMetricUnit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_lengthmetricunit) unit | 指定高度的单位，默认为vp。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]setShadow()

```c
int32_t (*setShadow)(ArkUI_NativeDialogHandle handle, ArkUI_ShadowStyle shadow)
```

**描述：**

设置自定义弹窗的背板阴影。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/1fuE6HmdQ2yRvDzuNNCyEg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014808Z&HW-CC-Expire=86400&HW-CC-Sign=FDDC6E274C26C335066D39CC1A607C2D5702712E046F61482F102FA3E16073AA)

setShadow方法需要在调用[show](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1#show)之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) handle | 指向自定义弹窗控制器的指针。 |
| [ArkUI\_ShadowStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_shadowstyle) shadow | 背板阴影样式，枚举值。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]setCustomShadow()

```c
int32_t (*setCustomShadow)(ArkUI_NativeDialogHandle handle, const ArkUI_AttributeItem* customShadow)
```

**描述：**

设置自定义弹窗的背板阴影。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/ESfGjH05RBeEDUoMwG4WQQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014808Z&HW-CC-Expire=86400&HW-CC-Sign=0088DBE131E91627628B5D8206296018CA5782CCCE161809325C5871A68A8022)

setCustomShadow方法需要在调用[show](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1#show)之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) handle | 指向自定义弹窗控制器的指针。 |
| const [ArkUI\_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)\* customShadow | 自定义阴影参数，格式与[ArkUI\_NodeAttributeType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h#arkui_nodeattributetype)中的NODE\_SHADOW属性一致。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]setBackgroundBlurStyle()

```c
int32_t (*setBackgroundBlurStyle)(ArkUI_NativeDialogHandle handle, ArkUI_BlurStyle blurStyle)
```

**描述：**

设置自定义弹窗的背板模糊材质。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/JhoUHhcNR8qa4y3VNfs9NQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014808Z&HW-CC-Expire=86400&HW-CC-Sign=5868A7653A729B646D67D835D1350730063E5413ECFD8DBAE5FAE503148BE304)

setBackgroundBlurStyle方法需要在调用[show](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1#show)之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) handle | 指向自定义弹窗控制器的指针。 |
| [ArkUI\_BlurStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_blurstyle) blurStyle | 背板模糊材质，枚举值。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]setKeyboardAvoidMode()

```c
int32_t (*setKeyboardAvoidMode)(ArkUI_NativeDialogHandle handle, ArkUI_KeyboardAvoidMode keyboardAvoidMode)
```

**描述：**

设置自定义弹窗避让键盘模式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/hoOC1rH7SnaSFAmAubh5_A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014808Z&HW-CC-Expire=86400&HW-CC-Sign=BE75FD477291F20396BED662C77638DE2764F9ADF4C56E84DCE6AD7125574B39)

setKeyboardAvoidMode方法需要在调用[show](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1#show)之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) handle | 指向自定义弹窗控制器的指针。 |
| [ArkUI\_KeyboardAvoidMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_keyboardavoidmode) keyboardAvoidMode | 避让键盘模式，枚举值。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]enableHoverMode()

```c
int32_t (*enableHoverMode)(ArkUI_NativeDialogHandle handle, bool enableHoverMode)
```

**描述：**

设置自定义弹窗是否响应悬停态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/mplJLZ7zTnK7I6BF3OvKKw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014808Z&HW-CC-Expire=86400&HW-CC-Sign=D6C27B69087C22091768619891A54819845F176BE8DF987158EBD88D2B88B943)

enableHoverMode方法需要在调用[show](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1#show)之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) handle | 指向自定义弹窗控制器的指针。 |
| bool enableHoverMode | 是否响应悬停态，默认false。true表示响应悬停态，false表示不响应悬停态。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]setHoverModeArea()

```c
int32_t (*setHoverModeArea)(ArkUI_NativeDialogHandle handle, ArkUI_HoverModeAreaType hoverModeAreaType)
```

**描述：**

设置悬停态下自定义弹窗默认展示区域。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/AimCzygTRS2T1p5IP-szCg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014808Z&HW-CC-Expire=86400&HW-CC-Sign=71FE42ACFE23AF7CDE5A7B1D5E44C28492E00982D5F9921E74CF483CD9518ACF)

setHoverModeArea方法需要在调用[show](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1#show)之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) handle | 指向自定义弹窗控制器的指针。 |
| [ArkUI\_HoverModeAreaType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_hovermodeareatype) hoverModeAreaType | 悬停态区域，枚举值。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]setFocusable()

```c
int32_t (*setFocusable)(ArkUI_NativeDialogHandle handle, bool focusable)
```

**描述：**

设置自定义弹窗是否获取焦点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/TFK7deJ8SS29pHFvoQXZhA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014808Z&HW-CC-Expire=86400&HW-CC-Sign=EF1F3113FB6EF5487C5C719F6BBAA38AEAA8442180C3AE759222E3AE502879E2)

setFocusable方法需要在调用[show](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1#show)之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) handle | 指向自定义弹窗控制器的指针。 |
| bool focusable | 自定义弹窗是否获取焦点。true表示自动获取焦点，false表示不自动获取焦点。默认值：true |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]setBackgroundBlurStyleOptions()

```c
int32_t (*setBackgroundBlurStyleOptions)(ArkUI_NativeDialogHandle handle, const ArkUI_AttributeItem* backgroundBlurStyleOptions)
```

**描述：**

设置自定义弹窗的背景模糊效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/StiL00zESSCMr7SMPnZYiQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014808Z&HW-CC-Expire=86400&HW-CC-Sign=EF7E2C0BB7204851EF9043241D8286301C8A762B616B20D437BE5280927FAD6A)

setBackgroundBlurStyleOptions方法需要在调用[show](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1#show)之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) handle | 指向自定义弹窗控制器的指针。 |
| const [ArkUI\_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)\* backgroundBlurStyleOptions | 
背景模糊效果。参数[ArkUI\_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式：

.value\[0\].i32：表示深浅色模式，取[ArkUI\_ColorMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_colormode)枚举值。

.value\[1\]?.i32：表示取色模式，取[ArkUI\_AdaptiveColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_adaptivecolor)枚举值。

.value\[2\]?.f32：表示模糊效果程度，取\[0.0,1.0\]范围内的值，超出有效值区间时取边界值。

.value\[3\]?.u32：表示灰阶模糊参数，对黑色的提亮程度，有效值范围为\[0,127\]，超出有效值范围，取0。

.value\[4\]?.u32：表示灰阶模糊参数，对白色的压暗程度，有效值范围为\[0,127\]，超出有效值范围，取0。

.value\[5\]?.i32：表示模糊激活策略，取[ArkUI\_BlurStyleActivePolicy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_blurstyleactivepolicy)枚举值。

.value\[6\]?.u32：表示窗口失焦后，窗口内控件模糊效果会被移除，此时控件背板的颜色，0xargb类型。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]setBackgroundEffect()

```c
int32_t (*setBackgroundEffect)(ArkUI_NativeDialogHandle handle, const ArkUI_AttributeItem* backgroundEffect)
```

**描述：**

设置自定义弹窗的背景效果参数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/Jp6G6-fFT12H8aXfkjsu9A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014808Z&HW-CC-Expire=86400&HW-CC-Sign=753ACFB77DADE47A529F8DC024C894A48E5AD5CD26B1A7960DB9978C8A9F121D)

setBackgroundEffect方法需要在调用[show](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1#show)之前调用。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) handle | 指向自定义弹窗控制器的指针。 |
| const [ArkUI\_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)\* backgroundEffect | 
背景效果参数。参数[ArkUI\_AttributeItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem)格式：

.value\[0\].f32：表示模糊半径，单位为vp。

.value\[1\]?.f32：表示饱和度。

.value\[2\]?.f32：表示亮度。

.value\[3\]?.u32：表示颜色，0xargb类型。

.value\[4\]?.i32：表示取色模式，取[ArkUI\_AdaptiveColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_adaptivecolor)枚举值。

.value\[5\]?.u32：表示灰阶模糊参数，对黑色的提亮程度，有效值范围为\[0,127\]，超出有效值范围，取0。

.value\[6\]?.u32：表示灰阶模糊参数，对白色的压暗程度，有效值范围为\[0,127\]，超出有效值范围，取0。

.value\[7\]?.i32：表示模糊激活策略，取[ArkUI\_BlurStyleActivePolicy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_blurstyleactivepolicy)枚举值。

.value\[8\]?.u32：表示窗口失焦后，窗口内控件模糊效果会被移除，此时控件背板的颜色，0xargb类型。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

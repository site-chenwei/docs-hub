---
title: "ArkUI_NativeDialogAPI_1"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "C API"
  - "结构体"
  - "ArkUI_NativeDialogAPI_1"
captured_at: "2026-04-17T01:48:08.710Z"
---

# ArkUI\_NativeDialogAPI\_1

```c
typedef struct {...} ArkUI_NativeDialogAPI_1
```

#### 概述

ArkUI提供的Native侧自定义弹窗接口集合。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)

**所在头文件：** [native\_dialog.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-dialog-h)

#### 汇总

#### \[h2\]成员函数

| 名称 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle (\*create)()](#create) | 创建自定义弹窗并返回指向自定义弹窗的指针。 |
| [void (\*dispose)(ArkUI\_NativeDialogHandle handle)](#dispose) | 销毁自定义弹窗。 |
| [int32\_t (\*setContent)(ArkUI\_NativeDialogHandle handle, ArkUI\_NodeHandle content)](#setcontent) | 挂载自定义弹窗内容。 |
| [int32\_t (\*removeContent)(ArkUI\_NativeDialogHandle handle)](#removecontent) | 卸载自定义弹窗内容。 |
| [int32\_t (\*setContentAlignment)(ArkUI\_NativeDialogHandle handle, int32\_t alignment, float offsetX, float offsetY)](#setcontentalignment) | 设置自定义弹窗对齐方式。 |
| [int32\_t (\*resetContentAlignment)(ArkUI\_NativeDialogHandle handle)](#resetcontentalignment) | 重置setContentAlignment方法设置的属性，使用系统默认的对齐方式。 |
| [int32\_t (\*setModalMode)(ArkUI\_NativeDialogHandle handle, bool isModal)](#setmodalmode) | 设置自定义弹窗是否开启模态样式的弹窗。 |
| [int32\_t (\*setAutoCancel)(ArkUI\_NativeDialogHandle handle, bool autoCancel)](#setautocancel) | 设置自定义弹窗是否允许通过点击遮罩层退出。 |
| [int32\_t (\*setMask)(ArkUI\_NativeDialogHandle handle, uint32\_t maskColor, const ArkUI\_Rect\* maskRect)](#setmask) | 设置自定义弹窗遮罩属性。 |
| [int32\_t (\*setBackgroundColor)(ArkUI\_NativeDialogHandle handle, uint32\_t backgroundColor)](#setbackgroundcolor) | 设置弹窗背景色。 |
| [int32\_t (\*setCornerRadius)(ArkUI\_NativeDialogHandle handle, float topLeft, float topRight,float bottomLeft, float bottomRight)](#setcornerradius) | 设置弹窗背板圆角半径。 |
| [int32\_t (\*setGridColumnCount)(ArkUI\_NativeDialogHandle handle, int32\_t gridCount)](#setgridcolumncount) | 设置弹窗宽度占栅格宽度的个数。 |
| [int32\_t (\*enableCustomStyle)(ArkUI\_NativeDialogHandle handle, bool enableCustomStyle)](#enablecustomstyle) | 弹窗容器样式是否可以自定义。 |
| [int32\_t (\*enableCustomAnimation)(ArkUI\_NativeDialogHandle handle, bool enableCustomAnimation)](#enablecustomanimation) | 弹窗容器是否使用自定义弹窗动画。 |
| [int32\_t (\*registerOnWillDismiss)(ArkUI\_NativeDialogHandle handle, ArkUI\_OnWillDismissEvent eventHandler)](#registeronwilldismiss) | 当触发系统定义的返回操作、键盘ESC关闭交互操作时，如果注册了该回调函数，弹窗不会立即关闭，而是由用户决定是否关闭。 |
| [int32\_t (\*show)(ArkUI\_NativeDialogHandle handle, bool showInSubWindow)](#show) | 显示自定义弹窗。 |
| [int32\_t (\*close)(ArkUI\_NativeDialogHandle handle)](#close) | 关闭自定义弹窗，如已关闭，则不生效。该接口后台执行是异步的，在关闭动画执行完成后弹窗节点才会下树。如需关闭后再次打开弹窗，请在延迟300ms以后再执行。 |
| [int32\_t (\*registerOnWillDismissWithUserData)(ArkUI\_NativeDialogHandle handle, void\* userData, void (\*callback)(ArkUI\_DialogDismissEvent\* event))](#registeronwilldismisswithuserdata) | 注册系统关闭自定义弹窗的监听事件。 |

#### 成员函数说明

#### \[h2\]create()

```c
ArkUI_NativeDialogHandle (*create)()
```

**描述：**

创建自定义弹窗并返回指向自定义弹窗的指针。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/mdfzHyCbR2aD2WEzUYPhlA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014808Z&HW-CC-Expire=86400&HW-CC-Sign=0619608BE378F245B4A7C907C58DF0DD618FBB35521124C4A5171240388527E3)

create方法需要在调用[show](#show)方法之前调用。

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) | 返回指向自定义弹窗的指针，如果创建失败，则返回空指针。 |

#### \[h2\]dispose()

```c
void (*dispose)(ArkUI_NativeDialogHandle handle)
```

**描述：**

销毁自定义弹窗。

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) handle | 指向自定义弹窗控制器的指针。 |

#### \[h2\]setContent()

```c
int32_t (*setContent)(ArkUI_NativeDialogHandle handle, ArkUI_NodeHandle content)
```

**描述：**

挂载自定义弹窗内容。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/b4IS62x8RcSj1i7UXpJ1-A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014808Z&HW-CC-Expire=86400&HW-CC-Sign=A212DEEB4CCF3F113E4D73AC3E8C61BB306C43B8BC7E8B97C6BD765B68233915)

setContent方法需要在调用[show](#show)方法之前调用。

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) handle | 指向自定义弹窗控制器的指针。 |
| [ArkUI\_NodeHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h) content | 弹窗内容根节点指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]removeContent()

```c
int32_t (*removeContent)(ArkUI_NativeDialogHandle handle)
```

**描述：**

卸载自定义弹窗内容。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/A_TUKlEDRL2hv2QKNcjXTw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014808Z&HW-CC-Expire=86400&HW-CC-Sign=6EDAC67696F501DD62E9424B555932002A8FB8BBD305A5496DB36A5F969141E2)

removeContent方法需要在调用[show](#show)方法之前调用。

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) handle | 指向自定义弹窗控制器的指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]setContentAlignment()

```c
int32_t (*setContentAlignment)(ArkUI_NativeDialogHandle handle, int32_t alignment, float offsetX, float offsetY)
```

**描述：**

设置自定义弹窗对齐方式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/D5sPwId5RN2X05_5Cp5XgQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014808Z&HW-CC-Expire=86400&HW-CC-Sign=C2069FEBD9F51F70AB9DE5764A27370B89E7BB7D94C887E7D53AA2F6C89C1C11)

setContentAlignment方法需要在调用[show](#show)方法之前调用。

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) handle | 指向自定义弹窗控制器的指针。 |
| int32\_t alignment | 对齐方式，参数类型[ArkUI\_Alignment](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_alignment)。 |
| float offsetX | 弹窗的水平偏移量，浮点型，单位：vp。 |
| float offsetY | 弹窗的垂直偏移量，浮点型，单位：vp。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]resetContentAlignment()

```c
int32_t (*resetContentAlignment)(ArkUI_NativeDialogHandle handle)
```

**描述：**

重置setContentAlignment方法设置的属性，使用系统默认的对齐方式，默认值：ARKUI\_ALIGNMENT\_TOP\_START，参考[ArkUI\_Alignment](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_alignment)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/o8PSb81hT4O8NahhiPEiIA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014808Z&HW-CC-Expire=86400&HW-CC-Sign=F00EB48F4D7510E6006551882F00711DDB096AB998813B702E366BDFD695CFAA)

resetContentAlignment方法需要在调用[show](#show)方法之前调用。

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) handle | 指向自定义弹窗控制器的指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]setModalMode()

```c
int32_t (*setModalMode)(ArkUI_NativeDialogHandle handle, bool isModal)
```

**描述：**

设置自定义弹窗是否开启模态样式的弹窗。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/c568Zu5mRBu1ppsuhjyzGA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014808Z&HW-CC-Expire=86400&HW-CC-Sign=BA823F432B60D51C19715F73C782817FB63E1DA9E1B01BE26D9EC82604B15D83)

setModalMode方法需要在调用[show](#show)方法之前调用。

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) handle | 指向自定义弹窗控制器的指针。 |
| bool isModal | 设置是否开启模态窗口，模态窗口有蒙层，非模态窗口无蒙层。为true时开启模态窗口，为false时不开启模态窗口。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]setAutoCancel()

```c
int32_t (*setAutoCancel)(ArkUI_NativeDialogHandle handle, bool autoCancel)
```

**描述：**

设置自定义弹窗是否允许通过点击遮罩层退出。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/8DO7MvdnRHq70aonPpQx0g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014808Z&HW-CC-Expire=86400&HW-CC-Sign=F26E329040032C5A3352F8FE267033D7461C2023E7312341ABD357B207443D26)

setAutoCancel方法需要在调用[show](#show)方法之前调用。

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) handle | 指向自定义弹窗控制器的指针。 |
| bool autoCancel | 设置是否允许通过点击遮罩层退出，true表示关闭弹窗，false表示不关闭弹窗。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]setMask()

```c
int32_t (*setMask)(ArkUI_NativeDialogHandle handle, uint32_t maskColor, const ArkUI_Rect* maskRect)
```

**描述：**

设置自定义弹窗遮罩属性。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/qoGl266USne-prLoHg2I1g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014808Z&HW-CC-Expire=86400&HW-CC-Sign=87F41BB6EEDD3DA00F40376A2D7FF858D07D480E6D903843C622126BC2970D3B)

setMask方法需要在调用[show](#show)方法之前调用。

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) handle | 指向自定义弹窗控制器的指针。 |
| uint32\_t maskColor | 设置遮罩颜色，0xargb格式。 |
| const [ArkUI\_Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-rect)\* maskRect | 遮蔽层区域范围的指针，遮蔽层区域内的事件不透传，在遮蔽层区域外的事件透传。参数类型[ArkUI\_Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-rect)。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]setBackgroundColor()

```c
int32_t (*setBackgroundColor)(ArkUI_NativeDialogHandle handle, uint32_t backgroundColor)
```

**描述：**

设置弹窗背景色。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/y--yW9ZPQf-JI0bX0pf_JA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014808Z&HW-CC-Expire=86400&HW-CC-Sign=BDA60C14789AAAACE70946E9F369BDBF8CC4D2A09B0BB0E96A20FE7D065BEC8A)

setBackgroundColor方法需要在调用[show](#show)方法之前调用。

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) handle | 指向自定义弹窗控制器的指针。 |
| uint32\_t backgroundColor | 设置弹窗背景颜色，0xargb格式。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]setCornerRadius()

```c
int32_t (*setCornerRadius)(ArkUI_NativeDialogHandle handle, float topLeft, float topRight,float bottomLeft, float bottomRight)
```

**描述：**

设置弹窗背板圆角半径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/ADUDl-_gSbCaFeTDf8T9-g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014808Z&HW-CC-Expire=86400&HW-CC-Sign=E74C89FADF185CF57C14120465DF40B1B909B1D2AFC8369B96D1FDDA0FB94883)

setCornerRadius方法需要在调用[show](#show)方法之前调用。

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) handle | 指向自定义弹窗控制器的指针。 |
| float topLeft | 设置弹窗背板左上角圆角半径，单位：vp。默认值：从API version 12开始，为32vp。API version 11及之前版本，为24vp。 |
| float topRight | 设置弹窗背板右上角圆角半径，单位：vp。默认值：从API version 12开始，为32vp。API version 11及之前版本，为24vp。 |
| float bottomLeft | 设置弹窗背板左下圆角半径，单位：vp。默认值：从API version 12开始，为32vp。API version 11及之前版本，为24vp。 |
| float bottomRight | 设置弹窗背板右下角圆角半径，单位：vp。默认值：从API version 12开始，为32vp。API version 11及之前版本，为24vp。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]setGridColumnCount()

```c
int32_t (*setGridColumnCount)(ArkUI_NativeDialogHandle handle, int32_t gridCount)
```

**描述：**

设置弹窗宽度占栅格宽度的个数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/B_piZVL-RYeFWyCVeGcrog/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014808Z&HW-CC-Expire=86400&HW-CC-Sign=802F0829109F9EBB7B656C121A3D0E7A3AE07FDB7BAE32AA45DAF6D5095D043A)

setGridColumnCount方法需要在调用[show](#show)方法之前调用。

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) handle | 指向自定义弹窗控制器的指针。 |
| int32\_t gridCount | 
默认为按照窗口大小自适应，最大栅格数为[系统最大栅格数](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-grid-layout#布局的总列数)。

取值范围：大于等于0的整数。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]enableCustomStyle()

```c
int32_t (*enableCustomStyle)(ArkUI_NativeDialogHandle handle, bool enableCustomStyle)
```

**描述：**

弹窗容器样式是否可以自定义。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/xecn19UARyKQtH9MS9Z9FA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014808Z&HW-CC-Expire=86400&HW-CC-Sign=3C2817985F07E60706DAB37D5FEF6FDB1E453C70BFA31A557C551B384EBAB3BD)

enableCustomStyle方法需要在调用[show](#show)方法之前调用。

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) handle | 指向自定义弹窗控制器的指针。 |
| bool enableCustomStyle | 
弹窗容器样式是否可以自定义。

默认值：false

true：弹窗容器样式不能自定义，宽度自适应子节点，圆角为0，弹窗背景色透明；false：弹窗容器样式可以自定义，高度自适应子节点，宽度由栅格系统定义，圆角半径24vp，PC/2in1设备避让屏幕边缘以及窗口标题栏。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]enableCustomAnimation()

```c
int32_t (*enableCustomAnimation)(ArkUI_NativeDialogHandle handle, bool enableCustomAnimation)
```

**描述：**

弹窗容器是否使用自定义弹窗动画。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/PX7RnaQ8R22qItEl9zu_5A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014808Z&HW-CC-Expire=86400&HW-CC-Sign=BFD961A8821646DDC2507C8D7406027208E5CBD31F204F02200882F9658024C4)

enableCustomAnimation方法需要在调用[show](#show)方法之前调用。

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) handle | 指向自定义弹窗控制器的指针。 |
| bool enableCustomAnimation | true:使用自定义动画，关闭系统默认动画；false:使用系统默认动画。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]registerOnWillDismiss()

```c
int32_t (*registerOnWillDismiss)(ArkUI_NativeDialogHandle handle, ArkUI_OnWillDismissEvent eventHandler)
```

**描述：**

当触发系统定义的返回操作、键盘ESC关闭交互操作时，如果注册了该回调函数，弹窗不会立即关闭，而是由用户决定是否关闭。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/Px4KD5_dQDSk9g1EdgPzsQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014808Z&HW-CC-Expire=86400&HW-CC-Sign=3D6BD5F614B3B5F7B57A049737EBA96A585BE06B99EADFEA6ADFE48377BC797B)

registerOnWillDismiss方法需要在调用[show](#show)方法之前调用。

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) handle | 指向自定义弹窗控制器的指针。 |
| [ArkUI\_OnWillDismissEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-dialog-h#arkui_onwilldismissevent) eventHandler | 弹窗关闭的回调函数。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]show()

```c
int32_t (*show)(ArkUI_NativeDialogHandle handle, bool showInSubWindow)
```

**描述：**

显示自定义弹窗。

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) handle | 指向自定义弹窗控制器的指针。 |
| bool showInSubWindow | 是否在子窗口显示弹窗。true表示在子窗显示弹窗。false表示不在子窗显示弹窗。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]close()

```c
int32_t (*close)(ArkUI_NativeDialogHandle handle)
```

**描述：**

关闭自定义弹窗，如已关闭，则不生效。该接口后台执行是异步的，在关闭动画执行完成后弹窗节点才会下树。如需关闭后再次打开弹窗，请在延迟300ms以后再执行。

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) handle | 指向自定义弹窗控制器的指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。此时仅表示关闭指令下发成功，不代表弹窗完全关闭。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

#### \[h2\]registerOnWillDismissWithUserData()

```c
int32_t (*registerOnWillDismissWithUserData)(ArkUI_NativeDialogHandle handle, void* userData, void (*callback)(ArkUI_DialogDismissEvent* event))
```

**描述：**

注册系统关闭自定义弹窗的监听事件。

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h) handle | 指向自定义弹窗控制器的指针。 |
| void\* userData | 用户自定义数据指针。 |
| callback | 
监听自定义弹窗关闭的回调事件。

\- event: 回调函数的入参，捕获关闭原因。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
错误码。

[ARKUI\_ERROR\_CODE\_NO\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 成功。

[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h#arkui_errorcode) 函数参数异常。

 |

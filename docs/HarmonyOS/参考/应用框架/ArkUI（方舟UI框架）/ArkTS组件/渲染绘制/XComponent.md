---
title: "XComponent"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-xcomponent"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "ArkTS组件"
  - "渲染绘制"
  - "XComponent"
captured_at: "2026-04-17T01:47:58.373Z"
---

# XComponent

提供用于图形绘制和媒体数据写入的Surface，XComponent负责将其嵌入到视图中，支持应用自定义Surface位置和大小。具体指南请参考[自定义渲染 (XComponent)文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/napi-xcomponent-guidelines)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/RYdAFJiTTl2ITvNbDarbZg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014800Z&HW-CC-Expire=86400&HW-CC-Sign=B7F56F0892161FFE7F0E6BA39CC3D9AFBE264A966C2EE919814D01D31F73D1D6)

该组件从API version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 子组件

无

#### 接口

#### \[h2\]XComponent19+

XComponent(params: NativeXComponentParameters)

在Native侧获取XComponent节点实例、注册XComponent持有的Surface的生命周期回调和触摸、鼠标、按键等组件事件回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| params | [NativeXComponentParameters](#nativexcomponentparameters19) | 是 | 定义XComponent的具体配置参数。 |

#### \[h2\]XComponent12+

XComponent(options: XComponentOptions)

创建XComponent组件，支持在ArkTS侧获取SurfaceId、注册XComponent持有的Surface的生命周期回调和触摸、鼠标、按键等组件事件回调，支持AI分析。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [XComponentOptions](#xcomponentoptions12) | 是 | 定义XComponent的具体配置参数。 |

#### \[h2\]XComponent10+

XComponent(value: {id: string, type: XComponentType, libraryname?: string, controller?: XComponentController})

创建XComponent组件，支持Native侧触发XComponent生命周期回调。

该接口从API version 12开始不再演进，推荐使用[XComponent(options: XComponentOptions)](#xcomponent12)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| id | string | 是 | 组件的唯一标识，支持最大的字符串长度128。 |
| type | [XComponentType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#xcomponenttype10) | 是 | 用于指定XComponent组件类型。 |
| libraryname | string | 否 | 用Native层编译输出动态库名称（对应的动态库不支持跨模块加载），仅类型为SURFACE或TEXTURE时有效。 |
| controller | [XComponentController](#xcomponentcontroller) | 否 | 给组件绑定一个控制器，通过控制器调用组件方法，仅类型为SURFACE或TEXTURE时有效。 |

#### \[h2\]XComponent(deprecated)

XComponent(value: {id: string, type: string, libraryname?: string, controller?: XComponentController})

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/4jRolc-FTpuZhhfn_dRqwA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014800Z&HW-CC-Expire=86400&HW-CC-Sign=DBBE752B99E71605E8B3B2B0FFB2DB4DD0C57F8648414725E51718FA72B03BA9)

从API version 8开始支持，从API version 12开始废弃，建议使用[XComponent(value: {id: string, type: XComponentType, libraryname?: string, controller?: XComponentController})](#xcomponent10)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| id | string | 是 | 组件的唯一标识，支持最大的字符串长度128。 |
| type | string | 是 | 
用于指定XComponent组件类型，可选值仅有两个为：

\-"surface"：用于EGL/OpenGLES和媒体数据写入，开发者定制的绘制内容单独展示到屏幕上。

\-"component"9+ ：XComponent将变成一个容器组件，并可在其中执行非UI逻辑以动态加载显示内容。

其他值均会被视为"surface"类型

 |
| libraryname | string | 否 | 应用Native层编译输出动态库名称（对应的动态库不支持跨模块加载），仅XComponent类型为"surface"时有效。 |
| controller | [XComponentController](#xcomponentcontroller) | 否 | 给组件绑定一个控制器，通过控制器调用组件方法，仅XComponent类型为"surface"时有效。 |

#### XComponentOptions12+

定义XComponent的具体配置参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| type | [XComponentType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#xcomponenttype10) | 否 | 否 | 用于指定XComponent组件类型。 |
| controller | [XComponentController](#xcomponentcontroller) | 否 | 否 | 给组件绑定一个控制器，通过控制器调用组件方法，仅类型为SURFACE或TEXTURE时有效。 |
| imageAIOptions | [ImageAIOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-common#imageaioptions12) | 否 | 是 | 给组件设置一个AI分析选项，通过此项可配置分析类型或绑定一个分析控制器。 |

#### NativeXComponentParameters19+

定义XComponent的具体配置参数。通过这种构造参数创建的XComponent，可以将其对应的[FrameNode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-framenode)对象传递至Native侧，使用NDK接口进行Surface生命周期的相关设置和[监听组件事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-listen-to-component-events)。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| type | [XComponentType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#xcomponenttype10) | 否 | 否 | 用于指定XComponent组件类型。 |
| imageAIOptions | [ImageAIOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-common#imageaioptions12) | 否 | 是 | 给组件设置一个AI分析选项，通过此项可配置分析类型或绑定一个分析控制器。 |

#### 属性

除支持通用属性外，还支持以下属性：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/6C6fhIUjTMWRn_KSd3V6_A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014800Z&HW-CC-Expire=86400&HW-CC-Sign=B9373933E55506F38A9DA3E144DC0D192A7DA762DA52D45A5B13C16D938A9AE5)

不支持foregroundColor、obscured和pixelStretchEffect属性。API version 17及之前，type为SURFACE类型时也不支持动态属性设置、自定义绘制、背景设置(backgroundColor除外)、图像效果(shadow除外)、maskShape和foregroundEffect属性。从API version 18开始，type为SURFACE类型时不支持设置的动态属性包含background、foregroundColor、animation、gesture、priorityGesture、parallelGesture、useEffect、renderGroup、flexGrow、direction、align、useSizeType、clip、geometryTransition、bindPopup、bindMenu、bindContextMenu、bindContentCover、bindSheet、stateStyles、restoreId、onVisibleAreaChange、accessibilityGroup、obscured、reuseId、accessibilityVirtualNode。

对于TEXTURE和SURFACE类型的XComponent组件，当不设置[renderFit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-renderfit#renderfit)属性时，取默认值为RenderFit.RESIZE\_FILL。

对于SURFACE类型的XComponent组件，背景色设置为不透明的纯黑色，在API version 18之前，其[renderFit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-renderfit#renderfit18)通用属性仅支持设置为RenderFit.RESIZE\_FILL；在API version 18及之后，支持所有的RenderFit枚举值。

对于使用[ArkUI NDK接口](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-access-the-arkts-page)创建的XComponent组件，不支持使用属性获取函数[getAttribute](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#getattribute)获取其renderFit属性值。

#### \[h2\]enableAnalyzer12+

enableAnalyzer(enable: boolean)

设置组件支持AI分析，当前支持主体识别、文字识别和对象查找等功能。

本功能需要搭配XComponentController的[StartImageAnalyzer](#startimageanalyzer12)和[StopImageAnalyzer](#stopimageanalyzer12)一起使用。

不能和[overlay](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-overlay#overlay)属性同时使用，两者同时设置时overlay中[CustomBuilder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#custombuilder8)属性将失效。该特性依赖设备能力。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| enable | boolean | 是 | 
是否启用图像分析功能。

true：开启图像分析；false：关闭图像分析。

默认值：false

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/aSnzKO3_T4OwTOyXbeBTxw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014800Z&HW-CC-Expire=86400&HW-CC-Sign=C5CDD1852E9F0C0A4D172F23B9F7D4FA9B58C133CE6C5B53E511C848C7E52D56)

仅type为SURFACE和TEXTURE时该功能有效。

#### \[h2\]enableSecure13+

enableSecure(isSecure: boolean)

防止组件内自绘制内容被截屏、录屏。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| isSecure | boolean | 是 | 
是否开启隐私图层模式。

true：开启隐私图层模式；false：关闭隐私图层模式。

默认值：false

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/pEn7mCG7S-iUduL4FQt47Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014800Z&HW-CC-Expire=86400&HW-CC-Sign=0A5620B812193B7FB61D5753CF19E0BA4F6484C09C90D2F8F0F036C08F7CCBAF)

仅type为SURFACE时有效。

不支持[ArkUI NDK接口](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-build-ui-overview)创建的XComponent组件。

#### \[h2\]hdrBrightness20+

hdrBrightness(brightness: number)

用于调整组件播放HDR视频的亮度。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| brightness | number | 是 | 
用于调整组件播放HDR视频的亮度; brightness的取值范围为0.0~1.0; 小于0.0的值等价于0.0，大于1.0的值等价于1.0，异常值按1.0处理; 0.0 表示SDR视频的亮度，1.0 表示HDR视频的亮度。

默认值：1.0

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/0bnQUxpaQWmM7j6a8rrPaQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014800Z&HW-CC-Expire=86400&HW-CC-Sign=78849695E1CAE5F3F119B6C2FB3C579F635DBDDB37818862BAAAC814BF6AA140)

仅type为SURFACE时有效。

不支持[ArkUI NDK接口](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-build-ui-overview)创建的XComponent组件。

#### 事件

从API version 12开始，type为SURFACE或TEXTURE时，支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-events)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/eqg4NzutQcyOF-zfi9Kdbg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014800Z&HW-CC-Expire=86400&HW-CC-Sign=52C8F9CAC20DBC2921A0C793716EEC5BF6ECF5647113076222A65053DE387857)

当配置libraryname参数时，[点击事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-click)、[触摸事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-touch)、[挂载卸载事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-show-hide)、[按键事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-key)、[焦点事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-focus-event)、[鼠标事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-mouse-key)仅响应C-API侧事件接口。

仅type为SURFACE或TEXTURE时以下事件有效：

#### \[h2\]onLoad

onLoad(callback: OnNativeLoadCallback )

插件加载完成时回调事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | [OnNativeLoadCallback](#onnativeloadcallback18) | 是 | XComponent持有的Surface创建后回调事件。 |

#### \[h2\]onDestroy

onDestroy(event: VoidCallback )

插件卸载完成时回调事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| event | [VoidCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#voidcallback12) | 是 | XComponent销毁后回调事件。 |

#### OnNativeLoadCallback18+

type OnNativeLoadCallback = (event?: object) => void

XComponent持有的Surface创建后回调事件。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| event | object | 否 | 获取XComponent实例对象的context，context上挂载的方法由开发者在Native层定义。 |

#### XComponentController

XComponent组件的控制器，可以将此对象绑定至XComponent组件，然后通过控制器来调用组件方法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]constructor

constructor()

XComponentController的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ts
xcomponentController: XComponentController = new XComponentController();
```

#### \[h2\]getXComponentSurfaceId9+

getXComponentSurfaceId(): string

获取XComponent对应Surface的ID，仅XComponent类型为SURFACE("surface")或TEXTURE时有效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | XComponent持有Surface的ID。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/jKhoH3hfQCyOfpwhUYEIFQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014800Z&HW-CC-Expire=86400&HW-CC-Sign=6EB6557B25E35A683D583A5D5E50578BB8D6887AE7F930E194992404B6A7CE45)

使用自定义组件节点创建XComponent组件时，因为onLoad回调触发时机早于[onSurfaceCreated](#onsurfacecreated12)，所以在onLoad回调中调用[getXComponentSurfaceId](#getxcomponentsurfaceid9)获取surfaceId会失败，建议在[onSurfaceCreated](#onsurfacecreated12)回调中获取。

**示例：**

```ts
// xxx.ets
@Entry
@Component
struct Index {
  myXComponentController: XComponentController = new XComponentController();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      XComponent({
        type: XComponentType.SURFACE,
        controller: this.myXComponentController
      })
        .onLoad(() => {
          let surfaceId: string = this.myXComponentController.getXComponentSurfaceId();
          console.info("XComponent SurfaceId: " + surfaceId);
        })
    }
  }
}
```

#### \[h2\]setXComponentSurfaceSize(deprecated)

setXComponentSurfaceSize(value: {surfaceWidth: number, surfaceHeight: number}): void

设置XComponent持有Surface的宽度和高度，仅XComponent类型为SURFACE("surface")或TEXTURE时有效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/spjwCRgUT-ubJyX5eJhoFA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014800Z&HW-CC-Expire=86400&HW-CC-Sign=B67150B51FE6736C60BAC4D5A0D0ACA622767F543B12A04AB9961F2B6E987CEB)

该接口从API version 9开始支持，从API version 12开始废弃，建议使用[setXComponentSurfaceRect](#setxcomponentsurfacerect12)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| surfaceWidth | number | 是 | XComponent持有Surface的宽度。 |
| surfaceHeight | number | 是 | XComponent持有Surface的高度。 |

#### \[h2\]getXComponentContext

getXComponentContext(): Object

获取XComponent实例对象的context，仅XComponent类型为SURFACE("surface")或TEXTURE时有效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Object | 获取XComponent实例对象的context，context包含的具体接口方法由开发者自定义，context内容与onLoad回调中的第一个参数一致。 |

#### \[h2\]setXComponentSurfaceRect12+

setXComponentSurfaceRect(rect: SurfaceRect): void

设置XComponent持有Surface的显示区域，包括宽高和相对于组件左上角的位置坐标，仅XComponent类型为SURFACE("surface")或TEXTURE时有效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| rect | [SurfaceRect](#surfacerect12对象说明) | 是 | XComponent持有Surface的显示区域。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/l7X3MpM4QOOVkt9KlZD4Tg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014800Z&HW-CC-Expire=86400&HW-CC-Sign=471FC62B29000F226ED92A74B38700939CF637FC1FB8E5E6E5051BC56B4E5629)

rect参数中的offsetX/offsetY不设置或传入异常值时，Surface显示区域相对于XComponent左上角x/y轴的偏移效果默认按照居中显示。

rect参数中的surfaceWidth和surfaceHeight存在0、负数或其他异常值时，调用该接口设置显示区域不生效。未调用该接口主动设置Surface显示区域时，surfaceWidth默认与组件宽度一致，surfaceHeight默认与组件高度一致。

该方法优先级高于[border](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-border#border)、[padding](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#padding)等可以改变内容偏移和大小的属性。

#### \[h2\]getXComponentSurfaceRect12+

getXComponentSurfaceRect(): SurfaceRect

获取XComponent持有Surface的显示区域，包括宽高和相对于组件左上角的位置坐标，仅XComponent类型为SURFACE("surface")或TEXTURE时有效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [SurfaceRect](#surfacerect12对象说明) | 获取XComponent持有Surface的显示区域。 |

#### \[h2\]onSurfaceCreated12+

onSurfaceCreated(surfaceId: string): void

当XComponent持有的Surface创建后进行该回调，仅XComponent类型为SURFACE("surface")或TEXTURE时有效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| surfaceId | string | 是 | 回调该方法的时候，绑定XComponent持有Surface的ID。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/Jv0nrg9GRiWK07Q4sGtJXQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014800Z&HW-CC-Expire=86400&HW-CC-Sign=F54B0F5BA34783B2C7FA98B67E1A02B8D350C540224F34DDB67B3F4631858A94)

仅当XComponent组件未设置libraryname参数时，会进行该回调。

#### \[h2\]onSurfaceChanged12+

onSurfaceChanged(surfaceId: string, rect: SurfaceRect): void

当XComponent持有的Surface大小改变后（包括首次创建时的大小改变）进行该回调，仅XComponent类型为SURFACE("surface")或TEXTURE时有效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| surfaceId | string | 是 | 回调该方法的时候，绑定XComponent持有Surface的ID。 |
| rect | [SurfaceRect](#surfacerect12对象说明) | 是 | 回调该方法的时候，绑定XComponent持有Surface的显示区域。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/WuAZHYhYTympi2qiixixaQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014800Z&HW-CC-Expire=86400&HW-CC-Sign=ED73085483EC54C61C0EBE5B31165C23475B987F15F616546DCE1B39B826CB32)

仅当XComponent组件未设置libraryname参数时，会进行该回调。

#### \[h2\]onSurfaceDestroyed12+

onSurfaceDestroyed(surfaceId: string): void

当XComponent持有的Surface销毁后进行该回调，仅XComponent类型为SURFACE("surface")或TEXTURE时有效，具体可以参考指南[创建XComponent和管理Surface生命周期](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/napi-xcomponent-guidelines#创建xcomponent和管理surface生命周期)章节。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| surfaceId | string | 是 | 回调该方法的时候，绑定XComponent持有Surface的ID。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/zv1hypVGRu-eGz7JIUKK2Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014800Z&HW-CC-Expire=86400&HW-CC-Sign=38DD2B8ABF038AB9D02D069E3E53905CFDCA914B126EB690015D298E7E776D75)

仅当XComponent组件未设置libraryname参数时，会进行该回调。

#### \[h2\]startImageAnalyzer12+

startImageAnalyzer(config: ImageAnalyzerConfig): Promise<void>

配置AI分析并启动AI分析功能，使用前需先[启用图像AI分析能力](#enableanalyzer12)。使用Promise异步回调。

该方法调用时，将截取调用时刻的画面帧进行分析，使用时需注意启动分析的时机，避免出现画面和分析内容不一致的情况。

若该方法尚未执行完毕，此时重复调用，则会触发错误回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/H600kzOGR225u-KwszbfNg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014800Z&HW-CC-Expire=86400&HW-CC-Sign=CA7EACCF94D58137BF6C5769008161AB4214FB932721F42C2076444EDA782C01)

分析类型不支持动态修改。

该特性依赖设备能力，不支持该能力的情况下，将返回错误码。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| config | [ImageAnalyzerConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-common#imageanalyzerconfig12) | 是 | 执行AI分析所需要的入参，用于配置AI分析功能。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象，无返回结果。用于获取AI分析是否成功执行。 |

**错误码：**

以下错误码的详细介绍请参见[图像AI分析错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-image-analyzer)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 110001 | Image analysis feature is unsupported. |
| 110002 | Image analysis is currently being executed. |
| 110003 | Image analysis is stopped. |

#### \[h2\]stopImageAnalyzer12+

stopImageAnalyzer(): void

停止AI分析功能，AI分析展示的内容将被销毁。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/HFkgKnG3SJO_bCdaY6N4CA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014800Z&HW-CC-Expire=86400&HW-CC-Sign=F6BD55763D1CDD486E2E6B55953B49A2D95D38EB7E854EF2DB9410B85C535B52)

在startImageAnalyzer方法未返回结果时调用本方法，会触发其错误回调。

该特性依赖设备能力。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]setXComponentSurfaceRotation12+

setXComponentSurfaceRotation(rotationOptions: SurfaceRotationOptions): void

设置XComponent持有Surface在屏幕旋转时是否锁定方向，仅XComponent类型为SURFACE("surface")时有效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| rotationOptions | [SurfaceRotationOptions](#surfacerotationoptions12对象说明) | 是 | 设置XComponent持有Surface在屏幕旋转时是否锁定方向。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/7SdxLtZ3Ts6LkQAF0Kw3eg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014800Z&HW-CC-Expire=86400&HW-CC-Sign=F9E859F57BF7AD4ED8BEFAFB0DE3E115C7BDCB61D4072965129298BC583E7A7A)

rotationOptions未配置时，默认XComponent持有Surface在屏幕旋转时不锁定方向，跟随屏幕进行旋转。

仅在屏幕旋转过程中生效，旋转完成后不再锁定Surface。

仅在屏幕旋转90°，即发生横竖屏切换时生效。

锁定旋转后的Buffer宽高需要保持不变，否则会有拉伸问题。

#### \[h2\]getXComponentSurfaceRotation12+

getXComponentSurfaceRotation(): Required<SurfaceRotationOptions>

获取XComponent持有Surface在屏幕旋转时是否锁定方向的设置，仅XComponent类型为SURFACE("surface")时有效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Required<[SurfaceRotationOptions](#surfacerotationoptions12对象说明)\> | 获取XComponent持有Surface在屏幕旋转时是否锁定方向的设置。 |

#### \[h2\]lockCanvas20+

lockCanvas(): DrawingCanvas | null

返回可用于向XComponent上绘制内容的画布对象。具体绘制方法请参考[Canvas](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-canvas)。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [DrawingCanvas](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-drawingrenderingcontext#drawingcanvas12对象说明) | null | 可用于向XComponent区域绘制的画布对象或者空对象null。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/kvgUHFz8R-qxfJGdcYtJmQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014800Z&HW-CC-Expire=86400&HW-CC-Sign=CE2387B356E245CE3E57B529F4A9ACE9D5B5AD9A27578C747EBB26CCBF2FE19F)

如果当前XComponent状态无法获取画布对象则将返回null。原因通常为：

1.  XComponent持有的Surface未创建完成（可通过设置[onLoad](#onload)/[onSurfaceCreated](#onsurfacecreated12)回调来确定，此回调触发时，Surface已创建完成）。
    
2.  之前已经调用过lockCanvas来获取过画布对象，且该画布对象未调用[unlockCanvasAndPost](#unlockcanvasandpost20)去释放。
    

只支持TEXTURE和SURFACE模式。

使用此接口后，同时在NDK侧获取NativeWindow并调用相关接口进行绘制，可能出现缓冲区竞争和上下文冲突而发生绘制画面错误等异常，因此不允许使用。

此接口需要和[unlockCanvasAndPost](#unlockcanvasandpost20)接口配对使用，具体参考[示例3使用画布对象在XComponent上绘制内容](#示例3使用画布对象在xcomponent上绘制内容)。

#### \[h2\]unlockCanvasAndPost20+

unlockCanvasAndPost(canvas: DrawingCanvas): void

将画布对象中的内容绘制在XComponent区域，并释放该画布对象。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| canvas | [DrawingCanvas](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-drawingrenderingcontext#drawingcanvas12对象说明) | 是 | 之前调用lockCanvas方法返回的画布对象。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/KRxwlqwLR1mdqtMDIZiynA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014800Z&HW-CC-Expire=86400&HW-CC-Sign=718E4A8B9FC94C137234FC22EB7666A84F0113D552230455F189412CA9C9D529)

1.  画布对象调用unlockCanvasAndPost释放后，不可再使用该画布对象。
    
2.  只支持TEXTURE和SURFACE模式。
    
3.  使用此接口后，同时在NDK侧获取NativeWindow并调用相关接口进行绘制，可能出现缓冲区竞争和上下文冲突而发生绘制画面错误等异常，因此不允许使用。
    
4.  此接口需要和[lockCanvas](#lockcanvas20)接口配对使用，具体参考[示例3使用画布对象在XComponent上绘制内容](#示例3使用画布对象在xcomponent上绘制内容)。
    

#### \[h2\]setXComponentSurfaceConfig22+

setXComponentSurfaceConfig(config: SurfaceConfig): void

设置XComponent创建的Surface的选项，用于设置XComponent持有的Surface在渲染时是否需要被视为不透明。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/lKkfjYcwRHqhj2ovXxAtfg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014800Z&HW-CC-Expire=86400&HW-CC-Sign=BA286677F4CAE3407A8FF95AA57518D388B2CC890A6B0FA17727DF126610F461)

仅当XComponent组件类型为TEXTURE或SURFACE时，本接口生效。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| config | [SurfaceConfig](#surfaceconfig22对象说明) | 是 | Surface选项。 |

#### SurfaceRotationOptions12+对象说明

用于描述XComponent持有Surface在屏幕旋转时是否锁定方向的设置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| lock | boolean | 否 | 是 | 
Surface在屏幕旋转时是否锁定方向，未设置时默认取值为false，即不锁定方向。

true：锁定方向；false：不锁定方向。

 |

#### SurfaceRect12+对象说明

用于描述XComponent持有Surface的显示区域。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| offsetX | number | 否 | 是 | Surface显示区域相对于XComponent组件左上角的x轴坐标，单位：px。 |
| offsetY | number | 否 | 是 | Surface显示区域相对于XComponent组件左上角的y轴坐标，单位：px。 |
| surfaceWidth | number | 否 | 否 | Surface显示区域的宽度，单位：px。 |
| surfaceHeight | number | 否 | 否 | Surface显示区域的高度，单位：px。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/A2YoHXGJRoyxKVi-iplxVw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014800Z&HW-CC-Expire=86400&HW-CC-Sign=C102B7CAE0C1EEF5E776B5FA0E8607F4706DC1D3C60F65F522EFBF6361F47E7A)

surfaceWidth和surfaceHeight属性在未调用[setXComponentSurfaceRect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-xcomponent#setxcomponentsurfacerect12)也未设置[border](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-border#border)和[padding](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#padding)等属性时，其取值大小为XComponent组件的大小。

surfaceWidth和surfaceHeight属性的取值都不可超过8192px，否则会导致渲染异常。

沉浸式场景下，默认布局的SurfaceRect不包括安全区，需调用[setXComponentSurfaceRect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-xcomponent#setxcomponentsurfacerect12)接口主动设置Surface显示区域达到沉浸式效果。

#### SurfaceConfig22+对象说明

用于描述XComponent持有的Surface在渲染时是否需要被视为不透明。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| isOpaque | boolean | 否 | 是 | 
XComponent持有的Surface在渲染时是否需要被视为不透明，未设置时默认取值为false，即在渲染时会应用Surface中绘制内容像素的透明度。

true表示需要被视为不透明，false表示不需要被视为不透明。

默认值：false

 |

#### 示例

示例效果请以真机运行为准，当前DevEco Studio预览器不支持。

#### \[h2\]示例1（图像AI分析功能）

使用enableAnalyzer属性开启图像AI分析功能。可通过XComponentController控制开始、停止图形AI分析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/ZdvidIoRS6W2H9x6pJUjhA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014800Z&HW-CC-Expire=86400&HW-CC-Sign=E53354E9B7353D28504C8A4BE73EB7D9733B137C9D511C73C3BD9F7B841FFE06)

本示例画图逻辑具体实现（和nativeRender相关的函数实现）可以参考[ArkTS XComponent示例](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/ArkTSXComponent)

```ts
// xxx.ets
import { BusinessError } from '@kit.BasicServicesKit';
import nativeRender from 'libnativerender.so';// 开发者自己实现的so，详见上述说明。

class CustomXComponentController extends XComponentController {
  onSurfaceCreated(surfaceId: string): void {
    console.info(`onSurfaceCreated surfaceId: ${surfaceId}`);
    nativeRender.SetSurfaceId(BigInt(surfaceId));
  }

  onSurfaceChanged(surfaceId: string, rect: SurfaceRect): void {
    console.info(`onSurfaceChanged surfaceId: ${surfaceId}, rect: ${JSON.stringify(rect)}`);
    nativeRender.ChangeSurface(BigInt(surfaceId), rect.surfaceWidth, rect.surfaceHeight);
  }

  onSurfaceDestroyed(surfaceId: string): void {
    console.info(`onSurfaceDestroyed surfaceId: ${surfaceId}`);
    nativeRender.DestroySurface(BigInt(surfaceId));
  }
}

@Entry
@Component
struct XComponentExample {
  xComponentController: XComponentController = new CustomXComponentController();
  private config: ImageAnalyzerConfig = {
    types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT]
  };
  private aiController: ImageAnalyzerController = new ImageAnalyzerController();
  private options: ImageAIOptions = {
    types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT],
    aiController: this.aiController
  };
  @State xcWidth: string = "720px";
  @State xcHeight: string = "720px";
  @State currentStatus: string = "index";

  build() {
    Column({ space: 5 }) {
      Row() {
        Text('Native XComponent Sample')
          .fontSize('24fp')
          .fontWeight(500)
          .margin({
            left: 24,
            top: 12
          })
      }
      .margin({ top: 24 })
      .width('100%')
      .height(56)

      XComponent({
        type: XComponentType.SURFACE,
        controller: this.xComponentController,
        imageAIOptions: this.options
      })
        .width(this.xcWidth)
        .height(this.xcHeight)
        .enableAnalyzer(true)
        .onClick(() => {
          let surfaceId = this.xComponentController.getXComponentSurfaceId();
          nativeRender.ChangeColor(BigInt(surfaceId));
          let hasChangeColor: boolean = false;
          if (nativeRender.GetXComponentStatus(BigInt(surfaceId))) {
            hasChangeColor = nativeRender.GetXComponentStatus(BigInt(surfaceId)).hasChangeColor;
          }
          if (hasChangeColor) {
            this.currentStatus = "change color";
          }
        })
      Text(this.currentStatus)
        .fontSize('24fp')
        .fontWeight(500)
      Column() {
        Button('start AI analyze')
          .onClick(() => {
            this.xComponentController.startImageAnalyzer(this.config)
              .then(() => {
                console.info("analysis complete");
              })
              .catch((error: BusinessError) => {
                console.error("error code: " + error.code);
              })
          })
          .margin(2)
        Button('stop AI analyze')
          .onClick(() => {
            this.xComponentController.stopImageAnalyzer();
          })
          .margin(2)
        Button('get analyzer types')
          .onClick(() => {
            this.aiController.getImageAnalyzerSupportTypes();
          })
          .margin(2)
        Button('Draw Star')
          .fontSize('16fp')
          .fontWeight(500)
          .margin({ bottom: 24 })
          .onClick(() => {
            let surfaceId = this.xComponentController.getXComponentSurfaceId();
            console.info(`surface rect is ${this.xComponentController.getXComponentSurfaceRect()}`);
            nativeRender.DrawPattern(BigInt(surfaceId));
            let hasDraw: boolean = false;
            if (nativeRender.GetXComponentStatus(BigInt(surfaceId))) {
              hasDraw = nativeRender.GetXComponentStatus(BigInt(surfaceId)).hasDraw;
            }
            if (hasDraw) {
              this.currentStatus = "draw star";
            }
          })
          .margin(2)
      }.justifyContent(FlexAlign.Center)
    }
    .width("100%")
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/ipFG3KmTTGGiWzqiWAUcuA/zh-cn_image_0000002568900671.gif?HW-CC-KV=V1&HW-CC-Date=20260417T014800Z&HW-CC-Expire=86400&HW-CC-Sign=7D062804199CDABF6448887DB7B9C47DCCDE67B8E41B243C1344A96B6A5CC6D6)

#### \[h2\]示例2（在surface旋转过程中锁定）

通过setXComponentSurfaceRotation设置surface在屏幕旋转过程中锁定方向，不跟随屏幕进行旋转。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/_JH4i6PRRv-XeSPSaT5TzA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014800Z&HW-CC-Expire=86400&HW-CC-Sign=42EDC07B68FF86F4B67BEDE57F746C15D562A1437AAC6975F1F624CD67B130FC)

本示例画图逻辑具体实现（和nativeRender相关的函数实现）可以参考[ArkTS XComponent示例](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/BasicFeature/Native/ArkTSXComponent)。

```ts
// xxx.ets
import nativeRender from 'libnativerender.so';

class MyXComponentController extends XComponentController {
  onSurfaceCreated(surfaceId: string): void {
    console.info(`onSurfaceCreated surfaceId: ${surfaceId}`);
    nativeRender.SetSurfaceId(BigInt(surfaceId));
  }

  onSurfaceChanged(surfaceId: string, rect: SurfaceRect): void {
    console.info(`onSurfaceChanged surfaceId: ${surfaceId}, rect: ${JSON.stringify(rect)}}`);
    nativeRender.ChangeSurface(BigInt(surfaceId), rect.surfaceWidth, rect.surfaceHeight);
  }

  onSurfaceDestroyed(surfaceId: string): void {
    console.info(`onSurfaceDestroyed surfaceId: ${surfaceId}`);
    nativeRender.DestroySurface(BigInt(surfaceId));
  }
}

@Entry
@Component
struct Index {
  @State isLock: boolean = true;
  @State xc_width: number = 500;
  @State xc_height: number = 700;
  myXComponentController: XComponentController = new MyXComponentController();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Start }) {
      XComponent({
        id: "XComponent",
        type: XComponentType.SURFACE,
        controller: this.myXComponentController
      })
        .onLoad(() => {
          let surfaceRotation: SurfaceRotationOptions = { lock: this.isLock };
          this.myXComponentController.setXComponentSurfaceRotation(surfaceRotation);
          console.info("Surface getXComponentSurfaceRotation lock = " +
          this.myXComponentController.getXComponentSurfaceRotation().lock);
        })
        .width(this.xc_width)
        .height(this.xc_height)
      Button("Draw")
        .onClick(() => {
          let surfaceId = this.myXComponentController.getXComponentSurfaceId();
          nativeRender.DrawPattern(BigInt(surfaceId));
        })
    }
  }
}
```

#### \[h2\]示例3（使用画布对象在XComponent上绘制内容）

从API version 20开始，该示例通过调用[lockCanvas](#lockcanvas20)返回画布对象，通过画布对象调用对应的绘制接口，再调用[unlockCanvasAndPost](#unlockcanvasandpost20)在XComponent上绘制内容。

```ts
// xxx.ets
import { drawing } from '@kit.ArkGraphics2D';

@Entry
@Component
struct Index {
  private xcController: XComponentController = new XComponentController();
  private mCanvas: DrawingCanvas | null = null;

  build() {
    Column() {
      XComponent({ type: XComponentType.SURFACE, controller: this.xcController })
        .width("80%")
        .height("80%")
        .onLoad(() => {
          this.mCanvas = this.xcController.lockCanvas();
          if (this.mCanvas) {
            this.mCanvas.drawColor(255, 240, 250, 255); // 每次绘制前必须完全重绘整个XComponent区域,可以调用此方法实现
            const brush = new drawing.Brush(); // 创建画刷对象
            brush.setColor({ // 设置画刷的颜色
              alpha: 255,
              red: 39,
              green: 135,
              blue: 217
            });
            this.mCanvas.attachBrush(brush); // 绑定画刷到画布上
            this.mCanvas.drawRect({ // 绘制一个矩形
              left: 300,
              right: 800,
              top: 100,
              bottom: 800
            });
            this.mCanvas.detachBrush(); // 将画刷与画布解绑
            this.xcController.unlockCanvasAndPost(this.mCanvas);
          }
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/KIxfO8PHTse0R8cjzpNf6g/zh-cn_image_0000002538020970.png?HW-CC-KV=V1&HW-CC-Date=20260417T014800Z&HW-CC-Expire=86400&HW-CC-Sign=3DDE9DE297037B055656789FE1513DEA15B7EF2E68B6CC65F1C5E255568CDC4E)

#### \[h2\]示例4（XComponent实现沉浸式效果）

从API version 20开始，在示例3的基础上，调用setXComponentSurfaceRect接口主动设置Surface显示区域达到沉浸式效果。

```ts
// xxx.ets
import { drawing } from '@kit.ArkGraphics2D';
import { display } from '@kit.ArkUI'
@Entry
@Component
struct Index {
  private xcController: XComponentController = new XComponentController();
  private mCanvas: DrawingCanvas | null = null;
  @State screenWidth: number = 0;
  @State screenHeight:number = 0;
  aboutToAppear() {
    try {
      const displayClass = display.getDefaultDisplaySync();
      this.screenWidth = displayClass.width;
      this.screenHeight = displayClass.height;
    } catch (error) {
      console.error(`失败代码: ${error.code}，信息: ${error.message}`);
    }
  }

  build() {
    Column() {
      XComponent({ type: XComponentType.SURFACE, controller: this.xcController })
        .width("100%")
        .height("100%")
        .onLoad(() => {
          // 请在此处设置Surface大小，过大可能会导致绘制时间长
          this.xcController.setXComponentSurfaceRect({surfaceWidth: this.screenWidth, surfaceHeight: this.screenHeight, offsetX: 0, offsetY: 0});
          this.mCanvas = this.xcController.lockCanvas();
          if (this.mCanvas) {
            this.mCanvas.drawColor(255, 39, 135, 217); // 每次绘制前必须完全重绘整个XComponent区域，可以调用此方法实现
            this.xcController.unlockCanvasAndPost(this.mCanvas);
          }
        })
        .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
    }
    .height('100%')
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/aRxE0dkySf2SmhJ-cM1bzA/zh-cn_image_0000002538180896.jpeg?HW-CC-KV=V1&HW-CC-Date=20260417T014800Z&HW-CC-Expire=86400&HW-CC-Sign=57200D52FA0327DCED9B6DB6328985617DCCF467C979C0384073D55981659C17)

#### \[h2\]示例5（设置XComponent持有Surface在渲染时是否需要被视为不透明）

从API version 22开始，该示例通过调用[setXComponentSurfaceConfig](#setxcomponentsurfaceconfig22)接口设置XComponent持有的Surface在渲染时是否需要被视为不透明。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/pvWgc93gQHWwO8B94P8B1g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014800Z&HW-CC-Expire=86400&HW-CC-Sign=BE9D1366BF4E6CA27FDD599D05E007FE2E458DB1006BF635852E85128BDC3639)

本示例画图逻辑具体实现（和nativeRender相关的函数实现）可以参考[ArkTS XComponent示例](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/BasicFeature/Native/ArkTSXComponent)。

```ts
// xxx.ets
import nativeRender from 'libnativerender.so'; // 开发者自己实现的so，详见上述说明。

// 重写XComponentController，设置生命周期回调
class MyXComponentController extends XComponentController{
  onSurfaceCreated(surfaceId: string): void {
    console.info(`onSurfaceCreated surfaceId: ${surfaceId}`);
    nativeRender.SetSurfaceId(BigInt(surfaceId));
  }
  onSurfaceChanged(surfaceId: string, rect: SurfaceRect): void {
    console.info(`onSurfaceChanged surfaceId: ${surfaceId}, rect: ${JSON.stringify(rect)}`);
    // 在onSurfaceChanged中调用ChangeSurface绘制内容
    nativeRender.ChangeSurface(BigInt(surfaceId), rect.surfaceWidth, rect.surfaceHeight);
  }
  onSurfaceDestroyed(surfaceId: string): void {
    console.info(`onSurfaceDestroyed surfaceId: ${surfaceId}`);
    nativeRender.DestroySurface(BigInt(surfaceId));
  }
}

@Entry
@Component
struct Index {
  @State currentStatus: string = "index";
  xComponentController: XComponentController = new MyXComponentController();

  aboutToAppear(): void {
    // 设置XComponent持有的Surface在渲染时被视为不透明
    this.xComponentController.setXComponentSurfaceConfig({ isOpaque: true });
  }

  build() {
    Column() {
      Column({ space: 10 }) {
        XComponent({
          type: XComponentType.SURFACE,
          controller: this.xComponentController
        })
          .backgroundColor(Color.Transparent)
        Text(this.currentStatus)
          .fontSize('24fp')
          .fontWeight(500)
      }
      .onClick(() => {
        let surfaceId = this.xComponentController.getXComponentSurfaceId();
        nativeRender.ChangeColor(BigInt(surfaceId));
        let hasChangeColor: boolean = false;
        if (nativeRender.GetXComponentStatus(BigInt(surfaceId))) {
          hasChangeColor = nativeRender.GetXComponentStatus(BigInt(surfaceId)).hasChangeColor;
        }
        if (hasChangeColor) {
          this.currentStatus = "change color";
        }
      })
      .margin({
        top: 27,
        left: 12,
        right: 12
      })
      .height('40%')
      .width('90%')
      Row() {
        Button('Draw Star')
          .fontSize('16fp')
          .fontWeight(500)
          .margin({ bottom: 24 })
          .onClick(() => {
            let surfaceId = this.xComponentController.getXComponentSurfaceId();
            nativeRender.DrawPattern(BigInt(surfaceId));
            let hasDraw: boolean = false;
            if (nativeRender.GetXComponentStatus(BigInt(surfaceId))) {
              hasDraw = nativeRender.GetXComponentStatus(BigInt(surfaceId)).hasDraw;
            }
            if (hasDraw) {
              this.currentStatus = "draw star";
            }
          })
          .width('53.6%')
          .height(40)
      }
      .width('100%')
      .justifyContent(FlexAlign.Center)
      .alignItems(VerticalAlign.Bottom)
      .layoutWeight(1)
    }
    .width('100%')
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/DJGsvdmyTpaUQpcx5x7oYQ/zh-cn_image_0000002569020683.jpeg?HW-CC-KV=V1&HW-CC-Date=20260417T014800Z&HW-CC-Expire=86400&HW-CC-Sign=469C6CD506631A91715984B988BB9448D212B5B2EA633008C4AF31DBB5CE1A4A)

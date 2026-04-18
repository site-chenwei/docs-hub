---
title: "NavRouter"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navrouter"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "ArkTS组件"
  - "已停止维护的组件与接口"
  - "NavRouter"
captured_at: "2026-04-17T01:48:00.319Z"
---

# NavRouter

导航组件，默认提供点击响应处理，不需要开发者自定义点击事件逻辑。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/MLvQX9_qTUaPb9HMnKqGIQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014802Z&HW-CC-Expire=86400&HW-CC-Sign=08F1251E4532F7C830C617F9A2B9362EBFDA9DF566C41C6BC474CDCAA70EE1B5)

从API version 13开始，该组件不再维护，推荐使用[NavPathStack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#navpathstack10)配合navDestination属性进行页面路由。

该组件从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 子组件

必须包含两个子组件，其中第二个子组件必须为[NavDestination](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/HKYs46ffTwqIzfjB9BL3-g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014802Z&HW-CC-Expire=86400&HW-CC-Sign=7321C3B176E2143BEF19F717B68608A672749B47737D0D01F57BE4242867A1CA)

子组件个数异常时：

1.  有且仅有1个时，触发路由到NavDestination的能力失效。
2.  有且仅有1个时，且使用NavDestination场景下，不进行路由。
3.  大于2个时，后续的子组件不显示。
4.  第二个子组件不为NavDestination时，触发路由功能失效。

#### 接口

#### \[h2\]NavRouter(deprecated)

NavRouter()

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/E7OVR5fsQ7eILv5eL8FhEQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014802Z&HW-CC-Expire=86400&HW-CC-Sign=54349907EF6F3DB518532BFBF8CE73ECE7A4A0246CF2BD76BC7AE6538C3AE085)

从API version 9开始支持，从API version 13开始废弃，建议使用[NavPathStack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#navpathstack10)和[navDestination](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#navdestination10)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]NavRouter(deprecated)

NavRouter(value: RouteInfo)

提供路由信息，指定点击NavRouter时，要跳转的NavDestination页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/e-O3EQZ8T_OVNYi88-pFIQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014802Z&HW-CC-Expire=86400&HW-CC-Sign=90632104E15A731880FC9D4B25396AC768144986CE367130F47C33914316117D)

从API version 10开始支持，从API version 13开始废弃，建议使用[NavPathStack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#navpathstack10)和[navDestination](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#navdestination10)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| value | [RouteInfo](#routeinfodeprecated对象说明) | 是 | 路由信息。 |

#### 属性

除支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)外，还支持以下属性：

#### \[h2\]mode(deprecated)

mode(mode: NavRouteMode)

设置指定点击NavRouter跳转到NavDestination页面时，使用的路由模式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/Blbf7d4XQaOyTg2RozXMtQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014802Z&HW-CC-Expire=86400&HW-CC-Sign=E71AA66DBF3E6394E0F3C517D4B69AB1A37C6FC8BDF71508C981DB14F2FC1C6E)

从API version 10开始支持，从API version 13开始废弃，建议使用[LaunchMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#launchmode12枚举说明)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| mode | [NavRouteMode](#navroutemodedeprecated枚举说明) | 是 | 
指定点击NavRouter跳转到NavDestination页面时，使用的路由模式。

默认值：NavRouteMode.PUSH\_WITH\_RECREATE

 |

#### RouteInfo(deprecated)对象说明

路由信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| name | string | 否 | 否 | 
点击NavRouter跳转到的NavDestination页面的名称。

**说明：**

从API version 10开始支持，从API version 13开始废弃，建议使用[name](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#属性-1)替代。

 |
| param | unknown | 否 | 是 | 

点击NavRouter跳转到NavDestination页面时，传递的参数。

**说明：**

从API version 10开始支持，从API version 13开始废弃，建议使用[param](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#属性-1)替代。

 |

#### NavRouteMode(deprecated)枚举说明

路由模式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/ZZx5j7xJTVOWBV9YxEJnJw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014802Z&HW-CC-Expire=86400&HW-CC-Sign=408C89020656E96CF107DA51CAF39F1DF39F6C147D25862E27679192E8BB2B34)

从API version 10开始支持，从API version 13开始废弃，建议使用[NavPathStack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#navpathstack10)和[navDestination](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#navdestination10)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 说明 |
| :-- | :-- |
| PUSH\_WITH\_RECREATE | 跳转到新的NavDestination页面时，替换当前显示的NavDestination页面，页面销毁，但该页面信息仍保留在路由栈中。 |
| PUSH | 跳转到新的NavDestination页面时，覆盖当前显示的NavDestination页面，该页面不销毁，且页面信息保留在路由栈中。 |
| REPLACE | 跳转到新的NavDestination页面时，替换当前显示的NavDestination页面，页面销毁，且该页面信息从路由栈中清除。 |

#### 事件

#### \[h2\]onStateChange(deprecated)

onStateChange(callback: (isActivated: boolean) => void)

组件激活状态切换时触发该回调。开发者点击激活NavRouter，加载对应的NavDestination子组件时，回调onStateChange(true)。NavRouter对应的NavDestination子组件不再显示时，回调onStateChange(false)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/vJ75FHUeQMeP_QvDKmiSVw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014802Z&HW-CC-Expire=86400&HW-CC-Sign=F2297815DC6B2EF8B94806884183960716FCF7D178F3E7FB4E069950EC73FF68)

从API version 9开始支持，从API version 13开始废弃，建议使用[onShown](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination#onshown10)和[onHidden](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination#onhidden10)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| isActivated | boolean | 是 | isActivated为true时表示激活，为false时表示未激活。 |

#### 示例

```ts
// xxx.ets
@Entry
@Component
struct NavRouterExample {
  @State isActiveWLAN: boolean = false
  @State isActiveBluetooth: boolean = false

  build() {
    Navigation() {
      NavRouter() {
        Row() {
          Row()
            .width(30)
            .height(30)
            .borderRadius(30)
            .margin({ left: 3, right: 10 })
            .backgroundColor(Color.Pink)
          Text(`WLAN`)
            .fontSize(22)
            .fontWeight(500)
            .textAlign(TextAlign.Center)
        }
        .width('90%')
        .height(60)

        NavDestination() {
          Flex({ direction: FlexDirection.Row }) {
            Text('未找到可用WLAN').fontSize(30).padding({ left: 15 })
          }
        }.title("WLAN")
      }
      .margin({ top: 10, bottom: 10 })
      .backgroundColor(this.isActiveWLAN ? '#ccc' : '#fff')
      .borderRadius(20)
      .mode(NavRouteMode.PUSH_WITH_RECREATE)
      .onStateChange((isActivated: boolean) => {
        this.isActiveWLAN = isActivated
      })

      NavRouter() {
        Row() {
          Row()
            .width(30)
            .height(30)
            .borderRadius(30)
            .margin({ left: 3, right: 10 })
            .backgroundColor(Color.Pink)
          Text(`蓝牙`)
            .fontSize(22)
            .fontWeight(500)
            .textAlign(TextAlign.Center)
        }
        .width('90%')
        .height(60)

        NavDestination() {
          Flex({ direction: FlexDirection.Row }) {
            Text('未找到可用蓝牙').fontSize(30).padding({ left: 15 })
          }
        }.title("蓝牙")
      }
      .margin({ top: 10, bottom: 10 })
      .backgroundColor(this.isActiveBluetooth ? '#ccc' : '#fff')
      .borderRadius(20)
      .mode(NavRouteMode.REPLACE)
      .onStateChange((isActivated: boolean) => {
        this.isActiveBluetooth = isActivated
      })
    }
    .height('100%')
    .width('100%')
    .title('设置')
    .backgroundColor("#F2F3F5")
    .titleMode(NavigationTitleMode.Free)
    .mode(NavigationMode.Auto)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/cf9LcJlVQUy4kt97lxUQSQ/zh-cn_image_0000002569020829.gif?HW-CC-KV=V1&HW-CC-Date=20260417T014802Z&HW-CC-Expire=86400&HW-CC-Sign=C1A6B11A6D3F082605F058E5FFA781A1BBA02066ED1C6C8B69A914F9D2FA829A)

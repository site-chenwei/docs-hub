---
title: "@ohos.net.vpn (VPN管理)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-vpn"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Network Kit（网络服务）"
  - "ArkTS API"
  - "@ohos.net.vpn (VPN管理)"
captured_at: "2026-04-17T01:48:22.749Z"
---

# @ohos.net.vpn (VPN管理)

本模块是操作系统提供的内置VPN功能，允许用户通过系统的网络设置进行VPN连接，通常提供的功能较少，而且有比较严格的限制。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/rJYvxieQQ_2F4L6AYwl5mw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=720CB5232F299A8D57140585E5C1DAB971A0B194B82E354606E0010D0C5B76A5)

本模块首批接口从 API version 10 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```js
import { vpn } from '@kit.NetworkKit';
```

#### LinkAddress

type LinkAddress = connection.LinkAddress

获取网络链接信息。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 类型 | 说明 |
| :-- | :-- |
| [connection.LinkAddress](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection#linkaddress) | 网络链路信息。 |

#### RouteInfo

type RouteInfo = connection.RouteInfo

获取网络路由信息。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 类型 | 说明 |
| :-- | :-- |
| [connection.RouteInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection#routeinfo) | 网络路由信息。 |

#### AbilityContext

type AbilityContext = \_AbilityContext

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| :-- | :-- |
| [\_AbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext) | 需要保存状态的UIAbility所对应的context，继承自[Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)，提供UIAbility的相关配置信息以及操作UIAbility和ServiceExtensionAbility的方法。 |

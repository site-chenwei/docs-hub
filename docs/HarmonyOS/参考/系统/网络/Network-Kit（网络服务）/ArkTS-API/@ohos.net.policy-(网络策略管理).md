---
title: "@ohos.net.policy (网络策略管理)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-policy"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Network Kit（网络服务）"
  - "ArkTS API"
  - "@ohos.net.policy (网络策略管理)"
captured_at: "2026-04-17T01:48:22.639Z"
---

# @ohos.net.policy (网络策略管理)

本模块提供网络策略管理能力，采用防火墙技术对用户使用数据流量进行控制管理。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/l4RAt-QsRZCMscSjkFXGgw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=38AF74D513FCF3F292ABA3E2AB59484430E298922D6F0D46C31C780B3054D449)

本模块首批接口从 API version 10 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import { policy } from '@kit.NetworkKit';
```

#### NetBearType

type NetBearType = connection.NetBearType

网络类型。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 类型 | 说明 |
| :-- | :-- |
| [connection.NetBearType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection#netbeartype) | 网络类型。 |

#### policy.showAppNetPolicySettings22+

showAppNetPolicySettings(context: Context): Promise<void>

当需要设置当前应用能否使用Wi-Fi/蜂窝联网时，调用该接口可以打开当前应用的联网设置界面，以设置应用的联网权限。使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetManager.Core

**模型约束：** 此接口仅可在Stage模型下使用。

**设备行为差异**：该接口在Phone、2in1、Tablet设备中可正常调用，在其他设备调用不生效。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| context | [Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context) | 是 | Stage模型的应用上下文（仅支持UIAbilityContext和ExtensionContext）。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/BuQqfY_1RJ2rgz9Tm3oMwQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=4A7DC1E591BB2A9129CDB350F46383AFF14B533F3D6B25FC0B64AC0EC6A6CB4E)

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
import { policy } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
policy.showAppNetPolicySettings(context).then(() => {
    console.info("showAppNetPolicySettings success");
}).catch(() => {
    console.error("showAppNetPolicySettings failed");
    }
)
```

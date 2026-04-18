---
title: "@ohos.app.ability.VpnExtensionAbility (三方VPN能力)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-vpnextensionability"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Network Kit（网络服务）"
  - "ArkTS API"
  - "@ohos.app.ability.VpnExtensionAbility (三方VPN能力)"
captured_at: "2026-04-17T01:48:22.818Z"
---

# @ohos.app.ability.VpnExtensionAbility (三方VPN能力)

VpnExtensionAbility模块提供三方VPN相关能力，提供三方VPN创建、销毁等生命周期回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/f2cM--vFT6aYulU4L6EX8g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=32A542457C35D4FB3C99560E898AE743D88473BD2E904B4376388B825B745DAC)

-   本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
    
-   本模块接口仅可在Stage模型下使用。
    

#### 导入模块

```ts
import { VpnExtensionAbility } from '@kit.NetworkKit';
```

#### 属性

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| context | [VpnExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-vpnextensioncontext) | 否 | 否 | VpnExtension的上下文环境，继承自ExtensionContext。 |

#### VpnExtensionAbility.onCreate

onCreate(want: Want): void

在启动三方VPN进行初始化时回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/SNJGelq7QdaG11lPxPKf9Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=9DE7B1511A581D5A4DC14213D808260DFDD8A626954081FACBC0AF7775439E34)

建议配对调用[onDestroy](#vpnextensionabilityondestroy)监听三方VPN的销毁，执行资源清理等操作。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| want | [Want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-want) | 是 | 指示要启动的信息。 |

**示例：**

```ts
import { VpnExtensionAbility } from '@kit.NetworkKit';
import { Want } from '@kit.AbilityKit';

class MyVpnExtAbility extends VpnExtensionAbility {
    onCreate(want: Want) {
       console.info('MyVpnExtAbility onCreate');
    }
}
```

#### VpnExtensionAbility.onDestroy

onDestroy(): void

VpnExtensionAbility生命周期回调，在销毁时回调，执行资源清理等操作。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**示例：**

```ts
import { VpnExtensionAbility } from '@kit.NetworkKit';

class MyVpnExtAbility extends VpnExtensionAbility {
    onDestroy() {
       console.info('MyVpnExtAbility onDestroy');
    }
}
```

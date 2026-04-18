---
title: "AbilityMonitor"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitymonitor"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "接口依赖的元素及定义"
  - "application"
  - "AbilityMonitor"
captured_at: "2026-04-17T01:47:47.404Z"
---

# AbilityMonitor

本模块提供监听指定[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)生命周期状态变化的能力。开发者可以将AbilityMonitor作为[abilityDelegator.addAbilityMonitor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitydelegator#addabilitymonitor9)的入参来注册监听。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/VVJrmurJSmqjF4d4lyxB_g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=A1CFCE572275C75E65B4E8DEB2EF75EE90C8774823716504ECECC542B1C26C16)

本模块首批接口从API version 9 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import { abilityDelegatorRegistry } from '@kit.TestKit';
```

#### 使用说明

可以作为abilityDelegator中的[addAbilityMonitor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitydelegator#addabilitymonitor9)的入参来监听指定Ability的生命周期变化。

#### AbilityMonitor

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| abilityName | string | 否 | 否 | 被监听的UIAbility对象名称。 |
| moduleName | string | 否 | 是 | 被监听的UIAbility对象所属模块名称。 |
| onAbilityCreate | (ability: [UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)) => void | 否 | 是 | UIAbility对象被创建时，触发该回调函数。 |
| onAbilityForeground | (ability: [UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)) => void | 否 | 是 | UIAbility对象状态变成前台时，触发该回调函数。 |
| onAbilityBackground | (ability: [UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)) => void | 否 | 是 | UIAbility对象状态变成后台时，触发该回调函数。 |
| onAbilityDestroy | (ability: [UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)) => void | 否 | 是 | UIAbility对象被销毁前，触发该回调函数。 |
| onWindowStageCreate | (ability: [UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)) => void | 否 | 是 | 当WindowStage实例被创建时，触发该回调函数。 |
| onWindowStageRestore | (ability: [UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)) => void | 否 | 是 | 当UIAbility跨端迁移时，目标端UIAbility恢复页面栈时，触发该回调函数。 |
| onWindowStageDestroy | (ability: [UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)) => void | 否 | 是 | 当WindowStage被销毁前，触发该回调函数。 |

**示例：**

```ts
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

function onAbilityCreateCallback(data: UIAbility) {
  console.info(`onAbilityCreateCallback, data: ${JSON.stringify(data)}`);
}

let monitor: abilityDelegatorRegistry.AbilityMonitor = {
  abilityName: 'abilityname',
  moduleName: "moduleName",
  onAbilityCreate: onAbilityCreateCallback
}

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.addAbilityMonitor(monitor, (error: BusinessError) => {
  if (error) {
    console.error(`addAbilityMonitor fail, error: ${JSON.stringify(error)}`);
  }
});
```

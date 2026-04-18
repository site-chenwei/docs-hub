---
title: "AbilityStageMonitor"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitystagemonitor"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "接口依赖的元素及定义"
  - "application"
  - "AbilityStageMonitor"
captured_at: "2026-04-17T01:47:47.471Z"
---

# AbilityStageMonitor

本模块提供监听指定[AbilityStage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-abilitystage)对象的能力。开发者可以将AbilityStageMonitor作为[abilityDelegator.waitAbilityStageMonitor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitydelegator#waitabilitystagemonitor9)的入参来注册监听。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/wOjkMr8_R0GeNfK5XfiStg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=EA8F948652DA782461FE4D4A05ED0C809383A715E157BC6F8BC6C80C1A90560F)

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### AbilityStageMonitor

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| moduleName | string | 否 | 否 | 被监听的AbilityStage的模块名。 |
| srcEntrance | string | 否 | 否 | 被监听的AbilityStage的源路径。 |

**示例：**

```ts
import { abilityDelegatorRegistry } from '@kit.TestKit';

let monitor: abilityDelegatorRegistry.AbilityStageMonitor = {
  moduleName: 'feature_as1',
  srcEntrance: './ets/Application/MyAbilityStage.ts',
}

let abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.waitAbilityStageMonitor(monitor, (error, data) => {
  if (error) {
    console.error(`waitAbilityStageMonitor fail, error: ${JSON.stringify(error)}`);
  } else {
    console.info(`waitAbilityStageMonitor success, data: ${JSON.stringify(data)}`);
  }
});
```

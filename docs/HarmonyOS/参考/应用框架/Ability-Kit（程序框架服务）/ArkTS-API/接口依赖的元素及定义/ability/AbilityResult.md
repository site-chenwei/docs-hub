---
title: "AbilityResult"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-abilityresult"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "接口依赖的元素及定义"
  - "ability"
  - "AbilityResult"
captured_at: "2026-04-17T01:47:47.341Z"
---

# AbilityResult

定义UIAbility被拉起并退出后返回给调用方的结果码和数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/u4yc-hXCTVq4PuH4-QsjAQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=0D7531CB67112611F8DB0AD0A4448598442D584EEA89B45E8355546D4DF88D30)

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

[Stage模型](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ability-terminology#stage模型)下：

```ts
import { common } from '@kit.AbilityKit';
```

[FA模型](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ability-terminology#fa模型)下：

```ts
import ability from '@ohos.ability.ability';
```

#### 使用说明

Stage模型下：可以通过[startAbilityForResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#startabilityforresult)获取被拉起的UIAbility退出后返回的AbilityResult对象，被startAbilityForResult拉起的UIAbility对象可以通过[terminateSelfWithResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#terminateselfwithresult)返回AbilityResult对象。

FA模型下：可以通过[startAbilityForResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-ability-featureability#featureabilitystartabilityforresult7)获取被拉起的UIAbility退出后返回的AbilityResult对象，被startAbilityForResult拉起的UIAbility对象可以通过[terminateSelfWithResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-ability-featureability#featureabilityterminateselfwithresult7)返回AbilityResult对象。

#### 属性

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityBase

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| resultCode | number | 否 | 否 | 
目标方的UIAbility被拉起并退出后，目标方返回给拉起方的结果码。

\- 正常情况下，返回目标方传递的结果码。

\- 异常情况下，返回-1。

 |
| want | [Want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-want) | 否 | 是 | 表示UIAbility被拉起并退出后返回的数据。 |

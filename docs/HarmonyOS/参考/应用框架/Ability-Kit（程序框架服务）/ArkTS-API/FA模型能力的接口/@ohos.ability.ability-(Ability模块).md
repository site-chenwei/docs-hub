---
title: "@ohos.ability.ability (Ability模块)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-ability-ability"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "FA模型能力的接口"
  - "@ohos.ability.ability (Ability模块)"
captured_at: "2026-04-17T01:47:46.752Z"
---

# @ohos.ability.ability (Ability模块)

Ability模块将二级模块API组织在一起方便开发者进行导出。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/GsyZDrcrRyyLw_qJKP4PwA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=800CDC01F526995965160852712648D1EDADFC82601918E3AF07E21C04F36F24)

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import { ability } from '@kit.AbilityKit';
```

#### DataAbilityHelper

type DataAbilityHelper = \_DataAbilityHelper

DataAbilityHelper二级模块。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

| 类型 | 说明 |
| :-- | :-- |
| [\_DataAbilityHelper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-dataabilityhelper) | DataAbilityHelper二级模块。 |

#### PacMap

type PacMap = \_PacMap

PacMap二级模块。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

| 类型 | 说明 |
| :-- | :-- |
| [\_PacMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-dataabilityhelper#pacmap) | DataAbilityHelper二级模块。 |

#### DataAbilityOperation

type DataAbilityOperation = \_DataAbilityOperation

DataAbilityOperation二级模块。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

| 类型 | 说明 |
| :-- | :-- |
| [\_DataAbilityOperation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-dataabilityoperation) | DataAbilityOperation二级模块。 |

#### DataAbilityResult

type DataAbilityResult = \_DataAbilityResult

DataAbilityResult二级模块。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

| 类型 | 说明 |
| :-- | :-- |
| [\_DataAbilityResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-dataabilityresult) | DataAbilityResult二级模块。 |

#### AbilityResult

type AbilityResult = \_AbilityResult

AbilityResult二级模块。

**系统能力**：SystemCapability.Ability.AbilityBase

**模型约束**：此接口仅可在FA模型下使用。

| 类型 | 说明 |
| :-- | :-- |
| [\_AbilityResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-abilityresult) | AbilityResult二级模块。 |

#### ConnectOptions

type ConnectOptions = \_ConnectOptions

ConnectOptions二级模块。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在FA模型下使用。

| 类型 | 说明 |
| :-- | :-- |
| [\_ConnectOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-connectoptions) | ConnectOptions二级模块。 |

#### StartAbilityParameter

type StartAbilityParameter = \_StartAbilityParameter

StartAbilityParameter二级模块。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

| 类型 | 说明 |
| :-- | :-- |
| [\_StartAbilityParameter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-startabilityparameter) | StartAbilityParameter二级模块。 |

**示例：**

```ts
import { ability } from '@kit.AbilityKit';

let dataAbilityHelper: ability.DataAbilityHelper;
let pacMap: ability.PacMap;
let dataAbilityOperation: ability.DataAbilityOperation;
let dataAbilityResult: ability.DataAbilityResult;
let abilityResult: ability.AbilityResult;
let connectOptions: ability.ConnectOptions;
let startAbilityParameter: ability.StartAbilityParameter;
```

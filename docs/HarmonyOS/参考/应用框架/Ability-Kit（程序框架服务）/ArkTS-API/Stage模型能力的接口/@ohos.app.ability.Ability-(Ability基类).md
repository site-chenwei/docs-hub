---
title: "@ohos.app.ability.Ability (Ability基类)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-ability"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "Stage模型能力的接口"
  - "@ohos.app.ability.Ability (Ability基类)"
captured_at: "2026-04-17T01:47:45.983Z"
---

# @ohos.app.ability.Ability (Ability基类)

Ability类是应用生命周期调度的基本单元，是[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)和[ExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-extensionability)的基类，提供系统配置更新回调和系统内存级别变化回调能力。该基类不支持开发者直接继承，开发者应根据具体的业务场景选择使用[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)或[ExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-extensionability)，相关指南参见[Ability Kit简介](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/abilitykit-overview)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/8yadjR5ORXCBzx9zKOqYLg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014747Z&HW-CC-Expire=86400&HW-CC-Sign=6C715CD96AECD66D592E768ACE636A49F7C7CBF1A31AAEA81E539248094C5598)

本模块首批接口从API version 9 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ts
import { Ability } from '@kit.AbilityKit';
```

#### Ability的继承关系说明

Ability基类及其子类的继承关系如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/ULKe8qslTaK5roFzj_4VUw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014747Z&HW-CC-Expire=86400&HW-CC-Sign=550722531E9294DBD620AEF260FB94C7EAA2A32FABC303112FB00270A1797B14)

部分ExtensionAbility组件（例如[FormExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-form-formextensionability)、[InputMethodExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod-extension-ability)等）与下图中的ExtensionAbility基类不存在继承关系，均未在图中列出。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/z0ABMnjzQZafGfdx72dX5Q/zh-cn_image_0000002569020053.png?HW-CC-KV=V1&HW-CC-Date=20260417T014747Z&HW-CC-Expire=86400&HW-CC-Sign=CCD69725AAE75BCF189DD63EE8A15133FF01FFB77D1D5AA0D7409D13DCABB3EB)

#### Ability.onConfigurationUpdate

onConfigurationUpdate(newConfig: Configuration): void

当系统环境变量发生变化时，系统会触发该回调。开发者可以重写该回调实现对系统环境变量变化时的响应，例如当系统语言类型发生变化时，应用可以在回调中进行定制化的处理等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/vMQr3nL5SX2Tg_5KPNMRZQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014747Z&HW-CC-Expire=86400&HW-CC-Sign=C624410D9954DE979C03EF606D2E192A4FB20E492FBBDAACB0B7314DBF4C1848)

该回调方法在实际触发时存在一定限制。例如如果开发者通过[setLanguage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-applicationcontext#applicationcontextsetlanguage11)接口设置应用的语言，即便系统语言发生变化，系统也不再触发onConfigurationUpdate回调。详见[使用场景](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/subscribe-system-environment-variable-changes#使用场景)。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| newConfig | [Configuration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-configuration) | 是 | 表示更新后的配置信息。 |

**示例：**

```ts
// Ability是顶层基类，不支持开发者直接继承。故以派生类UIAbility举例说明。
import { UIAbility, Configuration } from '@kit.AbilityKit';

class MyUIAbility extends UIAbility {
  onConfigurationUpdate(config: Configuration) {
    console.info(`onConfigurationUpdate, config: ${JSON.stringify(config)}`);
  }
}
```

#### Ability.onMemoryLevel

onMemoryLevel(level: AbilityConstant.MemoryLevel): void

当整机可用内存变化到指定程度时，系统会触发该回调。开发者可以重写该回调实现对内存级别变化的响应，例如释放缓存数据等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/2KJ55bpqQz2wLpH0Bnqiow/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014747Z&HW-CC-Expire=86400&HW-CC-Sign=0CC4915BF451886A99AF4A675D3B4D65C5B1AD42858DE0B5E9095853F74EA6DC)

onMemoryLevel回调运行在当前进程的主线程中，如果在该回调中做耗时的UI组件释放，会阻塞主线程任务，因此不建议在该回调中释放UI组件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| level | [AbilityConstant.MemoryLevel](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-abilityconstant#memorylevel) | 是 | 整机可用内存级别，对应的触发场景详见[AbilityConstant.MemoryLevel](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-abilityconstant#memorylevel)。 |

**示例：**

```ts
// Ability是顶层基类，不支持开发者直接继承。故以派生类UIAbility举例说明。
import { UIAbility, AbilityConstant } from '@kit.AbilityKit';

class MyUIAbility extends UIAbility {
  onMemoryLevel(level: AbilityConstant.MemoryLevel) {
    console.info(`onMemoryLevel, level: ${JSON.stringify(level)}`);
  }
}
```

---
title: "ExtensionContext"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-extensioncontext"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "接口依赖的元素及定义"
  - "application"
  - "ExtensionContext"
captured_at: "2026-04-17T01:47:47.640Z"
---

# ExtensionContext

ExtensionContext是[ExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-extensionability)的上下文环境，继承自[Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context#context)。

ExtensionContext模块提供访问特定[ExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-extensionability)的资源的能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/A5VafPpmRtOW4QaQ42nTXw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=918DD9E4EE12F0946BDECE0DF8057729F5DF0943D69DA202FA3A99F5AA219544)

-   本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
-   本模块接口仅可在Stage模型下使用。

#### 导入模块

```ts
import { common } from '@kit.AbilityKit';
```

#### 属性

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| currentHapModuleInfo | [HapModuleInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-hapmoduleinfo) | 否 | 否 | 所属Hap包的信息。 |
| config | [Configuration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-configuration) | 否 | 否 | 所属Module的配置信息。 |
| extensionAbilityInfo | [ExtensionAbilityInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-extensionabilityinfo) | 否 | 否 | 所属[ExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-extensionability)的信息。 |

#### 使用场景

ExtensionContext主要用于查询所属ExtensionAbility的信息、Module的配置信息以及HAP包的信息，开发者可根据自身业务需求使用对应的信息。

**示例：**

在扩展的[FormExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-form-formextensionability)中获取上下文，查询该扩展的FormExtensionAbility所属HAP包等信息。

```ts
import { FormExtensionAbility, formBindingData } from '@kit.FormKit';
import { Want } from '@kit.AbilityKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onAddForm(want: Want) {
    console.info(`FormExtensionAbility onAddForm, want: ${want.abilityName}`);
    let extensionContext = this.context;
    let hapInfo = extensionContext.currentHapModuleInfo;
    console.info(`HAP name is: ${hapInfo.name}`);
    let dataObj1: Record<string, string> = {
      'temperature': '11c',
      'time': '11:00'
    };
    let obj1: formBindingData.FormBindingData = formBindingData.createFormBindingData(dataObj1);
    return obj1;
  }
};
```

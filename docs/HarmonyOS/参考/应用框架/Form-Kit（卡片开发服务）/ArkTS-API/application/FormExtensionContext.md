---
title: "FormExtensionContext"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-formextensioncontext"
menu_path:
  - "参考"
  - "应用框架"
  - "Form Kit（卡片开发服务）"
  - "ArkTS API"
  - "application"
  - "FormExtensionContext"
captured_at: "2026-04-17T01:48:14.982Z"
---

# FormExtensionContext

FormExtensionContext模块是[FormExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-form-formextensionability)的上下文环境，继承自[ExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-extensioncontext)。

FormExtensionContext模块提供FormExtensionAbility具有的接口和能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/w76L4TyDS_-HWRSYsraXnw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=36CC8B94DF618F1EEF9F9F8D236D152D8B104F59C6B8B7B262F803F18A9CBE07)

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 使用说明

FormExtensionContext主要用于查询所属FormExtensionAbility的信息、Module的配置信息以及HAP包的信息，开发者可根据自身业务需求使用对应的信息。

```ts
import { FormExtensionAbility, formBindingData } from '@kit.FormKit';
import { Want } from '@kit.AbilityKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onAddForm(want: Want) {
    console.info(`FormExtensionAbility onAddForm, want: ${want.abilityName}`);
    let formData: Record<string, string> = {
      'temperature': '11c',
      'time': '11:00'
    };
    console.info("current language is：", this.context.config.language);
    return formBindingData.createFormBindingData(formData);
  }
};
```

#### FormExtensionContext

FormExtensionContext模块是[FormExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-form-formextensionability)的上下文环境。

**系统能力：** SystemCapability.Ability.Form

**模型约束：** 本模块接口仅可在Stage模型下使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

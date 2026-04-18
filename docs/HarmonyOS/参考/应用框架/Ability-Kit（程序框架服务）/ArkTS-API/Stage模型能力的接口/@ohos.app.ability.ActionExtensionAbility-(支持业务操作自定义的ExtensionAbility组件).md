---
title: "@ohos.app.ability.ActionExtensionAbility (支持业务操作自定义的ExtensionAbility组件)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-actionextensionability"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "Stage模型能力的接口"
  - "@ohos.app.ability.ActionExtensionAbility (支持业务操作自定义的ExtensionAbility组件)"
captured_at: "2026-04-17T01:47:46.141Z"
---

# @ohos.app.ability.ActionExtensionAbility (支持业务操作自定义的ExtensionAbility组件)

ActionExtensionAbility是为开发者提供的自定义操作业务模板，继承自[UIExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiextensionability)。

开发者通过实现ActionExtensionAbility，为其他应用提供内容查看与处理功能。例如，开发者使用ActionExtensionAbility实现了文本翻译功能。其他应用可以通过调用该ActionExtensionAbility来处理需要翻译的内容，并获取到处理后的翻译内容。

各类Ability的继承关系详见[继承关系说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-ability#ability的继承关系说明)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/cPbbyUKyTPeTvmP2bO6Qzg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014747Z&HW-CC-Expire=86400&HW-CC-Sign=17F656FC09AB1FF9F3E77421EB83C5E6FFFC48FE4D8743D6874D8C2639C1836B)

本模块首批接口从API version 10 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ts
import { ActionExtensionAbility } from '@kit.AbilityKit';
```

#### ActionExtensionAbility

ActionExtensionAbility是为开发者提供的自定义操作业务模板，继承自[UIExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiextensionability)。

ActionExtensionAbility主要用于实现宿主应用的内容查看及交互处理功能。例如，添加一个书签、将选中的文本翻译成其他语言、在当前页面编辑图像等。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

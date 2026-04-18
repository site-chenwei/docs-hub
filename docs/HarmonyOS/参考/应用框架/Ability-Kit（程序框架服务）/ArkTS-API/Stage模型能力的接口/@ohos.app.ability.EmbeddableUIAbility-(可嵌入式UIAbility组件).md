---
title: "@ohos.app.ability.EmbeddableUIAbility (可嵌入式UIAbility组件)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-embeddableuiability"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "Stage模型能力的接口"
  - "@ohos.app.ability.EmbeddableUIAbility (可嵌入式UIAbility组件)"
captured_at: "2026-04-17T01:47:46.311Z"
---

# @ohos.app.ability.EmbeddableUIAbility (可嵌入式UIAbility组件)

EmbeddableUIAbility组件是为元服务提供可嵌入式的UIAbility组件，继承自[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)。

开发者通过实现EmbeddableUIAbility，为其他应用提供跳出式启动和嵌入式启动元服务方式。

各类Ability的继承关系详见[继承关系说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-ability#ability的继承关系说明)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/X29NnbEUQ5qB_L6TU9WvFw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014747Z&HW-CC-Expire=86400&HW-CC-Sign=F09524523616034A4E4C9AD304784FC875210869BB4DBEEEFB7D5C97A70AF093)

本模块首批接口从API version 12 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ts
import { EmbeddableUIAbility } from '@kit.AbilityKit';
```

#### EmbeddableUIAbility

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| context | [EmbeddableUIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/-apis-inner-application-embeddableuiabilitycontext) | 否 | 否 | EmbeddableUIAbility组件的上下文。 |

---
title: "EmbeddableUIAbilityContext"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/-apis-inner-application-embeddableuiabilitycontext"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "接口依赖的元素及定义"
  - "application"
  - "EmbeddableUIAbilityContext"
captured_at: "2026-04-17T01:47:47.602Z"
---

# EmbeddableUIAbilityContext

EmbeddableUIAbilityContext是[EmbeddableUIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-embeddableuiability)组件的上下文，继承自[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)。

每个EmbeddableUIAbility组件实例化时，系统都会自动创建对应的EmbeddableUIAbilityContext。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/LN9H-gdyTAaUtEWBL1ZpVQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=14B27BAFDE5AE3C217862A4BAE2A86D7EA91C924B7C7E24023912DE7165D6C7B)

-   本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
-   本模块接口仅可在Stage模型下使用。
-   本模块接口需要在主线程中使用，不要在Worker、TaskPool等子线程中使用。

#### 导入模块

```ts
import { common } from '@kit.AbilityKit';
```

#### EmbeddableUIAbilityContext

开发者可以通过EmbeddableUIAbilityContext获取EmbeddableUIAbility的相关配置信息以及操作EmbeddableUIAbility和ServiceExtensionAbility的方法，如启动EmbeddableUIAbility，停止当前EmbeddableUIAbilityContext所属的EmbeddableUIAbility，启动、停止、连接、断开连接ServiceExtensionAbility等。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

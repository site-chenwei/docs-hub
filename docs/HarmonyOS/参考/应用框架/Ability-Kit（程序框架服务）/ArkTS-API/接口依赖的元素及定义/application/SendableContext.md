---
title: "SendableContext"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-sendablecontext"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "接口依赖的元素及定义"
  - "application"
  - "SendableContext"
captured_at: "2026-04-17T01:47:47.860Z"
---

# SendableContext

SendableContext符合[Sendable协议](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable#sendable协议)，继承自[lang.ISendable](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkts-lang#langisendable)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/43LWQnOSRaGCXvTLOxZYIA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=C111B792A65A8BB68269886F2A563E0F707213A04E1129D315A9C46E25E3C62A)

-   本模块首批接口从API version 12 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
-   本模块接口仅可在Stage模型下使用。

#### 导入模块

```ts
import { sendableContextManager } from '@kit.AbilityKit';
```

#### SendableContext

SendableContext符合[Sendable协议](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable#sendable协议)，可以与Context对象相互转换，用于ArkTS并发实例间（包括主线程、TaskPool&Worker工作线程）的数据传递。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

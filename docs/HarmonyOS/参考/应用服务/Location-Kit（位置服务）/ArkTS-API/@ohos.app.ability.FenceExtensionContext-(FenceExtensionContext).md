---
title: "@ohos.app.ability.FenceExtensionContext (FenceExtensionContext)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-fenceextensioncontext"
menu_path:
  - "参考"
  - "应用服务"
  - "Location Kit（位置服务）"
  - "ArkTS API"
  - "@ohos.app.ability.FenceExtensionContext (FenceExtensionContext)"
captured_at: "2026-04-17T01:48:59.017Z"
---

# @ohos.app.ability.FenceExtensionContext (FenceExtensionContext)

FenceExtensionContext是FenceExtensionAbility的上下文环境，继承自[ExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-extensioncontext)，提供FenceExtensionAbility的相关配置信息以及启动Ability接口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/tiiDauhUS_m-A_5G4F-N7w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014859Z&HW-CC-Expire=86400&HW-CC-Sign=F0589E0BA37B1D2387FE1201B4BA1E68D55291EEE012ED9051E74537A27D8D31)

本模块首批接口从API version 14开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ts
import { FenceExtensionContext } from '@kit.LocationKit';
```

#### 使用说明

在使用FenceExtensionContext的功能前，需要通过FenceExtensionAbility获取。

```ts
import { FenceExtensionAbility, FenceExtensionContext } from '@kit.LocationKit';

class MyFenceExtensionAbility extends FenceExtensionAbility {
  onCreate() {
    let fenceExtensionContext: FenceExtensionContext = this.context;
  }
}
```

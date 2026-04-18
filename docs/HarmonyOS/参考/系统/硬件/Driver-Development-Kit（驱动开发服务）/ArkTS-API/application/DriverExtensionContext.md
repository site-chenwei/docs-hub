---
title: "DriverExtensionContext"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-driverextensioncontext"
menu_path:
  - "参考"
  - "系统"
  - "硬件"
  - "Driver Development Kit（驱动开发服务）"
  - "ArkTS API"
  - "application"
  - "DriverExtensionContext"
captured_at: "2026-04-17T01:48:32.349Z"
---

# DriverExtensionContext

DriverExtensionContext模块是DriverExtensionAbility的上下文环境，继承自ExtensionContext。

DriverExtensionContext模块提供DriverExtensionAbility实现中需要主动发起的操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/AbO9LtQkREKj5Ym_XXjdEg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014834Z&HW-CC-Expire=86400&HW-CC-Sign=D1FA931516F0DD752BBD4FF9821D8A1C19FFF555E759282284DE009B05B69BDF)

-   本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
-   本模块接口仅可在Stage模型下使用。

#### 导入模块

```ts
import { common } from '@kit.AbilityKit';
```

#### 使用说明

在使用DriverExtensionContext的功能前，需要通过DriverExtensionAbility子类实例获取。

```ts
  import { DriverExtensionAbility, DriverExtensionContext } from '@kit.DriverDevelopmentKit';

  let context : DriverExtensionContext | undefined;
  class EntryAbility extends DriverExtensionAbility {
    onInit() {
      context = this.context; // 获取DriverExtensionContext
    }
  }
```

#### DriverExtensionContext.updateDriverState

updateDriverState(): void

驱动状态上报。预留接口，暂不提供具体功能。

**系统能力**：SystemCapability.Driver.ExternalDevice

**示例：**

```ts
// 当前代码实现依赖上一节代码实现
if (context != null) {
  context.updateDriverState();
}
```

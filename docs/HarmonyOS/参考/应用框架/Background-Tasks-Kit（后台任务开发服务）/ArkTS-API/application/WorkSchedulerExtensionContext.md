---
title: "WorkSchedulerExtensionContext"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-workschedulerextensioncontext"
menu_path:
  - "参考"
  - "应用框架"
  - "Background Tasks Kit（后台任务开发服务）"
  - "ArkTS API"
  - "application"
  - "WorkSchedulerExtensionContext"
captured_at: "2026-04-17T01:48:13.463Z"
---

# WorkSchedulerExtensionContext

WorkSchedulerExtensionContext是WorkSchedulerExtensionAbility的上下文环境，继承自[ExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-extensioncontext)。

WorkSchedulerExtensionContext可直接作为WorkSchedulerExtension的上下文环境，提供允许访问特定于WorkSchedulerExtensionAbility的资源的能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/xySjS2WpQJStoixEc3-tZw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=5216E658FE416294E71E0231A0D1FF5F43C72BFE6B879135F62DED8CBF6AA873)

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 使用说明

通过WorkSchedulerExtensionAbility子类实例来获取。

```ts
import { WorkSchedulerExtensionAbility, workScheduler } from '@kit.BackgroundTasksKit';

class MyWorkSchedulerExtensionAbility extends WorkSchedulerExtensionAbility {
    onWorkStart(workInfo: workScheduler.WorkInfo) {
        let WorkSchedulerExtensionContext = this.context; // 获取WorkSchedulerExtensionContext
    }
}
```

#### WorkSchedulerExtensionContext

WorkSchedulerExtensionContext是WorkSchedulerExtensionAbility的上下文环境。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**模型约束：** 本模块接口仅可在Stage模型下使用。

---
title: "@ohos.WorkSchedulerExtensionAbility (延迟任务调度回调)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-workschedulerextensionability"
menu_path:
  - "参考"
  - "应用框架"
  - "Background Tasks Kit（后台任务开发服务）"
  - "ArkTS API"
  - "@ohos.WorkSchedulerExtensionAbility (延迟任务调度回调)"
captured_at: "2026-04-17T01:48:13.456Z"
---

# @ohos.WorkSchedulerExtensionAbility (延迟任务调度回调)

本模块提供延迟任务回调能力。开发者可重写模块接口，在延迟任务触发时，系统可通过本模块接口回调应用，在回调里处理任务逻辑。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/Td_WbL2_TKm2tzS4Jf2gyg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=AD22CBE41F5090C79AF9B687E64B86395665DE2C8ACF2D5F86ADEB72B155BE29)

-   本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
    
-   本模块接口仅可在Stage模型下使用。
    

#### 导入模块

```ts
import { WorkSchedulerExtensionAbility } from '@kit.BackgroundTasksKit';
```

#### WorkSchedulerExtensionContext10+

type WorkSchedulerExtensionContext = \_WorkSchedulerExtensionContext

WorkSchedulerExtensionContext是WorkSchedulerExtensionAbility的上下文环境，继承自[ExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-extensioncontext)。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

| 类型 | 说明 |
| :-- | :-- |
| [\_WorkSchedulerExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-workschedulerextensioncontext) | WorkSchedulerExtension的上下文环境。 |

#### WorkSchedulerExtensionAbility

延迟任务回调，当满足调度条件或调度结束时，系统会回调应用WorkSchedulerExtensionAbility中[onWorkStart()](#onworkstart)或[onWorkStop()](#onworkstop)的方法。

#### \[h2\]属性

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| context10+ | [WorkSchedulerExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-workschedulerextensioncontext) | 否 | 否 | WorkSchedulerExtension的上下文环境，继承自ExtensionContext。 |

#### \[h2\]onWorkStart

onWorkStart(work: workScheduler.WorkInfo): void

开始延迟任务调度回调。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| work | [workScheduler.WorkInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resourceschedule-workscheduler#workinfo) | 是 | 要添加到执行队列的任务。 |

**示例：**

```ts
import { workScheduler } from '@kit.BackgroundTasksKit';
import { WorkSchedulerExtensionAbility } from '@kit.BackgroundTasksKit';

export default class MyWorkSchedulerExtensionAbility extends WorkSchedulerExtensionAbility {
  onWorkStart(workInfo: workScheduler.WorkInfo) {
      console.info(`MyWorkSchedulerExtensionAbility onWorkStart, workId: ${workInfo.workId},
          bundleName: ${workInfo.bundleName}, abilityName: ${workInfo.abilityName}.`);
  }
}
```

#### \[h2\]onWorkStop

onWorkStop(work: workScheduler.WorkInfo): void

结束延迟任务调度回调。当延迟任务2分钟超时或应用调用[stopWork](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resourceschedule-workscheduler#workschedulerstopwork)接口取消任务时，触发该回调。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| work | [workScheduler.WorkInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resourceschedule-workscheduler#workinfo) | 是 | 执行队列中要结束回调的任务。 |

**示例：**

```ts
import { workScheduler } from '@kit.BackgroundTasksKit';
import { WorkSchedulerExtensionAbility } from '@kit.BackgroundTasksKit';

export default class MyWorkSchedulerExtensionAbility extends WorkSchedulerExtensionAbility {
  onWorkStop(workInfo: workScheduler.WorkInfo) {
      console.info(`MyWorkSchedulerExtensionAbility onWorkStop, workId: ${workInfo.workId},
          bundleName: ${workInfo.bundleName}, abilityName: ${workInfo.abilityName}.`);
  }
}
```

---
title: "@ohos.backgroundTaskManager (后台任务管理)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-backgroundtaskmanager"
menu_path:
  - "参考"
  - "应用框架"
  - "Background Tasks Kit（后台任务开发服务）"
  - "ArkTS API"
  - "已停止维护的接口"
  - "@ohos.backgroundTaskManager (后台任务管理)"
captured_at: "2026-04-17T01:48:13.550Z"
---

# @ohos.backgroundTaskManager (后台任务管理)

本模块提供后台任务管理能力。

当应用或业务模块处于后台（无可见界面）时，如果有需要继续执行或者后续执行的业务，可基于业务类型，申请短时任务延迟挂起（Suspend）或者长时任务避免进入挂起状态。

应用有不可中断且短时间能完成的任务时（如，用户在文件管理器上点击垃圾文件清理，若清理未完成时退到后台，文件管理器需要申请短时任务完成清理），可以使用短时任务机制。

应用中存在用户能够直观感受到的且需要一直在后台运行的业务时（如，后台播放音乐），可以使用长时任务机制。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/kmiVM6eSRmac3GHERPzQEA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=7A186BE6DFC4098F597EC521E6DB16669AC605D7825613E308447DC61967B609)

-   从API Version 9 开始，该接口不再维护，推荐使用新接口[@ohos.resourceschedule.backgroundTaskManager (后台任务管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager)。
    
-   本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
    

#### 导入模块

```ts
import backgroundTaskManager from '@ohos.backgroundTaskManager';
```

#### backgroundTaskManager.requestSuspendDelay(deprecated)

requestSuspendDelay(reason: string, callback: Callback<void>): DelaySuspendInfo

后台应用申请延迟挂起。

延迟挂起时间一般情况下默认值为3分钟，低电量（依据系统低电量广播）时默认值为1分钟。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/k9GXPe_7T0uX3mYnSATB5Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=80E5DA423E4909B7F078A18CDD4AC2870ABE908EB7DB11434771819479285073)

从API version 7开始支持，从API version 9开始废弃。建议使用[backgroundTaskManager.requestSuspendDelay](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager#backgroundtaskmanagerrequestsuspenddelay)替代。

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| reason | string | 是 | 延迟挂起申请的原因。 |
| callback | Callback<void> | 是 | 延迟即将超时的回调函数，一般在超时前6秒通过此回调通知应用。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| [DelaySuspendInfo](#delaysuspendinfodeprecated) | 返回延迟挂起信息。 |

**示例**：

```ts
import backgroundTaskManager from '@ohos.backgroundTaskManager';
import { BusinessError } from '@ohos.base';

// 设置延迟任务挂起的原因
let myReason = 'test requestSuspendDelay';
// 申请延迟任务
let delayInfo = backgroundTaskManager.requestSuspendDelay(myReason, () => {
    console.info("Request suspension delay will time out.");
})
// 打印延迟任务信息
let id = delayInfo.requestId;
let time = delayInfo.actualDelayTime;
console.info("The requestId is: " + id);
console.info("The actualDelayTime is: " + time);
```

#### backgroundTaskManager.getRemainingDelayTime(deprecated)

getRemainingDelayTime(requestId: number, callback: AsyncCallback<number>): void

获取应用程序进入挂起状态前的剩余时间，使用callback形式返回。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/B4OFW6DBQGqCq82Bu9FBKw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=E5E5BBCEE0FD3178AEE4557EBF99E79E3C702528772188AFF56F70C20F6F7421)

从API version 7开始支持，从API version 9开始废弃。建议使用[backgroundTaskManager.getRemainingDelayTime](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager#backgroundtaskmanagergetremainingdelaytime)替代。

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| requestId | number | 是 | 延迟挂起的请求ID。这个值通过调用[requestSuspendDelay](#backgroundtaskmanagerrequestsuspenddelaydeprecated)方法获取。 |
| callback | AsyncCallback<number> | 是 | 指定的callback回调方法。用于返回应用程序进入挂起状态之前的剩余时间，以毫秒为单位。 |

**示例**：

```ts
import backgroundTaskManager from '@ohos.backgroundTaskManager';
import { BusinessError } from '@ohos.base';

let delayInfo = backgroundTaskManager.requestSuspendDelay("test", () => {});
backgroundTaskManager.getRemainingDelayTime(delayInfo.requestId, (err: BusinessError, res: number) => {
    if(err) {
        console.info('callback => Operation getRemainingDelayTime failed. Cause: ' + err.code);
    } else {
        console.info('callback => Operation getRemainingDelayTime succeeded. Data: ' + JSON.stringify(res));
    }
})
```

#### backgroundTaskManager.getRemainingDelayTime(deprecated)

getRemainingDelayTime(requestId: number): Promise<number>

获取应用程序进入挂起状态前的剩余时间，使用Promise形式返回。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/mZ5-JWbCQkKlk9u5DP0GKw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=2620184C5F2C6FDE6212B478CFC912011FD7828E6D75F9462E628C33340B24A2)

从API version 7开始支持，从API version 9开始废弃。建议使用[backgroundTaskManager.getRemainingDelayTime](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager#backgroundtaskmanagergetremainingdelaytime-1)替代。

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| requestId | number | 是 | 延迟挂起的请求ID。这个值通过调用[requestSuspendDelay](#backgroundtaskmanagerrequestsuspenddelaydeprecated)方法获取。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | 指定的Promise回调方法。返回应用程序进入挂起状态之前的剩余时间，以毫秒为单位。 |

**示例**：

```ts
import backgroundTaskManager from '@ohos.backgroundTaskManager';
import { BusinessError } from '@ohos.base';

let delayInfo = backgroundTaskManager.requestSuspendDelay("test", () => {});
    backgroundTaskManager.getRemainingDelayTime(delayInfo.requestId).then((res:number) => {
    console.info('promise => Operation getRemainingDelayTime succeeded. Data: ' + JSON.stringify(res));
}).catch((err : BusinessError) => {
    console.info('promise => Operation getRemainingDelayTime failed. Cause: ' + err.code);
})
```

#### backgroundTaskManager.cancelSuspendDelay(deprecated)

cancelSuspendDelay(requestId: number): void

取消延迟挂起。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/nGXQHtbdT_uaOlwyLZYdeQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=2446605FCED5E01CA085B67F8992BA9639CD93B3C42820901B1D1197CE8D3921)

从API version 7开始支持，从API version 9开始废弃。建议使用[backgroundTaskManager.cancelSuspendDelay](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager#backgroundtaskmanagercancelsuspenddelay)替代。

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| requestId | number | 是 | 延迟挂起的请求ID。这个值通过调用[requestSuspendDelay](#backgroundtaskmanagerrequestsuspenddelaydeprecated)方法获取。 |

**示例**：

```ts
let delayInfo = backgroundTaskManager.requestSuspendDelay("test", () => {});
backgroundTaskManager.cancelSuspendDelay(delayInfo.requestId);
```

#### backgroundTaskManager.startBackgroundRunning(deprecated)

startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent, callback: AsyncCallback<void>): void

向系统申请长时任务，使用callback形式返回结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/CxFXWqauT4yKbSWJYwieTw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=DA21EA7C766C0EBBC1AF89680B0CFB6ABA8D762C85E2A49DCF1F7411C70B83E8)

从API version 8开始支持，从API version 9开始废弃。建议使用[backgroundTaskManager.startBackgroundRunning](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager#backgroundtaskmanagerstartbackgroundrunning)替代。

**需要权限:** ohos.permission.KEEP\_BACKGROUND\_RUNNING

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| context | Context | 是 | 
应用运行的上下文。

FA模型的应用Context定义见[Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-app-context)。

Stage模型的应用Context定义见[Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)。

 |
| bgMode | [BackgroundMode](#backgroundmodedeprecated) | 是 | 向系统申请的后台模式。 |
| wantAgent | [WantAgent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-wantagent) | 是 | 通知参数，用于指定长时任务通知点击后跳转的界面。 |
| callback | AsyncCallback<void> | 是 | callback形式返回启动长时任务的结果。 |

**示例**：

FA模型示例：

```js
import backgroundTaskManager from '@ohos.backgroundTaskManager';
import featureAbility from '@ohos.ability.featureAbility';
import wantAgent, { WantAgent } from '@ohos.app.ability.wantAgent';
import { BusinessError } from '@ohos.base';

function callback(err: BusinessError, data: void) {
  if (err) {
    console.error("Operation startBackgroundRunning failed Cause: " + err);
  } else {
    console.info("Operation startBackgroundRunning succeeded");
  }
}

let wantAgentInfo : wantAgent.WantAgentInfo = {
  wants: [
    {
      bundleName: "com.example.myapplication",
      abilityName: "EntryAbility"
    }
  ],
  operationType: wantAgent.OperationType.START_ABILITY,
  requestCode: 0,
  wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
};

wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj : WantAgent) => {
  backgroundTaskManager.startBackgroundRunning(featureAbility.getContext(),
    backgroundTaskManager.BackgroundMode.LOCATION, wantAgentObj, callback)
});
```

Stage模型示例：

```ts
import UIAbility from '@ohos.app.ability.UIAbility';
import backgroundTaskManager from '@ohos.backgroundTaskManager';
import wantAgent, { WantAgent } from '@ohos.app.ability.wantAgent';
import Want from '@ohos.app.ability.Want';
import AbilityConstant from '@ohos.app.ability.AbilityConstant';
import { BusinessError } from '@ohos.base';

function callback(err: BusinessError, data: void) {
  if (err) {
    console.error("Operation startBackgroundRunning failed Cause: " + err);
  } else {
    console.info("Operation startBackgroundRunning succeeded");
  }
}

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    let wantAgentInfo : wantAgent.WantAgentInfo = {
      wants: [
        {
          bundleName: "com.example.myapplication",
          abilityName: "EntryAbility"
        }
      ],
      operationType: wantAgent.OperationType.START_ABILITY,
      requestCode: 0,
      wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
    };

    wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj : WantAgent) => {
      backgroundTaskManager.startBackgroundRunning(this.context,
        backgroundTaskManager.BackgroundMode.LOCATION, wantAgentObj, callback)
    });
  }
};
```

#### backgroundTaskManager.startBackgroundRunning(deprecated)

startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent): Promise<void>

向系统申请长时任务，使用promise形式返回结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/Hd_XAHA8RnCN-_BYTon2LA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=D2A2EA4B56763208A08A8718136DBC1E4EFAD19D5D51674CF813E8F17F6ACC02)

从API version 8开始支持，从API version 9开始废弃。建议使用[backgroundTaskManager.startBackgroundRunning](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager#backgroundtaskmanagerstartbackgroundrunning-1)替代。

**需要权限:** ohos.permission.KEEP\_BACKGROUND\_RUNNING

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| context | Context | 是 | 
应用运行的上下文。

FA模型的应用Context定义见[Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-app-context)。

Stage模型的应用Context定义见[Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)。

 |
| bgMode | [BackgroundMode](#backgroundmodedeprecated) | 是 | 向系统申请的后台模式。 |
| wantAgent | [WantAgent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-wantagent) | 是 | 通知参数，用于指定长时任务通知点击跳转的界面。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 使用Promise形式返回结果。 |

**示例**：

FA模型示例（需使用js代码开发）：

```js
import backgroundTaskManager from '@ohos.backgroundTaskManager';
import featureAbility from '@ohos.ability.featureAbility';
import wantAgent, { WantAgent } from '@ohos.app.ability.wantAgent';
import { BusinessError } from '@ohos.base';

let wantAgentInfo : wantAgent.WantAgentInfo = {
  wants: [
    {
      bundleName: "com.example.myapplication",
      abilityName: "EntryAbility"
    }
  ],
  operationType: wantAgent.OperationType.START_ABILITY,
  requestCode: 0,
  wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
};

wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: WantAgent) => {
  backgroundTaskManager.startBackgroundRunning(featureAbility.getContext(),
    backgroundTaskManager.BackgroundMode.LOCATION, wantAgentObj).then(() => {
    console.info("Operation startBackgroundRunning succeeded");
  }).catch((err: BusinessError) => {
    console.error("Operation startBackgroundRunning failed Cause: " + err);
  });
});
```

Stage模型示例：

```ts
import UIAbility from '@ohos.app.ability.UIAbility';
import backgroundTaskManager from '@ohos.backgroundTaskManager';
import wantAgent, { WantAgent } from '@ohos.app.ability.wantAgent';
import Want from '@ohos.app.ability.Want';
import AbilityConstant from '@ohos.app.ability.AbilityConstant';
import { BusinessError } from '@ohos.base';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    let wantAgentInfo : wantAgent.WantAgentInfo = {
      wants: [
        {
          bundleName: "com.example.myapplication",
          abilityName: "EntryAbility"
        }
      ],
      // 点击通知后，动作类型
      operationType: wantAgent.OperationType.START_ABILITY,
      requestCode: 0,
      // 点击通知后，动作执行属性
      wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
    };

    wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj : WantAgent) => {
      backgroundTaskManager.startBackgroundRunning(this.context,
        backgroundTaskManager.BackgroundMode.LOCATION, wantAgentObj).then(() => {
        console.info("Operation startBackgroundRunning succeeded");
      }).catch((err: BusinessError) => {
        console.error("Operation startBackgroundRunning failed Cause: " + err);
      });
    });
  }
};
```

#### backgroundTaskManager.stopBackgroundRunning(deprecated)

stopBackgroundRunning(context: Context, callback: AsyncCallback<void>): void

向系统申请取消长时任务，使用callback形式返回结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/elLegjUTSAO--unMHtj-3g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=DAB7ECAA3651C59A50A76408D8DBF2085067CEA7D4E2BE8D36F0F5153410FF0B)

从API version 8开始支持，从API version 9开始废弃。建议使用[backgroundTaskManager.stopBackgroundRunning](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager#backgroundtaskmanagerstopbackgroundrunning)替代。

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| context | Context | 是 | 
应用运行的上下文。

FA模型的应用Context定义见[Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-app-context)。

Stage模型的应用Context定义见[Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)。

 |
| callback | AsyncCallback<void> | 是 | callback形式返回启动长时任务的结果。 |

**示例**：

FA模型示例（需使用js代码开发）：

```js
import backgroundTaskManager from '@ohos.backgroundTaskManager';
import featureAbility from '@ohos.ability.featureAbility';
import { BusinessError } from '@ohos.base';

function callback(err: BusinessError, data: void) {
  if (err) {
    console.error("Operation stopBackgroundRunning failed Cause: " + err);
  } else {
    console.info("Operation stopBackgroundRunning succeeded");
  }
}

backgroundTaskManager.stopBackgroundRunning(featureAbility.getContext(), callback);
```

Stage模型示例：

```ts
import UIAbility from '@ohos.app.ability.UIAbility';
import backgroundTaskManager from '@ohos.backgroundTaskManager';
import Want from '@ohos.app.ability.Want';
import AbilityConstant from '@ohos.app.ability.AbilityConstant';
import { BusinessError } from '@ohos.base';

function callback(err: BusinessError, data: void) {
  if (err) {
    console.error("Operation stopBackgroundRunning failed Cause: " + err);
  } else {
    console.info("Operation stopBackgroundRunning succeeded");
  }
}

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    backgroundTaskManager.stopBackgroundRunning(this.context, callback);
  }
};
```

#### backgroundTaskManager.stopBackgroundRunning(deprecated)

stopBackgroundRunning(context: Context): Promise<void>

向系统申请取消长时任务，使用promise形式返回结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/P61TDNC8SoW9g3ROJ7jWYw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=664E261CC621965CDF0D395A9880C28CC8BDE7D5544F178530D48BE3BA156CCD)

从API version 8开始支持，从API version 9开始废弃。建议使用[backgroundTaskManager.stopBackgroundRunning](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager#backgroundtaskmanagerstopbackgroundrunning-1)替代。

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| context | Context | 是 | 
应用运行的上下文。

FA模型的应用Context定义见[Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-app-context)。

Stage模型的应用Context定义见[Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)。

 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 使用Promise形式返回结果。 |

**示例**：

FA模型示例：

```js
import backgroundTaskManager from '@ohos.backgroundTaskManager';
import featureAbility from '@ohos.ability.featureAbility';
import { BusinessError } from '@ohos.base';

// 取消长时任务
backgroundTaskManager.stopBackgroundRunning(featureAbility.getContext()).then(() => {
  console.info("Operation stopBackgroundRunning succeeded");
}).catch((err: BusinessError) => {
  console.error("Operation stopBackgroundRunning failed Cause: " + err);
});
```

Stage模型示例：

```ts
import UIAbility from '@ohos.app.ability.UIAbility';
import backgroundTaskManager from '@ohos.backgroundTaskManager';
import Want from '@ohos.app.ability.Want';
import AbilityConstant from '@ohos.app.ability.AbilityConstant';
import { BusinessError } from '@ohos.base';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    // 取消长时任务
    backgroundTaskManager.stopBackgroundRunning(this.context).then(() => {
      console.info("Operation stopBackgroundRunning succeeded");
    }).catch((err: BusinessError) => {
      console.error("Operation stopBackgroundRunning failed Cause: " + err);
    });
  }
};
```

#### DelaySuspendInfo(deprecated)

延迟挂起信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/oSmMFODzSP6WMRIYFH2rWw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=14E6371E7C177E40CCD485A128AC824530B3082C5ADD3E101D3A5EE561BE525C)

从API version 7开始支持，从API version 9开始废弃。建议使用[DelaySuspendInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager#delaysuspendinfo)替代。

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| requestId | number | 否 | 否 | 延迟挂起的请求ID。 |
| actualDelayTime | number | 否 | 否 | 
应用的实际挂起延迟时间，以毫秒为单位。

一般情况下默认值为180000，低电量（依据系统低电量广播）时默认值为60000。

 |

#### BackgroundMode(deprecated)

长时任务类型。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/2FocatL5Tq6-l71Te0Ekyw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=01A8D9AF6ADCDB6D9DA558A66B8479639C6B121249676C22E0FA43A266DF065C)

从API version 8开始支持，从API version 9开始废弃。建议使用[BackgroundMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager#backgroundmode)替代。

**系统能力:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| DATA\_TRANSFER | 1 | 数据传输。 |
| AUDIO\_PLAYBACK | 2 | 音频播放。 |
| AUDIO\_RECORDING | 3 | 录音。 |
| LOCATION | 4 | 定位导航。 |
| BLUETOOTH\_INTERACTION | 5 | 蓝牙相关。 |
| MULTI\_DEVICE\_CONNECTION | 6 | 多设备互联。 |
| TASK\_KEEPING | 9 | 计算任务（仅在特定设备生效）。 |

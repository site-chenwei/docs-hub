---
title: "@ohos.ability.particleAbility (ParticleAbility模块)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-ability-particleability"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "FA模型能力的接口"
  - "@ohos.ability.particleAbility (ParticleAbility模块)"
captured_at: "2026-04-17T01:47:46.830Z"
---

# @ohos.ability.particleAbility (ParticleAbility模块)

particleAbility模块提供了操作Data和Service类型的Ability的能力，包括启动、停止指定的particleAbility，获取dataAbilityHelper，连接、断连指定的ServiceAbility等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/ATFdZJeXRoOj5BRjKDEJOQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=3B4C011D086D0193C7987F186214138ED8DD101C33242D214833C4AA780D42C6)

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在FA模型下使用。

#### 使用限制

particleAbility模块用来对Data和Service类型的Ability进行操作。

#### 导入模块

```ts
import { particleAbility } from '@kit.AbilityKit';
```

#### particleAbility.startAbility

startAbility(parameter: StartAbilityParameter, callback: AsyncCallback<void>): void

启动指定的particleAbility。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/NvS6F5CzQ0W0sLk5ljC24Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=3722942076FF5712DDE0169510CA8F977827DD263641F8B9FDFEA016545D6602)

组件启动规则详见：[组件启动规则（FA模型）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/component-startup-rules-fa)。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| parameter | [StartAbilityParameter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-startabilityparameter) | 是 | 表示启动的ability。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当启动指定的particleAbility成功，err为undefined，否则为错误对象。 |

**示例：**

```ts
import { particleAbility, wantConstant } from '@kit.AbilityKit';

particleAbility.startAbility(
  {
    want:
    {
      action: 'ohos.want.action.home',
      entities: ['entity.system.home'],
      type: 'MIMETYPE',
      flags: wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION,
      deviceId: '',
      bundleName: 'com.example.Data',
      abilityName: 'com.example.Data.EntryAbility',
      uri: ''
    },
  },
  (error, data) => {
    if (error && error.code !== 0) {
      console.error(`startAbility fail, error: ${JSON.stringify(error)}`);
    } else {
      console.info(`startAbility success, data: ${JSON.stringify(data)}`);
    }
  },
);
```

#### particleAbility.startAbility

startAbility(parameter: StartAbilityParameter): Promise<void>

启动指定的particleAbility。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/zQaCIpl1QoeuPaf_h3MQVA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=3780FFECC6A6AC3A84E2EDA52CC10ECCF36427C5E2BF61027E853B816B7AF1FE)

组件启动规则详见：[组件启动规则（FA模型）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/component-startup-rules-fa)。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| parameter | [StartAbilityParameter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-startabilityparameter) | 是 | 表示启动的ability。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```ts
import { particleAbility, wantConstant } from '@kit.AbilityKit';

particleAbility.startAbility(
  {
    want:
    {
      action: 'ohos.want.action.home',
      entities: ['entity.system.home'],
      type: 'MIMETYPE',
      flags: wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION,
      deviceId: '',
      bundleName: 'com.example.Data',
      abilityName: 'com.example.Data.EntryAbility',
      uri: ''
    },
  },
).then(() => {
  console.info('particleAbility startAbility');
});
```

#### particleAbility.terminateSelf

terminateSelf(callback: AsyncCallback<void>): void

销毁当前particleAbility。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | 是 | 回调函数。当销毁当前particleAbility成功，err为undefined，否则为错误对象。 |

**示例：**

```ts
import { particleAbility } from '@kit.AbilityKit';

particleAbility.terminateSelf(
  (error) => {
    if (error && error.code !== 0) {
      console.error(`terminateSelf fail, error: ${JSON.stringify(error)}`);
    }
  }
);
```

#### particleAbility.terminateSelf

terminateSelf(): Promise<void>

销毁当前particleAbility。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```ts
import { particleAbility } from '@kit.AbilityKit';

particleAbility.terminateSelf().then(() => {
  console.info('particleAbility terminateSelf');
});
```

#### particleAbility.acquireDataAbilityHelper

acquireDataAbilityHelper(uri: string): DataAbilityHelper

获取dataAbilityHelper对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/Xp0CKEiIR4aVZ5gkp8q1kQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=EEBDB417DA890D2F279872061D89FF9DDDFC1329953DB11E8C0A4C22BFF87F2C)

组件启动规则详见：[组件启动规则（FA模型）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/component-startup-rules-fa)。

跨应用访问dataAbility，对端应用需配置关联启动。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| uri | string | 是 | 表示要打开的文件的路径。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [DataAbilityHelper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-dataabilityhelper) | 用来协助其他Ability访问DataAbility的工具类。 |

**示例：**

```ts
import { particleAbility } from '@kit.AbilityKit';

let uri = '';
particleAbility.acquireDataAbilityHelper(uri);
```

#### particleAbility.startBackgroundRunning(deprecated)

startBackgroundRunning(id: number, request: NotificationRequest, callback: AsyncCallback<void>): void

向系统申请长时任务。使用callback异步回调。

**需要权限**：ohos.permission.KEEP\_BACKGROUND\_RUNNING

**系统能力**：SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/n8CBkKG8QWSU8VdUzIzSKg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=1F654897F9C532891237E6E8C1AEA2E6E1A1AD7F365EF53547A0C4D2BE0A3C8A)

从API version 7开始支持，从API version 9开始废弃，建议使用[backgroundTaskManager.startBackgroundRunning](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager#backgroundtaskmanagerstartbackgroundrunning)替代。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| id | number | 是 | 长时任务通知id号。 |
| request | [NotificationRequest](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notification#notificationrequest) | 是 | 通知参数，用于显示通知栏的信息。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当向系统申请长时任务成功，err为undefined，否则为错误对象。 |

**示例**：

```ts
import { particleAbility, wantAgent } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import notification from '@ohos.notification';

function callback(error: BusinessError, data: void) {
  if (error && error.code !== 0) {
    console.error(`Operation failed error: ${JSON.stringify(error)}`);
  } else {
    console.info(`Operation succeeded, data: ${data}`);
  }
}

let wantAgentInfo: wantAgent.WantAgentInfo = {
  wants: [
    {
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    }
  ],
  operationType: wantAgent.OperationType.START_ABILITY,
  requestCode: 0,
  wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
};

wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj) => {
  let id = 1;
  particleAbility.startBackgroundRunning(id, {
    content:
    {
      contentType: notification.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
      normal:
      {
        title: 'title',
        text: 'text'
      }
    },
    wantAgent: wantAgentObj
  }, callback);
});
```

#### particleAbility.startBackgroundRunning(deprecated)

startBackgroundRunning(id: number, request: NotificationRequest): Promise<void>

向系统申请长时任务。使用Promise异步回调。

**需要权限**：ohos.permission.KEEP\_BACKGROUND\_RUNNING

**系统能力**：SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/xKWyfpsKSu2h54vWI6fBvg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=2BB1D881BBC38DD34F5738826F8FD50E0E1A2086D84F175A26E6C32BD1D557AE)

从API version 7开始支持，从API version 9开始废弃，建议使用[backgroundTaskManager.startBackgroundRunning](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager#backgroundtaskmanagerstartbackgroundrunning-1)替代。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| id | number | 是 | 长时任务通知id号。 |
| request | [NotificationRequest](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notification#notificationrequest) | 是 | 通知参数，用于显示通知栏的信息。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例**：

```ts
import { particleAbility, wantAgent } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import notification from '@ohos.notification';

let wantAgentInfo: wantAgent.WantAgentInfo = {
  wants: [
    {
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    }
  ],
  operationType: wantAgent.OperationType.START_ABILITY,
  requestCode: 0,
  wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
};

wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj) => {
  let id = 1;
  particleAbility.startBackgroundRunning(id, {
    content:
    {
      contentType: notification.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
      normal:
      {
        title: 'title',
        text: 'text'
      }
    },
    wantAgent: wantAgentObj
  }).then(() => {
    console.info('Operation succeeded');
  }).catch((err: BusinessError) => {
    console.error(`Operation failed cause: ${JSON.stringify(err)}`);
  });
});
```

#### particleAbility.cancelBackgroundRunning(deprecated)

cancelBackgroundRunning(callback: AsyncCallback<void>): void

向系统申请取消长时任务。使用callback异步回调。

**系统能力**：SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/TD4WvqSBTFGPaSl9EaWH2w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=C5D416269788DFC4F4EF20B44003FF55018F90DCCCAB23A3670EF91EE7DF196C)

从API version 7开始支持，从API version 9开始废弃，建议使用[backgroundTaskManager.stopBackgroundRunning](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager#backgroundtaskmanagerstopbackgroundrunning)替代。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | 是 | 回调函数。当向系统申请取消长时任务成功，err为undefined，否则为错误对象。 |

**示例**：

```ts
import { particleAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback(error: BusinessError, data: void) {
  if (error && error.code !== 0) {
    console.error(`Operation failed error: ${JSON.stringify(error)}`);
  } else {
    console.info(`Operation succeeded, data: ${data}`);
  }
}

particleAbility.cancelBackgroundRunning(callback);
```

#### particleAbility.cancelBackgroundRunning(deprecated)

cancelBackgroundRunning(): Promise<void>

向系统申请取消长时任务。使用Promise异步回调。

**系统能力**：SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/JV0Mr7SXRyKk_V99jXgUIg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=B04AA101FEB78F082FD6FC2E0C353F3E5095E2F5ED87C8AFC8FBF3E6F9BB82E3)

从API version 7开始支持，从API version 9开始废弃，建议使用[backgroundTaskManager.stopBackgroundRunning](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager#backgroundtaskmanagerstopbackgroundrunning-1)替代。

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例**：

```ts
import { particleAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

particleAbility.cancelBackgroundRunning().then(() => {
  console.info('Operation succeeded');
}).catch((err: BusinessError) => {
  console.error(`Operation failed cause: ${JSON.stringify(err)}`);
});
```

#### particleAbility.connectAbility

connectAbility(request: Want, options:ConnectOptions): number

将当前ability与指定的ServiceAbility进行连接。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/aItYOTlhR5-ULlYESaItxA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=D75F1E8E3CA3799CAFC301961893D217872435A3B58CE39FCC124FC7DF8FAC7A)

组件启动规则详见：[组件启动规则（FA模型）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/component-startup-rules-fa)。

跨应用连接serviceAbility，对端应用需配置关联启动。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| request | [Want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-want) | 是 | 表示被连接的ServiceAbility。 |
| options | [ConnectOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-connectoptions) | 是 | 连接回调方法。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 连接的ServiceAbility的ID(ID从0开始自增，每连接成功一次ID加1)。 |

**示例**：

```ts
import { particleAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { BusinessError } from '@kit.BasicServicesKit';

let connId = particleAbility.connectAbility(
  {
    bundleName: 'com.ix.ServiceAbility',
    abilityName: 'ServiceAbilityA',
  },
  {
    onConnect: (element, remote) => {
      console.info(`ConnectAbility onConnect remote is proxy: ${(remote instanceof rpc.RemoteProxy)}`);
    },
    onDisconnect: (element) => {
      console.info(`ConnectAbility onDisconnect element.deviceId: ${element.deviceId}`);
    },
    onFailed: (code) => {
      console.error(`particleAbilityTest ConnectAbility onFailed errCode: ${code}`);
    },
  },
);

particleAbility.disconnectAbility(connId).then((data) => {
  console.info(`data: ${data}`);
}).catch((error: BusinessError) => {
  console.error(`particleAbilityTest result errCode: ${error.code}`);
});
```

#### particleAbility.disconnectAbility

disconnectAbility(connection: number, callback:AsyncCallback<void>): void

断开当前ability与指定ServiceAbility的连接。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| connection | number | 是 | 表示断开连接的ServiceAbility的ID。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当断开当前ability与指定ServiceAbility的连接成功，err为undefined，否则为错误对象。 |

**示例**：

```ts
import { particleAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';

let connId = particleAbility.connectAbility(
  {
    bundleName: 'com.ix.ServiceAbility',
    abilityName: 'ServiceAbilityA',
  },
  {
    onConnect: (element, remote) => {
      console.info(`ConnectAbility onConnect remote is proxy: ${(remote instanceof rpc.RemoteProxy)}`);
    },
    onDisconnect: (element) => {
      console.info(`ConnectAbility onDisconnect element.deviceId: ${element.deviceId}`);
    },
    onFailed: (code) => {
      console.error(`particleAbilityTest ConnectAbility onFailed errCode: ${code}`);
    },
  },
);

particleAbility.disconnectAbility(connId, (err) => {
  console.error(`particleAbilityTest disconnectAbility err: ${JSON.stringify(err)}`);
});
```

#### particleAbility.disconnectAbility

disconnectAbility(connection: number): Promise<void>

断开当前ability与指定ServiceAbility的连接。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| connection | number | 是 | 表示断开连接的ServiceAbility的ID。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例**：

```ts
import { particleAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { BusinessError } from '@kit.BasicServicesKit';

let connId = particleAbility.connectAbility(
  {
    bundleName: 'com.ix.ServiceAbility',
    abilityName: 'ServiceAbilityA',
  },
  {
    onConnect: (element, remote) => {
      console.info(`ConnectAbility onConnect remote is proxy: ${(remote instanceof rpc.RemoteProxy)}`);
    },
    onDisconnect: (element) => {
      console.info(`ConnectAbility onDisconnect element.deviceId: ${element.deviceId}`);
    },
    onFailed: (code) => {
      console.error(`particleAbilityTest ConnectAbility onFailed errCode: ${code}`);
    },
  },
);

particleAbility.disconnectAbility(connId).then(() => {
  console.info('disconnectAbility success');
}).catch((error: BusinessError) => {
  console.error(`particleAbilityTest result errCode : ${error.code}`);
});
```

#### ErrorCode

定义启动Ability时返回的错误码。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| INVALID\_PARAMETER | \-1 | 无效的参数。 |

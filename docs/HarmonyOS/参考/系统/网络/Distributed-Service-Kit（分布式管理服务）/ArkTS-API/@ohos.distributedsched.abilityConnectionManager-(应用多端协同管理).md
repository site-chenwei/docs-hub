---
title: "@ohos.distributedsched.abilityConnectionManager (应用多端协同管理)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributed-abilityconnectionmanager"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Distributed Service Kit（分布式管理服务）"
  - "ArkTS API"
  - "@ohos.distributedsched.abilityConnectionManager (应用多端协同管理)"
captured_at: "2026-04-17T01:48:22.161Z"
---

# @ohos.distributedsched.abilityConnectionManager (应用多端协同管理)

abilityConnectionManager模块提供了应用协同接口管理能力。设备组网成功（需登录同账号、双端打开蓝牙）后，系统应用和三方应用可以跨设备拉起同应用的一个[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)，拉起并连接成功后可实现跨设备数据传输（文本信息）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/6x0bdhfcTcufhweEMnhwNQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=4817936F3F6C759CB4769C98C333174C6E6F73C429B0675ECF76DF743585C71B)

本模块首批接口从API version 18开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 导入模块

```js
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
```

#### abilityConnectionManager.createAbilityConnectionSession

createAbilityConnectionSession(serviceName: string, context: Context, peerInfo: PeerInfo , connectOptions: ConnectOptions): number

创建应用间的协同会话。

**需要权限**：ohos.permission.INTERNET、ohos.permission.GET\_NETWORK\_INFO、ohos.permission.SET\_NETWORK\_INFO和ohos.permission.DISTRIBUTED\_DATASYNC

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| serviceName | string | 是 | 应用设置的服务名称（两端必须一致），最大长度为256字符。 |
| context | [Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context) | 是 | 表示应用上下文。 |
| peerInfo | [PeerInfo](#peerinfo) | 是 | 对端的协同信息。 |
| connectOptions | [ConnectOptions](#connectoptions) | 是 | 应用设置的连接选项。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 成功创建的协同会话ID。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

1.  在设备A上，应用需要主动调用createAbilityConnectionSession()接口创建协同会话并返回sessionId。
    
    ```ts
    import { abilityConnectionManager, distributedDeviceManager } from '@kit.DistributedServiceKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
    let dmClass: distributedDeviceManager.DeviceManager;
    
    function initDmClass(): void {
      try {
        dmClass = distributedDeviceManager.createDeviceManager('com.example.remotephotodemo');
      } catch (err) {
        hilog.error(0x0000, 'testTag', 'createDeviceManager err: ' + JSON.stringify(err));
      }
    }
    
    function getRemoteDeviceId(): string | undefined {
      initDmClass();
      if (typeof dmClass === 'object' && dmClass !== null) {
        hilog.info(0x0000, 'testTag', 'getRemoteDeviceId begin');
        let list = dmClass.getAvailableDeviceListSync();
        if (typeof (list) === 'undefined' || typeof (list.length) === 'undefined') {
          hilog.info(0x0000, 'testTag', 'getRemoteDeviceId err: list is null');
          return;
        }
        if (list.length === 0) {
          hilog.info(0x0000, 'testTag', 'getRemoteDeviceId err: list is empty');
          return;
        }
        return list[0].networkId;
      } else {
        hilog.info(0x0000, 'testTag', 'getRemoteDeviceId err: dmClass is null');
        return;
      }
    }
    
    @Entry
    @Component
    struct Index {
      createSession(): void {
        // 定义peer信息
        const peerInfo: abilityConnectionManager.PeerInfo = {
          deviceId: getRemoteDeviceId()!,
          bundleName: 'com.example.remotephotodemo',
          moduleName: 'entry',
          abilityName: 'EntryAbility',
          serviceName: 'collabTest'
        };
        const myRecord: Record<string, string> = {
          "newKey1": "value1",
        };
    
        // 定义连接选项
        const connectOptions: abilityConnectionManager.ConnectOptions = {
          needSendData: true,
          startOptions: abilityConnectionManager.StartOptionParams.START_IN_FOREGROUND,
          parameters: myRecord
        };
        let context = this.getUIContext().getHostContext();
        try {
          let sessionId = abilityConnectionManager.createAbilityConnectionSession("collabTest", context, peerInfo, connectOptions);
          hilog.info(0x0000, 'testTag', 'createSession sessionId is', sessionId);
        } catch (error) {
          hilog.error(0x0000, 'testTag', error);
        }
      }
    
      build() {
      }
    }
    ```
    
2.  在设备B上，对于createAbilityConnectionSession接口的调用，可在应用被拉起后触发协同生命周期函数onCollaborate时，在onCollaborate内进行。
    
    ```ts
    import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
    import { abilityConnectionManager } from '@kit.DistributedServiceKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
     
    export default class EntryAbility extends UIAbility {
      onCollaborate(wantParam: Record<string, Object>): AbilityConstant.CollaborateResult {
        hilog.info(0x0000, 'testTag', '%{public}s', 'on collaborate');
        let param = wantParam["ohos.extra.param.key.supportCollaborateIndex"] as Record<string, Object>
        this.onCollab(param);
        return 0;
      }
     
      onCollab(collabParam: Record<string, Object>) {
        const sessionId = this.createSessionFromWant(collabParam);
        if (sessionId == -1) {
          hilog.info(0x0000, 'testTag', 'Invalid session ID.');
          return;
        }
      }
     
      createSessionFromWant(collabParam: Record<string, Object>): number {
        let sessionId = -1;
        const peerInfo = collabParam["PeerInfo"] as abilityConnectionManager.PeerInfo;
        if (peerInfo == undefined) {
          return sessionId;
        }
     
        const options = collabParam["ConnectOption"] as abilityConnectionManager.ConnectOptions;
        try {
          sessionId = abilityConnectionManager.createAbilityConnectionSession("collabTest", this.context, peerInfo, options);
          AppStorage.setOrCreate('sessionId', sessionId);
          hilog.info(0x0000, 'testTag', 'createSession sessionId is' + sessionId);
        } catch (error) {
          hilog.error(0x0000, 'testTag', error);
        }
        return sessionId;
      }
    }
    ```
    

#### abilityConnectionManager.destroyAbilityConnectionSession

destroyAbilityConnectionSession(sessionId: number): void

销毁应用间的协同会话。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| sessionId | number | 是 | 待销毁的协同会话ID。 |

**示例：**

```ts
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

hilog.info(0x0000, 'testTag', 'destroyAbilityConnectionSession called');
let sessionId = 100;
abilityConnectionManager.destroyAbilityConnectionSession(sessionId);
```

#### abilityConnectionManager.getPeerInfoById

getPeerInfoById(sessionId: number): PeerInfo | undefined

获取指定会话中对端应用信息。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| sessionId | number | 是 | 协同会话ID。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [PeerInfo](#peerinfo) | undefined | 若存在对应peerInfo，则返回接收端的协作应用信息。若sessionId未找到，则查询失败，返回undefined。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**示例：**

```ts
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

hilog.info(0x0000, 'testTag', 'getPeerInfoById called');
let sessionId = 100;
const peerInfo = abilityConnectionManager.getPeerInfoById(sessionId);
```

#### abilityConnectionManager.connect

connect(sessionId: number): Promise<ConnectResult>

创建协同会话成功并获得会话ID后，设备A上可进行UIAbility的连接。使用Promise异步回调。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| sessionId | number | 是 | 已创建的协同会话ID。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<ConnectResult> | 以Promise形式返回[连接结果](#connectresult)。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

设备A上的应用在创建协同会话成功并获得会话ID后，调用connect()方法启动UIAbility连接，并拉起设备B应用。

```ts
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let sessionId = 100;
abilityConnectionManager.connect(sessionId).then((ConnectResult) => {
  if (!ConnectResult.isConnected) {
    hilog.info(0x0000, 'testTag', 'connect failed');
    return;
  }
}).catch(() => {
  hilog.error(0x0000, 'testTag', "connect failed");
})
```

#### abilityConnectionManager.acceptConnect

acceptConnect(sessionId: number, token: string): Promise<void>

设备B上的应用，在创建协同会话成功并获得会话ID后，调用acceptConnect()方法接受连接。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| sessionId | number | 是 | 已创建的协同会话ID。 |
| token | string | 是 | 设备A应用传入的token值。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

设备B上的应用，在createAbilityConnectionSession接口调用并获取sessionId成功后，可调用acceptConnect接口来选择接受连接。

```ts
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
  }

  onCollaborate(wantParam: Record<string, Object>): AbilityConstant.CollaborateResult {
    hilog.info(0x0000, 'testTag', '%{public}s', 'on collaborate');
    let param = wantParam["ohos.extra.param.key.supportCollaborateIndex"] as Record<string, Object>
    this.onCollab(param);
    return 0;
  }

  onCollab(collabParam: Record<string, Object>) {
    const sessionId = this.createSessionFromWant(collabParam);
    if (sessionId == -1) {
      hilog.info(0x0000, 'testTag', 'Invalid session ID.');
      return;
    }
    const collabToken = collabParam["ohos.dms.collabToken"] as string;
    abilityConnectionManager.acceptConnect(sessionId, collabToken).then(() => {
      hilog.info(0x0000, 'testTag', 'acceptConnect success');
    }).catch(() => {
      hilog.error(0x0000, 'testTag', 'failed');
    })
  }

  createSessionFromWant(collabParam: Record<string, Object>): number {
    let sessionId = -1;
    const peerInfo = collabParam["PeerInfo"] as abilityConnectionManager.PeerInfo;
    if (peerInfo == undefined) {
      return sessionId;
    }

    const options = collabParam["ConnectOption"] as abilityConnectionManager.ConnectOptions;
    try {
      sessionId = abilityConnectionManager.createAbilityConnectionSession("collabTest", this.context, peerInfo, options);
      AppStorage.setOrCreate('sessionId', sessionId);
      hilog.info(0x0000, 'testTag', 'createSession sessionId is' + sessionId);
    } catch (error) {
      hilog.error(0x0000, 'testTag', error);
    }
    return sessionId;
  }
}
```

#### abilityConnectionManager.disconnect

disconnect(sessionId: number): void

当协同业务执行完毕后，协同双端的任意一台设备，应断开UIAbility的连接，结束协同状态。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| sessionId | number | 是 | 协同会话ID |

**示例：**

```ts
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

hilog.info(0x0000, 'testTag', 'disconnectRemoteAbility begin');
let sessionId = 100;
abilityConnectionManager.disconnect(sessionId);
```

#### abilityConnectionManager.reject

reject(token: string, reason: string): void;

在跨端应用协同过程中，在拒绝对端的连接请求后，向对端发送拒绝原因。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| token | string | 是 | 用于协作服务管理的令牌。 |
| reason | string | 是 | 连接被拒绝的原因。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```ts
import { AbilityConstant, UIAbility, Want} from '@kit.AbilityKit';
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class EntryAbility extends UIAbility {
    onCollaborate(wantParam: Record<string, Object>): AbilityConstant.CollaborateResult {
      hilog.info(0x0000, 'testTag', '%{public}s', 'on collaborate');
      let collabParam = wantParam["ohos.extra.param.key.supportCollaborateIndex"] as Record<string, Object>;
      const collabToken = collabParam["ohos.dms.collabToken"] as string;
      const reason = "test";
      hilog.info(0x0000, 'testTag', 'reject begin');
      abilityConnectionManager.reject(collabToken, reason);
      return AbilityConstant.CollaborateResult.REJECT;
    }
}
```

#### abilityConnectionManager.on('connect')

on(type: 'connect', sessionId: number, callback: Callback<EventCallbackInfo>): void

注册connect事件的回调监听。使用callback异步回调。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 事件回调类型，支持的事件为'connect'，完成[abilityConnectionManager.connect()](#abilityconnectionmanagerconnect)调用，触发该事件。 |
| sessionId | number | 是 | 创建的协同会话ID。 |
| callback | Callback<[EventCallbackInfo](#eventcallbackinfo)\> | 是 | 注册的回调函数。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```ts
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let sessionId = 100;
abilityConnectionManager.on("connect", sessionId,(callbackInfo) => {
  hilog.info(0x0000, 'testTag', 'session connect, sessionId is', callbackInfo.sessionId);
});
```

#### abilityConnectionManager.off('connect')

off(type: 'connect', sessionId: number, callback?: Callback<EventCallbackInfo>): void

取消connect事件的回调监听。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 事件回调类型，支持的事件为'connect'。 |
| sessionId | number | 是 | 创建的协同会话ID。 |
| callback | Callback<[EventCallbackInfo](#eventcallbackinfo)\> | 否 | 注册的回调函数。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```ts
import { abilityConnectionManager } from '@kit.DistributedServiceKit';

let sessionId = 100;
abilityConnectionManager.off("connect", sessionId);
```

#### abilityConnectionManager.on('disconnect')

on(type: 'disconnect', sessionId: number, callback: Callback<EventCallbackInfo>): void

注册disconnect事件的回调监听。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 事件回调类型，支持的事件为'disconnect'，完成[abilityConnectionManager.disconnect()](#abilityconnectionmanagerdisconnect)调用，触发该事件。 |
| sessionId | number | 是 | 创建的协同会话ID。 |
| callback | Callback<[EventCallbackInfo](#eventcallbackinfo)\> | 是 | 注册的回调函数。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```ts
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let sessionId = 100;
abilityConnectionManager.on("disconnect", sessionId,(callbackInfo) => {
  hilog.info(0x0000, 'testTag', 'session disconnect, sessionId is', callbackInfo.sessionId);
});
```

#### abilityConnectionManager.off('disconnect')

off(type: 'disconnect', sessionId: number, callback?: Callback<EventCallbackInfo>): void

取消disconnect事件的回调监听。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 事件回调类型，支持的事件为'disconnect'。 |
| sessionId | number | 是 | 创建的协同会话ID。 |
| callback | Callback<[EventCallbackInfo](#eventcallbackinfo)\> | 否 | 注册的回调函数。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```ts
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let sessionId = 100;
abilityConnectionManager.off("disconnect", sessionId);
```

#### abilityConnectionManager.on('receiveMessage')

on(type: 'receiveMessage', sessionId: number, callback: Callback<EventCallbackInfo>): void

注册receiveMessage事件的回调监听。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 事件回调类型，支持的事件为'receiveMessage'，完成[abilityConnectionManager.sendMessage()](#abilityconnectionmanagersendmessage)调用，触发该事件。 |
| sessionId | number | 是 | 创建的协同会话ID。 |
| callback | Callback<[EventCallbackInfo](#eventcallbackinfo)\> | 是 | 注册的回调函数。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```ts
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let sessionId = 100;
abilityConnectionManager.on("receiveMessage", sessionId,(callbackInfo) => {
  hilog.info(0x0000, 'testTag', 'receiveMessage, sessionId is', callbackInfo.sessionId);
});
```

#### abilityConnectionManager.off('receiveMessage')

off(type: 'receiveMessage', sessionId: number, callback?: Callback<EventCallbackInfo>): void

取消receiveMessage事件的回调监听。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 事件回调类型，支持的事件为'receiveMessage'。 |
| sessionId | number | 是 | 创建的协同会话ID。 |
| callback | Callback<[EventCallbackInfo](#eventcallbackinfo)\> | 否 | 注册的回调函数。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```ts
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let sessionId = 100;
abilityConnectionManager.off("receiveMessage", sessionId);
```

#### abilityConnectionManager.on('receiveData')

on(type: 'receiveData', sessionId: number, callback: Callback<EventCallbackInfo>): void

注册receiveData事件的回调监听。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 事件回调类型，支持的事件为'receiveData'，完成[abilityConnectionManager.sendData()](#abilityconnectionmanagersenddata)调用，触发该事件。 |
| sessionId | number | 是 | 创建的协同会话ID。 |
| callback | Callback<[EventCallbackInfo](#eventcallbackinfo)\> | 是 | 注册的回调函数。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```ts
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let sessionId = 100;
abilityConnectionManager.on("receiveData", sessionId,(callbackInfo) => {
  hilog.info(0x0000, 'testTag', 'receiveData, sessionId is', callbackInfo.sessionId);
});
```

#### abilityConnectionManager.off('receiveData')

off(type: 'receiveData', sessionId: number, callback?: Callback<EventCallbackInfo>): void

取消receiveData事件的回调监听。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 事件回调类型，支持的事件为'receiveData'，完成。 |
| sessionId | number | 是 | 创建的协同会话ID。 |
| callback | Callback<[EventCallbackInfo](#eventcallbackinfo)\> | 否 | 注册的回调函数。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```ts
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let sessionId = 100;
abilityConnectionManager.off("receiveData", sessionId);
```

#### abilityConnectionManager.sendMessage

sendMessage(sessionId: number, msg: string): Promise<void>

应用连接成功后，设备A或设备B可向对端设备发送文本信息。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| sessionId | number | 是 | 协同会话ID。 |
| msg | string | 是 | 文本信息内容（内容最大限制为1KB）。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的promise对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```ts
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let sessionId = 100;
abilityConnectionManager.sendMessage(sessionId, "message send success").then(() => {
  hilog.info(0x0000, 'testTag', "sendMessage success");
}).catch(() => {
  hilog.error(0x0000, 'testTag', "connect failed");
})
```

#### abilityConnectionManager.sendData

sendData(sessionId: number, data: ArrayBuffer): Promise<void>

应用连接成功后，设备A或设备B可向对端设备发送[ArrayBuffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arraybuffer-object)字节流。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| sessionId | number | 是 | 协同会话ID。 |
| data | [ArrayBuffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arraybuffer-object) | 是 | 字节流信息。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的promise对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```ts
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { util } from '@kit.ArkTS';

let textEncoder = util.TextEncoder.create("utf-8");
const arrayBuffer  = textEncoder.encodeInto("data send success");

let sessionId = 100;
abilityConnectionManager.sendData(sessionId, arrayBuffer.buffer).then(() => {
  hilog.info(0x0000, 'testTag', "sendMessage success");
}).catch(() => {
  hilog.info(0x0000, 'testTag', "sendMessage failed");
})
```

#### PeerInfo

应用协同信息。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | 否 | 否 | 对端设备ID。 |
| bundleName | string | 否 | 否 | 对端应用的包名。 |
| moduleName | string | 否 | 否 | 对端应用的模块名。 |
| abilityName | string | 否 | 否 | 对端应用的组件名。 |
| serviceName | string | 否 | 是 | 应用设置的服务名称。 |

#### ConnectOptions

应用连接时所需的连接选项。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| needSendData | boolean | 否 | 是 | true代表需要传输数据，false代表不需要传输数据。 |
| startOptions | [StartOptionParams](#startoptionparams) | 否 | 是 | 配置应用启动选项。 |
| parameters | Record<string, string> | 否 | 是 | 配置连接所需的额外信息。 |

#### ConnectResult

连接的结果。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| isConnected | boolean | 否 | 否 | true表示连接成功，false表示连接失败。 |
| errorCode | [ConnectErrorCode](#connecterrorcode) | 否 | 是 | 表示连接错误码。 |
| reason | string | 否 | 是 | 表示拒绝连接的原因。 |

#### EventCallbackInfo

回调方法的接收信息。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| sessionId | number | 否 | 否 | 表示当前事件对应的协同会话ID。 |
| reason | [DisconnectReason](#disconnectreason) | 否 | 是 | 表示断连原因。 |
| msg | string | 否 | 是 | 表示接收的消息。 |
| data | ArrayBuffer | 否 | 是 | 表示接收的字节流。 |

#### CollaborateEventInfo

协同事件信息。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| eventType | [CollaborateEventType](#collaborateeventtype) | 否 | 否 | 表示协同事件的类型。 |
| eventMsg | string | 否 | 是 | 表示协同事件的消息内容。 |

#### ConnectErrorCode

连接的错误码。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| CONNECTED\_SESSION\_EXISTS | 0 | 表示应用之间存在已连接的会话。 |
| PEER\_APP\_REJECTED | 1 | 表示对端应用拒绝了协作请求。 |
| LOCAL\_WIFI\_NOT\_OPEN | 2 | 表示本端WiFi未开启。 |
| PEER\_WIFI\_NOT\_OPEN | 3 | 表示对端WiFi未开启。 |
| PEER\_ABILITY\_NO\_ONCOLLABORATE | 4 | 表示未实现onCollaborate方法。 |
| SYSTEM\_INTERNAL\_ERROR | 5 | 表示系统内部错误。 |

#### StartOptionParams

启动选项参数的枚举。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| START\_IN\_FOREGROUND | 0 | 表示将对端应用启动至前台。 |

#### CollaborateEventType

协同事件类型的枚举。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| SEND\_FAILURE | 0 | 表示任务发送失败。 |
| COLOR\_SPACE\_CONVERSION\_FAILURE | 1 | 表示色彩空间转换失败。 |

#### DisconnectReason

当前断连原因的枚举。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| PEER\_APP\_CLOSE\_COLLABORATION | 0 | 表示对端应用主动关闭了协作。 |
| PEER\_APP\_EXIT | 1 | 表示对端应用退出。 |
| NETWORK\_DISCONNECTED | 2 | 表示网络断开。 |

#### CollaborationKeys

应用协作键值的枚举。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| PEER\_INFO | ohos.collaboration.key.peerInfo | 表示对端设备信息的键值。 |
| CONNECT\_OPTIONS | ohos.collaboration.key.connectOptions | 表示连接选项的键值。 |
| COLLABORATE\_TYPE | ohos.collaboration.key.abilityCollaborateType | 表示协作类型的键值。 |

#### CollaborationValues

**模型约束**：此接口仅可在Stage模型下使用。

应用协作相关值的枚举。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| ABILITY\_COLLABORATION\_TYPE\_DEFAULT | ohos.collaboration.value.abilityCollab | 表示默认的协作类型。 |
| ABILITY\_COLLABORATION\_TYPE\_CONNECT\_PROXY | ohos.collaboration.value.connectProxy | 表示连接代理的协作类型。 |

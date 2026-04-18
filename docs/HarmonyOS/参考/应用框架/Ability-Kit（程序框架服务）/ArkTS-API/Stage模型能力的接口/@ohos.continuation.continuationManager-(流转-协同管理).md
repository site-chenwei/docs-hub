---
title: "@ohos.continuation.continuationManager (流转/协同管理)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-continuation-continuationmanager"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "Stage模型能力的接口"
  - "@ohos.continuation.continuationManager (流转/协同管理)"
captured_at: "2026-04-17T01:47:46.812Z"
---

# @ohos.continuation.continuationManager (流转/协同管理)

continuationManager模块提供了流转/协同入口管理服务能力，包括连接/取消流转管理服务，注册/解注册设备连接变化监听，拉起设备选择模块，更新连接状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/qnLzSO2kQ4OUF5e8XhUghw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=369C8DAD609EE51F4F9522DE1709D52CAB9B79A4C1B4CDD98BC9A0E153A104FE)

本模块首批接口从API version 8开始支持，从API version 22开始废弃，建议使用[分布式设备管理](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager)替代。

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ts
import { continuationManager } from '@kit.AbilityKit';
```

#### continuationManager.register(deprecated)

register(callback: AsyncCallback<number>): void

注册流转管理服务，并获取对应的注册token，无过滤条件，使用AsyncCallback方式作为异步方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/9dITL7yEThKvgQmWGoljtw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=E698ACC7B6D0603705ADB31401ACA150FEE61DAFED060FB123737B5BB617FE0D)

从API version 9开始废弃，建议使用[ondevicestatechange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager#ondevicestatechange)替代。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | 是 | AsyncCallback形式返回流转管理服务连接后生成的token。 |

**示例：**

```ts
import { continuationManager } from '@kit.AbilityKit';

let token: number = -1;
continuationManager.register((err, data) => {
  if (err.code != 0) {
    console.error('register failed, cause: ' + JSON.stringify(err));
    return;
  }
  console.info('register finished, ' + JSON.stringify(data));
  token = data;
});
```

#### continuationManager.register(deprecated)

register(options: ContinuationExtraParams, callback: AsyncCallback<number>): void

连接流转管理服务，并获取对应的注册token，使用AsyncCallback方式作为异步方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/9pRr9nu8S3qXtv95h10vqQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=AEA92660A0C32EC7C691C1B09C85900FD7635FC6E9DBA74F1A53B872C7FF831E)

从API version 9开始废弃，建议使用[onDeviceStateChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager#ondevicestatechange)替代。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [ContinuationExtraParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-continuation-continuationextraparams) | 是 | 过滤可选择设备列表的额外参数。 |
| callback | AsyncCallback<number> | 是 | AsyncCallback形式返回流转管理服务连接后生成的token。 |

**示例：**

```ts
import { continuationManager } from '@kit.AbilityKit';

let token: number = -1;
continuationManager.register(
  {
    deviceType: ["00E"]
  },
  (err, data) => {
    if (err.code != 0) {
      console.error('register failed, cause: ' + JSON.stringify(err));
      return;
    }
    console.info('register finished, ' + JSON.stringify(data));
    token = data;
});
```

#### continuationManager.register(deprecated)

register(options?: ContinuationExtraParams): Promise<number>

连接流转管理服务，并获取对应的注册token，使用Promise方式作为异步方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/C_BtdJFdTDeZ4-cbFRCtoQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=F023F7B29CA27C70AC9F74FF7C119ECAC42D6C9FB7BC8A2D0AE500DE6841EC08)

从API version 9开始废弃，建议使用[onDeviceStateChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager#ondevicestatechange)替代。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [ContinuationExtraParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-continuation-continuationextraparams) | 否 | 过滤可选择设备列表的额外参数，该参数可缺省。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | Promise形式返回流转管理服务连接后生成的token。 |

**示例：**

```ts
import { continuationManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let token: number = -1;
continuationManager.register(
  { deviceType: ["00E"] }).then((data) => {
    console.info('register finished, ' + JSON.stringify(data));
    token = data;
  }).catch((err: BusinessError) => {
    console.error('register failed, cause: ' + JSON.stringify(err));
});
```

#### continuationManager.registerContinuation(deprecated)

registerContinuation(callback: AsyncCallback<number>): void

注册流转管理服务，并获取对应的注册token，无过滤条件，使用AsyncCallback方式作为异步方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/o3diGEtvTz-ZVx-qxwoeCw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=30C6DF67E83F089E49787230815A0AEAA9AAEB63D4581DEB6839C9E15A8A0710)

从API version 9开始支持，从API version 22开始废弃，建议使用[onDeviceStateChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager#ondevicestatechange)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | 是 | AsyncCallback形式返回流转管理服务连接后生成的token。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[DistributedSchedule错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-distributedschedule)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600003 | The number of token registration times has reached the upper limit. |

**示例：**

```ts
import { continuationManager } from '@kit.AbilityKit';

let token: number = -1;
try {
  continuationManager.registerContinuation((err, data) => {
    if (err.code != 0) {
      console.error('registerContinuation failed, cause: ' + JSON.stringify(err));
      return;
    }
    console.info('registerContinuation finished, ' + JSON.stringify(data));
    token = data;
  });
} catch (err) {
  console.error('registerContinuation failed, cause: ' + JSON.stringify(err));
}
```

#### continuationManager.registerContinuation(deprecated)

registerContinuation(options: ContinuationExtraParams, callback: AsyncCallback<number>): void

连接流转管理服务，并获取对应的注册token，使用AsyncCallback方式作为异步方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/A_46oA45S421BBwLG7CE0g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=F00AB3747078B6D1983FBF2F87A34D5BB517444D3D730293DCE5D28810A41A2D)

从API version 9开始支持，从API version 22开始废弃，建议使用[onDeviceStateChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager#ondevicestatechange)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [ContinuationExtraParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-continuation-continuationextraparams) | 是 | 过滤可选择设备列表的额外参数。 |
| callback | AsyncCallback<number> | 是 | AsyncCallback形式返回流转管理服务连接后生成的token。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[DistributedSchedule错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-distributedschedule)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600003 | The number of token registration times has reached the upper limit. |

**示例：**

```ts
import { continuationManager } from '@kit.AbilityKit';

let token: number = -1;
try {
  continuationManager.registerContinuation(
    {
      deviceType: ["00E"]
    },
    (err, data) => {
      if (err.code != 0) {
        console.error('registerContinuation failed, cause: ' + JSON.stringify(err));
        return;
      }
      console.info('registerContinuation finished, ' + JSON.stringify(data));
      token = data;
  });
} catch (err) {
  console.error('registerContinuation failed, cause: ' + JSON.stringify(err));
}
```

#### continuationManager.registerContinuation(deprecated)

registerContinuation(options?: ContinuationExtraParams): Promise<number>

连接流转管理服务，并获取对应的注册token，使用Promise方式作为异步方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/UwPgb52SSoOXDqpXr5czwg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=6BF2EB0AA0EB467A1DCF63944D2F1FC9421E6B2E9EFA6F95C406180EFC4DD4DA)

从API version 9开始支持，从API version 22开始废弃，建议使用[onDeviceStateChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager#ondevicestatechange)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [ContinuationExtraParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-continuation-continuationextraparams) | 否 | 过滤可选择设备列表的额外参数，该参数可缺省。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | Promise形式返回流转管理服务连接后生成的token。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[DistributedSchedule错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-distributedschedule)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600003 | The number of token registration times has reached the upper limit. |

**示例：**

```ts
import { continuationManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let token: number = -1;
try {
  continuationManager.registerContinuation(
    {
      deviceType: ["00E"]
    }).then((data) => {
      console.info('registerContinuation finished, ' + JSON.stringify(data));
      token = data;
    }).catch((err: BusinessError) => {
      console.error('registerContinuation failed, cause: ' + JSON.stringify(err));
  });
} catch (err) {
  console.error('registerContinuation failed, cause: ' + JSON.stringify(err));
}
```

#### continuationManager.on('deviceConnect')(deprecated)

on(type: 'deviceConnect', callback: Callback<ContinuationResult>): void

异步方法，监听设备连接状态，使用Callback形式返回连接的设备信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/-3dCk5aqSZW1ZWpW07GAUw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=EDE154EE29C4A91133E1012F5D1D43DDB0D100570B0421CBC638577151B2C1B2)

从API version 9开始废弃，建议使用[onDeviceStateChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager#ondevicestatechange)替代。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 监听的事件类型，固定值"deviceConnect"。 |
| callback | Callback<[ContinuationResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-continuation-continuationresult)\> | 是 | 当用户从设备选择模块中选择设备时调用，返回设备ID、设备类型和设备名称供开发者使用。 |

**示例：**

```ts
import { continuationManager } from '@kit.AbilityKit';

continuationManager.on("deviceConnect", (data) => {
  console.info('onDeviceConnect deviceId: ' + JSON.stringify(data.id));
  console.info('onDeviceConnect deviceType: ' + JSON.stringify(data.type));
  console.info('onDeviceConnect deviceName: ' + JSON.stringify(data.name));
});
```

#### continuationManager.on('deviceDisconnect')(deprecated)

on(type: 'deviceDisconnect', callback: Callback<string>): void

异步方法，监听设备断开状态，使用Callback形式返回断开的设备信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/FxHd7Nx1Syy3z6Bi7I_wuw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=232FC8B4BE315BA3D6462B22EE42F4BF6A9310948695515A05B8A612E1573486)

从API version 9开始废弃，建议使用[onDeviceStateChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager#ondevicestatechange)替代。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 监听的事件类型，固定值"deviceDisconnect"。 |
| callback | Callback<string> | 是 | 当用户从设备选择模块中断开设备时调用，返回设备ID供开发者使用。 |

**示例：**

```ts
import { continuationManager } from '@kit.AbilityKit';

continuationManager.on("deviceDisconnect", (data) => {
  console.info('onDeviceDisconnect deviceId: ' + JSON.stringify(data));
});
```

#### continuationManager.off('deviceConnect')(deprecated)

off(type: 'deviceConnect', callback?: Callback<ContinuationResult>): void

异步方法，取消监听设备连接状态，使用Callback形式返回连接的设备信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/kOeW3XzzTgKNUWCtMrcx1A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=F6D38A3CF0731D6C9D31925A15AFB332A2BFAC0E4FB83C96CFD7AAAC079346C0)

从API version 9开始废弃，建议使用[offDeviceStateChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager#offdevicestatechange)替代。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 取消监听的事件类型，固定值"deviceConnect"。 |
| callback | Callback<[ContinuationResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-continuation-continuationresult)\> | 否 | 当用户从设备选择模块中选择设备时调用，返回设备ID、设备类型和设备名称供开发者使用。 |

**示例：**

```ts
import { continuationManager } from '@kit.AbilityKit';

continuationManager.off("deviceConnect", (data) => {
  console.info('onDeviceConnect deviceId: ' + JSON.stringify(data.id));
  console.info('onDeviceConnect deviceType: ' + JSON.stringify(data.type));
  console.info('onDeviceConnect deviceName: ' + JSON.stringify(data.name));
});
```

#### continuationManager.off('deviceDisconnect')(deprecated)

off(type: 'deviceDisconnect', callback?: Callback<string>): void

异步方法，取消监听设备断开状态，使用Callback形式返回连接的设备信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/WFHKcH2zRb2f9gVoKAiUNw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=7F2D911839CC05E76DD7425E7F789FA7D0368351DF471DB666BD46A6E769B8B3)

从API version 9开始废弃，建议使用[offDeviceStateChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager#offdevicestatechange)替代。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 取消监听的事件类型，固定值"deviceDisconnect"。 |
| callback | Callback<string> | 否 | 当用户从设备选择模块中断开设备时调用，返回设备ID供开发者使用。 |

**示例：**

```ts
import { continuationManager } from '@kit.AbilityKit';

continuationManager.off("deviceDisconnect", (data) => {
  console.info('onDeviceDisconnect deviceId: ' + JSON.stringify(data));
});
```

#### continuationManager.on('deviceSelected')(deprecated)

on(type: 'deviceSelected', token: number, callback: Callback<Array<ContinuationResult>>): void

异步方法，监听设备连接状态，使用Callback形式返回连接的设备信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/TTJJFXRCQJOTE0T9LOvXsA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=308F2EBE502A8A4CFB9AA3FFAF909AF42221F18F56F8EF436994E63CCF866A0E)

从API version 9开始支持，从API version 22开始废弃，建议使用[onDeviceStateChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager#ondevicestatechange)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 监听的事件类型，固定值"deviceSelected"。 |
| token | number | 是 | 注册后的token。 |
| callback | Callback<Array<[ContinuationResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-continuation-continuationresult)\>> | 是 | 当用户从设备选择模块中选择设备时调用，返回设备ID、设备类型和设备名称供开发者使用。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[DistributedSchedule错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-distributedschedule)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600002 | The specified token or callback is not registered. |
| 16600004 | The specified callback has been registered. |

**示例：**

```ts
import { continuationManager } from '@kit.AbilityKit';

let token: number = 1;
try {
  continuationManager.on("deviceSelected", token, (data) => {
    console.info('onDeviceSelected len: ' + data.length);
    for (let i = 0; i < data.length; i++) {
      console.info('onDeviceSelected deviceId: ' + JSON.stringify(data[i].id));
      console.info('onDeviceSelected deviceType: ' + JSON.stringify(data[i].type));
      console.info('onDeviceSelected deviceName: ' + JSON.stringify(data[i].name));
    }
  });
} catch (err) {
  console.error('on failed, cause: ' + JSON.stringify(err));
}
```

#### continuationManager.on('deviceUnselected')(deprecated)

on(type: 'deviceUnselected', token: number, callback: Callback<Array<ContinuationResult>>): void

异步方法，监听设备断开状态，使用Callback形式返回断开的设备信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/gzzy_mmkSVKl8tEbDz5GXw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=494FDDCC483D4C1E698C399A913A851E47F5A144FD9C791A6FA7BEE83497567A)

从API version 9开始支持，从API version 22开始废弃，建议使用[onDeviceStateChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager#ondevicestatechange)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 监听的事件类型，固定值"deviceUnselected"。 |
| token | number | 是 | 注册后的token。 |
| callback | Callback<Array<[ContinuationResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-continuation-continuationresult)\>> | 是 | 当用户从设备选择模块中断开设备时调用，返回设备ID、设备类型和设备名称供开发者使用。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[DistributedSchedule错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-distributedschedule)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600002 | The specified token or callback is not registered. |
| 16600004 | The specified callback has been registered. |

**示例：**

```ts
import { continuationManager } from '@kit.AbilityKit';

let token: number = 1;
try {
  continuationManager.on("deviceUnselected", token, (data) => {
    console.info('onDeviceUnselected len: ' + data.length);
    for (let i = 0; i < data.length; i++) {
      console.info('onDeviceUnselected deviceId: ' + JSON.stringify(data[i].id));
      console.info('onDeviceUnselected deviceType: ' + JSON.stringify(data[i].type));
      console.info('onDeviceUnselected deviceName: ' + JSON.stringify(data[i].name));
    }
    console.info('onDeviceUnselected finished.');
  });
} catch (err) {
  console.error('on failed, cause: ' + JSON.stringify(err));
}
```

#### continuationManager.off('deviceSelected')(deprecated)

off(type: 'deviceSelected', token: number): void

取消监听设备连接状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/oRjEOVROSQiK2csQC92azA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=BD4DA8797492F4E439A6FFAF502D2C8840DA6E47FDA57C7BD50F8FE4DF1B7EA2)

从API version 9开始支持，从API version 22开始废弃，建议使用[offDeviceStateChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager#offdevicestatechange)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 取消监听的事件类型，固定值"deviceSelected"。 |
| token | number | 是 | 注册后的token。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[DistributedSchedule错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-distributedschedule)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600002 | The specified token or callback is not registered. |
| 16600004 | The specified callback has been registered. |

**示例：**

```ts
import { continuationManager } from '@kit.AbilityKit';

let token: number = 1;
try {
  continuationManager.off("deviceSelected", token);
} catch (err) {
  console.error('off failed, cause: ' + JSON.stringify(err));
}
```

#### continuationManager.off('deviceUnselected')(deprecated)

off(type: 'deviceUnselected', token: number): void

取消监听设备断开状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/Edowr3EoQAidfTVJSXOGkA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=CDF0C2D02AC05C202A02DED3B9E83DDD4C34772693D561BC34452777F8B346BB)

从API version 9开始支持，从API version 22开始废弃，建议使用[offDeviceStateChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager#offdevicestatechange)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 取消监听的事件类型，固定值"deviceUnselected"。 |
| token | number | 是 | 注册后的token。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[DistributedSchedule错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-distributedschedule)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600002 | The specified token or callback is not registered. |
| 16600004 | The specified callback has been registered. |

**示例：**

```ts
import { continuationManager } from '@kit.AbilityKit';

let token: number = 1;
try {
  continuationManager.off("deviceUnselected", token);
} catch (err) {
  console.error('off failed, cause: ' + JSON.stringify(err));
}
```

#### continuationManager.startDeviceManager(deprecated)

startDeviceManager(token: number, callback: AsyncCallback<void>): void

拉起设备选择模块，可显示组网内可选择设备列表信息，无过滤条件，使用AsyncCallback方式作为异步方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/cYZCpioXSemhbH6bTqSrUg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=63DC11B4A0816BE6549142389BAE6738CC6535D23CFDA84CB7999573D36DC911)

从API version 9开始废弃，建议使用[startDiscovering](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager#startdiscovering)替代。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| token | number | 是 | 注册后的token。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当模块选择完成，err为undefined，否则返回错误对象。 |

**示例：**

```ts
import { continuationManager } from '@kit.AbilityKit';

let token: number = 1;
continuationManager.startDeviceManager(token, (err) => {
  if (err.code != 0) {
    console.error('startDeviceManager failed, cause: ' + JSON.stringify(err));
    return;
  }
  console.info('startDeviceManager finished. ');
});
```

#### continuationManager.startDeviceManager(deprecated)

startDeviceManager(token: number, options: ContinuationExtraParams, callback: AsyncCallback<void>): void

拉起设备选择模块，可显示组网内可选择设备列表信息，使用AsyncCallback方式作为异步方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/1gBWI57jSH62G57uxq4x0w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=2AD65AEB720D46FFE49D2167523F6C25047024CF2EB7EF07D4A68B7E8905CA74)

从API version 9开始废弃，建议使用[startDiscovering](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager#startdiscovering)替代。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| token | number | 是 | 注册后的token。 |
| options | [ContinuationExtraParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-continuation-continuationextraparams) | 是 | 过滤可选择设备列表的额外参数。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当模块选择完成，err为undefined，否则返回错误对象。 |

**示例：**

```ts
import { continuationManager } from '@kit.AbilityKit';

let token: number = 1;
continuationManager.startDeviceManager(
  token,
  {
    deviceType: ["00E"]
  },
  (err) => {
    if (err.code != 0) {
      console.error('startDeviceManager failed, cause: ' + JSON.stringify(err));
      return;
    }
    console.info('startDeviceManager finished. ');
});
```

#### continuationManager.startDeviceManager(deprecated)

startDeviceManager(token: number, options?: ContinuationExtraParams): Promise<void>

拉起设备选择模块，可显示组网内可选择设备列表信息，使用Promise方式作为异步方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/dvMXClrVTxCHV_KnB0ZGFQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=2584642EAEEDAB196556A854015AE610F978B5EF2D10E70C64E9A8740EA63EAE)

从API version 9开始废弃，建议使用[startDiscovering](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager#startdiscovering)替代。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| token | number | 是 | 注册后的token。 |
| options | [ContinuationExtraParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-continuation-continuationextraparams) | 否 | 过滤可选择设备列表的额外参数，该参数可缺省。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise形式返回接口调用结果。 |

**示例：**

```ts
import { continuationManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let token: number = -1;
continuationManager.startDeviceManager(
  token,
  {
    deviceType: ["00E"]
  }).then(() => {
    console.info('startDeviceManager finished. ');
  }).catch((err: BusinessError) => {
    console.error('startDeviceManager failed, cause: ' + JSON.stringify(err));
});
```

#### continuationManager.startContinuationDeviceManager(deprecated)

startContinuationDeviceManager(token: number, callback: AsyncCallback<void>): void

拉起设备选择模块，可显示组网内可选择设备列表信息，无过滤条件，使用AsyncCallback方式作为异步方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/Jq2_E6o5Ri-yrPpTKgczsA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=D146FCA63D1FD1FB7CDD85B0ECA34669EDC97306AB2832D06992EAB36F0F770A)

从API version 9开始支持，从API version 22开始废弃，建议使用[startDiscovering](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager#startdiscovering)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| token | number | 是 | 注册后的token。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当模块选择完成，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[DistributedSchedule错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-distributedschedule)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600002 | The specified token or callback is not registered. |

**示例：**

```ts
import { continuationManager } from '@kit.AbilityKit';

let token: number = -1;
try {
  continuationManager.startContinuationDeviceManager(token, (err) => {
    if (err.code != 0) {
      console.error('startContinuationDeviceManager failed, cause: ' + JSON.stringify(err));
      return;
    }
    console.info('startContinuationDeviceManager finished. ');
  });
} catch (err) {
  console.error('startContinuationDeviceManager failed, cause: ' + JSON.stringify(err));
}
```

#### continuationManager.startContinuationDeviceManager(deprecated)

startContinuationDeviceManager(token: number, options: ContinuationExtraParams, callback: AsyncCallback<void>): void

拉起设备选择模块，可显示组网内可选择设备列表信息，使用AsyncCallback方式作为异步方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/lpG_D_upRI2EBG0HZnThBQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=B18693BF21F2CC70DC98F61D73608735955651756F9EB17269E1B1809122C61C)

从API version 9开始支持，从API version 22开始废弃，建议使用[startDiscovering](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager#startdiscovering)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| token | number | 是 | 注册后的token。 |
| options | [ContinuationExtraParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-continuation-continuationextraparams) | 是 | 过滤可选择设备列表的额外参数。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当模块选择完成，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[DistributedSchedule错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-distributedschedule)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600002 | The specified token or callback is not registered. |

**示例：**

```ts
import { continuationManager } from '@kit.AbilityKit';

let token: number = -1;
try {
  continuationManager.startContinuationDeviceManager(
    token,
    {
      deviceType: ["00E"]
    },
    (err) => {
      if (err.code != 0) {
        console.error('startContinuationDeviceManager failed, cause: ' + JSON.stringify(err));
        return;
      }
      console.info('startContinuationDeviceManager finished. ');
  });
} catch (err) {
  console.error('startContinuationDeviceManager failed, cause: ' + JSON.stringify(err));
}
```

#### continuationManager.startContinuationDeviceManager(deprecated)

startContinuationDeviceManager(token: number, options?: ContinuationExtraParams): Promise<void>

拉起设备选择模块，可显示组网内可选择设备列表信息，使用Promise方式作为异步方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/-bJICaksTy6mmpcBPOg0Pg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=92B380ACB5D66A9F8B4C0E2FE4F6E6131587437A6666BB58AC0CC76DDA6AEC68)

从API version 9开始支持，从API version 22开始废弃，建议使用[startDiscovering](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager#startdiscovering)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| token | number | 是 | 注册后的token。 |
| options | [ContinuationExtraParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-continuation-continuationextraparams) | 否 | 过滤可选择设备列表的额外参数，该参数可缺省。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise形式返回接口调用结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[DistributedSchedule错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-distributedschedule)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600002 | The specified token or callback is not registered. |

**示例：**

```ts
import { continuationManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let token: number = -1;
try {
  continuationManager.startContinuationDeviceManager(
    token,
    {
      deviceType: ["00E"]
    }).then(() => {
      console.info('startContinuationDeviceManager finished. ');
    }).catch((err: BusinessError) => {
      console.error('startContinuationDeviceManager failed, cause: ' + JSON.stringify(err));
    });
} catch (err) {
  console.error('startContinuationDeviceManager failed, cause: ' + JSON.stringify(err));
}
```

#### continuationManager.updateConnectStatus(deprecated)

updateConnectStatus(token: number, deviceId: string, status: DeviceConnectState, callback: AsyncCallback<void>): void

通知设备选择模块，更新当前的连接状态，使用AsyncCallback方式作为异步方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/ZJIp2zwGQKOMfNG7YkFmdA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=2EFA78233700D2CEE3EB78D871DD930BEFDC62346AECDDA81EE25986C33A0233)

从API version 9开始废弃，建议使用[getAvailableDeviceListSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager#getavailabledevicelistsync)替代。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| token | number | 是 | 注册后的token。 |
| deviceId | string | 是 | 设备ID。 |
| status | [DeviceConnectState](#deviceconnectstatedeprecated) | 是 | 设备连接状态。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当通知设备成功，err为undefined，否则返回错误对象。 |

**示例：**

```ts
import { continuationManager } from '@kit.AbilityKit';

let token: number = -1;
let deviceId: string = "test deviceId";
continuationManager.updateConnectStatus(token, deviceId, continuationManager.DeviceConnectState.CONNECTED, (err) => {
  if (err.code != 0) {
    console.error('updateConnectStatus failed, cause: ' + JSON.stringify(err));
    return;
  }
  console.info('updateConnectStatus finished. ');
});
```

#### continuationManager.updateConnectStatus(deprecated)

updateConnectStatus(token: number, deviceId: string, status: DeviceConnectState): Promise<void>

通知设备选择模块，更新当前的连接状态，使用Promise方式作为异步方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/jaYw7wPKSiaUJtvKC-l6EQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=5389F75DBA1DA3536F0297064E794AA1768681BFC2412D9B039AFD090B663E8B)

从API version 9开始废弃，建议使用[getAvailableDeviceListSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager#getavailabledevicelistsync)替代。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| token | number | 是 | 注册后的token。 |
| deviceId | string | 是 | 设备ID。 |
| status | [DeviceConnectState](#deviceconnectstatedeprecated) | 是 | 设备连接状态。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise形式返回接口调用结果。 |

**示例：**

```ts
import { continuationManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let token: number = 1;
let deviceId: string = "test deviceId";
continuationManager.updateConnectStatus(token, deviceId, continuationManager.DeviceConnectState.CONNECTED)
  .then(() => {
    console.info('updateConnectStatus finished. ');
  })
  .catch((err: BusinessError) => {
    console.error('updateConnectStatus failed, cause: ' + JSON.stringify(err));
});
```

#### continuationManager.updateContinuationState(deprecated)

updateContinuationState(token: number, deviceId: string, status: DeviceConnectState, callback: AsyncCallback<void>): void

通知设备选择模块，更新当前的连接状态，使用AsyncCallback方式作为异步方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/P9S1RxJaS4u8farViPQ5MQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=C249E2279561208233083EBA8C7940F95B436791D969A7CD376A0EC936D5F045)

从API version 9开始支持，从API version 22开始废弃，建议使用[getAvailableDeviceListSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager#getavailabledevicelistsync)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| token | number | 是 | 注册后的token。 |
| deviceId | string | 是 | 设备ID。 |
| status | [DeviceConnectState](#deviceconnectstatedeprecated) | 是 | 设备连接状态。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当通知设备成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[DistributedSchedule错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-distributedschedule)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600002 | The specified token or callback is not registered. |

**示例：**

```ts
import { continuationManager } from '@kit.AbilityKit';

let token: number = 1;
let deviceId: string = "test deviceId";
try {
  continuationManager.updateContinuationState(token, deviceId, continuationManager.DeviceConnectState.CONNECTED, (err) => {
    if (err.code != 0) {
      console.error('updateContinuationState failed, cause: ' + JSON.stringify(err));
      return;
    }
    console.info('updateContinuationState finished. ');
  });
} catch (err) {
  console.error('updateContinuationState failed, cause: ' + JSON.stringify(err));
}
```

#### continuationManager.updateContinuationState(deprecated)

updateContinuationState(token: number, deviceId: string, status: DeviceConnectState): Promise<void>

通知设备选择模块，更新当前的连接状态，使用Promise方式作为异步方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/t4n1xYctQNKyYntBrQQAWA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=3D3C853376B1507A78D737FBFDF4973ACD9D1DCE4127ED2E9AC3D768CCA06431)

从API version 9开始支持，从API version 22开始废弃，建议使用[getAvailableDeviceListSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager#getavailabledevicelistsync)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| token | number | 是 | 注册后的token。 |
| deviceId | string | 是 | 设备ID。 |
| status | [DeviceConnectState](#deviceconnectstatedeprecated) | 是 | 设备连接状态。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise形式返回接口调用结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[DistributedSchedule错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-distributedschedule)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600002 | The specified token or callback is not registered. |

**示例：**

```ts
import { continuationManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let token: number = 1;
let deviceId: string = "test deviceId";
try {
  continuationManager.updateContinuationState(token, deviceId, continuationManager.DeviceConnectState.CONNECTED)
    .then(() => {
      console.info('updateContinuationState finished. ');
    })
    .catch((err: BusinessError) => {
      console.error('updateContinuationState failed, cause: ' + JSON.stringify(err));
    });
} catch (err) {
  console.error('updateContinuationState failed, cause: ' + JSON.stringify(err));
}
```

#### continuationManager.unregister(deprecated)

unregister(token: number, callback: AsyncCallback<void>): void

解注册流转管理服务，传入注册时获取的token进行解注册，使用AsyncCallback方式作为异步方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/6L-PGPXeTeel-YeHTXqUUA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=49135EA2A6A7B524DE521EDBD692EAF2402C04CF20FAFA671D46A5227011CEC6)

从API version 9开始废弃，建议使用[offDeviceStateChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager#offdevicestatechange)替代。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| token | number | 是 | 注册后的token。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当解注册成功，err为undefined，否则返回错误对象。 |

**示例：**

```ts
import { continuationManager } from '@kit.AbilityKit';

let token: number = 1;
continuationManager.unregister(token, (err) => {
  if (err.code != 0) {
    console.error('unregister failed, cause: ' + JSON.stringify(err));
    return;
  }
  console.info('unregister finished. ');
});
```

#### continuationManager.unregister(deprecated)

unregister(token: number): Promise<void>

解注册流转管理服务，传入注册时获取的token进行解注册，使用Promise方式作为异步方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/FCExLLK4SnCwFj_WtvniKQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=556AB3D52B24B8F5D4605C78432A084F131617CE077ACEC9F929A9B926C6CA53)

从API version 9开始废弃，建议使用[offDeviceStateChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager#offdevicestatechange)替代。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| token | number | 是 | 注册后的token。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise形式返回接口调用结果。 |

**示例：**

```ts
import { continuationManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let token: number = 1;
continuationManager.unregister(token)
  .then(() => {
    console.info('unregister finished. ');
  }).catch((err: BusinessError) => {
    console.error('unregister failed, cause: ' + JSON.stringify(err));
});
```

#### continuationManager.unregisterContinuation(deprecated)

unregisterContinuation(token: number, callback: AsyncCallback<void>): void

解注册流转管理服务，传入注册时获取的token进行解注册，使用AsyncCallback方式作为异步方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/F7Tn2XpiQD-uk-0cpUyvbQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=AEA6DBB57BBA9589828F6C499205DEDA6E6D2E6BEB87859924B0F2471EE12626)

从API version 9开始支持，从API version 22开始废弃，建议使用[offDeviceStateChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager#offdevicestatechange)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| token | number | 是 | 注册后的token。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当解注册成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[DistributedSchedule错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-distributedschedule)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600002 | The specified token or callback is not registered. |

**示例：**

```ts
import { continuationManager } from '@kit.AbilityKit';

let token: number = 1;
try {
  continuationManager.unregisterContinuation(token, (err) => {
    if (err.code != 0) {
      console.error('unregisterContinuation failed, cause: ' + JSON.stringify(err));
      return;
    }
    console.info('unregisterContinuation finished. ');
  });
} catch (err) {
  console.error('unregisterContinuation failed, cause: ' + JSON.stringify(err));
}
```

#### continuationManager.unregisterContinuation(deprecated)

unregisterContinuation(token: number): Promise<void>

解注册流转管理服务，传入注册时获取的token进行解注册，使用Promise方式作为异步方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/38gkWVRxTMSrbbtXrTLJfg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=BFA5E785199F3069B998599776AACADB0CE1E8E84FBE1DCE569E76CCC8471330)

从API version 9开始支持，从API version 22开始废弃，建议使用[offDeviceStateChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager#offdevicestatechange)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| token | number | 是 | 注册后的token。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise形式返回接口调用结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[DistributedSchedule错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-distributedschedule)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600002 | The specified token or callback is not registered. |

**示例：**

```ts
import { continuationManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let token: number = -1;
try {
  continuationManager.unregisterContinuation(token).then(() => {
      console.info('unregisterContinuation finished. ');
    }).catch((err: BusinessError) => {
      console.error('unregisterContinuation failed, cause: ' + JSON.stringify(err));
  });
} catch (err) {
  console.error('unregisterContinuation failed, cause: ' + JSON.stringify(err));
}
```

#### DeviceConnectState(deprecated)

设备连接状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/VxK0CZ3TRmKXBuwKkoiVPA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=9BF9D0AD0A9A1FF89A9C00BF8AC95E35EF2EFC69AE0C99C78445B24D83CDAB05)

从API version 22开始废弃，建议使用[DeviceStateChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager#devicestatechange)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| IDLE | 0 | 设备连接初始状态。 |
| CONNECTING | 1 | 设备连接中状态。 |
| CONNECTED | 2 | 设备已连接状态。 |
| DISCONNECTING | 3 | 设备断开连接状态。 |

#### ContinuationMode(deprecated)

设备选择模块连接模式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/vg3-e-jtSkKMYCtUZFlRLA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=97AC7D532D678F5FEAD1B2B0190A479F038CAA19D6CA377DB2FA55B386B8B05F)

从API version 22开始废弃，建议使用[DeviceStateChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager#devicestatechange)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| COLLABORATION\_SINGLE | 0 | 设备选择模块单选模式。 |
| COLLABORATION\_MULTIPLE | 1 | 设备选择模块多选模式。 |

#### ContinuationResult(deprecated)

type ContinuationResult = \_ContinuationResult

流转管理入口返回的设备信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/FgmMqclsTMmQjg4Azbd0nw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=58D99DC8CFA002C2B2201E3D25F34B17EB98FC6E69F09CFA4CB55138BD9AAA62)

从API version 10开始支持，从API version 22开始废弃，建议使用[DeviceBasicInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager#devicebasicinfo)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

| 类型 | 说明 |
| :-- | :-- |
| [\_ContinuationResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-continuation-continuationresult) | 表示流转管理入口返回的设备信息。 |

#### ContinuationExtraParams(deprecated)

type ContinuationExtraParams = \_ContinuationExtraParams

流转管理入口中设备选择模块所需的过滤参数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/-2wYmxHKQGuUZ4AJ4RSovA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=9775D81CD0E96814FBB83D67D09A031C1657E8CDE83977ABEA7C002A9E2DED50)

从API version 10开始支持，从API version 22开始废弃，建议使用[DeviceBasicInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager#devicebasicinfo)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

| 类型 | 说明 |
| :-- | :-- |
| [\_ContinuationExtraParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-continuation-continuationextraparams) | 表示流转管理入口中设备选择模块所需的过滤参数。 |

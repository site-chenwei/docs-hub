---
title: "@ohos.data.sendablePreferences (共享用户首选项)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-sendablepreferences"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkData（方舟数据管理）"
  - "ArkTS API"
  - "@ohos.data.sendablePreferences (共享用户首选项)"
captured_at: "2026-04-17T01:47:49.264Z"
---

# @ohos.data.sendablePreferences (共享用户首选项)

共享用户首选项为应用提供Key-Value键值型的数据处理能力，支持应用持久化轻量级数据，并对其修改和查询。

数据存储形式为键值对，键的类型为字符串型，值的存储数据类型包括number、string、boolean、bigint以及可序列化的object。

共享用户首选项的持久化文件存储在[preferencesDir](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-context-stage#获取应用文件路径)路径下，创建preferences对象前，需要保证preferencesDir路径可读写。持久化文件存储路径中的[加密等级](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-contextconstant#areamode)会影响文件的可读写状态，路径访问限制详见[应用文件目录与应用文件路径](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-sandbox-directory#应用文件目录与应用文件路径)。

共享用户首选项可以在ArkTS并发实例间（包括主线程、TaskPool&Worker工作线程）传递，传递的行为是引用传递，性能优于普通的[用户首选项](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-preferences)，可参考[Sendable使用场景](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sendable-guide)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/N4sXwVqtQjKJ6wtsKiGmpg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014751Z&HW-CC-Expire=86400&HW-CC-Sign=798A3F671EF82D39E1634EF562A9A411059F253666814DD30A7CB63046A5C9AB)

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

共享用户首选项无法保证进程并发安全，会有文件损坏和数据丢失的风险，不支持在多进程场景下使用。

#### 导入模块

```ts
import { sendablePreferences } from '@kit.ArkData';
```

#### 常量

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

| 名称 | 类型 | 只读 | 说明 |
| :-- | :-- | :-- | :-- |
| MAX\_KEY\_LENGTH | number | 是 | Key的最大长度限制为1024个字节。 |
| MAX\_VALUE\_LENGTH | number | 是 | Value的最大长度限制为16MB。 |

#### sendablePreferences.getPreferences

getPreferences(context: Context, options: Options): Promise<Preferences>

获取Preferences实例，使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| context | [Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context) | 是 | 应用上下文。 |
| options | [Options](#options) | 是 | 与Preferences实例相关的配置选项。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[Preferences](#preferences)\> | 
Promise对象，返回Preferences实例。

该实例继承[ISendable](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable#isendable)，可以在ArkTS并发实例间（包括主线程、TaskPool&Worker工作线程）传递，传递的行为是引用传递，参考[Sendable使用场景](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sendable-guide)。

 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[用户首选项错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-preferences)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 801 | Capability not supported. |
| 15500000 | Inner error. |
| 15501001 | The operations is supported in stage mode only. |
| 15501002 | Invalid dataGroupId. |

**示例：**

```ts
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

let preferences: sendablePreferences.Preferences;

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let options: sendablePreferences.Options = { name: 'myStore' };
    let promise = sendablePreferences.getPreferences(this.context, options);
    promise.then((object: sendablePreferences.Preferences) => {
      preferences = object;
      console.info("Succeeded in getting preferences.");
    }).catch((err: BusinessError) => {
      console.error(`Failed to get preferences. code: ${err.code}, message: ${err.message}`);
    });
  }
}
```

#### sendablePreferences.getPreferencesSync

getPreferencesSync(context: Context, options: Options): Preferences

获取Preferences实例，此为同步接口。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| context | [Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context) | 是 | 应用上下文。 |
| options | [Options](#options) | 是 | 与Preferences实例相关的配置选项。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [Preferences](#preferences) | 
返回Preferences实例。

该实例继承[ISendable](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable#isendable)，可以在ArkTS并发实例间（包括主线程、TaskPool&Worker工作线程）传递，传递的行为是引用传递，参考[Sendable使用场景](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sendable-guide)。

 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[用户首选项错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-preferences)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 801 | Capability not supported. |
| 15500000 | Inner error. |
| 15501001 | The operations is supported in stage mode only. |
| 15501002 | Invalid dataGroupId. |

**示例：**

```ts
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

let preferences: sendablePreferences.Preferences;

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let options: sendablePreferences.Options = { name: 'myStore' };
    preferences = sendablePreferences.getPreferencesSync(this.context, options);
  }
}
```

#### sendablePreferences.deletePreferences

deletePreferences(context: Context, options: Options): Promise<void>

从缓存中删除指定的Preferences实例，若Preferences实例有对应的持久化文件，则同时删除其持久化文件。使用Promise异步回调。

调用该接口后，不建议再使用旧的Preferences实例进行数据操作，否则会导致数据一致性问题。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| context | [Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context) | 是 | 应用上下文。 |
| options | [Options](#options) | 是 | 与Preferences实例相关的配置选项。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[用户首选项错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-preferences)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 801 | Capability not supported. |
| 15500000 | Inner error. |
| 15500010 | Failed to delete the user preferences persistence file. |
| 15501001 | The operations is supported in stage mode only. |
| 15501002 | Invalid dataGroupId. |

**示例：**

```ts
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let options: sendablePreferences.Options = { name: 'myStore' };
    let promise = sendablePreferences.deletePreferences(this.context, options);
    promise.then(() => {
      console.info("Succeeded in deleting preferences.");
    }).catch((err: BusinessError) => {
      console.error(`Failed to delete preferences. code: ${err.code}, message: ${err.message}`);
    });
  }
}
```

#### sendablePreferences.removePreferencesFromCache

removePreferencesFromCache(context: Context, options: Options): Promise<void>

从缓存中移除指定的Preferences实例，使用Promise异步回调。

应用首次调用[getPreferences](#sendablepreferencesgetpreferences)接口获取某个Preferences实例后，该实例会被缓存起来，后续调用[getPreferences](#sendablepreferencesgetpreferences)时不会再次从持久化文件中读取，直接从缓存中获取Preferences实例。调用此接口移除缓存中的实例之后，再次getPreferences将会重新读取持久化文件，生成新的Preferences实例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| context | [Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context) | 是 | 应用上下文。 |
| options | [Options](#options) | 是 | 与Preferences实例相关的配置选项。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[用户首选项错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-preferences)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 801 | Capability not supported. |
| 15500000 | Inner error. |
| 15501001 | The operations is supported in stage mode only. |
| 15501002 | Invalid dataGroupId. |

**示例：**

```ts
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let options: sendablePreferences.Options = { name: 'myStore' };
    let promise = sendablePreferences.removePreferencesFromCache(this.context, options);
    promise.then(() => {
      console.info("Succeeded in removing preferences.");
    }).catch((err: BusinessError) => {
      console.error(`Failed to remove preferences. code: ${err.code}, message: ${err.message}`);
    });
  }
}
```

#### sendablePreferences.removePreferencesFromCacheSync

removePreferencesFromCacheSync(context: Context, options: Options):void

从缓存中移除指定的Preferences实例，此为同步接口。

应用首次调用[getPreferences](#sendablepreferencesgetpreferences)接口获取某个Preferences实例后，该实例会被缓存起来，后续调用[getPreferences](#sendablepreferencesgetpreferences)时不会再次从持久化文件中读取，直接从缓存中获取Preferences实例。调用此接口移除缓存中的实例之后，再次getPreferences将会重新读取持久化文件，生成新的Preferences实例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| context | [Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context) | 是 | 应用上下文。 |
| options | [Options](#options) | 是 | 与Preferences实例相关的配置选项。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[用户首选项错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-preferences)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 801 | Capability not supported. |
| 15500000 | Inner error. |
| 15501001 | The operations is supported in stage mode only. |
| 15501002 | Invalid dataGroupId. |

**示例：**

```ts
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let options: sendablePreferences.Options = { name: 'myStore' };
    sendablePreferences.removePreferencesFromCacheSync(this.context, options);
  }
}
```

#### Options

Preferences实例配置选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| name | string | 否 | 否 | Preferences实例的名称。 |
| dataGroupId | string|null | 否 | 是 | 
应用组ID，需要向应用市场获取，详见[dataGroupId申请流程](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ime-kit-security#section4219152220459)。基于dataGroupId的数据共享支持两种场景：1.同一应用的不同进程间共享，只支持三方应用中输入法和输入法的扩展场景使用；2.不同应用间的数据共享，只支持系统应用使用。

为可选参数。指定在此dataGroupId对应的沙箱路径下创建Preferences实例。当此参数不填时，默认在本应用沙箱目录下创建Preferences实例。

**模型约束：** 此属性仅在Stage模型下可用。

 |

#### Preferences

Preferences继承自[ISendable](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable#isendable)，可以在ArkTS并发实例间（包括主线程、TaskPool&Worker工作线程）传递，传递的行为是引用传递，提供获取和修改存储数据的接口。

下列接口都需先使用[sendablePreferences.getPreferences](#sendablepreferencesgetpreferences)获取到Preferences实例，再通过此实例调用对应接口。

#### \[h2\]get

get(key: string, defValue: lang.ISendable): Promise<lang.ISendable>

从缓存的Preferences实例中获取键对应的值，如果值为null或者非默认值类型，返回默认数据defValue，使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| key | string | 是 | 要获取的存储Key名称，不能为空，最大长度限制为[MAX\_KEY\_LENGTH](#常量)。 |
| defValue | [lang.ISendable](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable#isendable) | 是 | 默认返回值。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[lang.ISendable](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable#isendable)\> | 
Promise对象，返回键对应的值。

该实例继承[ISendable](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable#isendable)，可以在ArkTS并发实例间（包括主线程、TaskPool&Worker工作线程）传递，传递的行为是引用传递，参考[Sendable使用场景](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sendable-guide)。

 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[用户首选项错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-preferences)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { lang } from '@kit.ArkTS';

let promise = preferences.get('startup', 'default');
promise.then((data: lang.ISendable) => {
  let dataStr = data as string;
  console.info(`Succeeded in getting value of 'startup'. Data: ${dataStr}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get value of 'startup'. code: ${err.code}, message: ${err.message}`);
});
```

#### \[h2\]getSync

getSync(key: string, defValue: lang.ISendable): lang.ISendable

从缓存的Preferences实例中获取键对应的值，如果值为null或者非默认值类型，返回默认数据defValue，此为同步接口。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| key | string | 是 | 要获取的存储Key名称，不能为空，最大长度限制为[MAX\_KEY\_LENGTH](#常量)。 |
| defValue | [lang.ISendable](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable#isendable) | 是 | 默认返回值。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [lang.ISendable](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable#isendable) | 
返回键对应的值。

该实例继承[ISendable](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable#isendable)，可以在ArkTS并发实例间（包括主线程、TaskPool&Worker工作线程）传递，传递的行为是引用传递，参考[Sendable使用场景](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sendable-guide)。

 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[用户首选项错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-preferences)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```ts
import { lang } from '@kit.ArkTS';
let value: lang.ISendable = preferences.getSync('startup', 'default');
```

#### \[h2\]getAll

getAll(): Promise<lang.ISendable>

获取缓存的Preferences实例中的所有键值数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[lang.ISendable](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable#isendable)\> | 
Promise对象，返回所有包含的键值数据。

该对象继承[ISendable](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable#isendable)，可以在ArkTS并发实例间（包括主线程、TaskPool&Worker工作线程）传递，传递的行为是引用传递，参考[Sendable使用场景](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sendable-guide)。

 |

**错误码：**

以下错误码的详细介绍请参见[用户首选项错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-preferences)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 15500000 | Inner error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { lang } from '@kit.ArkTS';

let promise = preferences.getAll();
promise.then((keyValues: lang.ISendable) => {
  for (let value of Object.keys(keyValues)) {
    console.info("getAll " + JSON.stringify(value));
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to get all key-values. code: ${err.code}, message: ${err.message}`);
});
```

#### \[h2\]getAllSync

getAllSync(): lang.ISendable

获取缓存的Preferences实例中的所有键值数据，此为同步接口。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [lang.ISendable](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable#isendable) | 
返回所有包含的键值数据。

该对象继承[ISendable](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable#isendable)，可以在ArkTS并发实例间（包括主线程、TaskPool&Worker工作线程）传递，传递的行为是引用传递，参考[Sendable使用场景](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sendable-guide)。

 |

**错误码：**

以下错误码的详细介绍请参见[用户首选项错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-preferences)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 15500000 | Inner error. |

**示例：**

```ts
import { lang } from '@kit.ArkTS';

let keyValues: lang.ISendable = preferences.getAllSync();
for (let value of Object.keys(keyValues)) {
  console.info("getAll " + JSON.stringify(value));
}
```

#### \[h2\]put

put(key: string, value: lang.ISendable): Promise<void>

将数据写入缓存的Preferences实例中，可通过[flush](#flush)将Preferences实例持久化，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/tWr-LwdVRzSq37Efh7aXEg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014751Z&HW-CC-Expire=86400&HW-CC-Sign=5085C8F358C03B7992DCA2F0DF50EDBD9E6F7D645C1F0DADD9E80403790303C5)

当value中包含非UTF-8格式的字符串时，请使用Uint8Array类型存储，否则会造成持久化文件出现格式错误造成文件损坏。

当对应的键已经存在时，put()方法会覆盖其值。可以使用hasSync()方法检查是否存在对应键值对。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| key | string | 是 | 要修改的存储的Key，不能为空，最大长度限制为[MAX\_KEY\_LENGTH](#常量)。 |
| value | [lang.ISendable](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable#isendable) | 是 | 存储的新值。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[用户首选项错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-preferences)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let promise = preferences.put('startup', 'auto');
promise.then(() => {
  console.info("Succeeded in putting value of 'startup'.");
}).catch((err: BusinessError) => {
  console.error(`Failed to put value of 'startup'. code: ${err.code}, message: ${err.message}`);
});
```

#### \[h2\]putSync

putSync(key: string, value: lang.ISendable): void

将数据写入缓存的Preferences实例中，可通过[flush](#flush)将Preferences实例持久化，此为同步接口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/YRy_DzJZTaS5q7FhCF_WpQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014751Z&HW-CC-Expire=86400&HW-CC-Sign=0D5AAE38AC2B2F19F7F3FE023DD9A0BE1B0437616C24581D15CBB32BE581C664)

当value中包含非UTF-8格式的字符串时，请使用Uint8Array类型存储，否则会造成持久化文件出现格式错误造成文件损坏。

当对应的键已经存在时，putSync()方法会覆盖其值。可以使用hasSync()方法检查是否存在对应键值对。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| key | string | 是 | 要修改的存储的Key，不能为空，最大长度限制为[MAX\_KEY\_LENGTH](#常量)。 |
| value | [lang.ISendable](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable#isendable) | 是 | 存储的新值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[用户首选项错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-preferences)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```ts
preferences.putSync('startup', 'auto');
```

#### \[h2\]has

has(key: string): Promise<boolean>

检查缓存的Preferences实例中是否包含名为给定Key的存储键值对，使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| key | string | 是 | 要检查的存储key名称，不能为空，最大长度限制为[MAX\_KEY\_LENGTH](#常量)。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象。返回Preferences实例是否包含给定key的存储键值对，true表示存在，false表示不存在。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[用户首选项错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-preferences)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let promise = preferences.has('startup');
promise.then((val: boolean) => {
  if (val) {
    console.info("The key 'startup' is contained.");
  } else {
    console.error("The key 'startup' does not contain.");
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to check the key 'startup'. code: ${err.code}, message: ${err.message}`);
});
```

#### \[h2\]hasSync

hasSync(key: string): boolean

检查缓存的Preferences实例中是否包含名为给定Key的存储键值对，此为同步接口。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| key | string | 是 | 要检查的存储key名称，不能为空，最大长度限制为[MAX\_KEY\_LENGTH](#常量)。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 返回Preferences实例是否包含给定key的存储键值对，true表示存在，false表示不存在。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[用户首选项错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-preferences)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```ts
let isExist: boolean = preferences.hasSync('startup');
if (isExist) {
  console.info("The key 'startup' is contained.");
} else {
  console.error("The key 'startup' does not contain.");
}
```

#### \[h2\]delete

delete(key: string): Promise<void>

从缓存的Preferences实例中删除名为给定Key的存储键值对，可通过[flush](#flush)将Preferences实例持久化，使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| key | string | 是 | 要删除的存储key名称，不能为空，最大长度限制为[MAX\_KEY\_LENGTH](#常量)。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[用户首选项错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-preferences)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let promise = preferences.delete('startup');
promise.then(() => {
  console.info("Succeeded in deleting the key 'startup'.");
}).catch((err: BusinessError) => {
  console.error(`Failed to delete the key 'startup'. code: ${err.code}, message: ${err.message}`);
});
```

#### \[h2\]deleteSync

deleteSync(key: string): void

从缓存的Preferences实例中删除名为给定Key的存储键值对，可通过[flush](#flush)将Preferences实例持久化，此为同步接口。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| key | string | 是 | 要删除的存储key名称，不能为空，最大长度限制为[MAX\_KEY\_LENGTH](#常量)。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[用户首选项错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-preferences)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```ts
preferences.deleteSync('startup');
```

#### \[h2\]flush

flush(): Promise<void>

将缓存的Preferences实例中的数据异步存储到共享用户首选项的持久化文件中，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/cyLI-l2jQDaJPBd6arx-Uw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014751Z&HW-CC-Expire=86400&HW-CC-Sign=682EF14123E25E53299E7239077B7C77679355A8840BD90114EFD7CFCE82CECB)

当数据未修改或修改后的数据与缓存数据一致时，不会刷新持久化文件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[用户首选项错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-preferences)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 15500000 | Inner error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let promise = preferences.flush();
promise.then(() => {
  console.info("Succeeded in flushing.");
}).catch((err: BusinessError) => {
  console.error(`Failed to flush. code: ${err.code}, message: ${err.message}`);
});
```

#### \[h2\]flushSync14+

flushSync(): void

将缓存的Preferences实例中的数据存储到共享用户首选项的持久化文件中。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/hBc20IG7TUy01oeARc6z1w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014751Z&HW-CC-Expire=86400&HW-CC-Sign=3C603DC10958CA3E7BAF63278DE84487D6BD0AE47C203A931DFC37DA5E741BD9)

当数据未修改或修改后的数据与缓存数据一致时，不会刷新持久化文件。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**错误码：**

以下错误码的详细介绍请参见[用户首选项错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-preferences)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 15500000 | Inner error. |

**示例：**

```ts
preferences.flushSync();
```

#### \[h2\]clear

clear(): Promise<void>

清除缓存的Preferences实例中的所有数据，可通过[flush](#flush)将Preferences实例持久化，使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[用户首选项错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-preferences)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 15500000 | Inner error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let promise = preferences.clear();
promise.then(() => {
  console.info("Succeeded in clearing.");
}).catch((err: BusinessError) => {
  console.error(`Failed to clear. code: ${err.code}, message: ${err.message}`);
});
```

#### \[h2\]clearSync

clearSync(): void

清除缓存的Preferences实例中的所有数据，可通过[flush](#flush)将Preferences实例持久化，此为同步接口。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**错误码：**

以下错误码的详细介绍请参见[用户首选项错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-preferences)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 15500000 | Inner error. |

**示例：**

```ts
preferences.clearSync();
```

#### \[h2\]on('change')

on(type: 'change', callback: Callback<string>): void

订阅数据变更，订阅的Key的值发生变更后，在执行[flush](#flush)方法后，触发callback回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/2FO0Pxd8TfiR54M2YtDUkA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014751Z&HW-CC-Expire=86400&HW-CC-Sign=455C5B6C79C4FE76EF52D5C29F338C41E24B7CFE56ABC67578557ECAE512EEF4)

当调用[removePreferencesFromCache](#sendablepreferencesremovepreferencesfromcache)或者[deletePreferences](#sendablepreferencesdeletepreferences)后，订阅的数据变更会主动取消订阅，在重新[getPreferences](#sendablepreferencesgetpreferences)后需要重新订阅数据变更。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 事件类型，固定值'change'，表示数据变更。 |
| callback | Callback<string> | 是 | 回调函数。返回发生变更的Key。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[用户首选项错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-preferences)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let observer = (key: string) => {
  console.info("The key " + key + " changed.");
};
preferences.on('change', observer);
preferences.putSync('startup', 'manual');
preferences.flush().then(() => {
  console.info("Succeeded in flushing.");
}).catch((err: BusinessError) => {
  console.error(`Failed to flush. code: ${err.code}, message: ${err.message}`);
});
```

#### \[h2\]on('multiProcessChange')

on(type: 'multiProcessChange', callback: Callback<string>): void

订阅进程间数据变更，多个进程持有同一个首选项文件时，在任意一个进程（包括本进程）执行[flush](#flush)方法，持久化文件发生变更后，触发callback回调。

本接口提供给申请了[dataGroupId](#options)的应用进行使用，未申请的应用不推荐使用，多进程操作可能会损坏持久化文件，导致数据丢失。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/9pFXTg8JQqyT9LFy4UxwDg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014751Z&HW-CC-Expire=86400&HW-CC-Sign=245CFD11997C58E80CE2A558CD57F29F37034172F96C295A4A00A25FCE3CD556)

同一持久化文件在当前进程订阅进程间数据变更的最大数量为50次，超过最大限制后会订阅失败。建议在触发callback回调后及时取消订阅。

当调用[removePreferencesFromCache](#sendablepreferencesremovepreferencesfromcache)或者[deletePreferences](#sendablepreferencesdeletepreferences)后，订阅的数据变更会主动取消订阅，在重新[getPreferences](#sendablepreferencesgetpreferences)后需要重新订阅数据变更。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 事件类型，固定值'multiProcessChange'，表示多进程间的数据变更。 |
| callback | Callback<string> | 是 | 回调函数。返回发生变更的Key。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[用户首选项错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-preferences)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |
| 15500019 | Failed to obtain the subscription service. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let observer = (key: string) => {
  console.info("The key " + key + " changed.");
};
preferences.on('multiProcessChange', observer);
preferences.putSync('startup', 'manual');
preferences.flush().then(() => {
  console.info("Succeeded in flushing.");
}).catch((err: BusinessError) => {
  console.error(`Failed to flush. code: ${err.code}, message: ${err.message}`);
});
```

#### \[h2\]on('dataChange')

on(type: 'dataChange', keys: Array<string>, callback: Callback<lang.ISendable>): void

精确订阅数据变更，只有被订阅的key值发生变更后，在执行[flush](#flush)方法后，触发callback回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/b_q1dBbpRrKe6F8jwt5kWQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014751Z&HW-CC-Expire=86400&HW-CC-Sign=66BE6E857CA3AE4A56EAD7D3A666F27E029D1CB7811A213AA05E73128B20BB39)

当调用[removePreferencesFromCache](#sendablepreferencesremovepreferencesfromcache)或者[deletePreferences](#sendablepreferencesdeletepreferences)后，订阅的数据变更会主动取消订阅，在重新[getPreferences](#sendablepreferencesgetpreferences)后需要重新订阅数据变更。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 事件类型，固定值'dataChange'，表示精确的数据变更。 |
| keys | Array<string> | 是 | 需要订阅的key集合。 |
| callback | Callback<[lang.ISendable](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable#isendable)\> | 是 | 回调函数。回调支持返回多个键值对，其中键为发生变更的订阅key，值为变更后的数据：支持number、string、boolean、bigint以及可序列化的object。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[用户首选项错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-preferences)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { lang } from '@kit.ArkTS';

let observer = (data: lang.ISendable) => {
  console.info(`observer : ${data}`);
};
let keys = ['name', 'age'];
preferences.on('dataChange', keys, observer);
preferences.putSync('name', 'xiaohong');
preferences.putSync('weight', 125);
preferences.flush().then(() => {
  console.info("Succeeded in flushing.");
}).catch((err: BusinessError) => {
  console.error(`Failed to flush. code: ${err.code}, message: ${err.message}`);
});
```

#### \[h2\]off('change')

off(type: 'change', callback?: Callback<string>): void

取消订阅数据变更。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 事件类型，固定值'change'，表示数据变更。 |
| callback | Callback<string> | 否 | 需要取消的回调函数，不填写则全部取消。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[用户首选项错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-preferences)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let observer = (key: string) => {
  console.info("The key " + key + " changed.");
};
preferences.on('change', observer);
preferences.putSync('startup', 'auto');
preferences.flush().then(() => {
  console.info("Succeeded in flushing.");
  preferences.off('change', observer);
}).catch((err: BusinessError) => {
  console.error(`Failed to flush. code: ${err.code}, message: ${err.message}`);
});
```

#### \[h2\]off('multiProcessChange')

off(type: 'multiProcessChange', callback?: Callback<string>): void

取消订阅进程间数据变更。

本接口提供给申请了[dataGroupId](#options)的应用进行使用，未申请的应用不推荐使用，多进程操作可能会损坏持久化文件，导致数据丢失。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 事件类型，固定值'multiProcessChange'，表示多进程间的数据变更。 |
| callback | Callback<string> | 否 | 需要取消的回调函数，不填写则全部取消。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[用户首选项错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-preferences)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let observer = (key: string) => {
  console.info("The key " + key + " changed.");
};
preferences.on('multiProcessChange', observer);
preferences.putSync('startup', 'auto');
preferences.flush().then(() => {
  console.info("Succeeded in flushing.");
  preferences.off('multiProcessChange', observer);
}).catch((err: BusinessError) => {
  console.error(`Failed to flush. code: ${err.code}, message: ${err.message}`);
});
```

#### \[h2\]off('dataChange')

off(type: 'dataChange', keys: Array<string>, callback?: Callback<lang.ISendable>): void

取消精确订阅数据变更。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 事件类型，固定值'dataChange'，表示精确的数据变更。 |
| keys | Array<string> | 是 | 需要取消订阅的key集合，当keys为空数组时，表示取消订阅全部key；当keys为非空数组时，表示只取消订阅key集合中的key。 |
| callback | Callback<[lang.ISendable](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable#isendable)\> | 否 | 需要取消的回调函数，若callback不填写，表示所有的callback都需要处理；若callback填写，表示只处理该callback。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[用户首选项错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-preferences)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { lang } from '@kit.ArkTS';

let observer = (data: lang.ISendable) => {
  console.info(`observer : ${data}`);
};
let keys = ['name', 'age'];
preferences.on('dataChange', keys, observer);
preferences.putSync('name', 'xiaohong');
preferences.putSync('weight', 125);
preferences.flush().then(() => {
  console.info("Succeeded in flushing.");
  preferences.off('dataChange', keys, observer);
}).catch((err: BusinessError) => {
  console.error(`Failed to flush. code: ${err.code}, message: ${err.message}`);
});
```

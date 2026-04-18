---
title: "@ohos.bundle (Bundle模块)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "已停止维护的接口"
  - "@ohos.bundle (Bundle模块)"
captured_at: "2026-04-17T01:47:48.300Z"
---

# @ohos.bundle (Bundle模块)

本模块提供应用信息查询能力，支持[包信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-bundleinfo)、[应用信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-applicationinfo)、[Ability组件信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-abilityinfo)等信息的查询，以及应用禁用状态的查询、设置等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/OS_z7vKsRnSdyveGr9Ha1g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=93E64CB3F8E9F121B580FCAC642D04C7C5EF5674E25697159A8662D5F2361D47)

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API version 9开始，该模块不再维护，建议使用[@ohos.bundle.bundleManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager)替代。

#### 导入模块

```ts
import bundle from '@ohos.bundle';
```

#### 权限列表

| 权限 | 权限等级 | 描述 |
| :-- | :-- | :-- |
| ohos.permission.GET\_BUNDLE\_INFO | normal | 查询指定应用信息。 |
| ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED | system\_basic | 可查询所有应用信息。 |

权限等级参考[权限APL等级说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-permission-mgmt-overview#权限机制中的基本概念)。

#### bundle.getApplicationInfodeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/loL1QQCBSi282n4qRb280w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=5B68F339A2F3983BEE863A57C5CC5079C45EB924825FC757AEC9F48E5A7E5330)

从API version 7开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

getApplicationInfo(bundleName: string, bundleFlags: number, userId?: number): Promise<ApplicationInfo>

根据给定的Bundle名称获取ApplicationInfo。使用Promise异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED 或 ohos.permission.GET\_BUNDLE\_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| bundleName | string | 是 | 要查询的应用Bundle名称。 |
| bundleFlags | number | 是 | 用于指定返回的应用信息对象中包含信息的标记。取值范围请参考[BundleFlag说明](#bundleflagdeprecated)中应用信息相关flag。 |
| userId | number | 否 | 用户ID。默认值：调用方所在用户，取值范围：大于等于0。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[ApplicationInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-applicationinfo)\> | Promise形式返回应用程序信息。 |

**示例：**

```ts
import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let bundleName: string = "com.example.myapplication";
let bundleFlags: number = 0;
let userId: number = 100;

bundle.getApplicationInfo(bundleName, bundleFlags, userId)
  .then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })
```

#### bundle.getApplicationInfodeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/zby0WsZwQt2hf6IGu2XDmw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=58C0079CCB5FEF914B3210CBF8974A339FFE623B07EB56EEDECA26AC4F5899CE)

从API version 7开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

getApplicationInfo(bundleName: string, bundleFlags: number, userId: number, callback: AsyncCallback<ApplicationInfo>): void

根据给定的Bundle名称获取指定用户下的ApplicationInfo，使用callback异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED 或 ohos.permission.GET\_BUNDLE\_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| bundleName | string | 是 | 要查询的应用Bundle名称。 |
| bundleFlags | number | 是 | 用于指定返回的应用信息对象中包含信息的标记。取值范围：参考[BundleFlag说明](#bundleflagdeprecated)中应用信息相关flag。 |
| userId | number | 是 | 用户ID。取值范围：大于等于0。 |
| callback | AsyncCallback<[ApplicationInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-applicationinfo)\> | 是 | 程序启动作为入参的回调函数，返回应用程序信息。 |

**示例：**

```ts
import bundle from '@ohos.bundle';

let bundleName: string = "com.example.myapplication";
let bundleFlags: number = 0;
let userId: number = 100;

bundle.getApplicationInfo(bundleName, bundleFlags, userId, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})
```

#### bundle.getApplicationInfodeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/B4i4ixU7Ta6o-FHG2Bw9wQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=B9F8A6BD4D9F226CDAD6069362D0483D493EAA9379CBA6D626DB2C9ED5A70F3D)

从API version 7开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

getApplicationInfo(bundleName: string, bundleFlags: number, callback: AsyncCallback<ApplicationInfo>): void

根据给定的Bundle名称获取ApplicationInfo，使用callback异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED 或 ohos.permission.GET\_BUNDLE\_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| bundleName | string | 是 | 要查询的应用Bundle名称。 |
| bundleFlags | number | 是 | 用于指定返回的应用信息对象中包含信息的标记。取值范围：参考[BundleFlag说明](#bundleflagdeprecated)中应用信息相关flag。 |
| callback | AsyncCallback<[ApplicationInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-applicationinfo)\> | 是 | 程序启动作为入参的回调函数，返回应用程序信息。 |

**示例：**

```ts
import bundle from '@ohos.bundle';

let bundleName: string = "com.example.myapplication";
let bundleFlags: number = 0;

bundle.getApplicationInfo(bundleName, bundleFlags, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})
```

#### bundle.getAllBundleInfodeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/dN6ftEqkSV-L6WhT78Zi-g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=3D97875A560D33C7037B8916C40708CFF1EBF46F681188AF4263280D1F35230F)

从API version 7开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

getAllBundleInfo(bundleFlag: BundleFlag, userId?: number): Promise<Array<BundleInfo>>

获取指定用户所有的BundleInfo，使用Promise形式异步回调。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| bundleFlag | BundleFlag | 是 | 用于指定返回的包信息对象中包含信息的标记。取值范围：参考[BundleFlag说明](#bundleflagdeprecated)中包信息相关flag。 |
| userId | number | 否 | 用户ID。默认值：调用方所在用户，取值范围：大于等于0。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<[BundleInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-bundleinfo)\>> | Promise形式返回所有可用的BundleInfo |

**示例：**

```ts
import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let bundleFlag: number = 0;
let userId: number = 100;

bundle.getAllBundleInfo(bundleFlag, userId)
  .then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })
```

#### bundle.getAllBundleInfodeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/M4bk9R0zRCyVXA6lRZS2NQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=2B4AC9836F5CB8A9B4453CC1909F09CE5677D2C3AFA5D1EEFCE52708F448E906)

从API version 7开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

getAllBundleInfo(bundleFlag: BundleFlag, callback: AsyncCallback<Array<BundleInfo>>): void

获取当前用户所有的BundleInfo，使用callback异步回调。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| bundleFlag | BundleFlag | 是 | 用于指定返回的应用信息对象中包含信息的标记。取值范围：参考[BundleFlag说明](#bundleflagdeprecated)中包信息相关flag。 |
| callback | AsyncCallback<Array<[BundleInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-bundleinfo)\>> | 是 | 程序启动作为入参的回调函数，返回所有可用的BundleInfo。 |

**示例：**

```ts
import bundle from '@ohos.bundle';

let bundleFlag: number = 0;

bundle.getAllBundleInfo(bundleFlag, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})
```

#### bundle.getAllBundleInfodeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/5h6hofV8QXKlT1BVT4qSGA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=39B351AF0981EACA80ECF4F3BBBD2776F5E3B94BCC4B6A654478921748252A36)

从API version 7开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

getAllBundleInfo(bundleFlag: BundleFlag, userId: number, callback: AsyncCallback<Array<BundleInfo>>): void

获取系统中指定用户下所有的BundleInfo，使用callback异步回调。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| bundleFlag | BundleFlag | 是 | 用于指定返回的应用信息对象中包含信息的标记。取值范围：参考[BundleFlag说明](#bundleflagdeprecated)中包信息相关flag。 |
| userId | number | 是 | 用户ID。默认值：调用方所在用户，取值范围：大于等于0。 |
| callback | AsyncCallback<Array<[BundleInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-bundleinfo)\>> | 是 | 程序启动作为入参的回调函数，返回指定用户下所有包的BundleInfo。 |

**示例：**

```ts
import bundle from '@ohos.bundle';

let bundleFlag: number = 0;
let userId: number = 100;

bundle.getAllBundleInfo(bundleFlag, userId, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})
```

#### bundle.getBundleInfodeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/e6vxs5TRTqWHFK774DDtAA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=C55A35C4150D0D824FBAD74B6A3E6BE9B66203E0BCC2F18CDEF3BE16BAB4DD3D)

从API version 7开始支持，从API version 9开始废弃，建议使用[getBundleInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager#bundlemanagergetbundleinfo14-2)替代。

getBundleInfo(bundleName: string, bundleFlags: number, options?: BundleOptions): Promise<BundleInfo>

根据给定的Bundle名称获取BundleInfo，使用Promise异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED 或 ohos.permission.GET\_BUNDLE\_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| bundleName | string | 是 | 要查询的应用Bundle名称。 |
| bundleFlags | number | 是 | 用于指定返回的应用信息对象中包含信息的标记。取值范围：参考[BundleFlag说明](#bundleflagdeprecated)中包信息相关flag。 |
| options | [BundleOptions](#bundleoptionsdeprecated) | 否 | 包含userid的查询选项。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[BundleInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-bundleinfo)\> | Promise对象，获取成功时返回包信息。 |

**示例：**

```ts
import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let bundleName: string = "com.example.myapplication";
let bundleFlags: number = 1;
let options: bundle.BundleOptions = {
  "userId": 100
};

bundle.getBundleInfo(bundleName, bundleFlags, options)
  .then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })
```

#### bundle.getBundleInfodeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/pxbd3Dl7T1m9osd9KdBIiQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=B5DD234145BD78DD11D5C8C32350EDAB795BAF9E8FABA88F8A3D4BAF1EA9EFCE)

从API version 7开始支持，从API version 9开始废弃，建议使用[getBundleInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager#bundlemanagergetbundleinfo14-1)替代。

getBundleInfo(bundleName: string, bundleFlags: number, callback: AsyncCallback<BundleInfo>): void

根据给定的Bundle名称获取BundleInfo，使用callback异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED 或 ohos.permission.GET\_BUNDLE\_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| bundleName | string | 是 | 需要查询的应用Bundle名称。 |
| bundleFlags | number | 是 | 用于指定返回的应用信息对象中包含信息的标记。取值范围：参考[BundleFlag说明](#bundleflagdeprecated)中包信息相关flag。 |
| callback | AsyncCallback<[BundleInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-bundleinfo)\> | 是 | 程序启动作为入参的回调函数，返回包信息。 |

**示例：**

```ts
import bundle from '@ohos.bundle';

let bundleName: string = "com.example.myapplication";
let bundleFlags: number = 1;

bundle.getBundleInfo(bundleName, bundleFlags, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})
```

#### bundle.getBundleInfodeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/ZbdL1ct0TOiiYOvV9lXuqA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=DE9334FB1378F7C6640333E9B4E18194ECD0C83343EB719E6EC80EF98F2700F8)

从API version 7开始支持，从API version 9开始废弃，建议使用[getBundleInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager#bundlemanagergetbundleinfo14)替代。

getBundleInfo(bundleName: string, bundleFlags: number, options: BundleOptions, callback: AsyncCallback<BundleInfo>): void

根据给定的Bundle名称获取BundleInfo，使用callback异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED 或 ohos.permission.GET\_BUNDLE\_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| bundleName | string | 是 | 要查询的应用Bundle名称。 |
| bundleFlags | number | 是 | 用于指定返回的应用信息对象中包含信息的标记。取值范围：参考[BundleFlag说明](#bundleflagdeprecated)中包信息相关flag。 |
| options | [BundleOptions](#bundleoptionsdeprecated) | 是 | 包含userid。 |
| callback | AsyncCallback<[BundleInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-bundleinfo)\> | 是 | 程序启动作为入参的回调函数，返回包信息。 |

**示例：**

```ts
import bundle from '@ohos.bundle';

let bundleName: string = "com.example.myapplication";
let bundleFlags: number = 1;
let options: bundle.BundleOptions = {
  "userId": 100
};

bundle.getBundleInfo(bundleName, bundleFlags, options, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})
```

#### bundle.getAllApplicationInfodeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/UMoZDAzERLKWNyOnrylOiw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=46D8C960E6BB00FF55CABF735A5D45E09872481F3D05EA20B63FEB20F9FF108A)

从API version 7开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

getAllApplicationInfo(bundleFlags: number, userId?: number): Promise<Array<ApplicationInfo>>

获取指定用户下所有已安装的应用信息，使用promise异步回调。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| bundleFlags | number | 是 | 用于指定返回的应用信息对象中包含信息的标记。取值范围：参考[BundleFlag说明](#bundleflagdeprecated)中应用信息相关flag。 |
| userId | number | 否 | 用户ID。默认值：调用方所在用户，取值范围：大于等于0。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<[ApplicationInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-applicationinfo)\>> | Promise对象，获取成功时返回应用信息列表。 |

**示例：**

```ts
import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let bundleFlags: number = 8;
let userId: number = 100;

bundle.getAllApplicationInfo(bundleFlags, userId)
  .then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })
```

#### bundle.getAllApplicationInfodeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/ktR65ux8Q7WUNsGT6kPe4w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=77EAEE05E55650F568A95BDD934027D58E9F1C812A36D542293CEAD253316F8E)

从API version 7开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

getAllApplicationInfo(bundleFlags: number, userId: number, callback: AsyncCallback<Array<ApplicationInfo>>): void

获取指定用户下所有已安装的应用信息，使用callback异步回调。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| bundleFlags | number | 是 | 用于指定返回的应用信息对象中包含信息的标记。取值范围：参考[BundleFlag说明](#bundleflagdeprecated)中应用信息相关flag。 |
| userId | number | 是 | 用户ID。默认值：调用方所在用户，取值范围：大于等于0。 |
| callback | AsyncCallback<Array<[ApplicationInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-applicationinfo)\>> | 是 | 程序启动作为入参的回调函数，返回应用信息列表。 |

**示例：**

```ts
import bundle from '@ohos.bundle';

let bundleFlags: number = bundle.BundleFlag.GET_APPLICATION_INFO_WITH_PERMISSION;
let userId: number = 100;

bundle.getAllApplicationInfo(bundleFlags, userId, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})
```

#### bundle.getAllApplicationInfodeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/S18Wz3MZR2Ci2-EO-QGEtA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=2E2184C62C1FF8702C0D6CC90A5C065944FC8B0FFA362B5BD7227BF7FBA85ABB)

从API version 7开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

getAllApplicationInfo(bundleFlags: number, callback: AsyncCallback<Array<ApplicationInfo>>): void

获取调用方所在用户下已安装的应用信息，使用callback异步回调。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| bundleFlags | number | 是 | 用于指定返回的应用信息对象中包含信息的标记。取值范围：参考[BundleFlag说明](#bundleflagdeprecated)中应用信息相关flag。 |
| callback | AsyncCallback<Array<[ApplicationInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-applicationinfo)\>> | 是 | 程序启动作为入参的回调函数，返回应用信息列表。 |

**示例：**

```ts
import bundle from '@ohos.bundle';

let bundleFlags: number = bundle.BundleFlag.GET_APPLICATION_INFO_WITH_PERMISSION;

bundle.getAllApplicationInfo(bundleFlags, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})
```

#### bundle.getBundleArchiveInfodeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/aAYwRPNjTSChWZaXp8i6jw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=34E62D3EDBEA93689E4E325C67D3EFE84D13FBCE0B039FC69F60D2E794CCFBD7)

从API version 7开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

getBundleArchiveInfo(hapFilePath: string, bundleFlags: number) : Promise<BundleInfo>

获取有关HAP中包含的应用程序包的信息，使用Promise异步回调。

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| hapFilePath | string | 是 | HAP存放路径。支持当前应用程序的绝对路径和数据目录沙箱路径。 |
| bundleFlags | number | 是 | 用于指定要返回的BundleInfo对象中包含信息的标记。取值范围：参考[BundleFlag说明](#bundleflagdeprecated)中包信息相关flag。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[BundleInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-bundleinfo)\> | 返回值为Promise对象，Promise中包含有关HAP中包含的应用程序的信息。 |

**示例：**

```ts
import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let hapFilePath: string = "/data/storage/el2/base/test.hap";
let bundleFlags: number = 0;

bundle.getBundleArchiveInfo(hapFilePath, bundleFlags)
  .then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })
```

#### bundle.getBundleArchiveInfodeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/P8P-LwIOQ7aKpxCHRHIFcA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=8AE090123E29ADE8F0B3DEAE83D5DBAD305BB00D946FF372023270E11B00BB61)

从API version 7开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

getBundleArchiveInfo(hapFilePath: string, bundleFlags: number, callback: AsyncCallback<BundleInfo>) : void

获取有关HAP中包含的应用程序包的信息，使用callback异步回调。

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| hapFilePath | string | 是 | HAP存放路径，支持当前应用程序的绝对路径和数据目录沙箱路径。 |
| bundleFlags | number | 是 | 用于指定要返回的BundleInfo对象中包含信息的标记。取值范围：参考[BundleFlag说明](#bundleflagdeprecated)中包信息相关flag。 |
| callback | AsyncCallback<[BundleInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-bundleinfo)\> | 是 | 程序启动作为入参的回调函数，返回HAP中包含的应用程序包的信息。 |

**示例：**

```ts
import bundle from '@ohos.bundle';

let hapFilePath: string = "/data/storage/el2/base/test.hap";
let bundleFlags: number = 0;

bundle.getBundleArchiveInfo(hapFilePath, bundleFlags, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})
```

#### bundle.getAbilityInfodeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/WTBI4RBGTIGLDbJQRlSabw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=C17C32A5ECEE6483AC0BE5F9B7145D78EBCD03675DC45345C63891C2199EEAD9)

从API version 7开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

getAbilityInfo(bundleName: string, abilityName: string): Promise<AbilityInfo>

通过Bundle名称和组件名获取Ability组件信息，使用Promise形式异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED 或 ohos.permission.GET\_BUNDLE\_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| bundleName | string | 是 | 应用Bundle名称。 |
| abilityName | string | 是 | Ability组件名称。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[AbilityInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-abilityinfo)\> | Promise形式返回Ability信息。 |

**示例：**

```ts
import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let bundleName: string = "com.example.myapplication";
let abilityName: string = "EntryAbility";

bundle.getAbilityInfo(bundleName, abilityName)
  .then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })
```

#### bundle.getAbilityInfodeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/NcHAm1moT32cXSEG5qMG8w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=E4495EC0041A37E4766C809123C2B95A30AA9839906076C35616E09A0CD0BE27)

从API version 7开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

getAbilityInfo(bundleName: string, abilityName: string, callback: AsyncCallback<AbilityInfo>): void

通过Bundle名称和组件名获取Ability组件信息，使用callback异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED 或 ohos.permission.GET\_BUNDLE\_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| bundleName | string | 是 | 应用Bundle名称。 |
| abilityName | string | 是 | Ability名称。 |
| callback | AsyncCallback<[AbilityInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-abilityinfo)\> | 是 | 程序启动作为入参的回调函数，返回Ability信息。 |

**示例：**

```ts
import bundle from '@ohos.bundle';

let bundleName: string = "com.example.myapplication";
let abilityName: string = "EntryAbility";

bundle.getAbilityInfo(bundleName, abilityName, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})
```

#### bundle.getAbilityLabel8+ deprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/Xyf3srhbSyqppVjuP1F_wA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=8DFB1A91EC9B8F1D4C561BCC5681D73CD3AD09FE74885DC524D5D9021A693D30)

从API version 8开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

getAbilityLabel(bundleName: string, abilityName: string): Promise<string>

通过Bundle名称和ability名称获取应用名称，使用Promise异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED 或 ohos.permission.GET\_BUNDLE\_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| bundleName | string | 是 | 应用Bundle名称。 |
| abilityName | string | 是 | Ability名称。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | Promise形式返回应用名称信息。 |

**示例：**

```ts
import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let bundleName: string = "com.example.myapplication";
let abilityName: string = "EntryAbility";

bundle.getAbilityLabel(bundleName, abilityName)
  .then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })
```

#### bundle.getAbilityLabel8+ deprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/1qYE5KALQyymlHV2JdTJkg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=94B2937561EA1907E9C604756CFFE3C9C1CDBB7D16125C93E22555C1A5E0F4DB)

从API version 8开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

getAbilityLabel(bundleName: string, abilityName: string, callback : AsyncCallback<string>): void

通过Bundle名称和Ability组件名获取应用名称，使用callback异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED 或 ohos.permission.GET\_BUNDLE\_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| bundleName | string | 是 | 应用Bundle名称。 |
| abilityName | string | 是 | Ability名称。 |
| callback | AsyncCallback<string> | 是 | 程序启动作为入参的回调函数，返回应用名称信息。 |

**示例：**

```ts
import bundle from '@ohos.bundle';

let bundleName: string = "com.example.myapplication";
let abilityName: string = "EntryAbility";

bundle.getAbilityLabel(bundleName, abilityName, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})
```

#### bundle.isAbilityEnabled8+ deprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/Asy4f7s-TL-8clL-yYo17Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=A82EE83CC2735BEE3665A197831A7801F37CB373A120065F4055B1A25FD9644D)

从API version 8开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

isAbilityEnabled(info: AbilityInfo): Promise<boolean>

根据给定的AbilityInfo查询ability是否已经启用，使用Promise异步回调。

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| info | [AbilityInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-abilityinfo) | 是 | Ability的配置信息。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise形式返回boolean代表是否启用。 |

**示例：**

```ts
import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let bundleName: string = "com.example.myapplication";
let abilityName: string = "EntryAbility";

bundle.getAbilityInfo(bundleName, abilityName).then((abilityInfo) => {
  bundle.isAbilityEnabled(abilityInfo).then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })
})
```

#### bundle.isAbilityEnabled8+ deprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/HUF4_LDdRdWVmlOdPhpDTw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=910B147F34AAAD24A2B9FF6DF3DEDBC0ED91DA968A28979F2873294F420A2050)

从API version 8开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

isAbilityEnabled(info : AbilityInfo, callback : AsyncCallback<boolean>): void

根据给定的AbilityInfo查询ability是否已经启用，使用callback异步回调。

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| info | [AbilityInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-abilityinfo) | 是 | Ability的配置信息。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数，返回boolean代表是否启用。 |

**示例：**

```ts
import bundle from '@ohos.bundle';

let bundleName: string = "com.example.myapplication";
let abilityName: string = "EntryAbility";

bundle.getAbilityInfo(bundleName, abilityName).then((abilityInfo) => {
  bundle.isAbilityEnabled(abilityInfo, (err, data) => {
    if (err) {
      console.error('Operation failed. Cause: ' + JSON.stringify(err));
      return;
    }
    console.info('Operation successful. Data:' + JSON.stringify(data));
  })
})
```

#### bundle.isApplicationEnabled8+ deprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/z3Es7h3sQ0uLyyTXGJdkLw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=B004243D7A7A6E415A494FEC63C0B62586B4F98B867E192F3082EE586A5A114A)

从API version 8开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

isApplicationEnabled(bundleName: string): Promise<boolean>

根据给定的bundleName查询指定应用程序是否已经启用，使用Promise异步回调。

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| bundleName | string | 是 | 要查询的应用Bundle名称。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise形式返回boolean代表是否启用。 |

**示例：**

```ts
import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let bundleName: string = "com.example.myapplication";

bundle.isApplicationEnabled(bundleName)
  .then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })
```

#### bundle.isApplicationEnabled8+ deprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/vPN6Bh07Sy6QOSR63aKHtQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=B7C7A25560863B44B3A014C25A84BFC94CFB52E34036877785C6E165F9C867B8)

从API version 8开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

isApplicationEnabled(bundleName: string, callback : AsyncCallback<boolean>): void

根据给定的bundleName查询指定应用程序是否已经启用，使用callback异步回调。

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| bundleName | string | 是 | 要查询的应用Bundle名称。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数，返回boolean代表是否启用。 |

**示例：**

```ts
import bundle from '@ohos.bundle';

let bundleName: string = "com.example.myapplication";

bundle.isApplicationEnabled(bundleName, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})
```

#### bundle.queryAbilityByWantdeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/8TfmGNdhTR62ztpwqpfbzQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=A1CA0FE109D875A086A495B7A021ABC63B87FCDA7C3FD47FE70BC10A6EDDC569)

从API version 7开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

queryAbilityByWant(want: Want, bundleFlags: number, userId?: number): Promise<Array<AbilityInfo>>

根据给定的意图获取Ability组件信息，使用Promise异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED 或 ohos.permission.GET\_BUNDLE\_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| want | [Want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-want) | 是 | 包含要查询的应用Bundle名称的意图。 |
| bundleFlags | number | 是 | 用于指定返回abilityInfo信息。取值范围：参考[BundleFlag说明](#bundleflagdeprecated)中Ability信息相关flag。 |
| userId | number | 否 | 用户ID。默认值：调用方所在用户，取值范围：大于等于0。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<[AbilityInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-abilityinfo)\>> | Promise形式返回Ability信息。 |

**示例：**

```ts
import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';
import Want from '@ohos.app.ability.Want';

let bundleFlags: number = 0;
let userId: number = 100;
let want: Want = {
  bundleName: "com.example.myapplication",
  abilityName: "EntryAbility"
};

bundle.queryAbilityByWant(want, bundleFlags, userId)
  .then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })
```

#### bundle.queryAbilityByWantdeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/Mqy4Ei73R4iBa6P6HuR3OQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=087BA33D35246D2F67D91D3C1A0E9F9C113395A08DDAFA46FEF1A1ABD59B24D3)

从API version 7开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

queryAbilityByWant(want: Want, bundleFlags: number, userId: number, callback: AsyncCallback<Array<AbilityInfo>>): void

根据给定的意图获取指定用户下Ability信息，使用callback异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED 或 ohos.permission.GET\_BUNDLE\_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| want | [Want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-want) | 是 | 指示包含要查询的应用Bundle名称的意图。 |
| bundleFlags | number | 是 | 用于指定返回abilityInfo信息。取值范围：参考[BundleFlag说明](#bundleflagdeprecated)中Ability信息相关flag。 |
| userId | number | 是 | 用户ID。取值范围：大于等于0。 |
| callback | AsyncCallback<Array<[AbilityInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-abilityinfo)\>> | 是 | 程序启动作为入参的回调函数，返回Ability信息。 |

**示例：**

```ts
import bundle from '@ohos.bundle';
import Want from '@ohos.app.ability.Want';

let bundleFlags: number = 0;
let userId: number = 100;
let want: Want = {
  bundleName: "com.example.myapplication",
  abilityName: "EntryAbility"
};

bundle.queryAbilityByWant(want, bundleFlags, userId, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})
```

#### bundle.queryAbilityByWantdeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/ieN1WUN3Q4yGeZR8gR2qrw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=A86BDA2E7E5D56CBEE99547B9CCB488CAA5D74D52DB295447B7B9535BD1E9508)

从API version 7开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

queryAbilityByWant(want: Want, bundleFlags: number, callback: AsyncCallback<Array<AbilityInfo>>): void

根据给定的意图获取Ability信息，使用callback异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED 或 ohos.permission.GET\_BUNDLE\_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| want | [Want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-want) | 是 | 指示包含要查询的应用Bundle名称的意图。 |
| bundleFlags | number | 是 | 用于指定返回abilityInfo信息。取值范围：参考[BundleFlag说明](#bundleflagdeprecated)中Ability信息相关flag。 |
| callback | AsyncCallback<Array<[AbilityInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-abilityinfo)\>> | 是 | 程序启动作为入参的回调函数，返回Ability信息。 |

**示例：**

```ts
import bundle from '@ohos.bundle';
import Want from '@ohos.app.ability.Want';

let bundleFlags: number = 0;
let want: Want = {
  bundleName: "com.example.myapplication",
  abilityName: "EntryAbility"
};

bundle.queryAbilityByWant(want, bundleFlags, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})
```

#### bundle.getLaunchWantForBundledeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/4u504IY8T4WguKcMaZy5vA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=29E0E81FDAEC6C62FB47895080D0D1943B5A1F1EC99EBBA542864F07AB9AE1DC)

从API version 7开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

getLaunchWantForBundle(bundleName: string): Promise<Want>

查询拉起指定应用的want对象，使用Promise异步回调。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| bundleName | string | 是 | 要查询的应用Bundle名称。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[Want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-want)\> | 返回值为Promise对象，Promise中包含拉起指定应用的Want对象。 |

**示例：**

```ts
import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let bundleName: string = "com.example.myapplication";

bundle.getLaunchWantForBundle(bundleName)
  .then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })
```

#### bundle.getLaunchWantForBundledeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/gDiR_6chQp6Zp5zic9O_Sg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=3B71AB71796468DFADCE28E6D34FB151D38A518B7AFC4570DD2B7927208E94F0)

从API version 7开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

getLaunchWantForBundle(bundleName: string, callback: AsyncCallback<Want>): void

查询拉起指定应用的want对象，使用callback异步回调。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| bundleName | string | 是 | 要查询的应用Bundle名称。 |
| callback | AsyncCallback<[Want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-want)\> | 是 | 程序启动作为入参的回调函数，返回拉起指定应用的want对象。 |

**示例：**

```ts
import bundle from '@ohos.bundle';

let bundleName: string = "com.example.myapplication";

bundle.getLaunchWantForBundle(bundleName, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})
```

#### bundle.getNameForUid8+ deprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/D-BQAKmsTBS_6C8pVSMEKA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=4F634E9607D05CFE956117E42C02B27047C9B9110A5782CB491F35C88EF81BF4)

从API version 8开始支持，从API version 9开始废弃，建议使用[getBundleNameByUid](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager#bundlemanagergetbundlenamebyuid14-1)替代。

getNameForUid(uid: number): Promise<string>

通过uid获取对应的Bundle名称，使用Promise异步回调。

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| uid | number | 是 | 要查询的uid。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | 返回值为Promise对象，Promise中包含指定uid的Bundle名称。 |

**示例：**

```ts
import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let uid: number = 20010005;

bundle.getNameForUid(uid)
  .then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })
```

#### bundle.8+ deprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/xeOnJ807QLOS2gG-tRXZKQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=573FD53DFA5D5E0368744D348A601AAC71046AC12293513A7125A12D06953250)

从API version 8开始支持，从API version 9开始废弃，建议使用[getBundleNameByUid](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager#bundlemanagergetbundlenamebyuid14)替代。

getNameForUid(uid: number, callback: AsyncCallback<string>) : void

通过uid获取对应的Bundle名称，使用callback异步回调。

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| uid | number | 是 | 要查询的uid。 |
| callback | AsyncCallback<string> | 是 | 程序启动作为入参的回调函数，返回指定uid的Bundle名称。 |

**示例：**

```ts
import bundle from '@ohos.bundle';

let uid: number = 20010005;

bundle.getNameForUid(uid, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})
```

#### bundle.getAbilityIcon8+ deprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/IVFBemUVR8CpfpW-4wcxyg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=078E9FC940F3526995B713ECDA71C96F79C85B3983461B94A1692562B78D74AF)

从API version 8开始支持，从API version 9开始废弃，建议使用[resourceManager.getMediaContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resource-manager#getmediacontent9)替代。

getAbilityIcon(bundleName: string, abilityName: string): Promise<image.PixelMap>

通过bundleName和abilityName获取对应Icon的[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)，使用Promise异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED 或 ohos.permission.GET\_BUNDLE\_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| bundleName | string | 是 | 要查询的应用Bundle名称。 |
| abilityName | string | 是 | 要查询的Ability组件名。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<image.PixelMap> | 返回值为[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)。 |

**示例：**

```ts
import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let bundleName: string = "com.example.myapplication";
let abilityName: string = "EntryAbility";

bundle.getAbilityIcon(bundleName, abilityName)
  .then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })
```

#### bundle.getAbilityIcon8+ deprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/kJdo_qq_TimGE8Qm19dhog/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=D647E1619C7F87960BCBF22649F0657869F07AC91D586E1A420EF12D00FBBA1C)

从API version 8开始支持，从API version 9开始废弃，建议使用[resourceManager.getMediaContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resource-manager#getmediacontent9)替代。

getAbilityIcon(bundleName: string, abilityName: string, callback: AsyncCallback<image.PixelMap>): void

通过bundleName和abilityName获取对应Icon的[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)，使用callback异步回调。

获取调用方自己的信息时不需要权限。

**需要权限：**

ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED 或 ohos.permission.GET\_BUNDLE\_INFO

**系统能力：**

SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| bundleName | string | 是 | 要查询的应用Bundle名称。 |
| abilityName | string | 是 | 要查询的Ability组件名。 |
| callback | AsyncCallback<image.PixelMap> | 是 | 程序启动作为入参的回调函数，返回指定[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)。 |

**示例：**

```ts
import bundle from '@ohos.bundle';

let bundleName: string = "com.example.myapplication";
let abilityName: string = "EntryAbility";

bundle.getAbilityIcon(bundleName, abilityName, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})
```

#### InstallErrorCodedeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/4iHiPmOFQTycim85W2JBlg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=641C5C35936FD71C797ACAAD910C35EA1D754FD5141A73632F932A6D5EE18AE2)

从API version 7开始支持，从API version 9开始废弃，建议使用[包管理子系统通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bundle)替代。

**系统能力：** SystemCapability.BundleManager.BundleFramework

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| SUCCESS | 0 | 安装成功。 |
| STATUS\_INSTALL\_FAILURE | 1 | 安装失败（不存在安装的应用）。 |
| STATUS\_INSTALL\_FAILURE\_ABORTED | 2 | 安装中止。 |
| STATUS\_INSTALL\_FAILURE\_INVALID | 3 | 安装参数无效。 |
| STATUS\_INSTALL\_FAILURE\_CONFLICT | 4 | 安装冲突 （常见于升级和已有应用基本信息不一致）。 |
| STATUS\_INSTALL\_FAILURE\_STORAGE | 5 | 存储包信息失败。 |
| STATUS\_INSTALL\_FAILURE\_INCOMPATIBLE | 6 | 安装不兼容（常见于版本降级安装或者签名信息错误）。 |
| STATUS\_UNINSTALL\_FAILURE | 7 | 卸载失败 （不存在卸载的应用）。 |
| STATUS\_UNINSTALL\_FAILURE\_BLOCKED | 8 | 卸载中止 （没有使用）。 |
| STATUS\_UNINSTALL\_FAILURE\_ABORTED | 9 | 卸载中止 （参数无效导致）。 |
| STATUS\_UNINSTALL\_FAILURE\_CONFLICT | 10 | 卸载冲突 （卸载系统应用失败， 结束应用进程失败）。 |
| STATUS\_INSTALL\_FAILURE\_DOWNLOAD\_TIMEOUT | 0x0B | 安装失败 （下载超时）。 |
| STATUS\_INSTALL\_FAILURE\_DOWNLOAD\_FAILED | 0x0C | 安装失败 （下载失败）。 |
| STATUS\_RECOVER\_FAILURE\_INVALID8+ | 0x0D | 恢复预置应用失败。 |
| STATUS\_ABILITY\_NOT\_FOUND | 0x40 | Ability未找到。 |
| STATUS\_BMS\_SERVICE\_ERROR | 0x41 | BMS服务错误。 |
| STATUS\_FAILED\_NO\_SPACE\_LEFT8+ | 0x42 | 设备空间不足。 |
| STATUS\_GRANT\_REQUEST\_PERMISSIONS\_FAILED8+ | 0x43 | 应用授权失败。 |
| STATUS\_INSTALL\_PERMISSION\_DENIED8+ | 0x44 | 缺少安装权限。 |
| STATUS\_UNINSTALL\_PERMISSION\_DENIED8+ | 0x45 | 缺少卸载权限。 |

#### BundleFlagdeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/NiOTdRrcT6mrWVGTp9oYLw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=A41F3105AEA49F9BB0F0E516B0256835FB16950B135107B8D1FB7E9022D42959)

从API version 7开始支持，从API version 9开始废弃，建议使用[bundleManager.BundleFlag](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager#bundleflag)替代。

包信息标志，指示需要获取的包信息的内容。

当接口与标志不匹配时，该标志会被忽略，例如获取application时使用GET\_ABILITY\_INFO\_WITH\_PERMISSION对结果不会产生影响。

标志可以叠加使用，例如使用GET\_APPLICATION\_INFO\_WITH\_PERMISSION + GET\_APPLICATION\_INFO\_WITH\_DISABLE可以使结果同时包含应用权限信息和被禁用的应用信息。

**系统能力：** SystemCapability.BundleManager.BundleFramework

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| GET\_BUNDLE\_DEFAULT | 0x00000000 | 获取默认的应用信息。 |
| GET\_BUNDLE\_WITH\_ABILITIES | 0x00000001 | 获取包括Ability信息的包信息。 |
| GET\_ABILITY\_INFO\_WITH\_PERMISSION | 0x00000002 | 获取包括权限的Ability信息。 |
| GET\_ABILITY\_INFO\_WITH\_APPLICATION | 0x00000004 | 获取包括Application的ability信息。 |
| GET\_APPLICATION\_INFO\_WITH\_PERMISSION | 0x00000008 | 获取包括权限的应用信息。 |
| GET\_BUNDLE\_WITH\_REQUESTED\_PERMISSION | 0x00000010 | 获取包括所需权限的包信息。 |
| GET\_ABILITY\_INFO\_WITH\_METADATA8+ | 0x00000020 | 获取ability的元数据信息。 |
| GET\_APPLICATION\_INFO\_WITH\_METADATA8+ | 0x00000040 | 获取应用的元数据信息。 |
| GET\_ABILITY\_INFO\_SYSTEMAPP\_ONLY8+ | 0x00000080 | 获取仅包括系统应用的ability信息。 |
| GET\_ABILITY\_INFO\_WITH\_DISABLE8+ | 0x00000100 | 获取包括被禁用的ability信息。 |
| GET\_APPLICATION\_INFO\_WITH\_DISABLE8+ | 0x00000200 | 获取包括被禁用的应用信息。 |
| GET\_ALL\_APPLICATION\_INFO | 0xFFFF0000 | 获取应用所有的信息。 |

#### BundleOptionsdeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/lEd8k85JRx6akG2pZjzYvQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=5E735CB8154EDD854B2C25C50AF824AE92364D643BC785B47DA81B696EF1E466)

从API version 7开始支持，从API version 9开始废弃，暂无替代接口。

查询选项，包含userId。

**系统能力：** SystemCapability.BundleManager.BundleFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| userId | number | 否 | 是 | 用户ID。默认值：调用方所在用户，取值范围：大于等于0。 |

#### AbilityTypedeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/kb-vKOA6SayaMYCuOVH1fg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=9165793B7C02452E7F9D83456382B074A1BB3045935A327705D78646508AA0F7)

从API version 7开始支持，从API version 9开始废弃，建议使用[bundleManager.AbilityType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager#abilitytype)替代。

Ability组件类型。

**系统能力：** SystemCapability.BundleManager.BundleFramework

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| UNKNOWN | 无 | 未知Ability类型。 |
| PAGE | 无 | 表示基于Page模板开发的FA，用于提供与用户交互的能力。 |
| SERVICE | 无 | 表示基于Service模板开发的PA，用于提供后台运行任务的能力。 |
| DATA | 无 | 表示基于Data模板开发的PA，用于对外部提供统一的数据访问对象。 |

#### DisplayOrientationdeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/iIisDc0VR967eZtZ8P5qaw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=E4F71B468EF7CBCDB4D9BC14D2A181AC69FB6E6761F88F8EA9E6A2E85785C53A)

从API version 7开始支持，从API version 9开始废弃，建议使用[bundleManager.DisplayOrientation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager#displayorientation)替代。

屏幕显示方向。

**系统能力：** SystemCapability.BundleManager.BundleFramework

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| UNSPECIFIED | 无 | 屏幕方向--不指定。 |
| LANDSCAPE | 无 | 屏幕方向--横屏。 |
| PORTRAIT | 无 | 屏幕方向--竖屏。 |
| FOLLOW\_RECENT | 无 | 屏幕方向--紧跟上一个组件。 |

#### LaunchModedeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/-l0iTvWpTbK718-Dm-TspQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=04CD5CE1E66C4D967F0D6D9D6100B307315A0BB05A194246B94B621F647DDD9D)

从API version 7开始支持，从API version 9开始废弃，建议使用[bundleManager.LaunchType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager#launchtype)替代。

Ability组件的启动模式。

**系统能力：** SystemCapability.BundleManager.BundleFramework

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| SINGLETON | 0 | Ability只有一个实例。 |
| STANDARD | 1 | Ability有多个实例。 |

#### AbilitySubTypedeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/xPCn2o9iQaqdDVzVrN-uIg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=474EA9E50AB59961FCE2F8BD5A3FAA7B89116895FA7670D0B9CA5032CE1B28DD)

从API version 7开始支持，从API version 9开始废弃，暂无替代接口。

Ability组件的子类型。

**系统能力：** SystemCapability.BundleManager.BundleFramework

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| UNSPECIFIED | 0 | 未定义Ability子类型。 |
| CA | 1 | Ability子类型是带有 UI 的服务。 |

#### ColorModedeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/VmM9TYmFRfarbaREcL87_w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=E2C3E44667EE026F8D74961A1CE92466462F68A9019526C3FD7F3D129A4E4059)

从API version 7开始支持，从API version 9开始废弃，暂无替代接口。

应用、卡片等的颜色模式。

**系统能力：** SystemCapability.BundleManager.BundleFramework

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| AUTO\_MODE | \-1 | 自动模式。 |
| DARK\_MODE | 0 | 黑色模式。 |
| LIGHT\_MODE | 1 | 亮度模式。 |

#### GrantStatusdeprecated

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/ELNcxdeES-KLQXE54SH77w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=97ACA538AC39E3F2227E621FEF2F080985EEE14E3578439D5FBC0B5AAE228680)

从API version 7开始支持，从API version 9开始废弃，建议使用[bundleManager.PermissionGrantState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager#permissiongrantstate)替代。

权限授予状态。

**系统能力：** SystemCapability.BundleManager.BundleFramework

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| PERMISSION\_DENIED | \-1 | 拒绝授予权限。 |
| PERMISSION\_GRANTED | 0 | 授予权限。 |

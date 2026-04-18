---
title: "@ohos.abilityAccessCtrl (程序访问控制管理)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-abilityaccessctrl"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "通用能力的接口(推荐)"
  - "@ohos.abilityAccessCtrl (程序访问控制管理)"
captured_at: "2026-04-17T01:47:47.014Z"
---

# @ohos.abilityAccessCtrl (程序访问控制管理)

程序访问控制提供应用程序的权限校验和管理能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/n3WcWshoTBGp1bcfdfXWuQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=CD978DFC6411568F57D9AFD19D780CEBE3C6D2FCC063D3E6D53162C057486DD2)

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import { abilityAccessCtrl } from '@kit.AbilityKit';
```

#### abilityAccessCtrl.createAtManager

createAtManager(): AtManager

访问控制管理：创建程序访问控制管理的实例对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.AccessToken

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [AtManager](#atmanager) | 获取程序访问控制模块的实例。 |

**示例：**

```ts
let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
```

#### AtManager

管理访问控制模块的实例。

AtManager接口调用依赖于tokenID，应用可通过[bundleManager.getBundleInfoForSelf](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager#bundlemanagergetbundleinfoforself)获取tokenID。

#### \[h2\]checkAccessToken9+

checkAccessToken(tokenID: number, permissionName: Permissions): Promise<GrantStatus>

校验应用是否被授予权限。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.AccessToken

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| tokenID | number | 是 | 要校验的目标应用的身份标识，可通过应用的[ApplicationInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-applicationinfo)的accessTokenId字段获得。 |
| permissionName | [Permissions](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-permissions) | 是 | 需要校验的权限名称，合法的权限名取值可在[应用权限列表](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-permissions)中查询。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[GrantStatus](#grantstatus)\> | Promise对象，返回授权状态结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[访问控制错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-access-token)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 12100001 | Invalid parameter. The tokenID is 0, or the permissionName exceeds 256 characters. |

**示例：**

```ts
import { abilityAccessCtrl } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let tokenID: number = 0; // 获取tokenID的方式可参考AtManager章节的描述。
atManager.checkAccessToken(tokenID, 'ohos.permission.GRANT_SENSITIVE_PERMISSIONS').then((data: abilityAccessCtrl.GrantStatus) => {
  console.info(`checkAccessToken success, result: ${data}`);
}).catch((err: BusinessError) => {
  console.error(`checkAccessToken fail, code: ${err.code}, message: ${err.message}`);
});
```

#### \[h2\]checkAccessTokenSync10+

checkAccessTokenSync(tokenID: number, permissionName: Permissions): GrantStatus

校验应用是否被授予权限，同步返回结果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.AccessToken

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| tokenID | number | 是 | 要校验的目标应用的身份标识，可通过应用的[ApplicationInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-applicationinfo)的accessTokenId字段获得。 |
| permissionName | [Permissions](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-permissions) | 是 | 需要校验的权限名称，合法的权限名取值可在[应用权限列表](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-permissions)中查询。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [GrantStatus](#grantstatus) | 枚举实例，返回授权状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[访问控制错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-access-token)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 12100001 | Invalid parameter. The tokenID is 0, or the permissionName exceeds 256 characters. |

**示例：**

```ts
import { abilityAccessCtrl, Permissions } from '@kit.AbilityKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let tokenID: number = 0; // 获取tokenID的方式可参考AtManager章节的描述。
let permissionName: Permissions = 'ohos.permission.GRANT_SENSITIVE_PERMISSIONS';
let data: abilityAccessCtrl.GrantStatus = atManager.checkAccessTokenSync(tokenID, permissionName);
console.info(`Result: ${data}`);
```

#### \[h2\]on18+

on(type: 'selfPermissionStateChange', permissionList: Array<Permissions>, callback: Callback<PermissionStateChangeInfo>): void

订阅本应用的指定权限列表的权限授权状态变化事件。当本应用对应权限的授权状态发生变化时，触发对应回调函数的执行。使用callback异步回调。

-   多次调用本订阅接口时，如果订阅的权限列表相同，callback不同，允许订阅成功。
    
-   多次调用本订阅接口时，如果订阅的权限列表间有相同的子集，callback相同时，订阅失败。
    

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.AccessToken

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅事件类型，固定为'selfPermissionStateChange'，自身权限状态变更事件。 |
| permissionList | Array<[Permissions](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-permissions)\> | 是 | 订阅的权限名列表，如果为空，则表示订阅所有的权限状态变化，合法的权限名取值可在[应用权限列表](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-permissions)中查询。 |
| callback | Callback<[PermissionStateChangeInfo](#permissionstatechangeinfo18)\> | 是 | 回调函数，返回订阅指定权限名状态变更事件的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[访问控制错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-access-token)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 12100001 | Invalid parameter. Possible causes: 1. The permissionList exceeds the size limit; 2. The permissionNames in the list are all invalid. |
| 12100004 | The API is used repeatedly with the same input. |
| 12100005 | The registration time has exceeded the limit. |
| 12100007 | The service is abnormal. |

**示例：**

```ts
import { abilityAccessCtrl, Permissions } from '@kit.AbilityKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let permissionList: Array<Permissions> = ['ohos.permission.APPROXIMATELY_LOCATION'];
try {
    atManager.on('selfPermissionStateChange', permissionList, (data: abilityAccessCtrl.PermissionStateChangeInfo) => {
        console.info(`receive permission state change, result: ${data}`);
    });
} catch(err) {
    console.error(`Code: ${err.code}, message: ${err.message}`);
}
```

#### \[h2\]off18+

off(type: 'selfPermissionStateChange', permissionList: Array<Permissions>, callback?: Callback<PermissionStateChangeInfo>): void

取消订阅自身指定权限列表的权限状态变更事件。使用callback异步回调。

取消订阅不传callback时，批量删除permissionList下面的所有callback。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.AccessToken

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅事件类型，固定为'selfPermissionStateChange'，权限状态变更事件。 |
| permissionList | Array<[Permissions](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-permissions)\> | 是 | 取消订阅的权限名列表，为空时表示取消订阅所有的权限状态变化，必须与[on](#on18)的输入一致，合法的权限名取值可在[应用权限列表](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-permissions)中查询。 |
| callback | Callback<[PermissionStateChangeInfo](#permissionstatechangeinfo18)\> | 否 | 回调函数，返回取消订阅指定tokenID与指定权限名状态变更事件的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[访问控制错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-access-token)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 12100004 | The API is not used in pair with "on". |
| 12100007 | The service is abnormal. |

**示例：**

```ts
import { abilityAccessCtrl, Permissions } from '@kit.AbilityKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let permissionList: Array<Permissions> = ['ohos.permission.APPROXIMATELY_LOCATION'];
try {
    atManager.off('selfPermissionStateChange', permissionList);
} catch(err) {
    console.error(`Code: ${err.code}, message: ${err.message}`);
}
```

#### \[h2\]requestPermissionsFromUser9+

requestPermissionsFromUser(context: Context, permissionList: Array<Permissions>, requestCallback: AsyncCallback<PermissionRequestResult>): void

用于UIAbility/UIExtensionAbility拉起弹框请求[用户授权](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/request-user-authorization)。使用callback异步回调。

如果用户拒绝授权，将无法再次拉起弹框，需要用户在系统应用“设置”的界面中，手动授予权限，或是调用[requestPermissionOnSetting](#requestpermissiononsetting12)，拉起权限设置弹框，引导用户授权。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/EWWeWCdGTR2SgQIWpH81lw/zh-cn_image_0000002569020057.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=D4575084D53409280CFEB6A7ADAEA912A51B89D5F3FFC973A3AC5231CF4C8DEA)

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.AccessToken

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| context | [Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context) | 是 | 请求权限的UIAbility/UIExtensionAbility的Context。 |
| permissionList | Array<[Permissions](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-permissions)\> | 是 | 权限名列表，合法的权限名取值可在[应用权限列表](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-permissions)中查询。 |
| requestCallback | AsyncCallback<[PermissionRequestResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-permissionrequestresult)\> | 是 | 回调函数。当拉起权限请求弹框成功，err为undefined，data为获取到的PermissionRequestResult；否则err为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[访问控制错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-access-token)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 12100001 | (Deprecated in 12) Invalid parameter. The context is invalid when it does not belong to the application itself. |
| 12100009 | Common inner error. An error occurs when creating the pop-up window or obtaining user operation results. |

**示例：**

下述示例中context的获取方式请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

关于向用户申请授权的完整流程及示例，请参见[向用户申请授权](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/request-user-authorization)。

```ts
import { abilityAccessCtrl, Context, PermissionRequestResult, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
// 请在组件内获取context
let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
atManager.requestPermissionsFromUser(context, ['ohos.permission.CAMERA'], (err: BusinessError, data: PermissionRequestResult) => {
  if (err) {
    console.error(`requestPermissionsFromUser fail, code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`requestPermissionsFromUser success, result: ${data}`);
    console.info('requestPermissionsFromUser data permissions:' + data.permissions);
    console.info('requestPermissionsFromUser data authResults:' + data.authResults);
    console.info('requestPermissionsFromUser data dialogShownResults:' + data.dialogShownResults);
    console.info('requestPermissionsFromUser data errorReasons:' + data.errorReasons);
  }
});
```

#### \[h2\]requestPermissionsFromUser9+

requestPermissionsFromUser(context: Context, permissionList: Array<Permissions>): Promise<PermissionRequestResult>

用于UIAbility/UIExtensionAbility拉起弹框请求[用户授权](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/request-user-authorization)。使用Promise异步回调。

如果用户拒绝授权，将无法再次拉起弹框，需要用户在系统应用“设置”的界面中，手动授予权限，或是调用[requestPermissionOnSetting](#requestpermissiononsetting12)，拉起权限设置弹框，引导用户授权。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.AccessToken

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| context | [Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context) | 是 | 请求权限的UIAbility/UIExtensionAbility的Context。 |
| permissionList | Array<[Permissions](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-permissions)\> | 是 | 权限名列表，合法的权限名取值可在[应用权限列表](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-permissions)中查询。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[PermissionRequestResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-permissionrequestresult)\> | Promise对象，返回接口的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[访问控制错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-access-token)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 12100001 | (Deprecated in 12) Invalid parameter. The context is invalid when it does not belong to the application itself. |
| 12100009 | Common inner error. An error occurs when creating the pop-up window or obtaining user operation results. |

**示例：**

下述示例中context的获取方式请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

关于向用户申请授权的完整流程及示例，请参见[向用户申请授权](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/request-user-authorization)。

```ts
import { abilityAccessCtrl, Context, PermissionRequestResult, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
// 请在组件内获取context
let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
atManager.requestPermissionsFromUser(context, ['ohos.permission.CAMERA']).then((data: PermissionRequestResult) => {
  console.info(`requestPermissionsFromUser success, result: ${data}`);
  console.info('requestPermissionsFromUser data permissions:' + data.permissions);
  console.info('requestPermissionsFromUser data authResults:' + data.authResults);
  console.info('requestPermissionsFromUser data dialogShownResults:' + data.dialogShownResults);
  console.info('requestPermissionsFromUser data errorReasons:' + data.errorReasons);
}).catch((err: BusinessError) => {
  console.error(`requestPermissionsFromUser fail, code: ${err.code}, message: ${err.message}`);
});
```

#### \[h2\]requestPermissionOnSetting12+

requestPermissionOnSetting(context: Context, permissionList: Array<Permissions>): Promise<Array<GrantStatus>>

用于[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability#uiability)/[UIExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiextensionability#uiextensionability)二次拉起权限设置弹框。使用Promise异步回调。

在调用此接口前，应用需要先调用[requestPermissionsFromUser](#requestpermissionsfromuser9)，如果用户在首次弹窗授权时已授权，调用当前接口将无法拉起弹窗。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/Iw79kLO9QmaRq4EdSAH1hg/zh-cn_image_0000002568900049.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=B286BA1C0A76F4AABD8DA161590AA0F37A4DB8346EA540255F8516A4C41FFBD1)

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.AccessToken

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| context | [Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context) | 是 | 请求权限的UIAbility/UIExtensionAbility的Context。 |
| permissionList | Array<[Permissions](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-permissions)\> | 是 | 权限名列表，合法的权限名取值可在[应用权限组列表](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-permission-group-list)中查询。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<[GrantStatus](#grantstatus)\>> | Promise对象，返回授权状态结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[访问控制错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-access-token)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12100001 | 
Invalid parameter. Possible causes:

1\. The context is invalid because it does not belong to the application itself;

2\. The permission list contains the permission that is not declared in the module.json file;

3\. The permission list is invalid because the permissions in it do not belong to the same permission group;

4\. The permission list contains one or more system\_grant permissions.

 |
| 12100009 | Common inner error. An error occurs when creating the pop-up window or obtaining user operation result. |
| 12100011 | All permissions in the permission list have been granted. |
| 12100012 | The permission list contains the permission that has not been revoked by the user. |
| 12100014 | Unexpected permission. You cannot request this type of permission from users via a pop-up window. |

**示例：**

示例中context的获取方式请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
import { abilityAccessCtrl, Context, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
// 请在组件内获取context
let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
atManager.requestPermissionOnSetting(context, ['ohos.permission.CAMERA']).then((data: Array<abilityAccessCtrl.GrantStatus>) => {
  console.info(`requestPermissionOnSetting success, result: ${data}`);
}).catch((err: BusinessError) => {
  console.error(`requestPermissionOnSetting fail, code: ${err.code}, message: ${err.message}`);
});
```

#### \[h2\]requestGlobalSwitch12+

requestGlobalSwitch(context: Context, type: SwitchType): Promise<boolean>

用于UIAbility/UIExtensionAbility拉起全局开关设置弹框。使用Promise异步回调。

在某些情况下，如果录音、拍照等功能被禁用，应用可拉起此弹框请求用户同意开启对应功能。如果当前全局开关的状态为开启，则不拉起弹框。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/tXLI1j29StGU3juxNyBffQ/zh-cn_image_0000002538020344.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=8B1E84461DEED272EA8DDCE24AE3CF4130BAC718B5A744AA2DB87D16A4E5F673)

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.AccessToken

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| context | [Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context) | 是 | 请求权限的UIAbility/UIExtensionAbility的Context。 |
| type | [SwitchType](#switchtype12) | 是 | 全局开关类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象。返回true，表示全局开关状态为开启。返回false，表示全局开关状态为关闭。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[访问控制错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-access-token)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12100001 | Invalid parameter. Possible causes: 1. The context is invalid because it does not belong to the application itself; 2. The type of global switch is not support. |
| 12100009 | Common inner error. An error occurs when creating the pop-up window or obtaining user operation result. |
| 12100013 | The specific global switch is already open. |

**示例：**

示例中context的获取方式请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
import { abilityAccessCtrl, Context, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
// 请在组件内获取context
let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
atManager.requestGlobalSwitch(context, abilityAccessCtrl.SwitchType.CAMERA).then((data: Boolean) => {
  console.info(`requestGlobalSwitch success, result: ${data}`);
}).catch((err: BusinessError) => {
  console.error(`requestGlobalSwitch fail, code: ${err.code}, message: ${err.message}`);
});
```

#### \[h2\]getSelfPermissionStatus20+

getSelfPermissionStatus(permissionName: Permissions): PermissionStatus

查询应用权限状态，同步返回结果。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.AccessToken

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| permissionName | [Permissions](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-permissions) | 是 | 需要校验的权限名称，合法的权限名取值可在[应用权限列表](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-permissions)中查询。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [PermissionStatus](#permissionstatus20) | 枚举实例，返回权限状态。 |

**错误码：**

以下错误码的详细介绍请参见[访问控制错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-access-token)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12100001 | Invalid parameter. The permissionName is empty or exceeds 256 characters. |
| 12100007 | The service is abnormal. |

**示例：**

```ts
import { abilityAccessCtrl } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
try {
  let data: abilityAccessCtrl.PermissionStatus = atManager.getSelfPermissionStatus('ohos.permission.CAMERA');
  console.info(`getSelfPermissionStatus success, result: ${data}`);
} catch(err) {
  console.error(`getSelfPermissionStatus fail, code: ${err.code}, message: ${err.message}`);
}
```

#### \[h2\]openPermissionOnSetting22+

openPermissionOnSetting(context: Context, permission: Permissions): Promise<SelectedResult>

用于[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability#uiability)/[UIExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiextensionability#uiextensionability)拉起跳转设置页的弹窗。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.AccessToken

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| context | [Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context) | 是 | 请求权限的UIAbility/UIExtensionAbility的Context。 |
| permission | [Permissions](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-permissions) | 是 | 权限名，只支持授权方式为[manual\_settings](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-permission-mgmt-overview#manual_settings手动设置授权)类型的权限。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[SelectedResult](#selectedresult22)\> | Promise对象，返回跳转设置页弹窗结果。 |

**错误码：**

以下错误码的详细介绍请参见[访问控制错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-access-token)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12100001 | 
Invalid parameter. Possible causes:

1\. The context is invalid because it does not belong to the application itself;

2\. The permission is invalid or not declared in the module.json file.

 |
| 12100009 | Common inner error. An error occurs when creating the pop-up window or obtaining user operation result. |
| 12100014 | Unexpected permission. The permission is not a manual\_settings permission. |

**示例：**

示例中context的获取方式请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
import { abilityAccessCtrl, Context, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
// 请在组件内获取context
let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
atManager.openPermissionOnSetting(context, 'ohos.permission.HOOK_KEY_EVENT').then((data: abilityAccessCtrl.SelectedResult) => {
  console.info(`openPermissionOnSetting success, result: ${data}`);
}).catch((err: BusinessError) => {
  console.error(`openPermissionOnSetting fail, code: ${err.code}, message: ${err.message}`);
});
```

#### \[h2\]verifyAccessTokenSync9+

verifyAccessTokenSync(tokenID: number, permissionName: Permissions): GrantStatus

校验应用是否被授予权限，同步返回结果。

**系统能力：** SystemCapability.Security.AccessToken

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| tokenID | number | 是 | 要校验的目标应用的身份标识，可通过应用的[ApplicationInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-applicationinfo)的accessTokenId字段获得。 |
| permissionName | [Permissions](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-permissions) | 是 | 需要校验的权限名称，合法的权限名取值可在[应用权限列表](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-permissions)中查询。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [GrantStatus](#grantstatus) | 枚举实例，返回授权状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[访问控制错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-access-token)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 12100001 | Invalid parameter. The tokenID is 0, or the permissionName exceeds 256 characters. |

**示例：**

```ts
import { abilityAccessCtrl } from '@kit.AbilityKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let tokenID: number = 0; // 获取tokenID的方式可参考AtManager章节的描述。
try {
  let data: abilityAccessCtrl.GrantStatus = atManager.verifyAccessTokenSync(tokenID, 'ohos.permission.GRANT_SENSITIVE_PERMISSIONS');
  console.info(`verifyAccessTokenSync success, result: ${data}`);
} catch(err) {
  console.error(`verifyAccessTokenSync fail, code: ${err.code}, message: ${err.message}`);
}
```

#### \[h2\]verifyAccessToken9+

verifyAccessToken(tokenID: number, permissionName: Permissions): Promise<GrantStatus>

校验应用是否被授予权限。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/DkNdKfGwTf6Z1BzY6YzIbw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=B87968599140F84D7EB74BDA30CF6697012DDD7E35460774B4BEB7B0B56D139E)

建议使用[checkAccessToken](#checkaccesstoken9)替代。

**系统能力：** SystemCapability.Security.AccessToken

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| tokenID | number | 是 | 要校验的目标应用的身份标识，可通过应用的[ApplicationInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-applicationinfo)的accessTokenId字段获得。 |
| permissionName | [Permissions](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-permissions) | 是 | 需要校验的权限名称，合法的权限名取值可在[应用权限列表](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-permissions)中查询。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[GrantStatus](#grantstatus)\> | Promise对象，返回授权状态结果。 |

**示例：**

```ts
import { abilityAccessCtrl, Permissions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let tokenID: number = 0; // 获取tokenID的方式可参考AtManager章节的描述。
let permissionName: Permissions = 'ohos.permission.GRANT_SENSITIVE_PERMISSIONS';
atManager.verifyAccessToken(tokenID, permissionName).then((data: abilityAccessCtrl.GrantStatus) => {
  console.info(`verifyAccessToken success, result: ${data}`);
}).catch((err: BusinessError) => {
  console.error(`verifyAccessToken fail, code: ${err.code}, message: ${err.message}`);
});
```

#### \[h2\]verifyAccessToken(deprecated)

verifyAccessToken(tokenID: number, permissionName: string): Promise<GrantStatus>

校验应用是否被授予权限。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/r8Y4xtcvSQKi9DXc7F9qCw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=86EC859BFE7BCE688BE7BC0B1E4A0A746F5BBD21D0AD875C813F410562F0E9E0)

从API version 8 开始支持，从API version 9 开始废弃，建议使用[checkAccessToken](#checkaccesstoken9)替代。

**系统能力：** SystemCapability.Security.AccessToken

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| tokenID | number | 是 | 要校验的目标应用的身份标识，可通过应用的[ApplicationInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-applicationinfo)的accessTokenId字段获得。 |
| permissionName | string | 是 | 需要校验的权限名称，合法的权限名取值可在[应用权限列表](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-permissions)中查询。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[GrantStatus](#grantstatus)\> | Promise对象，返回授权状态结果。 |

**示例：**

```ts
import { abilityAccessCtrl } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let tokenID: number = 0; // 获取tokenID的方式可参考AtManager章节的描述。
atManager.verifyAccessToken(tokenID, 'ohos.permission.GRANT_SENSITIVE_PERMISSIONS').then((data: abilityAccessCtrl.GrantStatus) => {
  console.info(`verifyAccessToken success, result: ${data}`);
}).catch((err: BusinessError) => {
  console.error(`verifyAccessToken fail, code: ${err.code}, message: ${err.message}`);
});
```

#### GrantStatus

表示授权状态的枚举。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.AccessToken

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| PERMISSION\_DENIED | \-1 | 表示未授权。 |
| PERMISSION\_GRANTED | 0 | 表示已授权。 |

#### SwitchType12+

表示全局开关类型的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.AccessToken

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| CAMERA | 0 | 表示相机全局开关。 |
| MICROPHONE | 1 | 表示麦克风全局开关。 |
| LOCATION | 2 | 表示位置全局开关。 |

#### PermissionStateChangeType18+

表示权限授权状态变化操作类型的枚举。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.AccessToken

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| PERMISSION\_REVOKED\_OPER | 0 | 表示权限取消操作。 |
| PERMISSION\_GRANTED\_OPER | 1 | 表示权限授予操作。 |

#### PermissionStateChangeInfo18+

表示某次权限授权状态变化的详情。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.AccessToken

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| change | [PermissionStateChangeType](#permissionstatechangetype18) | 否 | 否 | 权限授权状态变化类型。 |
| tokenID | number | 否 | 否 | 被订阅的应用身份标识，可通过应用的[ApplicationInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-applicationinfo)的accessTokenId字段获得。 |
| permissionName | [Permissions](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-permissions) | 否 | 否 | 当前授权状态发生变化的权限名，合法的权限名取值可在[应用权限列表](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-permissions)中查询。 |

#### PermissionRequestResult10+

type PermissionRequestResult = \_PermissionRequestResult

权限请求结果对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.AccessToken

| 类型 | 说明 |
| :-- | :-- |
| [\_PermissionRequestResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-permissionrequestresult) | 权限请求结果对象。 |

#### Context10+

type Context = \_Context

提供了ability或application的上下文的能力，包括访问特定应用程序的资源等。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.AccessToken

| 类型 | 说明 |
| :-- | :-- |
| [\_Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context) | 提供了ability或application的上下文的能力，包括访问特定应用程序的资源等。 |

#### PermissionStatus20+

表示权限状态的枚举。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.AccessToken

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| DENIED | \-1 | 表示用户未授权。 |
| GRANTED | 0 | 表示已授权。 |
| NOT\_DETERMINED | 1 | 表示未操作。应用声明[用户授权权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/permissions-for-all-user)，暂未调用[requestPermissionsFromUser](#requestpermissionsfromuser9)接口请求用户授权时，或用户在设置中将权限状态修改为每次询问时，查询权限状态将返回此值。 |
| INVALID | 2 | 表示无效。应用未[声明权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/declare-permissions)或当前无法处理。例如：当模糊位置权限的状态为NOT\_DETERMINED时，查询精确位置权限状态，返回此值。 |
| RESTRICTED | 3 | 表示受限。用户未同意隐私声明（仅系统应用会返回此状态）。 |

#### SelectedResult22+

表示跳转设置页弹窗结果的枚举。

**系统能力：** SystemCapability.Security.AccessToken

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| REJECTED | \-1 | 表示用户选择不允许前往设置。 |
| OPENED | 0 | 表示用户选择前往设置。 |
| GRANTED | 1 | 表示权限已授权，无需弹窗。 |

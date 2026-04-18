---
title: "@ohos.account.appAccount (应用账号管理)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-appaccount"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "Basic Services Kit（基础服务）"
  - "ArkTS API"
  - "账号管理"
  - "@ohos.account.appAccount (应用账号管理)"
captured_at: "2026-04-17T01:48:27.907Z"
---

# @ohos.account.appAccount (应用账号管理)

本模块提供应用账号信息的添加、删除、修改和查询基础能力，并支持应用间鉴权和分布式数据同步功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/BvlIuqbGQ1udmXBMz5V9kw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=7545992BC8D4056210926BD2FAAAA65BA183CAF346542311C299A321DB025660)

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import { appAccount } from '@kit.BasicServicesKit';
```

#### appAccount.createAppAccountManager

createAppAccountManager(): AppAccountManager

创建应用账号管理器对象。

**系统能力：** SystemCapability.Account.AppAccount

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [AppAccountManager](#appaccountmanager) | 应用账号管理器对象。 |

**示例：**

```ts
let appAccountManager: appAccount.AppAccountManager = appAccount.createAppAccountManager();
```

#### AppAccountManager

应用账号管理器，可用于管理应用自身的账号信息。

#### \[h2\]createAccount9+

createAccount(name: string, callback: AsyncCallback<void>): void

根据账号名创建应用账号。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当创建成功时，err为null，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name. |
| 12300004 | Account already exists. |
| 12300007 | The number of accounts reaches the upper limit. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.createAccount('WangWu', (err: BusinessError) => {
    if (err) {
      console.error(`createAccount code: code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('createAccount successful.');
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`createAccount err: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]createAccount9+

createAccount(name: string, options: CreateAccountOptions, callback: AsyncCallback<void>): void

根据账号名和可选项创建应用账号。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| options | [CreateAccountOptions](#createaccountoptions9) | 是 | 创建应用账号的选项，可提供自定义数据，但不建议包含敏感数据（如密码、Token等）。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当创建成功时，err为null，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name or options. |
| 12300004 | Account already exists. |
| 12300007 | The number of accounts reaches the upper limit. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let options: appAccount.CreateAccountOptions = {
  customData: {
    age: '10'
  }
}
try {
  appAccountManager.createAccount('LiSi', options, (err: BusinessError) => {
    if (err) {
      console.error(`createAccount failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('createAccount successfully');
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`createAccount exception: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]createAccount9+

createAccount(name: string, options?: CreateAccountOptions): Promise<void>

根据账号名和可选项创建应用账号。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| options | [CreateAccountOptions](#createaccountoptions9) | 否 | 创建应用账号的选项，可提供自定义数据，但不建议包含敏感数据（如密码、Token等）。不填无影响，默认为空，表示创建的该账号无额外信息需要添加。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name or options. |
| 12300004 | Account already exists. |
| 12300007 | The number of accounts reaches the upper limit. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let options: appAccount.CreateAccountOptions = {
  customData: {
    age: '10'
  }
}
try {
  appAccountManager.createAccount('LiSi', options).then(() => {
    console.info('createAccount successfully');
  }).catch((err: BusinessError) => {
    console.error(`createAccount failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`createAccount exception: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]createAccountImplicitly9+

createAccountImplicitly(owner: string, callback: AuthCallback): void

根据指定的账号所有者隐式地创建应用账号。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| owner | string | 是 | 应用账号所有者的包名。 |
| callback | [AuthCallback](#authcallback9) | 是 | 认证器回调对象，返回创建结果。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid owner. |
| 12300007 | The number of accounts reaches the upper limit. |
| 12300010 | Account service busy. |
| 12300113 | Authenticator service not found. |
| 12300114 | Authenticator service exception. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { Want, common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext

  onResultCallback(code: number, result?: appAccount.AuthResult): void {
    console.info('resultCode: ' + code);
    console.info('result: ' + JSON.stringify(result));
  }

  onRequestRedirectedCallback(request: Want): void {
    let wantInfo: Want = {
      deviceId: '',
      bundleName: 'com.example.accountjsdemo',
      action: 'ohos.want.action.viewData',
      entities: ['entity.system.default'],
    }
    this.context.startAbility(wantInfo).then(() => {
      console.info('startAbility successfully');
    }).catch((err: BusinessError) => {
      console.error(`startAbility err: code is ${err.code}, message is ${err.message}`);
    })
  }

  aboutToAppear(): void {
    try {
      appAccountManager.createAccountImplicitly('com.example.accountjsdemo', {
        onResult: this.onResultCallback,
        onRequestRedirected: this.onRequestRedirectedCallback
      });
    } catch (e) {
      const err = e as BusinessError;
      console.error(`createAccountImplicitly exception: code is ${err.code}, message is ${err.message}`);
    }
  }
  build() {}
}
```

#### \[h2\]createAccountImplicitly9+

createAccountImplicitly(owner: string, options: CreateAccountImplicitlyOptions, callback: AuthCallback): void

根据指定的账号所有者和可选项隐式地创建应用账号。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| owner | string | 是 | 应用账号所有者的包名。 |
| options | [CreateAccountImplicitlyOptions](#createaccountimplicitlyoptions9) | 是 | 隐式创建账号的选项。 |
| callback | [AuthCallback](#authcallback9) | 是 | 认证器回调对象，返回创建结果。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid owner or options. |
| 12300007 | The number of accounts reaches the upper limit. |
| 12300010 | Account service busy. |
| 12300113 | Authenticator service not found. |
| 12300114 | Authenticator service exception. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { Want, common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext

  onResultCallback(code: number, result?: appAccount.AuthResult): void {
    console.info('resultCode: ' + code);
    console.info('result: ' + JSON.stringify(result));
  }

  onRequestRedirectedCallback(request: Want): void {
    let wantInfo: Want = {
      deviceId: '',
      bundleName: 'com.example.accountjsdemo',
      action: 'ohos.want.action.viewData',
      entities: ['entity.system.default'],
    }
    this.context.startAbility(wantInfo).then(() => {
      console.info('startAbility successfully');
    }).catch((err: BusinessError) => {
      console.error(`startAbility err: code is ${err.code}, message is ${err.message}`);
    })
  }

  aboutToAppear(): void {
    let options: appAccount.CreateAccountImplicitlyOptions = {
      authType: 'getSocialData',
      requiredLabels: ['student']
    };
    try {
      appAccountManager.createAccountImplicitly('com.example.accountjsdemo', options, {
        onResult: this.onResultCallback,
        onRequestRedirected: this.onRequestRedirectedCallback
      });
    } catch (e) {
      const err = e as BusinessError;
      console.error(`createAccountImplicitly exception: code is ${err.code}, message is ${err.message}`);
    }
  }
  build() {}
}
```

#### \[h2\]removeAccount9+

removeAccount(name: string, callback: AsyncCallback<void>): void

删除应用账号。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当删除成功时，err为null，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name. |
| 12300003 | Account not found. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.removeAccount('ZhaoLiu', (err: BusinessError) => {
    if (err) {
      console.error(`removeAccount failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('removeAccount successfully');
    }
 });
} catch (e) {
  const err = e as BusinessError;
  console.error(`removeAccount exception: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]removeAccount9+

removeAccount(name: string): Promise<void>

删除应用账号。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name. |
| 12300003 | Account not found. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.removeAccount('Lisi').then(() => {
    console.info('removeAccount successfully');
  }).catch((err: BusinessError) => {
    console.error(`removeAccount failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`removeAccount exception: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]setAppAccess9+

setAppAccess(name: string, bundleName: string, isAccessible: boolean, callback: AsyncCallback<void>): void

设置指定应用对特定账号的访问权限。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| bundleName | string | 是 | 第三方应用的包名。 |
| isAccessible | boolean | 是 | 是否可访问。true表示允许访问，false表示禁止访问。 |
| callback | AsyncCallback<void> | 是 | 回调函数，如果设置成功，err为null，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name or bundleName. |
| 12300003 | Account not found. |
| 12400005 | The size of authorization list reaches the upper limit. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.setAppAccess('ZhangSan', 'com.example.accountjsdemo', true, (err: BusinessError) => {
    if (err) {
      console.error(`setAppAccess failed: code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('setAppAccess successfully');
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setAppAccess exception: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]setAppAccess9+

setAppAccess(name: string, bundleName: string, isAccessible: boolean): Promise<void>

设置指定应用对特定账号的数据访问权限。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| bundleName | string | 是 | 第三方应用的包名。 |
| isAccessible | boolean | 是 | 是否可访问。true表示允许访问，false表示禁止访问。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name or bundleName. |
| 12300003 | Account not found. |
| 12400005 | The size of authorization list reaches the upper limit. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.setAppAccess('ZhangSan', 'com.example.accountjsdemo', true).then(() => {
    console.info('setAppAccess successfully');
  }).catch((err: BusinessError) => {
    console.error(`setAppAccess failed: code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setAppAccess exception: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]checkAppAccess9+

checkAppAccess(name: string, bundleName: string, callback: AsyncCallback<boolean>): void

检查指定应用对特定账号的数据是否可访问。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| bundleName | string | 是 | 第三方应用的包名。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示指定应用可访问特定账号的数据；返回false表示不可访问。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name or bundleName. |
| 12300003 | Account not found. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.checkAppAccess('ZhangSan', 'com.example.accountjsdemo',
    (err: BusinessError, isAccessible: boolean) => {
      if (err) {
        console.error(`checkAppAccess failed, code is ${err.code}, message is ${err.message}`);
      } else {
        console.info('checkAppAccess successfully');
      }
    });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkAppAccess exception: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]checkAppAccess9+

checkAppAccess(name: string, bundleName: string): Promise<boolean>

检查指定应用对特定账号的数据是否可访问。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| bundleName | string | 是 | 第三方应用的包名。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象。返回true表示指定应用可访问特定账号的数据；返回false表示不可访问。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name or bundleName. |
| 12300003 | Account not found. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.checkAppAccess('ZhangSan', 'com.example.accountjsdemo').then((isAccessible: boolean) => {
    console.info('checkAppAccess successfully, isAccessible: ' + isAccessible);
  }).catch((err: BusinessError) => {
    console.error(`checkAppAccess failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkAppAccess exception: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]setDataSyncEnabled9+

setDataSyncEnabled(name: string, isEnabled: boolean, callback: AsyncCallback<void>): void

开启或禁止指定应用账号的数据同步功能。使用callback异步回调。

**需要权限：** ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| isEnabled | boolean | 是 | 是否开启数据同步。true表示开启数据同步，false表示关闭数据同步。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当开启或禁止成功时，err为null，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name. |
| 12300003 | Account not found. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
    appAccountManager.setDataSyncEnabled('ZhangSan', true, (err: BusinessError) => {
        console.error(`setDataSyncEnabled err: code is ${err.code}, message is ${err.message}`);
    });
} catch (e) {
    const err = e as BusinessError;
    console.error(`setDataSyncEnabled err: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]setDataSyncEnabled9+

setDataSyncEnabled(name: string, isEnabled: boolean): Promise<void>

开启或禁止指定应用账号的数据同步功能。使用Promise异步回调。

**需要权限：** ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| isEnabled | boolean | 是 | 是否开启数据同步。true表示开启数据同步，false表示关闭数据同步。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name. |
| 12300003 | Account not found. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
    appAccountManager.setDataSyncEnabled('ZhangSan', true).then(() => {
        console.info('setDataSyncEnabled Success');
    }).catch((err: BusinessError) => {
        console.error(`setDataSyncEnabled err: code is ${err.code}, message is ${err.message}`);
    });
} catch (e) {
    const err = e as BusinessError;
    console.error(`setDataSyncEnabled err: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]checkDataSyncEnabled9+

checkDataSyncEnabled(name: string, callback: AsyncCallback<boolean>): void

检查指定应用账号是否开启数据同步功能。使用callback异步回调。

**需要权限：** ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示指定应用账号已开启数据同步功能；返回false表示未开启。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name. |
| 12300003 | Account not found. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.checkDataSyncEnabled('ZhangSan', (err: BusinessError, isEnabled: boolean) => {
    if (err) {
      console.error(`checkDataSyncEnabled failed, err: code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('checkDataSyncEnabled successfully, isEnabled: ' + isEnabled);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkDataSyncEnabled err: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]checkDataSyncEnabled9+

checkDataSyncEnabled(name: string): Promise<boolean>

检查指定应用账号是否开启数据同步功能。使用Promise异步回调。

**需要权限：** ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象。返回true表示指定应用账号已开启数据同步功能；返回false表示未开启。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name. |
| 12300003 | Account not found. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.checkDataSyncEnabled('ZhangSan').then((isEnabled: boolean) => {
      console.info('checkDataSyncEnabled successfully, isEnabled: ' + isEnabled);
  }).catch((err: BusinessError) => {
    console.error(`checkDataSyncEnabled failed, err: code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkDataSyncEnabled err: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]setCredential9+

setCredential(name: string, credentialType: string, credential: string,callback: AsyncCallback<void>): void

设置指定应用账号的凭据。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| credentialType | string | 是 | 凭据类型。 |
| credential | string | 是 | 凭据取值。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当凭据设置成功时，err为null，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name, credentialType or credential. |
| 12300003 | Account not found. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.setCredential('ZhangSan', 'PIN_SIX', 'xxxxxx', (err: BusinessError) => {
    if (err) {
      console.error(`setCredential failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('setCredential successfully');
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setCredential exception: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]setCredential9+

setCredential(name: string, credentialType: string, credential: string): Promise<void>

设置指定应用账号的凭据。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| credentialType | string | 是 | 凭据类型。 |
| credential | string | 是 | 凭据取值。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name, credentialType or credential. |
| 12300003 | Account not found. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.setCredential('ZhangSan', 'PIN_SIX', 'xxxxxx').then(() => {
    console.info('setCredential successfully');
  }).catch((err: BusinessError) => {
    console.error(`setCredential failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setCredential exception: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]getCredential9+

getCredential(name: string, credentialType: string, callback: AsyncCallback<string>): void

获取指定应用账号的凭据。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| credentialType | string | 是 | 凭据类型。 |
| callback | AsyncCallback<string> | 是 | 回调函数。当获取凭据成功时，err为null，data为指定应用账号的凭据；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name or credentialType. |
| 12300003 | Account not found. |
| 12300102 | Credential not found. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getCredential('ZhangSan', 'PIN_SIX', (err: BusinessError, result: string) => {
    if (err) {
      console.error(`getCredential failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('getCredential successfully, result: ' + result);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getCredential err: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]getCredential9+

getCredential(name: string, credentialType: string): Promise<string>

获取指定应用账号的凭据。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| credentialType | string | 是 | 凭据类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | Promise对象，返回指定应用账号的凭据。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name or credentialType. |
| 12300003 | Account not found. |
| 12300102 | Credential not found. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getCredential('ZhangSan', 'PIN_SIX').then((credential: string) => {
    console.info('getCredential successfully, credential: ' + credential);
  }).catch((err: BusinessError) => {
    console.error(`getCredential failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getCredential exception: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]setCustomData9+

setCustomData(name: string, key: string, value: string, callback: AsyncCallback<void>): void

设置指定应用账号的自定义数据。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| key | string | 是 | 自定义数据的键名。 |
| value | string | 是 | 自定义数据的取值。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置自定义数据成功时，err为null，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name, key or value. |
| 12300003 | Account not found. |
| 12400003 | The number of custom data reaches the upper limit. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.setCustomData('ZhangSan', 'age', '12', (err: BusinessError) => {
    if (err) {
      console.error(`setCustomData failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('setCustomData successfully');
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setCustomData exception: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]setCustomData9+

setCustomData(name: string, key: string, value: string): Promise<void>

设置指定应用账号的自定义数据。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| key | string | 是 | 自定义数据的键名。 |
| value | string | 是 | 自定义数据的取值。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name, key or value. |
| 12300003 | Account not found. |
| 12400003 | The number of custom data reaches the upper limit. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.setCustomData('ZhangSan', 'age', '12').then(() => {
    console.info('setCustomData successfully');
  }).catch((err: BusinessError) => {
    console.error(`setCustomData failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setCustomData exception: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]getCustomData9+

getCustomData(name: string, key: string, callback: AsyncCallback<string>): void

根据指定键名获取特定应用账号的自定义数据。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| key | string | 是 | 自定义数据的键名。 |
| callback | AsyncCallback<string> | 是 | 回调函数。当获取成功时，err为null，data为自定义数据的取值；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name or key. |
| 12300003 | Account not found. |
| 12400002 | Custom data not found. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getCustomData('ZhangSan', 'age', (err: BusinessError, data: string) => {
    if (err) {
      console.error('getCustomData failed, error: ' + err);
    } else {
      console.info('getCustomData successfully, data: ' + data);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getCustomData exception: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]getCustomData9+

getCustomData(name: string, key: string): Promise<string>

根据指定键名获取特定应用账号的自定义数据。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| key | string | 是 | 自定义数据的键名。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | Promise对象，返回自定义数据的取值。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name or key. |
| 12300003 | Account not found. |
| 12400002 | Custom data not found. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getCustomData('ZhangSan', 'age').then((data: string) => {
    console.info('getCustomData successfully, data: ' + data);
  }).catch((err: BusinessError) => {
    console.error(`getCustomData failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getCustomData exception: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]getCustomDataSync9+

getCustomDataSync(name: string, key: string): string

根据指定键名获取特定应用账号的自定义数据。使用同步方式返回结果。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| key | string | 是 | 自定义数据的键名。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 自定义数据的取值。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name or key. |
| 12300003 | Account not found. |
| 12400002 | Custom data not found. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value = appAccountManager.getCustomDataSync('ZhangSan', 'age');
  console.info('getCustomDataSync successfully, value: ' + value);
} catch (e) {
  const err = e as BusinessError;
  console.error(`getCustomDataSync failed, code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]getAllAccounts9+

getAllAccounts(callback: AsyncCallback<Array<AppAccountInfo>>): void

获取所有可访问的应用账号信息。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[AppAccountInfo](#appaccountinfo)\>> | 是 | 回调函数。当查询成功时，err为null，data为获取到的应用账号信息列表；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getAllAccounts((err: BusinessError, data: appAccount.AppAccountInfo[]) => {
    if (err) {
      console.error(`getAllAccounts failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('getAllAccounts successfully');
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getAllAccounts exception: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]getAllAccounts9+

getAllAccounts(): Promise<Array<AppAccountInfo>>

获取所有可访问的应用账号信息。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<[AppAccountInfo](#appaccountinfo)\>> | Promise对象，返回全部应用已授权账号信息对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12300001 | System service exception. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getAllAccounts().then((data: appAccount.AppAccountInfo[]) => {
    console.info('getAllAccounts successfully');
  }).catch((err: BusinessError) => {
    console.error(`getAllAccounts failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getAllAccounts exception: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]getAccountsByOwner9+

getAccountsByOwner(owner: string, callback: AsyncCallback<Array<AppAccountInfo>>): void

根据应用账号所有者获取调用方可访问的应用账号列表。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| owner | string | 是 | 应用账号所有者的包名。 |
| callback | AsyncCallback<Array<[AppAccountInfo](#appaccountinfo)\>> | 是 | 回调函数。如果获取成功，err为null，data为获取到的应用账号列表；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid owner. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getAccountsByOwner('com.example.accountjsdemo2',
    (err: BusinessError, data: appAccount.AppAccountInfo[]) => {
      if (err) {
        console.error(`getAccountsByOwner failed, code is ${err.code}, message is ${err.message}`);
      } else {
        console.info('getAccountsByOwner successfully, data:' + JSON.stringify(data));
      }
    });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getAccountsByOwner exception:code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]getAccountsByOwner9+

getAccountsByOwner(owner: string): Promise<Array<AppAccountInfo>>

根据应用账号所有者获取调用方可访问的应用账号列表。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| owner | string | 是 | 应用账号所有者的包名。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<[AppAccountInfo](#appaccountinfo)\>> | Promise对象，返回获取到的应用账号列表。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid owner. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getAccountsByOwner('com.example.accountjsdemo2').then((
    data: appAccount.AppAccountInfo[]) => {
    console.info('getAccountsByOwner successfully, data: ' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error(`getAccountsByOwner failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getAccountsByOwner exception: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]on('accountChange')9+

on(type: 'accountChange', owners: Array<string>, callback: Callback<Array<AppAccountInfo>>): void

订阅指定应用的账号信息变更事件。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | 'accountChange' | 是 | 事件回调类型，支持的事件为'accountChange'，当目标应用更新账号信息时，触发该事件。 |
| owners | Array<string> | 是 | 应用账号所有者的包名列表。 |
| callback | Callback<Array<[AppAccountInfo](#appaccountinfo)\>> | 是 | 需要注册的回调函数，返回信息为发生变更的应用账号列表。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid type or owners. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

function changeOnCallback(data: appAccount.AppAccountInfo[]): void {
  console.info('receive change data:' + JSON.stringify(data));
}

try {
  appAccountManager.on('accountChange', ['com.example.actsaccounttest'], changeOnCallback);
} catch (e) {
  const err = e as BusinessError;
  console.error(`on accountChange failed, code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]off('accountChange')9+

off(type: 'accountChange', callback?: Callback<Array<AppAccountInfo>>): void

取消订阅账号信息变更事件。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | 'accountChange' | 是 | 事件回调类型，支持的事件为'accountChange'，当账号所有者更新账号信息时，触发该事件。 |
| callback | Callback<Array<[AppAccountInfo](#appaccountinfo)\>> | 否 | 需要注销的回调函数，默认为空，表示取消该类型事件所有的回调。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid type. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

function changeOnCallback(data: appAccount.AppAccountInfo[]): void {
  console.info('receive change data:' + JSON.stringify(data));
}

try {
  appAccountManager.on('accountChange', ['com.example.actsaccounttest'], changeOnCallback);
} catch (e) {
  const err = e as BusinessError;
  console.error(`on accountChange failed, code is ${err.code}, message is ${err.message}`);
}
try {
  appAccountManager.off('accountChange', changeOnCallback);
} catch (e) {
  const err = e as BusinessError;
  console.error(`off accountChange failed, code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]auth9+

auth(name: string, owner: string, authType: string, callback: AuthCallback): void

对应用账号进行鉴权以获取授权令牌。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| owner | string | 是 | 应用账号所有者的包名。 |
| authType | string | 是 | 鉴权类型。 |
| callback | [AuthCallback](#authcallback9) | 是 | 回调对象，返回鉴权结果。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name, owner or authType. |
| 12300003 | Account not found. |
| 12300010 | Account service busy. |
| 12300113 | Authenticator service not found. |
| 12300114 | Authenticator service exception. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { Want, common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext

  onResultCallback(code: number, authResult?: appAccount.AuthResult): void {
    console.info('resultCode: ' + code);
    console.info('authResult: ' + JSON.stringify(authResult));
  }

  onRequestRedirectedCallback(request: Want): void {
    let wantInfo: Want = {
      deviceId: '',
      bundleName: 'com.example.accountjsdemo',
      action: 'ohos.want.action.viewData',
      entities: ['entity.system.default'],
    }
    this.context.startAbility(wantInfo).then(() => {
      console.info('startAbility successfully');
    }).catch((err: BusinessError) => {
      console.error(`startAbility err: code is ${err.code}, message is ${err.message}`);
    })
  }

  aboutToAppear(): void {
    try {
      appAccountManager.auth('LiSi', 'com.example.accountjsdemo', 'getSocialData', {
        onResult: this.onResultCallback,
        onRequestRedirected: this.onRequestRedirectedCallback
      });
    } catch (e) {
      const err = e as BusinessError;
      console.error(`auth exception: code is ${err.code}, message is ${err.message}`);
    }
  }

  build() {}
}
```

#### \[h2\]auth9+

auth(name: string, owner: string, authType: string, options: Record<string, Object>, callback: AuthCallback): void

对应用账号进行鉴权以获取授权令牌。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| owner | string | 是 | 应用账号所有者的包名。 |
| authType | string | 是 | 鉴权类型。 |
| options | Record<string, Object> | 是 | 鉴权所需的可选项。 |
| callback | [AuthCallback](#authcallback9) | 是 | 回调对象，返回鉴权结果。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name, owner, authType or options. |
| 12300003 | Account not found. |
| 12300010 | Account service busy. |
| 12300113 | Authenticator service not found. |
| 12300114 | Authenticator service exception. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { Want, common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext

  onResultCallback(code: number, authResult?: appAccount.AuthResult): void {
    console.info('resultCode: ' + code);
    console.info('authResult: ' + JSON.stringify(authResult));
  }

  onRequestRedirectedCallback(request: Want): void {
    let wantInfo: Want = {
      deviceId: '',
      bundleName: 'com.example.accountjsdemo',
      action: 'ohos.want.action.viewData',
      entities: ['entity.system.default'],
    }
    this.context.startAbility(wantInfo).then(() => {
      console.info('startAbility successfully');
    }).catch((err: BusinessError) => {
      console.error(`startAbility err: code is ${err.code}, message is ${err.message}`);
    })
  }

  aboutToAppear(): void {
    let options: Record<string, Object> = {
      'password': 'xxxx',
    };
    try {
      appAccountManager.auth('LiSi', 'com.example.accountjsdemo', 'getSocialData', options, {
        onResult: this.onResultCallback,
        onRequestRedirected: this.onRequestRedirectedCallback
      });
    } catch (e) {
      const err = e as BusinessError;
      console.error(`auth exception: code is ${err.code}, message is ${err.message}`);
    }
  }

  build() {}
}
```

#### \[h2\]getAuthToken9+

getAuthToken(name: string, owner: string, authType: string, callback: AsyncCallback<string>): void

获取指定应用账号的特定鉴权类型的授权令牌。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| owner | string | 是 | 应用账号所有者的包名。 |
| authType | string | 是 | 鉴权类型。 |
| callback | AsyncCallback<string> | 是 | 回调函数。当获取成功时，err为null，data为授权令牌值；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name, owner or authType. |
| 12300003 | Account not found. |
| 12300107 | AuthType not found. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getAuthToken('LiSi', 'com.example.accountjsdemo', 'getSocialData',
    (err: BusinessError, token: string) => {
      if (err) {
        console.error(`getAuthToken failed, code is ${err.code}, message is ${err.message}`);
      } else {
        console.info('getAuthToken successfully, token: ' + token);
      }
    });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getAuthToken exception: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]getAuthToken9+

getAuthToken(name: string, owner: string, authType: string): Promise<string>

获取指定应用账号的特定鉴权类型的授权令牌。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| owner | string | 是 | 应用账号所有者的包名。 |
| authType | string | 是 | 鉴权类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | Promise对象，返回授权令牌。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name, owner or authType. |
| 12300003 | Account not found. |
| 12300107 | AuthType not found. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getAuthToken('LiSi', 'com.example.accountjsdemo', 'getSocialData').then((token: string) => {
    console.info('getAuthToken successfully, token: ' + token);
  }).catch((err: BusinessError) => {
    console.error(`getAuthToken failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getAuthToken exception: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]setAuthToken9+

setAuthToken(name: string, authType: string, token: string, callback: AsyncCallback<void>): void

为指定应用账号设置特定鉴权类型的授权令牌。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| authType | string | 是 | 鉴权类型。 |
| token | string | 是 | 授权令牌。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置成功时，err为null；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name, authType or token. |
| 12300003 | Account not found. |
| 12400004 | The number of tokens reaches the upper limit. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.setAuthToken('LiSi', 'getSocialData', 'xxxx', (err: BusinessError) => {
    if (err) {
      console.error(`setAuthToken failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('setAuthToken successfully');
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setAuthToken exception: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]setAuthToken9+

setAuthToken(name: string, authType: string, token: string): Promise<void>

为指定应用账号设置特定鉴权类型的授权令牌。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| authType | string | 是 | 鉴权类型。 |
| token | string | 是 | 授权令牌。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name, authType or token. |
| 12300003 | Account not found. |
| 12400004 | The number of tokens reaches the upper limit. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.setAuthToken('LiSi', 'getSocialData', 'xxxx').then(() => {
    console.info('setAuthToken successfully');
  }).catch((err: BusinessError) => {
    console.error(`setAuthToken failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setAuthToken exception: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]deleteAuthToken9+

deleteAuthToken(name: string, owner: string, authType: string, token: string, callback: AsyncCallback<void>): void

删除指定应用账号的特定鉴权类型的授权令牌。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| owner | string | 是 | 应用账号所有者的包名。 |
| authType | string | 是 | 鉴权类型。 |
| token | string | 是 | 授权令牌。如果授权令牌不存在，则不执行任何操作。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当删除成功时，err为null；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name, owner, authType or token. |
| 12300003 | Account not found. |
| 12300107 | AuthType not found. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.deleteAuthToken('LiSi', 'com.example.accountjsdemo', 'getSocialData', 'xxxxx',
    (err: BusinessError) => {
      if (err) {
        console.error(`deleteAuthToken failed, code is ${err.code}, message is ${err.message}`);
      } else {
        console.info('deleteAuthToken successfully');
      }
    });
} catch (e) {
  const err = e as BusinessError;
  console.error(`deleteAuthToken exception: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]deleteAuthToken9+

deleteAuthToken(name: string, owner: string, authType: string, token: string): Promise<void>

删除指定应用账号的特定鉴权类型的授权令牌。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| owner | string | 是 | 应用账号所有者的包名。 |
| authType | string | 是 | 鉴权类型。 |
| token | string | 是 | 授权令牌。如果授权令牌不存在，则不执行任何操作。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name, owner, authType or token. |
| 12300003 | Account not found. |
| 12300107 | AuthType not found. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.deleteAuthToken('LiSi', 'com.example.accountjsdemo', 'getSocialData', 'xxxxx').then(() => {
    console.info('deleteAuthToken successfully');
  }).catch((err: BusinessError) => {
    console.error(`deleteAuthToken failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`deleteAuthToken exception: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]setAuthTokenVisibility9+

setAuthTokenVisibility(name: string, authType: string, bundleName: string, isVisible: boolean, callback: AsyncCallback<void>): void

设置指定账号的特定鉴权类型的授权令牌对指定应用的可见性。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| authType | string | 是 | 鉴权类型。 |
| bundleName | string | 是 | 被设置可见性的应用包名。 |
| isVisible | boolean | 是 | 是否可见。true表示可见，false表示不可见。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置成功时，err为null；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name, authType or bundleName. |
| 12300003 | Account not found. |
| 12300107 | AuthType not found. |
| 12400005 | The size of authorization list reaches the upper limit. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.setAuthTokenVisibility('LiSi', 'getSocialData', 'com.example.accountjsdemo', true,
    (err: BusinessError) => {
      if (err) {
        console.error(`setAuthTokenVisibility failed, code is ${err.code}, message is ${err.message}`);
      } else {
        console.info('setAuthTokenVisibility successfully');
      }
    });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setAuthTokenVisibility exception: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]setAuthTokenVisibility9+

setAuthTokenVisibility(name: string, authType: string, bundleName: string, isVisible: boolean): Promise<void>

设置指定账号的特定鉴权类型的授权令牌对指定应用的可见性。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| authType | string | 是 | 鉴权类型。 |
| bundleName | string | 是 | 被设置可见性的应用包名。 |
| isVisible | boolean | 是 | 是否可见。true表示可见，false表示不可见。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name, authType or bundleName. |
| 12300003 | Account not found. |
| 12300107 | AuthType not found. |
| 12400005 | The size of authorization list reaches the upper limit. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.setAuthTokenVisibility('LiSi', 'getSocialData', 'com.example.accountjsdemo', true).then(() => {
    console.info('setAuthTokenVisibility successfully');
  }).catch((err: BusinessError) => {
    console.error(`setAuthTokenVisibility failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setAuthTokenVisibility exception: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]checkAuthTokenVisibility9+

checkAuthTokenVisibility(name: string, authType: string, bundleName: string, callback: AsyncCallback<boolean>): void

检查指定应用账号的特定鉴权类型的授权令牌对指定应用的可见性。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| authType | string | 是 | 鉴权类型。 |
| bundleName | string | 是 | 检查可见性的应用包名。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当检查成功时，err为null，data为true表示可见，data为false表示不可见；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name, authType or bundleName. |
| 12300003 | Account not found. |
| 12300107 | AuthType not found. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.checkAuthTokenVisibility('LiSi', 'getSocialData', 'com.example.accountjsdemo',
    (err: BusinessError, isVisible: boolean) => {
      if (err) {
        console.error(`checkAuthTokenVisibility failed, code is ${err.code}, message is ${err.message}`);
      } else {
        console.info('checkAuthTokenVisibility successfully, isVisible: ' + isVisible);
      }
    });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkAuthTokenVisibility exception: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]checkAuthTokenVisibility9+

checkAuthTokenVisibility(name: string, authType: string, bundleName: string): Promise<boolean>

检查指定应用账号的特定鉴权类型的授权令牌对指定应用的可见性。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| authType | string | 是 | 鉴权类型。 |
| bundleName | string | 是 | 用于检查可见性的应用包名。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象。返回true表示授权令牌对指定应用的可见，返回false表示不可见。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name, authType or bundleName. |
| 12300003 | Account not found. |
| 12300107 | AuthType not found. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.checkAuthTokenVisibility('LiSi', 'getSocialData', 'com.example.accountjsdemo').then((
    isVisible: boolean) => {
    console.info('checkAuthTokenVisibility successfully, isVisible: ' + isVisible);
  }).catch((err: BusinessError) => {
    console.error(`checkAuthTokenVisibility failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkAuthTokenVisibility exception: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]getAllAuthTokens9+

getAllAuthTokens(name: string, owner: string, callback: AsyncCallback<Array<AuthTokenInfo>>): void

获取指定账号对调用方可见的所有授权令牌。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| owner | string | 是 | 应用账号所有者的包名。 |
| callback | AsyncCallback<Array<[AuthTokenInfo](#authtokeninfo9)\>> | 是 | 回调函数。当获取成功时，err为null，data为授权令牌数组；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name or owner. |
| 12300003 | Account not found. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getAllAuthTokens('LiSi', 'com.example.accountjsdemo',
    (err: BusinessError, tokenArr: appAccount.AuthTokenInfo[]) => {
      if (err) {
        console.error(`getAllAuthTokens failed, code is ${err.code}, message is ${err.message}`);
      } else {
        console.info('getAllAuthTokens successfully, tokenArr: ' + tokenArr);
      }
    });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getAllAuthTokens exception: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]getAllAuthTokens9+

getAllAuthTokens(name: string, owner: string): Promise<Array<AuthTokenInfo>>

获取指定账号对调用方可见的所有授权令牌。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| owner | string | 是 | 应用账号所有者的包名。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<[AuthTokenInfo](#authtokeninfo9)\>> | Promise对象，返回授权令牌数组。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name or owner. |
| 12300003 | Account not found. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getAllAuthTokens('LiSi', 'com.example.accountjsdemo').then((
    tokenArr: appAccount.AuthTokenInfo[]) => {
    console.info('getAllAuthTokens successfully, tokenArr: ' + JSON.stringify(tokenArr));
  }).catch((err: BusinessError) => {
    console.error(`getAllAuthTokens failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getAllAuthTokens exception: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]getAuthList9+

getAuthList(name: string, authType: string, callback: AsyncCallback<Array<string>>): void

获取指定应用账号的特定鉴权类型的授权列表，即被授权的包名数组（令牌的授权列表通过[setAuthTokenVisibility](#setauthtokenvisibility9)来设置）。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| authType | string | 是 | 鉴权类型。 |
| callback | AsyncCallback<Array<string>> | 是 | 回调函数。当获取成功时，err为null，data为被授权的包名数组；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name or authType. |
| 12300003 | Account not found. |
| 12300107 | AuthType not found. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getAuthList('LiSi', 'getSocialData', (err: BusinessError, authList: string[]) => {
    if (err) {
      console.error(`getAuthList failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('getAuthList successfully, authList: ' + authList);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getAuthList exception: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]getAuthList9+

getAuthList(name: string, authType: string): Promise<Array<string>>

获取指定应用账号的特定鉴权类型的授权列表，即被授权的包名数组（令牌的授权列表通过[setAuthTokenVisibility](#setauthtokenvisibility9)来设置）。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| authType | string | 是 | 鉴权类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<string>> | Promise对象，返回被授权的包名数组。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name or authType. |
| 12300003 | Account not found. |
| 12300107 | AuthType not found. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getAuthList('LiSi', 'getSocialData').then((authList: string[]) => {
    console.info('getAuthList successfully, authList: ' + authList);
  }).catch((err: BusinessError) => {
    console.error(`getAuthList failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getAuthList exception: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]getAuthCallback9+

getAuthCallback(sessionId: string, callback: AsyncCallback<AuthCallback>): void

获取鉴权会话的认证器回调对象。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| sessionId | string | 是 | 鉴权会话的标识。 |
| callback | AsyncCallback<[AuthCallback](#authcallback9)\> | 是 | 回调函数。当获取成功时，err为null，data为鉴权会话的认证器回调对象；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid sessionId. |
| 12300108 | Session not found. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { Want, UIAbility, AbilityConstant } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, param: AbilityConstant.LaunchParam) { // ability 生命周期函数
    let sessionId: string = want.parameters![appAccount.Constants.KEY_SESSION_ID] as string;
    try {
      appAccountManager.getAuthCallback(sessionId, (err: BusinessError, callback: appAccount.AuthCallback) => {
        if (err != null) {
          console.error(`getAuthCallback err: code is ${err.code}, message is ${err.message}`);
          return;
        }
        let result: appAccount.AuthResult = {
          account: {
            name: 'Lisi',
            owner: 'com.example.accountjsdemo',
          },
          tokenInfo: {
            token: 'xxxxxx',
            authType: 'getSocialData'
          }
        };
        callback.onResult(0, result);
      });
    } catch (e) {
      const err = e as BusinessError;
      console.error(`getAuthCallback exception: code is ${err.code}, message is ${err.message}`);
    }
  }
}
```

#### \[h2\]getAuthCallback9+

getAuthCallback(sessionId: string): Promise<AuthCallback>

获取鉴权会话的认证器回调对象。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| sessionId | string | 是 | 鉴权会话的标识。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[AuthCallback](#authcallback9)\> | Promise对象，返回鉴权会话的认证器回调对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid sessionId. |
| 12300108 | Session not found. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { Want, UIAbility, AbilityConstant } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, param: AbilityConstant.LaunchParam) { // ability 生命周期函数
    let sessionId: string = want.parameters![appAccount.Constants.KEY_SESSION_ID] as string;
    try {
      appAccountManager.getAuthCallback(sessionId).then((callback: appAccount.AuthCallback) => {
      let result: appAccount.AuthResult = {
        account: {
          name: 'Lisi',
          owner: 'com.example.accountjsdemo',
        },
        tokenInfo: {
          token: 'xxxxxx',
          authType: 'getSocialData'
        }
      };
      callback.onResult(0, result);
      }).catch((err: BusinessError) => {
        console.error(`getAuthCallback err: code is ${err.code}, message is ${err.message}`);
      });
    } catch (e) {
      const err = e as BusinessError;
      console.error(`getAuthCallback exception: code is ${err.code}, message is ${err.message}`);
    }
  }
}
```

#### \[h2\]queryAuthenticatorInfo9+

queryAuthenticatorInfo(owner: string, callback: AsyncCallback<AuthenticatorInfo>): void

获取指定应用的认证器信息。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| owner | string | 是 | 应用账号所有者的包名。 |
| callback | AsyncCallback<[AuthenticatorInfo](#authenticatorinfo8)\> | 是 | 回调函数。当获取成功时，err为null，data为认证器信息对象；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid owner. |
| 12300113 | Authenticator service not found. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.queryAuthenticatorInfo('com.example.accountjsdemo',
    (err: BusinessError, info: appAccount.AuthenticatorInfo) => {
      if (err) {
        console.error(`queryAuthenticatorInfo failed, code is ${err.code}, message is ${err.message}`);
      } else {
        console.info('queryAuthenticatorInfo successfully, info: ' + JSON.stringify(info));
      }
    });
} catch (e) {
  const err = e as BusinessError;
  console.error(`queryAuthenticatorInfo exception: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]queryAuthenticatorInfo9+

queryAuthenticatorInfo(owner: string): Promise<AuthenticatorInfo>

获取指定应用的认证器信息。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| owner | string | 是 | 应用账号所有者的包名。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[AuthenticatorInfo](#authenticatorinfo8)\> | Promise对象，返回指定应用的认证器信息对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid owner. |
| 12300113 | Authenticator service not found. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.queryAuthenticatorInfo('com.example.accountjsdemo').then((
    info: appAccount.AuthenticatorInfo) => {
    console.info('queryAuthenticatorInfo successfully, info: ' + JSON.stringify(info));
  }).catch((err: BusinessError) => {
    console.error(`queryAuthenticatorInfo failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`queryAuthenticatorInfo exception: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]checkAccountLabels9+

checkAccountLabels(name: string, owner: string, labels: Array<string>, callback: AsyncCallback<boolean>): void

检查指定应用账号是否满足特定的标签集合。使用callback异步回调。该方法依赖目标应用的认证器提供标签检查的能力。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| owner | string | 是 | 应用账号所有者的包名。 |
| labels | Array<string> | 是 | 标签数组。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当检查成功时，err为null，data为true表示满足特定的标签集合，data为false表示不满足；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name, owner or labels. |
| 12300003 | Account not found. |
| 12300010 | Account service busy. |
| 12300113 | Authenticator service not found. |
| 12300114 | Authenticator service exception. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let labels = ['student'];
try {
  appAccountManager.checkAccountLabels('zhangsan', 'com.example.accountjsdemo', labels,
    (err: BusinessError, hasAllLabels: boolean) => {
      if (err) {
        console.error(`checkAccountLabels failed, code is ${err.code}, message is ${err.message}`);
      } else {
        console.info('checkAccountLabels successfully, hasAllLabels: ' + hasAllLabels);
      }
    });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkAccountLabels exception: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]checkAccountLabels9+

checkAccountLabels(name: string, owner: string, labels: Array<string>): Promise<boolean>

检查指定应用账号是否满足特定的标签集合。使用Promise异步回调。该方法依赖目标应用的认证器提供标签检查的能力。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| owner | string | 是 | 应用账号所有者的包名。 |
| labels | Array<string> | 是 | 标签数组。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象。返回true表示指定账号满足特定的标签集合，返回false表示不满足。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name, owner or labels. |
| 12300003 | Account not found. |
| 12300010 | Account service busy. |
| 12300113 | Authenticator service not found. |
| 12300114 | Authenticator service exception. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let labels = ['student'];
try {
  appAccountManager.checkAccountLabels('zhangsan', 'com.example.accountjsdemo', labels).then((
    hasAllLabels: boolean) => {
    console.info('checkAccountLabels successfully: ' + hasAllLabels);
  }).catch((err: BusinessError) => {
    console.error(`checkAccountLabels failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkAccountLabels exception: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]deleteCredential9+

deleteCredential(name: string, credentialType: string, callback: AsyncCallback<void>): void

删除指定应用账号的特定类型的凭据信息。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| credentialType | string | 是 | 凭据类型。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当删除成功时，err为null；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name or credentialType. |
| 12300003 | Account not found. |
| 12300102 | Credential not found. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.deleteCredential('zhangsan', 'PIN_SIX', (err: BusinessError) => {
    if (err) {
      console.error(`deleteCredential failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('deleteCredential successfully');
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`deleteCredential exception: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]deleteCredential9+

deleteCredential(name: string, credentialType: string): Promise<void>

删除指定应用账号的特定类型的凭据信息。使用Promise异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| credentialType | string | 是 | 凭据类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name or credentialType. |
| 12300003 | Account not found. |
| 12300102 | Credential not found. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.deleteCredential('zhangsan', 'PIN_SIX').then(() => {
    console.info('deleteCredential successfully');
  }).catch((err: BusinessError) => {
    console.error(`deleteCredential failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`deleteCredential exception: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]selectAccountsByOptions9+

selectAccountsByOptions(options: SelectAccountsOptions, callback: AsyncCallback<Array<AppAccountInfo>>): void

根据选项选择调用方可访问的账号列表。使用callback异步回调。如果选项中包含标签约束，则该方法依赖目标应用的认证器提供标签检查的能力。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [SelectAccountsOptions](#selectaccountsoptions9) | 是 | 选择账号的选项。 |
| callback | AsyncCallback<Array<[AppAccountInfo](#appaccountinfo)\>> | 是 | 回调函数。当根据选项选择请求方可访问的账号列表时，err为null，data为可访问的账号信息对象；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid options. |
| 12300010 | Account service busy. |
| 12300114 | Authenticator service exception. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let options: appAccount.SelectAccountsOptions = {
  allowedOwners: ['com.example.accountjsdemo'],
  requiredLabels: ['student']
};
try {
  appAccountManager.selectAccountsByOptions(options,
    (err: BusinessError, accountArr: appAccount.AppAccountInfo[]) => {
      if (err) {
        console.error(`selectAccountsByOptions failed, code is ${err.code}, message is ${err.message}`);
      } else {
        console.info('selectAccountsByOptions successfully, accountArr: ' + JSON.stringify(accountArr));
      }
    });
} catch (e) {
  const err = e as BusinessError;
  console.error(`selectAccountsByOptions exception: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]selectAccountsByOptions9+

selectAccountsByOptions(options: SelectAccountsOptions): Promise<Array<AppAccountInfo>>

根据选项选择调用方可访问的账号列表。使用Promise异步回调。如果选项中包含标签约束，则该方法依赖目标应用的认证器提供标签检查的能力。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [SelectAccountsOptions](#selectaccountsoptions9) | 是 | 选择账号的选项。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<[AppAccountInfo](#appaccountinfo)\>> | Promise对象，返回调用方可访问的账号列表。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid options. |
| 12300010 | Account service busy. |
| 12300114 | Authenticator service exception. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let options: appAccount.SelectAccountsOptions = {
  allowedOwners: ['com.example.accountjsdemo']
};
try {
  appAccountManager.selectAccountsByOptions(options).then((accountArr: appAccount.AppAccountInfo[]) => {
    console.info('selectAccountsByOptions successfully, accountArr: ' + JSON.stringify(accountArr));
  }).catch((err: BusinessError) => {
    console.error(`selectAccountsByOptions failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`selectAccountsByOptions exception: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]verifyCredential9+

verifyCredential(name: string, owner: string, callback: AuthCallback): void

验证指定账号的凭据。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| owner | string | 是 | 应用账号所有者的包名。 |
| callback | [AuthCallback](#authcallback9) | 是 | 回调函数，返回验证结果。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name or owner. |
| 12300003 | Account not found. |
| 12300010 | Account service busy. |
| 12300113 | Authenticator service not found. |
| 12300114 | Authenticator service exception. |

**示例：**

```ts
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.verifyCredential('zhangsan', 'com.example.accountjsdemo', {
    onResult: (resultCode: number, result?: appAccount.AuthResult) => {
      console.info('verifyCredential onResult, resultCode: ' + JSON.stringify(resultCode));
      console.info('verifyCredential onResult, result: ' + JSON.stringify(result));
    },
    onRequestRedirected: (request: Want) => {
      console.info('verifyCredential onRequestRedirected, request: ' + JSON.stringify(request));
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`verifyCredential err: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]verifyCredential9+

verifyCredential(name: string, owner: string, options: VerifyCredentialOptions, callback: AuthCallback): void

验证用户凭据。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| owner | string | 是 | 应用账号所有者的包名。 |
| options | [VerifyCredentialOptions](#verifycredentialoptions9) | 是 | 验证凭据的选项。 |
| callback | [AuthCallback](#authcallback9) | 是 | 回调函数，返回验证结果。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid name, owner or options. |
| 12300003 | Account not found. |
| 12300010 | Account service busy. |
| 12300113 | Authenticator service not found. |
| 12300114 | Authenticator service exception. |

**示例：**

```ts
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let options: appAccount.VerifyCredentialOptions = {
  credentialType: 'pin',
  credential: '123456'
};
try {
  appAccountManager.verifyCredential('zhangsan', 'com.example.accountjsdemo', options, {
    onResult: (resultCode: number, result?: appAccount.AuthResult) => {
      console.info('verifyCredential onResult, resultCode: ' + JSON.stringify(resultCode));
      console.info('verifyCredential onResult, result: ' + JSON.stringify(result));
    },
    onRequestRedirected: (request: Want) => {
      console.info('verifyCredential onRequestRedirected, request: ' + JSON.stringify(request));
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`verifyCredential err: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]setAuthenticatorProperties9+

setAuthenticatorProperties(owner: string, callback: AuthCallback): void

设置指定应用的认证器属性。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| owner | string | 是 | 认证器的所有者的包名。 |
| callback | [AuthCallback](#authcallback9) | 是 | 回调函数，返回设置属性的结果。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid owner. |
| 12300010 | Account service busy. |
| 12300113 | Authenticator service not found. |
| 12300114 | Authenticator service exception. |

**示例：**

```ts
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.setAuthenticatorProperties('com.example.accountjsdemo', {
    onResult: (resultCode: number, result?: appAccount.AuthResult) => {
      console.info('setAuthenticatorProperties onResult, resultCode: ' + JSON.stringify(resultCode));
      console.info('setAuthenticatorProperties onResult, result: ' + JSON.stringify(result));
    },
    onRequestRedirected: (request: Want) => {
      console.info('setAuthenticatorProperties onRequestRedirected, request: ' + JSON.stringify(request));
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setAuthenticatorProperties err: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]setAuthenticatorProperties9+

setAuthenticatorProperties(owner: string, options: SetPropertiesOptions, callback: AuthCallback): void

设置认证器属性。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| owner | string | 是 | 认证器的所有者的包名。 |
| options | [SetPropertiesOptions](#setpropertiesoptions9) | 是 | 设置属性的选项。 |
| callback | [AuthCallback](#authcallback9) | 是 | 认证器回调，返回设置属性的结果。 |

**错误码：**

以下错误码的详细介绍请参见[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | System service exception. |
| 12300002 | Invalid owner or options. |
| 12300010 | Account service busy. |
| 12300113 | Authenticator service not found. |
| 12300114 | Authenticator service exception. |

**示例：**

```ts
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let options: appAccount.SetPropertiesOptions = {
  properties: { prop1: 'value1' }
};
try {
  appAccountManager.setAuthenticatorProperties('com.example.accountjsdemo', options, {
    onResult: (resultCode: number, result?: appAccount.AuthResult) => {
      console.info('setAuthenticatorProperties onResult, resultCode: ' + JSON.stringify(resultCode));
      console.info('setAuthenticatorProperties onResult, result: ' + JSON.stringify(result));
    },
    onRequestRedirected: (request: Want) => {
      console.info('setAuthenticatorProperties onRequestRedirected, request: ' + JSON.stringify(request));
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setAuthenticatorProperties err: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]addAccount(deprecated)

addAccount(name: string, callback: AsyncCallback<void>): void

根据账号名添加应用账号。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/MUGbbx3eQ3yZteL3wZZs3w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=CCEE4A967C4ABD8894179E1AF6B0C05FDC4BB5AFA859F23FDA6DC7907A21EF86)

从API version 7开始支持，从API version 9开始废弃。建议使用[createAccount](#createaccount9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当创建成功时，err为null，否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.addAccount('WangWu', (err: BusinessError) => {
  console.error(`addAccount err: code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]addAccount(deprecated)

addAccount(name: string, extraInfo: string, callback: AsyncCallback<void>): void

根据账号名和额外信息添加应用账号。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/tq9EmwcaTr6_JNQxD2s4RA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=95955524A43570432FC6E29BE32BE983C6E2F016F9F2218AFD8DD495EDA7B819)

从API version 7开始支持，从API version 9开始废弃。建议使用[createAccount](#createaccount9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| extraInfo | string | 是 | 额外信息(能转换string类型的其它信息)，额外信息不能是应用账号的敏感信息（如应用账号密码、token等）。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当创建成功时，err为null，否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.addAccount('LiSi', 'token101', (err: BusinessError) => {
  console.error(`addAccount err: code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]addAccount(deprecated)

addAccount(name: string, extraInfo?: string): Promise<void>

根据账号名和额外信息添加应用账号。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/N0USlAGeQjWgHqRhjcyaCQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=4E777B879C49571A7B6689E8D29506335BFE5A8F0931FDAEA5691EDB9ACF047A)

从API version 7开始支持，从API version 9开始废弃。建议使用[createAccount](#createaccount9-2)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| extraInfo | string | 否 | 额外信息(能转换string类型的其它信息)，额外信息不能是应用账号的敏感信息（如应用账号密码、token等），默认为空，表示创建的该账号无额外信息需要添加。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.addAccount('LiSi', 'token101').then(()=> {
  console.info('addAccount Success');
}).catch((err: BusinessError) => {
  console.error(`addAccount err: code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]addAccountImplicitly(deprecated)

addAccountImplicitly(owner: string, authType: string, options: {\[key: string\]: any;}, callback: AuthenticatorCallback): void

根据指定的账号所有者隐式地添加应用账号。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/WqlrwMMxRT6TjNSbYFOlGw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=192992E3BF3B2F0EBFFEABB44692A07F579F0C2675E8B2BE241E27921DACA531)

从API version 8开始支持，从API version 9开始废弃。建议使用[createAccountImplicitly](#createaccountimplicitly9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| owner | string | 是 | 应用账号所有者的包名。 |
| authType | string | 是 | 鉴权类型。鉴权类型为自定义。 |
| options | {\[key: string\]: any} | 是 | 鉴权所需要的可选项。可选项可根据自己需要设置。 |
| callback | [AuthenticatorCallback](#authenticatorcallbackdeprecated) | 是 | 认证器回调对象，返回添加结果。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { Want, common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext

  onResultCallback(code: number, result: Record<string, Object>): void {
    console.info('resultCode: ' + code);
    console.info('result: ' + JSON.stringify(result));
  }

  onRequestRedirectedCallback(request: Want): void {
    let wantInfo: Want = {
      deviceId: '',
      bundleName: 'com.example.accountjsdemo',
      action: 'ohos.want.action.viewData',
      entities: ['entity.system.default'],
    }
    this.context.startAbility(wantInfo).then(() => {
      console.info('startAbility successfully');
    }).catch((err: BusinessError) => {
      console.error(`startAbility err: code is ${err.code}, message is ${err.message}`);
    })
  }

  aboutToAppear(): void {
    appAccountManager.addAccountImplicitly('com.example.accountjsdemo', 'getSocialData', {}, {
      onResult: this.onResultCallback,
      onRequestRedirected: this.onRequestRedirectedCallback
    });
  }

  build() {}
}
```

#### \[h2\]deleteAccount(deprecated)

deleteAccount(name: string, callback: AsyncCallback<void>): void

删除应用账号。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/XUaug5DOR0S4vDx-knC4_g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=A2C5EAFC410E2F72D8DAB4CC01B6DE9C96234F1982543E4CD578E65E070E83FD)

从API version 7开始支持，从API version 9开始废弃。建议使用[removeAccount](#removeaccount9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当删除成功时，err为null，否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.deleteAccount('ZhaoLiu', (err: BusinessError) => {
  console.error(`deleteAccount err: code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]deleteAccount(deprecated)

deleteAccount(name: string): Promise<void>

删除应用账号。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/EmIX3YRiQyG_Hlsxz2YFQw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=4C70746A4C913E74F7172ACA64E163C5A5CD7A7EE1715349E8F1A6380CEF408C)

从API version 7开始支持，从API version 9开始废弃。建议使用[removeAccount](#removeaccount9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.deleteAccount('ZhaoLiu').then(() => {
  console.info('deleteAccount Success');
}).catch((err: BusinessError) => {
  console.error(`deleteAccount err: code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]disableAppAccess(deprecated)

disableAppAccess(name: string, bundleName: string, callback: AsyncCallback<void>): void

禁止指定第三方应用账号名称对指定的第三方应用进行访问。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/VzHkvcnkRLq_bi8SLf5S3A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=2A417B2933C71CFB7ABFF948CFE1EF225CB36EDF4D6A6AA4FE104E8644773BB3)

从API version 7开始支持，从API version 9开始废弃。建议使用[setAppAccess](#setappaccess9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| bundleName | string | 是 | 第三方应用的包名。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当禁止指定第三方应用账号名称对指定包名称的第三方应用进行访问设置成功时，err为null，否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.disableAppAccess('ZhangSan', 'com.example.accountjsdemo', (err: BusinessError) => {
  console.error(`disableAppAccess err: code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]disableAppAccess(deprecated)

disableAppAccess(name: string, bundleName: string): Promise<void>

禁止指定第三方应用账号名称对指定包名称的第三方应用进行访问。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/tqzVmJTHSJ-wCKZTdLSsEA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=9DEC2C4FD8E08B394E13191026ABF3A0801DEBE6EE7DE656ACC9D431691E8C60)

从API version 7开始支持，从API version 9开始废弃。建议使用[setAppAccess](#setappaccess9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 要禁用访问的第三方应用账号的名称。 |
| bundleName | string | 是 | 第三方应用的包名。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.disableAppAccess('ZhangSan', 'com.example.accountjsdemo').then(() => {
  console.info('disableAppAccess Success');
}).catch((err: BusinessError) => {
  console.error(`disableAppAccess err: code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]enableAppAccess(deprecated)

enableAppAccess(name: string, bundleName: string, callback: AsyncCallback<void>): void

允许指定第三方应用账号名称对指定包名称的第三方应用进行访问。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/z-srfAzHQMyLPrD7ijB_2g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=679887FF7C42B7103049968668D2D9507DDAC15FCD1011C111B7E6002EC5DE93)

从API version 7开始支持，从API version 9开始废弃。建议使用[setAppAccess](#setappaccess9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| bundleName | string | 是 | 第三方应用的包名。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当允许指定第三方应用账号名称对指定包名称的第三方应用进行访问设置成功时，err为null，否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.enableAppAccess('ZhangSan', 'com.example.accountjsdemo', (err: BusinessError) => {
  if (err) {
    console.error(`enableAppAccess err: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('enableAppAccess successful.');
  }
});
```

#### \[h2\]enableAppAccess(deprecated)

enableAppAccess(name: string, bundleName: string): Promise<void>

允许指定第三方应用账号的名称对指定包名称的第三方应用进行访问。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/GOfNY-ZfRcqYJ9X8a9TQ_g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=D88D703FC5143E396365F9A8E38A8612F4D8537F09A58768497801155206343A)

从API version 7开始支持，从API version 9开始废弃。建议使用[setAppAccess](#setappaccess9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| bundleName | string | 是 | 第三方应用的包名。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.enableAppAccess('ZhangSan', 'com.example.accountjsdemo').then(() => {
  console.info('enableAppAccess Success');
}).catch((err: BusinessError) => {
  console.error(`enableAppAccess err: code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]checkAppAccountSyncEnable(deprecated)

checkAppAccountSyncEnable(name: string, callback: AsyncCallback<boolean>): void

检查指定应用账号是否开启数据同步功能。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/9kuq5pQmTwyKBsCSRst1Dw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=E2D4D2A5EFFF59852C2D794ED81FE47360DE1198C66DE779FCA8D14FA558F669)

从API version 7开始支持，从API version 9开始废弃。建议使用[checkDataSyncEnabled](#checkdatasyncenabled9)替代。

**需要权限：** ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示指定应用账号已开启数据同步功能；返回false表示未开启。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.checkAppAccountSyncEnable('ZhangSan', (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`checkAppAccountSyncEnable code: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('checkAppAccountSyncEnable result: ' + result);
  }
});
```

#### \[h2\]checkAppAccountSyncEnable(deprecated)

checkAppAccountSyncEnable(name: string): Promise<boolean>

检查指定应用账号是否开启数据同步功能。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/v97laayzSheKj2aTBJ9LeA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=D413E346EE6250884C7034184FD1A45CBFD07DD2465F1D49DB862CC0FFCD63AC)

从API version 7开始支持，从API version 9开始废弃。建议使用[checkDataSyncEnabled](#checkdatasyncenabled9-1)替代。

**需要权限：** ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象。返回true表示指定应用账号已开启数据同步功能；返回false表示未开启。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.checkAppAccountSyncEnable('ZhangSan').then((data: boolean) => {
  console.info('checkAppAccountSyncEnable, result: ' + data);
}).catch((err: BusinessError) => {
  console.error(`checkAppAccountSyncEnable err: code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]setAccountCredential(deprecated)

setAccountCredential(name: string, credentialType: string, credential: string,callback: AsyncCallback<void>): void

设置指定应用账号的凭据。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/gso3usbiTqSyVatZN3n3iA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=146D8D49C5892EA8897116DB1B6EF29A48A57826B5B1EB0D48966679D95BCD28)

从API version 7开始支持，从API version 9开始废弃，建议使用[setCredential](#setcredential9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| credentialType | string | 是 | 凭据类型。 |
| credential | string | 是 | 凭据取值。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置此应用程序账号的凭据成功时，err为null，否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.setAccountCredential('ZhangSan', 'credentialType001', 'credential001', (err: BusinessError) => {
  if (err) {
    console.error(`setAccountCredential err: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('setAccountCredential successful.');
  }
});
```

#### \[h2\]setAccountCredential(deprecated)

setAccountCredential(name: string, credentialType: string, credential: string): Promise<void>

设置指定应用账号的凭据。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/hvVEV8LhRsmye6VqtS5Sag/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=118746C9DE6C751A6F33800EBE7C2AC9D3ACA076D83C8CE4937F0AA1772D454D)

从API version 7开始支持，从API version 9开始废弃，建议使用[setCredential](#setcredential9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| credentialType | string | 是 | 凭据类型。 |
| credential | string | 是 | 凭据取值。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.setAccountCredential('ZhangSan', 'credentialType001', 'credential001').then(() => {
  console.info('setAccountCredential Success');
}).catch((err: BusinessError) => {
  console.error(`setAccountCredential err: code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]setAccountExtraInfo(deprecated)

setAccountExtraInfo(name: string, extraInfo: string, callback: AsyncCallback<void>): void

设置指定应用账号的额外信息。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/ZKYEM8kOSyyOzPDqE2e3ng/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=34B2A22616807BB828C55FA1A7008D5FF3A8ACAB83DA1D09DE6650E0CF9B8C98)

从API version 7开始支持，从API version 9开始废弃。建议使用[setCustomData](#setcustomdata9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| extraInfo | string | 是 | 额外信息(能转换string类型的其它信息)，额外信息不能是应用账号的敏感信息（如应用账号密码、token等）。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置成功时，err为null，否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.setAccountExtraInfo('ZhangSan', 'Tk002', (err: BusinessError) => {
  if (err) {
    console.error(`setAccountExtraInfo err: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('setAccountExtraInfo successful.');
  }
});
```

#### \[h2\]setAccountExtraInfo(deprecated)

setAccountExtraInfo(name: string, extraInfo: string): Promise<void>

设置此应用程序账号的额外信息。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/ConhSvPmQWaUU3WSD1z4rA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=BE35F7CE539656492C95374FA3D49210E0985EF39F22C3664ED57213B68E9FC9)

从API version 7开始支持，从API version 9开始废弃。建议使用[setCustomData](#setcustomdata9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| extraInfo | string | 是 | 额外信息(能转换string类型的其它信息)，额外信息不能是应用账号的敏感信息（如应用账号密码、token等）。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.setAccountExtraInfo('ZhangSan', 'Tk002').then(() => {
  console.info('setAccountExtraInfo Success');
}).catch((err: BusinessError) => {
  console.error(`setAccountExtraInfo err: code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]setAppAccountSyncEnable(deprecated)

setAppAccountSyncEnable(name: string, isEnable: boolean, callback: AsyncCallback<void>): void

开启或禁止指定应用账号的数据同步功能。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/IsQ33WmHTGCnbWdlJnnmvw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=5900A5310477E475BCEEF4FF383821F23C996E566EFF1D25A0910F36DFCA9878)

从API version 7开始支持，从API version 9开始废弃。建议使用[setDataSyncEnabled](#setdatasyncenabled9)替代。

**需要权限：** ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| isEnable | boolean | 是 | 是否开启数据同步。true表示开启数据同步，false表示关闭数据同步。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当开启或禁止成功时，err为null，否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.setAppAccountSyncEnable('ZhangSan', true, (err: BusinessError) => {
  if (err) {
    console.error(`setAppAccountSyncEnable err: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('setAppAccountSyncEnable successful.');
  }
});
```

#### \[h2\]setAppAccountSyncEnable(deprecated)

setAppAccountSyncEnable(name: string, isEnable: boolean): Promise<void>

开启或禁止指定应用账号的数据同步功能。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/-lq30II6QfyEiKhM2ooPPg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=EC4AE18864DEC421D7A752DED08648843E0A6F73205C400C10958725D75777B2)

从API version 7开始支持，从API version 9开始废弃。建议使用[setDataSyncEnabled](#setdatasyncenabled9-1)替代。

**需要权限：** ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| isEnable | boolean | 是 | 是否开启数据同步。true表示开启数据同步，false表示关闭数据同步。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.setAppAccountSyncEnable('ZhangSan', true).then(() => {
  console.info('setAppAccountSyncEnable Success');
}).catch((err: BusinessError) => {
  console.error(`setAppAccountSyncEnable err: code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]setAssociatedData(deprecated)

setAssociatedData(name: string, key: string, value: string, callback: AsyncCallback<void>): void

设置指定应用账号的关联数据。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/023PSScZRYWszRCXBF0h5A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=44B79F20F0E41A638F57C7E1A7CC683FAA8E32C153AB7B7DEC5B75968FF3BE4C)

从API version 7开始支持，从API version 9开始废弃。建议使用[setCustomData](#setcustomdata9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| key | string | 是 | 关联数据的键名。 |
| value | string | 是 | 关联数据的取值。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置与此应用账号关联的数据成功时，err为null，否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.setAssociatedData('ZhangSan', 'k001', 'v001', (err: BusinessError) => {
  if (err) {
    console.error(`setAssociatedData err: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('setAssociatedData successful.');
  }
});
```

#### \[h2\]setAssociatedData(deprecated)

setAssociatedData(name: string, key: string, value: string): Promise<void>

设置指定应用账号的关联数据。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/A2ff8rnbRvuAjuwOhCYa-w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=032BC16176E3CE576DEC1DD3D541A952A3242A5E8ED98308B59AA201C6B9D7F4)

从API version 7开始支持，从API version 9开始废弃。建议使用[setCustomData](#setcustomdata9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| key | string | 是 | 关联数据的键名。 |
| value | string | 是 | 关联数据的取值。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.setAssociatedData('ZhangSan', 'k001', 'v001').then(() => {
  console.info('setAssociatedData Success');
}).catch((err: BusinessError) => {
  console.error(`setAssociatedData err: code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]getAllAccessibleAccounts(deprecated)

getAllAccessibleAccounts(callback: AsyncCallback<Array<AppAccountInfo>>): void

获取所有可访问的应用账号信息。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/iVk99waOQoWtsjMLl2jruw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=B14F8C4FEEAE1B61D1129E2966063E2DF0D5E00EF15C21B688CCF418B2229920)

从API version 7开始支持，从API version 9开始废弃。建议使用[getAllAccounts](#getallaccounts9)替代。

**需要权限：** ohos.permission.GET\_ALL\_APP\_ACCOUNTS，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[AppAccountInfo](#appaccountinfo)\>> | 是 | 回调函数。当查询成功时，err为null，data为获取到的应用账号信息列表；否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getAllAccessibleAccounts((err: BusinessError, data: appAccount.AppAccountInfo[])=>{
  if (err) {
    console.error(`getAllAccessibleAccounts err: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('getAllAccessibleAccounts data: ' + JSON.stringify(data));
  }
});
```

#### \[h2\]getAllAccessibleAccounts(deprecated)

getAllAccessibleAccounts(): Promise<Array<AppAccountInfo>>

获取所有可访问的应用账号信息。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/S3f1XlRARYqA1ENTlqBvXA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=FAF32C66C4E0946F53F400713AF11A99785EDAC5DAD2876349842F66F66C35D7)

从API version 7开始支持，从API version 9开始废弃。建议使用[getAllAccounts](#getallaccounts9-1)替代。

**需要权限：** ohos.permission.GET\_ALL\_APP\_ACCOUNTS，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.AppAccount

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<[AppAccountInfo](#appaccountinfo)\>> | Promise对象，返回全部应用已授权账号信息对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getAllAccessibleAccounts().then((data: appAccount.AppAccountInfo[]) => {
  console.info('getAllAccessibleAccounts: ' + data);
}).catch((err: BusinessError) => {
  console.error(`getAllAccessibleAccounts err: code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]getAllAccounts(deprecated)

getAllAccounts(owner: string, callback: AsyncCallback<Array<AppAccountInfo>>): void

根据应用账号所有者获取调用方可访问的应用账号列表。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/4ltcl277SUCsZNAWOSFnNw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=E54E7253664D344D516035272CCAB430833C8D5965208A3996B700B20EE1EBED)

从API version 7开始支持，从API version 9开始废弃。建议使用[getAccountsByOwner](#getaccountsbyowner9)替代。

**需要权限：** ohos.permission.GET\_ALL\_APP\_ACCOUNTS，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| owner | string | 是 | 应用账号所有者的包名。 |
| callback | AsyncCallback<Array<[AppAccountInfo](#appaccountinfo)\>> | 是 | 应用账号信息列表。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

const selfBundle = 'com.example.actsgetallaaccounts';
appAccountManager.getAllAccounts(selfBundle, (err: BusinessError, data: appAccount.AppAccountInfo[])=>{
  if (err) {
    console.error(`getAllAccounts err: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('getAllAccounts data:' + JSON.stringify(data));
  }
});
```

#### \[h2\]getAllAccounts(deprecated)

getAllAccounts(owner: string): Promise<Array<AppAccountInfo>>

根据应用账号所有者获取调用方可访问的应用账号列表。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/itUhb-_vR1qE1-t66H5GAw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=C00EA0C6FCDBAF9E031179AC49E9604EA86FB27FC89B414E30EFF4D76D4BAAA3)

从API version 7开始支持，从API version 9开始废弃。建议使用[getAccountsByOwner](#getaccountsbyowner9-1)替代。

**需要权限：** ohos.permission.GET\_ALL\_APP\_ACCOUNTS，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| owner | string | 是 | 应用账号所有者的包名。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<[AppAccountInfo](#appaccountinfo)\>> | Promise对象，返回指定应用全部账号信息对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

const selfBundle = 'com.example.actsgetallaaccounts';
appAccountManager.getAllAccounts(selfBundle).then((data: appAccount.AppAccountInfo[]) => {
  console.info('getAllAccounts: ' + data);
}).catch((err: BusinessError) => {
  console.error(`getAllAccounts err: code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]getAccountCredential(deprecated)

getAccountCredential(name: string, credentialType: string, callback: AsyncCallback<string>): void

获取指定应用账号的凭据。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/GYw84BKtSyKaRSHlaxhBPQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=670AD4CF932DFE6EA0A860EE64AC4E5E2FB0346F7881E7CEAE76CCB599D52E97)

从API version 7开始支持，从API version 9开始废弃。建议使用[getCredential](#getcredential9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| credentialType | string | 是 | 凭据类型。 |
| callback | AsyncCallback<string> | 是 | 回调函数。当获取凭据成功时，err为null，data为指定应用账号的凭据；否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getAccountCredential('ZhangSan', 'credentialType001', (err: BusinessError, result: string) => {
  if (err) {
    console.error(`getAccountCredential err: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('getAccountCredential result: ' + result);
  }
});
```

#### \[h2\]getAccountCredential(deprecated)

getAccountCredential(name: string, credentialType: string): Promise<string>

获取指定应用账号的凭据。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/MdFkY463SzKXSISzmWITDg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=F9A81CD50833E7002245AB8703F197EE399566A4212E10A7B3ED46B79637D521)

从API version 7开始支持，从API version 9开始废弃。建议使用[getCredential](#getcredential9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| credentialType | string | 是 | 凭据类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | Promise对象，返回指定应用账号的凭据。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getAccountCredential('ZhangSan', 'credentialType001').then((data: string) => {
  console.info('getAccountCredential, result: ' + data);
}).catch((err: BusinessError) => {
  console.error(`getAccountCredential err: code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]getAccountExtraInfo(deprecated)

getAccountExtraInfo(name: string, callback: AsyncCallback<string>): void

获取指定应用账号的额外信息（能转换成string类型的其它信息）。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/UI_ygwkrRRawEA6mkvLfmQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=2720F173FA71C5F55B65585A738A76239494F09F4CA5C7D417B104B45F86BBAC)

从API version 7开始支持，从API version 9开始废弃。建议使用[getCustomData](#getcustomdata9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| callback | AsyncCallback<string> | 是 | 回调函数。当获取此应用账号的额外信息成功时，err为null，data返回此应用账号的额外信息对象；否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getAccountExtraInfo('ZhangSan', (err: BusinessError, result: string) => {
  if (err) {
    console.error(`getAccountExtraInfo err: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('getAccountExtraInfo result: ' + result);
  }
});
```

#### \[h2\]getAccountExtraInfo(deprecated)

getAccountExtraInfo(name: string): Promise<string>

获取指定应用账号的额外信息（能转换成string类型的其它信息）。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/8Au1WuzYQFqHX0whxNZDCw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=903F1E8061BE8D42CA1B1DF60214489403414D641604633ED43BBC1ACF566E15)

从API version 7开始支持，从API version 9开始废弃。建议使用[getCustomData](#getcustomdata9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | Promise对象，返回此应用程序账号的额外信息对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getAccountExtraInfo('ZhangSan').then((data: string) => {
  console.info('getAccountExtraInfo, result: ' + data);
}).catch((err: BusinessError) => {
  console.error(`getAccountExtraInfo err: code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]getAssociatedData(deprecated)

getAssociatedData(name: string, key: string, callback: AsyncCallback<string>): void

根据指定键名获取特定应用账号的关联数据。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/1nuT6V_oRT6ryjis8wIs1Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=6AFE531D17F8D7A349D22ADB198E9190AEC72A27D47DC1FF76D2CB9AE1C9B9E6)

从API version 7开始支持，从API version 9开始废弃。建议使用[getCustomData](#getcustomdata9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| key | string | 是 | 关联数据的键名。 |
| callback | AsyncCallback<string> | 是 | 回调函数。当获取成功时，err为null，data为关联数据的取值；否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getAssociatedData('ZhangSan', 'k001', (err: BusinessError, result: string) => {
  if (err) {
    console.error(`getAssociatedData err: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('getAssociatedData result: ' + result);
  }
});
```

#### \[h2\]getAssociatedData(deprecated)

getAssociatedData(name: string, key: string): Promise<string>

获取与此应用程序账号关联的数据。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/vxL5wRwlSfqZsjztTKxxFA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=FE268492A83A523F82C7BAA883C9AE7D0E07DD7C01711BCCA7C8F5310CA67C0A)

从API version 7开始支持，从API version 9开始废弃。建议使用[getCustomData](#getcustomdata9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| key | string | 是 | 关联数据的键名。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | Promise对象，返回关联数据的取值。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getAssociatedData('ZhangSan', 'k001').then((data: string) => {
  console.info('getAssociatedData: ' + data);
}).catch((err: BusinessError) => {
  console.error(`getAssociatedData err: code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]on('change')(deprecated)

on(type: 'change', owners: Array<string>, callback: Callback<Array<AppAccountInfo>>): void

订阅指定应用的账号信息变更事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/FP_46wh9Rn-o2RFS_2NPqw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=A4ABB3A1554E20689BE8DFEE1DDB3720D45B7E7C6AE1ED1EFF0383224C176ED8)

从API version 7开始支持，从API version 9开始废弃。建议使用[on('accountChange')](#onaccountchange9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | 'change' | 是 | 事件回调类型，支持的事件为'change'，当账号所有者更新账号信息时，触发该事件。 |
| owners | Array<string> | 是 | 应用账号所有者的包名列表。 |
| callback | Callback<Array<[AppAccountInfo](#appaccountinfo)\>> | 是 | 需要注册的回调函数，返回信息发生变更的应用账号列表。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

function changeOnCallback(data: appAccount.AppAccountInfo[]): void {
  console.info('receive change data:' + JSON.stringify(data));
}

try {
  appAccountManager.on('change', ['com.example.actsaccounttest'], changeOnCallback);
} catch (e) {
  const err = e as BusinessError;
  console.error(`on accountOnOffDemo code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]off('change')(deprecated)

off(type: 'change', callback?: Callback<Array<AppAccountInfo>>): void

取消订阅账号信息变更事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/Y5F8tV5nQ1a7eJbSrJ4yNQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=F05036481B87718CDA5C2130A1C9137DD8FD5828663F7AFC87EC4EAFB0DAAD8D)

从API version 7开始支持，从API version 9开始废弃。建议使用[off('accountChange')](#offaccountchange9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | 'change' | 是 | 事件回调类型，支持的事件为'change'，当账号所有者更新账号信息时，触发该事件。 |
| callback | Callback<Array<[AppAccountInfo](#appaccountinfo)\>> | 否 | 需要注销的回调函数，默认为空，表示取消该类型事件的所有回调。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

function changeOnCallback(data: appAccount.AppAccountInfo[]): void {
  console.info('receive change data: ' + JSON.stringify(data));
  appAccountManager.off('change', () => {
    console.info('off finish');
  })
}

try {
  appAccountManager.on('change', ['com.example.actsaccounttest'], changeOnCallback);
} catch (e) {
  const err = e as BusinessError;
  console.error(`on accountOnOffDemo err: code is ${err.code}, message is ${err.message}`);
}
```

#### \[h2\]authenticate(deprecated)

authenticate(name: string, owner: string, authType: string, options: {\[key: string\]: any;}, callback: AuthenticatorCallback): void

对应用账号进行鉴权以获取授权令牌。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/izSwb_quTjquR1_zsvjLQA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=BADE14B2EB017D23B81CA1C7F7E448F6A9719D3CEC1D6774856C32A7A15F2ED7)

从API version 8开始支持，从API version 9开始废弃。建议使用[auth](#auth9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| owner | string | 是 | 应用账号所有者的包名。 |
| authType | string | 是 | 鉴权类型。 |
| options | {\[key: string\]: any} | 是 | 鉴权所需的可选项。 |
| callback | [AuthenticatorCallback](#authenticatorcallbackdeprecated) | 是 | 回调对象，返回鉴权结果。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { Want, common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext

  onResultCallback(code: number, result: Record<string, Object>): void {
    console.info('resultCode: ' + code);
    console.info('result: ' + JSON.stringify(result));
  }

  onRequestRedirectedCallback(request: Want): void {
    let wantInfo: Want = {
      deviceId: '',
      bundleName: 'com.example.accountjsdemo',
      action: 'ohos.want.action.viewData',
      entities: ['entity.system.default'],
    }
    this.context.startAbility(wantInfo).then(() => {
      console.info('startAbility successfully');
    }).catch((err: BusinessError) => {
      console.error(`startAbility err: code is ${err.code}, message is ${err.message}`);
    })
  }

  aboutToAppear(): void {
    appAccountManager.authenticate('LiSi', 'com.example.accountjsdemo', 'getSocialData', {}, {
      onResult: this.onResultCallback,
      onRequestRedirected: this.onRequestRedirectedCallback
    });
  }

  build() {}
}
```

#### \[h2\]getOAuthToken(deprecated)

getOAuthToken(name: string, owner: string, authType: string, callback: AsyncCallback<string>): void

获取指定应用账号的特定鉴权类型的授权令牌。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/zzPTJmwRTDqyQ_5Rty5sXQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=356AC26DCFA52FF003483F11E338C6968E91CE99E6DA59124942DF9E076D8ED2)

从API version 8开始支持，从API version 9开始废弃。建议使用[getAuthToken](#getauthtoken9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| owner | string | 是 | 应用账号所有者的包名。 |
| authType | string | 是 | 鉴权类型。 |
| callback | AsyncCallback<string> | 是 | 回调函数。当获取成功时，err为null，data为授权令牌值；否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getOAuthToken('LiSi', 'com.example.accountjsdemo', 'getSocialData',
  (err: BusinessError, data: string) => {
    if (err) {
      console.error(`getOAuthToken err: code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('getOAuthToken token: ' + data);
    }
  });
```

#### \[h2\]getOAuthToken(deprecated)

getOAuthToken(name: string, owner: string, authType: string): Promise<string>

获取指定应用账号的特定鉴权类型的授权令牌。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/v_BXywI4TmyZOscs9WI4VA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=95B1C3BBFE319CB3A096E815FE29E99350A35A5D4B0E7EA00354A79461B60560)

从API version 8开始支持，从API version 9开始废弃。建议使用[getAuthToken](#getauthtoken9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| owner | string | 是 | 应用账号所有者的包名。 |
| authType | string | 是 | 鉴权类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | Promise对象，返回授权令牌。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getOAuthToken('LiSi', 'com.example.accountjsdemo', 'getSocialData').then((data: string) => {
  console.info('getOAuthToken token: ' + data);
}).catch((err: BusinessError) => {
  console.error(`getOAuthToken err: code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]setOAuthToken(deprecated)

setOAuthToken(name: string, authType: string, token: string, callback: AsyncCallback<void>): void

为指定应用账号设置特定鉴权类型的授权令牌。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/s_cSrC7nSp-7W_fIFREj2w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=620972068B2F7960D4F8D2CFC6A5DBA2C93E56AC43F81D27347B7A57E71C1925)

从API version 8开始支持，从API version 9开始废弃。建议使用[setAuthToken](#setauthtoken9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| authType | string | 是 | 鉴权类型。 |
| token | string | 是 | 授权令牌。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置成功时，err为null；否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.setOAuthToken('LiSi', 'getSocialData', 'xxxx', (err: BusinessError) => {
  if (err) {
    console.error(`setOAuthToken err: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('setOAuthToken successful.');
  }
});
```

#### \[h2\]setOAuthToken(deprecated)

setOAuthToken(name: string, authType: string, token: string): Promise<void>

为指定应用账号设置特定鉴权类型的授权令牌。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/-Fbc_MWuTKioQ_6EA3zQBA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=40E9BE4B32282E562045F28FF8EDB7768C6EE33B89A9C1CC77EE908FAE64AEB1)

从API version 8开始支持，从API version 9开始废弃。建议使用[setAuthToken](#setauthtoken9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| authType | string | 是 | 鉴权类型。 |
| token | string | 是 | 授权令牌。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.setOAuthToken('LiSi', 'getSocialData', 'xxxx').then(() => {
  console.info('setOAuthToken successfully');
}).catch((err: BusinessError) => {
  console.error(`setOAuthToken err: code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]deleteOAuthToken(deprecated)

deleteOAuthToken(name: string, owner: string, authType: string, token: string, callback: AsyncCallback<void>): void

删除指定应用账号的特定鉴权类型的授权令牌。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/iSvLWjX-TjKhM_3F9vZClQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=7F72AB14B2F29173539AEEAAB2B903BF9519FD01C1577DFD7629BB302DAB65E2)

从API version 8开始支持，从API version 9开始废弃。建议使用[deleteAuthToken](#deleteauthtoken9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| owner | string | 是 | 应用账号所有者的包名。 |
| authType | string | 是 | 鉴权类型。 |
| token | string | 是 | 授权令牌。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当删除成功时，err为null；否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.deleteOAuthToken('LiSi', 'com.example.accountjsdemo', 'getSocialData', 'xxxxx',
  (err: BusinessError) => {
    if (err) {
      console.error(`deleteOAuthToken err: code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('deleteOAuthToken successful.');
    }
  });
```

#### \[h2\]deleteOAuthToken(deprecated)

deleteOAuthToken(name: string, owner: string, authType: string, token: string): Promise<void>

删除指定应用账号的特定鉴权类型的授权令牌。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/i2Q07FxlTYyq1ithCGlGIw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=2574236B0143641A71F294083E479FB9680987E96EF7A7F1BE6DC10C22E6B63B)

从API version 8开始支持，从API version 9开始废弃。建议使用[deleteAuthToken](#deleteauthtoken9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| owner | string | 是 | 应用账号所有者的包名。 |
| authType | string | 是 | 鉴权类型。 |
| token | string | 是 | 授权令牌。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.deleteOAuthToken('LiSi', 'com.example.accountjsdemo', 'getSocialData', 'xxxxx').then(() => {
  console.info('deleteOAuthToken successfully');
}).catch((err: BusinessError) => {
  console.error(`deleteOAuthToken err: code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]setOAuthTokenVisibility(deprecated)

setOAuthTokenVisibility(name: string, authType: string, bundleName: string, isVisible: boolean, callback: AsyncCallback<void>): void

设置指定账号的特定鉴权类型的授权令牌对指定应用的可见性。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/YJgnq8GpQ6iOiGk9lwQ-Wg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=6489F8D967FBECD6EB7722A83E8CA7B10B2FE6CD6F7ABD4BFB791447093E4D36)

从API version 8开始支持，从API version 9开始废弃。建议使用[setAuthTokenVisibility](#setauthtokenvisibility9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| authType | string | 是 | 鉴权类型。 |
| bundleName | string | 是 | 被设置可见性的应用包名。 |
| isVisible | boolean | 是 | 是否可见。true表示可见，false表示不可见。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置成功时，err为null；否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.setOAuthTokenVisibility('LiSi', 'getSocialData', 'com.example.accountjsdemo', true,
  (err: BusinessError) => {
    if (err) {
      console.error(`setOAuthTokenVisibility err: code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('setOAuthTokenVisibility successful.');
    }
  });
```

#### \[h2\]setOAuthTokenVisibility(deprecated)

setOAuthTokenVisibility(name: string, authType: string, bundleName: string, isVisible: boolean): Promise<void>

设置指定账号的特定鉴权类型的授权令牌对指定应用的可见性。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/JgL6SbmjRKO-svMIny0ibg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=585F34926DA517DAA551FE4C3C6AB7242D2E70D011CE5A941DD99B911098DB00)

从API version 8开始支持，从API version 9开始废弃。建议使用[setAuthTokenVisibility](#setauthtokenvisibility9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| authType | string | 是 | 鉴权类型。 |
| bundleName | string | 是 | 被设置可见性的应用包名。 |
| isVisible | boolean | 是 | 是否可见。true表示可见，false表示不可见。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.setOAuthTokenVisibility('LiSi', 'getSocialData', 'com.example.accountjsdemo', true).then(() => {
  console.info('setOAuthTokenVisibility successfully');
}).catch((err: BusinessError) => {
  console.error(`setOAuthTokenVisibility err: code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]checkOAuthTokenVisibility(deprecated)

checkOAuthTokenVisibility(name: string, authType: string, bundleName: string, callback: AsyncCallback<boolean>): void

检查指定应用账号的特定鉴权类型的授权令牌对指定应用的可见性。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/2fx0iJ9sSmOtFi29kVBZlQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=D7FF8BCADF0212CE7E15189CBE9E9A80B89265F3E766D8695AC27C03AE4FC0DC)

从API version 8开始支持，从API version 9开始废弃。建议使用[checkAuthTokenVisibility](#checkauthtokenvisibility9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| authType | string | 是 | 鉴权类型。 |
| bundleName | string | 是 | 检查可见性的应用包名。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当检查成功时，err为null，data为true表示可见，data为false表示不可见；否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.checkOAuthTokenVisibility('LiSi', 'getSocialData', 'com.example.accountjsdemo',
  (err: BusinessError, data: boolean) => {
    if (err) {
      console.error(`checkOAuthTokenVisibility err: code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('checkOAuthTokenVisibility isVisible: ' + data);
    }
  });
```

#### \[h2\]checkOAuthTokenVisibility(deprecated)

checkOAuthTokenVisibility(name: string, authType: string, bundleName: string): Promise<boolean>

检查指定应用账号的特定鉴权类型的授权令牌对指定应用的可见性。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/vFjyWd4MSR6SzVm2c1FfDQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=B5695430E0005A6D2767279ED623A679713ADCD0CE6ACCEE9718C190BFCF215F)

从API version 8开始支持，从API version 9开始废弃。建议使用[checkAuthTokenVisibility](#checkauthtokenvisibility9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| authType | string | 是 | 鉴权类型。 |
| bundleName | string | 是 | 用于检查可见性的应用包名。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象。返回true表示指定鉴权类型的OAuth令牌对特定应用的可见，返回false表示不可见。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.checkOAuthTokenVisibility('LiSi', 'getSocialData', 'com.example.accountjsdemo').then((
  data: boolean) => {
  console.info('checkOAuthTokenVisibility isVisible: ' + data);
}).catch((err: BusinessError) => {
  console.error(`checkOAuthTokenVisibility err: code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]getAllOAuthTokens(deprecated)

getAllOAuthTokens(name: string, owner: string, callback: AsyncCallback<Array<OAuthTokenInfo>>): void

获取指定账号对调用方可见的所有授权令牌。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/Gq_OOrIlS--vWN6Ekyr0Qw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=349181516DDB21284C7339B46E89233AE00037534AC545477D8DF1D00667DBB2)

从API version 8开始支持，从API version 9开始废弃。建议使用[getAllAuthTokens](#getallauthtokens9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| owner | string | 是 | 应用账号所有者的包名。 |
| callback | AsyncCallback<Array<[OAuthTokenInfo](#oauthtokeninfodeprecated)\>> | 是 | 回调函数。当获取成功时，err为null，data为授权令牌数组；否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getAllOAuthTokens('LiSi', 'com.example.accountjsdemo',
  (err: BusinessError, data: appAccount.OAuthTokenInfo[]) => {
    if (err) {
      console.error(`getAllOAuthTokens err: code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('getAllOAuthTokens data: ' + JSON.stringify(data));
    }
  });
```

#### \[h2\]getAllOAuthTokens(deprecated)

getAllOAuthTokens(name: string, owner: string): Promise<Array<OAuthTokenInfo>>

获取指定账号对调用方可见的所有授权令牌。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/1nI509WoTYeVYJxJhZlrGA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=C20B076FB9848CC9FCF24A3F1FB0F6B3F5AE18AF752053FB4FFF5D95A788C4EA)

从API version 8开始支持，从API version 9开始废弃。建议使用[getAllAuthTokens](#getallauthtokens9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| owner | string | 是 | 应用账号所有者的包名。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array< [OAuthTokenInfo](#oauthtokeninfodeprecated)\>> | Promise对象，返回授权令牌数组。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getAllOAuthTokens('LiSi', 'com.example.accountjsdemo').then((
  data: appAccount.OAuthTokenInfo[]) => {
  console.info('getAllOAuthTokens data: ' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error(`getAllOAuthTokens err: code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]getOAuthList(deprecated)

getOAuthList(name: string, authType: string, callback: AsyncCallback<Array<string>>): void

获取指定应用账号的特定鉴权类型的授权列表，即被授权的包名数组（令牌的授权列表通过[setOAuthTokenVisibility](#setoauthtokenvisibilitydeprecated)来设置）。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/yCgjFZ6RSyCev-9CT7mfKA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=F70F7D0600C6905CDD933F2710B5E113B02E4684BE3BE11D394ACD5326A0B5A1)

从API version 8开始支持，从API version 9开始废弃。建议使用[getAuthList](#getauthlist9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| authType | string | 是 | 鉴权类型。 |
| callback | AsyncCallback<Array<string>> | 是 | 回调函数。当获取成功时，err为null，data为被授权的包名数组；否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getOAuthList('LiSi', 'getSocialData', (err: BusinessError, data: string[]) => {
  if (err) {
    console.error(`getOAuthList err: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('getOAuthList data: ' + JSON.stringify(data));
  }
});
```

#### \[h2\]getOAuthList(deprecated)

getOAuthList(name: string, authType: string): Promise<Array<string>>

获取指定应用账号的特定鉴权类型的授权列表，即被授权的包名数组（令牌的授权列表通过[setOAuthTokenVisibility](#setoauthtokenvisibilitydeprecated)来设置）。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/hTIzrC_1S-iaa9N9s3WnRg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=B555BF3B3EBE903CD69DE4782EC242A19A5065A936C7AEDDAD9BC3E9CF783058)

从API version 8开始支持，从API version 9开始废弃。建议使用[getAuthList](#getauthlist9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| authType | string | 是 | 鉴权类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<string>> | Promise对象，返回被授权的包名数组。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getOAuthList('LiSi', 'getSocialData').then((data: string[]) => {
  console.info('getOAuthList data: ' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error(`getOAuthList err: code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]getAuthenticatorCallback(deprecated)

getAuthenticatorCallback(sessionId: string, callback: AsyncCallback<AuthenticatorCallback>): void

获取鉴权会话的认证器回调。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/Y_MapDgxTCCHqQWgBwWZww/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=D32BA875FF62FBD0FC9136E23385AE9ABABE41CCCE3D4869784671FA1BA8196C)

从API version 8开始支持，从API version 9开始废弃。建议使用[getAuthCallback](#getauthcallback9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| sessionId | string | 是 | 鉴权会话的标识。 |
| callback | AsyncCallback<[AuthenticatorCallback](#authenticatorcallbackdeprecated)\> | 是 | 回调函数。当获取鉴权会话的认证器回调函数成功时，err为null，data为认证器回调函数；否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { Want, UIAbility, AbilityConstant } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, param: AbilityConstant.LaunchParam) { // ability 生命周期函数
    let sessionId: string = want.parameters![appAccount.Constants.KEY_SESSION_ID] as string;
    appAccountManager.getAuthenticatorCallback(sessionId,
        (err: BusinessError, callback: appAccount.AuthenticatorCallback) => {
        if (err.code != appAccount.ResultCode.SUCCESS) {
            console.error(`getAuthenticatorCallback err: code is ${err.code}, message is ${err.message}`);
            return;
        }
        callback.onResult(appAccount.ResultCode.SUCCESS, {
          name: 'LiSi',
          owner: 'com.example.accountjsdemo',
          authType: 'getSocialData',
          token: 'xxxxxx'
        });
      });
  }
}
```

#### \[h2\]getAuthenticatorCallback(deprecated)

getAuthenticatorCallback(sessionId: string): Promise<AuthenticatorCallback>

获取鉴权会话的认证器回调。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/SWGIJiM6SVe9cN2LhZGeaA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=5D611893CDD47C7494E5804DCE7A068AB5CBFB124F71FE3668D7A2BEFF39C383)

从API version 8开始支持，从API version 9开始废弃。建议使用[getAuthCallback](#getauthcallback9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| sessionId | string | 是 | 鉴权会话的标识。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[AuthenticatorCallback](#authenticatorcallbackdeprecated)\> | Promise对象，返回鉴权会话的认证器回调对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { Want, UIAbility, AbilityConstant } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, param: AbilityConstant.LaunchParam) { // ability 生命周期函数
    let sessionId: string = want.parameters![appAccount.Constants.KEY_SESSION_ID] as string;
    appAccountManager.getAuthenticatorCallback(sessionId).then((
      callback: appAccount.AuthenticatorCallback) => {
      callback.onResult(appAccount.ResultCode.SUCCESS, {
        name: 'LiSi',
        owner: 'com.example.accountjsdemo',
        authType: 'getSocialData',
        token: 'xxxxxx'
      });
    }).catch((err: BusinessError) => {
      console.error(`getAuthenticatorCallback err: code is ${err.code}, message is ${err.message}`);
    });
  }
}
```

#### \[h2\]getAuthenticatorInfo(deprecated)

getAuthenticatorInfo(owner: string, callback: AsyncCallback<AuthenticatorInfo>): void

获取指定应用的认证器信息。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/By48zU7TRH6BNiiEJqRocw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=69D3A477A53DE5B5C5E71F271E660511CCDF1F3CCBD4827F055947CD495B983F)

从API version 8开始支持，从API version 9开始废弃。建议使用[queryAuthenticatorInfo](#queryauthenticatorinfo9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| owner | string | 是 | 应用账号所有者的包名。 |
| callback | AsyncCallback<[AuthenticatorInfo](#authenticatorinfo8)\> | 是 | 回调函数。当获取成功时，err为null，data为认证器信息对象；否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getAuthenticatorInfo('com.example.accountjsdemo',
  (err: BusinessError, data: appAccount.AuthenticatorInfo) => {
    if (err) {
      console.error(`getAuthenticatorInfo err: code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('getAuthenticatorInfo data: ' + JSON.stringify(data));
    }
  });
```

#### \[h2\]getAuthenticatorInfo(deprecated)

getAuthenticatorInfo(owner: string): Promise<AuthenticatorInfo>

获取指定应用的认证器信息。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/Qe1nBaqtTTecec6KVt4HvA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=2AAD8776F509239D4989EAFF3316084824EB32AC52BD6AB5CB1FC93D6A725993)

从API version 8开始支持，从API version 9开始废弃。建议使用[queryAuthenticatorInfo](#queryauthenticatorinfo9-1)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| owner | string | 是 | 应用账号所有者的包名。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[AuthenticatorInfo](#authenticatorinfo8)\> | Promise对象，返回指定应用的认证器信息对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getAuthenticatorInfo('com.example.accountjsdemo').then((
  data: appAccount.AuthenticatorInfo) => {
  console.info('getAuthenticatorInfo: ' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error(`getAuthenticatorInfo err: code is ${err.code}, message is ${err.message}`);
});
```

#### AppAccountInfo

表示应用账号信息。

**系统能力：** SystemCapability.Account.AppAccount

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| owner | string | 否 | 否 | 应用账号所有者的包名。 |
| name | string | 否 | 否 | 应用账号的名称。 |

#### AuthTokenInfo9+

表示Auth令牌信息。

**系统能力：** SystemCapability.Account.AppAccount

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| authType | string | 否 | 否 | 令牌的鉴权类型。 |
| token | string | 否 | 否 | 令牌的取值。 |
| account | [AppAccountInfo](#appaccountinfo) | 否 | 是 | 令牌所属的账号信息，默认为空。 |

#### OAuthTokenInfo(deprecated)

表示OAuth令牌信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/7jYqv2FuRwqi3Hjsv9eNJQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=B87E9CAEED5BC72CF72E9CDF5DC1478C8B8331323C5982259465485F3900C6C9)

从API version 8开始支持，从API version 9开始废弃。建议使用[AuthTokenInfo](#authtokeninfo9)替代。

**系统能力：** SystemCapability.Account.AppAccount

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| authType | string | 否 | 否 | 令牌的鉴权类型。 |
| token | string | 否 | 否 | 令牌的取值。 |

#### AuthenticatorInfo8+

表示OAuth认证器信息。

**系统能力：** SystemCapability.Account.AppAccount

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| owner | string | 否 | 否 | 认证器的所有者的包名。 |
| iconId | number | 否 | 否 | 认证器的图标标识。 |
| labelId | number | 否 | 否 | 认证器的标签标识。 |

#### AuthResult9+

表示认证结果信息。

**系统能力：** SystemCapability.Account.AppAccount

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| account | [AppAccountInfo](#appaccountinfo) | 否 | 是 | 令牌所属的账号信息，默认为空。 |
| tokenInfo | [AuthTokenInfo](#authtokeninfo9) | 否 | 是 | 令牌信息，默认为空。 |

#### CreateAccountOptions9+

表示创建账号的选项。

**系统能力：** SystemCapability.Account.AppAccount

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| customData | Record<string, string> | 否 | 是 | 自定义数据，默认为空。 |

#### CreateAccountImplicitlyOptions9+

表示隐式创建账号的选项。

**系统能力：** SystemCapability.Account.AppAccount

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| requiredLabels | Array<string> | 否 | 是 | 所需的标签，默认为空。 |
| authType | string | 否 | 是 | 鉴权类型，默认为空。 |
| parameters | Record<string, Object> | 否 | 是 | 自定义参数对象，默认为空。 |

#### SelectAccountsOptions9+

表示用于选择账号的选项。

**系统能力：** SystemCapability.Account.AppAccount

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| allowedAccounts | Array<[AppAccountInfo](#appaccountinfo)\> | 否 | 是 | 允许的账号数组，默认为空。 |
| allowedOwners | Array<string> | 否 | 是 | 允许的账号所有者数组，默认为空。 |
| requiredLabels | Array<string> | 否 | 是 | 认证器的标签标识，默认为空。 |

#### VerifyCredentialOptions9+

表示用于验证凭据的选项。

**系统能力：** SystemCapability.Account.AppAccount

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| credentialType | string | 否 | 是 | 凭据类型，默认为空。 |
| credential | string | 否 | 是 | 凭据取值，默认为空。 |
| parameters | Record<string, Object> | 否 | 是 | 自定义参数对象，默认为空。 |

#### SetPropertiesOptions9+

表示用于设置属性的选项。

**系统能力：** SystemCapability.Account.AppAccount

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| properties | Record<string, Object> | 否 | 是 | 属性对象，默认为空。 |
| parameters | Record<string, Object> | 否 | 是 | 自定义参数对象，默认为空。 |

#### Constants8+

表示常量的枚举。

**系统能力：** SystemCapability.Account.AppAccount

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| ACTION\_ADD\_ACCOUNT\_IMPLICITLY(deprecated) | 'addAccountImplicitly' | 
表示操作，隐式添加账号。

\*\*说明：\*\*从API version 8开始支持，从API version 9开始废弃，建议使用ACTION\_CREATE\_ACCOUNT\_IMPLICITLY替代。

 |
| ACTION\_AUTHENTICATE(deprecated) | 'authenticate' | 

表示操作，鉴权。

\*\*说明：\*\*从API version 8开始支持，从API version 9开始废弃，建议使用ACTION\_AUTH替代。

 |
| ACTION\_CREATE\_ACCOUNT\_IMPLICITLY9+ | 'createAccountImplicitly' | 表示操作，隐式创建账号。 |
| ACTION\_AUTH9+ | 'auth' | 表示操作，鉴权。 |
| ACTION\_VERIFY\_CREDENTIAL9+ | 'verifyCredential' | 表示操作，验证凭据。 |
| ACTION\_SET\_AUTHENTICATOR\_PROPERTIES9+ | 'setAuthenticatorProperties' | 表示操作，设置认证器属性。 |
| KEY\_NAME | 'name' | 表示键名，应用账号的名称。 |
| KEY\_OWNER | 'owner' | 表示键名，应用账号所有者的包名。 |
| KEY\_TOKEN | 'token' | 表示键名，令牌。 |
| KEY\_ACTION | 'action' | 表示键名，操作。 |
| KEY\_AUTH\_TYPE | 'authType' | 表示键名，鉴权类型。 |
| KEY\_SESSION\_ID | 'sessionId' | 表示键名，会话标识。 |
| KEY\_CALLER\_PID | 'callerPid' | 表示键名，调用方PID。 |
| KEY\_CALLER\_UID | 'callerUid' | 表示键名，调用方UID。 |
| KEY\_CALLER\_BUNDLE\_NAME | 'callerBundleName' | 表示键名，调用方包名。 |
| KEY\_REQUIRED\_LABELS9+ | 'requiredLabels' | 表示键名，必需的标签。 |
| KEY\_BOOLEAN\_RESULT9+ | 'booleanResult' | 表示键名，布尔返回值。 |

#### ResultCode(deprecated)

表示返回码的枚举。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/xG4NQM5_Tai2v2e5xf3wcQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=BCAFE690E949DAB127B10AAF9335E18F666EB4328D6E3FEAC3513D9622319F1A)

从API version 8开始支持，从API version 9开始废弃。相关信息建议查看[账号管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-account)替代。

**系统能力：** SystemCapability.Account.AppAccount

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| SUCCESS | 0 | 表示操作成功。 |
| ERROR\_ACCOUNT\_NOT\_EXIST | 10001 | 表示应用账号不存在。 |
| ERROR\_APP\_ACCOUNT\_SERVICE\_EXCEPTION | 10002 | 表示应用账号服务异常。 |
| ERROR\_INVALID\_PASSWORD | 10003 | 表示密码无效。 |
| ERROR\_INVALID\_REQUEST | 10004 | 表示请求无效。 |
| ERROR\_INVALID\_RESPONSE | 10005 | 表示响应无效。 |
| ERROR\_NETWORK\_EXCEPTION | 10006 | 表示网络异常。 |
| ERROR\_OAUTH\_AUTHENTICATOR\_NOT\_EXIST | 10007 | 表示认证器不存在。 |
| ERROR\_OAUTH\_CANCELED | 10008 | 表示鉴权取消。 |
| ERROR\_OAUTH\_LIST\_TOO\_LARGE | 10009 | 表示开放授权列表过大。 |
| ERROR\_OAUTH\_SERVICE\_BUSY | 10010 | 表示开放授权服务忙碌。 |
| ERROR\_OAUTH\_SERVICE\_EXCEPTION | 10011 | 表示开放授权服务异常。 |
| ERROR\_OAUTH\_SESSION\_NOT\_EXIST | 10012 | 表示鉴权会话不存在。 |
| ERROR\_OAUTH\_TIMEOUT | 10013 | 表示鉴权超时。 |
| ERROR\_OAUTH\_TOKEN\_NOT\_EXIST | 10014 | 表示开放授权令牌不存在。 |
| ERROR\_OAUTH\_TOKEN\_TOO\_MANY | 10015 | 表示开放授权令牌过多。 |
| ERROR\_OAUTH\_UNSUPPORT\_ACTION | 10016 | 表示不支持的鉴权操作。 |
| ERROR\_OAUTH\_UNSUPPORT\_AUTH\_TYPE | 10017 | 表示不支持的鉴权类型。 |
| ERROR\_PERMISSION\_DENIED | 10018 | 表示权限不足。 |

#### AuthCallback9+

认证器回调类。

#### \[h2\]onResult9+

onResult: (code: number, result?: AuthResult) => void

通知请求结果。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| code | number | 是 | 鉴权结果码。 |
| result | [AuthResult](#authresult9) | 否 | 鉴权结果，默认为空，表示不接收认证结果信息。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let appAccountManager: appAccount.AppAccountManager = appAccount.createAppAccountManager();
let sessionId = '1234';
appAccountManager.getAuthCallback(sessionId).then((callback: appAccount.AuthCallback) => {
  let result: appAccount.AuthResult = {
    account: {
      name: 'Lisi',
      owner: 'com.example.accountjsdemo',
    },
    tokenInfo: {
      token: 'xxxxxx',
      authType: 'getSocialData'
    }
  };
  callback.onResult(appAccount.ResultCode.SUCCESS, result);
}).catch((err: BusinessError) => {
  console.error(`getAuthCallback err: code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]onRequestRedirected9+

onRequestRedirected: (request: Want) => void

通知请求被跳转。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| request | [Want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-want) | 是 | 用于跳转的请求信息。 |

**示例：**

```ts
import { Want } from '@kit.AbilityKit';

class MyAuthenticator extends appAccount.Authenticator {
  createAccountImplicitly(
    options: appAccount.CreateAccountImplicitlyOptions, callback: appAccount.AuthCallback) {
    let want: Want = {
      bundleName: 'com.example.accountjsdemo',
      abilityName: 'com.example.accountjsdemo.LoginAbility',
    };
    callback.onRequestRedirected(want);
  }

  auth(name: string, authType: string,
    options: Record<string, Object>, callback: appAccount.AuthCallback) {
    let result: appAccount.AuthResult = {
      account: {
        name: 'Lisi',
        owner: 'com.example.accountjsdemo',
      },
      tokenInfo: {
        token: 'xxxxxx',
        authType: 'getSocialData'
      }
    };
    callback.onResult(appAccount.ResultCode.SUCCESS, result);
  }
}
```

#### \[h2\]onRequestContinued9+

onRequestContinued?: () => void

通知请求被继续处理。

**系统能力：** SystemCapability.Account.AppAccount

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let appAccountManager: appAccount.AppAccountManager = appAccount.createAppAccountManager();
let sessionId = '1234';
appAccountManager.getAuthCallback(sessionId).then((callback: appAccount.AuthCallback) => {
  if (callback.onRequestContinued != undefined) {
    callback.onRequestContinued();
  }
}).catch((err: BusinessError) => {
  console.error(`getAuthCallback err: code is ${err.code}, message is ${err.message}`);
});
```

#### AuthenticatorCallback(deprecated)

OAuth认证器回调接口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/TAyGaXE6Qs-Jq_3rlYv5nQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=35A83CD95C31A63BA13F4AFDFE34E1E93E548B79D639D3BDE55848CE0153F583)

从API version 8开始支持，从API version 9开始废弃。建议使用[AuthCallback](#authcallback9)替代。

#### \[h2\]onResult(deprecated)

onResult: (code: number, result: {\[key: string\]: any;}) => void

通知请求结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/14AkyCHaRqCI6PThsQ-JaQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=96081B9BA51DF9D1D817215C06AC9DCAFB91AD15D778534C5CB47E2BB696FBEE)

从API version 8开始支持，从API version 9开始废弃。建议使用[onResult](#onresult9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| code | number | 是 | 鉴权结果码。 |
| result | {\[key: string\]: any} | 是 | 鉴权结果。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let appAccountManager: appAccount.AppAccountManager = appAccount.createAppAccountManager();
let sessionId = '1234';
appAccountManager.getAuthenticatorCallback(sessionId).then((callback: appAccount.AuthenticatorCallback) => {
  callback.onResult(appAccount.ResultCode.SUCCESS, {
    name: 'LiSi',
    owner: 'com.example.accountjsdemo',
    authType: 'getSocialData',
    token: 'xxxxxx'
  });
}).catch((err: BusinessError) => {
  console.error(`getAuthenticatorCallback err: code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]onRequestRedirected(deprecated)

onRequestRedirected: (request: Want) => void

通知请求被跳转。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/YrBURMwbS2KxtfrmGOgUzA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=34B117A19D6EA7720B4AE0CE26CDD8D8798D3AE1EA737C5EEF1EE5E727742D43)

从API version 8开始支持，从API version 9开始废弃。建议使用[onRequestRedirected](#onrequestredirected9)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| request | [Want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-want) | 是 | 用于跳转的请求信息。 |

**示例：**

```ts
import { Want } from '@kit.AbilityKit';

class MyAuthenticator extends appAccount.Authenticator {
  addAccountImplicitly(authType: string, callerBundleName: string,
    options: Record<string, Object>, callback: appAccount.AuthenticatorCallback) {
    let want: Want = {
      bundleName: 'com.example.accountjsdemo',
      abilityName: 'com.example.accountjsdemo.LoginAbility',
    };
    callback.onRequestRedirected(want);
  }

  authenticate(name: string, authType: string, callerBundleName: string,
    options: Record<string, Object>, callback: appAccount.AuthenticatorCallback) {
    callback.onResult(appAccount.ResultCode.SUCCESS, {
      name: name,
      authType: authType,
      token: 'xxxxxx'
    });
  }
}
```

#### Authenticator8+

认证器基类。

#### \[h2\]createAccountImplicitly9+

createAccountImplicitly(options: CreateAccountImplicitlyOptions, callback: AuthCallback): void

根据指定的账号所有者隐式地创建应用账号。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [CreateAccountImplicitlyOptions](#createaccountimplicitlyoptions9) | 是 | 隐式创建账号的选项。 |
| callback | [AuthCallback](#authcallback9) | 是 | 认证器回调对象，用于返回创建结果。 |

#### \[h2\]addAccountImplicitly(deprecated)

addAccountImplicitly(authType: string, callerBundleName: string, options: {\[key: string\]: any;}, callback: AuthenticatorCallback): void

根据指定的鉴权类型和可选项，隐式地添加应用账号。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/V4NROQbCTaG_BzfQWaow4A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=14A2AF6ACA7B56809E8603C19ADE4F1EBC95AF061D3CC1358D96E6B34D65C900)

从API version 8开始支持, 从API version 9开始废弃。建议使用[createAccountImplicitly](#createaccountimplicitly9-2)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| authType | string | 是 | 应用账号的鉴权类型。 |
| callerBundleName | string | 是 | 鉴权请求方的包名。 |
| options | {\[key: string\]: any} | 是 | 鉴权所需要的可选项。 |
| callback | [AuthenticatorCallback](#authenticatorcallbackdeprecated) | 是 | 认证器回调，用于返回鉴权结果。 |

#### \[h2\]auth9+

auth(name: string, authType: string, options: Record<string, Object>, callback: AuthCallback): void

对应用账号进行鉴权以获取授权令牌。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| authType | string | 是 | 应用账号的鉴权类型。 |
| options | Record<string, Object> | 是 | 鉴权所需要的可选项。 |
| callback | [AuthCallback](#authcallback9) | 是 | 回调对象，用于返回鉴权结果。 |

#### \[h2\]authenticate(deprecated)

authenticate(name: string, authType: string, callerBundleName: string, options: {\[key: string\]: any;}, callback: AuthenticatorCallback): void

对应用账号进行鉴权，获取OAuth令牌。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/6kjQD6BvTE2B5oj1QX86Jg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=C70BF1AA849D7DC78FD472CE1F1DA8D92EB5197EE44D4E4426CE45C8D950ABC6)

从API version 8开始支持, 从API version 9开始废弃。建议使用[auth](#auth9-2)替代。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| authType | string | 是 | 应用账号的鉴权类型。 |
| callerBundleName | string | 是 | 鉴权请求方的包名。 |
| options | {\[key: string\]: any} | 是 | 鉴权所需要的可选项。 |
| callback | [AuthenticatorCallback](#authenticatorcallbackdeprecated) | 是 | 认证器回调，用于返回鉴权结果。 |

#### \[h2\]verifyCredential9+

verifyCredential(name: string, options: VerifyCredentialOptions, callback: AuthCallback): void

验证应用账号的凭据。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| options | [VerifyCredentialOptions](#verifycredentialoptions9) | 是 | 验证凭据的可选项。 |
| callback | [AuthCallback](#authcallback9) | 是 | 认证器回调，用于返回验证结果。 |

**示例：**

接口需组合使用，请查看[getRemoteObject](#getremoteobject9)中的示例。

#### \[h2\]setProperties9+

setProperties(options: SetPropertiesOptions, callback: AuthCallback): void

设置认证器属性。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [SetPropertiesOptions](#setpropertiesoptions9) | 是 | 设置属性的可选项。 |
| callback | [AuthCallback](#authcallback9) | 是 | 认证器回调，用于返回设置结果。 |

**示例：**

接口需组合使用，请查看[getRemoteObject](#getremoteobject9)中的示例。

#### \[h2\]checkAccountLabels9+

checkAccountLabels(name: string, labels: Array<string>, callback: AuthCallback): void

检查账号标签。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| labels | Array<string> | 是 | 标签数组。 |
| callback | [AuthCallback](#authcallback9) | 是 | 认证器回调，用于返回检查结果。 |

**示例：**

接口需组合使用，请查看[getRemoteObject](#getremoteobject9)中的示例。

#### \[h2\]checkAccountRemovable9+

checkAccountRemovable(name: string, callback: AuthCallback): void

判断账号是否可以删除。使用callback异步回调。

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 应用账号的名称。 |
| callback | [AuthCallback](#authcallback9) | 是 | 认证器回调，用于返回判断结果。 |

**示例：**

接口需组合使用，请查看[getRemoteObject](#getremoteobject9)中的示例。

#### \[h2\]getRemoteObject9+

getRemoteObject(): rpc.RemoteObject

获取认证器的远程对象，不可以重载实现。

**系统能力：** SystemCapability.Account.AppAccount

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [rpc.RemoteObject](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-rpc#remoteobject) | 认证器Authenticator的远程对象。用于跨进程通信。 |

**示例：**

接口需组合使用，请查看[getRemoteObject](#getremoteobject9)中的示例。

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { Want } from '@kit.AbilityKit';

class MyAuthenticator extends appAccount.Authenticator {
  verifyCredential(name: string,
    options: appAccount.VerifyCredentialOptions, callback: appAccount.AuthCallback) {
      let want: Want = {
        bundleName: 'com.example.accountjsdemo',
        abilityName: 'com.example.accountjsdemo.VerifyAbility',
        parameters: {
          name: name
        }
      };
      callback.onRequestRedirected(want);
  }

  setProperties(options: appAccount.SetPropertiesOptions, callback: appAccount.AuthCallback) {
    let want: Want = {
      bundleName: 'com.example.accountjsdemo',
      abilityName: 'com.example.accountjsdemo.SetPropertiesAbility',
      parameters: {
        options: options
      }
    };
    callback.onRequestRedirected(want);
  }

  checkAccountLabels(name: string, labels: string[], callback: appAccount.AuthCallback) {
    callback.onResult(0);
  }

  checkAccountRemovable(name: string, callback: appAccount.AuthCallback) {
    callback.onResult(0);
  }
}

export default {
  onConnect(want: Want): rpc.RemoteObject { // serviceAbility 生命周期函数, 需要放在serviceAbility中
    let authenticator = new MyAuthenticator();
    return authenticator.getRemoteObject();
  }
}
```

---
title: "@ohos.userIAM.userAuth (用户认证)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-useriam-userauth"
menu_path:
  - "参考"
  - "系统"
  - "安全"
  - "User Authentication Kit（用户认证服务）"
  - "ArkTS API"
  - "@ohos.userIAM.userAuth (用户认证)"
captured_at: "2026-04-17T01:48:21.187Z"
---

# @ohos.userIAM.userAuth (用户认证)

提供用户认证能力，应用于设备解锁、支付、应用登录等场景。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/bJbmjNKZR4CpyH2_4c2sAQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=626B0E79F48B2FBE3E0D2B89409CA391EFB3EB389B3BF6A714FCD8CB892B7118)

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import { userAuth } from '@kit.UserAuthenticationKit';
```

#### 常量

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 值 | 说明 |
| :-- | :-- | :-- | :-- |
| MAX\_ALLOWABLE\_REUSE\_DURATION12+ | number | 300000 | 
复用解锁认证结果最大有效时长，值为300000毫秒。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| PERMANENT\_LOCKOUT\_DURATION22+ | number | 0x7fffffff | 

永久冻结时间，值为0x7fffffff毫秒。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

 |

#### AuthLockState22+

认证类型的身份认证冻结状态。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| isLocked | boolean | 否 | 否 | 表示认证是否已被冻结。true表示已冻结；false表示未冻结。 |
| remainingAuthAttempts | number | 否 | 否 | 认证未被冻结时的剩余尝试次数，最大为5次。 |
| lockoutDuration | number | 否 | 否 | 
认证被冻结时的剩余冻结时间，单位为毫秒。

当永久冻结时，值为PERMANENT\_LOCKOUT\_DURATION，需要PIN认证解锁。

 |

#### UserAuthTipCode20+

表示身份认证中间状态的枚举。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| COMPARE\_FAILURE | 1 | 认证失败。 |
| TIMEOUT | 2 | 认证超时。 |
| TEMPORARILY\_LOCKED | 3 | 临时冻结。 |
| PERMANENTLY\_LOCKED | 4 | 永久冻结。 |
| WIDGET\_LOADED | 5 | 身份认证界面加载完毕。 |
| WIDGET\_RELEASED | 6 | 当前的身份认证界面退出，切换其他认证界面或身份认证控件关闭。 |
| COMPARE\_FAILURE\_WITH\_FROZEN | 7 | 认证失败并触发了认证冻结。 |

#### EnrolledState12+

用户注册凭据的状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| credentialDigest | number | 否 | 否 | 注册的凭据摘要，在凭据增加时随机生成。 |
| credentialCount | number | 否 | 否 | 注册的凭据数量。 |

#### ReuseMode12+

复用解锁认证结果的模式。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| AUTH\_TYPE\_RELEVANT | 1 | 
与认证类型相关，只有当设备解锁认证结果在有效时间内，并且设备解锁的认证类型匹配上本次认证指定认证类型之一时，可以复用该结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| AUTH\_TYPE\_IRRELEVANT | 2 | 

与认证类型无关，设备解锁认证结果在有效时间内，可以重复使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| CALLER\_IRRELEVANT\_AUTH\_TYPE\_RELEVANT14+ | 3 | 

与认证类型相关，任意身份认证（包括设备解锁）结果在有效时间内，并且身份认证的认证类型匹配上本次认证指定认证类型之一时，可以复用该结果。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

 |
| CALLER\_IRRELEVANT\_AUTH\_TYPE\_IRRELEVANT14+ | 4 | 

与认证类型无关，任意身份认证（包括设备解锁）结果在有效时间内，可以重复使用。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

 |

#### ReuseUnlockResult12+

复用解锁认证结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/0Ml9I0zoSmeliQA2FtckCg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=3E83850A39CC006F25D061AA1F2CED2B3DF32E55F3D8EFDEEC6F248E1B57DFCB)

如果身份认证解锁（包括设备解锁）后，在有效时间内凭据发生了变化，身份认证的结果依然可以复用，认证结果中返回当前实际的EnrolledState。若复用认证结果时，之前认证时所使用的身份认证凭据已经被删除，如果删除的是人脸、指纹，则认证结果依然可以复用，只是返回的EnrolledState中credentialCount和credentialDigest均为0；如果删除的是锁屏口令，则此次复用会失败。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| reuseMode | [ReuseMode](#reusemode12) | 否 | 否 | 复用解锁认证结果的模式。 |
| reuseDuration | number | 否 | 否 | 允许复用解锁认证结果的有效时长，单位为毫秒。有效时长的值应大于0，最大值为[MAX\_ALLOWABLE\_REUSE\_DURATION](#常量)。 |

#### userAuth.getAuthLockState22+

getAuthLockState(authType: UserAuthType): Promise<AuthLockState>

查询指定认证类型的冻结状态，使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_BIOMETRIC

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| authType | [UserAuthType](#userauthtype8) | 是 | 认证类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[AuthLockState](#authlockstate22)\> | Promise对象，当查询成功时，返回值为指定认证类型的身份认证冻结状态。失败时报错。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[用户认证错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-useriam)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 12500002 | General operation error. |
| 12500005 | The authentication type is not supported. |
| 12500008 | The parameter is out of range. |
| 12500010 | The type of credential has not been enrolled. |

**示例：**

```ts
import { userAuth } from '@kit.UserAuthenticationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let queryType = userAuth.UserAuthType.PIN;
let authLockState : userAuth.AuthLockState = {
  isLocked : false,
  remainingAuthAttempts : 0,
  lockoutDuration : 0
}

userAuth.getAuthLockState(queryType)
  .then((result : userAuth.AuthLockState) => {
    authLockState = result;
    console.info(`get auth lock state success, authLockState is: ${JSON.stringify(authLockState)}`);
  })
  .catch((err : BusinessError) => {
    console.info(`get auth lock state failed, err code is : ${err?.code}, err message is : ${err?.message}`);
  })
```

#### userAuth.getEnrolledState12+

getEnrolledState(authType: UserAuthType): EnrolledState

查询凭据注册的状态，以检测用户注册凭据的变更。

**需要权限：** ohos.permission.ACCESS\_BIOMETRIC

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| authType | [UserAuthType](#userauthtype8) | 是 | 认证类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [EnrolledState](#enrolledstate12) | 当查询成功时，返回值为用户注册凭据的状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[用户认证错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-useriam)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | 
Parameter error. Possible causes:

1.Mandatory parameters are left unspecified.

 |
| 12500002 | General operation error. |
| 12500005 | The authentication type is not supported. |
| 12500010 | The type of credential has not been enrolled. |

**示例：**

```ts
import { userAuth } from '@kit.UserAuthenticationKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let enrolledState = userAuth.getEnrolledState(userAuth.UserAuthType.FACE);
  console.info(`get current enrolled state success, enrolledState = ${JSON.stringify(enrolledState)}`);
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`get current enrolled state failed, Code is ${err?.code}, message is ${err?.message}`);
}
```

#### AuthParam10+

用户认证相关参数。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| challenge | Uint8Array | 否 | 否 | 
随机挑战值，可用于防重放攻击。最大长度为32字节，可传Uint8Array(\[\])。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| authType | [UserAuthType](#userauthtype8)\[\] | 否 | 否 | 

认证类型列表，用来指定用户认证界面提供的认证方法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| authTrustLevel | [AuthTrustLevel](#authtrustlevel8) | 否 | 否 | 

期望达到的认证可信等级。典型操作需要的身份认证可信等级，以及身份认证可信等级的划分请参见[认证可信等级划分原则](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-authentication-overview#生物认证可信等级划分原则)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| reuseUnlockResult12+ | [ReuseUnlockResult](#reuseunlockresult12) | 否 | 是 | 

表示可以复用解锁认证的结果。默认为不复用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| skipLockedBiometricAuth20+ | boolean | 否 | 是 | 

是否跳过已禁用的认证方式自动切换至其它方式的认证。若无可切换的认证方式则关闭控件，返回认证冻结错误码。

true表示生物认证冻结时，跳过倒计时界面直接切换到其他方式的认证；

false表示不跳过；默认为false。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

 |

#### WidgetParam10+

用户认证界面配置相关参数。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| title | string | 否 | 否 | 
用户认证界面的标题，建议传入认证目的，例如用于支付、登录应用等，不支持传空字串，最大长度为500字符。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| navigationButtonText | string | 否 | 是 | 

导航按键的说明文本，最大长度为60字符。在单指纹、单人脸场景下支持，从API 18开始，增加支持人脸+指纹场景。默认为不展示自定义导航按键。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| uiContext18+ | Context | 否 | 是 | 

以模应用方式显示身份认证对话框，仅支持在2in1设备上使用，如果没有此参数或其他类型的设备，身份认证对话框将以模系统方式显示。 默认以模系统方式显示身份认证对话框。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

 |

#### UserAuthResult10+

用户认证结果。认证成功时，返回认证类型和认证成功的令牌信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| result | number | 否 | 否 | 用户认证结果。若成功返回SUCCESS，若失败返回相应错误码，参见[UserAuthResultCode](#userauthresultcode9)。 |
| token | Uint8Array | 否 | 是 | 认证成功时，返回认证成功的令牌信息。最大长度为1024字节。 |
| authType | [UserAuthType](#userauthtype8) | 否 | 是 | 认证成功时，返回认证类型。 |
| enrolledState12+ | [EnrolledState](#enrolledstate12) | 否 | 是 | 认证成功时，返回注册凭据的状态。 |

#### IAuthCallback10+

返回认证结果的回调对象。

#### \[h2\]onResult10+

onResult(result: UserAuthResult): void

回调函数，返回认证结果。认证成功时，可以通过UserAuthResult获取到认证成功的令牌信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| result | [UserAuthResult](#userauthresult10) | 是 | 认证结果。 |

**示例1：**

发起用户认证，采用认证可信等级≥ATL3的锁屏口令认证，获取认证结果。

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: [userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: '请输入密码',
  };

  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance success');
  // 需要调用UserAuthInstance的start()接口，启动认证后，才能通过onResult获取到认证结果。
  userAuthInstance.on('result', {
    onResult (result) {
      console.info(`userAuthInstance callback result = ${JSON.stringify(result)}`);
    }
  });
  console.info('auth on success');
  userAuthInstance.start();
  console.info('auth start success');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth catch error. Code is ${err?.code}, message is ${err?.message}`);
}
```

**示例2：**

发起用户认证，采用认证可信等级≥ATL3的锁屏口令+认证类型相关+复用设备解锁最大有效时长认证，获取认证结果。

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

let reuseUnlockResult: userAuth.ReuseUnlockResult = {
  reuseMode: userAuth.ReuseMode.AUTH_TYPE_RELEVANT,
  reuseDuration: userAuth.MAX_ALLOWABLE_REUSE_DURATION,
}
try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: [userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
    reuseUnlockResult: reuseUnlockResult,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: '请输入密码',
  };
  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance success');
  // 需要调用UserAuthInstance的start()接口，启动认证后，才能通过onResult获取到认证结果。
  userAuthInstance.on('result', {
    onResult (result) {
      console.info(`userAuthInstance callback result = ${JSON.stringify(result)}`);
    }
  });
  console.info('auth on success');
  userAuthInstance.start();
  console.info('auth start success');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth catch error. Code is ${err?.code}, message is ${err?.message}`);
}
```

**示例3：**

发起用户认证，采用认证可信等级≥ATL3的锁屏口令+任意应用认证类型相关+复用任意应用最大有效时长认证，获取认证结果。

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

let reuseUnlockResult: userAuth.ReuseUnlockResult = {
  reuseMode: userAuth.ReuseMode.CALLER_IRRELEVANT_AUTH_TYPE_RELEVANT,
  reuseDuration: userAuth.MAX_ALLOWABLE_REUSE_DURATION,
}
try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: [userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
    reuseUnlockResult: reuseUnlockResult,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: '请输入密码',
  };
  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance success');
  // 需要调用UserAuthInstance的start()接口，启动认证后，才能通过onResult获取到认证结果。
  userAuthInstance.on('result', {
    onResult (result) {
      console.info(`userAuthInstance callback result = ${JSON.stringify(result)}`);
    }
  });
  console.info('auth on success');
  userAuthInstance.start();
  console.info('auth start success');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth catch error. Code is ${err?.code}, message is ${err?.message}`);
}
```

#### AuthTipInfo20+

用户认证中间状态。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| tipType | [UserAuthType](#userauthtype8) | 否 | 否 | 中间状态对应的认证类型。 |
| tipCode | [UserAuthTipCode](#userauthtipcode20) | 否 | 否 | 中间状态值。 |

#### AuthTipCallback20+

type AuthTipCallback = (authTipInfo: AuthTipInfo) => void

回调函数，返回认证中间状态。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| authTipInfo | [AuthTipInfo](#authtipinfo20) | 是 | 认证中间状态。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: [userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: '请输入密码',
  };

  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance success');
  // 需要调用UserAuthInstance的start()接口，启动认证后，才能通过onAuthTip获取到认证中间状态。
  userAuthInstance.on('authTip', (authTipInfo: userAuth.AuthTipInfo) => {
    console.info(`userAuthInstance callback authTipInfo = ${JSON.stringify(authTipInfo)}`);
  });
  console.info('auth on success');
  userAuthInstance.start();
  console.info('auth start success');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth catch error. Code is ${err?.code}, message is ${err?.message}`);
}
```

#### UserAuthInstance10+

用于执行用户身份认证，并支持使用统一用户身份认证控件。

使用以下接口前，需先通过[getUserAuthInstance](#userauthgetuserauthinstance10)方法获取UserAuthInstance对象。

#### \[h2\]on10+

on(type: 'result', callback: IAuthCallback): void

订阅用户身份认证的最终结果。通过该接口获取到的是用户在认证控件完成身份认证交互后的最终身份认证结果。认证控件消失前，用户中间的认证失败尝试并不会通过该接口返回。如果需要感知整个认证过程中用户的每一次认证失败尝试，请通过[on('authTip')](#on20)接口订阅。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/zbCiJFZ6Tj-HQO3nopGclA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=AD73F9F5533E4DA1E7F83016314586246DCCFA67719396DA0BF6CA2EAA44E4A2)

在PC/2in1设备上，应用如果使用模应用方式发起认证（即配置用户界面参数[widgetParam](#widgetparam10)时传入了有效的uiContext），收到认证结果后，若需弹出其他窗口，应先获取控件弹窗释放的标志消息，通过[on('authTip')](#on20)接口订阅控件释放消息（authTipInfo.tipCode = UserAuthTipCode.WIDGET\_RELEASED）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | 'result' | 是 | 订阅事件类型，表明该事件用来返回认证结果。 |
| callback | [IAuthCallback](#iauthcallback10) | 是 | 认证接口的回调函数，用于返回认证结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[用户认证错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-useriam)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.Mandatory parameters are left unspecified.

2.Incorrect parameter types.

3.Parameter verification failed.

 |
| 12500002 | General operation error. |

**示例1：**

以模系统方式进行用户身份认证。

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: [userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: '请输入密码',
  };
  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance success');
  // 需要调用UserAuthInstance的start()接口，启动认证后，才能通过onResult获取到认证结果。
  userAuthInstance.on('result', {
    onResult (result) {
      console.info(`userAuthInstance callback result = ${JSON.stringify(result)}`);
    }
  });
  console.info('auth on success');
  userAuthInstance.start();
  console.info('auth start success');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth catch error. Code is ${err?.code}, message is ${err?.message}`);
}
```

**示例2：**

以模应用方式进行用户身份认证。

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

@Entry
@Component
struct Index {
  modelApplicationAuth(): void {
    try {
      const rand = cryptoFramework.createRandom();
      const len: number = 16;
      let randData: Uint8Array | null = null;
      let retryCount = 0;
      while(retryCount < 3){
        randData = rand?.generateRandomSync(len)?.data;
        if(randData){
          break;
        }
        retryCount++;
      }
      if(!randData){
        return;
      }
      const authParam: userAuth.AuthParam = {
        challenge: randData,
        authType: [userAuth.UserAuthType.PIN],
        authTrustLevel: userAuth.AuthTrustLevel.ATL3,
      };
      const uiContext: UIContext = this.getUIContext();
      const context: Context | undefined = uiContext.getHostContext();
      const widgetParam: userAuth.WidgetParam = {
        title: '请输入密码',
        uiContext: context,
      };
      const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
      console.info('get userAuth instance success');
      // 需要调用UserAuthInstance的start()接口，启动认证后，才能通过onResult获取到认证结果。
      userAuthInstance.on('result', {
        onResult (result) {
          console.info(`userAuthInstance callback result = ${JSON.stringify(result)}`);
        }
      });
      console.info('auth on success');
      userAuthInstance.start();
      console.info('auth start success');
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error(`auth catch error. Code is ${err?.code}, message is ${err?.message}`);
    }
  }

  build() {
    Column() {
      Button('start auth')
        .onClick(() => {
          this.modelApplicationAuth();
        })
    }
  }
}
```

#### \[h2\]off10+

off(type: 'result', callback?: IAuthCallback): void

取消订阅用户身份认证的结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/rdMSFi0FTY-XiG-Ie7fdyQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=DBBFCF078F6C5491872B4AEDA020B292ED39673C2CC8F45CA94FB6C14646772E)

需要使用已经成功订阅事件的[UserAuthInstance](#userauthinstance10)对象调用该接口进行取消订阅。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | 'result' | 是 | 订阅事件类型，表明该事件用来返回认证结果。 |
| callback | [IAuthCallback](#iauthcallback10) | 否 | 认证接口的回调函数，用于返回认证结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[用户认证错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-useriam)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.Mandatory parameters are left unspecified.

2.Incorrect parameter types.

3.Parameter verification failed.

 |
| 12500002 | General operation error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: [userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: '请输入密码',
  };
  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance success');
  userAuthInstance.off('result', {
    onResult (result) {
      console.info(`auth off result = ${JSON.stringify(result)}`);
    }
  });
  console.info('auth off success');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth catch error. Code is ${err?.code}, message is ${err?.message}`);
}
```

#### \[h2\]start10+

start(): void

开始认证。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/TmV9W-V1R0yLPIsVKWn6ug/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=9BB3A9140AEE98797DB78E916CD0C2012628B274012A2C802072CDB7EEC90AD5)

每个UserAuthInstance只能进行一次认证，需要再次认证时，必须重新获取UserAuthInstance。

**需要权限：** ohos.permission.ACCESS\_BIOMETRIC 或 ohos.permission.USER\_AUTH\_FROM\_BACKGROUND（仅向系统应用开放）

从API 20开始，仅系统应用可以通过申请ohos.permission.USER\_AUTH\_FROM\_BACKGROUND，在后台发起认证。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[用户认证错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-useriam)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | 
Permission denied. Possible causes:

1.No permission to access biometric.

2.No permission to start authentication from background.

 |
| 401 | 

Parameter error. Possible causes:

1.Incorrect parameter types.

 |
| 12500002 | General operation error. |
| 12500003 | Authentication canceled. |
| 12500005 | The authentication type is not supported. |
| 12500006 | The authentication trust level is not supported. |
| 12500009 | Authentication is locked out. |
| 12500010 | The type of credential has not been enrolled. |
| 12500011 | Switched to the customized authentication process. |
| 12500013 | Operation failed because of PIN expired. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: [userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: '请输入密码',
  };
  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance success');
  userAuthInstance.start();
  console.info('auth start success');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth catch error. Code is ${err?.code}, message is ${err?.message}`);
}
```

#### \[h2\]cancel10+

cancel(): void

取消认证。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/R7_uFP2jSnCHP6Rr7bMw4w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=16BAA192AA1D812F789F85F5FE0F11EA8EC5F29B2469B0EEE9974A024C33E3DF)

此时UserAuthInstance必须是正在进行认证的对象。

**需要权限：** ohos.permission.ACCESS\_BIOMETRIC

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | 
Parameter error. Possible causes:

1.Incorrect parameter types.

 |
| 12500002 | General operation error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam : userAuth.AuthParam = {
    challenge: randData,
    authType: [userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: '请输入密码',
  };
  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance success');
  // 需要调用UserAuthInstance的start()接口，启动认证后，才能调用cancel()接口。
  userAuthInstance.start();
  console.info('auth start success');
  userAuthInstance.cancel();
  console.info('auth cancel success');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth catch error. Code is ${err?.code}, message is ${err?.message}`);
}
```

#### \[h2\]on20+

on(type: 'authTip', callback: AuthTipCallback): void

订阅身份认证过程中的提示信息。通过该接口可以获取到认证过程中控件的拉起和退出提示，以及认证过程中用户的每一次认证失败尝试。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/mA4pzbEZShSeLeTKvB45bQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=8FDC5C68CC47321DBADA5CB03BB3DA16F4904FECB190B2A766D7B07DC0DC75A9)

在PC/2in1设备上，应用如果使用模应用方式发起认证（即配置用户界面参数[widgetParam](#widgetparam10)时传入了有效的uiContext），收到认证结果后，若需弹出其他窗口，应先获取控件弹窗释放的标志消息，通过[on('authTip')](#on20)接口订阅控件释放消息（authTipInfo.tipCode = UserAuthTipCode.WIDGET\_RELEASED）。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅事件类型，支持的事件为'authTip'，当[start()](#start10)调用完成，发起身份认证，触发该事件。 |
| callback | [AuthTipCallback](#authtipcallback20) | 是 | 认证接口的回调函数，用于返回认证中间状态。 |

**错误码：**

以下错误码的详细介绍请参见[用户认证错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-useriam)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12500002 | General operation error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: [userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: '请输入密码',
  };
  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance success');
  // 需要调用UserAuthInstance的start()接口，启动认证后，才能通过onAuthTip获取到认证中间状态。
  userAuthInstance.on('authTip', (authTipInfo: userAuth.AuthTipInfo) => {
    console.info(`userAuthInstance callback authTipInfo = ${JSON.stringify(authTipInfo)}`);
  });
  console.info('auth on success');
  userAuthInstance.start();
  console.info('auth start success');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth catch error. Code is ${err?.code}, message is ${err?.message}`);
}
```

#### \[h2\]off20+

off(type: 'authTip', callback?: AuthTipCallback): void

取消订阅用户身份认证中间状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/JqGrNme3QFKO6TgLQvvpaQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=2039C4931E17043C9B37101F9E7E84AFED8B366D0B05482489B1B4BF765A3C1F)

需要使用已经成功订阅事件的[UserAuthInstance](#userauthinstance10)对象调用该接口进行取消订阅。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 取消订阅的事件类型，支持的事件为'authTip'，当[start()](#start10)调用完成，发起身份认证并调用[on()](#on20)订阅该事件后，调用该方法可取消订阅，不会再触发该事件。 |
| callback | [AuthTipCallback](#authtipcallback20) | 否 | 认证接口的回调函数，用于返回认证中间状态。 当不传该参数时默认值为调用[on()](#on20)接口时传递的参数值。 |

**错误码：**

以下错误码的详细介绍请参见[用户认证错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-useriam)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12500002 | General operation error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: [userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: '请输入密码',
  };
  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance success');
  userAuthInstance.off('authTip', (authTipInfo: userAuth.AuthTipInfo) => {
    console.info(`userAuthInstance callback authTipInfo = ${JSON.stringify(authTipInfo)}`);
  });
  console.info('auth off success');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth catch error. Code is ${err?.code}, message is ${err?.message}`);
}
```

#### userAuth.getUserAuthInstance10+

getUserAuthInstance(authParam: AuthParam, widgetParam: WidgetParam): UserAuthInstance

获取[UserAuthInstance](#userauthinstance10)对象，执行用户身份认证，并支持使用统一用户身份认证控件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/traIruhMRyaiUUUMZPul-Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=B2E5C57750A0DEFC5566FA7CD28BC8CAFF0605B73D87B794AB98777485804F43)

每个UserAuthInstance只能进行一次认证，需要再次认证时，必须重新获取UserAuthInstance。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| authParam | [AuthParam](#authparam10) | 是 | 用户认证相关参数。 |
| widgetParam | [WidgetParam](#widgetparam10) | 是 | 用户认证界面配置相关参数。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [UserAuthInstance](#userauthinstance10) | 支持用户界面的认证器对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[用户认证错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-useriam)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.Mandatory parameters are left unspecified.

2.Incorrect parameter types.

3.Parameter verification failed.

 |
| 12500002 | General operation error. |
| 12500005 | The authentication type is not supported. |
| 12500006 | The authentication trust level is not supported. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: [userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: '请输入密码',
  };
  let userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance success');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth catch error. Code is ${err?.code}, message is ${err?.message}`);
}
```

#### AuthResultInfo(deprecated)

表示认证结果信息，用于描述认证结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/WXbRw0AoRHmQr9h3qzw20w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=0E5D538A3540D160018151D2CABED372B1A68BDFF99B40C87F9BE2B0CB41471B)

从 API version 9 开始支持，从 API version 11 开始废弃，请使用[UserAuthResult](#userauthresult10)替代。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| result | number | 否 | 否 | 认证结果。 |
| token | Uint8Array | 否 | 是 | 用户身份认证通过的凭证。 |
| remainAttempts | number | 否 | 是 | 剩余的认证尝试次数。 |
| lockoutDuration | number | 否 | 是 | 认证操作的锁定时长，时间单位为毫秒ms。 |

#### TipInfo(deprecated)

表示认证过程中的提示信息，用于提供认证过程的反馈。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/0NbqgcsETpSnroW7rxo6qg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=1E8D92ACE4591FA35A4897B40C95AFEA99C2A733C8D5F2A7AAAC8C92F681EA86)

从 API version 9 开始支持，从 API version 11 开始废弃，请使用[AuthTipInfo](#authtipinfo20)替代。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| module | number | 否 | 否 | 发送提示信息的模块标识。 |
| tip | number | 否 | 否 | 认证过程提示信息。 |

#### EventInfo(deprecated)

type EventInfo = AuthResultInfo | TipInfo

表示认证过程中事件信息的类型。

该类型为下表类型取值中的联合类型。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/k4YY10MzSgCAOWv6oasyog/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=3F3E8A1AEB53D42A6B0EFD3B6EA82F3A52459C4BDBCB32788CC5C9983D55BA93)

从 API version 9 开始支持，从 API version 11 开始废弃，请使用[UserAuthResult](#userauthresult10)替代。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 类型 | 说明 |
| :-- | :-- |
| [AuthResultInfo](#authresultinfodeprecated) | 获取到的认证结果信息。 |
| [TipInfo](#tipinfodeprecated) | 认证过程中的提示信息。 |

#### AuthEventKey(deprecated)

type AuthEventKey = 'result' | 'tip'

表示认证事件类型的关键字，作为[on](#ondeprecated)接口的参数。

该类型为下表类型取值中的联合类型。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/o5RRVwFtR4mF-qHfZyOLBA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=1E53237873CACDE51E6951F06AE3954B82FAEC44B061639626D8A5CAEA29E533)

从 API version 9 开始支持，从 API version 11 开始废弃。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 类型 | 说明 |
| :-- | :-- |
| 'result' | [on](#ondeprecated)接口第一个参数为"result"时，[callback](#callbackdeprecated)回调返回认证的结果信息。 |
| 'tip' | [on](#ondeprecated)接口第一个参数为"tip"时，[callback](#callbackdeprecated)回调返回认证操作中的提示信息。 |

#### AuthEvent(deprecated)

认证接口的异步回调对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/tI6iD1kPRBiUynwcD9GBSw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=8019F6159E205BBC5C7C2BA53E3F1F92549FD7B646CFAC82EBA887060507C918)

从 API version 9 开始支持，从 API version 11 开始废弃，请使用[IAuthCallback](#iauthcallback10)替代。

#### \[h2\]callback(deprecated)

callback(result : EventInfo) : void

通过该回调获取认证结果信息或认证过程中的提示信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/upTr19aiR6OjgMzN05sIuA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=B7FACA3582D6B4FF2639228ECFFB9EB6F979ED038DF81C939141B58FB82D05EB)

从 API version 9 开始支持，从 API version 11 开始废弃，请使用[onResult](#onresult10)替代。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| result | [EventInfo](#eventinfodeprecated) | 是 | 返回的认证结果信息或提示信息。 |

**示例：**

```ts
import { userAuth } from '@kit.UserAuthenticationKit';

let challenge = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8]);
let authType = userAuth.UserAuthType.FACE;
let authTrustLevel = userAuth.AuthTrustLevel.ATL1;
// 通过callback获取认证结果。
try {
  let auth = userAuth.getAuthInstance(challenge, authType, authTrustLevel);
  auth.on('result', {
    callback: (result: userAuth.AuthResultInfo) => {
      console.info(`authV9 result ${result.result}`);
      console.info(`authV9 token ${result.token}`);
      console.info(`authV9 remainAttempts ${result.remainAttempts}`);
      console.info(`authV9 lockoutDuration ${result.lockoutDuration}`);
    }
  } as userAuth.AuthEvent);
  auth.start();
  console.info('authV9 start success');
} catch (error) {
  console.error(`authV9 error = ${error}`);
  // do error.
}
// 通过callback获取认证过程中的提示信息。
try {
  let auth = userAuth.getAuthInstance(challenge, authType, authTrustLevel);
  auth.on('tip', {
    callback : (result : userAuth.TipInfo) => {
      switch (result.tip) {
        case userAuth.FaceTips.FACE_AUTH_TIP_TOO_BRIGHT:
          // do something;
          break;
        case userAuth.FaceTips.FACE_AUTH_TIP_TOO_DARK:
          // do something;
          break;
        default:
          // do others.
      }
    }
  } as userAuth.AuthEvent);
  auth.start();
  console.info('authV9 start success');
} catch (error) {
  console.error(`authV9 error = ${error}`);
  // do error.
}
```

#### AuthInstance(deprecated)

执行用户认证的对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/jIwYeLj1Rn-juGT1Zezzdg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=FB7B830089F63EE523FF53A68E662B27B5EE9D105AE64FC780C62D8CF0B0A8EB)

从 API version 9 开始支持，从 API version 10 开始废弃，请使用[UserAuthInstance](#userauthinstance10)替代。

#### \[h2\]on(deprecated)

on : (name : AuthEventKey, callback : AuthEvent) => void

订阅指定类型的用户认证事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/T4G8kXKSS7uRjJ9jDUVEOg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=F259FC437DC8E586A1C2C5808BB2FD1179AAA2FE3A4AFB2B4D1195DD24E368AA)

从 API version 9 开始支持，从 API version 10 开始废弃，请使用[on](#on10)替代。

使用获取到的[AuthInstance](#authinstancedeprecated)对象调用该接口进行订阅。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | [AuthEventKey](#autheventkeydeprecated) | 是 | 表示认证事件类型，取值为"result"时，回调函数返回认证结果；取值为"tip"时，回调函数返回认证过程中的提示信息。 |
| callback | [AuthEvent](#autheventdeprecated) | 是 | 认证接口的回调函数，用于返回认证结果或认证过程中的提示信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[用户认证错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-useriam)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 12500002 | General operation error. |

**示例：**

```ts
import { userAuth } from '@kit.UserAuthenticationKit';

let challenge = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8]);
let authType = userAuth.UserAuthType.FACE;
let authTrustLevel = userAuth.AuthTrustLevel.ATL1;
try {
  let auth = userAuth.getAuthInstance(challenge, authType, authTrustLevel);
  // 订阅认证结果。
  auth.on('result', {
    callback: (result: userAuth.AuthResultInfo) => {
      console.info(`authV9 result ${result.result}`);
      console.info(`authV9 token ${result.token}`);
      console.info(`authV9 remainAttempts ${result.remainAttempts}`);
      console.info(`authV9 lockoutDuration ${result.lockoutDuration}`);
    }
  });
  // 订阅认证过程中的提示信息。
  auth.on('tip', {
    callback : (result : userAuth.TipInfo) => {
      switch (result.tip) {
        case userAuth.FaceTips.FACE_AUTH_TIP_TOO_BRIGHT:
          // do something;
          break;
        case userAuth.FaceTips.FACE_AUTH_TIP_TOO_DARK:
          // do something;
          break;
        default:
          // do others.
      }
    }
  } as userAuth.AuthEvent);
  auth.start();
  console.info('authV9 start success');
} catch (error) {
  console.error(`authV9 error = ${error}`);
  // do error.
}
```

#### \[h2\]off(deprecated)

off : (name : AuthEventKey) => void

取消订阅特定类型的认证事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/1fnSUpRtT9SkeR-UOgz7XA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=C5538679EABF844365A5F94102C1A859E4C62401A692774BE6DBBC0A7FE8ADD0)

从 API version 9 开始支持，从 API version 10 开始废弃，请使用[off](#off10)替代。

需要使用已经成功订阅事件的[AuthInstance](#authinstancedeprecated)对象调用该接口进行取消订阅。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | [AuthEventKey](#autheventkeydeprecated) | 是 | 表示认证事件类型，取值为"result"时，取消订阅认证结果；取值为"tip"时，取消订阅认证过程中的提示信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[用户认证错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-useriam)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 12500002 | General operation error. |

**示例：**

```ts
import { userAuth } from '@kit.UserAuthenticationKit';

let challenge = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8]);
let authType = userAuth.UserAuthType.FACE;
let authTrustLevel = userAuth.AuthTrustLevel.ATL1;
try {
  let auth = userAuth.getAuthInstance(challenge, authType, authTrustLevel);
  // 订阅认证结果。
  auth.on('result', {
    callback: (result: userAuth.AuthResultInfo) => {
      console.info(`authV9 result ${result.result}`);
      console.info(`authV9 token ${result.token}`);
      console.info(`authV9 remainAttempts ${result.remainAttempts}`);
      console.info(`authV9 lockoutDuration ${result.lockoutDuration}`);
    }
  });
  // 取消订阅结果。
  auth.off('result');
  console.info('cancel subscribe authentication event success');
} catch (error) {
  console.error(`cancel subscribe authentication event failed, error = ${error}`);
  // do error.
}
```

#### \[h2\]start(deprecated)

start : () => void

开始认证。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/X0ghf-3PTQqYEAf8WiwzIw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=EA8E08EC14777F2B28F7A2F430CB4E36437431774C131E141519DEAAEF8A93B1)

从 API version 9 开始支持，从 API version 10 开始废弃，请使用[start](#start10)替代。

使用获取到的[AuthInstance](#authinstancedeprecated)对象调用该接口进行认证。

**需要权限：** ohos.permission.ACCESS\_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[用户认证错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-useriam)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 12500001 | Authentication failed. |
| 12500002 | General operation error. |
| 12500003 | The operation is canceled. |
| 12500004 | The operation is time-out. |
| 12500005 | The authentication type is not supported. |
| 12500006 | The authentication trust level is not supported. |
| 12500007 | The authentication task is busy. |
| 12500009 | The authenticator is locked. |
| 12500010 | The type of credential has not been enrolled. |

**示例：**

```ts
import { userAuth } from '@kit.UserAuthenticationKit';

let challenge = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8]);
let authType = userAuth.UserAuthType.FACE;
let authTrustLevel = userAuth.AuthTrustLevel.ATL1;

try {
  let auth = userAuth.getAuthInstance(challenge, authType, authTrustLevel);
  auth.start();
  console.info('authV9 start auth success');
} catch (error) {
  console.error(`authV9 start auth failed, error = ${error}`);
}
```

#### \[h2\]cancel(deprecated)

cancel : () => void

取消认证。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/OnS0at0qQrK3wykiMbRkUw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=0C21D60B96718C0ED9D5C9D52F7F895FFCA5B65C43FC45D3957D89FD9E979B3C)

从 API version 9 开始支持，从 API version 10 开始废弃，请使用[cancel](#cancel10)替代。

使用获取到的[AuthInstance](#authinstancedeprecated)对象调用该接口进行取消认证，此[AuthInstance](#authinstancedeprecated)需要是正在进行认证的对象。

**需要权限：** ohos.permission.ACCESS\_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[用户认证错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-useriam)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. |
| 12500002 | General operation error. |

**示例：**

```ts
import { userAuth } from '@kit.UserAuthenticationKit';

let challenge = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8]);
let authType = userAuth.UserAuthType.FACE;
let authTrustLevel = userAuth.AuthTrustLevel.ATL1;

try {
  let auth = userAuth.getAuthInstance(challenge, authType, authTrustLevel);
  auth.cancel();
  console.info('cancel auth success');
} catch (error) {
  console.error(`cancel auth failed, error = ${error}`);
}
```

#### userAuth.getAuthInstance(deprecated)

getAuthInstance(challenge : Uint8Array, authType : UserAuthType, authTrustLevel : AuthTrustLevel): AuthInstance

获取AuthInstance对象，用于执行用户身份认证。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/mT_YjGtMQGGT7hD7rJE_6A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=DAEE9B3E8ABE2433950F11498BA5587511A025F789116A627DAB9C99702F42F7)

从 API version 9 开始支持，从 API version 10 开始废弃，请使用[getUserAuthInstance](#userauthgetuserauthinstance10)替代。

每个AuthInstance只能进行一次认证，若需要再次进行认证则需重新获取AuthInstance。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| challenge | Uint8Array | 是 | 挑战值，最大长度为32字节，可以传Uint8Array(\[\])。 |
| authType | [UserAuthType](#userauthtype8) | 是 | 认证类型，当前支持FACE和FINGERPRINT。 |
| authTrustLevel | [AuthTrustLevel](#authtrustlevel8) | 是 | 认证信任等级。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [AuthInstance](#authinstancedeprecated) | 认证器对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[用户认证错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-useriam)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 12500002 | General operation error. |
| 12500005 | The authentication type is not supported. |
| 12500006 | The authentication trust level is not supported. |

**示例：**

```ts
import { userAuth } from '@kit.UserAuthenticationKit';

let challenge = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8]);
let authType = userAuth.UserAuthType.FACE;
let authTrustLevel = userAuth.AuthTrustLevel.ATL1;

try {
  let auth = userAuth.getAuthInstance(challenge, authType, authTrustLevel);
  console.info('let auth instance success');
} catch (error) {
  console.error(`get auth instance success failed, error = ${error}`);
}
```

#### userAuth.getAvailableStatus9+

getAvailableStatus(authType : UserAuthType, authTrustLevel : AuthTrustLevel): void

查询指定类型和等级的认证能力是否支持。

**需要权限：** ohos.permission.ACCESS\_BIOMETRIC

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| authType | [UserAuthType](#userauthtype8) | 是 | 认证类型。从 API version 11 开始支持PIN查询。 |
| authTrustLevel | [AuthTrustLevel](#authtrustlevel8) | 是 | 认证信任等级。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/bGzWi0xxRgOi3wy061flQw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=AA60892ADD21D30CF659DBF765C6894A3626B5AD440ED35021D451709F2C189F)

如果未注册对应执行器，系统不支持该认证能力，需返回12500005。

如果已注册对应执行器，功能未禁用，但认证安全等级低于业务指定时，需返回12500006。

如果已注册对应执行器，功能未禁用，但用户未注册凭据时，需返回12500010。

如果已注册对应执行器，功能未禁用，但密码过期时，需返回12500013。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/wZEPNoxaR5eXT4WAQHCJXw/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=733461264C2BA5988DC74A5D0C525FE90692CD60BDF992694B8521F7A89F3297)

若用户注册的锁屏口令是4位PIN时，其认证可信等级为ATL3，调用该接口查询是否支持ATL4级别的密码认证时，需返回12500010。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[用户认证错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-useriam)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | 
Parameter error. Possible causes:

1.Mandatory parameters are left unspecified.

 |
| 12500002 | General operation error. |
| 12500005 | The authentication type is not supported. |
| 12500006 | The authentication trust level is not supported. |
| 12500010 | The type of credential has not been enrolled. |
| 12500013 | Operation failed because of PIN expired. |

**示例：**

```ts
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  userAuth.getAvailableStatus(userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL3);
  console.info('current auth trust level is supported');
} catch (error) {
  console.error(`current auth trust level is not supported, error = ${error}`);
}
```

#### UserAuthResultCode9+

表示返回码的枚举。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| SUCCESS | 12500000 | 
执行成功。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| FAIL | 12500001 | 

认证失败。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| GENERAL\_ERROR | 12500002 | 

操作通用错误。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| CANCELED | 12500003 | 

认证取消。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| TIMEOUT | 12500004 | 

认证超时。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| TYPE\_NOT\_SUPPORT | 12500005 | 

认证类型不支持。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| TRUST\_LEVEL\_NOT\_SUPPORT | 12500006 | 

认证等级不支持。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| BUSY | 12500007 | 

系统繁忙。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| INVALID\_PARAMETERS20+ | 12500008 | 

参数校验失败。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

 |
| LOCKED | 12500009 | 

认证器已锁定。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| NOT\_ENROLLED | 12500010 | 

用户未录入指定的系统身份认证凭据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| CANCELED\_FROM\_WIDGET10+ | 12500011 | 

用户取消了系统认证方式，选择应用自定义认证。需调用者拉起自定义认证界面。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| PIN\_EXPIRED12+ | 12500013 | 

当前的认证操作执行失败。返回这个错误码，表示系统锁屏口令过期。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |

#### UserAuth(deprecated)

认证器对象。

#### \[h2\]constructor(deprecated)

constructor()

创建认证器对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/BpmubIBuRliy29_qk4lFsw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=C7A86606AF240E6AFC7B2955DB95B0B416EDE6A2D8E6DDD8FFA14C23D35D0DCF)

从 API version 8 开始支持，从 API version 9 开始废弃，请使用[getAuthInstance](#userauthgetauthinstancedeprecated)替代。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**示例：**

```ts
import { userAuth } from '@kit.UserAuthenticationKit';

let auth = new userAuth.UserAuth();
```

#### \[h2\]getVersion(deprecated)

getVersion() : number

获取认证器的版本信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/z-VGrt2eSgy1hTeQBppyuA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=99B09F8D5C42731375A6827B2BB8D63E93A2E43FAD8D0C60B49127612967056F)

从 API version 8 开始支持，从 API version 9 开始废弃。

**需要权限：** ohos.permission.ACCESS\_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 认证器版本信息。 |

**示例：**

```ts
import { userAuth } from '@kit.UserAuthenticationKit';

let auth = new userAuth.UserAuth();
let version = auth.getVersion();
console.info(`auth version = ${version}`);
```

#### \[h2\]getAvailableStatus(deprecated)

getAvailableStatus(authType : UserAuthType, authTrustLevel : AuthTrustLevel) : number

查询指定类型和等级的认证能力是否支持。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/pG3Lo_SmT3uOJ3Q2vothyg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=F4ED8DDFCF233D030DED7F1AA65D6581050218253FE73B48FC9361477257363C)

从 API version 8 开始支持，从 API version 9 开始废弃，请使用[getAvailableStatus](#userauthgetavailablestatus9)替代。

**需要权限：** ohos.permission.ACCESS\_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| authType | [UserAuthType](#userauthtype8) | 是 | 认证类型，当前支持FACE和FINGERPRINT。 |
| authTrustLevel | [AuthTrustLevel](#authtrustlevel8) | 是 | 认证信任等级。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 查询结果，结果为SUCCESS时表示支持，其他返回值参见[ResultCode](#resultcodedeprecated)。 |

**示例：**

```ts
import { userAuth } from '@kit.UserAuthenticationKit';

let auth = new userAuth.UserAuth();
let checkCode = auth.getAvailableStatus(userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL1);
if (checkCode == userAuth.ResultCode.SUCCESS) {
  console.info('check auth support success');
} else {
  console.error(`check auth support fail, code = ${checkCode}`);
}
```

#### \[h2\]auth(deprecated)

auth(challenge: Uint8Array, authType: UserAuthType, authTrustLevel: AuthTrustLevel, callback: IUserAuthCallback): Uint8Array

执行用户认证，使用回调函数返回结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/w1V8CmGoQiaxstkEf_nAEg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=60A1E07E09DF72116EA5403767B345612B12FAD8207154844E5AFF75DFCFAAA8)

从 API version 8 开始支持，从 API version 9 开始废弃，请使用[start](#startdeprecated)代替。

**需要权限：** ohos.permission.ACCESS\_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| challenge | Uint8Array | 是 | 挑战值，可以传Uint8Array(\[\])。 |
| authType | [UserAuthType](#userauthtype8) | 是 | 认证类型，当前支持FACE和FINGERPRINT。 |
| authTrustLevel | [AuthTrustLevel](#authtrustlevel8) | 是 | 认证信任等级。 |
| callback | [IUserAuthCallback](#iuserauthcallbackdeprecated) | 是 | 回调函数。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Uint8Array | ContextId，作为取消认证[cancelAuth](#cancelauthdeprecated)接口的入参。 |

**示例：**

```ts
import { userAuth } from '@kit.UserAuthenticationKit';

let auth = new userAuth.UserAuth();
let challenge = new Uint8Array([]);
auth.auth(challenge, userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL1, {
  onResult: (result, extraInfo) => {
    try {
      console.info(`auth onResult result = ${result}`);
      console.info(`auth onResult extraInfo = ${JSON.stringify(extraInfo)}`);
      if (result == userAuth.ResultCode.SUCCESS) {
        // 此处添加认证成功逻辑。
      } else {
        // 此处添加认证失败逻辑。
      }
    } catch (error) {
      console.error(`auth onResult error = ${error}`);
    }
  }
});
```

#### \[h2\]cancelAuth(deprecated)

cancelAuth(contextID : Uint8Array) : number

表示通过contextID取消本次认证。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/jk1xvdJLSvCA2QfM6NVmfw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=739BB27E8E223CD989D5CDCE5128D912BC55D1B2825391AF88EAADC0D7D6957A)

从 API version 8 开始支持，从 API version 9 开始废弃，请使用[cancel](#canceldeprecated)代替。

**需要权限：** ohos.permission.ACCESS\_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| contextID | Uint8Array | 是 | 上下文的标识，通过[auth](#authdeprecated)接口获取。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 取消认证的结果，结果为SUCCESS时表示取消成功，其他返回值参见[ResultCode](#resultcodedeprecated)。 |

**示例：**

```ts
import { userAuth } from '@kit.UserAuthenticationKit';

// contextId可通过auth接口获取，此处直接定义。
let contextId = new Uint8Array([0, 1, 2, 3, 4, 5, 6, 7]);
let auth = new userAuth.UserAuth();
let cancelCode = auth.cancelAuth(contextId);
if (cancelCode == userAuth.ResultCode.SUCCESS) {
  console.info('cancel auth success');
} else {
  console.error('cancel auth fail');
}
```

#### IUserAuthCallback(deprecated)

返回认证结果的回调对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/shu64kRYQCyS71HVNrilsA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=5EB19150AAF64746AF6B982C9AF79569B263AEA5FF0686C053DB2FD9CD94F6F7)

从 API version 8 开始支持，从 API version 9 开始废弃，请使用[AuthEvent](#autheventdeprecated)代替。

#### \[h2\]onResult(deprecated)

onResult: (result : number, extraInfo : AuthResult) => void

回调函数，返回认证结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/FX_JmxX9SVGABbLjmDNv8A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=B4CF7C199713757F9B5C94A439E4D24971FB3A368BCD50945DE06FACF86AF876)

从 API version 8 开始支持，从 API version 9 开始废弃，请使用[callback](#callbackdeprecated)代替。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| result | number | 是 | 认证结果，参见[ResultCode](#resultcodedeprecated)。 |
| extraInfo | [AuthResult](#authresultdeprecated) | 是 | 
扩展信息，不同情况下的具体信息，

如果身份验证通过，则在extraInfo中返回用户认证令牌，

如果身份验证失败，则在extraInfo中返回剩余的用户认证次数，

如果身份验证执行器被锁定，则在extraInfo中返回冻结时间。

 |

**示例：**

```ts
import { userAuth } from '@kit.UserAuthenticationKit';

let auth = new userAuth.UserAuth();
let challenge = new Uint8Array([]);
auth.auth(challenge, userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL1, {
  onResult: (result, extraInfo) => {
    try {
      console.info(`auth onResult result = ${result}`);
      console.info(`auth onResult extraInfo = ${JSON.stringify(extraInfo)}`);
      if (result == userAuth.ResultCode.SUCCESS) {
        // 此处添加认证成功逻辑。
      }  else {
        // 此处添加认证失败逻辑。
      }
    } catch (error) {
      console.error(`auth onResult error = ${error}`);
    }
  }
});
```

#### \[h2\]onAcquireInfo(deprecated)

onAcquireInfo ?: (module : number, acquire : number, extraInfo : any) => void

回调函数，返回认证过程中的提示信息，非必须实现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/qN4g52swSrubKd7KXE5smQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=5F4ED2B55879051DF5C4C0902D0CB6C77A4FE9772FE680497492A94561CB22F6)

从 API version 8 开始支持，从 API version 9 开始废弃，请使用[callback](#callbackdeprecated)代替。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| module | number | 是 | 发送提示信息的模块标识。 |
| acquire | number | 是 | 认证执过程中的提示信息。 |
| extraInfo | any | 是 | 预留字段。 |

**示例：**

```ts
import { userAuth } from '@kit.UserAuthenticationKit';

let auth = new userAuth.UserAuth();
let challenge = new Uint8Array([]);
auth.auth(challenge, userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL1, {
  onResult: (result, extraInfo) => {
    try {
      console.info(`auth onResult result = ${result}`);
      console.info(`auth onResult extraInfo = ${JSON.stringify(extraInfo)}`);
      if (result == userAuth.ResultCode.SUCCESS) {
        // 此处添加认证成功逻辑。
      }  else {
        // 此处添加认证失败逻辑。
      }
    } catch (error) {
      console.error(`auth onResult error = ${error}`);
    }
  },
  onAcquireInfo: (module, acquire, extraInfo : userAuth.AuthResult) => {
    try {
      console.info(`auth onAcquireInfo module = ${module}`);
      console.info(`auth onAcquireInfo acquire = ${acquire}`);
      console.info(`auth onAcquireInfo extraInfo = ${JSON.stringify(extraInfo)}`);
    } catch (error) {
      console.error(`auth onAcquireInfo error = ${error}`);
    }
  }
});
```

#### AuthResult(deprecated)

表示认证结果的对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/i3ChAWqXQvyQHFLQSB-mzg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=145FE11234B820ED42ED101701A76209718318FA2670C6F2EC336920DEB4698E)

从 API version 8 开始支持，从 API version 9 开始废弃，请使用[AuthResultInfo](#authresultinfodeprecated)代替。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| token | Uint8Array | 否 | 是 | 认证成功的令牌信息。 |
| remainTimes | number | 否 | 是 | 剩余的认证操作次数。 |
| freezingTime | number | 否 | 是 | 认证操作的冻结时间。单位为毫秒。 |

#### ResultCode(deprecated)

表示返回码的枚举。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/Nnsg3yr5S-ebxPk6RCIAPQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=AF902EFD86C6EB8246AA9A0D5B9A60A58D93062BBC7A2EB441EF92A29359F90B)

从 API version 8 开始支持，从 API version 9 开始废弃，请使用[UserAuthResultCode](#userauthresultcode9)代替。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| SUCCESS | 0 | 执行成功。 |
| FAIL | 1 | 认证失败。 |
| GENERAL\_ERROR | 2 | 操作通用错误。 |
| CANCELED | 3 | 操作取消。 |
| TIMEOUT | 4 | 操作超时。 |
| TYPE\_NOT\_SUPPORT | 5 | 不支持的认证类型。 |
| TRUST\_LEVEL\_NOT\_SUPPORT | 6 | 不支持的认证等级。 |
| BUSY | 7 | 忙碌状态。 |
| INVALID\_PARAMETERS | 8 | 无效参数。 |
| LOCKED | 9 | 认证器已锁定。 |
| NOT\_ENROLLED | 10 | 用户未录入认证信息。 |

#### FaceTips(deprecated)

表示人脸认证过程中提示码的枚举。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/TSzmJiEcSNyOzEg4rf_qeg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=66E5F60C429A99D417D5356DEB48ED290BD0BA3A6DE25C0020F9FCD9EF262C64)

从 API version 8 开始支持，从 API version 11 开始废弃。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| FACE\_AUTH\_TIP\_TOO\_BRIGHT | 1 | 光线太强，获取的图像太亮。 |
| FACE\_AUTH\_TIP\_TOO\_DARK | 2 | 光线太暗，获取的图像太暗。 |
| FACE\_AUTH\_TIP\_TOO\_CLOSE | 3 | 人脸距离设备过近。 |
| FACE\_AUTH\_TIP\_TOO\_FAR | 4 | 人脸距离设备过远。 |
| FACE\_AUTH\_TIP\_TOO\_HIGH | 5 | 设备太高，仅获取到人脸上部。 |
| FACE\_AUTH\_TIP\_TOO\_LOW | 6 | 设备太低，仅获取到人脸下部。 |
| FACE\_AUTH\_TIP\_TOO\_RIGHT | 7 | 设备太靠右，仅获取到人脸右部。 |
| FACE\_AUTH\_TIP\_TOO\_LEFT | 8 | 设备太靠左，仅获取到人脸左部。 |
| FACE\_AUTH\_TIP\_TOO\_MUCH\_MOTION | 9 | 在图像采集过程中，用户人脸移动太快。 |
| FACE\_AUTH\_TIP\_POOR\_GAZE | 10 | 没有正视摄像头。 |
| FACE\_AUTH\_TIP\_NOT\_DETECTED | 11 | 没有检测到人脸信息。 |

#### FingerprintTips(deprecated)

表示指纹认证过程中提示码的枚举。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/n3NCup_8QVCTgIsiOIBDwg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=7B3A1E307AF1882D710365419F8912FB43FDC6B4D1E29DD1D65F74D0669EE6FF)

从 API version 8 开始支持，从 API version 11 开始废弃。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| FINGERPRINT\_AUTH\_TIP\_GOOD | 0 | 获取的指纹图像良好。 |
| FINGERPRINT\_AUTH\_TIP\_DIRTY | 1 | 由于传感器上可疑或检测到的污垢，指纹图像噪音过大。 |
| FINGERPRINT\_AUTH\_TIP\_INSUFFICIENT | 2 | 由于检测到的情况，指纹图像噪声太大，无法处理。 |
| FINGERPRINT\_AUTH\_TIP\_PARTIAL | 3 | 仅检测到部分指纹图像。 |
| FINGERPRINT\_AUTH\_TIP\_TOO\_FAST | 4 | 快速移动，指纹图像不完整。 |
| FINGERPRINT\_AUTH\_TIP\_TOO\_SLOW | 5 | 缺少运动，指纹图像无法读取。 |

#### UserAuthType8+

表示身份认证的凭据类型枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| PIN10+ | 1 | 口令认证。 |
| FACE | 2 | 人脸认证。 |
| FINGERPRINT | 4 | 指纹认证。 |

#### AuthTrustLevel8+

表示认证结果的信任等级枚举。

典型场景及举例可参考[认证可信等级划分原则](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/user-authentication-overview#生物认证可信等级划分原则)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| ATL1 | 10000 | 认证结果的信任等级级别1，表示该认证方案能够识别用户个体，具备一定的活体检测能力。适用于业务风控、一般个人数据查询等场景。 |
| ATL2 | 20000 | 认证结果的信任等级级别2，表示该认证方案能够精确识别用户个体，具备一定的活体检测能力。适用于维持设备解锁状态、应用登录等场景。 |
| ATL3 | 30000 | 认证结果的信任等级级别3，表示该认证方案能够精确识别用户个体，具备较强的活体检测能力。适用于设备解锁等场景。 |
| ATL4 | 40000 | 认证结果的信任等级级别4，表示该认证方案能够高精度的识别用户个体，具备很强的活体检测能力。适用于小额支付等场景。 |

#### SecureLevel(deprecated)

type SecureLevel = string

表示认证的安全级别。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/wrTR6pIdQV-Vsr-N2vU7zg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=E62A57F0C2D30AC6249ED4605BF8187AF014A97537EC792794695F1BCBF8F754)

从 API version 6 开始支持，从 API version 8 开始废弃，请使用[AuthTrustLevel](#authtrustlevel8)替代。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 类型 | 说明 |
| :-- | :-- |
| string | 
表示类型为字符，认证的安全级别包括：'S1' | 'S2'|'S3'|'S4'。

\- 'S1'：认证结果的信任等级级别1，代表该认证方案能够识别用户个体，有一定的活体检测能力。常用的业务场景有业务风控、一般个人数据查询等。

\- 'S2'：认证结果的信任等级级别2，代表该认证方案能够精确识别用户个体，有一定的活体检测能力。常用的业务场景有维持设备解锁状态，应用登录等。

\- 'S3'：认证结果的信任等级级别3，代表该认证方案能够精确识别用户个体，有较强的活体检测能力。常用的业务场景有设备解锁等。

\- 'S4'：认证结果的信任等级级别4，代表该认证方案能够高精度的识别用户个体，有很强的活体检测能力。常用的业务场景有小额支付等。

 |

#### AuthType(deprecated)

type AuthType = string

表示认证类型。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/vZrg_l12TN6Xmip39-o_IQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=D9947E865B70577B255A3D02E13896E8BA5C325E1D82282038FE18591701BB83)

从 API version 6 开始支持，从 API version 8 开始废弃，请使用[UserAuthType](#userauthtype8)替代。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 类型 | 说明 |
| :-- | :-- |
| string | 
表示认证类型为字符，认证类型包括：'ALL'|'FACE\_ONLY'。

\- 'ALL'：预留参数，当前版本暂不支持ALL类型的认证。

\- 'FACE\_ONLY'：人脸认证。

 |

#### userAuth.getAuthenticator(deprecated)

getAuthenticator(): Authenticator

获取Authenticator对象，用于执行用户身份认证。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/NDH4VIBMSCyJd-geOj5HBQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=4D312F0DF04E19F7758E9DEEDB41C6D8AF376FF9264643345D26F47458FA8FC0)

从 API version 6 开始支持，从 API version 8 开始废弃，请使用[getAuthInstance](#userauthgetauthinstancedeprecated)替代。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [Authenticator](#authenticatordeprecated) | 认证器对象。 |

**示例：**

```ts
import { userAuth } from '@kit.UserAuthenticationKit';

let authenticator = userAuth.getAuthenticator();
```

#### Authenticator(deprecated)

认证器对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/mUlSSy-lTOOiM5Hj9eAsAA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=FA228633899345276363037A2788C514138FF2F700A98AB542E8D9B6CACF064F)

从 API version 6 开始支持，从 API version 8 开始废弃，请使用[AuthInstance](#authinstancedeprecated)替代。

#### \[h2\]execute(deprecated)

execute(type: AuthType, level: SecureLevel, callback: AsyncCallback<number>): void

执行用户认证，使用callback方式作为异步方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/L-2wr_eDQL6PUJGDcesc5Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=F18A052C5C140939136EDF72023E6D07E72CB117D67B9FEEC69E9AAEB0DEB209)

从 API version 6 开始支持，从 API version 8 开始废弃，请使用[start](#startdeprecated)替代。

**需要权限：** ohos.permission.ACCESS\_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | AuthType | 是 | 
认证类型，当前只支持"FACE\_ONLY"。

ALL为预留参数。当前版本暂不支持ALL类型的认证。

 |
| level | SecureLevel | 是 | 

安全级别，对应认证的安全级别，有效值为"S1"（最低）、"S2"、"S3"、"S4"（最高）。

具备3D人脸识别能力的设备支持"S3"及以下安全级别的认证。

具备2D人脸识别能力的设备支持"S2"及以下安全级别的认证。

 |
| callback | AsyncCallback<number> | 是 | 回调函数。number表示认证结果，参见[AuthenticationResult](#authenticationresultdeprecated)。 |

**示例：**

```ts
import { userAuth } from '@kit.UserAuthenticationKit';

let authenticator = userAuth.getAuthenticator();
authenticator.execute('FACE_ONLY', 'S2', (error, code)=>{
  if (code === userAuth.ResultCode.SUCCESS) {
    console.info('auth success');
    return;
  }
  console.error(`auth fail, code = ${code}`);
});
```

#### \[h2\]execute(deprecated)

execute(type : AuthType, level : SecureLevel): Promise<number>

执行用户认证，使用promise方式作为异步方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/Ch54-3Q2Sg2HT9BfKoxKtQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=0B602584F880B3A40947DD97A6F4311E3B0A42391B9C6FABCE70440BA1A27AB8)

从 API version 6 开始支持，从 API version 8 开始废弃，请使用[start](#startdeprecated)替代。

**需要权限：** ohos.permission.ACCESS\_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | AuthType | 是 | 
认证类型，当前只支持"FACE\_ONLY"。

ALL为预留参数。当前版本暂不支持ALL类型的认证。

 |
| level | SecureLevel | 是 | 

安全级别，对应认证的安全级别，有效值为"S1"（最低）、"S2"、"S3"、"S4"（最高）。

具备3D人脸识别能力的设备支持"S3"及以下安全级别的认证。

具备2D人脸识别能力的设备支持"S2"及以下安全级别的认证。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | 返回携带一个number的Promise。number 为认证结果，参见[AuthenticationResult](#authenticationresultdeprecated)。 |

**示例：**

```ts
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  let authenticator = userAuth.getAuthenticator();
  authenticator.execute('FACE_ONLY', 'S2').then((code)=>{
    console.info('auth success');
  })
} catch (error) {
  console.error(`auth fail, code = ${error}`);
}
```

#### AuthenticationResult(deprecated)

表示认证结果的枚举。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/doNeg_0hSYGtT1jWd7dDjw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=8A10326F74958F89FFE194CF0C18E8DD529C6A7A9FA36A353E4F68EE18D03F25)

从 API version 6 开始支持，从 API version 8 开始废弃，请使用[ResultCode](#resultcodedeprecated)替代。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| NO\_SUPPORT | \-1 | 设备不支持当前的认证方式。 |
| SUCCESS | 0 | 认证成功。 |
| COMPARE\_FAILURE | 1 | 比对失败。 |
| CANCELED | 2 | 用户取消认证。 |
| TIMEOUT | 3 | 认证超时。 |
| CAMERA\_FAIL | 4 | 开启相机失败。 |
| BUSY | 5 | 认证服务忙，请稍后重试。 |
| INVALID\_PARAMETERS | 6 | 认证参数无效。 |
| LOCKED | 7 | 认证失败次数过多，已锁定。 |
| NOT\_ENROLLED | 8 | 未录入认证凭据。 |
| GENERAL\_ERROR | 100 | 其他错误。 |

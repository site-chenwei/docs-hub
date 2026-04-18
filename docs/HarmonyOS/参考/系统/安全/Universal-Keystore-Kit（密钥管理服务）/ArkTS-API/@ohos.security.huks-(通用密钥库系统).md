---
title: "@ohos.security.huks (通用密钥库系统)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huks"
menu_path:
  - "参考"
  - "系统"
  - "安全"
  - "Universal Keystore Kit（密钥管理服务）"
  - "ArkTS API"
  - "@ohos.security.huks (通用密钥库系统)"
captured_at: "2026-04-17T01:48:20.552Z"
---

# @ohos.security.huks (通用密钥库系统)

向应用提供密钥库能力，包括密钥管理及密钥的密码学操作等功能。

HUKS所管理的密钥可以由应用导入或者由应用调用HUKS接口生成。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/XasxbugySpmpFjOIweiE4w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014821Z&HW-CC-Expire=86400&HW-CC-Sign=3A4DCFF1F895D2E1F03D81FF4DD052EEEAB271A32EC8D8AA5ADE3688E78FD304)

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import { huks } from '@kit.UniversalKeystoreKit';
```

#### HuksParam

调用接口使用的options中的properties数组中的param。

**系统能力：** SystemCapability.Security.Huks.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| tag | [HuksTag](#hukstag) | 否 | 否 | 
标签。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| value | boolean|number|bigint|Uint8Array | 否 | 否 | 

标签对应值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |

#### HuksOptions

调用接口使用的options。

**系统能力：** SystemCapability.Security.Huks.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| properties | Array<[HuksParam](#huksparam)\> | 否 | 是 | 
属性，用于存HuksParam的数组。默认为空。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| inData | Uint8Array | 否 | 是 | 

输入数据。默认为空。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |

#### HuksSessionHandle9+

huks Handle结构体。

**系统能力：** SystemCapability.Security.Huks.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| handle | number | 否 | 否 | 
表示无符号整数类型的handle值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| challenge | Uint8Array | 否 | 是 | 

表示[initSession](#huksinitsession9)操作之后获取到的challenge信息。默认为空。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |

#### HuksReturnResult9+

调用接口返回的result。

**系统能力：** SystemCapability.Security.Huks.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| outData | Uint8Array | 否 | 是 | 
表示输出数据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| properties | Array<[HuksParam](#huksparam)\> | 否 | 是 | 

表示属性信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| certChains | Array<string> | 否 | 是 | 

表示证书链数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |

#### HuksListAliasesReturnResult12+

调用接口返回的result。

**系统能力**：SystemCapability.Security.Huks.Extension

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| keyAliases | Array<string> | 否 | 否 | 
表示密钥别名集。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |

#### huks.generateKeyItem9+

generateKeyItem(keyAlias: string, options: HuksOptions, callback: AsyncCallback<void>) : void

生成密钥。使用callback异步回调。

基于密钥不出TEE原则，此接口不会返回密钥材料内容，只用于表示此次调用是否成功。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| keyAlias | string | 是 | 密钥别名。密钥别名的最大长度为128字节，建议不包含个人信息等敏感词汇。 |
| options | [HuksOptions](#huksoptions) | 是 | 用于存放生成key所需TAG。其中密钥使用的算法、密钥用途、密钥长度为必选参数。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当生成密钥成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[HUKS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-huks)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | api is not supported. |
| 12000001 | algorithm mode is not supported. |
| 12000002 | algorithm param is missing. |
| 12000003 | algorithm param is invalid. |
| 12000004 | operating file failed. |
| 12000005 | IPC communication failed. |
| 12000006 | error occurred in crypto engine. |
| 12000012 | Device environment or input parameter abnormal. |
| 12000013 | queried credential does not exist. |
| 12000014 | memory is insufficient. |
| 12000015 | Failed to obtain the security information via UserIAM. |
| 12000017 | The key with same alias is already exist. |
| 12000018 | the group id specified by the access group tag is invalid. |

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';

/* 以生成ECC256密钥为例 */
let keyAlias: string = 'keyAlias';
let properties: Array<huks.HuksParam> = [
  {
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_ECC
  },
  {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_ECC_KEY_SIZE_256
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
  },
  {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
  },
];
let options: huks.HuksOptions = {
  properties: properties
};
huks.generateKeyItem(keyAlias, options, (error, data) => {
  if (error) {
    console.error(`callback: generateKeyItem failed`);
  } else {
    console.info(`callback: generateKeyItem key success`);
  }
});
```

#### huks.generateKeyItem9+

generateKeyItem(keyAlias: string, options: HuksOptions) : Promise<void>

生成密钥。使用Promise异步回调。

基于密钥不出TEE原则，此接口不会返回密钥材料内容，只用于表示此次调用是否成功。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| keyAlias | string | 是 | 密钥别名。密钥别名的最大长度为128字节，建议不包含个人信息等敏感词汇。 |
| options | [HuksOptions](#huksoptions) | 是 | 用于存放生成key所需TAG。其中密钥使用的算法、密钥用途、密钥长度为必选参数。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[HUKS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-huks)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | api is not supported. |
| 12000001 | algorithm mode is not supported. |
| 12000002 | algorithm param is missing. |
| 12000003 | algorithm param is invalid. |
| 12000004 | operating file failed. |
| 12000005 | IPC communication failed. |
| 12000006 | error occurred in crypto engine. |
| 12000012 | Device environment or input parameter abnormal. |
| 12000013 | queried credential does not exist. |
| 12000014 | memory is insufficient. |
| 12000015 | Failed to obtain the security information via UserIAM. |
| 12000017 | The key with same alias is already exist. |
| 12000018 | the group id specified by the access group tag is invalid. |

**示例：**

```ts
/* 以生成ECC256密钥为例 */
import { huks } from '@kit.UniversalKeystoreKit';

let keyAlias = 'keyAlias';
let properties: Array<huks.HuksParam> = [
  {
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_ECC
  },
  {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_ECC_KEY_SIZE_256
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
  },
  {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
  },
];
let options: huks.HuksOptions = {
  properties: properties
};
huks.generateKeyItem(keyAlias, options)
  .then((data) => {
    console.info(`promise: generateKeyItem success`);
  });
```

#### huks.deleteKeyItem9+

deleteKeyItem(keyAlias: string, options: HuksOptions, callback: AsyncCallback<void>) : void

删除密钥。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| keyAlias | string | 是 | 密钥别名，应为生成key时传入的别名。 |
| options | [HuksOptions](#huksoptions) | 是 | 
用于删除密钥时指定密钥的属性，如使用[HuksAuthStorageLevel](#huksauthstoragelevel11)指定需删除密钥的安全级别，

可传空，当API version ≥ 12时，传空默认为CE，当API version ＜ 12时，传空默认为DE。

 |
| callback | AsyncCallback<void> | 是 | 回调函数。当删除密钥成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[HUKS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-huks)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | api is not supported. |
| 12000004 | operating file failed. |
| 12000005 | IPC communication failed. |
| 12000011 | queried entity does not exist. |
| 12000012 | Device environment or input parameter abnormal. |
| 12000014 | memory is insufficient. |
| 12000018 | the group id specified by the access group tag is invalid. |

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';

/* 此处options选择emptyOptions传空 */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};
huks.deleteKeyItem(keyAlias, emptyOptions, (error, data) => {
  if (error) {
    console.error(`callback: deleteKeyItem failed`);
  } else {
    console.info(`callback: deleteKeyItem key success`);
  }
});
```

#### huks.deleteKeyItem9+

deleteKeyItem(keyAlias: string, options: HuksOptions) : Promise<void>

删除密钥。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| keyAlias | string | 是 | 密钥别名，应为生成key时传入的别名。 |
| options | [HuksOptions](#huksoptions) | 是 | 
用于删除时指定密钥的属性TAG，如使用[HuksAuthStorageLevel](#huksauthstoragelevel11)指定需删除密钥的安全级别，

可传空，当API version ≥ 12时，传空默认为CE，当API version ＜ 12时，传空默认为DE。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[HUKS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-huks)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | api is not supported. |
| 12000004 | operating file failed. |
| 12000005 | IPC communication failed. |
| 12000011 | queried entity does not exist. |
| 12000012 | Device environment or input parameter abnormal. |
| 12000014 | memory is insufficient. |
| 12000018 | the group id specified by the access group tag is invalid. |

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';

/* 此处options选择emptyOptions传空 */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};
huks.deleteKeyItem(keyAlias, emptyOptions)
  .then((data) => {
    console.info(`promise: deleteKeyItem key success`);
  });
```

#### huks.importKeyItem9+

importKeyItem(keyAlias: string, options: HuksOptions, callback: AsyncCallback<void>) : void

导入明文密钥。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

API version 9-11系统能力为SystemCapability.Security.Huks.Extension；从API version 12开始为SystemCapability.Security.Huks.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| keyAlias | string | 是 | 密钥别名。密钥别名的最大长度为128字节，建议不包含个人信息等敏感词汇。 |
| options | [HuksOptions](#huksoptions) | 是 | 用于导入时所需TAG和需要导入的密钥。其中密钥使用的算法、密钥用途、密钥长度为必选参数。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当导入密钥成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[HUKS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-huks)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | api is not supported. |
| 12000001 | algorithm mode is not supported. |
| 12000002 | algorithm param is missing. |
| 12000003 | algorithm param is invalid. |
| 12000004 | operating file failed. |
| 12000005 | IPC communication failed. |
| 12000006 | error occurred in crypto engine. |
| 12000012 | Device environment or input parameter abnormal. |
| 12000013 | queried credential does not exist. |
| 12000014 | memory is insufficient. |
| 12000015 | Failed to obtain the security information via UserIAM. |
| 12000017 | The key with same alias is already exist. |
| 12000018 | the group id specified by the access group tag is invalid. |

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';

/* 以导入AES256密钥为例 */
let plainTextSize32 = makeRandomArr(32);

function makeRandomArr(size: number) {
  let arr = new Uint8Array(size);
  for (let i = 0; i < size; i++) {
    arr[i] = Math.floor(Math.random() * 10);
  }
  return arr;
};
let keyAlias = 'keyAlias';
let properties: Array<huks.HuksParam> = [
  {
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_AES
  },
  {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value:
    huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_PKCS7
  },
  {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_ECB
  }
];
let options: huks.HuksOptions = {
  properties: properties,
  inData: plainTextSize32
};
huks.importKeyItem(keyAlias, options, (error, data) => {
  if (error) {
    console.error(`callback: importKeyItem failed`);
  } else {
    console.info(`callback: importKeyItem success`);
  }
});
```

#### huks.importKeyItem9+

importKeyItem(keyAlias: string, options: HuksOptions) : Promise<void>

导入明文密钥。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| keyAlias | string | 是 | 密钥别名。密钥别名的最大长度为128字节，建议不包含个人信息等敏感词汇。 |
| options | [HuksOptions](#huksoptions) | 是 | 用于导入时所需TAG和需要导入的密钥。其中密钥使用的算法、密钥用途、密钥长度为必选参数。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[HUKS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-huks)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | api is not supported. |
| 12000001 | algorithm mode is not supported. |
| 12000002 | algorithm param is missing. |
| 12000003 | algorithm param is invalid. |
| 12000004 | operating file failed. |
| 12000005 | IPC communication failed. |
| 12000006 | error occurred in crypto engine. |
| 12000012 | Device environment or input parameter abnormal. |
| 12000013 | queried credential does not exist. |
| 12000014 | memory is insufficient. |
| 12000015 | Failed to obtain the security information via UserIAM. |
| 12000017 | The key with same alias is already exist. |
| 12000018 | the group id specified by the access group tag is invalid. |

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';

/* 以导入AES256为例 */
function makeRandomArr(size: number) {
  let arr = new Uint8Array(size);
  for (let i = 0; i < size; i++) {
    arr[i] = Math.floor(Math.random() * 10);
  }
  return arr;
};

/* 第一步：生成密钥 */
let plainTextSize32 = makeRandomArr(32);
let keyAlias = 'keyAlias';
let properties: Array<huks.HuksParam> = [
  {
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_AES
  },
  {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_PKCS7
  },
  {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_ECB
  }
];
let huksOptions: huks.HuksOptions = {
  properties: properties,
  inData: plainTextSize32
};
/* 第二步：导入密钥 */
huks.importKeyItem(keyAlias, huksOptions)
  .then((data) => {
    console.info(`promise: importKeyItem success`);
  });
```

#### huks.attestKeyItem9+

attestKeyItem(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksReturnResult>) : void

获取密钥证书。使用callback异步回调。

**需要权限**：ohos.permission.ATTEST\_KEY，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Security.Huks.Extension

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/G_FB9y6KQrGITRuc8l9jeQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014821Z&HW-CC-Expire=86400&HW-CC-Sign=C7690B9D9E67CA6A211B26C639BB71831F74BD37BE8C2055F0BB5DACF9CAC3E1)

使用非匿名证书密钥证明时生成的证书链包含设备标识符，设备标识符的使用、留存、销毁由开发者决定，开发者需在隐私声明中对其使用目的，留存策略和销毁方式进行说明。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| keyAlias | string | 是 | 密钥别名，存放待获取证书密钥的别名。 |
| options | [HuksOptions](#huksoptions) | 是 | 用于获取证书时指定所需参数与数据。 |
| callback | AsyncCallback<[HuksReturnResult](#huksreturnresult9)\> | 是 | 回调函数。当获取密钥证书成功时，err为undefined，data为获取到的HuksReturnResult；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[HUKS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-huks)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | check permission failed. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | api is not supported. |
| 12000001 | algorithm mode is not supported. |
| 12000004 | operating file failed. |
| 12000005 | IPC communication failed. |
| 12000006 | error occurred in crypto engine. |
| 12000011 | queried entity does not exist. |
| 12000012 | Device environment or input parameter abnormal. |
| 12000014 | memory is insufficient. |
| 12000018 | the group id specified by the access group tag is invalid. |

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';

function stringToUint8Array(str: string) {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  let tmpUint8Array = new Uint8Array(arr);
  return tmpUint8Array;
}

let securityLevel = stringToUint8Array('sec_level');
let challenge = stringToUint8Array('challenge_data');
let versionInfo = stringToUint8Array('version_info');
let keyAliasString = "key attest";

async function generateKeyThenAttestKey() {
  let aliasString = keyAliasString;
  let aliasUint8 = stringToUint8Array(aliasString);
  let generateProperties: Array<huks.HuksParam> = [
    {
      tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
      value: huks.HuksKeyAlg.HUKS_ALG_RSA
    },
    {
      tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
      value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
    },
    {
      tag: huks.HuksTag.HUKS_TAG_PURPOSE,
      value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
    },
    {
      tag: huks.HuksTag.HUKS_TAG_DIGEST,
      value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
    },
    {
      tag: huks.HuksTag.HUKS_TAG_PADDING,
      value: huks.HuksKeyPadding.HUKS_PADDING_PSS
    },
    {
      tag: huks.HuksTag.HUKS_TAG_KEY_GENERATE_TYPE,
      value: huks.HuksKeyGenerateType.HUKS_KEY_GENERATE_TYPE_DEFAULT
    },
    {
      tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
      value: huks.HuksCipherMode.HUKS_MODE_ECB
    }
  ];
  let generateOptions: huks.HuksOptions = {
    properties: generateProperties
  };
  let attestProperties: Array<huks.HuksParam> = [
    {
      tag: huks.HuksTag.HUKS_TAG_ATTESTATION_ID_SEC_LEVEL_INFO,
      value: securityLevel
    },
    {
      tag: huks.HuksTag.HUKS_TAG_ATTESTATION_CHALLENGE,
      value: challenge
    },
    {
      tag: huks.HuksTag.HUKS_TAG_ATTESTATION_ID_VERSION_INFO,
      value: versionInfo
    },
    {
      tag: huks.HuksTag.HUKS_TAG_ATTESTATION_ID_ALIAS,
      value: aliasUint8
    }
  ];
  let attestOptions: huks.HuksOptions = {
    properties: attestProperties
  };
  huks.generateKeyItem(aliasString, generateOptions, (error, data) => {
    if (error) {
      console.error(`callback: generateKeyItem failed`);
    } else {
      console.info(`callback: generateKeyItem success`);
      huks.attestKeyItem(aliasString, attestOptions, (error, data) => {
        if (error) {
          console.error(`callback: attestKeyItem failed`);
        } else {
          console.info(`callback: attestKeyItem success`);
        }
      });
    }
  });
}
```

#### huks.attestKeyItem9+

attestKeyItem(keyAlias: string, options: HuksOptions) : Promise<HuksReturnResult>

获取密钥证书。使用Promise异步回调。

**需要权限**：ohos.permission.ATTEST\_KEY，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Security.Huks.Extension

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/73LLwa3FSX2WDgQ3f36Bmg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014821Z&HW-CC-Expire=86400&HW-CC-Sign=FBF2FD35F4CE169C47F1E6D2AF813E1527D74AADE099E7070D42E1B34CBB800F)

使用非匿名证书密钥证明时生成的证书链包含设备标识符，设备标识符的使用、留存、销毁由开发者决定，开发者需在隐私声明中对其使用目的，留存策略和销毁方式进行说明。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| keyAlias | string | 是 | 密钥别名，存放待获取证书密钥的别名。 |
| options | [HuksOptions](#huksoptions) | 是 | 用于获取证书时指定所需参数与数据。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[HuksReturnResult](#huksreturnresult9)\> | Promise对象。当调用成功时，HuksReturnResult的certChains成员非空，为获取到的证书链。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[HUKS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-huks)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | check permission failed. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | api is not supported. |
| 12000001 | algorithm mode is not supported. |
| 12000004 | operating file failed. |
| 12000005 | IPC communication failed. |
| 12000006 | error occurred in crypto engine. |
| 12000011 | queried entity does not exist. |
| 12000012 | Device environment or input parameter abnormal. |
| 12000014 | memory is insufficient. |
| 12000018 | the group id specified by the access group tag is invalid. |

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';

function stringToUint8Array(str: string) {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  let tmpUint8Array = new Uint8Array(arr);
  return tmpUint8Array;
}

let securityLevel = stringToUint8Array('sec_level');
let challenge = stringToUint8Array('challenge_data');
let versionInfo = stringToUint8Array('version_info');
let keyAliasString = "key attest";

async function generateKey(alias: string) {
  let properties: Array<huks.HuksParam> = [
    {
      tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
      value: huks.HuksKeyAlg.HUKS_ALG_RSA
    },
    {
      tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
      value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
    },
    {
      tag: huks.HuksTag.HUKS_TAG_PURPOSE,
      value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
    },
    {
      tag: huks.HuksTag.HUKS_TAG_DIGEST,
      value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
    },
    {
      tag: huks.HuksTag.HUKS_TAG_PADDING,
      value: huks.HuksKeyPadding.HUKS_PADDING_PSS
    },
    {
      tag: huks.HuksTag.HUKS_TAG_KEY_GENERATE_TYPE,
      value: huks.HuksKeyGenerateType.HUKS_KEY_GENERATE_TYPE_DEFAULT
    },
    {
      tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
      value: huks.HuksCipherMode.HUKS_MODE_ECB
    }
  ];
  let options: huks.HuksOptions = {
    properties: properties
  };
  await huks.generateKeyItem(alias, options)
    .then((data) => {
      console.info(`promise: generateKeyItem success`);
    });
}

async function attestKey() {
  let aliasString = keyAliasString;
  let aliasUint8 = stringToUint8Array(aliasString);
  let properties: Array<huks.HuksParam> = [
    {
      tag: huks.HuksTag.HUKS_TAG_ATTESTATION_ID_SEC_LEVEL_INFO,
      value: securityLevel
    },
    {
      tag: huks.HuksTag.HUKS_TAG_ATTESTATION_CHALLENGE,
      value: challenge
    },
    {
      tag: huks.HuksTag.HUKS_TAG_ATTESTATION_ID_VERSION_INFO,
      value: versionInfo
    },
    {
      tag: huks.HuksTag.HUKS_TAG_ATTESTATION_ID_ALIAS,
      value: aliasUint8
    }
  ];
  let options: huks.HuksOptions = {
    properties: properties
  };
  await generateKey(aliasString);
  await huks.attestKeyItem(aliasString, options)
    .then((data) => {
      console.info(`promise: attestKeyItem success`);
    });
}
```

#### huks.anonAttestKeyItem11+

anonAttestKeyItem(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksReturnResult>) : void

获取匿名化密钥证书。使用callback异步回调。

该操作需要联网进行，且耗时较长。返回12000012错误码时，可能是由于网络异常导致。此时如果没有联网，需要提示用户网络没有连接，如果已经联网，可能是由于网络抖动导致失败，建议重试。

密钥证明证书格式说明请参考[应用真实性证明-密钥证明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/device-attestation-servers#section8815174119330)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| keyAlias | string | 是 | 密钥别名，存放待获取证书密钥的别名。 |
| options | [HuksOptions](#huksoptions) | 是 | 用于获取证书时指定所需参数与数据。 |
| callback | AsyncCallback<[HuksReturnResult](#huksreturnresult9)\> | 是 | 回调函数。当获取匿名化密钥证书成功时，err为undefined，data为获取到的HuksReturnResult；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[HUKS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-huks)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | api is not supported. |
| 12000001 | algorithm mode is not supported. |
| 12000004 | operating file failed. |
| 12000005 | IPC communication failed. |
| 12000006 | error occurred in crypto engine. |
| 12000011 | queried entity does not exist. |
| 12000012 | Device environment or input parameter abnormal. |
| 12000014 | memory is insufficient. |
| 12000018 | the group id specified by the access group tag is invalid. |

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';

function stringToUint8Array(str: string): Uint8Array {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  let tmpUint8Array = new Uint8Array(arr);
  return tmpUint8Array;
}

let securityLevel = stringToUint8Array('sec_level');
let challenge = stringToUint8Array('challenge_data');
let versionInfo = stringToUint8Array('version_info');
let keyAliasString = "key anon attest";

async function generateKeyThenAttestKey(): Promise<void> {
  let aliasString = keyAliasString;
  let aliasUint8 = stringToUint8Array(aliasString);
  let generateProperties: Array<huks.HuksParam> = [
    {
      tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
      value: huks.HuksKeyAlg.HUKS_ALG_RSA
    },
    {
      tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
      value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
    },
    {
      tag: huks.HuksTag.HUKS_TAG_PURPOSE,
      value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
    },
    {
      tag: huks.HuksTag.HUKS_TAG_DIGEST,
      value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
    },
    {
      tag: huks.HuksTag.HUKS_TAG_PADDING,
      value: huks.HuksKeyPadding.HUKS_PADDING_PSS
    },
    {
      tag: huks.HuksTag.HUKS_TAG_KEY_GENERATE_TYPE,
      value: huks.HuksKeyGenerateType.HUKS_KEY_GENERATE_TYPE_DEFAULT
    },
    {
      tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
      value: huks.HuksCipherMode.HUKS_MODE_ECB
    }
  ];
  let generateOptions: huks.HuksOptions = {
    properties: generateProperties
  };
  let anonAttestProperties: Array<huks.HuksParam> = [
    {
      tag: huks.HuksTag.HUKS_TAG_ATTESTATION_ID_SEC_LEVEL_INFO,
      value: securityLevel
    },
    {
      tag: huks.HuksTag.HUKS_TAG_ATTESTATION_CHALLENGE,
      value: challenge
    },
    {
      tag: huks.HuksTag.HUKS_TAG_ATTESTATION_ID_VERSION_INFO,
      value: versionInfo
    },
    {
      tag: huks.HuksTag.HUKS_TAG_ATTESTATION_ID_ALIAS,
      value: aliasUint8
    }
  ];
  let anonAttestOptions: huks.HuksOptions = {
    properties: anonAttestProperties
  };
  huks.generateKeyItem(aliasString, generateOptions, (error, data) => {
    if (error) {
      console.error(`callback: generateKeyItem failed`);
    } else {
      console.info(`callback: generateKeyItem success`);
      huks.anonAttestKeyItem(aliasString, anonAttestOptions, (error, data) => {
        if (error) {
          console.error(`callback: anonAttestKeyItem failed`);
        } else {
          console.info(`callback: anonAttestKeyItem success`);
        }
      });
    }
  });
}
```

#### huks.anonAttestKeyItem11+

anonAttestKeyItem(keyAlias: string, options: HuksOptions) : Promise<HuksReturnResult>

获取匿名化密钥证书。使用Promise异步回调。

该操作需要联网进行，且耗时较长。返回12000012错误码时，可能是由于网络异常导致。此时如果没有联网，需要提示用户网络没有连接，如果已经联网，可能是由于网络抖动导致失败，建议重试。

密钥证明证书格式说明请参考[应用真实性证明-密钥证明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/device-attestation-servers#section8815174119330)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| keyAlias | string | 是 | 密钥别名，存放待获取证书密钥的别名。 |
| options | [HuksOptions](#huksoptions) | 是 | 用于获取证书时指定所需参数与数据。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[HuksReturnResult](#huksreturnresult9)\> | Promise对象。当调用成功时，HuksReturnResult的certChains成员非空，为获取到的证书链。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[HUKS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-huks)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | api is not supported. |
| 12000001 | algorithm mode is not supported. |
| 12000004 | operating file failed. |
| 12000005 | IPC communication failed. |
| 12000006 | error occurred in crypto engine. |
| 12000011 | queried entity does not exist. |
| 12000012 | Device environment or input parameter abnormal. |
| 12000014 | memory is insufficient. |
| 12000018 | the group id specified by the access group tag is invalid. |

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';

function stringToUint8Array(str: string): Uint8Array {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  let tmpUint8Array = new Uint8Array(arr);
  return tmpUint8Array;
}

let securityLevel = stringToUint8Array('sec_level');
let challenge = stringToUint8Array('challenge_data');
let versionInfo = stringToUint8Array('version_info');
let keyAliasString = "key anon attest";

async function generateKey(alias: string): Promise<void> {
  let properties: Array<huks.HuksParam> = [
    {
      tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
      value: huks.HuksKeyAlg.HUKS_ALG_RSA
    },
    {
      tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
      value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
    },
    {
      tag: huks.HuksTag.HUKS_TAG_PURPOSE,
      value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
    },
    {
      tag: huks.HuksTag.HUKS_TAG_DIGEST,
      value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
    },
    {
      tag: huks.HuksTag.HUKS_TAG_PADDING,
      value: huks.HuksKeyPadding.HUKS_PADDING_PSS
    },
    {
      tag: huks.HuksTag.HUKS_TAG_KEY_GENERATE_TYPE,
      value: huks.HuksKeyGenerateType.HUKS_KEY_GENERATE_TYPE_DEFAULT
    },
    {
      tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
      value: huks.HuksCipherMode.HUKS_MODE_ECB
    }
  ];
  let options: huks.HuksOptions = {
    properties: properties
  };

  await huks.generateKeyItem(alias, options);
}

async function anonAttestKey(): Promise<void> {
  let aliasString = keyAliasString;
  let aliasUint8 = stringToUint8Array(aliasString);
  let properties: Array<huks.HuksParam> = [
    {
      tag: huks.HuksTag.HUKS_TAG_ATTESTATION_ID_SEC_LEVEL_INFO,
      value: securityLevel
    },
    {
      tag: huks.HuksTag.HUKS_TAG_ATTESTATION_CHALLENGE,
      value: challenge
    },
    {
      tag: huks.HuksTag.HUKS_TAG_ATTESTATION_ID_VERSION_INFO,
      value: versionInfo
    },
    {
      tag: huks.HuksTag.HUKS_TAG_ATTESTATION_ID_ALIAS,
      value: aliasUint8
    }
  ];
  let options: huks.HuksOptions = {
    properties: properties
  };

  await generateKey(aliasString);
  await huks.anonAttestKeyItem(aliasString, options);
}
```

#### huks.importWrappedKeyItem9+

importWrappedKeyItem(keyAlias: string, wrappingKeyAlias: string, options: HuksOptions, callback: AsyncCallback<void>) : void

安全导入密钥。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

API version 9-11系统能力为SystemCapability.Security.Huks.Extension；从API version 12开始为SystemCapability.Security.Huks.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| keyAlias | string | 是 | 密钥别名，存放待导入密钥的别名。 |
| wrappingKeyAlias | string | 是 | 密钥别名，对应密钥用于解密加密的密钥数据。 |
| options | [HuksOptions](#huksoptions) | 是 | 用于导入时所需TAG和需要导入的加密的密钥数据。其中密钥使用的算法、密钥用途、密钥长度为必选参数。 |
| callback | AsyncCallback<void> | 是 | 回调函数。不返回err值时表示接口使用成功时，其他时为错误。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[HUKS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-huks)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | api is not supported. |
| 12000001 | algorithm mode is not supported. |
| 12000002 | algorithm param is missing. |
| 12000003 | algorithm param is invalid. |
| 12000004 | operating file failed. |
| 12000005 | IPC communication failed. |
| 12000006 | error occurred in crypto engine. |
| 12000011 | queried entity does not exist. |
| 12000012 | Device environment or input parameter abnormal. |
| 12000013 | queried credential does not exist. |
| 12000014 | memory is insufficient. |
| 12000015 | Failed to obtain the security information via UserIAM. |
| 12000017 | The key with same alias is already exist. |
| 12000018 | the group id specified by the access group tag is invalid. |

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';

let alias1 = "importAlias";
let alias2 = "wrappingKeyAlias";

async function TestGenFunc(alias: string, options: huks.HuksOptions) {
  await genKey(alias, options)
    .then((data) => {
      console.info(`callback: generateKeyItem success`);
    });
}

function genKey(alias: string, options: huks.HuksOptions) {
  return new Promise<void>((resolve, reject) => {
    huks.generateKeyItem(alias, options, (error, data) => {
      if (error) {
        reject(error);
      } else {
        resolve(data);
      }
    });
  });
}

async function TestExportFunc(alias: string, options: huks.HuksOptions) {
  await exportKey(alias, options)
    .then((data) => {
      console.info(`callback: exportKeyItem success, data = ${JSON.stringify(data)}`);
    });
}

function exportKey(alias: string, options: huks.HuksOptions) {
  return new Promise<huks.HuksReturnResult>((resolve, reject) => {
    huks.exportKeyItem(alias, options, (error, data) => {
      if (error) {
        reject(error);
      } else {
        resolve(data);
      }
    });
  });
}

async function TestImportWrappedFunc(alias: string, wrappingAlias: string, options: huks.HuksOptions) {
  await importWrappedKey(alias, wrappingAlias, options)
    .then((data) => {
      console.info(`callback: importWrappedKeyItem success`);
    });
}

function importWrappedKey(alias: string, wrappingAlias: string, options: huks.HuksOptions) {
  return new Promise<void>((resolve, reject) => {
    huks.importWrappedKeyItem(alias, wrappingAlias, options, (error, data) => {
      if (error) {
        reject(error);
      } else {
        resolve(data);
      }
    });
  });
}

async function TestImportWrappedKeyFunc(
  alias: string,
  wrappingAlias: string,
  genOptions: huks.HuksOptions,
  importOptions: huks.HuksOptions
) {
  await TestGenFunc(wrappingAlias, genOptions);
  await TestExportFunc(wrappingAlias, genOptions);

  /* 以下操作不需要调用HUKS接口，此处不给出具体实现：
   * 假设待导入的密钥为keyA。
   * 1. 生成ECC公私钥keyB，公钥为keyB_pub, 私钥为keyB_pri。
   * 2. 使用keyB_pri和wrappingAlias密钥中获取的公钥进行密钥协商，协商出共享密钥share_key。
   * 3. 随机生成密钥kek，用于加密keyA，采用AES-GCM加密，加密过程中需要记录：nonce1、aad1、加密后的密文keyA_enc、加密后的tag1。
   * 4. 使用share_key加密kek，采用AES-GCM加密，加密过程中需要记录：nonce2、aad2、加密后的密文kek_enc、加密后的tag2。
   * 5. 拼接importOptions.inData字段，满足以下格式：
   *     keyB_pub的长度（4字节） + keyB_pub的数据 + aad2的长度（4字节） + aad2的数据 +
   *     nonce2的长度（4字节）   + nonce2的数据   + tag2的长度（4字节） + tag2的数据 +
   *     kek_enc的长度（4字节）  + kek_enc的数据  + aad1的长度（4字节） + aad1的数据 +
   *     nonce1的长度（4字节）   + nonce1的数据   + tag1的长度（4字节） + tag1的数据 +
   *     keyA长度占用的内存长度（4字节）  + keyA的长度     + keyA_enc的长度（4字节） + keyA_enc的数据
   */
  /* 该处为示例代码，实际运行过程中，应使用实际导入密钥数据。数据构造方式由上注释可见说明 */
  let inputKey = new Uint8Array([0x02, 0x00, 0x00, 0x00]);
  importOptions.inData = inputKey;
  await TestImportWrappedFunc(alias, wrappingAlias, importOptions);
}

function makeGenerateOptions() {
  let properties: Array<huks.HuksParam> = [
    {
      tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
      value: huks.HuksKeyAlg.HUKS_ALG_ECC
    },
    {
      tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
      value: huks.HuksKeySize.HUKS_ECC_KEY_SIZE_256
    },
    {
      tag: huks.HuksTag.HUKS_TAG_PURPOSE,
      value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_UNWRAP
    },
    {
      tag: huks.HuksTag.HUKS_TAG_DIGEST,
      value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
    },
    {
      tag: huks.HuksTag.HUKS_TAG_IMPORT_KEY_TYPE,
      value: huks.HuksImportKeyType.HUKS_KEY_TYPE_KEY_PAIR,
    }
  ];
  let options: huks.HuksOptions = {
    properties: properties
  };
  return options;
};

function makeImportOptions() {
  let properties: Array<huks.HuksParam> = [
    {
      tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
      value: huks.HuksKeyAlg.HUKS_ALG_AES
    },
    {
      tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
      value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
    },
    {
      tag: huks.HuksTag.HUKS_TAG_PURPOSE,
      value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
    },
    {
      tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
      value: huks.HuksCipherMode.HUKS_MODE_CBC
    },
    {
      tag: huks.HuksTag.HUKS_TAG_PADDING,
      value: huks.HuksKeyPadding.HUKS_PADDING_NONE
    },
    {
      tag: huks.HuksTag.HUKS_TAG_UNWRAP_ALGORITHM_SUITE,
      value: huks.HuksUnwrapSuite.HUKS_UNWRAP_SUITE_ECDH_AES_256_GCM_NOPADDING
    }
  ];
  let options: huks.HuksOptions = {
    properties: properties
  };
  return options;
};

function huksImportWrappedKey() {
  let genOptions = makeGenerateOptions();
  let importOptions = makeImportOptions();
  TestImportWrappedKeyFunc(
    alias1,
    alias2,
    genOptions,
    importOptions
  );
}
```

#### huks.importWrappedKeyItem9+

importWrappedKeyItem(keyAlias: string, wrappingKeyAlias: string, options: HuksOptions) : Promise<void>

安全导入密钥。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| keyAlias | string | 是 | 密钥别名，存放待导入密钥的别名。 |
| wrappingKeyAlias | string | 是 | 密钥别名，对应密钥用于解密加密的密钥数据。 |
| options | [HuksOptions](#huksoptions) | 是 | 用于导入时所需TAG和需要导入的加密的密钥数据。其中密钥使用的算法、密钥用途、密钥长度为必选参数。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[HUKS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-huks)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | api is not supported. |
| 12000001 | algorithm mode is not supported. |
| 12000002 | algorithm param is missing. |
| 12000003 | algorithm param is invalid. |
| 12000004 | operating file failed. |
| 12000005 | IPC communication failed. |
| 12000006 | error occurred in crypto engine. |
| 12000011 | queried entity does not exist. |
| 12000012 | Device environment or input parameter abnormal. |
| 12000013 | queried credential does not exist. |
| 12000014 | memory is insufficient. |
| 12000015 | Failed to obtain the security information via UserIAM. |
| 12000017 | The key with same alias is already exist. |
| 12000018 | the group id specified by the access group tag is invalid. |

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';

/* 处理流程与callback类似，主要差异点为如下函数： */
/* 该处为示例代码，实际运行过程中，应使用实际导入密钥数据。数据构造方式由上注释可见说明 */
async function TestImportWrappedFunc(alias: string, wrappingAlias: string, options: huks.HuksOptions) {
  await huks.importWrappedKeyItem(alias, wrappingAlias, options)
    .then((data) => {
      console.info(`promise: importWrappedKeyItem success`);
    });
}
```

#### huks.exportKeyItem9+

exportKeyItem(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksReturnResult>) : void

导出密钥。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

API version 9-11系统能力为SystemCapability.Security.Huks.Extension；从API version 12开始为SystemCapability.Security.Huks.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| keyAlias | string | 是 | 密钥别名，应与所用密钥生成时使用的别名相同。 |
| options | [HuksOptions](#huksoptions) | 是 | 
用于导出密钥时指定密钥的属性，如使用[HuksAuthStorageLevel](#huksauthstoragelevel11)指定需导出密钥的安全级别，

可传空，当API version ≥ 12时，传空默认为CE，当API version ＜ 12时，传空默认为DE。

 |
| callback | AsyncCallback<[HuksReturnResult](#huksreturnresult9)\> | 是 | 回调函数。当导出密钥成功时，err为undefined，data为获取到的HuksReturnResult；否则为错误对象。HuksReturnResult中的outData返回从HUKS中导出的公钥。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[HUKS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-huks)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | api is not supported. |
| 12000001 | algorithm mode is not supported. |
| 12000004 | operating file failed. |
| 12000005 | IPC communication failed. |
| 12000006 | error occurred in crypto engine. |
| 12000011 | queried entity does not exist. |
| 12000012 | Device environment or input parameter abnormal. |
| 12000014 | memory is insufficient. |
| 12000018 | the group id specified by the access group tag is invalid. |

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';

/* 此处options选择emptyOptions来传空 */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};

huks.exportKeyItem(keyAlias, emptyOptions, (error, data) => {
  if (error) {
    console.error(`callback: exportKeyItem failed`);
  } else {
    console.info(`callback: exportKeyItem success, data = ${JSON.stringify(data)}`);
  }
});
```

#### huks.exportKeyItem9+

exportKeyItem(keyAlias: string, options: HuksOptions) : Promise<HuksReturnResult>

导出密钥。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| keyAlias | string | 是 | 密钥别名，应与所用密钥生成时使用的别名相同。 |
| options | [HuksOptions](#huksoptions) | 是 | 空对象（此处传空即可）。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[HuksReturnResult](#huksreturnresult9)\> | Promise对象。当调用成功时，HuksReturnResult的outData成员非空，为从密钥中导出的公钥。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[HUKS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-huks)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | api is not supported. |
| 12000001 | algorithm mode is not supported. |
| 12000004 | operating file failed. |
| 12000005 | IPC communication failed. |
| 12000006 | error occurred in crypto engine. |
| 12000011 | queried entity does not exist. |
| 12000012 | Device environment or input parameter abnormal. |
| 12000014 | memory is insufficient. |
| 12000018 | the group id specified by the access group tag is invalid. |

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';

/* 此处options选择emptyOptions来传空 */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};

huks.exportKeyItem(keyAlias, emptyOptions)
  .then((data) => {
    console.info(`promise: exportKeyItem success, data = ${JSON.stringify(data)}`);
  });
```

#### huks.wrapKeyItem20+

wrapKeyItem(keyAlias: string, params: HuksOptions): Promise<HuksReturnResult>

加密导出密钥。使用Promise异步回调。

**系统能力：** SystemCapability.Security.Huks.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| keyAlias | string | 是 | 密钥别名，应与所用密钥生成时使用的别名相同。 |
| params | [HuksOptions](#huksoptions) | 是 | 用于指定导出密钥时的加密类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[HuksReturnResult](#huksreturnresult9)\> | Promise对象。当调用成功时，HuksReturnResult的outData成员非空，为导出的密钥密文。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[HUKS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-huks)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 801 | api is not supported. |
| 12000004 | operating file failed. |
| 12000005 | IPC communication failed. |
| 12000011 | queried entity does not exist. |
| 12000012 | Device environment or input parameter abnormal. |
| 12000014 | memory is insufficient. |
| 12000018 | the input parameter is invalid. |

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';

let keyAlias = "testWrapKey";
let properties: Array<huks.HuksParam> = [
  {
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_AES
  },
  {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_NONE
  },
  {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_GCM
  },
  /* 生成密钥时指定允许加密导出 */
  {
    tag: huks.HuksTag.HUKS_TAG_IS_ALLOWED_WRAP,
    value: true
  }
];

let options: huks.HuksOptions = {
  properties: properties,
};

let wrapKeyProperties: Array<huks.HuksParam> = [
  {
    tag: huks.HuksTag.HUKS_TAG_KEY_WRAP_TYPE,
    value: huks.HuksKeyWrapType.HUKS_KEY_WRAP_TYPE_HUK_BASED
  }
];

let wrapKeyOptions: huks.HuksOptions = {
  properties: wrapKeyProperties,
};

let wrappedKey: Uint8Array;

async function testGenerateKey() {
  await huks.generateKeyItem(keyAlias, options)
    .then((data) => {
      console.info(`promise: generateKeyItem success`);
    })
    .catch((error: Error) => {
      console.error(`promise: generateKeyItem failed`);
    });
}

async function testWrapKey(){
  await testGenerateKey();

  await huks.wrapKeyItem(keyAlias, wrapKeyOptions)
    .then((data) => {
      wrappedKey = data.outData as Uint8Array;
      console.info(`promise: wrapKeyItem success, data = ${JSON.stringify(data)}`);
    })
    .catch((error: Error) => {
      console.error(`promise: wrapKeyItem failed`);
    });
}
```

#### huks.unwrapKeyItem20+

unwrapKeyItem(keyAlias: string, params: HuksOptions, wrappedKey: Uint8Array): Promise<HuksReturnResult>

加密导入密钥。使用Promise异步回调。

**系统能力：** SystemCapability.Security.Huks.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| keyAlias | string | 是 | 密钥别名，指定导入密钥的密钥别名。 |
| params | [HuksOptions](#huksoptions) | 是 | 用于指定导入密钥时的加密类型。 |
| wrappedKey | Uint8Array | 是 | 加密导出密钥的密文。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[HuksReturnResult](#huksreturnresult9)\> | Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[HUKS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-huks)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 801 | api is not supported. |
| 12000004 | operating file failed. |
| 12000005 | IPC communication failed. |
| 12000012 | Device environment or input parameter abnormal. |
| 12000014 | memory is insufficient. |
| 12000015 | Failed to obtain the security information via UserIAM. |
| 12000018 | the input parameter is invalid. |

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';

let wrapKeyProperties: Array<huks.HuksParam> = [
  {
    tag: huks.HuksTag.HUKS_TAG_KEY_WRAP_TYPE,
    value: huks.HuksKeyWrapType.HUKS_KEY_WRAP_TYPE_HUK_BASED
  }
];
let wrapKeyOptions: huks.HuksOptions = {
  properties: wrapKeyProperties,
};

/* wrappedKey在wrapKeyItem后获取 */
let keyAlias = "testWrapKey";
let wrappedKey: Uint8Array;

async function testUnwrapKey(){
  await huks.unwrapKeyItem(keyAlias, wrapKeyOptions, wrappedKey)
    .then((data) => {
      console.info(`promise: unwrapKeyItem success`);
    })
    .catch((error: Error) => {
      console.error(`promise: unwrapKeyItem failed`);
    });
}
```

#### huks.getKeyItemProperties9+

getKeyItemProperties(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksReturnResult>) : void

获取密钥属性。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

API version 9-11系统能力为SystemCapability.Security.Huks.Extension；从API version 12开始为SystemCapability.Security.Huks.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| keyAlias | string | 是 | 密钥别名，应与所用密钥生成时使用的别名相同。 |
| options | [HuksOptions](#huksoptions) | 是 | 空对象（此处传空即可）。 |
| callback | AsyncCallback<[HuksReturnResult](#huksreturnresult9)\> | 是 | 回调函数。当获取密钥属性成功时，err为undefined，data为获取到的HuksReturnResult；否则为错误对象。HuksReturnResult的properties为生成密钥时所需参数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[HUKS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-huks)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | api is not supported. |
| 12000001 | algorithm mode is not supported. |
| 12000004 | operating file failed. |
| 12000005 | IPC communication failed. |
| 12000006 | error occurred in crypto engine. |
| 12000011 | queried entity does not exist. |
| 12000012 | Device environment or input parameter abnormal. |
| 12000014 | memory is insufficient. |
| 12000018 | the group id specified by the access group tag is invalid. |

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';

/* 此处options选择emptyOptions来传空 */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};

huks.getKeyItemProperties(keyAlias, emptyOptions, (error, data) => {
  if (error) {
    console.error(`callback: getKeyItemProperties failed`);
  } else {
    console.info(`callback: getKeyItemProperties success, data = ${JSON.stringify(data)}`);
  }
});
```

#### huks.getKeyItemProperties9+

getKeyItemProperties(keyAlias: string, options: HuksOptions) : Promise<HuksReturnResult>

获取密钥属性。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| keyAlias | string | 是 | 密钥别名，应与所用密钥生成时使用的别名相同。 |
| options | [HuksOptions](#huksoptions) | 是 | 空对象（此处传空即可）。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[HuksReturnResult](#huksreturnresult9)\> | Promise对象。返回HuksReturnResult。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[HUKS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-huks)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | api is not supported. |
| 12000001 | algorithm mode is not supported. |
| 12000004 | operating file failed. |
| 12000005 | IPC communication failed. |
| 12000006 | error occurred in crypto engine. |
| 12000011 | queried entity does not exist. |
| 12000012 | Device environment or input parameter abnormal. |
| 12000014 | memory is insufficient. |
| 12000018 | the group id specified by the access group tag is invalid. |

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';

/* 此处options选择emptyOptions来传空 */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};

huks.getKeyItemProperties(keyAlias, emptyOptions)
  .then((data) => {
    console.info(`promise: getKeyItemProperties success, data = ${JSON.stringify(data)}`);
  });
```

#### huks.isKeyItemExist9+

isKeyItemExist(keyAlias: string, options: HuksOptions, callback: AsyncCallback<boolean>) : void

判断密钥是否存在。使用callback异步回调。

若密钥不存在，则抛出错误码为12000011的异常。

**系统能力：** SystemCapability.Security.Huks.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| keyAlias | string | 是 | 所需查找的密钥的别名。 |
| options | [HuksOptions](#huksoptions) | 是 | 
用于查询时指定密钥的属性TAG，如使用[HuksAuthStorageLevel](#huksauthstoragelevel11)指定需查询密钥的安全级别，

可传空，当API version ≥ 12时，传空默认为CE，当API version ＜ 12时，传空默认为DE。

 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。密钥存在时，data为true；密钥不存在时，data为undefined，err中的错误码为12000011，并附带对应错误描述。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[HUKS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-huks)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | api is not supported. |
| 12000004 | operating file failed. |
| 12000005 | IPC communication failed. |
| 12000006 | error occurred in crypto engine. |
| 12000011 | queried entity does not exist. |
| 12000012 | Device environment or input parameter abnormal. |
| 12000014 | memory is insufficient. |
| 12000018 | the group id specified by the access group tag is invalid. |

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';

/* 此处options选择emptyOptions来传空 */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};

huks.isKeyItemExist(keyAlias, emptyOptions, (error, data) => {
  if (error) {
    console.error(`callback: isKeyItemExist failed`);
  } else {
    if (data) {
      console.info(`keyAlias:${keyAlias} is existed!`);
    } else {
      console.error(`find key failed`);
    }
  }
});
```

#### huks.isKeyItemExist9+

isKeyItemExist(keyAlias: string, options: HuksOptions) : Promise<boolean>

判断密钥是否存在。使用Promise异步回调。

若密钥不存在，则抛出错误码为12000011的异常。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| keyAlias | string | 是 | 所需查找的密钥的别名。 |
| options | [HuksOptions](#huksoptions) | 是 | 
用于查询时指定密钥的属性TAG，如使用[HuksAuthStorageLevel](#huksauthstoragelevel11)指定需查询密钥的安全级别，

可传空，当API version ≥ 12时，传空默认为CE，当API version ＜ 12时，传空默认为DE。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象。密钥存在时，data为true；密钥不存在时，err中的错误码为12000011，并附带对应错误描述。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[HUKS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-huks)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | api is not supported. |
| 12000004 | operating file failed. |
| 12000005 | IPC communication failed. |
| 12000006 | error occurred in crypto engine. |
| 12000011 | queried entity does not exist. |
| 12000012 | Device environment or input parameter abnormal. |
| 12000014 | memory is insufficient. |
| 12000018 | the group id specified by the access group tag is invalid. |

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';

/* 此处options选择emptyOptions来传空 */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};

huks.isKeyItemExist(keyAlias, emptyOptions).then((data) => {
  console.info(`keyAlias:${keyAlias} is existed!`);
});
```

#### huks.hasKeyItem11+

hasKeyItem(keyAlias: string, options: HuksOptions, callback: AsyncCallback<boolean>) : void

判断密钥是否存在。使用callback异步回调。

若密钥不存在，则通过callback返回false。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| keyAlias | string | 是 | 所需查找的密钥的别名。 |
| options | [HuksOptions](#huksoptions) | 是 | 
用于查询时指定密钥的属性TAG，如使用[HuksAuthStorageLevel](#huksauthstoragelevel11)指定需查询密钥的安全级别，

可传空，当API version ≥ 12时，传空默认为CE，当API version ＜ 12时，传空默认为DE。

 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。若密钥存在，data为true，若密钥不存在，data为false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[HUKS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-huks)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | api is not supported. |
| 12000004 | operating file failed. |
| 12000005 | IPC communication failed. |
| 12000006 | error occurred in crypto engine. |
| 12000012 | Device environment or input parameter abnormal. |
| 12000014 | memory is insufficient. |
| 12000018 | the group id specified by the access group tag is invalid. |

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';

/* 此处options选择emptyOptions来传空 */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};

huks.hasKeyItem(keyAlias, emptyOptions, (error, data) => {
  if (error) {
    console.error(`callback: hasKeyItem failed`);
  } else {
    if (data) {
      console.info(`keyAlias:${keyAlias} is existed!`);
    } else {
      console.error(`find key failed`);
    }
  }
});
```

#### huks.hasKeyItem11+

hasKeyItem(keyAlias: string, options: HuksOptions) : Promise<boolean>

判断密钥是否存在。使用Promise异步回调。

若密钥不存在，则通过Promise返回false。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| keyAlias | string | 是 | 所需查找的密钥的别名。 |
| options | [HuksOptions](#huksoptions) | 是 | 
用于查询时指定密钥的属性TAG，如使用[HuksAuthStorageLevel](#huksauthstoragelevel11)指定需查询密钥的安全级别，

可传空，当API version ≥ 12时，传空默认为CE，当API version ＜ 12时，传空默认为DE。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象。若密钥存在，返回值为true，若密钥不存在，返回值为false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[HUKS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-huks)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | api is not supported. |
| 12000004 | operating file failed. |
| 12000005 | IPC communication failed. |
| 12000006 | error occurred in crypto engine. |
| 12000012 | Device environment or input parameter abnormal. |
| 12000014 | memory is insufficient. |
| 12000018 | the group id specified by the access group tag is invalid. |

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';

/* 此处options选择emptyOptions来传空 */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};

huks.hasKeyItem(keyAlias, emptyOptions).then((data) => {
  if (data) {
    console.info(`keyAlias:${keyAlias} is existed!`);
  } else {
    console.info(`find key failed!`);
  }
});
```

#### huks.initSession9+

initSession(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksSessionHandle>) : void

initSession操作密钥接口。使用callback异步回调。

huks.initSession、huks.updateSession、huks.finishSession为三段式接口，需要一起使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| keyAlias | string | 是 | initSession操作密钥的别名。 |
| options | [HuksOptions](#huksoptions) | 是 | initSession操作的参数集合。 |
| callback | AsyncCallback<[HuksSessionHandle](#hukssessionhandle9)\> | 是 | 回调函数。当密钥操作init成功时，err为undefined，data为获取到的HuksSessionHandle；否则为错误对象。HuksSessionHandle的handle返回initSession生成的handle。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[HUKS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-huks)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | api is not supported. |
| 12000001 | algorithm mode is not supported. |
| 12000002 | algorithm param is missing. |
| 12000003 | algorithm param is invalid. |
| 12000004 | operating file failed. |
| 12000005 | IPC communication failed. |
| 12000006 | error occurred in crypto engine or Ukey driver. |
| 12000010 | the number of sessions has reached limit. |
| 12000011 | queried entity does not exist. |
| 12000012 | Device environment or input parameter abnormal. |
| 12000014 | memory is insufficient. |
| 12000018 | the input parameter is invalid. Possible causes: 1. the aead length is invalid. 2. the group id specified by the access group tag is invalid. |
| 12000020 | the provider operation failed. |
| 12000021 | the Ukey PIN is locked. |
| 12000023 | the Ukey PIN not authenticated. |
| 12000024 | the provider or Ukey is busy. |

#### huks.initSession9+

initSession(keyAlias: string, options: HuksOptions) : Promise<HuksSessionHandle>

initSession操作密钥接口。使用Promise异步回调。

huks.initSession、huks.updateSession、huks.finishSession为三段式接口，需要一起使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| keyAlias | string | 是 | initSession操作密钥的别名。 |
| options | [HuksOptions](#huksoptions) | 是 | initSession参数集合。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<[HuksSessionHandle](#hukssessionhandle9)\> | Promise对象。返回HuksSessionHandle。HuksSessionHandle的handle返回initSession生成的handle。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[HUKS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-huks)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | api is not supported. |
| 12000001 | algorithm mode is not supported. |
| 12000002 | algorithm param is missing. |
| 12000003 | algorithm param is invalid. |
| 12000004 | operating file failed. |
| 12000005 | IPC communication failed. |
| 12000006 | error occurred in crypto engine or Ukey driver. |
| 12000010 | the number of sessions has reached limit. |
| 12000011 | queried entity does not exist. |
| 12000012 | Device environment or input parameter abnormal. |
| 12000014 | memory is insufficient. |
| 12000018 | the input parameter is invalid. Possible causes: 1. the aead length is invalid. 2. the group id specified by the access group tag is invalid. |
| 12000020 | the provider operation failed. |
| 12000021 | the Ukey PIN is locked. |
| 12000023 | the Ukey PIN not authenticated. |
| 12000024 | the provider or Ukey is busy. |

#### huks.updateSession9+

updateSession(handle: number, options: HuksOptions, callback: AsyncCallback<HuksReturnResult>) : void

updateSession操作密钥接口。使用callback异步回调。

huks.initSession、huks.updateSession、huks.finishSession为三段式接口，需要一起使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| handle | number | 是 | updateSession操作的uint64类型的handle值。 |
| options | [HuksOptions](#huksoptions) | 是 | updateSession的参数集合。 |
| callback | AsyncCallback<[HuksReturnResult](#huksreturnresult9)\> | 是 | 回调函数。当密钥操作update成功时，err为undefined，data为获取到的HuksReturnResult；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[HUKS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-huks)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | api is not supported. |
| 12000001 | algorithm mode is not supported. |
| 12000002 | algorithm param is missing. |
| 12000003 | algorithm param is invalid. |
| 12000004 | operating file failed. |
| 12000005 | IPC communication failed. |
| 12000006 | error occurred in crypto engine or Ukey driver. |
| 12000007 | this credential is already invalidated permanently. |
| 12000008 | verify auth token failed. |
| 12000009 | auth token is already timeout. |
| 12000011 | queried entity does not exist. |
| 12000012 | Device environment or input parameter abnormal. |
| 12000014 | memory is insufficient. |
| 12000018 | the group id specified by the access group tag is invalid. |
| 12000020 | the provider operation failed. |
| 12000021 | the Ukey PIN is locked. |
| 12000023 | the Ukey PIN not authenticated. |
| 12000024 | the provider or Ukey is busy. |

#### huks.updateSession9+

updateSession(handle: number, options: HuksOptions, token: Uint8Array, callback: AsyncCallback<HuksReturnResult>) : void

支持用户身份认证访问控制的updateSession操作密钥接口。使用callback异步回调。

huks.initSession、huks.updateSession、huks.finishSession为三段式接口，需要一起使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| handle | number | 是 | updateSession操作的uint64类型的handle值。 |
| options | [HuksOptions](#huksoptions) | 是 | updateSession操作的参数集合。 |
| token | Uint8Array | 是 | 密钥[二次认证密钥访问控制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-identity-authentication-overview#二次认证密钥访问控制)的用户鉴权证明(AuthToken)。 |
| callback | AsyncCallback<[HuksReturnResult](#huksreturnresult9)\> | 是 | 回调函数。当密钥操作update成功时，err为undefined，data为获取到的HuksReturnResult；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[HUKS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-huks)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | api is not supported. |
| 12000001 | algorithm mode is not supported. |
| 12000002 | algorithm param is missing. |
| 12000003 | algorithm param is invalid. |
| 12000004 | operating file failed. |
| 12000005 | IPC communication failed. |
| 12000006 | error occurred in crypto engine. |
| 12000007 | this credential is already invalidated permanently. |
| 12000008 | verify auth token failed. |
| 12000009 | auth token is already timeout. |
| 12000011 | queried entity does not exist. |
| 12000012 | Device environment or input parameter abnormal. |
| 12000014 | memory is insufficient. |
| 12000018 | the group id specified by the access group tag is invalid. |

#### huks.updateSession9+

updateSession(handle: number, options: HuksOptions, token?: Uint8Array) : Promise<HuksReturnResult>

updateSession操作密钥接口。使用Promise异步回调。

huks.initSession、huks.updateSession、huks.finishSession为三段式接口，需要一起使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| handle | number | 是 | updateSession操作的uint64类型的handle值。 |
| options | [HuksOptions](#huksoptions) | 是 | updateSession操作的参数集合。 |
| token | Uint8Array | 否 | 密钥[二次认证密钥访问控制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-identity-authentication-overview#二次认证密钥访问控制)的用户鉴权证明(AuthToken)，不填表示不进行二次认证密钥访问控制。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<[HuksReturnResult](#huksreturnresult9)\> | Promise对象。将updateSession操作的结果添加到回调函数中。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[HUKS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-huks)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | api is not supported. |
| 12000001 | algorithm mode is not supported. |
| 12000002 | algorithm param is missing. |
| 12000003 | algorithm param is invalid. |
| 12000004 | operating file failed. |
| 12000005 | IPC communication failed. |
| 12000006 | error occurred in crypto engine or Ukey driver. |
| 12000007 | this credential is already invalidated permanently. |
| 12000008 | verify auth token failed. |
| 12000009 | auth token is already timeout. |
| 12000011 | queried entity does not exist. |
| 12000012 | Device environment or input parameter abnormal. |
| 12000014 | memory is insufficient. |
| 12000018 | the group id specified by the access group tag is invalid. |
| 12000020 | the provider operation failed. |
| 12000021 | the Ukey PIN is locked. |
| 12000023 | the Ukey PIN not authenticated. |
| 12000024 | the provider or Ukey is busy. |

#### huks.finishSession9+

finishSession(handle: number, options: HuksOptions, callback: AsyncCallback<HuksReturnResult>) : void

finishSession操作密钥接口。使用callback异步回调。

huks.initSession、huks.updateSession、huks.finishSession为三段式接口，需要一起使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| handle | number | 是 | finishSession操作的uint64类型的handle值。 |
| options | [HuksOptions](#huksoptions) | 是 | finishSession的参数集合。 |
| callback | AsyncCallback<[HuksReturnResult](#huksreturnresult9)\> | 是 | 回调函数。当密钥操作finish成功时，err为undefined，data为获取到的HuksReturnResult；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[HUKS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-huks)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | api is not supported. |
| 12000001 | algorithm mode is not supported. |
| 12000002 | algorithm param is missing. |
| 12000003 | algorithm param is invalid. |
| 12000004 | operating file failed. |
| 12000005 | IPC communication failed. |
| 12000006 | error occurred in crypto engine. |
| 12000007 | this credential is already invalidated permanently. |
| 12000008 | verify auth token failed. |
| 12000009 | auth token is already timeout. |
| 12000011 | queried entity does not exist. |
| 12000012 | Device environment or input parameter abnormal. |
| 12000014 | memory is insufficient. |
| 12000017 | The key with same alias is already exist. |
| 12000018 | the group id specified by the access group tag is invalid. |
| 12000020 | the provider operation failed. |
| 12000021 | the Ukey PIN is locked. |
| 12000023 | the Ukey PIN not authenticated. |
| 12000024 | the provider or Ukey is busy. |

#### huks.finishSession9+

finishSession(handle: number, options: HuksOptions, token: Uint8Array, callback: AsyncCallback<HuksReturnResult>) : void

支持用户身份认证访问控制的finishSession操作密钥接口。使用callback异步回调。

huks.initSession、huks.updateSession、huks.finishSession为三段式接口，需要一起使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| handle | number | 是 | finishSession操作的uint64类型的handle值。 |
| options | [HuksOptions](#huksoptions) | 是 | finishSession的参数集合。 |
| token | Uint8Array | 是 | 密钥[二次认证密钥访问控制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-identity-authentication-overview#二次认证密钥访问控制)的用户鉴权证明(AuthToken)。 |
| callback | AsyncCallback<[HuksReturnResult](#huksreturnresult9)\> | 是 | 回调函数。当密钥操作finish成功时，err为undefined，data为获取到的HuksReturnResult；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[HUKS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-huks)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | api is not supported. |
| 12000001 | algorithm mode is not supported. |
| 12000002 | algorithm param is missing. |
| 12000003 | algorithm param is invalid. |
| 12000004 | operating file failed. |
| 12000005 | IPC communication failed. |
| 12000006 | error occurred in crypto engine. |
| 12000007 | this credential is already invalidated permanently. |
| 12000008 | verify auth token failed. |
| 12000009 | auth token is already timeout. |
| 12000011 | queried entity does not exist. |
| 12000012 | Device environment or input parameter abnormal. |
| 12000014 | memory is insufficient. |
| 12000017 | The key with same alias is already exist. |
| 12000018 | the group id specified by the access group tag is invalid. |

#### huks.finishSession9+

finishSession(handle: number, options: HuksOptions, token?: Uint8Array) : Promise<HuksReturnResult>

finishSession操作密钥接口。使用Promise异步回调。

huks.initSession、huks.updateSession、huks.finishSession为三段式接口，需要一起使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| handle | number | 是 | finishSession操作的uint64类型的handle值。 |
| options | [HuksOptions](#huksoptions) | 是 | finishSession操作的参数集合。 |
| token | Uint8Array | 否 | 密钥[二次认证密钥访问控制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-identity-authentication-overview#二次认证密钥访问控制)的用户鉴权证明(AuthToken)，不填表示不进行二次认证密钥访问控制。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<[HuksReturnResult](#huksreturnresult9)\> | Promise对象。返回HuksReturnResult。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[HUKS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-huks)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | api is not supported. |
| 12000001 | algorithm mode is not supported. |
| 12000002 | algorithm param is missing. |
| 12000003 | algorithm param is invalid. |
| 12000004 | operating file failed. |
| 12000005 | IPC communication failed. |
| 12000006 | error occurred in crypto engine. |
| 12000007 | this credential is already invalidated permanently. |
| 12000008 | verify auth token failed. |
| 12000009 | auth token is already timeout. |
| 12000011 | queried entity does not exist. |
| 12000012 | Device environment or input parameter abnormal. |
| 12000014 | memory is insufficient. |
| 12000017 | The key with same alias is already exist. |
| 12000018 | the group id specified by the access group tag is invalid. |
| 12000020 | the provider operation failed. |
| 12000021 | the Ukey PIN is locked. |
| 12000023 | the Ukey PIN not authenticated. |
| 12000024 | the provider or Ukey is busy. |

#### huks.abortSession9+

abortSession(handle: number, options: HuksOptions, callback: AsyncCallback<void>) : void

abortSession终止密钥操作。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| handle | number | 是 | abortSession操作的uint64类型的handle值。 |
| options | [HuksOptions](#huksoptions) | 是 | abortSession操作的参数集合。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当密钥操作abort成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[HUKS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-huks)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | api is not supported. |
| 12000004 | operating file failed. |
| 12000005 | IPC communication failed. |
| 12000006 | error occurred in crypto engine or Ukey driver. |
| 12000012 | Device environment or input parameter abnormal. |
| 12000018 | the group id specified by the access group tag is invalid. |
| 12000014 | memory is insufficient. |
| 12000020 | the provider operation failed. |
| 12000024 | the provider or Ukey is busy. |

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';

/* huks.initSession、huks.updateSession、huks.finishSession为三段式接口，需要一起使用，
 * 当这三个操作中的任一阶段发生错误时，都需要调用huks.abortSession来终止密钥的使用
 *
 * 以下以RSA2048密钥的callback功能使用为例
 */

let keyAlias = "HuksDemoRSA";
let properties: Array<huks.HuksParam> = []
let options: huks.HuksOptions = {
  properties: properties,
  inData: new Uint8Array(0)
};
let handle: number = 0;

async function huksAbort() {
  properties = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_RSA
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT
  }, {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_PKCS1_V1_5
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
  }, {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_ECB,
  }];

  huks.generateKeyItem(keyAlias, options, (error, data) => {
    if (error) {
      console.error(`callback: generateKeyItem failed`);
    } else {
      console.info(`callback: generateKeyItem success`);
      huks.initSession(keyAlias, options, (error, data) => { // 以initSession阶段进行abortSession为例
        if (error) {
          console.error(`callback: initSession failed`);
        } else {
          console.info(`callback: initSession success, data = ${JSON.stringify(data)}`);
          handle = data.handle;
          huks.abortSession(handle, options, (error, data) => {
            if (error) {
              console.error(`callback: abortSession failed`);
            } else {
              console.info(`callback: abortSession success`);
            }
          });
        }
      });
    }
  });
}
```

#### huks.abortSession9+

abortSession(handle: number, options: HuksOptions) : Promise<void>

abortSession终止密钥操作。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| handle | number | 是 | abortSession操作的uint64类型的handle值。 |
| options | [HuksOptions](#huksoptions) | 是 | abortSession操作的参数集合。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[HUKS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-huks)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | api is not supported. |
| 12000004 | operating file failed. |
| 12000005 | IPC communication failed. |
| 12000006 | error occurred in crypto engine or Ukey driver. |
| 12000012 | Device environment or input parameter abnormal. |
| 12000018 | the group id specified by the access group tag is invalid. |
| 12000014 | memory is insufficient. |
| 12000020 | the provider operation failed. |
| 12000024 | the provider or Ukey is busy. |

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';

/* huks.initSession、huks.updateSession、huks.finishSession为三段式接口，需要一起使用，
 * 当这三个操作中的任一阶段发生错误时，都需要调用huks.abortSession来终止密钥的使用
 *
 * 以下以RSA2048密钥的promise功能使用为例
 */

function stringToUint8Array(str: string) {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  let tmpUint8Array = new Uint8Array(arr);
  return tmpUint8Array;
}

let keyAlias = "HuksDemoRSA";
let properties: Array<huks.HuksParam> = [];
let options: huks.HuksOptions = {
  properties: properties,
  inData: new Uint8Array(0)
};
let handle: number = 0;

async function generateKey() {
  properties = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_RSA
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT
  }, {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_PKCS1_V1_5
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
  }, {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_ECB,
  }];

  await huks.generateKeyItem(keyAlias, options)
    .then((data) => {
      console.info(`promise: generateKeyItem success`);
    });
}

async function huksInit() {
  console.info('enter huksInit');
  await huks.initSession(keyAlias, options)
    .then((data) => {
      console.info(`promise: initSession success, data = ${JSON.stringify(data)}`);
      handle = data.handle;
    });
}

async function huksUpdate() {
  console.info('enter huksUpdate');
  options.inData = stringToUint8Array("huksHmacTest");
  await huks.updateSession(handle, options)
    .then((data) => {
      console.info(`promise: updateSession success, data = ${JSON.stringify(data)}`);
    });
}

async function huksFinish() {
  console.info('enter huksFinish');
  options.inData = new Uint8Array(0);
  await huks.finishSession(handle, options)
    .then((data) => {
      console.info(`promise: finishSession success, data = ${JSON.stringify(data)}`);
    });
}

async function huksAbort() {
  console.info('enter huksAbort');
  await huks.abortSession(handle, options)
    .then((data) => {
      console.info(`promise: abortSession success`);
    });
}

async function testAbort() {
  await generateKey();
  await huksInit(); // 以initSession阶段进行abortSession为例
  await huksAbort();
}
```

#### huks.listAliases12+

listAliases(options: HuksOptions): Promise<HuksListAliasesReturnResult>

查询密钥别名集接口。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [HuksOptions](#huksoptions) | 是 | listAliases操作的参数集合。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<[HuksListAliasesReturnResult](#hukslistaliasesreturnresult12)\> | Promise对象。将listAliases操作的结果添加到回调函数中。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[HUKS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-huks)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 12000004 | operating file failed. |
| 12000005 | IPC communication failed. |
| 12000012 | Device environment or input parameter abnormal. |
| 12000014 | memory is insufficient. |
| 12000018 | the group id specified by the access group tag is invalid. |

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit'

async function testListAliases() {
  let queryProperties: Array<huks.HuksParam> = [
    {
      tag: huks.HuksTag.HUKS_TAG_AUTH_STORAGE_LEVEL,
      value: huks.HuksAuthStorageLevel.HUKS_AUTH_STORAGE_LEVEL_DE
    }
  ];
  let queryOptions: huks.HuksOptions = {
    properties: queryProperties
  };

  let result: huks.HuksListAliasesReturnResult = await huks.listAliases(queryOptions);
  console.info(`promise: listAliases success`);
}
```

#### HuksExceptionErrCode9+

表示错误码的枚举以及对应的错误信息，错误码表示错误类型，错误信息展示错误详情。

关于错误码的具体信息，可在[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[HUKS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-huks)中查看。

**系统能力：** SystemCapability.Security.Huks.Core

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| HUKS\_ERR\_CODE\_PERMISSION\_FAIL | 201 | 
权限错误导致失败。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_ERR\_CODE\_NOT\_SYSTEM\_APP12+ | 202 | 

非系统应用不可以调用系统API。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_ERR\_CODE\_ILLEGAL\_ARGUMENT | 401 | 

参数错误导致失败。可能原因：1. 必选参数未指定。2. 参数类型不正确。3. 参数校验失败。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_ERR\_CODE\_NOT\_SUPPORTED\_API | 801 | 

不支持的API。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_ERR\_CODE\_FEATURE\_NOT\_SUPPORTED | 12000001 | 

不支持的功能/特性。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_ERR\_CODE\_MISSING\_CRYPTO\_ALG\_ARGUMENT | 12000002 | 

缺少密钥算法参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_ERR\_CODE\_INVALID\_CRYPTO\_ALG\_ARGUMENT | 12000003 | 

无效密钥算法参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_ERR\_CODE\_FILE\_OPERATION\_FAIL | 12000004 | 

文件操作失败。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_ERR\_CODE\_COMMUNICATION\_FAIL | 12000005 | 

通信失败。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_ERR\_CODE\_CRYPTO\_FAIL | 12000006 | 

算法库操作失败。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_ERR\_CODE\_KEY\_AUTH\_PERMANENTLY\_INVALIDATED | 12000007 | 

密钥访问失败-密钥访问失效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_ERR\_CODE\_KEY\_AUTH\_VERIFY\_FAILED | 12000008 | 

密钥访问失败-密钥认证失败。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_ERR\_CODE\_KEY\_AUTH\_TIME\_OUT | 12000009 | 

密钥访问失败-密钥访问超时。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_ERR\_CODE\_SESSION\_LIMIT | 12000010 | 

密钥操作会话数已达上限。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_ERR\_CODE\_ITEM\_NOT\_EXIST | 12000011 | 

目标对象不存在。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_ERR\_CODE\_EXTERNAL\_ERROR | 12000012 | 

外部错误。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_ERR\_CODE\_CREDENTIAL\_NOT\_EXIST | 12000013 | 

缺失所需凭据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_ERR\_CODE\_INSUFFICIENT\_MEMORY | 12000014 | 

内存不足。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_ERR\_CODE\_CALL\_SERVICE\_FAILED | 12000015 | 

调用其他系统服务失败。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_ERR\_CODE\_DEVICE\_PASSWORD\_UNSET11+ | 12000016 | 

需要锁屏密码但未设置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

 |
| HUKS\_ERR\_CODE\_KEY\_ALREADY\_EXIST20+ | 12000017 | 

同名密钥已存在。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_ERR\_CODE\_INVALID\_ARGUMENT20+ | 12000018 | 

输入参数非法。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_ERR\_CODE\_ITEM\_EXISTS22+ | 12000019 | 

同名provider已注册。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_ERR\_CODE\_EXTERNAL\_MODULE22+ | 12000020 | 

依赖的外部模块返回错误。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_ERR\_CODE\_PIN\_LOCKED22+ | 12000021 | 

Ukey PIN码被锁。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

 |
| HUKS\_ERR\_CODE\_PIN\_INCORRECT22+ | 12000022 | 

Ukey PIN码错误。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

 |
| HUKS\_ERR\_CODE\_PIN\_NO\_AUTH22+ | 12000023 | 

Ukey PIN码未认证。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

 |
| HUKS\_ERR\_CODE\_BUSY22+ | 12000024 | 

设备或资源繁忙。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_ERR\_CODE\_EXCEED\_LIMIT22+ | 12000025 | 

资源超过限制。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |

#### HuksKeyPurpose

表示密钥用途。

一个密钥仅能用于单类用途，不能既用于加解密又用于签名验签。

**系统能力：** SystemCapability.Security.Huks.Core

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| HUKS\_KEY\_PURPOSE\_ENCRYPT | 1 | 
表示密钥用于对明文进行加密操作。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_KEY\_PURPOSE\_DECRYPT | 2 | 

表示密钥用于对密文进行解密操作。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_KEY\_PURPOSE\_SIGN | 4 | 

表示密钥用于对数据进行签名。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_KEY\_PURPOSE\_VERIFY | 8 | 

表示密钥用于验证签名后的数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_KEY\_PURPOSE\_DERIVE | 16 | 

表示密钥用于派生密钥。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_KEY\_PURPOSE\_WRAP | 32 | 

表示密钥用于加密导出。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_KEY\_PURPOSE\_UNWRAP | 64 | 

表示密钥用于安全导入。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_KEY\_PURPOSE\_MAC | 128 | 

表示密钥用于生成消息验证码。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_KEY\_PURPOSE\_AGREE | 256 | 

表示密钥用于进行密钥协商。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |

#### HuksKeyDigest

表示摘要算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

API version 8-11系统能力为SystemCapability.Security.Huks.Extension；从API version 12开始为SystemCapability.Security.Huks.Core

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| HUKS\_DIGEST\_NONE | 0 | 
表示无摘要算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_DIGEST\_MD5 | 1 | 

表示MD5摘要算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_DIGEST\_SM39+ | 2 | 

表示SM3摘要算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension9-11

 |
| HUKS\_DIGEST\_SHA1 | 10 | 

表示SHA1摘要算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_DIGEST\_SHA224 | 11 | 

表示SHA224摘要算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_DIGEST\_SHA256 | 12 | 

表示SHA256摘要算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_DIGEST\_SHA384 | 13 | 

表示SHA384摘要算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_DIGEST\_SHA512 | 14 | 

表示SHA512摘要算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |

#### HuksKeyPadding

表示补齐算法。

**系统能力：** SystemCapability.Security.Huks.Core

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| HUKS\_PADDING\_NONE | 0 | 
表示不使用补齐算法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_PADDING\_OAEP | 1 | 

表示使用OAEP补齐算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_PADDING\_PSS | 2 | 

表示使用PSS补齐算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_PADDING\_PKCS1\_V1\_5 | 3 | 

表示使用PKCS1\_V1\_5补齐算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_PADDING\_PKCS5 | 4 | 

表示使用PKCS5补齐算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_PADDING\_PKCS7 | 5 | 

表示使用PKCS7补齐算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_PADDING\_ISO\_IEC\_9796\_212+ | 6 | 

表示使用ISO\_IEC\_9796\_2填充算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_PADDING\_ISO\_IEC\_9797\_112+ | 7 | 

表示使用ISO\_IEC\_9797\_1填充算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |

#### HuksCipherMode

表示加密模式。

**系统能力：** SystemCapability.Security.Huks.Core

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| HUKS\_MODE\_ECB | 1 | 
表示使用ECB加密模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_MODE\_CBC | 2 | 

表示使用CBC加密模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_MODE\_CTR | 3 | 

表示使用CTR加密模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_MODE\_OFB | 4 | 

表示使用OFB加密模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_MODE\_CFB12+ | 5 | 

表示使用CFB加密模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_MODE\_CCM | 31 | 

表示使用CCM加密模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_MODE\_GCM | 32 | 

表示使用GCM加密模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |

#### HuksKeySize

表示密钥长度。

**系统能力：** SystemCapability.Security.Huks.Core

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| HUKS\_RSA\_KEY\_SIZE\_512 | 512 | 
表示使用RSA算法的密钥长度为512bit。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_RSA\_KEY\_SIZE\_768 | 768 | 

表示使用RSA算法的密钥长度为768bit。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_RSA\_KEY\_SIZE\_1024 | 1024 | 

表示使用RSA算法的密钥长度为1024bit。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_RSA\_KEY\_SIZE\_2048 | 2048 | 

表示使用RSA算法的密钥长度为2048bit。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_RSA\_KEY\_SIZE\_3072 | 3072 | 

表示使用RSA算法的密钥长度为3072bit。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_RSA\_KEY\_SIZE\_4096 | 4096 | 

表示使用RSA算法的密钥长度为4096bit。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_ECC\_KEY\_SIZE\_224 | 224 | 

表示使用ECC算法的密钥长度为224bit。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_ECC\_KEY\_SIZE\_256 | 256 | 

表示使用ECC算法的密钥长度为256bit。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_ECC\_KEY\_SIZE\_384 | 384 | 

表示使用ECC算法的密钥长度为384bit。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_ECC\_KEY\_SIZE\_521 | 521 | 

表示使用ECC算法的密钥长度为521bit。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_AES\_KEY\_SIZE\_128 | 128 | 

表示使用AES算法的密钥长度为128bit。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_AES\_KEY\_SIZE\_192 | 192 | 

表示使用AES算法的密钥长度为192bit。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_AES\_KEY\_SIZE\_256 | 256 | 

表示使用AES算法的密钥长度为256bit。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_AES\_KEY\_SIZE\_512(deprecated) | 512 | 

表示使用AES算法的密钥长度为512bit。

**说明：** 从API version 8开始支持，从API version 11开始废弃。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_CURVE25519\_KEY\_SIZE\_256 | 256 | 

表示使用CURVE25519算法的密钥长度为256bit。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_DH\_KEY\_SIZE\_2048 | 2048 | 

表示使用DH算法的密钥长度为2048bit。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_DH\_KEY\_SIZE\_3072 | 3072 | 

表示使用DH算法的密钥长度为3072bit。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_DH\_KEY\_SIZE\_4096 | 4096 | 

表示使用DH算法的密钥长度为4096bit。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_SM2\_KEY\_SIZE\_2569+ | 256 | 

表示SM2算法的密钥长度为256bit。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension9-11

 |
| HUKS\_SM4\_KEY\_SIZE\_1289+ | 128 | 

表示SM4算法的密钥长度为128bit。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension9-11

 |
| HUKS\_DES\_KEY\_SIZE\_6412+ | 64 | 

表示DES算法的密钥长度为64bit。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_3DES\_KEY\_SIZE\_12812+ | 128 | 

表示3DES算法的密钥长度为128bit。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_3DES\_KEY\_SIZE\_19212+ | 192 | 

表示3DES算法的密钥长度为192bit。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |

#### HuksKeyAlg

表示密钥使用的算法。

**系统能力：** SystemCapability.Security.Huks.Core

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| HUKS\_ALG\_RSA | 1 | 
表示使用RSA算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_ALG\_ECC | 2 | 

表示使用ECC算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_ALG\_DSA | 3 | 

表示使用DSA算法手机、平板、PC/2in1设备、TV、智能穿戴。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_ALG\_AES | 20 | 

表示使用AES算法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_ALG\_HMAC | 50 | 

表示使用HMAC算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_ALG\_HKDF | 51 | 

表示使用HKDF算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_ALG\_PBKDF2 | 52 | 

表示使用PBKDF2算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_ALG\_ECDH | 100 | 

表示使用ECDH算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_ALG\_X25519 | 101 | 

表示使用X25519算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_ALG\_ED25519 | 102 | 

表示使用ED25519算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_ALG\_DH | 103 | 

表示使用DH算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_ALG\_SM29+ | 150 | 

表示使用SM2算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension9-11

 |
| HUKS\_ALG\_SM39+ | 151 | 

表示使用SM3算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension9-11

 |
| HUKS\_ALG\_SM49+ | 152 | 

表示使用SM4算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension9-11

 |
| HUKS\_ALG\_DES12+ | 160 | 

表示使用DES算法（API 12开始支持轻量级智能穿戴，API 18开始支持手机、平板、PC/2in1设备、TV、智能穿戴）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_ALG\_3DES12+ | 161 | 

表示使用3DES算法（API 12开始支持轻量级智能穿戴，API 18开始支持手机、平板、PC/2in1设备、TV、智能穿戴）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_ALG\_CMAC12+ | 162 | 

表示使用CMAC算法（API 12开始支持轻量级智能穿戴，API 18开始支持手机、平板、PC/2in1设备、TV、智能穿戴）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |

#### HuksKeyGenerateType

表示生成密钥的类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

API version 8-11系统能力为SystemCapability.Security.Huks.Extension；从API version 12开始为SystemCapability.Security.Huks.Core

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| HUKS\_KEY\_GENERATE\_TYPE\_DEFAULT | 0 | 默认生成的密钥。 |
| HUKS\_KEY\_GENERATE\_TYPE\_DERIVE | 1 | 派生生成的密钥。 |
| HUKS\_KEY\_GENERATE\_TYPE\_AGREE | 2 | 协商生成的密钥。 |

#### HuksKeyFlag

表示密钥的产生方式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| HUKS\_KEY\_FLAG\_IMPORT\_KEY | 1 | 表示通过导入公钥接口导入的密钥。 |
| HUKS\_KEY\_FLAG\_GENERATE\_KEY | 2 | 表示通过生成密钥接口生成的密钥。 |
| HUKS\_KEY\_FLAG\_AGREE\_KEY | 3 | 表示通过生成密钥协商接口生成的密钥。 |
| HUKS\_KEY\_FLAG\_DERIVE\_KEY | 4 | 表示通过生成密钥派生接口生成的密钥。 |

#### HuksKeyStorageType

表示密钥存储方式。

**系统能力：** SystemCapability.Security.Huks.Core

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| HUKS\_STORAGE\_TEMP(deprecated) | 0 | 
表示通过本地直接管理密钥。

**说明：** 从API version 8开始支持，从API version 10开始废弃，由于开发者正常使用密钥管理过程中并不需要使用此TAG，故无替代接口。针对密钥派生场景，可使用HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS 与 HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_STORAGE\_PERSISTENT(deprecated) | 1 | 

表示通过HUKS service管理密钥。

**说明：** 从API version 8开始支持，从API version 10开始废弃，由于开发者正常使用密钥管理过程中并不需要使用此TAG，故无替代接口。针对密钥派生场景，可使用HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS 与 HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS10+ | 2 | 

表示主密钥派生的密钥存储于huks中，由HUKS进行托管。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension10-11

 |
| HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED10+ | 3 | 

表示主密钥派生的密钥直接导出给业务方，HUKS不对其进行托管服务。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension10-11

 |

#### HuksSendType

表示发送TAG的方式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

API version 8-11系统能力为SystemCapability.Security.Huks.Extension；从API version 12开始为SystemCapability.Security.Huks.Core

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| HUKS\_SEND\_TYPE\_ASYNC | 0 | 表示异步发送TAG。 |
| HUKS\_SEND\_TYPE\_SYNC | 1 | 表示同步发送TAG。 |

#### HuksKeyClassType22+

表示密钥的来源。

**系统能力：** SystemCapability.Security.Huks.Extension

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| HUKS\_KEY\_CLASS\_DEFAULT | 0 | 表示HUKS本地管理的密钥。 |
| HUKS\_KEY\_CLASS\_EXTENSION | 1 | 表示外部密钥管理扩展管理的密钥。 |

#### HuksUnwrapSuite9+

表示安全导入密钥的算法套件。

**系统能力：** SystemCapability.Security.Huks.Core

API version 9-11系统能力为SystemCapability.Security.Huks.Extension；从API version 12开始为SystemCapability.Security.Huks.Core

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| HUKS\_UNWRAP\_SUITE\_X25519\_AES\_256\_GCM\_NOPADDING | 1 | 
安全导入密钥时，X25519密钥协商后使用AES-256 GCM解密。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| HUKS\_UNWRAP\_SUITE\_ECDH\_AES\_256\_GCM\_NOPADDING | 2 | 

安全导入密钥时，ECDH密钥协商后使用AES-256 GCM解密。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| HUKS\_UNWRAP\_SUITE\_SM2\_SM4\_ECB\_NOPADDING23+ | 5 | 

安全导入密钥时，使用临时SM4密钥加密导入密钥，使用已导入HUKS的SM2密钥加密SM4密钥。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

 |

#### HuksImportKeyType9+

表示导入密钥的密钥类型，默认为导入公钥，导入对称密钥时不需要该字段。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

API version 9-11系统能力为SystemCapability.Security.Huks.Extension；从API version 12开始为SystemCapability.Security.Huks.Core

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| HUKS\_KEY\_TYPE\_PUBLIC\_KEY | 0 | 表示导入的密钥类型为公钥。 |
| HUKS\_KEY\_TYPE\_PRIVATE\_KEY | 1 | 表示导入的密钥类型为私钥。 |
| HUKS\_KEY\_TYPE\_KEY\_PAIR | 2 | 表示导入的密钥类型为公私钥对。 |

#### HuksRsaPssSaltLenType10+

表示Rsa在签名验签、padding为pss时需指定的salt\_len类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

API version 10-11系统能力为SystemCapability.Security.Huks.Extension；从API version 12开始为SystemCapability.Security.Huks.Core

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| HUKS\_RSA\_PSS\_SALT\_LEN\_DIGEST | 0 | 表示以摘要长度设置salt\_len。 |
| HUKS\_RSA\_PSS\_SALT\_LEN\_MAX | 1 | 表示以最大长度设置salt\_len。 |

#### HuksUserAuthType9+

表示用户认证类型。

**系统能力：** SystemCapability.Security.Huks.Extension

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| HUKS\_USER\_AUTH\_TYPE\_FINGERPRINT | 1 << 0 | 
表示用户认证类型为指纹。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| HUKS\_USER\_AUTH\_TYPE\_FACE | 1 << 1 | 

表示用户认证类型为人脸。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| HUKS\_USER\_AUTH\_TYPE\_PIN | 1 << 2 | 

表示用户认证类型为PIN码。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| HUKS\_USER\_AUTH\_TYPE\_TUI\_PIN20+ | 1 << 5 | 表示用户认证类型为TUI PIN码。 |

#### HuksUserAuthMode12+

表示用户认证模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| HUKS\_USER\_AUTH\_MODE\_LOCAL | 0 | 本地认证模式。 |
| HUKS\_USER\_AUTH\_MODE\_COAUTH | 1 | 跨端协同认证模式。 |

#### HuksAuthAccessType9+

表示安全访问控制类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| HUKS\_AUTH\_ACCESS\_INVALID\_CLEAR\_PASSWORD | 1 << 0 | 表示安全访问控制类型为清除密码后密钥无效。 |
| HUKS\_AUTH\_ACCESS\_INVALID\_NEW\_BIO\_ENROLL | 1 << 1 | 表示安全访问控制类型为新录入生物特征后密钥无效。 |
| HUKS\_AUTH\_ACCESS\_ALWAYS\_VALID11+ | 1 << 2 | 表示安全访问控制类型为该密钥总是有效。 |

#### HuksChallengeType9+

表示密钥使用时生成challenge的类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| HUKS\_CHALLENGE\_TYPE\_NORMAL | 0 | 表示challenge为普通类型，默认32字节。 |
| HUKS\_CHALLENGE\_TYPE\_CUSTOM | 1 | 表示challenge为用户自定义类型。支持使用多个密钥仅一次认证。 |
| HUKS\_CHALLENGE\_TYPE\_NONE | 2 | 表示免challenge类型。 |

#### HuksChallengePosition9+

表示challenge类型为用户自定义类型时，生成的challenge有效长度仅为8字节连续的数据，且仅支持4种位置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| HUKS\_CHALLENGE\_POS\_0 | 0 | 表示0~7字节为当前密钥的有效challenge。 |
| HUKS\_CHALLENGE\_POS\_1 | 1 | 表示8~15字节为当前密钥的有效challenge。 |
| HUKS\_CHALLENGE\_POS\_2 | 2 | 表示16~23字节为当前密钥的有效challenge。 |
| HUKS\_CHALLENGE\_POS\_3 | 3 | 表示24~31字节为当前密钥的有效challenge。 |

#### HuksSecureSignType9+

表示生成或导入密钥时，指定该密钥的签名类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| HUKS\_SECURE\_SIGN\_WITH\_AUTHINFO | 1 | 
表示签名类型为携带认证信息。生成或导入密钥时指定该字段，则在使用密钥进行签名时，对待签名的数据添加认证信息后进行签名。

**注意：**

携带的认证信息包含身份信息，开发者需在其隐私声明中对此身份信息的使用目的、存留策略和销毁方式进行说明。

 |

#### HuksAuthStorageLevel11+

表示生成或导入密钥时，指定该密钥的存储安全等级。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

API version 11系统能力为SystemCapability.Security.Huks.Extension；从API version 12开始为SystemCapability.Security.Huks.Core

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| HUKS\_AUTH\_STORAGE\_LEVEL\_DE | 0 | 表示密钥仅在开机后可访问。 |
| HUKS\_AUTH\_STORAGE\_LEVEL\_CE | 1 | 表示密钥仅在首次解锁后可访问。 |
| HUKS\_AUTH\_STORAGE\_LEVEL\_ECE | 2 | 表示密钥仅在解锁状态时可访问。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/cbg4zILVQp2m5GSSI5Cqgw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014821Z&HW-CC-Expire=86400&HW-CC-Sign=1FD89F395E1781A9C2B83F685ADDDD7419E2C9626A990964DCF8938D5C2CE97C)

业务在使用存储等级为ECE的密钥时，建议通过感知[锁屏事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/commoneventmanager-definitions#common_event_screen_locked)来清理使用该密钥创建的会话资源，以保证安全性。

#### HuksKeyWrapType20+

表示密钥加密类型（加密导出或导入密钥）的枚举。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| HUKS\_KEY\_WRAP\_TYPE\_HUK\_BASED | 2 | 硬件唯一密钥加密类型。 |

#### HuksTagType

表示Tag的数据类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| HUKS\_TAG\_TYPE\_INVALID | 0 << 28 | 表示非法的Tag类型。 |
| HUKS\_TAG\_TYPE\_INT | 1 << 28 | 表示该Tag的数据类型为int类型的number。 |
| HUKS\_TAG\_TYPE\_UINT | 2 << 28 | 表示该Tag的数据类型为uint类型的number。 |
| HUKS\_TAG\_TYPE\_ULONG | 3 << 28 | 表示该Tag的数据类型为bigint。 |
| HUKS\_TAG\_TYPE\_BOOL | 4 << 28 | 表示该Tag的数据类型为boolean。 |
| HUKS\_TAG\_TYPE\_BYTES | 5 << 28 | 表示该Tag的数据类型为Uint8Array。 |

#### HuksTag

表示调用参数的Tag。

**系统能力：** SystemCapability.Security.Huks.Core

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| HUKS\_TAG\_INVALID(deprecated) | HuksTagType.HUKS\_TAG\_TYPE\_INVALID | 0 | 
表示非法的Tag。

**说明：** 从API version 8开始使用，从API version 9开始废弃。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_TAG\_ALGORITHM | HuksTagType.HUKS\_TAG\_TYPE\_UINT | 1 | 

表示算法的Tag。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_TAG\_PURPOSE | HuksTagType.HUKS\_TAG\_TYPE\_UINT | 2 | 

表示密钥用途的Tag。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_TAG\_KEY\_SIZE | HuksTagType.HUKS\_TAG\_TYPE\_UINT | 3 | 

表示密钥长度的Tag。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_TAG\_DIGEST | HuksTagType.HUKS\_TAG\_TYPE\_UINT | 4 | 

表示摘要算法的Tag。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_TAG\_PADDING | HuksTagType.HUKS\_TAG\_TYPE\_UINT | 5 | 

表示填充模式的Tag。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_TAG\_BLOCK\_MODE | HuksTagType.HUKS\_TAG\_TYPE\_UINT | 6 | 

表示加密模式的Tag。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_TAG\_KEY\_TYPE | HuksTagType.HUKS\_TAG\_TYPE\_UINT | 7 | 

表示密钥类型的Tag。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_TAG\_ASSOCIATED\_DATA | HuksTagType.HUKS\_TAG\_TYPE\_BYTES | 8 | 

表示附加身份验证数据的Tag。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_TAG\_NONCE | HuksTagType.HUKS\_TAG\_TYPE\_BYTES | 9 | 

表示密钥加解密的NONCE字段。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_TAG\_IV | HuksTagType.HUKS\_TAG\_TYPE\_BYTES | 10 | 

表示密钥初始化的向量。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_TAG\_INFO | HuksTagType.HUKS\_TAG\_TYPE\_BYTES | 11 | 

表示密钥派生时的info。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_TAG\_SALT | HuksTagType.HUKS\_TAG\_TYPE\_BYTES | 12 | 

表示密钥派生时的盐值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_TAG\_PWD(deprecated) | HuksTagType.HUKS\_TAG\_TYPE\_BYTES | 13 | 

表示密钥派生时的password。

**说明：** 从API version 8开始，从API version 9开始废弃。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_TAG\_ITERATION | HuksTagType.HUKS\_TAG\_TYPE\_UINT | 14 | 

表示密钥派生时的迭代次数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_TAG\_KEY\_GENERATE\_TYPE | HuksTagType.HUKS\_TAG\_TYPE\_UINT | 15 | 

表示生成密钥类型的Tag。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_TAG\_DERIVE\_MAIN\_KEY(deprecated) | HuksTagType.HUKS\_TAG\_TYPE\_BYTES | 16 | 

表示密钥派生时的主密钥。

**说明：** 从API version 8开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.Security.Huks.Extension

 |
| HUKS\_TAG\_DERIVE\_FACTOR(deprecated) | HuksTagType.HUKS\_TAG\_TYPE\_BYTES | 17 | 

表示密钥派生时的派生因子。

**说明：** 从API version 8开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.Security.Huks.Extension

 |
| HUKS\_TAG\_DERIVE\_ALG(deprecated) | HuksTagType.HUKS\_TAG\_TYPE\_UINT | 18 | 

表示密钥派生时的算法类型。

**说明：** 从API version 8开始，从API version 9开始废弃。

**系统能力：** SystemCapability.Security.Huks.Extension

 |
| HUKS\_TAG\_AGREE\_ALG | HuksTagType.HUKS\_TAG\_TYPE\_UINT | 19 | 

表示密钥协商时的算法类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_TAG\_AGREE\_PUBLIC\_KEY\_IS\_KEY\_ALIAS | HuksTagType.HUKS\_TAG\_TYPE\_BOOL | 20 | 

表示密钥协商时的公钥别名。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_TAG\_AGREE\_PRIVATE\_KEY\_ALIAS | HuksTagType.HUKS\_TAG\_TYPE\_BYTES | 21 | 

表示密钥协商时的私钥别名。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_TAG\_AGREE\_PUBLIC\_KEY | HuksTagType.HUKS\_TAG\_TYPE\_BYTES | 22 | 

表示密钥协商时的公钥。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_TAG\_KEY\_ALIAS | HuksTagType.HUKS\_TAG\_TYPE\_BYTES | 23 | 

表示密钥别名。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_TAG\_DERIVE\_KEY\_SIZE | HuksTagType.HUKS\_TAG\_TYPE\_UINT | 24 | 

表示派生密钥的大小。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_TAG\_IMPORT\_KEY\_TYPE9+ | HuksTagType.HUKS\_TAG\_TYPE\_UINT | 25 | 

表示导入的密钥类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension9-11

 |
| HUKS\_TAG\_UNWRAP\_ALGORITHM\_SUITE9+ | HuksTagType.HUKS\_TAG\_TYPE\_UINT | 26 | 

表示安全导入密钥的套件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension9-11

 |
| HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG10+ | HuksTagType.HUKS\_TAG\_TYPE\_UINT |29 | 

表示派生密钥/协商密钥的存储类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension10-11

 |
| HUKS\_TAG\_RSA\_PSS\_SALT\_LEN\_TYPE10+ | HuksTagType.HUKS\_TAG\_TYPE\_UINT |30 | 

表示rsa\_pss\_salt\_length的类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension10-11

 |
| HUKS\_TAG\_ACTIVE\_DATETIME(deprecated) | HuksTagType.HUKS\_TAG\_TYPE\_ULONG | 201 | 

原为证书业务预留字段，当前证书管理已独立，此字段废弃，不再预留。

**说明：** 从API version 9开始废弃，无替代接口。

**系统能力：** SystemCapability.Security.Huks.Extension

 |
| HUKS\_TAG\_ORIGINATION\_EXPIRE\_DATETIME(deprecated) | HuksTagType.HUKS\_TAG\_TYPE\_ULONG | 202 | 

原为证书业务预留字段，当前证书管理已独立，此字段废弃，不再预留。

**说明：** 从API version 9开始废弃，无替代接口。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_TAG\_USAGE\_EXPIRE\_DATETIME(deprecated) | HuksTagType.HUKS\_TAG\_TYPE\_ULONG | 203 | 

原为证书业务预留字段，当前证书管理已独立，此字段废弃，不再预留。

**说明：** 从API version 9开始废弃，无替代接口。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_TAG\_CREATION\_DATETIME(deprecated) | HuksTagType.HUKS\_TAG\_TYPE\_ULONG | 204 | 

原为证书业务预留字段，当前证书管理已独立，此字段废弃，不再预留。

**说明：** 从API version 9开始废弃，无替代接口。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_TAG\_ALL\_USERS | HuksTagType.HUKS\_TAG\_TYPE\_BOOL | 301 | 

预留。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_TAG\_USER\_ID | HuksTagType.HUKS\_TAG\_TYPE\_UINT | 302 | 

表示当前密钥属于哪个userID。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_TAG\_NO\_AUTH\_REQUIRED | HuksTagType.HUKS\_TAG\_TYPE\_BOOL | 303 | 

预留。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_TAG\_USER\_AUTH\_TYPE | HuksTagType.HUKS\_TAG\_TYPE\_UINT | 304 | 

表示用户认证类型。从[HuksUserAuthType](#huksuserauthtype9)中选择，需要与安全访问控制类型同时设置。支持同时指定两种用户认证类型，如：安全访问控制类型指定为HUKS\_AUTH\_ACCESS\_INVALID\_NEW\_BIO\_ENROLL时，密钥访问认证类型可以指定以下三种： HUKS\_USER\_AUTH\_TYPE\_FACE 、HUKS\_USER\_AUTH\_TYPE\_FINGERPRINT、HUKS\_USER\_AUTH\_TYPE\_FACE | HUKS\_USER\_AUTH\_TYPE\_FINGERPRINT

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

 |
| HUKS\_TAG\_AUTH\_TIMEOUT | HuksTagType.HUKS\_TAG\_TYPE\_UINT | 305 | 

表示auth token单次有效期。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

 |
| HUKS\_TAG\_AUTH\_TOKEN | HuksTagType.HUKS\_TAG\_TYPE\_BYTES | 306 | 

用于传入authToken的字段。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

 |
| HUKS\_TAG\_KEY\_AUTH\_ACCESS\_TYPE9+ | HuksTagType.HUKS\_TAG\_TYPE\_UINT | 307 | 

表示安全访问控制类型。从[HuksAuthAccessType](#huksauthaccesstype9)中选择，需要和用户认证类型同时设置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

 |
| HUKS\_TAG\_KEY\_SECURE\_SIGN\_TYPE9+ | HuksTagType.HUKS\_TAG\_TYPE\_UINT | 308 | 

表示生成或导入密钥时，指定该密钥的签名类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

 |
| HUKS\_TAG\_CHALLENGE\_TYPE9+ | HuksTagType.HUKS\_TAG\_TYPE\_UINT | 309 | 

表示密钥使用时生成的challenge类型。从[HuksChallengeType](#hukschallengetype9)中选择。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

 |
| HUKS\_TAG\_CHALLENGE\_POS9+ | HuksTagType.HUKS\_TAG\_TYPE\_UINT | 310 | 

表示challenge类型为用户自定义类型时，huks产生的challenge有效长度仅为8字节连续的数据。从[HuksChallengePosition](#hukschallengeposition9)中选择。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

 |
| HUKS\_TAG\_KEY\_AUTH\_PURPOSE10+ | HuksTagType.HUKS\_TAG\_TYPE\_UINT |311 | 

表示密钥认证用途的tag。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

 |
| HUKS\_TAG\_AUTH\_STORAGE\_LEVEL11+ | HuksTagType.HUKS\_TAG\_TYPE\_UINT |316 | 

表示密钥存储安全等级的tag。从[HuksAuthStorageLevel](#huksauthstoragelevel11)中选择。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

 |
| HUKS\_TAG\_USER\_AUTH\_MODE12+ | HuksTagType.HUKS\_TAG\_TYPE\_UINT | 319 | 

表示用户认证模式。从[HuksUserAuthMode](#huksuserauthmode12)中选择。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

 |
| HUKS\_TAG\_ATTESTATION\_CHALLENGE | HuksTagType.HUKS\_TAG\_TYPE\_BYTES | 501 | 

表示attestation时的挑战值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

 |
| HUKS\_TAG\_ATTESTATION\_APPLICATION\_ID | HuksTagType.HUKS\_TAG\_TYPE\_BYTES | 502 | 

表示attestation时拥有该密钥的application的Id。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

 |
| HUKS\_TAG\_ATTESTATION\_ID\_BRAND(deprecated) | HuksTagType.HUKS\_TAG\_TYPE\_BYTES | 503 | 

表示设备的品牌。

**说明：** 从API version 8开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.Security.Huks.Extension

 |
| HUKS\_TAG\_ATTESTATION\_ID\_DEVICE(deprecated) | HuksTagType.HUKS\_TAG\_TYPE\_BYTES | 504 | 

表示设备的设备ID。

**说明：** 从API version 8开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.Security.Huks.Extension

 |
| HUKS\_TAG\_ATTESTATION\_ID\_PRODUCT(deprecated) | HuksTagType.HUKS\_TAG\_TYPE\_BYTES | 505 | 

表示设备的产品名。

**说明：** 从API version 8开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.Security.Huks.Extension

 |
| HUKS\_TAG\_ATTESTATION\_ID\_SERIAL(deprecated) | HuksTagType.HUKS\_TAG\_TYPE\_BYTES | 506 | 

表示设备的SN号。

**说明：** 从API version 8开始，从API version 9开始废弃。

**系统能力：** SystemCapability.Security.Huks.Extension

 |
| HUKS\_TAG\_ATTESTATION\_ID\_IMEI(deprecated) | HuksTagType.HUKS\_TAG\_TYPE\_BYTES | 507 | 

表示设备的IMEI号。

**说明：** 从API version 8开始，从API version 9开始废弃。

**系统能力：** SystemCapability.Security.Huks.Extension

 |
| HUKS\_TAG\_ATTESTATION\_ID\_MEID(deprecated) | HuksTagType.HUKS\_TAG\_TYPE\_BYTES | 508 | 

表示设备的MEID号。

**说明：** 从API version 8开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.Security.Huks.Extension

 |
| HUKS\_TAG\_ATTESTATION\_ID\_MANUFACTURER(deprecated) | HuksTagType.HUKS\_TAG\_TYPE\_BYTES | 509 | 

表示设备的制造商。

**说明：** 从API version 8开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.Security.Huks.Extension

 |
| HUKS\_TAG\_ATTESTATION\_ID\_MODEL(deprecated) | HuksTagType.HUKS\_TAG\_TYPE\_BYTES | 510 | 

表示设备的型号。

**说明：** 从API version 8开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.Security.Huks.Extension

 |
| HUKS\_TAG\_ATTESTATION\_ID\_ALIAS | HuksTagType.HUKS\_TAG\_TYPE\_BYTES | 511 | 

表示attestation时的密钥别名。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

 |
| HUKS\_TAG\_ATTESTATION\_ID\_SOCID(deprecated) | HuksTagType.HUKS\_TAG\_TYPE\_BYTES | 512 | 

表示设备的SOCID。

**说明：** 从API version 8开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.Security.Huks.Extension

 |
| HUKS\_TAG\_ATTESTATION\_ID\_UDID(deprecated) | HuksTagType.HUKS\_TAG\_TYPE\_BYTES | 513 | 

表示设备的UDID。

**说明：** 从API version 8开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.Security.Huks.Extension

 |
| HUKS\_TAG\_ATTESTATION\_ID\_SEC\_LEVEL\_INFO | HuksTagType.HUKS\_TAG\_TYPE\_BYTES | 514 | 

表示attestation时的安全凭据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

 |
| HUKS\_TAG\_ATTESTATION\_ID\_VERSION\_INFO | HuksTagType.HUKS\_TAG\_TYPE\_BYTES | 515 | 

表示attestation时的版本号。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

 |
| HUKS\_TAG\_KEY\_OVERRIDE20+ | HuksTagType.HUKS\_TAG\_TYPE\_BOOL | 520 | 

表示是否覆写同名密钥。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_TAG\_AE\_TAG\_LEN22+ | HuksTagType.HUKS\_TAG\_TYPE\_UINT | 521 | 

表示指定的AEAD标签长度。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_TAG\_KEY\_CLASS22+ | HuksTagType.HUKS\_TAG\_TYPE\_UINT | 522 | 

表示密钥来源。

**系统能力：** SystemCapability.Security.Huks.Extension

 |
| HUKS\_TAG\_KEY\_ACCESS\_GROUP23+ | HuksTagType.HUKS\_TAG\_TYPE\_BYTES | 523 | 

表示指定的分组信息。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

 |
| HUKS\_TAG\_IS\_KEY\_ALIAS | HuksTagType.HUKS\_TAG\_TYPE\_BOOL | 1001 | 

表示是否使用生成key时传入的别名的Tag。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_TAG\_KEY\_STORAGE\_FLAG | HuksTagType.HUKS\_TAG\_TYPE\_UINT | 1002 | 

表示密钥存储方式的Tag。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_TAG\_IS\_ALLOWED\_WRAP | HuksTagType.HUKS\_TAG\_TYPE\_BOOL | 1003 | 

预留。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_TAG\_KEY\_WRAP\_TYPE | HuksTagType.HUKS\_TAG\_TYPE\_UINT | 1004 | 

预留。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_TAG\_KEY\_AUTH\_ID | HuksTagType.HUKS\_TAG\_TYPE\_BYTES | 1005 | 

预留。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

 |
| HUKS\_TAG\_KEY\_ROLE | HuksTagType.HUKS\_TAG\_TYPE\_UINT | 1006 | 

预留。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_TAG\_KEY\_FLAG | HuksTagType.HUKS\_TAG\_TYPE\_UINT | 1007 | 

表示密钥标志的Tag。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_TAG\_IS\_ASYNCHRONIZED | HuksTagType.HUKS\_TAG\_TYPE\_UINT | 1008 | 

预留。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_TAG\_SECURE\_KEY\_ALIAS(deprecated) | HuksTagType.HUKS\_TAG\_TYPE\_BOOL | 1009 | 

原为预留字段。

**说明：** 从API version 9开始废弃，无替代接口。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_TAG\_SECURE\_KEY\_UUID(deprecated) | HuksTagType.HUKS\_TAG\_TYPE\_BYTES | 1010 | 

原为预留字段。

**说明：** 从API version 9开始废弃，无替代接口。

**系统能力：** SystemCapability.Security.Huks.Extension

 |
| HUKS\_TAG\_KEY\_DOMAIN | HuksTagType.HUKS\_TAG\_TYPE\_UINT | 1011 | 

预留。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_TAG\_IS\_DEVICE\_PASSWORD\_SET11+ | HuksTagType.HUKS\_TAG\_TYPE\_BOOL | 1012 | 

表示密钥锁屏密码访问控制字段，可限制密钥只有在用户设置了锁屏密码时可用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Extension

 |
| HUKS\_TAG\_PROCESS\_NAME(deprecated) | HuksTagType.HUKS\_TAG\_TYPE\_BYTES | 10001 | 

表示进程名称的Tag。

**说明：** 从API version 8开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_TAG\_PACKAGE\_NAME(deprecated) | HuksTagType.HUKS\_TAG\_TYPE\_BYTES | 10002 | 

原为预留字段。

**说明：** 从API version 9开始废弃，无替代接口。

**系统能力：** SystemCapability.Security.Huks.Extension

 |
| HUKS\_TAG\_ACCESS\_TIME(deprecated) | HuksTagType.HUKS\_TAG\_TYPE\_UINT | 10003 | 

原为预留字段。

**说明：** 从API version 9开始废弃，无替代接口。

**系统能力：** SystemCapability.Security.Huks.Extension

 |
| HUKS\_TAG\_USES\_TIME(deprecated) | HuksTagType.HUKS\_TAG\_TYPE\_UINT | 10004 | 

原为预留字段。

**说明：** 从API version 9开始废弃，无替代接口。

**系统能力：** SystemCapability.Security.Huks.Extension

 |
| HUKS\_TAG\_CRYPTO\_CTX(deprecated) | HuksTagType.HUKS\_TAG\_TYPE\_ULONG | 10005 | 

原为预留字段。

**说明：** 从API version 9开始废弃，无替代接口。

**系统能力：** SystemCapability.Security.Huks.Extension

 |
| HUKS\_TAG\_KEY | HuksTagType.HUKS\_TAG\_TYPE\_BYTES | 10006 | 

预留。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_TAG\_KEY\_VERSION(deprecated) | HuksTagType.HUKS\_TAG\_TYPE\_UINT | 10007 | 

表示密钥版本的Tag。

**说明：** 从API version 8开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.Security.Huks.Extension

 |
| HUKS\_TAG\_PAYLOAD\_LEN(deprecated) | HuksTagType.HUKS\_TAG\_TYPE\_UINT | 10008 | 

原为预留字段。

**说明：** 从API version 9开始废弃，无替代接口。

**系统能力：** SystemCapability.Security.Huks.Extension

 |
| HUKS\_TAG\_AE\_TAG | HuksTagType.HUKS\_TAG\_TYPE\_BYTES | 10009 | 

用于传入GCM模式中的AEAD数据的字段。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_TAG\_IS\_KEY\_HANDLE(deprecated) | HuksTagType.HUKS\_TAG\_TYPE\_ULONG | 10010 | 

原为预留字段。

**说明：** 从API version 9开始废弃，无替代接口。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_TAG\_OS\_VERSION(deprecated) | HuksTagType.HUKS\_TAG\_TYPE\_UINT | 10101 | 

表示操作系统版本的Tag。

**说明：** 从API version 8开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_TAG\_OS\_PATCHLEVEL(deprecated) | HuksTagType.HUKS\_TAG\_TYPE\_UINT | 10102 | 

表示操作系统补丁级别的Tag。

**说明：** 从API version 8开始支持，从API version 9开始废弃。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_TAG\_SYMMETRIC\_KEY\_DATA | HuksTagType.HUKS\_TAG\_TYPE\_BYTES | 20001 | 

预留。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core

 |
| HUKS\_TAG\_ASYMMETRIC\_PUBLIC\_KEY\_DATA | HuksTagType.HUKS\_TAG\_TYPE\_BYTES | 20002 | 

预留。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |
| HUKS\_TAG\_ASYMMETRIC\_PRIVATE\_KEY\_DATA | HuksTagType.HUKS\_TAG\_TYPE\_BYTES | 20003 | 

预留。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Huks.Core12+

SystemCapability.Security.Huks.Extension8-11

 |

#### huks.getSdkVersion(deprecated)

getSdkVersion(options: HuksOptions) : string

获取当前系统sdk版本。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/pLLv0tRTSvCjgPurIaGFKg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014821Z&HW-CC-Expire=86400&HW-CC-Sign=02F8E66CF6F5327A8F16977BD0860426B1ADBD0CE143272B554078D0CD3B5948)

从API version 8开始支持，从API version 11开始废弃。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [HuksOptions](#huksoptions) | 是 | 空对象（此处传空即可）。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 返回sdk版本。 |

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';

/* 此处options选择emptyOptions传空 */
let emptyOptions: huks.HuksOptions = {
  properties: []
};
let result = huks.getSdkVersion(emptyOptions);
```

#### huks.generateKey(deprecated)

generateKey(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksResult>) : void

生成密钥。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/X82FXG-5R3izZoYK8U5Cpg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014821Z&HW-CC-Expire=86400&HW-CC-Sign=F895F133D4F6798874597D7F2019A8B6DABE52A5CB200A0C99E78C84403C5A37)

从API version 8开始支持，从API version 9开始废弃，建议使用[huks.generateKeyItem9+](#huksgeneratekeyitem9)替代。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| keyAlias | string | 是 | 密钥别名。密钥别名的最大长度为128字节，建议不包含个人信息等敏感词汇。 |
| options | [HuksOptions](#huksoptions) | 是 | 用于存放生成key所需TAG。 |
| callback | AsyncCallback<[HuksResult](#huksresultdeprecated)\> | 是 | 回调函数。当生成密钥成功时，err为undefined，data为获取到的HuksResult；否则为错误对象。 |

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';

/* 以生成RSA512密钥为例 */

let keyAlias = 'keyAlias';
let properties: Array<huks.HuksParam> = [
  {
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_RSA
  },
  {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_512
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_OAEP
  },
  {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
  }
];
let options: huks.HuksOptions = {
  properties: properties
};
huks.generateKey(keyAlias, options, (err, data) => {
});
```

#### huks.generateKey(deprecated)

generateKey(keyAlias: string, options: HuksOptions) : Promise<HuksResult>

生成密钥。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/r-oqiu_jREq0MCqNrERpMw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014821Z&HW-CC-Expire=86400&HW-CC-Sign=628A2C96E07506CC698716C6AC44D54DEC57DD3BA830D8077DF10AC83698029F)

从API version 8开始支持，从API version 9开始废弃，建议使用[huks.generateKeyItem9+](#huksgeneratekeyitem9-1)替代。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| keyAlias | string | 是 | 密钥别名。密钥别名的最大长度为128字节，建议不包含个人信息等敏感词汇。 |
| options | [HuksOptions](#huksoptions) | 是 | 用于存放生成key所需TAG。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<[HuksResult](#huksresultdeprecated)\> | Promise对象。返回HuksResult。 |

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';

/* 以生成ECC256密钥为例 */

let keyAlias = 'keyAlias';
let properties: Array<huks.HuksParam> = [
  {
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_ECC
  },
  {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_ECC_KEY_SIZE_256
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
  },
  {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
  }
];
let options: huks.HuksOptions = {
  properties: properties
};
let result = huks.generateKey(keyAlias, options);
```

#### huks.deleteKey(deprecated)

deleteKey(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksResult>) : void

删除密钥。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/iwNkVwpITAKeWMu9jSFpRw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014821Z&HW-CC-Expire=86400&HW-CC-Sign=90B4CDA53F21876C8741F04AFD096848341B058E0BA4A506EE3710BD7467EE1D)

从API version 8开始支持，从API version 9开始废弃，建议使用[huks.deleteKeyItem9+](#huksdeletekeyitem9)替代。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| keyAlias | string | 是 | 密钥别名，应为生成key时传入的别名。 |
| options | [HuksOptions](#huksoptions) | 是 | 用于删除时指定密钥的属性TAG。 |
| callback | AsyncCallback<[HuksResult](#huksresultdeprecated)\> | 是 | 回调函数。当删除密钥成功时，err为undefined，data为获取到的HuksResult；否则为错误对象。 |

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';

/* 此处options选择emptyOptions传空 */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};
huks.deleteKey(keyAlias, emptyOptions, (err, data) => {
});
```

#### huks.deleteKey(deprecated)

deleteKey(keyAlias: string, options: HuksOptions) : Promise<HuksResult>

删除密钥。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/e9vPoa4CQ_-KQAbDSHIeGQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014821Z&HW-CC-Expire=86400&HW-CC-Sign=AC4FBE5B40D2A315BF135B465878B6195387375132432704D5C391EEF8BFAC85)

从API version 8开始支持，从API version 9开始废弃，建议使用[huks.deleteKeyItem9+](#huksdeletekeyitem9-1)替代。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| keyAlias | string | 是 | 密钥别名，应为生成key时传入的别名。 |
| options | [HuksOptions](#huksoptions) | 是 | 用于删除时指定密钥的属性TAG。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[HuksResult](#huksresultdeprecated)\> | Promise对象。返回HuksResult。 |

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';
import { BusinessError } from "@kit.BasicServicesKit"

/* 此处options选择emptyOptions传空 */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};
let result = huks.deleteKey(keyAlias, emptyOptions).then((data) => {
  console.info('delete key success');
}).catch((err: BusinessError) => {
  console.error("密钥删除失败，错误码是： " + err.code + " 错误码信息： " + err.message);
});
```

#### huks.importKey(deprecated)

importKey(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksResult>) : void

导入明文密钥，使用Callback方式回调异步返回结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/BU8eV5lOSt2E6XoClAxGOA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014821Z&HW-CC-Expire=86400&HW-CC-Sign=37B3199D620F83A4223F42DE93E1A54D4FBED8D17DED88F93A80CE10A7770804)

从API version 8开始支持，从API version 9开始废弃，建议使用[huks.importKeyItem9+](#huksimportkeyitem9)替代。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| keyAlias | string | 是 | 密钥别名。密钥别名的最大长度为128字节，建议不包含个人信息等敏感词汇。 |
| options | [HuksOptions](#huksoptions) | 是 | 用于导入时所需TAG和需要导入的密钥。 |
| callback | AsyncCallback<[HuksResult](#huksresultdeprecated)\> | 是 | 回调函数。当导入密钥成功时，err为undefined，data为获取到的HuksResult；否则为错误对象。 |

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';

/* 以导入AES256密钥为例 */

let plainTextSize32 = makeRandomArr(32);

function makeRandomArr(size: number) {
  let arr = new Uint8Array(size);
  for (let i = 0; i < size; i++) {
    arr[i] = Math.floor(Math.random() * 10);
  }
  return arr;
};
let keyAlias = 'keyAlias';
let properties: Array<huks.HuksParam> = [
  {
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_AES
  },
  {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value:
    huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_PKCS7
  },
  {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_ECB
  }
];
let options: huks.HuksOptions = {
  properties: properties,
  inData: plainTextSize32
};
huks.importKey(keyAlias, options, (err, data) => {
});
```

#### huks.importKey(deprecated)

importKey(keyAlias: string, options: HuksOptions) : Promise<HuksResult>

导入明文密钥。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/7Lo98jZjQ8qdPM1GisF_Cg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014821Z&HW-CC-Expire=86400&HW-CC-Sign=1AF4B2B1DDC321B28E50E23B163ACBB399204A68AD618B014BE68B3110CC2654)

从API version 8开始支持，从API version 9开始废弃，建议使用[huks.importKeyItem9+](#huksimportkeyitem9-1)替代。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| keyAlias | string | 是 | 密钥别名。密钥别名的最大长度为128字节，建议不包含个人信息等敏感词汇。 |
| options | [HuksOptions](#huksoptions) | 是 | 用于导入时所需TAG和需要导入的密钥。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[HuksResult](#huksresultdeprecated)\> | Promise对象。返回HuksResult。 |

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';

/* 以导入AES128为例 */

function makeRandomArr(size: number) {
  let arr = new Uint8Array(size);
  for (let i = 0; i < size; i++) {
    arr[i] = Math.floor(Math.random() * 10);
  }
  return arr;
};

/* 第一步：生成密钥 */
let plainTextSize32 = makeRandomArr(32);
let keyAlias = 'keyAlias';
let properties: Array<huks.HuksParam> = [
  {
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_AES
  },
  {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_128
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_PKCS7
  },
  {
    tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
    value: huks.HuksCipherMode.HUKS_MODE_ECB
  }
];
let huksOptions: huks.HuksOptions = {
  properties: properties,
  inData: plainTextSize32
};
/* 第二步：导入密钥 */
let result = huks.importKey(keyAlias, huksOptions);
```

#### huks.exportKey(deprecated)

exportKey(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksResult>) : void

导出密钥，使用Callback方式回调异步返回的结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/YHR52kl7Qla1O4r_xeoxAQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014821Z&HW-CC-Expire=86400&HW-CC-Sign=7E2D1045D334B5FCD07F761E928BE5B97FCD74E8A85D20E09179073F70EEE202)

从API version 8开始支持，从API version 9开始废弃，建议使用[huks.exportKeyItem9+](#huksexportkeyitem9)替代。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| keyAlias | string | 是 | 密钥别名，应与所用密钥生成时使用的别名相同。 |
| options | [HuksOptions](#huksoptions) | 是 | 空对象（此处传空即可）。 |
| callback | AsyncCallback<[HuksResult](#huksresultdeprecated)\> | 是 | 回调函数。当导出密钥成功时，err为undefined，data为获取到的HuksResult；否则为错误对象。HuksResult的outData返回从密钥中导出的公钥。 |

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';

/* 此处options选择emptyOptions来传空 */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};
huks.exportKey(keyAlias, emptyOptions, (err, data) => {
});
```

#### huks.exportKey(deprecated)

exportKey(keyAlias: string, options: HuksOptions) : Promise<HuksResult>

导出密钥。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/I97_XIUVT0G_WZAni5Z_jw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014821Z&HW-CC-Expire=86400&HW-CC-Sign=5FF29CE9526D70B77EE5B8975D087BD8ED69D2121628715CA5B117EC6A6C8D9E)

从API version 8开始支持，从API version 9开始废弃，建议使用[huks.exportKeyItem9+](#huksexportkeyitem9-1)替代。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| keyAlias | string | 是 | 密钥别名，应与所用密钥生成时使用的别名相同。 |
| options | [HuksOptions](#huksoptions) | 是 | 空对象（此处传空即可）。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[HuksResult](#huksresultdeprecated)\> | Promise对象。返回HuksResult。HuksResult的outData返回从HUKS中导出的公钥。 |

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';

/* 此处options选择emptyOptions来传空 */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};
let result = huks.exportKey(keyAlias, emptyOptions);
```

#### huks.getKeyProperties(deprecated)

getKeyProperties(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksResult>) : void

获取密钥属性。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/5FmK001RSgKMJJDOwyBLQQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014821Z&HW-CC-Expire=86400&HW-CC-Sign=5A10101CD4A36F7D99F4E9CB37843387B052EC1C2ADD2A6C2AE33597904964D0)

从API version 8开始支持，从API version 9开始废弃，建议使用[huks.getKeyItemProperties9+](#huksgetkeyitemproperties9)替代。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| keyAlias | string | 是 | 密钥别名，应与所用密钥生成时使用的别名相同。 |
| options | [HuksOptions](#huksoptions) | 是 | 空对象（此处传空即可）。 |
| callback | AsyncCallback<[HuksResult](#huksresultdeprecated)\> | 是 | 回调函数。当获取密钥属性成功时，err为undefined，data为获取到的HuksResult；否则为错误对象。 |

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';

/* 此处options选择emptyOptions来传空 */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};
huks.getKeyProperties(keyAlias, emptyOptions, (err, data) => {
});
```

#### huks.getKeyProperties(deprecated)

getKeyProperties(keyAlias: string, options: HuksOptions) : Promise<HuksResult>

获取密钥属性。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/8whST_4BQmiALIwn8bRfHg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014821Z&HW-CC-Expire=86400&HW-CC-Sign=A850E2A269476960945419DF2BF1180F5352E9321FBA40E7C7487C4ABA180EF9)

从API version 8开始支持，从API version 9开始废弃，建议使用[huks.getKeyItemProperties9+](#huksgetkeyitemproperties9-1)替代。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| keyAlias | string | 是 | 密钥别名，应与所用密钥生成时使用的别名相同。 |
| options | [HuksOptions](#huksoptions) | 是 | 空对象（此处传空即可）。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[HuksResult](#huksresultdeprecated)\> | Promise对象。返回HuksResult。HuksResult的properties返回密钥参数。 |

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';

/* 此处options选择emptyOptions来传空 */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};
let result = huks.getKeyProperties(keyAlias, emptyOptions);
```

#### huks.isKeyExist(deprecated)

isKeyExist(keyAlias: string, options: HuksOptions, callback: AsyncCallback<boolean>) : void

判断密钥是否存在。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/XCOm84ImR2WPBw6bbIxjpA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014821Z&HW-CC-Expire=86400&HW-CC-Sign=332F74CDD22378B93E1E8A03F147E0BBE2052D23A91EB795E8D3E63A2EC10581)

从API version 8开始支持，从API version 9开始废弃，建议使用[huks.isKeyItemExist9+](#huksiskeyitemexist9)替代。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| keyAlias | string | 是 | 所需查找的密钥的别名。 |
| options | [HuksOptions](#huksoptions) | 是 | 用于查询时指定密钥的属性TAG。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。false代表密钥不存在，true代表密钥存在。 |

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';

/* 此处options选择emptyOptions来传空 */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};
huks.isKeyExist(keyAlias, emptyOptions, (err, data) => {
});
```

#### huks.isKeyExist(deprecated)

isKeyExist(keyAlias: string, options: HuksOptions) : Promise<boolean>

判断密钥是否存在。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/cyi2MGQFS_6kgdlGqKyQug/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014821Z&HW-CC-Expire=86400&HW-CC-Sign=F8E87814BFC48E43F52F17F7868C300DA73A19CCC22DA0F673B0FD5FD13D08BF)

从API version 8开始支持，从API version 9开始废弃，建议使用[huks.isKeyItemExist9+](#huksiskeyitemexist9-1)替代。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| keyAlias | string | 是 | 所需查找的密钥的别名。 |
| options | [HuksOptions](#huksoptions) | 是 | 用于查询时指定密钥的属性TAG。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象。false代表密钥不存在，true代表密钥存在。 |

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';

/* 此处options选择emptyOptions来传空 */
let keyAlias = 'keyAlias';
let emptyOptions: huks.HuksOptions = {
  properties: []
};
let result = huks.isKeyExist(keyAlias, emptyOptions);
```

#### huks.init(deprecated)

init(keyAlias: string, options: HuksOptions, callback: AsyncCallback<HuksHandle>) : void

init操作密钥接口。使用callback异步回调。

huks.init、huks.update、huks.finish为三段式接口，需要一起使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/KR7dyHpIR--OYSfSushhRg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014821Z&HW-CC-Expire=86400&HW-CC-Sign=CC373125C33925279D0A4A5626ADBB93B928C2A9AB15787FE734C97D99E515B2)

从API version 8开始支持，从API version 9开始废弃，建议使用[huks.initSession9+](#huksinitsession9-1)替代。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| keyAlias | string | 是 | Init操作密钥的别名。 |
| options | [HuksOptions](#huksoptions) | 是 | Init操作的参数集合。 |
| callback | AsyncCallback<[HuksHandle](#hukshandledeprecated)\> | 是 | 回调函数。当密钥操作init成功时，err为undefined，data为获取到的HuksHandle；否则为错误对象。HuksHandle的handle返回init生成的handle。 |

#### huks.init(deprecated)

init(keyAlias: string, options: HuksOptions) : Promise<HuksHandle>

init操作密钥接口。使用Promise异步回调。

huks.init、huks.update、huks.finish为三段式接口，需要一起使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/jpY9rQqlTcqhlkHigL9Nvw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014821Z&HW-CC-Expire=86400&HW-CC-Sign=12A523D552BEB7635AC0C0E9D0FD75AF2C937FC6D534C4AFC848AFF3D1C07E93)

从API version 8开始支持，从API version 9开始废弃，建议使用[huks.initSession9+](#huksinitsession9-1)替代。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| keyAlias | string | 是 | Init操作密钥的别名。 |
| options | [HuksOptions](#huksoptions) | 是 | Init参数集合。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<[HuksHandle](#hukshandledeprecated)\> | Promise对象。返回HuksResult。HuksHandle的handle返回init生成的handle。 |

#### huks.update(deprecated)

update(handle: number, token?: Uint8Array, options: HuksOptions, callback: AsyncCallback<HuksResult>) : void

update操作密钥接口。使用callback异步回调。

huks.init、huks.update、huks.finish为三段式接口，需要一起使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/n2ZcSwosQhiebGUfn5B3EA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014821Z&HW-CC-Expire=86400&HW-CC-Sign=3B5F0DBB6732D1210C64E3EFCFA40959B64CDFD49D44D1DEA1B90772CB2D5E7F)

从API version 8开始支持，从API version 9开始废弃，建议使用[huks.updateSession9+](#huksupdatesession9-1)替代。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| handle | number | 是 | Update操作的uint64类型的handle值。 |
| token | Uint8Array | 否 | Update操作的token。 |
| options | [HuksOptions](#huksoptions) | 是 | Update操作的参数集合。 |
| callback | AsyncCallback<[HuksResult](#huksresultdeprecated)\> | 是 | 回调函数。当密钥操作update成功时，err为undefined，data为获取到的HuksResult；否则为错误对象。 |

#### huks.update(deprecated)

update(handle: number, token?: Uint8Array, options: HuksOptions) : Promise<HuksResult>

update操作密钥接口。使用Promise异步回调。

huks.init、huks.update、huks.finish为三段式接口，需要一起使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/zHlZT2F3ToGe0qyn4m-RYw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014821Z&HW-CC-Expire=86400&HW-CC-Sign=C5ACF420E70ADB0BECEAE989A084725104EED00C5B8F879B6A7A7821EEC3E0B6)

从API version 8开始支持，从API version 9开始废弃，建议使用[huks.updateSession9+](#huksupdatesession9-2)替代。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| handle | number | 是 | Update操作的uint64类型的handle值。 |
| token | Uint8Array | 否 | Update操作的token。 |
| options | [HuksOptions](#huksoptions) | 是 | Update操作的参数集合。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<[HuksResult](#huksresultdeprecated)\> | Promise对象。返回HuksResult。 |

#### huks.finish(deprecated)

finish(handle: number, options: HuksOptions, callback: AsyncCallback<HuksResult>) : void

finish操作密钥接口。使用callback异步回调。

huks.init、huks.update、huks.finish为三段式接口，需要一起使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/kk0N95G8Q8K79MQ-csOKpg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014821Z&HW-CC-Expire=86400&HW-CC-Sign=AA6FBD83953B1A7628D01E7017624B515F04551F9F0E5AD836210C78A89DBD28)

从API version 8开始支持，从API version 9开始废弃，建议使用[huks.finishSession9+](#huksfinishsession9)替代。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| handle | number | 是 | Finish操作的uint64类型的handle值。 |
| options | [HuksOptions](#huksoptions) | 是 | Finish的参数集合。 |
| callback | AsyncCallback<[HuksResult](#huksresultdeprecated)\> | 是 | 回调函数。当密钥操作finish成功时，err为undefined，data为获取到的HuksResult；否则为错误对象。 |

#### huks.finish(deprecated)

finish(handle: number, options: HuksOptions) : Promise<HuksResult>

finish操作密钥接口。使用Promise异步回调。

huks.init、huks.update、huks.finish为三段式接口，需要一起使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/m7bdrhomQhCmiQO_1xG5PA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014821Z&HW-CC-Expire=86400&HW-CC-Sign=8480E166D999F51D3658DA61E819D01EB3B6A90245BAD662514652212733606E)

从API version 8开始支持，从API version 9开始废弃，建议使用[huks.finishSession9+](#huksfinishsession9-1)替代。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| handle | number | 是 | Finish操作的uint64类型的handle值。 |
| options | [HuksOptions](#huksoptions) | 是 | Finish操作的参数集合。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<[HuksResult](#huksresultdeprecated)\> | Promise对象。返回HuksResult。 |

#### huks.abort(deprecated)

abort(handle: number, options: HuksOptions, callback: AsyncCallback<HuksResult>) : void

abort终止密钥操作。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/72YF-yBhTSmTYHsIworgkQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014821Z&HW-CC-Expire=86400&HW-CC-Sign=B9B4017D85BB41B07A1FC1B27DB7660E570EA11157E35FEC366172FD06D3FE20)

从API version 8开始支持，从API version 9开始废弃，建议使用[huks.abortSession9+](#huksabortsession9)替代。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| handle | number | 是 | Abort操作的uint64类型的handle值。 |
| options | [HuksOptions](#huksoptions) | 是 | Abort操作的参数集合。 |
| callback | AsyncCallback<[HuksResult](#huksresultdeprecated)\> | 是 | 回调函数。当密钥操作abort成功时，err为undefined，data为获取到的HuksResult；否则为错误对象。 |

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';

/* huks.init、huks.update、huks.finish为三段式接口，需要一起使用，
 * 当这三个操作中的任一阶段发生错误时，都需要调用huks.abort来终止密钥的使用
 *
 * 以下以RSA2048密钥的callback操作使用为例
 */

let keyAlias = "HuksDemoRSA";
let properties: Array<huks.HuksParam> = [];
let options: huks.HuksOptions = {
  properties: properties,
  inData: new Uint8Array(0)
};
let handle: number = 0;
let resultMessage = "";

async function generateKey() {
  properties = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_RSA
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT
  }, {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_OAEP
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
  }];
  huks.generateKey(keyAlias, options);
}

function stringToUint8Array(str: string) {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  let tmpUint8Array = new Uint8Array(arr);
  return tmpUint8Array;
}

async function huksInit() {
  await huks.init(keyAlias, options).then((data) => {
    console.info(`test init data: ${JSON.stringify(data)}`);
    handle = data.handle;
  });
}

async function huksUpdate() {
  options.inData = stringToUint8Array("huksHmacTest");
  await huks.update(handle, options.inData, options).then((data) => {
    if (data.errorCode === 0) {
      resultMessage += "update success!";
    } else {
      resultMessage += "update fail!";
    }
  });
  console.info(resultMessage);
}

function huksFinish() {
  options.inData = stringToUint8Array("HuksDemoHMAC");
  huks.finish(handle, options).then((data) => {
    if (data.errorCode === 0) {
      resultMessage = "finish success!";
      console.info(resultMessage);
    } else {
      resultMessage = "finish fail errorCode: " + data.errorCode;
      console.error(resultMessage);
    }
  });
}

async function huksAbort() {
  new Promise<huks.HuksResult>((resolve, reject) => {
    huks.abort(handle, options, (err, data) => {
      console.info(`huksAbort data ${JSON.stringify(data)}`);
      console.error(`huksAbort err ${JSON.stringify(err)}`);
    });
  });
}
```

#### huks.abort(deprecated)

abort(handle: number, options: HuksOptions) : Promise<HuksResult>

abort终止密钥操作。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/sA5DWknvT-y6Sktm7QjA7Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014821Z&HW-CC-Expire=86400&HW-CC-Sign=BBD8BCFE8726FCF0A442D8F5533333EA3925A88383FDDE1F31003DD35903773F)

从API version 8开始支持，从API version 9开始废弃，建议使用[huks.abortSession9+](#huksabortsession9-1)替代。

**系统能力：** SystemCapability.Security.Huks.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| handle | number | 是 | Abort操作的uint64类型的handle值。 |
| options | [HuksOptions](#huksoptions) | 是 | Abort操作的参数集合。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<[HuksResult](#huksresultdeprecated)\> | Promise对象。返回HuksResult。 |

**示例：**

```ts
import { huks } from '@kit.UniversalKeystoreKit';

/* huks.init、huks.update、huks.finish为三段式接口，需要一起使用，
 * 当这三个操作中的任一阶段发生错误时，都需要调用huks.abort来终止密钥的使用
 *
 * 以下以RSA2048密钥的promise操作使用为例
 */
let keyAlias = "HuksDemoRSA";
let properties: Array<huks.HuksParam> = [];
let options: huks.HuksOptions = {
  properties: properties,
  inData: new Uint8Array(0)
};
let handle: number = 0;
let resultMessage = "";

function stringToUint8Array(str: string) {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  let tmpUint8Array = new Uint8Array(arr);
  return tmpUint8Array;
}

async function generateKey() {
  properties = [{
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_RSA
  }, {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
  }, {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT
  }, {
    tag: huks.HuksTag.HUKS_TAG_PADDING,
    value: huks.HuksKeyPadding.HUKS_PADDING_OAEP
  }, {
    tag: huks.HuksTag.HUKS_TAG_DIGEST,
    value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
  }];
  huks.generateKey(keyAlias, options, (err, data) => {
    if (data.errorCode === 0) {
      resultMessage = "generate success!";
    } else {
      resultMessage = "generate fail errorCode: " + data.errorCode;
    }
  });
}

async function huksInit() {
  return new Promise<huks.HuksHandle>((resolve, reject) => {
    huks.init(keyAlias, options, async (err, data) => {
      if (data.errorCode === 0) {
        resultMessage = "init success!";
        handle = data.handle;
      } else {
        resultMessage = "init fail errorCode: " + data.errorCode;
      }
    });
  });
}

async function huksUpdate() {
  options.inData = stringToUint8Array("huksHmacTest");
  new Promise<huks.HuksResult>((resolve, reject) => {
    huks.update(handle, options.inData, options, (err, data) => {
      if (data.errorCode === 0) {
        resultMessage += "update success!";
        console.info(resultMessage);
      } else {
        resultMessage += "update fail!";
        console.error(resultMessage);
      }
    });
  });
}

async function huksFinish() {
  options.inData = stringToUint8Array("0");
  new Promise<huks.HuksResult>((resolve, reject) => {
    huks.finish(handle, options, (err, data) => {
      if (data.errorCode === 0) {
        resultMessage = "finish success!";
      } else {
        resultMessage = "finish fail errorCode: " + data.errorCode;
      }
    });
  });
}

function huksAbort() {
  huks.abort(handle, options).then((data) => {
    if (data.errorCode === 0) {
      console.info("abort success!");
    } else {
      console.error("abort fail errorCode: " + data.errorCode);
    }
  });
}
```

#### HuksHandle(deprecated)

huks Handle结构体。

**系统能力：** SystemCapability.Security.Huks.Extension

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/S5tzQWmxSymMjyVfb9ntfA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014821Z&HW-CC-Expire=86400&HW-CC-Sign=0FF0392D3C780F9605F1B74F170069F322BF7E2BABBC2FB1EF7CE4BAF3B08B45)

从API version 9开始废弃，建议使用[HuksSessionHandle9+](#hukssessionhandle9)替代。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| errorCode | number | 否 | 否 | 表示错误码。 |
| handle | number | 否 | 否 | 表示无符号整数类型的handle值。 |
| token | Uint8Array | 否 | 是 | 表示[init](#huksinitdeprecated)操作之后获取到的challenge信息。默认为空。 |

#### HuksResult(deprecated)

调用接口返回的result。

**系统能力：** SystemCapability.Security.Huks.Extension

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/LWLu8LHIRsqgU2IrYLzWFA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014821Z&HW-CC-Expire=86400&HW-CC-Sign=FB50A9B8F5202AAEE9B4EC87E30E21BA3D663AC0497229FDAD324B9BA35CAA44)

-   从API version 8开始，从API version 9开始废弃，建议使用[HuksReturnResult9+](#huksreturnresult9)替代。
-   errorCode的具体信息，请参考[HUKS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-huks)。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| errorCode | number | 否 | 否 | 表示错误码。 |
| outData | Uint8Array | 否 | 是 | 表示输出数据。默认为空。 |
| properties | Array<[HuksParam](#huksparam)\> | 否 | 是 | 表示属性信息。默认为空。 |
| certChains | Array<string> | 否 | 是 | 表示证书链数据。默认为空。 |

#### HuksErrorCode(deprecated)

表示错误码的枚举。

**系统能力：** SystemCapability.Security.Huks.Extension

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/23zJp_LTTDC468Fsh0SLbQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014821Z&HW-CC-Expire=86400&HW-CC-Sign=D082D1FB846427C36ACBA6A038FE17BE6A731F847B6084FDE078CB1F294B8D4C)

从API version 9开始废弃，建议使用[HuksExceptionErrCode9+](#huksexceptionerrcode9)替代。

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| HUKS\_SUCCESS | 0 | 表示成功。 |
| HUKS\_FAILURE | \-1 | 表示失败。 |
| HUKS\_ERROR\_BAD\_STATE | \-2 | 表示错误的状态。 |
| HUKS\_ERROR\_INVALID\_ARGUMENT | \-3 | 表示无效的数据。 |
| HUKS\_ERROR\_NOT\_SUPPORTED | \-4 | 表示不支持。 |
| HUKS\_ERROR\_NO\_PERMISSION | \-5 | 表示没有许可。 |
| HUKS\_ERROR\_INSUFFICIENT\_DATA | \-6 | 表示数据不足。 |
| HUKS\_ERROR\_BUFFER\_TOO\_SMALL | \-7 | 表示缓冲区太小。 |
| HUKS\_ERROR\_INSUFFICIENT\_MEMORY | \-8 | 表示内存不足。 |
| HUKS\_ERROR\_COMMUNICATION\_FAILURE | \-9 | 表示通讯失败。 |
| HUKS\_ERROR\_STORAGE\_FAILURE | \-10 | 表示存储故障。 |
| HUKS\_ERROR\_HARDWARE\_FAILURE | \-11 | 表示硬件故障。 |
| HUKS\_ERROR\_ALREADY\_EXISTS | \-12 | 表示已经存在。 |
| HUKS\_ERROR\_NOT\_EXIST | \-13 | 表示不存在。 |
| HUKS\_ERROR\_NULL\_POINTER | \-14 | 表示空指针。 |
| HUKS\_ERROR\_FILE\_SIZE\_FAIL | \-15 | 表示文件大小失败。 |
| HUKS\_ERROR\_READ\_FILE\_FAIL | \-16 | 表示读取文件失败。 |
| HUKS\_ERROR\_INVALID\_PUBLIC\_KEY | \-17 | 表示无效的公钥。 |
| HUKS\_ERROR\_INVALID\_PRIVATE\_KEY | \-18 | 表示无效的私钥。 |
| HUKS\_ERROR\_INVALID\_KEY\_INFO | \-19 | 表示无效的密钥信息。 |
| HUKS\_ERROR\_HASH\_NOT\_EQUAL | \-20 | 表示哈希不相等。 |
| HUKS\_ERROR\_MALLOC\_FAIL | \-21 | 表示MALLOC 失败。 |
| HUKS\_ERROR\_WRITE\_FILE\_FAIL | \-22 | 表示写文件失败。 |
| HUKS\_ERROR\_REMOVE\_FILE\_FAIL | \-23 | 表示删除文件失败。 |
| HUKS\_ERROR\_OPEN\_FILE\_FAIL | \-24 | 表示打开文件失败。 |
| HUKS\_ERROR\_CLOSE\_FILE\_FAIL | \-25 | 表示关闭文件失败。 |
| HUKS\_ERROR\_MAKE\_DIR\_FAIL | \-26 | 表示创建目录失败。 |
| HUKS\_ERROR\_INVALID\_KEY\_FILE | \-27 | 表示无效的密钥文件。 |
| HUKS\_ERROR\_IPC\_MSG\_FAIL | \-28 | 表示IPC 信息失败。 |
| HUKS\_ERROR\_REQUEST\_OVERFLOWS | \-29 | 表示请求溢出。 |
| HUKS\_ERROR\_PARAM\_NOT\_EXIST | \-30 | 表示参数不存在。 |
| HUKS\_ERROR\_CRYPTO\_ENGINE\_ERROR | \-31 | 表示CRYPTO ENGINE错误。 |
| HUKS\_ERROR\_COMMUNICATION\_TIMEOUT | \-32 | 表示通讯超时。 |
| HUKS\_ERROR\_IPC\_INIT\_FAIL | \-33 | 表示IPC 初始化失败。 |
| HUKS\_ERROR\_IPC\_DLOPEN\_FAIL | \-34 | 表示IPC DLOPEN 失败。 |
| HUKS\_ERROR\_EFUSE\_READ\_FAIL | \-35 | 表示EFUSE 读取失败。 |
| HUKS\_ERROR\_NEW\_ROOT\_KEY\_MATERIAL\_EXIST | \-36 | 表示存在新的根密钥材料。 |
| HUKS\_ERROR\_UPDATE\_ROOT\_KEY\_MATERIAL\_FAIL | \-37 | 表示更新根密钥材料失败。 |
| HUKS\_ERROR\_VERIFICATION\_FAILED | \-38 | 表示验证证书链失败。 |
| HUKS\_ERROR\_CHECK\_GET\_ALG\_FAIL | \-100 | 表示检查获取 ALG 失败。 |
| HUKS\_ERROR\_CHECK\_GET\_KEY\_SIZE\_FAIL | \-101 | 表示检查获取密钥大小失败。 |
| HUKS\_ERROR\_CHECK\_GET\_PADDING\_FAIL | \-102 | 表示检查获取填充失败。 |
| HUKS\_ERROR\_CHECK\_GET\_PURPOSE\_FAIL | \-103 | 表示检查获取目的失败。 |
| HUKS\_ERROR\_CHECK\_GET\_DIGEST\_FAIL | \-104 | 表示检查获取摘要失败。 |
| HUKS\_ERROR\_CHECK\_GET\_MODE\_FAIL | \-105 | 表示检查获取模式失败。 |
| HUKS\_ERROR\_CHECK\_GET\_NONCE\_FAIL | \-106 | 表示检查获取随机数失败。 |
| HUKS\_ERROR\_CHECK\_GET\_AAD\_FAIL | \-107 | 表示检查获取 AAD 失败。 |
| HUKS\_ERROR\_CHECK\_GET\_IV\_FAIL | \-108 | 表示检查 GET IV 失败。 |
| HUKS\_ERROR\_CHECK\_GET\_AE\_TAG\_FAIL | \-109 | 表示检查获取 AE 标记失败。 |
| HUKS\_ERROR\_CHECK\_GET\_SALT\_FAIL | \-110 | 表示检查获取SALT失败。 |
| HUKS\_ERROR\_CHECK\_GET\_ITERATION\_FAIL | \-111 | 表示检查获取迭代失败。 |
| HUKS\_ERROR\_INVALID\_ALGORITHM | \-112 | 表示无效的算法。 |
| HUKS\_ERROR\_INVALID\_KEY\_SIZE | \-113 | 表示无效的密钥大小。 |
| HUKS\_ERROR\_INVALID\_PADDING | \-114 | 表示无效的填充。 |
| HUKS\_ERROR\_INVALID\_PURPOSE | \-115 | 表示无效的目的。 |
| HUKS\_ERROR\_INVALID\_MODE | \-116 | 表示无效模式。 |
| HUKS\_ERROR\_INVALID\_DIGEST | \-117 | 表示无效的摘要。 |
| HUKS\_ERROR\_INVALID\_SIGNATURE\_SIZE | \-118 | 表示签名大小无效。 |
| HUKS\_ERROR\_INVALID\_IV | \-119 | 表示无效的 IV。 |
| HUKS\_ERROR\_INVALID\_AAD | \-120 | 表示无效的 AAD。 |
| HUKS\_ERROR\_INVALID\_NONCE | \-121 | 表示无效的随机数。 |
| HUKS\_ERROR\_INVALID\_AE\_TAG | \-122 | 表示无效的 AE 标签。 |
| HUKS\_ERROR\_INVALID\_SALT | \-123 | 表示无效SALT。 |
| HUKS\_ERROR\_INVALID\_ITERATION | \-124 | 表示无效的迭代。 |
| HUKS\_ERROR\_INVALID\_OPERATION | \-125 | 表示无效操作。 |
| HUKS\_ERROR\_INTERNAL\_ERROR | \-999 | 表示内部错误。 |
| HUKS\_ERROR\_UNKNOWN\_ERROR | \-1000 | 表示未知错误。 |

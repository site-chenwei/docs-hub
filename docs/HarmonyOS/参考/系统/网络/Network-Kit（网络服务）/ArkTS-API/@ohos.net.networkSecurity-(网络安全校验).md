---
title: "@ohos.net.networkSecurity (网络安全校验)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-networksecurity"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Network Kit（网络服务）"
  - "ArkTS API"
  - "@ohos.net.networkSecurity (网络安全校验)"
captured_at: "2026-04-17T01:48:22.829Z"
---

# @ohos.net.networkSecurity (网络安全校验)

本模块提供网络安全校验能力。应用可以通过证书校验API完成证书校验功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/DrzhK9RJSeCkADtZanHVrQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=77EF8839398DECA9D26E124E3AC35E0ACD937F1D3B1E1EBC76C586FE8D73913B)

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import { networkSecurity } from '@kit.NetworkKit';
```

#### 完整示例

```ts
import { networkSecurity } from '@kit.NetworkKit';

// Define certificate blobs
const cert: networkSecurity.CertBlob = {
  type: networkSecurity.CertType.CERT_TYPE_PEM,
  data: '-----BEGIN CERTIFICATE-----\n... (certificate data) ...\n-----END CERTIFICATE-----',
};

const caCert: networkSecurity.CertBlob = {
  type: networkSecurity.CertType.CERT_TYPE_PEM,
  data: '-----BEGIN CERTIFICATE-----\n... (CA certificate data) ...\n-----END CERTIFICATE-----',
};

// Perform asynchronous certificate verification
networkSecurity.certVerification(cert, caCert)
  .then((result) => {
    console.info('Certificate verification result:', result);
  })
  .catch((error: BusinessError) => {
    console.error('Certificate verification failed:', error);
  });
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/fo_l-EZlQSue057chSyXXw/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=0703B3E1A4974AD280E073D336D384F94BE32F02ECA3952C12AE3545CEEE2E5E)

请务必将示例中的证书数据替换为实际的证书内容。

#### CertType

证书编码类型。

**系统能力**: SystemCapability.Communication.NetStack

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| CERT\_TYPE\_PEM | 0 | PEM格式证书。 |
| CERT\_TYPE\_DER | 1 | DER格式证书。 |

#### CertBlob

证书数据。

**系统能力**: SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| type | CertType | 否 | 否 | 证书编码类型。 |
| data | string | ArrayBuffer | 否 | 否 | 证书内容。 |

#### networkSecurity.certVerification

certVerification(cert: CertBlob, caCert?: CertBlob): Promise<number>

系统将使用证书管理中的预置CA证书和用户安装的CA证书来校验应用传入的证书。使用Promise异步回调。

**系统能力**: SystemCapability.Communication.NetStack

**参数**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| cert | CertBlob | 是 | 被校验的证书。 |
| caCert | CertBlob | 否 | 传入自定义的CA证书。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | 以promise形式返回一个数字，表示证书验证的结果。如果证书验证成功，则返回0； 否则验证失败。 |

**错误码：**

以下错误码的详细介绍请参见[网络安全校验错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-networksecurity)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2305001 | Unspecified error. |
| 2305002 | Unable to get issuer certificate. |
| 2305003 | Unable to get certificate revocation list (CRL). |
| 2305004 | Unable to decrypt certificate signature. |
| 2305005 | Unable to decrypt CRL signature. |
| 2305006 | Unable to decode issuer public key. |
| 2305007 | Certificate signature failure. |
| 2305008 | CRL signature failure. |
| 2305009 | Certificate is not yet valid. |
| 2305010 | Certificate has expired. |
| 2305011 | CRL is not yet valid. |
| 2305012 | CRL has expired. |
| 2305018 | Self-signed certificate. |
| 2305023 | Certificate has been revoked. |
| 2305024 | Invalid certificate authority (CA). |
| 2305027 | Certificate is untrusted. |
| 2305069 | Invalid certificate verification context. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/NYsgTLYHRr-SQFJiD2NHEQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=3658CD03DE1109D9ACB81C1A3D75BFE3CC5DD2AD6E22E9ACC23AE417D6A205F3)

这些错误代码对应于证书验证过程中的各种失败。

**示例：**

```ts
import { networkSecurity } from '@kit.NetworkKit';

// Define certificate blobs
const cert:networkSecurity.CertBlob = {
  type: networkSecurity.CertType.CERT_TYPE_PEM,
  data: '-----BEGIN CERTIFICATE-----\n... (certificate data) ...\n-----END CERTIFICATE-----',
};

const caCert:networkSecurity.CertBlob = {
  type: networkSecurity.CertType.CERT_TYPE_PEM,
  data: '-----BEGIN CERTIFICATE-----\n... (CA certificate data) ...\n-----END CERTIFICATE-----',
};

// Perform asynchronous certificate verification
networkSecurity.certVerification(cert, caCert)
  .then((result) => {
    console.info('Certificate verification result:', result);
  })
  .catch((error: BusinessError) => {
    console.error('Certificate verification failed:', error);
  });
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/Ddq_lycLStuVunT-0fusaA/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=A9B0485C966C7301F6D289117E29A63963828DFF1DEFCD6DE1A36E0DDE7DC168)

请务必将示例中的证书数据替换为实际的证书内容。

#### networkSecurity.certVerificationSync

certVerificationSync(cert: CertBlob, caCert?: CertBlob): number

系统将使用证书管理中的预置CA证书和用户安装的CA证书来校验应用传入的证书，使用同步方式返回。

**系统能力**：SystemCapability.Communication.NetStack

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| cert | CertBlob | 是 | 被校验的证书。 |
| caCert | CertBlob | 否 | 传入自定义的CA证书。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 表示证书验证的结果。如果证书验证成功，则返回0； 否则验证失败。 |

**错误码：**

以下错误码的详细介绍请参见[网络安全校验错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-networksecurity)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2305001 | Unspecified error. |
| 2305002 | Unable to get issuer certificate. |
| 2305003 | Unable to get certificate revocation list (CRL). |
| 2305004 | Unable to decrypt certificate signature. |
| 2305005 | Unable to decrypt CRL signature. |
| 2305006 | Unable to decode issuer public key. |
| 2305007 | Certificate signature failure. |
| 2305008 | CRL signature failure. |
| 2305009 | Certificate is not yet valid. |
| 2305010 | Certificate has expired. |
| 2305011 | CRL is not yet valid. |
| 2305012 | CRL has expired. |
| 2305018 | Self-signed certificate. |
| 2305023 | Certificate has been revoked. |
| 2305024 | Invalid certificate authority (CA). |
| 2305027 | Certificate is untrusted. |
| 2305069 | Invalid certificate verification context. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/OFq14-h_T9acls7tNSIRtw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=CFC676DF11289ABA9CFAEFD71374F56B4E3ED2E0B8261FCBA06D6F5D2FEAFF3E)

这些错误代码对应于证书验证过程中的各种失败。

**示例：**

```ts
import { networkSecurity } from '@kit.NetworkKit';

// Create certificate blobs
const cert: networkSecurity.CertBlob = {
  type: networkSecurity.CertType.CERT_TYPE_PEM,
  data: '-----BEGIN CERTIFICATE-----\n...'
};

const caCert: networkSecurity.CertBlob = {
  type: networkSecurity.CertType.CERT_TYPE_PEM,
  data: '-----BEGIN CERTIFICATE-----\n...'
};

// Asynchronous verification
networkSecurity.certVerification(cert, caCert)
  .then((result) => {
    console.info('Verification Result:', result);
  })
  .catch((error: BusinessError) => {
    console.error('Verification Error:', error);
  });

// Synchronous verification
let resultSync: number = networkSecurity.certVerificationSync(cert, caCert);
console.info('Synchronous Verification Result:', resultSync);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/wablHSASQC6HdGgveZSIkw/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=37D31134114EEF6BCEB7BDF459617DE19D059A8B32E3729C25AF65A812FA146A)

请务必将示例中的证书数据替换为实际的证书内容。

#### networkSecurity.isCleartextPermitted18+

isCleartextPermitted(): boolean

从应用预置network\_config.json文件中获取整体明文HTTP是否允许信息，默认允许明文HTTP访问。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 整体明文HTTP是否允许。返回true表示允许访问明文HTTP，false表示不允许。默认返回true。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |

**示例：**

```ts
import { networkSecurity } from '@kit.NetworkKit';

try {
  let result: boolean = networkSecurity.isCleartextPermitted();
  console.info(`isCleartextPermitted Result: ${JSON.stringify(result)}`);
} catch (error) {
  console.error(`isCleartextPermitted Error: ${JSON.stringify(error)}`);
}
```

#### networkSecurity.isCleartextPermittedByHostName18+

isCleartextPermittedByHostName(hostName: string): boolean

从应用预置network\_config.json文件中获取按域名明文HTTP是否允许信息，默认允许明文HTTP访问。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| hostName | string | 是 | 需要查询的主机名。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 按域名明文HTTP是否允许。返回true表示允许明文HTTP访问该主机，false表示不允许。默认返回true。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |

**示例：**

```ts
import { networkSecurity } from '@kit.NetworkKit';

try {
  let result: boolean = networkSecurity.isCleartextPermittedByHostName("xxx");
  console.info(`isCleartextPermitted Result: ${JSON.stringify(result)}`);
} catch (error) {
  console.error(`isCleartextPermitted Error: ${JSON.stringify(error)}`);
}
```

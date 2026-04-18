---
title: "FIDO2_PublicKeyCredentialParameters"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___public_key_credential_parameters"
menu_path:
  - "参考"
  - "系统"
  - "安全"
  - "Online Authentication Kit（在线认证服务）"
  - "C API"
  - "结构体"
  - "FIDO2_PublicKeyCredentialParameters"
captured_at: "2026-04-17T01:48:19.889Z"
---

# FIDO2\_PublicKeyCredentialParameters

#### 概述

认证凭据的附加参数。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [FIDO2\_PublicKeyCredentialType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey#fido2_publickeycredentialtype-1) [type](#type) | PublicKey凭证类型。 |
| [FIDO2\_Algorithm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey#fido2_algorithm-1) [alg](#alg) | 算法。 |

#### 结构体成员变量说明

#### \[h2\]alg

```cpp
FIDO2_Algorithm FIDO2_PublicKeyCredentialParameters::alg
```

**描述**

算法。

#### \[h2\]type

```cpp
FIDO2_PublicKeyCredentialType FIDO2_PublicKeyCredentialParameters::type
```

**描述**

PublicKey凭证类型。

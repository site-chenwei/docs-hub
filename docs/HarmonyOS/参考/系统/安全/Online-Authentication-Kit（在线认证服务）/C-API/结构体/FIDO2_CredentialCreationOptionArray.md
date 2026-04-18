---
title: "FIDO2_CredentialCreationOptionArray"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___credential_creation_option_array"
menu_path:
  - "参考"
  - "系统"
  - "安全"
  - "Online Authentication Kit（在线认证服务）"
  - "C API"
  - "结构体"
  - "FIDO2_CredentialCreationOptionArray"
captured_at: "2026-04-17T01:48:19.770Z"
---

# FIDO2\_CredentialCreationOptionArray

#### 概述

认证凭据的附加参数数组。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t [pubKeyCredParamNum](#pubkeycredparamnum) | PubKeyCredParam参数数目。 |
| [FIDO2\_PublicKeyCredentialParameters](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___public_key_credential_parameters) \* [pubKeyCredParams](#pubkeycredparams) | 认证凭据的附加参数。 |

#### 结构体成员变量说明

#### \[h2\]pubKeyCredParamNum

```cpp
uint32_t FIDO2_CredentialCreationOptionArray::pubKeyCredParamNum
```

**描述**

PubKeyCredParam参数数目。

#### \[h2\]pubKeyCredParams

```cpp
FIDO2_PublicKeyCredentialParameters* FIDO2_CredentialCreationOptionArray::pubKeyCredParams
```

**描述**

认证凭据的附加参数。

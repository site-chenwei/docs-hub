---
title: "FIDO2_CredentialCreationOptions"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___credential_creation_options"
menu_path:
  - "参考"
  - "系统"
  - "安全"
  - "Online Authentication Kit（在线认证服务）"
  - "C API"
  - "结构体"
  - "FIDO2_CredentialCreationOptions"
captured_at: "2026-04-17T01:48:19.772Z"
---

# FIDO2\_CredentialCreationOptions

#### 概述

凭据请求的选项。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [FIDO2\_CredentialMediationRequirement](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey#fido2_credentialmediationrequirement-1) [mediation](#mediation) | 该操作是否需要用户参与。 |
| [FIDO2\_PublicKeyCredentialCreationOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___public_key_credential_creation_options) [publicKey](#publickey) | publicKey凭证请求的选项。 |

#### 结构体成员变量说明

#### \[h2\]mediation

```cpp
FIDO2_CredentialMediationRequirement FIDO2_CredentialCreationOptions::mediation
```

**描述**

操作是否需要用户参与。

#### \[h2\]publicKey

```cpp
FIDO2_PublicKeyCredentialCreationOptions FIDO2_CredentialCreationOptions::publicKey
```

**描述**

publicKey凭证请求的选项。

---
title: "FIDO2_PublicKeyCredentialDescriptor"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___public_key_credential_descriptor"
menu_path:
  - "参考"
  - "系统"
  - "安全"
  - "Online Authentication Kit（在线认证服务）"
  - "C API"
  - "结构体"
  - "FIDO2_PublicKeyCredentialDescriptor"
captured_at: "2026-04-17T01:48:19.809Z"
---

# FIDO2\_PublicKeyCredentialDescriptor

#### 概述

用于注册或认证凭据的参数。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [FIDO2\_PublicKeyCredentialType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey#fido2_publickeycredentialtype-1) [type](#type) | 凭证类型。 |
| [Uint8Buff](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_uint8_buff) [id](#id) | 凭据标识符。 |
| [FIDO2\_AuthenticatorTransportArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___authenticator_transport_array) [transports](#transports) | 定义身份认证器访问类型（USB、NFC、蓝牙）。 |

#### 结构体成员变量说明

#### \[h2\]id

```cpp
Uint8Buff FIDO2_PublicKeyCredentialDescriptor::id
```

**描述**

凭据标识符。

#### \[h2\]transports

```cpp
FIDO2_AuthenticatorTransportArray FIDO2_PublicKeyCredentialDescriptor::transports
```

**描述**

定义身份认证器访问类型（USB、NFC、蓝牙）。

#### \[h2\]type

```cpp
FIDO2_PublicKeyCredentialType FIDO2_PublicKeyCredentialDescriptor::type
```

**描述**

凭证类型。

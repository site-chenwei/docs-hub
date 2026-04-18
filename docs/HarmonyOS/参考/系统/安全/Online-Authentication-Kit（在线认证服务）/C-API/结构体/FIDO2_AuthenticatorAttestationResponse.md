---
title: "FIDO2_AuthenticatorAttestationResponse"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___authenticator_attestation_response"
menu_path:
  - "参考"
  - "系统"
  - "安全"
  - "Online Authentication Kit（在线认证服务）"
  - "C API"
  - "结构体"
  - "FIDO2_AuthenticatorAttestationResponse"
captured_at: "2026-04-17T01:48:19.698Z"
---

# FIDO2\_AuthenticatorAttestationResponse

#### 概述

认证器声明响应。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [Uint8Buff](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_uint8_buff) [attestationObject](#attestationobject) | 声明对象。 |
| [Uint8Buff](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_uint8_buff) [clientDataJson](#clientdatajson) | 获取客户端数据，表示WebAuthn依赖方和客户端的上下文绑定，包含类型、挑战值及源等数据。 |
| [Uint8Buff](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_uint8_buff) [publicKey](#publickey) | publicKey凭证请求的选项，字节流。 |
| [Uint8Buff](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_uint8_buff) [authenticatorData](#authenticatordata) | 认证器数据，字节流。 |
| [FIDO2\_Algorithm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey#fido2_algorithm-1) [publicKeyAlgorithm](#publickeyalgorithm) | 密码算法。 |
| [FIDO2\_AuthenticatorTransportArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___authenticator_transport_array) [transports](#transports) | 定义身份认证器访问类型（USB、NFC、蓝牙）。 |

#### 结构体成员变量说明

#### \[h2\]attestationObject

```cpp
Uint8Buff FIDO2_AuthenticatorAttestationResponse::attestationObject
```

**描述**

声明对象。

#### \[h2\]authenticatorData

```cpp
Uint8Buff FIDO2_AuthenticatorAttestationResponse::authenticatorData
```

**描述**

认证器数据，字节流。

#### \[h2\]clientDataJson

```cpp
Uint8Buff FIDO2_AuthenticatorAttestationResponse::clientDataJson
```

**描述**

获取客户端数据，表示WebAuthn依赖方和客户端的上下文绑定，包含类型、挑战值及源等数据。

#### \[h2\]publicKey

```cpp
Uint8Buff FIDO2_AuthenticatorAttestationResponse::publicKey
```

**描述**

publicKey凭证请求的选项，字节流。

#### \[h2\]publicKeyAlgorithm

```cpp
FIDO2_Algorithm FIDO2_AuthenticatorAttestationResponse::publicKeyAlgorithm
```

**描述**

密码算法。

#### \[h2\]transports

```cpp
FIDO2_AuthenticatorTransportArray FIDO2_AuthenticatorAttestationResponse::transports
```

**描述**

定义身份认证器访问类型（USB、NFC、蓝牙）。

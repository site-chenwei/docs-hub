---
title: "FIDO2_AuthenticatorResponse"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___authenticator_response"
menu_path:
  - "参考"
  - "系统"
  - "安全"
  - "Online Authentication Kit（在线认证服务）"
  - "C API"
  - "结构体"
  - "FIDO2_AuthenticatorResponse"
captured_at: "2026-04-17T01:48:19.673Z"
---

# FIDO2\_AuthenticatorResponse

#### 概述

定义获取认证器断言响应的结构体。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [Uint8Buff](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_uint8_buff) [authenticatorData](#authenticatordata) | 身份认证器数据。 |
| [Uint8Buff](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_uint8_buff) [signature](#signature) | 签名。 |
| [Uint8Buff](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_uint8_buff) [userHandle](#userhandle) | 用户句柄（用户ID）。可选。 |
| [Uint8Buff](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_uint8_buff) [clientDataJson](#clientdatajson) | 获取客户端数据，表示WebAuthn依赖方和客户端的上下文绑定，包含类型、挑战值及源等数据。 |

#### 结构体成员变量说明

#### \[h2\]authenticatorData

```cpp
Uint8Buff FIDO2_AuthenticatorResponse::authenticatorData
```

**描述**

身份认证器数据。

#### \[h2\]clientDataJson

```cpp
Uint8Buff FIDO2_AuthenticatorResponse::clientDataJson
```

**描述**

获取客户端数据，表示WebAuthn依赖方和客户端的上下文绑定，包含类型、挑战值及源等数据。

#### \[h2\]signature

```cpp
Uint8Buff FIDO2_AuthenticatorResponse::signature
```

**描述**

签名。

#### \[h2\]userHandle

```cpp
Uint8Buff FIDO2_AuthenticatorResponse::userHandle
```

**描述**

用户句柄。可选。

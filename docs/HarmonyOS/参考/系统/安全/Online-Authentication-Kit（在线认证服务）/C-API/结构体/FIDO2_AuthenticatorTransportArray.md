---
title: "FIDO2_AuthenticatorTransportArray"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___authenticator_transport_array"
menu_path:
  - "参考"
  - "系统"
  - "安全"
  - "Online Authentication Kit（在线认证服务）"
  - "C API"
  - "结构体"
  - "FIDO2_AuthenticatorTransportArray"
captured_at: "2026-04-17T01:48:19.700Z"
---

# FIDO2\_AuthenticatorTransportArray

#### 概述

认证器传输方式数组。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t [transportNum](#transportnum) | 传输方式数量。 |
| [FIDO2\_AuthenticatorTransport](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey#fido2_authenticatortransport-1) \* [transports](#transports) | 定义身份认证器访问类型（USB、NFC、蓝牙）。 |

#### 结构体成员变量说明

#### \[h2\]transportNum

```cpp
uint32_t FIDO2_AuthenticatorTransportArray::transportNum
```

**描述**

传输方式数量。

#### \[h2\]transports

```cpp
FIDO2_AuthenticatorTransport* FIDO2_AuthenticatorTransportArray::transports
```

**描述**

定义身份认证器访问类型（USB、NFC、蓝牙）。

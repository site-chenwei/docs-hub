---
title: "FIDO2_AuthenticatorMetadata"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___authenticator_metadata"
menu_path:
  - "参考"
  - "系统"
  - "安全"
  - "Online Authentication Kit（在线认证服务）"
  - "C API"
  - "结构体"
  - "FIDO2_AuthenticatorMetadata"
captured_at: "2026-04-17T01:48:19.661Z"
---

# FIDO2\_AuthenticatorMetadata

#### 概述

认证器元数据。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [Uint8Buff](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_uint8_buff) [aaguid](#aaguid) | 认证器的aaguid。 |
| [FIDO2\_Uvm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey#fido2_uvm-1) [uvm](#uvm) | 支持的认证器类型。 |
| bool [isAvailable](#isavailable) | 认证器是否可用。 |

#### 结构体成员变量说明

#### \[h2\]aaguid

```cpp
Uint8Buff FIDO2_AuthenticatorMetadata::aaguid
```

**描述**

认证器的aaguid。

#### \[h2\]isAvailable

```cpp
bool FIDO2_AuthenticatorMetadata::isAvailable
```

**描述**

认证器是否可用。如果返回true，则表示认证器可用；返回false，表示认证器不可用。

#### \[h2\]uvm

```cpp
FIDO2_Uvm FIDO2_AuthenticatorMetadata::uvm
```

**描述**

支持的认证器类型。

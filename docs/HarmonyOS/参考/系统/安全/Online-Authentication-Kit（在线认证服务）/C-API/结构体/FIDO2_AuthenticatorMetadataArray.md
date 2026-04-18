---
title: "FIDO2_AuthenticatorMetadataArray"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___authenticator_metadata_array"
menu_path:
  - "参考"
  - "系统"
  - "安全"
  - "Online Authentication Kit（在线认证服务）"
  - "C API"
  - "结构体"
  - "FIDO2_AuthenticatorMetadataArray"
captured_at: "2026-04-17T01:48:19.666Z"
---

# FIDO2\_AuthenticatorMetadataArray

#### 概述

描述支持的认证器数组。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t [number](#number) | 认证器数目。 |
| [FIDO2\_AuthenticatorMetadata](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___authenticator_metadata) \* [authenticators](#authenticators) | 认证器支持的扩展。 |

#### 结构体成员变量说明

#### \[h2\]authenticators

```cpp
FIDO2_AuthenticatorMetadata* FIDO2_AuthenticatorMetadataArray::authenticators
```

**描述**

认证器支持的扩展。

#### \[h2\]number

```cpp
uint32_t FIDO2_AuthenticatorMetadataArray::number
```

**描述**

认证器数目。

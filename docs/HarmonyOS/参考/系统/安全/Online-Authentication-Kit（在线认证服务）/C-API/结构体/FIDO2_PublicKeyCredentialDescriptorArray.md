---
title: "FIDO2_PublicKeyCredentialDescriptorArray"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___public_key_credential_descriptor_array"
menu_path:
  - "参考"
  - "系统"
  - "安全"
  - "Online Authentication Kit（在线认证服务）"
  - "C API"
  - "结构体"
  - "FIDO2_PublicKeyCredentialDescriptorArray"
captured_at: "2026-04-17T01:48:19.847Z"
---

# FIDO2\_PublicKeyCredentialDescriptorArray

#### 概述

PublicKey凭证描述符数组。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t [allowCredentiallNum](#allowcredentiallnum) | 允许凭证数目。 |
| [FIDO2\_PublicKeyCredentialDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___public_key_credential_descriptor) \* [allowCredentials](#allowcredentials) | 认证凭据的附加参数列表。默认值为\[\]。 |

#### 结构体成员变量说明

#### \[h2\]allowCredentiallNum

```cpp
uint32_t FIDO2_PublicKeyCredentialDescriptorArray::allowCredentiallNum
```

**描述**

允许凭证数目。

#### \[h2\]allowCredentials

```cpp
FIDO2_PublicKeyCredentialDescriptor* FIDO2_PublicKeyCredentialDescriptorArray::allowCredentials
```

**描述**

认证凭据的附加参数列表。默认值为\[\]。

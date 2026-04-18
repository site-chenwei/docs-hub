---
title: "FIDO2_PublicKeyCredentialHintArray"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___public_key_credential_hint_array"
menu_path:
  - "参考"
  - "系统"
  - "安全"
  - "Online Authentication Kit（在线认证服务）"
  - "C API"
  - "结构体"
  - "FIDO2_PublicKeyCredentialHintArray"
captured_at: "2026-04-17T01:48:19.899Z"
---

# FIDO2\_PublicKeyCredentialHintArray

#### 概述

认证方式指示数组。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t [hintNum](#hintnum) | 认证方式指示数目。 |
| [FIDO2\_PublicKeyCredentialHint](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey#fido2_publickeycredentialhint-1) \* [hints](#hints) | 认证方式指示列表。 |

#### 结构体成员变量说明

#### \[h2\]hintNum

```cpp
uint32_t FIDO2_PublicKeyCredentialHintArray::hintNum
```

**描述**

认证方式指示数目。

#### \[h2\]hints

```cpp
FIDO2_PublicKeyCredentialHint* FIDO2_PublicKeyCredentialHintArray::hints
```

**描述**

认证方式指示列表。

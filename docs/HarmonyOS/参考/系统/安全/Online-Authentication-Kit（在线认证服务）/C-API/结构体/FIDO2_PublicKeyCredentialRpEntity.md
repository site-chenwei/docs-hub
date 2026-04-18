---
title: "FIDO2_PublicKeyCredentialRpEntity"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___public_key_credential_rp_entity"
menu_path:
  - "参考"
  - "系统"
  - "安全"
  - "Online Authentication Kit（在线认证服务）"
  - "C API"
  - "结构体"
  - "FIDO2_PublicKeyCredentialRpEntity"
captured_at: "2026-04-17T01:48:19.901Z"
---

# FIDO2\_PublicKeyCredentialRpEntity

#### 概述

创建新凭据时依赖方的属性。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| char \* [id](#id) | 依赖方标识符。 |
| char \* [name](#name) | 依赖方名称。 |

#### 结构体成员变量说明

#### \[h2\]id

```cpp
char* FIDO2_PublicKeyCredentialRpEntity::id
```

**描述**

依赖方标识符。

#### \[h2\]name

```cpp
char* FIDO2_PublicKeyCredentialRpEntity::name
```

**描述**

依赖方名称。

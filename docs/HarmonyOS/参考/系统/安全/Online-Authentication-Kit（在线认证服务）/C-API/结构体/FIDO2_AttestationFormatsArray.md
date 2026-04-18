---
title: "FIDO2_AttestationFormatsArray"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___attestation_formats_array"
menu_path:
  - "参考"
  - "系统"
  - "安全"
  - "Online Authentication Kit（在线认证服务）"
  - "C API"
  - "结构体"
  - "FIDO2_AttestationFormatsArray"
captured_at: "2026-04-17T01:48:19.632Z"
---

# FIDO2\_AttestationFormatsArray

#### 概述

依赖方的数组可以使用此成员指定一个关于认证方使用的证明语句格式的首选项。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t [attestationFormatsNum](#attestationformatsnum) | PubKeyCredParam个数。 |
| char \*\* [attestationFormats](#attestationformats) | 认证凭据的附加参数列表。 |

#### 结构体成员变量说明

#### \[h2\]attestationFormats

```cpp
char** FIDO2_AttestationFormatsArray::attestationFormats
```

**描述**

认证凭据的附加参数列表。

#### \[h2\]attestationFormatsNum

```cpp
uint32_t FIDO2_AttestationFormatsArray::attestationFormatsNum
```

**描述**

认证凭据的附加参数列表长度。

---
title: "FIDO2_Capability"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___capability"
menu_path:
  - "参考"
  - "系统"
  - "安全"
  - "Online Authentication Kit（在线认证服务）"
  - "C API"
  - "结构体"
  - "FIDO2_Capability"
captured_at: "2026-04-17T01:48:19.709Z"
---

# FIDO2\_Capability

#### 概述

通行密钥能力的结构体。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [FIDO2\_ClientCapability](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey#fido2_clientcapability-1) [capability](#capability) | 通行密钥的能力。 |
| bool [isSupported](#issupported) | 是否支持。如果为true表示支持，false表示不支持。 |

#### 结构体成员变量说明

#### \[h2\]capability

```cpp
FIDO2_ClientCapability FIDO2_Capability::capability
```

**描述**

通行密钥的能力。

#### \[h2\]isSupported

```cpp
bool FIDO2_Capability::isSupported
```

**描述**

是否支持。如果为true表示支持，false表示不支持。

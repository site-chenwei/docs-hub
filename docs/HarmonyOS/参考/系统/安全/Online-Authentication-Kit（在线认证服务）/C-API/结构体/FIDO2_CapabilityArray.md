---
title: "FIDO2_CapabilityArray"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___capability_array"
menu_path:
  - "参考"
  - "系统"
  - "安全"
  - "Online Authentication Kit（在线认证服务）"
  - "C API"
  - "结构体"
  - "FIDO2_CapabilityArray"
captured_at: "2026-04-17T01:48:19.749Z"
---

# FIDO2\_CapabilityArray

#### 概述

描述能力数组。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t [number](#number) | 能力的数量。 |
| [FIDO2\_Capability](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___capability) \* [capability](#capability) | 能力的数组。 |

#### 结构体成员变量说明

#### \[h2\]capability

```cpp
FIDO2_Capability* FIDO2_CapabilityArray::capability
```

**描述**

能力数组。

#### \[h2\]number

```cpp
uint32_t FIDO2_CapabilityArray::number
```

**描述**

能力数组长度。

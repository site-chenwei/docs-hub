---
title: "FIDO2_TokenBinding"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_i_d_o2___token_binding"
menu_path:
  - "参考"
  - "系统"
  - "安全"
  - "Online Authentication Kit（在线认证服务）"
  - "C API"
  - "结构体"
  - "FIDO2_TokenBinding"
captured_at: "2026-04-17T01:48:19.911Z"
---

# FIDO2\_TokenBinding

#### 概述

Token binding协议，用于客户端与依赖方通信。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [FIDO2\_TokenBindingStatus](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey#fido2_tokenbindingstatus-1) [status](#status) | 客户端的绑定状态。 |
| char \* [id](#id) | 令牌绑定标识符。 |

#### 结构体成员变量说明

#### \[h2\]id

```cpp
char* FIDO2_TokenBinding::id
```

**描述**

令牌绑定标识符。

#### \[h2\]status

```cpp
FIDO2_TokenBindingStatus FIDO2_TokenBinding::status
```

**描述**

客户端的绑定状态。

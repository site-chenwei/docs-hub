---
title: "AuthenticationExtensionsClientOutputs"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_authentication_extensions_client_outputs"
menu_path:
  - "参考"
  - "系统"
  - "安全"
  - "Online Authentication Kit（在线认证服务）"
  - "C API"
  - "结构体"
  - "AuthenticationExtensionsClientOutputs"
captured_at: "2026-04-17T01:48:19.598Z"
---

# AuthenticationExtensionsClientOutputs

#### 概述

身份认证扩展输出。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| char \* [placeholder](#placeholder) | 占位符，表示返回的JSON消息中包含key clientExtensionResults。默认返回NULL。 |

#### 结构体成员变量说明

#### \[h2\]placeholder

```cpp
char* AuthenticationExtensionsClientOutputs::placeholder
```

**描述**

占位符，表示返回的JSON消息中包含"clientExtensionResults"这个key值。该值始终返回NULL。

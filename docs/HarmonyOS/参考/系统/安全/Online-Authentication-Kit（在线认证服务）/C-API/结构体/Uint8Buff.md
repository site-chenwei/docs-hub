---
title: "Uint8Buff"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_uint8_buff"
menu_path:
  - "参考"
  - "系统"
  - "安全"
  - "Online Authentication Kit（在线认证服务）"
  - "C API"
  - "结构体"
  - "Uint8Buff"
captured_at: "2026-04-17T01:48:19.912Z"
---

# Uint8Buff

#### 概述

定义uint8\_t字节流。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t [length](#length) | 字节流的长度。 |
| uint8\_t \* [val](#val) | 字节流的值。 |

#### 结构体成员变量说明

#### \[h2\]length

```cpp
uint32_t Uint8Buff::length
```

**描述**

字节流的长度。

#### \[h2\]val

```cpp
uint8_t* Uint8Buff::val
```

**描述**

字节流的值。

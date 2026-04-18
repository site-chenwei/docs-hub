---
title: "Rcp_CookieAttributeEntry"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___cookie_attribute_entry"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Remote Communication Kit（远场通信服务）"
  - "C API"
  - "结构体"
  - "Rcp_CookieAttributeEntry"
captured_at: "2026-04-17T01:48:26.106Z"
---

# Rcp\_CookieAttributeEntry

#### 概述

响应Cookie属性条目。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| const char \* [key](#key) | 键。 |
| const char \* [value](#value) | 值。 |
| struct [Rcp\_CookieAttributeEntry](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___cookie_attribute_entry) \* [next](#next) | 链式存储。指向下一个[Rcp\_CookieAttributeEntry](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___cookie_attribute_entry)的指针。 |

#### 结构体成员变量说明

#### \[h2\]key

```cpp
const char* Rcp_CookieAttributeEntry::key
```

**描述**

键。

#### \[h2\]next

```cpp
struct Rcp_CookieAttributeEntry* Rcp_CookieAttributeEntry::next
```

**描述**

链式存储。指向下一个[Rcp\_CookieAttributeEntry](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___cookie_attribute_entry)的指针。

#### \[h2\]value

```cpp
const char* Rcp_CookieAttributeEntry::value
```

**描述**

值。

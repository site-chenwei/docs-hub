---
title: "Rcp_ResponseCookies"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response_cookies"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Remote Communication Kit（远场通信服务）"
  - "C API"
  - "结构体"
  - "Rcp_ResponseCookies"
captured_at: "2026-04-17T01:48:26.628Z"
---

# Rcp\_ResponseCookies

#### 概述

响应Cookie。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| char \* [name](#name) | 响应Cookie名称。 |
| char \* [value](#value) | 响应Cookie值。 |
| char \* [domain](#domain) | 响应Cookie域属性。 |
| char \* [path](#path) | 响应Cookie路径属性。 |
| char \* [expires](#expires) | 响应Cookie过期属性。 |
| uint64\_t [maxAge](#maxage) | 响应Cookie maxAge属性。 |
| bool [secure](#secure) | 响应Cookie安全属性。 |
| bool [httpOnly](#httponly) | 响应Cookie httpOnly属性。 |
| char \* [sameSite](#samesite) | 响应Cookie sameSite属性。 |
| uint64\_t [rawSize](#rawsize) | 此响应Cookie的原始大小。 |
| char \* [originString](#originstring) | 原始字符串。 |
| [Rcp\_CookieAttributes](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#rcp_cookieattributes) \* [cookieAttributes](#cookieattributes) | 响应Cookie中的所有属性。 |
| struct [Rcp\_ResponseCookies](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response_cookies) \* [next](#next) | 链式存储。指向下一个[Rcp\_ResponseCookies](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response_cookies)的指针。 |

#### 结构体成员变量说明

#### \[h2\]cookieAttributes

```cpp
Rcp_CookieAttributes* Rcp_ResponseCookies::cookieAttributes
```

**描述**

响应Cookie中的所有属性。

#### \[h2\]domain

```cpp
char* Rcp_ResponseCookies::domain
```

**描述**

响应Cookie域属性。

#### \[h2\]expires

```cpp
char* Rcp_ResponseCookies::expires
```

**描述**

响应Cookie过期属性。

#### \[h2\]httpOnly

```cpp
bool Rcp_ResponseCookies::httpOnly
```

**描述**

响应Cookie httpOnly属性。

#### \[h2\]maxAge

```cpp
uint64_t Rcp_ResponseCookies::maxAge
```

**描述**

响应Cookie maxAge属性。

#### \[h2\]name

```cpp
char* Rcp_ResponseCookies::name
```

**描述**

响应Cookie名称。

#### \[h2\]next

```cpp
struct Rcp_ResponseCookies* Rcp_ResponseCookies::next
```

**描述**

链式存储。指向下一个[Rcp\_ResponseCookies](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response_cookies)的指针。

#### \[h2\]originString

```cpp
char* Rcp_ResponseCookies::originString
```

**描述**

原始字符串。

#### \[h2\]path

```cpp
char* Rcp_ResponseCookies::path
```

**描述**

响应Cookie路径属性。

#### \[h2\]rawSize

```cpp
uint64_t Rcp_ResponseCookies::rawSize
```

**描述**

此响应Cookie的原始大小。

#### \[h2\]sameSite

```cpp
char* Rcp_ResponseCookies::sameSite
```

**描述**

响应Cookie sameSite属性。

#### \[h2\]secure

```cpp
bool Rcp_ResponseCookies::secure
```

**描述**

响应Cookie安全属性。

#### \[h2\]value

```cpp
char* Rcp_ResponseCookies::value
```

**描述**

响应Cookie值。

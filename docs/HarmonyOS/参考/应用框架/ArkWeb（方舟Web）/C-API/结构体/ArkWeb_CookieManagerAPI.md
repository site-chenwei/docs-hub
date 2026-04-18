---
title: "ArkWeb_CookieManagerAPI"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-cookiemanagerapi"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkWeb（方舟Web）"
  - "C API"
  - "结构体"
  - "ArkWeb_CookieManagerAPI"
captured_at: "2026-04-17T01:48:13.272Z"
---

# ArkWeb\_CookieManagerAPI

```c
typedef struct {...} ArkWeb_CookieManagerAPI
```

#### 概述

定义了ArkWeb的CookieManager接口。在调用接口之前，建议使用[ARKWEB\_MEMBER\_MISSING](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-type-h#宏定义)检查函数结构体是否有对应的函数指针，避免SDK与设备ROM不匹配导致崩溃。CookieManager相关接口需在UI线程中调用OH\_ArkWeb\_GetNativeAPI方法获取。

**起始版本：** 12

**相关模块：** [Web](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web)

**所在头文件：** [arkweb\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| size\_t size | 结构体的大小。 |

#### \[h2\]成员函数

| 名称 | 描述 |
| :-- | :-- |
| [ArkWeb\_ErrorCode (\*fetchCookieSync)(const char\* url, bool incognito, bool includeHttpOnly, char\*\* cookieValue)](#fetchcookiesync) | 获取指定URL对应的cookie值。 |
| [ArkWeb\_ErrorCode (\*configCookieSync)(const char\* url,const char\* cookieValue, bool incognito, bool includeHttpOnly)](#configcookiesync) | 设置指定URL的cookie值。 |
| [bool (\*existCookies)(bool incognito)](#existcookies) | 检查Cookie是否存在。 |
| [void (\*clearAllCookiesSync)(bool incognito)](#clearallcookiessync) | 清除所有cookies。 |
| [void (\*clearSessionCookiesSync)()](#clearsessioncookiessync) | 清除所有会话Cookies。 |

#### 成员函数说明

#### \[h2\]fetchCookieSync()

```c
ArkWeb_ErrorCode (*fetchCookieSync)(const char* url, bool incognito, bool includeHttpOnly, char** cookieValue)
```

**描述：**

获取指定URL对应的cookie值。

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const char\* url | 要获取的cookie所属的URL，建议使用完整的URL。 |
| bool incognito | true表示获取隐私模式下webview的内存cookie, false表示获取非隐私模式下的cookie。 |
| bool includeHttpOnly | 如果为true，则标记为HTTP-Only属性的cookie也将包含在cookieValue中。 |
| char\*\* cookieValue | 获取与URL对应的cookie值。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [ArkWeb\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-error-code-h#arkweb_errorcode) | 
返回值错误码。

[ARKWEB\_SUCCESS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-error-code-h#arkweb_errorcode) 获取cookie成功。

[ARKWEB\_INVALID\_URL](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-error-code-h#arkweb_errorcode) 设置的URL无效。

[ARKWEB\_INVALID\_PARAM](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-error-code-h#arkweb_errorcode) cookieValue参数无效。

 |

#### \[h2\]configCookieSync()

```c
ArkWeb_ErrorCode (*configCookieSync)(const char* url,const char* cookieValue, bool incognito, bool includeHttpOnly)
```

**描述：**

设置指定URL的cookie值。

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const char\* url | 指定cookie所属的URL，建议填写完整的URL。 |
| const char\* cookieValue | 要设置的cookie的值。 |
| bool incognito | true表示在隐私模式下设置对应URL的Cookie，false表示以非隐私模式设置对应URL的cookie。 |
| bool includeHttpOnly | 如果为true，则标记为HTTP-Only的cookie也可以被覆盖。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [ArkWeb\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-error-code-h#arkweb_errorcode) | 
返回值错误码。

[ARKWEB\_SUCCESS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-error-code-h#arkweb_errorcode) 获取cookie成功。

[ARKWEB\_INVALID\_URL](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-error-code-h#arkweb_errorcode) 设置的URL无效。

[ARKWEB\_INVALID\_COOKIE\_VALUE](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-error-code-h#arkweb_errorcode) cookieValue参数无效。

 |

#### \[h2\]existCookies()

```c
bool (*existCookies)(bool incognito)
```

**描述：**

检查Cookie是否存在。

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| bool incognito | true表示隐私模式下是否存在cookie，false表示非隐私模式下是否存在cookie。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| bool | true表示cookie存在，false表示cookie不存在。 |

#### \[h2\]clearAllCookiesSync()

```c
void (*clearAllCookiesSync)(bool incognito)
```

**描述：**

清除所有cookies。

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| bool incognito | true表示清除隐私模式下的所有cookies，false表示清除非隐私模式下的所有cookies。 |

#### \[h2\]clearSessionCookiesSync()

```c
void (*clearSessionCookiesSync)()
```

**描述：**

清除所有会话Cookies。

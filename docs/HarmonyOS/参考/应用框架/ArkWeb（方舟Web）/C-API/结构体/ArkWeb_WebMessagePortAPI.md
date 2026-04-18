---
title: "ArkWeb_WebMessagePortAPI"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-webmessageportapi"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkWeb（方舟Web）"
  - "C API"
  - "结构体"
  - "ArkWeb_WebMessagePortAPI"
captured_at: "2026-04-17T01:48:13.269Z"
---

# ArkWeb\_WebMessagePortAPI

```c
typedef struct {...} ArkWeb_WebMessagePortAPI
```

#### 概述

Post Message相关的Native API结构体。在调用接口前建议通过[ARKWEB\_MEMBER\_MISSING](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-type-h#宏定义)校验该函数结构体是否有对应函数指针，避免SDK与设备ROM不匹配导致crash问题。WebMessagePort相关接口需在UI线程中调用OH\_ArkWeb\_GetNativeAPI方法获取。

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
| [ArkWeb\_ErrorCode (\*postMessage)(const ArkWeb\_WebMessagePortPtr webMessagePort, const char\* webTag, const ArkWeb\_WebMessagePtr webMessage)](#postmessage) | 发送消息到HTML。 |
| [void (\*close)(const ArkWeb\_WebMessagePortPtr webMessagePort, const char\* webTag)](#close) | 关闭消息端口。 |
| [void (\*setMessageEventHandler)(const ArkWeb\_WebMessagePortPtr webMessagePort, const char\* webTag, ArkWeb\_OnMessageEventHandler messageEventHandler, void\* userData)](#setmessageeventhandler) | 设置接收HTML消息的回调。 |

#### 成员函数说明

#### \[h2\]postMessage()

```c
ArkWeb_ErrorCode (*postMessage)(const ArkWeb_WebMessagePortPtr webMessagePort, const char* webTag, const ArkWeb_WebMessagePtr webMessage)
```

**描述：**

发送消息到HTML。

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const [ArkWeb\_WebMessagePortPtr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-webmessageport8h) webMessagePort | Post Message端口结构体指针。 |
| const char\* webTag | Web组件名称。 |
| const [ArkWeb\_WebMessagePtr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-webmessage8h) webMessage | 需要发送的消息。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [ArkWeb\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-error-code-h#arkweb_errorcode) | 
[ARKWEB\_SUCCESS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-error-code-h#arkweb_errorcode) 执行成功。

[ARKWEB\_INVALID\_PARAM](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-error-code-h#arkweb_errorcode) 参数无效。

[ARKWEB\_INIT\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-error-code-h#arkweb_errorcode) 初始化失败，没有找到与webTag绑定的Web组件。

 |

#### \[h2\]close()

```c
void (*close)(const ArkWeb_WebMessagePortPtr webMessagePort, const char* webTag)
```

**描述：**

关闭消息端口。

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const [ArkWeb\_WebMessagePortPtr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-webmessageport8h) webMessagePort | Post Message端口结构体指针。 |
| const char\* webTag | Web组件名称。 |

#### \[h2\]setMessageEventHandler()

```c
void (*setMessageEventHandler)(const ArkWeb_WebMessagePortPtr webMessagePort, const char* webTag,
        ArkWeb_OnMessageEventHandler messageEventHandler, void* userData)
```

**描述：**

设置接收HTML消息的回调。

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const [ArkWeb\_WebMessagePortPtr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-webmessageport8h) webMessagePort | Post Message端口结构体指针。 |
| const char\* webTag | Web组件名称。 |
| [ArkWeb\_OnMessageEventHandler](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-type-h#arkweb_onmessageeventhandler) messageEventHandler | 处理消息的回调。 |
| void\* userData | 用户自定义数据。 |

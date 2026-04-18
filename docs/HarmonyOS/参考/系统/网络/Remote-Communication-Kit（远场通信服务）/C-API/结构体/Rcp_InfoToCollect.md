---
title: "Rcp_InfoToCollect"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___info_to_collect"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Remote Communication Kit（远场通信服务）"
  - "C API"
  - "结构体"
  - "Rcp_InfoToCollect"
captured_at: "2026-04-17T01:48:26.412Z"
---

# Rcp\_InfoToCollect

#### 概述

指定要收集的请求处理事件。可以通过响应对象检查收集的事件。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| bool [textual](#textual) | 是否收集未分类的文本事件。默认值为false。 |
| bool [incomingHeader](#incomingheader) | 是否收集传入HTTP标头事件。默认值为false。 |
| bool [outgoingHeader](#outgoingheader) | 是否收集传出HTTP标头事件。默认值为false。 |
| bool [incomingData](#incomingdata) | 是否收集有关传入HTTP数据的事件。默认值为false。 |
| bool [outgoingData](#outgoingdata) | 是否收集有关传出HTTP数据的事件。默认值为false。 |
| bool [incomingSslData](#incomingssldata) | 是否收集传入的SSL/TLS事件。默认值为false。 |
| bool [outgoingSslData](#outgoingssldata) | 是否收集传出的SSL/TLS事件。默认值为false。 |

#### 结构体成员变量说明

#### \[h2\]incomingData

```cpp
bool Rcp_InfoToCollect::incomingData
```

**描述**

是否收集有关传入HTTP数据的事件。默认值为false。

#### \[h2\]incomingHeader

```cpp
bool Rcp_InfoToCollect::incomingHeader
```

**描述**

是否收集传入HTTP标头事件。默认值为false。

#### \[h2\]incomingSslData

```cpp
bool Rcp_InfoToCollect::incomingSslData
```

**描述**

是否收集传入的SSL/TLS事件。默认值为false。

#### \[h2\]outgoingData

```cpp
bool Rcp_InfoToCollect::outgoingData
```

**描述**

是否收集有关传出HTTP数据的事件。默认值为false。

#### \[h2\]outgoingHeader

```cpp
bool Rcp_InfoToCollect::outgoingHeader
```

**描述**

是否收集传出HTTP标头事件。默认值为false。

#### \[h2\]outgoingSslData

```cpp
bool Rcp_InfoToCollect::outgoingSslData
```

**描述**

是否收集传出的SSL/TLS事件。默认值为false。

#### \[h2\]textual

```cpp
bool Rcp_InfoToCollect::textual
```

**描述**

是否收集未分类的文本事件。默认值为false。

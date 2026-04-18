---
title: "Rcp_InterceptorArray"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___interceptor_array"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Remote Communication Kit（远场通信服务）"
  - "C API"
  - "结构体"
  - "Rcp_InterceptorArray"
captured_at: "2026-04-17T01:48:26.424Z"
---

# Rcp\_InterceptorArray

#### 概述

异步拦截器数组。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [Rcp\_Interceptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___interceptor) \* [interceptors](#interceptors) | 异步拦截器数组。 [Rcp\_Interceptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___interceptor)\[\]。 |
| int [size](#size) | 数组大小。 |

#### 结构体成员变量说明

#### \[h2\]interceptors

```cpp
Rcp_Interceptor* Rcp_InterceptorArray::interceptors
```

**描述**

异步拦截器数组。 [Rcp\_Interceptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___interceptor)\[\]。

#### \[h2\]size

```cpp
int Rcp_InterceptorArray::size
```

**描述**

数组大小。

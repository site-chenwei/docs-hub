---
title: "Rcp_SyncInterceptorArray"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___sync_interceptor_array"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Remote Communication Kit（远场通信服务）"
  - "C API"
  - "结构体"
  - "Rcp_SyncInterceptorArray"
captured_at: "2026-04-17T01:48:26.751Z"
---

# Rcp\_SyncInterceptorArray

#### 概述

同步拦截器数组。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [Rcp\_SyncInterceptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___sync_interceptor) \* [interceptors](#interceptors) | 同步拦截器数组。 [Rcp\_SyncInterceptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___sync_interceptor)\[\]。 |
| int [size](#size) | 数组大小。 |

#### 结构体成员变量说明

#### \[h2\]interceptors

```cpp
Rcp_SyncInterceptor* Rcp_SyncInterceptorArray::interceptors
```

**描述**

同步拦截器数组。 [Rcp\_SyncInterceptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___sync_interceptor)\[\]。

#### \[h2\]size

```cpp
int Rcp_SyncInterceptorArray::size
```

**描述**

数组大小。

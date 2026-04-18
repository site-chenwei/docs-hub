---
title: "Rcp_ServerAuthentication"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___server_authentication"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Remote Communication Kit（远场通信服务）"
  - "C API"
  - "结构体"
  - "Rcp_ServerAuthentication"
captured_at: "2026-04-17T01:48:26.636Z"
---

# Rcp\_ServerAuthentication

#### 概述

服务器身份验证。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [Rcp\_Credential](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___credential)[credential](#credential) | 服务器的凭据。 |
| [Rcp\_AuthenticationType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#rcp_authenticationtype)[authenticationType](#authenticationtype) | 服务器的身份验证类型。如果未设置，请与服务器协商。 |

#### 结构体成员变量说明

#### \[h2\]authenticationType

```cpp
Rcp_AuthenticationType Rcp_ServerAuthentication::authenticationType
```

**描述**

服务器的身份验证类型。如果未设置，请与服务器协商。

#### \[h2\]credential

```cpp
Rcp_Credential Rcp_ServerAuthentication::credential
```

**描述**

服务器的凭据。

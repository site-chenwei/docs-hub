---
title: "Rcp_Credential"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___credential"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Remote Communication Kit（远场通信服务）"
  - "C API"
  - "结构体"
  - "Rcp_Credential"
captured_at: "2026-04-17T01:48:26.122Z"
---

# Rcp\_Credential

#### 概述

凭据。某些服务器或代理服务器需要。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| char \* [username](#username) | 凭据的用户名。默认值为""。 |
| char \* [password](#password) | 凭据的密码。默认值为""。 |

#### 结构体成员变量说明

#### \[h2\]password

```cpp
char* Rcp_Credential::password
```

**描述**

凭据的密码。默认值为""。

#### \[h2\]username

```cpp
char* Rcp_Credential::username
```

**描述**

凭据的用户名。默认值为""。

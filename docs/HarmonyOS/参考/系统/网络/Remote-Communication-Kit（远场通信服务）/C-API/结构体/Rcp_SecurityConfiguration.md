---
title: "Rcp_SecurityConfiguration"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___security_configuration"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Remote Communication Kit（远场通信服务）"
  - "C API"
  - "结构体"
  - "Rcp_SecurityConfiguration"
captured_at: "2026-04-17T01:48:26.632Z"
---

# Rcp\_SecurityConfiguration

#### 概述

请求的安全配置。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [Rcp\_RemoteValidationType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#rcp_remotevalidationtype)[remoteValidationType](#remotevalidationtype) | 远端认证方法类型。 |
| [Rcp\_CertificateAuthority](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___certificate_authority)[certificateAuthority](#certificateauthority) | 用于验证远程服务器标识的证书颁发机构（CA）。默认值为“system”，如果未设置此字段，将使用system CA验证远程服务器的标识。 |
| [Rcp\_ClientCertificate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___client_certificate)[certificate](#certificate) | 发送到远程服务器的客户端证书，远程服务器将使用它来验证客户端的标识。 |
| [Rcp\_ServerAuthentication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___server_authentication)[serverAuthentication](#serverauthentication) | 服务器身份验证设置。默认情况下不进行身份验证。 |

#### 结构体成员变量说明

#### \[h2\]certificate

```cpp
Rcp_ClientCertificate Rcp_SecurityConfiguration::certificate
```

**描述**

发送到远程服务器的客户端证书，远程服务器将使用它来验证客户端的标识。

#### \[h2\]certificateAuthority

```cpp
Rcp_CertificateAuthority Rcp_SecurityConfiguration::certificateAuthority
```

**描述**

用于验证远程服务器标识的证书颁发机构（CA）。默认值为“system”，如果未设置此字段，将使用system CA验证远程服务器的标识。

#### \[h2\]remoteValidationType

```cpp
Rcp_RemoteValidationType Rcp_SecurityConfiguration::remoteValidationType
```

**描述**

远端认证方法类型。

#### \[h2\]serverAuthentication

```cpp
Rcp_ServerAuthentication Rcp_SecurityConfiguration::serverAuthentication
```

**描述**

服务器身份验证设置。默认情况下不进行身份验证。

---
title: "Rcp_ClientCertificate"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___client_certificate"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Remote Communication Kit（远场通信服务）"
  - "C API"
  - "结构体"
  - "Rcp_ClientCertificate"
captured_at: "2026-04-17T01:48:25.842Z"
---

# Rcp\_ClientCertificate

#### 概述

发送到远程服务器的客户端证书，远程服务器将使用它来验证客户端的标识。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| char \* [content](#content) | 客户端证书内容。它应采用“PEM”、“DER”或“P12”格式。 |
| char \* [filePath](#filepath) | 客户端证书的路径。文件的格式应为“PEM”、“DER”或“P12”格式。 |
| char \* [key](#key) | 客户端证书私钥的文件名。 |
| char \* [keyPassword](#keypassword) | 客户端证书私钥的密码。 |
| [Rcp\_CertType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#rcp_certtype)[type](#type) | 客户端证书类型。 |

#### 结构体成员变量说明

#### \[h2\]content

```cpp
char* Rcp_ClientCertificate::content
```

**描述**

客户端证书内容。它应采用“PEM”、“DER”或“P12”格式。

#### \[h2\]filePath

```cpp
char* Rcp_ClientCertificate::filePath
```

**描述**

客户端证书的路径。文件的格式应为“PEM”、“DER”或“P12”格式。

#### \[h2\]key

```cpp
char* Rcp_ClientCertificate::key
```

**描述**

客户端证书私钥的文件名。

#### \[h2\]keyPassword

```cpp
char* Rcp_ClientCertificate::keyPassword
```

**描述**

客户端证书私钥的密码。

#### \[h2\]type

```cpp
Rcp_CertType Rcp_ClientCertificate::type
```

**描述**

客户端证书类型。

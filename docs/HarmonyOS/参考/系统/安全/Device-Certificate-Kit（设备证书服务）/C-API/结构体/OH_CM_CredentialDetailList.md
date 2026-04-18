---
title: "OH_CM_CredentialDetailList"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-certmanagertype-oh-cm-credentialdetaillist"
menu_path:
  - "参考"
  - "系统"
  - "安全"
  - "Device Certificate Kit（设备证书服务）"
  - "C API"
  - "结构体"
  - "OH_CM_CredentialDetailList"
captured_at: "2026-04-17T01:48:20.185Z"
---

# OH\_CM\_CredentialDetailList

```c
typedef struct {...} OH_CM_CredentialDetailList
```

#### 概述

定义证书凭据详情列表的结构体类型。

**起始版本：** 22

**相关模块：** [CertManagerType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-certmanagertype)

**所在头文件：** [cm\_native\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cm-native-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t credentialCount | 表示证书凭据详情的个数。 |
| [OH\_CM\_Credential](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-certmanagertype-oh-cm-credential) \*credential | 表示证书凭据详情列表。 |

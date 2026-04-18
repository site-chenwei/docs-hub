---
title: "OH_Huks_ExternalCryptoParam"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/sexternalcryptotypeapi-oh-huks-externalcryptoparam"
menu_path:
  - "参考"
  - "系统"
  - "安全"
  - "Universal Keystore Kit（密钥管理服务）"
  - "C API"
  - "结构体"
  - "OH_Huks_ExternalCryptoParam"
captured_at: "2026-04-17T01:48:20.695Z"
---

# OH\_Huks\_ExternalCryptoParam

```c
typedef struct {...} OH_Huks_ExternalCryptoParam
```

#### 概述

定义参数集合中单个参数的结构体。

**起始版本：** 22

**相关模块：** [HuksExternalCryptoTypeApi](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-huksexternalcryptotypeapi)

**所在头文件：** [native\_huks\_external\_crypto\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-external-crypto-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t tag | 标签值。 |
| 
union {

bool boolParam;

int32\_t int32Param;

uint32\_t uint32Param;

uint64\_t uint64Param;

[struct OH\_Huks\_Blob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-blob) blob;

}

 | 

标签内容。

boolParam：布尔类型参数。

int32Param：int32\_t类型参数。

uint32Param：uint32\_t类型参数。

uint64Param：uint64\_t类型参数。

blob：OH\_Huks\_Blob类型参数。

 |

---
title: "OH_Huks_ExternalCryptoParamSet"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ternalcryptotypeapi-oh-huks-externalcryptoparamset"
menu_path:
  - "参考"
  - "系统"
  - "安全"
  - "Universal Keystore Kit（密钥管理服务）"
  - "C API"
  - "结构体"
  - "OH_Huks_ExternalCryptoParamSet"
captured_at: "2026-04-17T01:48:20.699Z"
---

# OH\_Huks\_ExternalCryptoParamSet

```c
typedef struct OH_Huks_ExternalCryptoParamSet {...} OH_Huks_ExternalCryptoParamSet
```

#### 概述

定义外部加密参数集合的结构。

**起始版本：** 22

**相关模块：** [HuksExternalCryptoTypeApi](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-huksexternalcryptotypeapi)

**所在头文件：** [native\_huks\_external\_crypto\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-external-crypto-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t paramSetSize | 
参数集合所占内存大小，单位：Byte。

**起始版本：** 22

 |
| uint32\_t paramsCnt | 

参数集合中的参数数量。

**起始版本：** 22

 |
| [OH\_Huks\_ExternalCryptoParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/sexternalcryptotypeapi-oh-huks-externalcryptoparam) params\[\] | 

参数数组，大小由paramSetSize与paramsCnt决定。

**起始版本：** 22

 |

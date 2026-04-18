---
title: "OH_Huks_CertChain"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-certchain"
menu_path:
  - "参考"
  - "系统"
  - "安全"
  - "Universal Keystore Kit（密钥管理服务）"
  - "C API"
  - "结构体"
  - "OH_Huks_CertChain"
captured_at: "2026-04-17T01:48:20.789Z"
---

# OH\_Huks\_CertChain

```c
struct OH_Huks_CertChain {...}
```

#### 概述

定义证书链的结构体类型。

**起始版本：** 9

**相关模块：** [HuksTypeApi](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi)

**所在头文件：** [native\_huks\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| struct [OH\_Huks\_Blob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-blob) \*certs | 指向证书数据的指针。 |
| uint32\_t certsCount | 证书数量。 |

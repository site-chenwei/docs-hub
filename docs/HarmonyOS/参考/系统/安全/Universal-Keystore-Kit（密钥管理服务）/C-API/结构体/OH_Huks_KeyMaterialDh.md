---
title: "OH_Huks_KeyMaterialDh"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-keymaterialdh"
menu_path:
  - "参考"
  - "系统"
  - "安全"
  - "Universal Keystore Kit（密钥管理服务）"
  - "C API"
  - "结构体"
  - "OH_Huks_KeyMaterialDh"
captured_at: "2026-04-17T01:48:20.888Z"
---

# OH\_Huks\_KeyMaterialDh

```c
struct OH_Huks_KeyMaterialDh {...}
```

#### 概述

定义DH密钥的结构体类型。

**起始版本：** 9

**相关模块：** [HuksTypeApi](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi)

**所在头文件：** [native\_huks\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| enum [OH\_Huks\_KeyAlg](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-type-h#oh_huks_keyalg) keyAlg | 密钥的算法类型。 |
| uint32\_t keySize | DH密钥的长度。 |
| uint32\_t pubKeySize | 公钥的长度。 |
| uint32\_t priKeySize | 私钥的长度。 |
| uint32\_t reserved | 保留。 |

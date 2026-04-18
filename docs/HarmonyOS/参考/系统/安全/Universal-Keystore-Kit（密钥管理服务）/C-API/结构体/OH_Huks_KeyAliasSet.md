---
title: "OH_Huks_KeyAliasSet"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-keyaliasset"
menu_path:
  - "参考"
  - "系统"
  - "安全"
  - "Universal Keystore Kit（密钥管理服务）"
  - "C API"
  - "结构体"
  - "OH_Huks_KeyAliasSet"
captured_at: "2026-04-17T01:48:20.890Z"
---

# OH\_Huks\_KeyAliasSet

```c
struct OH_Huks_KeyAliasSet {...}
```

#### 概述

定义密钥别名集的结构体类型。

**起始版本：** 20

**相关模块：** [HuksTypeApi](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi)

**所在头文件：** [native\_huks\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t aliasesCnt | 密钥别名集个数。 |
| struct [OH\_Huks\_Blob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-blob) \*aliases | 指向密钥别名集数据的指针。 |

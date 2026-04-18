---
title: "OH_Huks_ParamSet"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-paramset"
menu_path:
  - "参考"
  - "系统"
  - "安全"
  - "Universal Keystore Kit（密钥管理服务）"
  - "C API"
  - "结构体"
  - "OH_Huks_ParamSet"
captured_at: "2026-04-17T01:48:20.770Z"
---

# OH\_Huks\_ParamSet

```c
struct OH_Huks_ParamSet {...}
```

#### 概述

定义参数集的结构体类型。

**起始版本：** 9

**相关模块：** [HuksTypeApi](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi)

**所在头文件：** [native\_huks\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t paramSetSize | 参数集的内存大小。 |
| uint32\_t paramsCnt | 参数的个数。 |
| struct [OH\_Huks\_Param](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-param) params\[\] | 参数数组。 |

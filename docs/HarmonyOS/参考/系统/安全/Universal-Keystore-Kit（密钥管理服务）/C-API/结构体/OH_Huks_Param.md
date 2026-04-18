---
title: "OH_Huks_Param"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-param"
menu_path:
  - "参考"
  - "系统"
  - "安全"
  - "Universal Keystore Kit（密钥管理服务）"
  - "C API"
  - "结构体"
  - "OH_Huks_Param"
captured_at: "2026-04-17T01:48:20.704Z"
---

# OH\_Huks\_Param

```c
struct OH_Huks_Param {...}
```

#### 概述

定义参数集中的参数结构体类型。

**起始版本：** 9

**相关模块：** [HuksTypeApi](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi)

**所在头文件：** [native\_huks\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-type-h)

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

boolParam：bool型参数。

int32Param：int32\_t型参数。

uint32Param：uint32\_t型参数。

uint64Param：uint64\_t型参数。

blob：OH\_Huks\_Blob型参数。

 |

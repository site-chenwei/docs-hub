---
title: "OH_Huks_Blob"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-blob"
menu_path:
  - "参考"
  - "系统"
  - "安全"
  - "Universal Keystore Kit（密钥管理服务）"
  - "C API"
  - "结构体"
  - "OH_Huks_Blob"
captured_at: "2026-04-17T01:48:20.721Z"
---

# OH\_Huks\_Blob

```c
struct OH_Huks_Blob {...}
```

#### 概述

定义存放数据的结构体类型。

**起始版本：** 9

**相关模块：** [HuksTypeApi](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi)

**所在头文件：** [native\_huks\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-huks-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t size | 数据大小。 |
| uint8\_t \*data | 指向数据内存的指针。 |

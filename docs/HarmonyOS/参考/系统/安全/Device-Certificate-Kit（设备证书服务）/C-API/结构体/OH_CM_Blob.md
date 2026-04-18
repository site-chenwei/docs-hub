---
title: "OH_CM_Blob"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-certmanagertype-oh-cm-blob"
menu_path:
  - "参考"
  - "系统"
  - "安全"
  - "Device Certificate Kit（设备证书服务）"
  - "C API"
  - "结构体"
  - "OH_CM_Blob"
captured_at: "2026-04-17T01:48:20.180Z"
---

# OH\_CM\_Blob

```c
typedef struct {...} OH_CM_Blob
```

#### 概述

定义存放数据的结构体类型。

**起始版本：** 22

**相关模块：** [CertManagerType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-certmanagertype)

**所在头文件：** [cm\_native\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cm-native-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t size | 数据大小。 |
| uint8\_t \*data | 指向数据内存的指针。 |

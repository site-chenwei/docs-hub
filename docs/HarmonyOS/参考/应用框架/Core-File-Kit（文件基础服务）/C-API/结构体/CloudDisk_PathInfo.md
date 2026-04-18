---
title: "CloudDisk_PathInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk-clouddisk-pathinfo"
menu_path:
  - "参考"
  - "应用框架"
  - "Core File Kit（文件基础服务）"
  - "C API"
  - "结构体"
  - "CloudDisk_PathInfo"
captured_at: "2026-04-17T01:48:14.499Z"
---

# CloudDisk\_PathInfo

```c
typedef struct CloudDisk_PathInfo {...} CloudDisk_PathInfo
typedef struct CloudDisk_PathInfo CloudDisk_FieldInfo
typedef struct CloudDisk_PathInfo CloudDisk_SyncFolderPath
```

#### 概述

文件路径信息。

**起始版本：** 21

**相关模块：** [CloudDisk](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk)

**所在头文件：** [oh\_cloud\_disk\_manager.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-cloud-disk-manager-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| char \*value | 文件的路径，以'\\0'字符结尾。 |
| size\_t length | 文件路径的长度，不包括结尾的'\\0'字符。 |

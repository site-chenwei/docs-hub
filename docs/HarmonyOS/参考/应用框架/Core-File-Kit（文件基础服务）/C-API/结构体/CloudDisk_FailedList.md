---
title: "CloudDisk_FailedList"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk-clouddisk-failedlist"
menu_path:
  - "参考"
  - "应用框架"
  - "Core File Kit（文件基础服务）"
  - "C API"
  - "结构体"
  - "CloudDisk_FailedList"
captured_at: "2026-04-17T01:48:14.481Z"
---

# CloudDisk\_FailedList

```c
typedef struct CloudDisk_FailedList {...} CloudDisk_FailedList
```

#### 概述

同步操作中失败的文件列表信息。该结构包含文件路径信息以及失败的具体错误原因。

**起始版本：** 21

**相关模块：** [CloudDisk](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk)

**所在头文件：** [oh\_cloud\_disk\_manager.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-cloud-disk-manager-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [CloudDisk\_PathInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk-clouddisk-pathinfo) pathInfo | 失败文件的绝对路径信息。 |
| [CloudDisk\_ErrorReason](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-cloud-disk-manager-h#clouddisk_errorreason) errorReason | 文件同步失败的原因。 |

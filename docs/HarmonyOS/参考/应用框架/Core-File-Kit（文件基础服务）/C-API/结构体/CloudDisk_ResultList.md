---
title: "CloudDisk_ResultList"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk-clouddisk-resultlist"
menu_path:
  - "参考"
  - "应用框架"
  - "Core File Kit（文件基础服务）"
  - "C API"
  - "结构体"
  - "CloudDisk_ResultList"
captured_at: "2026-04-17T01:48:14.500Z"
---

# CloudDisk\_ResultList

```c
typedef struct CloudDisk_ResultList {...} CloudDisk_ResultList
```

#### 概述

表示一个文件同步操作的结果。该结构体包含文件的绝对路径、同步结果，以及同步状态或失败原因。

**起始版本：** 21

**相关模块：** [CloudDisk](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk)

**所在头文件：** [oh\_cloud\_disk\_manager.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-cloud-disk-manager-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [CloudDisk\_PathInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk-clouddisk-pathinfo) pathInfo | 文件的绝对路径信息。 |
| bool isSuccess{false} | 表示操作是否成功。true：表示操作成功；false：表示操作失败。默认值为false。 |
| [CloudDisk\_SyncState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-cloud-disk-manager-h#clouddisk_syncstate) syncState | 文件的同步状态。当isSuccess为true时才生效。 |
| [CloudDisk\_ErrorReason](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-cloud-disk-manager-h#clouddisk_errorreason) errorReason | 文件同步状态获取失败的原因。当isSuccess为false时才生效。 |

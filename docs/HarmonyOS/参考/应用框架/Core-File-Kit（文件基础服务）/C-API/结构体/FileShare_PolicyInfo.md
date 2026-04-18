---
title: "FileShare_PolicyInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-fileshare-fileshare-policyinfo"
menu_path:
  - "参考"
  - "应用框架"
  - "Core File Kit（文件基础服务）"
  - "C API"
  - "结构体"
  - "FileShare_PolicyInfo"
captured_at: "2026-04-17T01:48:14.437Z"
---

# FileShare\_PolicyInfo

```c
typedef struct FileShare_PolicyInfo {...} FileShare_PolicyInfo
```

#### 概述

需要授予或使能权限URI的策略信息。

**起始版本：** 12

**相关模块：** [fileShare](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-fileshare)

**所在头文件：** [oh\_file\_share.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-file-share-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| char \*uri | 需要授予或使能权限的URI。 |
| unsigned int length | URI的字节长度。 |
| unsigned int operationMode | 
授予或使能权限的URI访问模式。

示例：FileShare\_OperationMode.READ\_MODE 、 FileShare\_OperationMode.WRITE\_MODE

或者 FileShare\_OperationMode.READ\_MODE|FileShare\_OperationMode.WRITE\_MODE。

 |

---
title: "raw_dir.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-raw-dir-h"
menu_path:
  - "参考"
  - "应用框架"
  - "Localization Kit（本地化开发服务）"
  - "C API"
  - "头文件"
  - "raw_dir.h"
captured_at: "2026-04-17T01:48:16.567Z"
---

# raw\_dir.h

#### 概述

提供rawfile目录相关功能，包括遍历和关闭rawfile目录。

**引用文件：** <rawfile/raw\_dir.h>

**库：** librawfile.z.so

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 8

**相关模块：** [rawfile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rawfile)

#### 汇总

#### \[h2\]结构体

| 名称 | typedef关键字 | 描述 |
| :-- | :-- | :-- |
| [RawDir](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rawfile-rawdir) | RawDir | 提供对rawfile目录的访问。 |

#### \[h2\]函数

| 名称 | 描述 |
| :-- | :-- |
| [const char \*OH\_ResourceManager\_GetRawFileName(RawDir \*rawDir, int index)](#oh_resourcemanager_getrawfilename) | 通过索引获取rawfile文件名称。可以使用此方法遍历rawfile目录。 |
| [int OH\_ResourceManager\_GetRawFileCount(RawDir \*rawDir)](#oh_resourcemanager_getrawfilecount) | 获取[RawDir](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rawfile-rawdir)中的rawfile数量。通过此方法可以获取[OH\_ResourceManager\_GetRawFileName](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-raw-dir-h#oh_resourcemanager_getrawfilename)中可用的索引。 |
| [void OH\_ResourceManager\_CloseRawDir(RawDir \*rawDir)](#oh_resourcemanager_closerawdir) | 关闭已打开的[RawDir](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rawfile-rawdir)并释放所有相关联资源。 |

#### 函数说明

#### \[h2\]OH\_ResourceManager\_GetRawFileName()

```c
const char *OH_ResourceManager_GetRawFileName(RawDir *rawDir, int index)
```

**描述**

通过索引获取rawfile文件名称。可以使用此方法遍历rawfile目录。

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [RawDir](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rawfile-rawdir) \*rawDir | 表示指向[RawDir](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rawfile-rawdir)的指针。 |
| int index | 表示文件在[RawDir](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rawfile-rawdir)中的索引位置。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| const char \* | 
通过索引返回文件名称，此返回值可以作为[OH\_ResourceManager\_OpenRawFile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-raw-file-manager-h#oh_resourcemanager_openrawfile)的输入参数。

如果遍历完所有文件仍未找到，则返回NULL。

 |

**参考：**

[OH\_ResourceManager\_OpenRawFile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-raw-file-manager-h#oh_resourcemanager_openrawfile)

#### \[h2\]OH\_ResourceManager\_GetRawFileCount()

```c
int OH_ResourceManager_GetRawFileCount(RawDir *rawDir)
```

**描述**

获取[RawDir](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rawfile-rawdir)中的rawfile数量。通过此方法可以获取[OH\_ResourceManager\_GetRawFileName](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-raw-dir-h#oh_resourcemanager_getrawfilename)中可用的索引。

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [RawDir](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rawfile-rawdir) \*rawDir | 表示指向[RawDir](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rawfile-rawdir)的指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int | 返回rawDir下的文件个数。如果rawDir为空时返回0。 |

**参考：**

[OH\_ResourceManager\_GetRawFileName](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-raw-dir-h#oh_resourcemanager_getrawfilename)

#### \[h2\]OH\_ResourceManager\_CloseRawDir()

```c
void OH_ResourceManager_CloseRawDir(RawDir *rawDir)
```

**描述**

关闭已打开的[RawDir](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rawfile-rawdir)并释放所有相关联资源。

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [RawDir](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rawfile-rawdir) \*rawDir | 表示指向[RawDir](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rawfile-rawdir)的指针。 |

**参考：**

[OH\_ResourceManager\_OpenRawDir](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-raw-file-manager-h#oh_resourcemanager_openrawdir)

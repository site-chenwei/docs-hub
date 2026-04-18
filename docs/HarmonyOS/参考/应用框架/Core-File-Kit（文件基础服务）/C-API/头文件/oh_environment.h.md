---
title: "oh_environment.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-environment-h"
menu_path:
  - "参考"
  - "应用框架"
  - "Core File Kit（文件基础服务）"
  - "C API"
  - "头文件"
  - "oh_environment.h"
captured_at: "2026-04-17T01:48:14.288Z"
---

# oh\_environment.h

#### 概述

environment模块接口定义，使用environment提供的native接口，获取公共文件根目录的沙箱路径。

**引用文件：** <filemanagement/environment/oh\_environment.h>

**库：** libohenvironment.so

**系统能力：** SystemCapability.FileManagement.File.Environment.FolderObtain

**起始版本：** 12

**相关模块：** [Environment](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-environment)

#### 汇总

#### \[h2\]函数

| 名称 | 描述 |
| :-- | :-- |
| [FileManagement\_ErrCode OH\_Environment\_GetUserDownloadDir(char \*\*result)](#oh_environment_getuserdownloaddir) | 获取Download根目录沙箱路径。 |
| [FileManagement\_ErrCode OH\_Environment\_GetUserDesktopDir(char \*\*result)](#oh_environment_getuserdesktopdir) | 获取Desktop根目录沙箱路径。 |
| [FileManagement\_ErrCode OH\_Environment\_GetUserDocumentDir(char \*\*result)](#oh_environment_getuserdocumentdir) | 获取Document根目录沙箱路径。 |

#### 函数说明

#### \[h2\]OH\_Environment\_GetUserDownloadDir()

```c
FileManagement_ErrCode OH_Environment_GetUserDownloadDir(char **result)
```

**描述**

获取Download根目录沙箱路径。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| char \*\*result | Download根目录路径指针。请引用头文件malloc.h并使用free()进行资源释放。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [FileManagement\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-error-code-h#filemanagement_errcode) | 返回FileManagement模块错误码[FileManagement\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-error-code-h#filemanagement_errcode)。 |

#### \[h2\]OH\_Environment\_GetUserDesktopDir()

```c
FileManagement_ErrCode OH_Environment_GetUserDesktopDir(char **result)
```

**描述**

获取Desktop根目录沙箱路径。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| char \*\*result | Desktop根目录路径指针。请引用头文件malloc.h并使用free()进行资源释放。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [FileManagement\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-error-code-h#filemanagement_errcode) | 返回FileManagement模块错误码[FileManagement\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-error-code-h#filemanagement_errcode)。 |

#### \[h2\]OH\_Environment\_GetUserDocumentDir()

```c
FileManagement_ErrCode OH_Environment_GetUserDocumentDir(char **result)
```

**描述**

获取Document根目录沙箱路径。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| char \*\*result | Document根目录路径指针。请引用头文件malloc.h并使用free()进行资源释放。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [FileManagement\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-error-code-h#filemanagement_errcode) | 返回FileManagement模块错误码[FileManagement\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-error-code-h#filemanagement_errcode)。 |

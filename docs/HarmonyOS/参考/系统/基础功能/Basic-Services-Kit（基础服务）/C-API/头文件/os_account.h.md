---
title: "os_account.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-os-account-h"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "Basic Services Kit（基础服务）"
  - "C API"
  - "头文件"
  - "os_account.h"
captured_at: "2026-04-17T01:48:28.883Z"
---

# os\_account.h

#### 概述

声明访问和管理系统帐号信息的API。

**库：** libos\_account\_ndk.so

**引用文件：** <BasicServicesKit/os\_account.h>

**系统能力：** SystemCapability.Account.OsAccount

**起始版本：** 12

**相关模块：** [OsAccount](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-osaccount)

#### 汇总

#### \[h2\]函数

| 名称 | 描述 |
| :-- | :-- |
| [OsAccount\_ErrCode OH\_OsAccount\_GetName(char \*buffer, size\_t buffer\_size)](#oh_osaccount_getname) | 获取调用方进程所属的系统帐号的名称。 |

#### 函数说明

#### \[h2\]OH\_OsAccount\_GetName()

```c
OsAccount_ErrCode OH_OsAccount_GetName(char *buffer, size_t buffer_size)
```

**描述**

获取调用方进程所属的系统帐号的名称。

**系统能力：** SystemCapability.Account.OsAccount

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| char \*buffer | 名称字符数组，其应具有能够存放名称（最大长度为LOGIN\_NAME\_MAX）和结束字符（'\\0'）的空间。 |
| size\_t buffer\_size | 名称字符数组的大小。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [OsAccount\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-os-account-common-h#osaccount_errcode) | 
OS\_ACCOUNT\_ERR\_OK：表示成功。

OS\_ACCOUNT\_ERR\_INTERNAL\_ERROR：表示内部错误。

OS\_ACCOUNT\_ERR\_INVALID\_PARAMETER：表示buffer为NULL指针，或名称（不包括结束字符'\\0'）的长度大于等于buffer\_size。

 |

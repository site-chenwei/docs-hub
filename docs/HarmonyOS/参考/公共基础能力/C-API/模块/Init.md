---
title: "Init"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/init"
menu_path:
  - "参考"
  - "公共基础能力"
  - "C API"
  - "模块"
  - "Init"
captured_at: "2026-04-17T01:49:06.323Z"
---

# Init

#### 概述

提供系统能力查询接口。

通过读取系统能力参数文件，返回指定的某个系统能力是否被支持。

**起始版本：**

8

#### 汇总

#### \[h2\]文件

| 名称 | 描述 |
| :-- | :-- |
| [syscap\_ndk.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/syscap__ndk_8h) | 
查询单个系统能力是否被支持的API。

**引用文件**：<syscap\_ndk.h>

**库**：libdeviceinfo\_ndk.z.so

 |

#### \[h2\]函数

| 名称 | 描述 |
| :-- | :-- |
| [canIUse](#caniuse) (const char \*cap) | 查询指定的系统能力是否被支持。 系统能力（SystemCapability，简称SysCap），指操作系统中每一个相对独立的特性。不同的设备对应不同的系统能力集，每个系统能力对应一个或多个API。开发者可根据系统能力来判断是否可以使用某接口。 |

#### 函数说明

#### \[h2\]canIUse()

```c
bool canIUse (const char * cap)
```

**描述:**

查询指定的系统能力是否被支持。 系统能力（SystemCapability，简称SysCap），指操作系统中每一个相对独立的特性。不同的设备对应不同的系统能力集，每个系统能力对应一个或多个API。开发者可根据系统能力来判断是否可以使用某接口。

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| cap | 待查询的系统能力名称。 |

**返回:**

| 类型 | 说明 |
| :-- | :-- |
| bool | 系统能力查询结果，true表示系统具备该能力，false表示系统不具备。 |

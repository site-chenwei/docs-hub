---
title: "errorcode.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-errorcode-h"
menu_path:
  - "参考"
  - "应用框架"
  - "Localization Kit（本地化开发服务）"
  - "C API"
  - "头文件"
  - "errorcode.h"
captured_at: "2026-04-17T01:48:16.657Z"
---

# errorcode.h

#### 概述

提供国际化接口返回的错误码。

**引用文件：** <i18n/errorcode.h>

**库：** libohi18n.so

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

**相关模块：** [i18n](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n)

#### 汇总

#### \[h2\]枚举

| 名称 | typedef关键字 | 描述 |
| :-- | :-- | :-- |
| [I18n\_ErrorCode](#i18n_errorcode) | I18n\_ErrorCode | 国际化错误码。 |

#### 枚举类型说明

#### \[h2\]I18n\_ErrorCode

```c
enum I18n_ErrorCode
```

**描述**

国际化错误码。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

| 枚举项 | 描述 |
| :-- | :-- |
| SUCCESS = 0 | 成功。 |
| ERROR\_INVALID\_PARAMETER = 8900001 | 传入参数无效。 |
| UNEXPECTED\_ERROR = 8900050 | 预期之外的错误，例如内存错误。 |

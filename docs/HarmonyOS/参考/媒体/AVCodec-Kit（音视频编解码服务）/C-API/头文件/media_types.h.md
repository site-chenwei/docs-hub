---
title: "media_types.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-media-types-h"
menu_path:
  - "参考"
  - "媒体"
  - "AVCodec Kit（音视频编解码服务）"
  - "C API"
  - "头文件"
  - "media_types.h"
captured_at: "2026-04-17T01:48:37.140Z"
---

# media\_types.h

#### 概述

声明了常见媒体类型的定义。

**引用文件：** <multimedia/player\_framework/media\_types.h>

**库：** libnative\_media\_core.so

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 18

**相关模块：** [Core](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-core)

#### 汇总

#### \[h2\]枚举

| 名称 | typedef关键字 | 描述 |
| :-- | :-- | :-- |
| [OH\_Core\_HdrType](#oh_core_hdrtype) | OH\_Core\_HdrType | HDR类型枚举。 |

#### 枚举类型说明

#### \[h2\]OH\_Core\_HdrType

```c
enum OH_Core_HdrType
```

**描述**

HDR类型枚举。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 18

| 枚举项 | 描述 |
| :-- | :-- |
| OH\_CORE\_HDR\_TYPE\_NONE = 0 | 此选项用于标记非HDR类型。 |
| OH\_CORE\_HDR\_TYPE\_VIVID = 1 | 此选项用于标记HDR Vivid类型。 |

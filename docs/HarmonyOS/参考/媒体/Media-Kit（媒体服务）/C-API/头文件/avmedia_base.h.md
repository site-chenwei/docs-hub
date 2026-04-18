---
title: "avmedia_base.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avmedia-base-h"
menu_path:
  - "参考"
  - "媒体"
  - "Media Kit（媒体服务）"
  - "C API"
  - "头文件"
  - "avmedia_base.h"
captured_at: "2026-04-17T01:48:44.027Z"
---

# avmedia\_base.h

#### 概述

定义AVMedia的结构体和枚举类型。

**引用文件：** <multimedia/player\_framework/avmedia\_base.h>

**库：** libavmedia\_base.so

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 23

**相关模块：** [AVMediaBase](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avmediabase)

#### 汇总

#### \[h2\]枚举

| 名称 | typedef关键字 | 描述 |
| :-- | :-- | :-- |
| [OH\_AVMedia\_SeekMode](#oh_avmedia_seekmode) | OH\_AVMedia\_SeekMode | 指定时间点和帧对应关系的枚举类型。 |

#### 枚举类型说明

#### \[h2\]OH\_AVMedia\_SeekMode

```c
enum OH_AVMedia_SeekMode
```

**描述**

指定时间点和帧对应关系的枚举类型。

**起始版本：** 23

| 枚举项 | 描述 |
| :-- | :-- |
| OH\_AVMEDIA\_SEEK\_NEXT\_SYNC = 0 | 表示选取传入时间点或之后的关键帧。 |
| OH\_AVMEDIA\_SEEK\_PREVIOUS\_SYNC = 1 | 表示选取传入时间点或之前的关键帧。 |
| OH\_AVMEDIA\_SEEK\_CLOSEST\_SYNC = 2 | 表示选取离传入时间点最近的关键帧。 |
| OH\_AVMEDIA\_SEEK\_CLOSEST = 3 | 表示选取离传入时间点最近的帧，该帧不一定是关键帧。 |

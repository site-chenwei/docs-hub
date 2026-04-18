---
title: "OH_AVDataSource"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-codecbase-oh-avdatasource"
menu_path:
  - "参考"
  - "媒体"
  - "AVCodec Kit（音视频编解码服务）"
  - "C API"
  - "结构体"
  - "OH_AVDataSource"
captured_at: "2026-04-17T01:48:37.458Z"
---

# OH\_AVDataSource

```c
typedef struct OH_AVDataSource {...} OH_AVDataSource
```

#### 概述

用户自定义数据源。

**起始版本：** 12

**相关模块：** [CodecBase](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-codecbase)

**所在头文件：** [native\_avcodec\_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avcodec-base-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int64\_t size | 数据源的总大小。 |
| [OH\_AVDataSourceReadAt](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avcodec-base-h#oh_avdatasourcereadat) readAt | 数据源的数据回调。 |

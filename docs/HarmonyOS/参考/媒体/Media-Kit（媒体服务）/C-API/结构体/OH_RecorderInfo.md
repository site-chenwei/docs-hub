---
title: "OH_RecorderInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-recorderinfo"
menu_path:
  - "参考"
  - "媒体"
  - "Media Kit（媒体服务）"
  - "C API"
  - "结构体"
  - "OH_RecorderInfo"
captured_at: "2026-04-17T01:48:44.433Z"
---

# OH\_RecorderInfo

```c
typedef struct OH_RecorderInfo {...} OH_RecorderInfo
```

#### 概述

录制文件信息。

**起始版本：** 10

**相关模块：** [AVScreenCapture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture)

**所在头文件：** [native\_avscreen\_capture\_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avscreen-capture-base-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| char\* url | 录制文件的URL。 |
| uint32\_t urlLen | 录制文件的URL的长度值。 |
| [OH\_ContainerFormatType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avscreen-capture-base-h#oh_containerformattype) fileFormat | 录制文件的格式。 |

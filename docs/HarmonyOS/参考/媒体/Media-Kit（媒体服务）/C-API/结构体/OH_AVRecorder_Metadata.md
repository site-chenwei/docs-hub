---
title: "OH_AVRecorder_Metadata"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-oh-avrecorder-metadata"
menu_path:
  - "参考"
  - "媒体"
  - "Media Kit（媒体服务）"
  - "C API"
  - "结构体"
  - "OH_AVRecorder_Metadata"
captured_at: "2026-04-17T01:48:44.299Z"
---

# OH\_AVRecorder\_Metadata

```c
typedef struct OH_AVRecorder_Metadata {...} OH_AVRecorder_Metadata
```

#### 概述

元数据信息数据结构。

**起始版本：** 18

**相关模块：** [AVRecorder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder)

**所在头文件：** [avrecorder\_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-base-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| char\* genre | 媒体资源的类型或体裁。 |
| char\* videoOrientation | 视频的旋转方向，单位为度。 |
| [OH\_AVRecorder\_Location](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-oh-avrecorder-location) location | 视频的地理位置信息。 |
| [OH\_AVRecorder\_MetadataTemplate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-oh-avrecorder-metadatatemplate) customInfo | 从 moov.meta.list 读取的自定义参数键值映射。 |

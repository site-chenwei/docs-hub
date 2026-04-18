---
title: "OH_VideoEncInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-videoencinfo"
menu_path:
  - "参考"
  - "媒体"
  - "Media Kit（媒体服务）"
  - "C API"
  - "结构体"
  - "OH_VideoEncInfo"
captured_at: "2026-04-17T01:48:44.445Z"
---

# OH\_VideoEncInfo

```c
typedef struct OH_VideoEncInfo {...} OH_VideoEncInfo
```

#### 概述

视频编码参数。

**起始版本：** 10

**相关模块：** [AVScreenCapture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture)

**所在头文件：** [native\_avscreen\_capture\_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avscreen-capture-base-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [OH\_VideoCodecFormat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avscreen-capture-base-h#oh_videocodecformat) videoCodec | 视频采集编码格式。 |
| int32\_t videoBitrate | 视频采集比特率。 |
| int32\_t videoFrameRate | 视频采集帧率。 |

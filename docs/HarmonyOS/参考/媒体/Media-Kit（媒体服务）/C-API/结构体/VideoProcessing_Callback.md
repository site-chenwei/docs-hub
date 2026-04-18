---
title: "VideoProcessing_Callback"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-videoprocessing-videoprocessing-callback"
menu_path:
  - "参考"
  - "媒体"
  - "Media Kit（媒体服务）"
  - "C API"
  - "结构体"
  - "VideoProcessing_Callback"
captured_at: "2026-04-17T01:48:44.767Z"
---

# VideoProcessing\_Callback

```c
typedef struct VideoProcessing_Callback VideoProcessing_Callback
```

#### 概述

视频处理回调对象类型。

定义一个VideoProcessing\_Callback空指针，调用[OH\_VideoProcessingCallback\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-video-processing-h#oh_videoprocessingcallback_create)来创建一个回调对象。创建之前该指针必须为空。通过调用[OH\_VideoProcessing\_RegisterCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-video-processing-h#oh_videoprocessing_registercallback)来向视频处理实例注册回调对象。

**起始版本：** 12

**相关模块：** [VideoProcessing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-videoprocessing)

**所在头文件：** [video\_processing\_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-video-processing-types-h)

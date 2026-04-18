---
title: "VideoOutput_Callbacks"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-videooutput-callbacks"
menu_path:
  - "参考"
  - "媒体"
  - "Camera Kit（相机服务）"
  - "C API"
  - "结构体"
  - "VideoOutput_Callbacks"
captured_at: "2026-04-17T01:48:40.182Z"
---

# VideoOutput\_Callbacks

```c
typedef struct VideoOutput_Callbacks {...} VideoOutput_Callbacks
```

#### 概述

用于录像输出的回调。

**起始版本：** 11

**相关模块：** [OH\_Camera](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera)

**所在头文件：** [video\_output.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-video-output-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [OH\_VideoOutput\_OnFrameStart](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-video-output-h#oh_videooutput_onframestart) onFrameStart | 录像输出帧启动事件。 |
| [OH\_VideoOutput\_OnFrameEnd](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-video-output-h#oh_videooutput_onframeend) onFrameEnd | 录像输出帧结束事件。 |
| [OH\_VideoOutput\_OnError](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-video-output-h#oh_videooutput_onerror) onError | 录像输出错误事件。 |

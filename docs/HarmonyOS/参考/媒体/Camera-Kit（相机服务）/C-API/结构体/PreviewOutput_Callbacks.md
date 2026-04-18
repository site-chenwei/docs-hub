---
title: "PreviewOutput_Callbacks"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-previewoutput-callbacks"
menu_path:
  - "参考"
  - "媒体"
  - "Camera Kit（相机服务）"
  - "C API"
  - "结构体"
  - "PreviewOutput_Callbacks"
captured_at: "2026-04-17T01:48:40.148Z"
---

# PreviewOutput\_Callbacks

```c
typedef struct PreviewOutput_Callbacks {...} PreviewOutput_Callbacks
```

#### 概述

用于预览输出的回调。

**起始版本：** 11

**相关模块：** [OH\_Camera](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera)

**所在头文件：** [preview\_output.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-preview-output-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [OH\_PreviewOutput\_OnFrameStart](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-preview-output-h#oh_previewoutput_onframestart) onFrameStart | 预览输出帧开始事件。 |
| [OH\_PreviewOutput\_OnFrameEnd](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-preview-output-h#oh_previewoutput_onframeend) onFrameEnd | 预览输出帧结束事件。 |
| [OH\_PreviewOutput\_OnError](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-preview-output-h#oh_previewoutput_onerror) onError | 预览输出错误事件。 |

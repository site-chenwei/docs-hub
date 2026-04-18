---
title: "PhotoOutput_Callbacks"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-photooutput-callbacks"
menu_path:
  - "参考"
  - "媒体"
  - "Camera Kit（相机服务）"
  - "C API"
  - "结构体"
  - "PhotoOutput_Callbacks"
captured_at: "2026-04-17T01:48:40.086Z"
---

# PhotoOutput\_Callbacks

```c
typedef struct PhotoOutput_Callbacks {...} PhotoOutput_Callbacks
```

#### 概述

拍照输出的回调。

**起始版本：** 11

**相关模块：** [OH\_Camera](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera)

**所在头文件：** [photo\_output.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-photo-output-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [OH\_PhotoOutput\_OnFrameStart](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-photo-output-h#oh_photooutput_onframestart) onFrameStart | 拍照输出帧启动事件。 |
| [OH\_PhotoOutput\_OnFrameShutter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-photo-output-h#oh_photooutput_onframeshutter) onFrameShutter | 拍照输出帧快门事件。 |
| [OH\_PhotoOutput\_OnFrameEnd](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-photo-output-h#oh_photooutput_onframeend) onFrameEnd | 拍照输出帧结束事件。 |
| [OH\_PhotoOutput\_OnError](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-photo-output-h#oh_photooutput_onerror) onError | 拍照输出错误事件。 |

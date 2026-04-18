---
title: "CaptureSession_Callbacks"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-capturesession-callbacks"
menu_path:
  - "参考"
  - "媒体"
  - "Camera Kit（相机服务）"
  - "C API"
  - "结构体"
  - "CaptureSession_Callbacks"
captured_at: "2026-04-17T01:48:40.074Z"
---

# CaptureSession\_Callbacks

```c
typedef struct CaptureSession_Callbacks {...} CaptureSession_Callbacks
```

#### 概述

捕获会话的回调。

**起始版本：** 11

**相关模块：** [OH\_Camera](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera)

**所在头文件：** [capture\_session.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [OH\_CaptureSession\_OnFocusStateChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_onfocusstatechange) onFocusStateChange | 捕获会话焦点状态更改事件。 |
| [OH\_CaptureSession\_OnError](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_onerror) onError | 捕获会话错误事件。 |

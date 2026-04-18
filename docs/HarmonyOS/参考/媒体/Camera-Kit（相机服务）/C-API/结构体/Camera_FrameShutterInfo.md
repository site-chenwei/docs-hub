---
title: "Camera_FrameShutterInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-frameshutterinfo"
menu_path:
  - "参考"
  - "媒体"
  - "Camera Kit（相机服务）"
  - "C API"
  - "结构体"
  - "Camera_FrameShutterInfo"
captured_at: "2026-04-17T01:48:39.843Z"
---

# Camera\_FrameShutterInfo

```c
typedef struct Camera_FrameShutterInfo {...} Camera_FrameShutterInfo
```

#### 概述

帧快门回调信息。

**起始版本：** 11

**相关模块：** [OH\_Camera](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera)

**所在头文件：** [camera.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int32\_t captureId | 捕获id。 |
| uint64\_t timestamp | 帧的时间戳，单位毫秒。 |

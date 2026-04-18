---
title: "Camera_CaptureStartInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-capturestartinfo"
menu_path:
  - "参考"
  - "媒体"
  - "Camera Kit（相机服务）"
  - "C API"
  - "结构体"
  - "Camera_CaptureStartInfo"
captured_at: "2026-04-17T01:48:39.861Z"
---

# Camera\_CaptureStartInfo

```c
typedef struct Camera_CaptureStartInfo {...} Camera_CaptureStartInfo
```

#### 概述

拍照开始信息。

**起始版本：** 12

**相关模块：** [OH\_Camera](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera)

**所在头文件：** [camera.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int32\_t captureId | 拍照id。 |
| int64\_t time | 预估的单次拍照底层出sensor采集帧时间，如果上报-1，代表没有预估时间。 |

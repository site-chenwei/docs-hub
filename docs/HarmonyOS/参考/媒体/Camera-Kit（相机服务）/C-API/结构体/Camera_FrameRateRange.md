---
title: "Camera_FrameRateRange"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-frameraterange"
menu_path:
  - "参考"
  - "媒体"
  - "Camera Kit（相机服务）"
  - "C API"
  - "结构体"
  - "Camera_FrameRateRange"
captured_at: "2026-04-17T01:48:39.633Z"
---

# Camera\_FrameRateRange

```c
typedef struct Camera_FrameRateRange {...} Camera_FrameRateRange
```

#### 概述

帧速率范围。

**起始版本：** 11

**相关模块：** [OH\_Camera](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera)

**所在头文件：** [camera.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t min | 最小帧速率，单位帧每秒。 |
| uint32\_t max | 最大帧速率，单位帧每秒。 |

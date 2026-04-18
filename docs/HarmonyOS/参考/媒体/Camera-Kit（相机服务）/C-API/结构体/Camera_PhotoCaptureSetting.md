---
title: "Camera_PhotoCaptureSetting"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-photocapturesetting"
menu_path:
  - "参考"
  - "媒体"
  - "Camera Kit（相机服务）"
  - "C API"
  - "结构体"
  - "Camera_PhotoCaptureSetting"
captured_at: "2026-04-17T01:48:39.842Z"
---

# Camera\_PhotoCaptureSetting

```c
typedef struct Camera_PhotoCaptureSetting {...} Camera_PhotoCaptureSetting
```

#### 概述

要设置的拍照捕获选项。

**起始版本：** 11

**相关模块：** [OH\_Camera](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera)

**所在头文件：** [camera.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [Camera\_QualityLevel](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_qualitylevel) quality | 拍照图像质量。 |
| [Camera\_ImageRotation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_imagerotation) rotation | 拍照旋转角度。 |
| [Camera\_Location](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-location)\* location | 拍照位置。 |
| bool mirror | 
设置镜像拍照功能开关。

true为打开，false为关闭，默认为false。

 |

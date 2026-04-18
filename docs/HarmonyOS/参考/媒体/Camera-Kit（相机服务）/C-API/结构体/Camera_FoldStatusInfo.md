---
title: "Camera_FoldStatusInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-foldstatusinfo"
menu_path:
  - "参考"
  - "媒体"
  - "Camera Kit（相机服务）"
  - "C API"
  - "结构体"
  - "Camera_FoldStatusInfo"
captured_at: "2026-04-17T01:48:39.934Z"
---

# Camera\_FoldStatusInfo

```c
typedef struct Camera_FoldStatusInfo {...} Camera_FoldStatusInfo
```

#### 概述

折叠状态信息。

**起始版本：** 13

**相关模块：** [OH\_Camera](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera)

**所在头文件：** [camera.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [Camera\_Device](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-device)\*\* supportedCameras | 相机实例列表。 |
| uint32\_t cameraSize | 相机列表数量。 |
| [Camera\_FoldStatus](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_foldstatus) foldStatus | 当前折叠状态。 |

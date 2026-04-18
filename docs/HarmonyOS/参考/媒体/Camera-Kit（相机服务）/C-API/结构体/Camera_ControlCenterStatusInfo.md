---
title: "Camera_ControlCenterStatusInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-controlcenterstatusinfo"
menu_path:
  - "参考"
  - "媒体"
  - "Camera Kit（相机服务）"
  - "C API"
  - "结构体"
  - "Camera_ControlCenterStatusInfo"
captured_at: "2026-04-17T01:48:39.941Z"
---

# Camera\_ControlCenterStatusInfo

```c
typedef struct Camera_ControlCenterStatusInfo {...} Camera_ControlCenterStatusInfo
```

#### 概述

控制器效果激活状态信息。

**起始版本：** 20

**相关模块：** [OH\_Camera](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera)

**所在头文件：** [camera.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [Camera\_ControlCenterEffectType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_controlcentereffecttype) effectType | 控制器效果类型。 |
| bool isActive | 控制器是否激活。true表示激活，false表示未激活。 |

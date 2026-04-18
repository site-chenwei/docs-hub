---
title: "Camera_Device"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-device"
menu_path:
  - "参考"
  - "媒体"
  - "Camera Kit（相机服务）"
  - "C API"
  - "结构体"
  - "Camera_Device"
captured_at: "2026-04-17T01:48:39.740Z"
---

# Camera\_Device

```c
typedef struct Camera_Device {...} Camera_Device
```

#### 概述

相机设备对象。

**起始版本：** 11

**相关模块：** [OH\_Camera](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera)

**所在头文件：** [camera.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| char\* cameraId | 相机id属性。 |
| [Camera\_Position](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_position) cameraPosition | 相机位置属性。 |
| [Camera\_Type](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_type) cameraType | 相机类型属性。 |
| [Camera\_Connection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_connection) connectionType | 相机连接类型属性。 |

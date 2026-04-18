---
title: "Camera_DeviceQueryInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-devicequeryinfo"
menu_path:
  - "参考"
  - "媒体"
  - "Camera Kit（相机服务）"
  - "C API"
  - "结构体"
  - "Camera_DeviceQueryInfo"
captured_at: "2026-04-17T01:48:39.733Z"
---

# Camera\_DeviceQueryInfo

```c
typedef struct {...} Camera_DeviceQueryInfo
```

#### 概述

相机设备的查询信息。

**起始版本：** 23

**相关模块：** [OH\_Camera](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera)

**所在头文件：** [camera.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| Camera\_Type\* cameraType | 相机类型属性列表。 |
| uint32\_t cameraTypeSize | 相机类型属性列表的大小。 |
| [Camera\_Position](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_position) cameraPosition | 相机位置属性。 |
| [Camera\_Connection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_connection) connectionType | 相机连接类型属性。 |

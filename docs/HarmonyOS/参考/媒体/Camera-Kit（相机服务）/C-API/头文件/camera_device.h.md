---
title: "camera_device.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-device-h"
menu_path:
  - "参考"
  - "媒体"
  - "Camera Kit（相机服务）"
  - "C API"
  - "头文件"
  - "camera_device.h"
captured_at: "2026-04-17T01:48:39.452Z"
---

# camera\_device.h

#### 概述

定义相机的基本接口和功能。

**引用文件：** <ohcamera/camera\_device.h>

**库：** libohcamera.so

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 12

**相关模块：** [OH\_Camera](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera)

#### 汇总

#### \[h2\]函数

| 名称 | 描述 |
| :-- | :-- |
| [Camera\_ErrorCode OH\_CameraDevice\_GetCameraOrientation(Camera\_Device\* camera, uint32\_t\* orientation)](#oh_cameradevice_getcameraorientation) | 获取相机设备的传感器方向属性。 |
| [Camera\_ErrorCode OH\_CameraDevice\_GetHostDeviceName(Camera\_Device\* camera, char\*\* hostDeviceName)](#oh_cameradevice_gethostdevicename) | 获取远程设备名称。 |
| [Camera\_ErrorCode OH\_CameraDevice\_GetHostDeviceType(Camera\_Device\* camera, Camera\_HostDeviceType\* hostDeviceType)](#oh_cameradevice_gethostdevicetype) | 获取远程设备类型。 |

#### 函数说明

#### \[h2\]OH\_CameraDevice\_GetCameraOrientation()

```c
Camera_ErrorCode OH_CameraDevice_GetCameraOrientation(Camera_Device* camera, uint32_t* orientation)
```

**描述**

获取相机设备的传感器方向属性。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [Camera\_Device](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-device)\* camera | 用于获取属性的Camera\_Device。 |
| uint32\_t\* orientation | 返回相机sensor角度属性。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [Camera\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_errorcode) | 
CAMERA\_OK：方法调用成功，返回传感器方向属性。

CAMERA\_CAMERA\_INVALID\_ARGUMENT：参数丢失或者参数不正确。

CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。

 |

#### \[h2\]OH\_CameraDevice\_GetHostDeviceName()

```c
Camera_ErrorCode OH_CameraDevice_GetHostDeviceName(Camera_Device* camera, char** hostDeviceName)
```

**描述**

获取远程设备名称。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [Camera\_Device](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-device)\* camera | 用于获取属性的Camera\_Device。 |
| char\*\* hostDeviceName | 返回远程设备名称属性。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [Camera\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_errorcode) | 
CAMERA\_OK：方法调用成功，将返回远程设备名称属性。

CAMERA\_CAMERA\_INVALID\_ARGUMENT：参数丢失或者参数不正确。

CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。

 |

#### \[h2\]OH\_CameraDevice\_GetHostDeviceType()

```c
Camera_ErrorCode OH_CameraDevice_GetHostDeviceType(Camera_Device* camera, Camera_HostDeviceType* hostDeviceType)
```

**描述**

获取远程设备类型。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [Camera\_Device](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-device)\* camera | 用于获取属性的Camera\_Device。 |
| [Camera\_HostDeviceType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_hostdevicetype)\* hostDeviceType | 远程设备类型属性。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [Camera\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_errorcode) | 
CAMERA\_OK：方法调用成功，将返回远程设备名称属性。

CAMERA\_CAMERA\_INVALID\_ARGUMENT：参数丢失或者参数不正确。

CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。

 |

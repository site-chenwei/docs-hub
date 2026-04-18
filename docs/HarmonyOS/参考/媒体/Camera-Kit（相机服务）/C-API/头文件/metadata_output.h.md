---
title: "metadata_output.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-metadata-output-h"
menu_path:
  - "参考"
  - "媒体"
  - "Camera Kit（相机服务）"
  - "C API"
  - "头文件"
  - "metadata_output.h"
captured_at: "2026-04-17T01:48:39.528Z"
---

# metadata\_output.h

#### 概述

声明元数据输出概念。

**引用文件：** <ohcamera/metadata\_output.h>

**库：** libohcamera.so

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 11

**相关模块：** [OH\_Camera](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera)

#### 汇总

#### \[h2\]结构体

| 名称 | typedef关键字 | 描述 |
| :-- | :-- | :-- |
| [MetadataOutput\_Callbacks](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-metadataoutput-callbacks) | MetadataOutput\_Callbacks | 元数据输出的回调。 |
| [Camera\_MetadataOutput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-metadataoutput) | Camera\_MetadataOutput | 
元数据输出对象。

可以使用[OH\_CameraManager\_CreateMetadataOutput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_createmetadataoutput)方法创建指针。

 |

#### \[h2\]函数

| 名称 | typedef关键字 | 描述 |
| :-- | :-- | :-- |
| [typedef void (\*OH\_MetadataOutput\_OnMetadataObjectAvailable)(Camera\_MetadataOutput\* metadataOutput, Camera\_MetadataObject\* metadataObject, uint32\_t size)](#oh_metadataoutput_onmetadataobjectavailable) | OH\_MetadataOutput\_OnMetadataObjectAvailable | 在[MetadataOutput\_Callbacks](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-metadataoutput-callbacks)中被调用的元数据输出元数据对象可用回调。 |
| [typedef void (\*OH\_MetadataOutput\_OnError)(Camera\_MetadataOutput\* metadataOutput, Camera\_ErrorCode errorCode)](#oh_metadataoutput_onerror) | OH\_MetadataOutput\_OnError | 在[MetadataOutput\_Callbacks](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-metadataoutput-callbacks)中被调用的元数据输出错误回调。 |
| [Camera\_ErrorCode OH\_MetadataOutput\_RegisterCallback(Camera\_MetadataOutput\* metadataOutput, MetadataOutput\_Callbacks\* callback)](#oh_metadataoutput_registercallback) | \- | 注册元数据输出更改事件回调。 |
| [Camera\_ErrorCode OH\_MetadataOutput\_UnregisterCallback(Camera\_MetadataOutput\* metadataOutput, MetadataOutput\_Callbacks\* callback)](#oh_metadataoutput_unregistercallback) | \- | 注销元数据输出更改事件回调。 |
| [Camera\_ErrorCode OH\_MetadataOutput\_Start(Camera\_MetadataOutput\* metadataOutput)](#oh_metadataoutput_start) | \- | 启动元数据输出。 |
| [Camera\_ErrorCode OH\_MetadataOutput\_Stop(Camera\_MetadataOutput\* metadataOutput)](#oh_metadataoutput_stop) | \- | 停止元数据输出。 |
| [Camera\_ErrorCode OH\_MetadataOutput\_Release(Camera\_MetadataOutput\* metadataOutput)](#oh_metadataoutput_release) | \- | 释放元数据输出实例。 |
| [Camera\_ErrorCode OH\_MetadataOutput\_AddMetadataObjectTypes(Camera\_MetadataOutput\* metadataOutput, Camera\_MetadataObjectType\* types, uint32\_t size)](#oh_metadataoutput_addmetadataobjecttypes) | \- | 添加元数据对象类型。 |
| [Camera\_ErrorCode OH\_MetadataOutput\_RemoveMetadataObjectTypes(Camera\_MetadataOutput\* metadataOutput, Camera\_MetadataObjectType\* types, uint32\_t size)](#oh_metadataoutput_removemetadataobjecttypes) | \- | 移除元数据对象类型。 |

#### 函数说明

#### \[h2\]OH\_MetadataOutput\_OnMetadataObjectAvailable()

```c
typedef void (*OH_MetadataOutput_OnMetadataObjectAvailable)(Camera_MetadataOutput* metadataOutput, Camera_MetadataObject* metadataObject, uint32_t size)
```

**描述**

在[MetadataOutput\_Callbacks](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-metadataoutput-callbacks)中被调用的元数据输出元数据对象可用回调。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [Camera\_MetadataOutput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-metadataoutput)\* metadataOutput | 传递回调的元数据输出实例。 |
| [Camera\_MetadataObject](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-metadataobject)\* metadataObject | 回调传递的元数据实例信息。 |
| uint32\_t size | 元数据对象的大小。 |

#### \[h2\]OH\_MetadataOutput\_OnError()

```c
typedef void (*OH_MetadataOutput_OnError)(Camera_MetadataOutput* metadataOutput, Camera_ErrorCode errorCode)
```

**描述**

在[MetadataOutput\_Callbacks](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-metadataoutput-callbacks)中被调用的元数据输出错误回调。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [Camera\_MetadataOutput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-metadataoutput)\* metadataOutput | 传递回调的元数据输出实例。 |
| [Camera\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_errorcode) errorCode | 元数据输出的错误码。 |

**参考：**

[CAMERA\_SERVICE\_FATAL\_ERROR](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_errorcode)

#### \[h2\]OH\_MetadataOutput\_RegisterCallback()

```c
Camera_ErrorCode OH_MetadataOutput_RegisterCallback(Camera_MetadataOutput* metadataOutput, MetadataOutput_Callbacks* callback)
```

**描述**

注册元数据输出更改事件回调。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [Camera\_MetadataOutput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-metadataoutput)\* metadataOutput | 元数据输出实例。 |
| [MetadataOutput\_Callbacks](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-metadataoutput-callbacks)\* callback | 要注册的元数据输出回调。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [Camera\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_errorcode) | 
CAMERA\_OK：方法调用成功。

CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。

 |

#### \[h2\]OH\_MetadataOutput\_UnregisterCallback()

```c
Camera_ErrorCode OH_MetadataOutput_UnregisterCallback(Camera_MetadataOutput* metadataOutput, MetadataOutput_Callbacks* callback)
```

**描述**

注销元数据输出更改事件回调。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [Camera\_MetadataOutput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-metadataoutput)\* metadataOutput | 元数据输出实例。 |
| [MetadataOutput\_Callbacks](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-metadataoutput-callbacks)\* callback | 要注销的元数据输出回调。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [Camera\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_errorcode) | 
CAMERA\_OK：方法调用成功。

CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。

 |

#### \[h2\]OH\_MetadataOutput\_Start()

```c
Camera_ErrorCode OH_MetadataOutput_Start(Camera_MetadataOutput* metadataOutput)
```

**描述**

启动元数据输出。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [Camera\_MetadataOutput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-metadataoutput)\* metadataOutput | 要启动的元数据输出实例。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [Camera\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_errorcode) | 
CAMERA\_OK：方法调用成功。

CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。

CAMERA\_SESSION\_NOT\_CONFIG：捕获会话未配置。

CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。

 |

#### \[h2\]OH\_MetadataOutput\_Stop()

```c
Camera_ErrorCode OH_MetadataOutput_Stop(Camera_MetadataOutput* metadataOutput)
```

**描述**

停止元数据输出。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [Camera\_MetadataOutput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-metadataoutput)\* metadataOutput | 要停止的元数据输出实例。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [Camera\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_errorcode) | 
CAMERA\_OK：方法调用成功。

CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。

CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。

 |

#### \[h2\]OH\_MetadataOutput\_Release()

```c
Camera_ErrorCode OH_MetadataOutput_Release(Camera_MetadataOutput* metadataOutput)
```

**描述**

释放元数据输出实例。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [Camera\_MetadataOutput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-metadataoutput)\* metadataOutput | 要释放的元数据输出实例。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [Camera\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_errorcode) | 
CAMERA\_OK：方法调用成功。

CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。

CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。

 |

#### \[h2\]OH\_MetadataOutput\_AddMetadataObjectTypes()

```c
Camera_ErrorCode OH_MetadataOutput_AddMetadataObjectTypes(Camera_MetadataOutput* metadataOutput, Camera_MetadataObjectType* types, uint32_t size)
```

**描述**

添加元数据对象类型。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [Camera\_MetadataOutput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-metadataoutput)\* metadataOutput | 元数据输出实例。 |
| [Camera\_MetadataObjectType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_metadataobjecttype)\* types | 用于添加到Camera\_MetadataOutput实例的元数据对象类型数组。 |
| uint32\_t size | 元数据对象类型数组长度。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [Camera\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_errorcode) | 
CAMERA\_OK：方法调用成功。

CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。

CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。

 |

#### \[h2\]OH\_MetadataOutput\_RemoveMetadataObjectTypes()

```c
Camera_ErrorCode OH_MetadataOutput_RemoveMetadataObjectTypes(Camera_MetadataOutput* metadataOutput, Camera_MetadataObjectType* types, uint32_t size)
```

**描述**

移除元数据对象类型。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [Camera\_MetadataOutput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-metadataoutput)\* metadataOutput | 元数据输出实例。 |
| [Camera\_MetadataObjectType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_metadataobjecttype)\* types | 从Camera\_MetadataOutput实例移除的元数据对象类型数组。 |
| uint32\_t size | 元数据对象类型数组长度。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [Camera\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_errorcode) | 
CAMERA\_OK：方法调用成功。

CAMERA\_INVALID\_ARGUMENT：参数丢失或参数类型不正确。

CAMERA\_SERVICE\_FATAL\_ERROR：相机服务异常。

 |

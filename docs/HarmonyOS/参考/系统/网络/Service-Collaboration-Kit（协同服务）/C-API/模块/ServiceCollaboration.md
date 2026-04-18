---
title: "ServiceCollaboration"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-module"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Service Collaboration Kit（协同服务）"
  - "C API"
  - "模块"
  - "ServiceCollaboration"
captured_at: "2026-04-17T01:48:27.101Z"
---

# ServiceCollaboration

#### 概述

提供ServiceCollaboration跨设备互通的相关NDK接口。

**系统能力：** SystemCapability.Collaboration.Service

**起始版本：** 5.0.0(12)

#### 汇总

#### \[h2\]文件

| 名称 | 描述 |
| :-- | :-- |
| [service\_collaboration\_api.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-h) | 跨设备互通的接口以及相关类型的定义。 |

#### \[h2\]结构体

| 名称 | 描述 |
| :-- | :-- |
| struct [ServiceCollaboration\_CollaborationDeviceInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-collaborationdeviceinfo) | 跨设备互通获取的设备信息对象，包含设备的基本信息和能力类型。 |
| struct [ServiceCollaboration\_CollaborationDeviceInfoSets](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-collaborationdeviceinfosets) | 通过[HMS\_ServiceCollaboration\_GetCollaborationDeviceInfos](#hms_servicecollaboration_getcollaborationdeviceinfos)获取的对端设备信息对象集合。 |
| struct [ServiceCollaboration\_SelectInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-selectinfo) | 使用[HMS\_ServiceCollaboration\_StartCollaboration](#hms_servicecollaboration_startcollaboration)触发跨设备互通时，被选择的设备信息。 |
| struct [ServiceCollaborationCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaborationcallback) | 传给[HMS\_ServiceCollaboration\_StartCollaboration](#hms_servicecollaboration_startcollaboration)的回调方法。 |
| struct [ServiceCollaboration\_SelectInfoV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-selectinfov2) | 使用[HMS\_ServiceCollaboration\_StartCollaborationV2](#hms_servicecollaboration_startcollaborationv2)触发跨设备互通时，被选择的设备信息，支持选择具有图片和视频回传能力的设备。 |

#### \[h2\]宏定义

| 名称 | 描述 |
| :-- | :-- |
| [COLLABORATIONDEVICEINFO\_DEVICENETWORKID\_MAXLENGTH](#collaborationdeviceinfo_devicenetworkid_maxlength) 65 | 设备network Id最大长度。 |
| [COLLABORATIONDEVICEINFO\_DEVICENAME\_MAXLENGTH](#collaborationdeviceinfo_devicename_maxlength) 128 | 设备名最大长度。 |
| [SERVICE\_COLLABORATION\_URI\_MAXLENGTH](#service_collaboration_uri_maxlength) 4096 | 传入沙箱目录uri的最大长度。 |

#### \[h2\]类型定义

| 名称 | 描述 |
| :-- | :-- |
| typedef enum [ServiceCollaborationFilterType](#servicecollaborationfiltertype-1) [ServiceCollaborationFilterType](#servicecollaborationfiltertype) | 跨设备互通能力类型枚举。 |
| typedef enum [ServiceCollaborationDataType](#servicecollaborationdatatype-1) [ServiceCollaborationDataType](#servicecollaborationdatatype) | 回传数据类型。 |
| typedef enum [ServiceCollaborationEventCode](#servicecollaborationeventcode-1) [ServiceCollaborationEventCode](#servicecollaborationeventcode) | 错误码枚举。 |
| typedef struct [ServiceCollaboration\_CollaborationDeviceInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-collaborationdeviceinfo) [ServiceCollaboration\_CollaborationDeviceInfo](#servicecollaboration_collaborationdeviceinfo) | 设备信息对象。 |
| typedef struct [ServiceCollaboration\_CollaborationDeviceInfoSets](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-collaborationdeviceinfosets) [ServiceCollaboration\_CollaborationDeviceInfoSets](#servicecollaboration_collaborationdeviceinfosets) | 设备信息对象集合。 |
| typedef struct [ServiceCollaboration\_SelectInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-selectinfo) [ServiceCollaboration\_SelectInfo](#servicecollaboration_selectinfo) | 被选择的设备信息。 |
| typedef struct [ServiceCollaborationCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaborationcallback) [ServiceCollaborationCallback](#servicecollaborationcallback) | 回调跨设备互通状态信息。 |
| typedef struct [ServiceCollaboration\_SelectInfoV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-selectinfov2) [ServiceCollaboration\_SelectInfoV2](#servicecollaboration_selectinfov2) | 使用[HMS\_ServiceCollaboration\_StartCollaborationV2](#hms_servicecollaboration_startcollaborationv2)触发跨设备互通时，被选择的设备信息，支持选择具有图片和视频回传能力的设备。 |
| typedef enum [CollaborationDeviceFilterType](#collaborationdevicefiltertype) [CollaborationDeviceFilterType](#collaborationdevicefiltertype) | 跨设备互通被调用端能力类型枚举 |

#### \[h2\]枚举

| 名称 | 描述 |
| :-- | :-- |
| 
[ServiceCollaborationFilterType](#servicecollaborationfiltertype-1) {

TAKE\_PHOTO = 1,

SCAN\_DOCUMENT = 2,

IMAGE\_PICKER = 3,

VIDEO\_PICKER = 5,

IMAGE\_VIDEO\_PICKER = 6

}

 | 跨设备互通能力类型的枚举。 |
| 

[ServiceCollaborationDataType](#servicecollaborationdatatype-1){

IMAGE = 1,

VIDEO = 2

}

 | 回传数据类型。 |
| 

[ServiceCollaborationEventCode](#servicecollaborationeventcode-1){

LAST\_DATA\_BACK = 1001202000,

PEER\_CANCEL = 1001202001,

NETWORK\_ERROR = 1001202002,

PEER\_WIFI\_NOT\_OPEN = 1001202004,

LOCAL\_WIFI\_NOT\_OPEN = 1001202005,

DATA\_BACK\_START = 1001202006,

MIDDLE\_DATA\_BACK = 1001202007,

TIMEOUT\_AUTO\_CANCEL = 1001202008,

DATA\_READ\_FAILED = 1001202009,

LINK\_SHUTDOWN = 1001202011,

REMOTE\_HOTSPOT\_CONFLICT = 1001202013,

REMOTE\_DISTRIBUTED\_SERVICES\_CONFLICT = 1001202014,

SEND\_VIDEO\_SUCCESS = 1001202015,

MULTI\_VIDEO\_SENDING\_BACK = 1001202016,

STORE\_VIDEO\_FAIL = 1001202017

}

 | 错误码枚举。 |
| 

[CollaborationDeviceFilterType](#collaborationdevicefiltertype) {

PHONE = 1,

TABLET = 2,

PC\_2IN1 = 3

}

 | 设备类型枚举 |

#### \[h2\]函数

| 名称 | 描述 |
| :-- | :-- |
| 
[ServiceCollaboration\_CollaborationDeviceInfoSets](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-collaborationdeviceinfosets)\* [HMS\_ServiceCollaboration\_GetCollaborationDeviceInfos](#hms_servicecollaboration_getcollaborationdeviceinfos)(

uint32\_t fileterNum, [ServiceCollaborationFilterType](#servicecollaborationfiltertype-1) serviceFileterTypes\[\])

 | 获取支持相关能力的设备列表。 |
| 

uint32\_t [HMS\_ServiceCollaboration\_StartCollaboration](#hms_servicecollaboration_startcollaboration)(

const [ServiceCollaboration\_SelectInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-selectinfo)\* selectService, [ServiceCollaborationCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaborationcallback)\* callback)

 | 拉起跨设备互通回传图片的能力。 |
| int32\_t [HMS\_ServiceCollaboration\_StopCollaboration](#hms_servicecollaboration_stopcollaboration)(uint32\_t collaborationId) | 取消跨设备互通能力。 |
| 

int32\_t [HMS\_ServiceCollaboration\_StartCollaborationV2](#hms_servicecollaboration_startcollaborationv2)(

const [ServiceCollaboration\_SelectInfoV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-selectinfov2)\* selectService, [ServiceCollaborationCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaborationcallback)\* callback)

)

 | 拉起跨设备互通回传图片和视频的能力。 |
| 

[ServiceCollaboration\_CollaborationDeviceInfoSets](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-collaborationdeviceinfosets)\*

[HMS\_ServiceCollaboration\_GetCollaborationDeviceInfosV2](#hms_servicecollaboration_getcollaborationdeviceinfosv2) (

uint32\_t deviceFilterNum, [CollaborationDeviceFilterType](#collaborationdevicefiltertype)

deviceFilterTypes\[\], uint32\_t serviceFilterNum,

[ServiceCollaborationFilterType](#servicecollaborationfiltertype-1) serviceFilterTypes\[\])

 | 获取支持相关能力的指定设备列表。 |

#### 宏定义说明

#### \[h2\]COLLABORATIONDEVICEINFO\_DEVICENETWORKID\_MAXLENGTH

```c
#define COLLABORATIONDEVICEINFO_DEVICENETWORKID_MAXLENGTH   65
```

**描述**

设备network Id最大长度。

**起始版本：** 5.0.0(12)

#### \[h2\]COLLABORATIONDEVICEINFO\_DEVICENAME\_MAXLENGTH

```c
#define COLLABORATIONDEVICEINFO_DEVICENAME_MAXLENGTH   128
```

**描述**

设备名最大长度。

**起始版本：** 5.0.0(12)

#### \[h2\]SERVICE\_COLLABORATION\_URI\_MAXLENGTH

```c
#define SERVICE_COLLABORATION_URI_MAXLENGTH   4096
```

**描述**

应用沙箱目录uri的最大长度。

**起始版本：** 6.1.0(23)

#### 类型定义说明

#### \[h2\]ServiceCollaboration\_CollaborationDeviceInfo

```c
typedef struct ServiceCollaboration_CollaborationDeviceInfo ServiceCollaboration_CollaborationDeviceInfo
```

**描述**

设备信息对象。

**起始版本：** 5.0.0(12)

#### \[h2\]ServiceCollaboration\_CollaborationDeviceInfoSets

```c
typedef struct ServiceCollaboration_CollaborationDeviceInfoSets ServiceCollaboration_CollaborationDeviceInfoSets
```

**描述**

设备信息对象集合。

**起始版本：** 5.0.0(12)

#### \[h2\]ServiceCollaboration\_SelectInfo

```c
typedef struct ServiceCollaboration_SelectInfo ServiceCollaboration_SelectInfo
```

**描述**

被选择的设备信息。

**起始版本：** 5.0.0(12)

#### \[h2\]ServiceCollaborationCallback

```c
typedef struct ServiceCollaborationCallback ServiceCollaborationCallback
```

**描述**

回调跨设备互通状态信息。

**起始版本：** 5.0.0(12)

#### \[h2\]ServiceCollaborationFilterType

```c
typedef enum ServiceCollaborationFilterType ServiceCollaborationFilterType
```

**描述**

跨设备互通能力类型的枚举。

**起始版本：** 5.0.0(12)

#### \[h2\]ServiceCollaborationDataType

```c
typedef enum ServiceCollaborationDataType ServiceCollaborationDataType
```

**描述**

回传数据类型。

**起始版本：** 5.0.0(12)

#### \[h2\]ServiceCollaborationEventCode

```c
typedef enum ServiceCollaborationEventCode ServiceCollaborationEventCode
```

**描述**

错误码枚举。

**起始版本：** 5.0.0(12)

#### \[h2\]ServiceCollaboration\_SelectInfoV2

```c
typedef struct ServiceCollaboration_SelectInfoV2 ServiceCollaboration_SelectInfoV2
```

**描述**

使用[HMS\_ServiceCollaboration\_StartCollaborationV2](#hms_servicecollaboration_startcollaborationv2)触发跨设备互通时，被选择的设备信息，支持选择具有图片和视频回传能力的设备。

**起始版本：** 6.1.0(23)

#### 枚举定义说明

#### \[h2\]ServiceCollaborationFilterType

```c
enum ServiceCollaborationFilterType
```

**描述**

跨设备互通能力类型枚举。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| :-- | :-- |
| TAKE\_PHOTO = 1 | 拍照。 |
| SCAN\_DOCUMENT = 2 | 扫描。 |
| IMAGE\_PICKER = 3 | 从图库中选择图片。 |
| VIDEO\_PICKER = 5 | 
从图库中选择视频。

**起始版本：** 6.1.0(23)

 |
| IMAGE\_VIDEO\_PICKER = 6 | 

从图库中选择图片与视频。

**起始版本：** 6.1.0(23)

 |

#### \[h2\]CollaborationDeviceFilterType

```c
enum CollaborationDeviceFilterType
```

**描述**

跨设备互通设备类型枚举。

**起始版本：** 6.1.0(23)

| 枚举值 | 描述 |
| :-- | :-- |
| PHONE | 手机。 |
| TABLET | 平板。 |
| PC\_2IN1 | PC/2in1。 |

#### \[h2\]ServiceCollaborationDataType

```c
enum ServiceCollaborationDataType
```

**描述**

回传数据类型。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| :-- | :-- |
| IMAGE = 1 | 图片。 |
| VIDEO = 2 | 
视频。

**起始版本：** 6.1.0(23)

 |

#### \[h2\]ServiceCollaborationEventCode

```c
enum ServiceCollaborationEventCode
```

**描述**

错误码枚举。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| :-- | :-- |
| LAST\_DATA\_BACK = 1001202000 | 已收到最后一个数据包。 |
| PEER\_CANCEL = 1001202001 | 对端取消。 |
| NETWORK\_ERROR = 1001202002 | 网络异常。 |
| PEER\_WIFI\_NOT\_OPEN = 1001202004 | 对端WLAN未开启。 |
| LOCAL\_WIFI\_NOT\_OPEN = 1001202005 | 本端WLAN未开启。 |
| DATA\_BACK\_START = 1001202006 | 开始回传数据。 |
| MIDDLE\_DATA\_BACK = 1001202007 | 收到中间数据。 |
| TIMEOUT\_AUTO\_CANCEL = 1001202008 | 接收数据超时取消。 |
| DATA\_READ\_FAILED = 1001202009 | 数据读取失败。 |
| LINK\_SHUTDOWN = 1001202011 | 链路断开。 |
| REMOTE\_HOTSPOT\_CONFLICT = 1001202013 | 
由于对端开启热点产生了链路冲突。

**起始版本：** 5.1.0(18)

 |
| REMOTE\_DISTRIBUTED\_SERVICES\_CONFLICT = 1001202014 | 

由于对端设备正在与其他设备进行互联而产生了链路冲突。

**起始版本：** 5.1.0(18)

 |
| SEND\_VIDEO\_SUCCESS = 1001202015 | 

视频回传成功。

**起始版本：** 6.1.0(23)

 |
| MULTI\_VIDEO\_SENDING\_BACK = 1001202016 | 

开始多个视频回传。

**起始版本：** 6.1.0(23)

 |
| STORE\_VIDEO\_FAIL = 1001202017 | 

内存不足视频回传失败。

**起始版本：** 6.1.0(23)

 |

#### 函数说明

#### \[h2\]HMS\_ServiceCollaboration\_GetCollaborationDeviceInfos

```c
ServiceCollaboration_CollaborationDeviceInfoSets* HMS_ServiceCollaboration_GetCollaborationDeviceInfos(
    uint32_t fileterNum, ServiceCollaborationFilterType serviceFileterTypes[]);
```

**描述**

获取支持相关能力的设备列表。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t fileterNum | 服务能力类型总数。 |
| [ServiceCollaborationFilterType](#servicecollaborationfiltertype-1) serviceFileterTypes\[\] | 具体需要的服务能力类型的数组。 |

**返回：**

返回[ServiceCollaboration\_CollaborationDeviceInfoSets](#servicecollaboration_collaborationdeviceinfosets)，设备信息对象集合。

#### \[h2\]HMS\_ServiceCollaboration\_GetCollaborationDeviceInfosV2

```c
ServiceCollaboration_CollaborationDeviceInfoSets* HMS_ServiceCollaboration_GetCollaborationDeviceInfosV2(
    uint32_t deviceFilterNum, CollaborationDeviceFilterType deviceFilterTypes[], uint32_t serviceFilterNum, ServiceCollaborationFilterType serviceFilterTypes[]);
```

**描述**

获取支持相关能力的指定设备列表。

**起始版本：** 6.1.0(23)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t deviceFilterNum | 设备类型总数。 |
| [CollaborationDeviceFilterType](#collaborationdevicefiltertype) deviceFilterTypes\[\] | 被调用端的设备类型的数组。 |
| uint32\_t serviceFilterNum | 服务能力类型总数。 |
| [ServiceCollaborationFilterType](#servicecollaborationfiltertype-1) serviceFilterTypes\[\] | 服务能力类型的数组。 |

**返回：**

返回[ServiceCollaboration\_CollaborationDeviceInfoSets](#servicecollaboration_collaborationdeviceinfosets)，设备信息对象集合。

#### \[h2\]HMS\_ServiceCollaboration\_StartCollaboration

```c
uint32_t HMS_ServiceCollaboration_StartCollaboration(
    const ServiceCollaboration_SelectInfo* selectService, ServiceCollaborationCallback* callback);
```

**描述**

拉起跨设备互通回传图片的能力。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| const [ServiceCollaboration\_SelectInfo](#servicecollaboration_selectinfo)\* selectService | 选择需要拉起的服务能力类型。 |
| [ServiceCollaborationCallback](#servicecollaborationcallback)\* callback | 回调，传递跨设备互通状态信息。 |

**返回：**

返回uint32\_t的collaborationId，本次跨设备互通唯一标识。

#### \[h2\]HMS\_ServiceCollaboration\_StopCollaboration

```c
int32_t HMS_ServiceCollaboration_StopCollaboration(uint32_t collaborationId);
```

**描述**

取消跨设备互通能力。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t collaborationId | 跨设备互通唯一标识。 |

**返回：**

返回stop结果，0为成功。

#### \[h2\]HMS\_ServiceCollaboration\_StartCollaborationV2

```c
uint32_t HMS_ServiceCollaboration_StartCollaborationV2(
    const ServiceCollaboration_SelectInfoV2* selectService, ServiceCollaborationCallback* callback);
```

**描述**

拉起跨设备互通回传图片和视频的能力。

**起始版本：** 6.1.0(23)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| const [ServiceCollaboration\_SelectInfoV2](#servicecollaboration_selectinfov2)\* selectService | 选择需要拉起的服务能力类型。 |
| [ServiceCollaborationCallback](#servicecollaborationcallback)\* callback | 回调，传递跨设备互通状态信息。 |

**返回：**

返回uint32\_t的collaborationId，本次跨设备互通唯一标识。

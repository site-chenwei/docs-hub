---
title: "ServiceCollaboration_CollaborationDeviceInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-collaborationdeviceinfo"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Service Collaboration Kit（协同服务）"
  - "C API"
  - "头文件和结构体"
  - "结构体"
  - "ServiceCollaboration_CollaborationDeviceInfo"
captured_at: "2026-04-17T01:48:27.174Z"
---

# ServiceCollaboration\_CollaborationDeviceInfo

#### 概述

跨设备互通获取的设备信息对象，包含设备的基本信息和能力类型。

**起始版本：** 5.0.0(12)

**相关模块：** [ServiceCollaboration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-module)

**所在头文件：** [service\_collaboration\_api.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t [deviceType](#devicetype) | 对端设备类型。只有手机或者平板。手机设备类型的值为0x14，平板设备类型的值为0x17。 |
| char [deviceNetworkId](#devicenetworkid) \[[COLLABORATIONDEVICEINFO\_DEVICENETWORKID\_MAXLENGTH](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-module#collaborationdeviceinfo_devicenetworkid_maxlength)\] | 对端设备network Id。 |
| char [deviceName](#devicename) \[[COLLABORATIONDEVICEINFO\_DEVICENAME\_MAXLENGTH](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-module#collaborationdeviceinfo_devicename_maxlength)\] | 对端设备名。 |
| uint32\_t [filterNum](#filternum) | 对端设备支持的能力类型列表的大小。 |
| [ServiceCollaborationFilterType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-module#servicecollaborationfiltertype-1) \* [serviceFilterTypes](#servicefiltertypes) | 对端设备支持的能力类型列表。 |

#### 结构体成员变量说明

#### \[h2\]deviceName

```c
char ServiceCollaboration_CollaborationDeviceInfo::deviceName[COLLABORATIONDEVICEINFO_DEVICENAME_MAXLENGTH]
```

**描述**

对端设备名。

#### \[h2\]deviceNetworkId

```c
char ServiceCollaboration_CollaborationDeviceInfo::deviceNetworkId[COLLABORATIONDEVICEINFO_DEVICENETWORKID_MAXLENGTH]
```

**描述**

对端设备network Id。

#### \[h2\]deviceType

```c
uint32_t ServiceCollaboration_CollaborationDeviceInfo::deviceType
```

**描述**

对端设备类型。只有手机或者平板。手机设备类型的值为0x14，平板设备类型的值为0x17。

#### \[h2\]filterNum

```c
uint32_t ServiceCollaboration_CollaborationDeviceInfo::filterNum
```

**描述**

对端设备支持的能力类型列表的大小。

#### \[h2\]serviceFilterTypes

```c
ServiceCollaborationFilterType* ServiceCollaboration_CollaborationDeviceInfo::serviceFilterTypes
```

**描述**

对端设备支持的能力类型列表。

---
title: "ServiceCollaboration_CollaborationDeviceInfoSets"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-collaborationdeviceinfosets"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Service Collaboration Kit（协同服务）"
  - "C API"
  - "头文件和结构体"
  - "结构体"
  - "ServiceCollaboration_CollaborationDeviceInfoSets"
captured_at: "2026-04-17T01:48:27.184Z"
---

# ServiceCollaboration\_CollaborationDeviceInfoSets

#### 概述

通过[HMS\_ServiceCollaboration\_GetCollaborationDeviceInfos](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-module#hms_servicecollaboration_getcollaborationdeviceinfos)获取的对端设备信息对象集合。

**起始版本：** 5.0.0(12)

**相关模块：** [ServiceCollaboration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-module)

**所在头文件：** [service\_collaboration\_api.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t [size](#size) | 对端设备信息对象集合的大小。 |
| [ServiceCollaboration\_CollaborationDeviceInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-collaborationdeviceinfo) \* [deviceInfoSets](#deviceinfosets) | 对端设备信息对象集合。 |

#### 结构体成员变量说明

#### \[h2\]deviceInfoSets

```c
ServiceCollaboration_CollaborationDeviceInfo* ServiceCollaboration_CollaborationDeviceInfoSets::deviceInfoSets
```

**描述**

对端设备信息对象集合。

#### \[h2\]size

```c
uint32_t ServiceCollaboration_CollaborationDeviceInfoSets::size
```

**描述**

对端设备信息对象集合的大小。

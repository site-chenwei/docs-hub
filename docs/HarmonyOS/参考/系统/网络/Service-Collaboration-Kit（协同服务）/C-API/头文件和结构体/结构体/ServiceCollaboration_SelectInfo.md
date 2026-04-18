---
title: "ServiceCollaboration_SelectInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-selectinfo"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Service Collaboration Kit（协同服务）"
  - "C API"
  - "头文件和结构体"
  - "结构体"
  - "ServiceCollaboration_SelectInfo"
captured_at: "2026-04-17T01:48:27.189Z"
---

# ServiceCollaboration\_SelectInfo

#### 概述

使用[HMS\_ServiceCollaboration\_StartCollaboration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-module#hms_servicecollaboration_startcollaboration)触发跨设备互通时，被选择的设备信息。

**起始版本：** 5.0.0(12)

**相关模块：** [ServiceCollaboration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-module)

**所在头文件：** [service\_collaboration\_api.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [ServiceCollaborationFilterType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-module#servicecollaborationfiltertype-1) [serviceFilterType](#servicefiltertype) | 开发者期望的设备能力类型。 |
| char [deviceNetworkId](#devicenetworkid) \[[COLLABORATIONDEVICEINFO\_DEVICENETWORKID\_MAXLENGTH](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-module#collaborationdeviceinfo_devicenetworkid_maxlength)\] | 被选择的设备network Id。 |
| uint32\_t [maxSize](#maxsize) | 被选择的设备能被选中的最大图片数量。 |

#### 结构体成员变量说明

#### \[h2\]deviceNetworkId

```c
char ServiceCollaboration_SelectInfo::deviceNetworkId[COLLABORATIONDEVICEINFO_DEVICENETWORKID_MAXLENGTH]
```

**描述**

被选择的设备network Id。

#### \[h2\]maxSize

```c
uint32_t ServiceCollaboration_SelectInfo::maxSize
```

**描述**

能被选中的最大图片数量，默认50。

#### \[h2\]serviceFilterType

```c
ServiceCollaborationFilterType ServiceCollaboration_SelectInfo::serviceFilterType
```

**描述**

开发者期望的设备能力类型。

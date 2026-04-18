---
title: "ServiceCollaboration_SelectInfoV2"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-selectinfov2"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Service Collaboration Kit（协同服务）"
  - "C API"
  - "头文件和结构体"
  - "结构体"
  - "ServiceCollaboration_SelectInfoV2"
captured_at: "2026-04-17T01:48:27.203Z"
---

# ServiceCollaboration\_SelectInfoV2

#### 概述

使用[HMS\_ServiceCollaboration\_StartCollaborationV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-module#hms_servicecollaboration_startcollaborationv2)触发跨设备互通时，被选择的设备信息，支持选择具有图片和视频回传能力的设备。

**起始版本：** 6.1.0(23)

**相关模块：** [ServiceCollaboration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-module)

**所在头文件：** [service\_collaboration\_api.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [ServiceCollaborationFilterType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-module#servicecollaborationfiltertype) [serviceFilterType](#servicefiltertype) | 开发者期望的设备能力类型。 |
| char [deviceNetworkId](#devicenetworkid) \[[COLLABORATIONDEVICEINFO\_DEVICENETWORKID\_MAXLENGTH](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-module#collaborationdeviceinfo_devicenetworkid_maxlength)\] | 被选择的设备network Id。 |
| uint32\_t [maxSize](#maxsize) | 能被选中的最大图片数量。 |
| char uri\[[SERVICE\_COLLABORATION\_URI\_MAXLENGTH](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-module#service_collaboration_uri_maxlength)\] | 应用沙箱目录uri路径。 |

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

能被选中的最大图片数量，默认50，取值范围为1到50。

#### \[h2\]serviceFilterType

```c
ServiceCollaborationFilterType ServiceCollaboration_SelectInfo::serviceFilterType
```

**描述**

开发者期望的设备能力类型。

#### \[h2\]uri

```c
uint32_t ServiceCollaboration_SelectInfo::uri[SERVICE_COLLABORATION_URI_MAXLENGTH]
```

**描述**

应用沙箱目录uri路径。

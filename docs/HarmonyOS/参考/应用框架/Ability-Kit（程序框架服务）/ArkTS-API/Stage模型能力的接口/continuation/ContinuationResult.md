---
title: "ContinuationResult"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-continuation-continuationresult"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "Stage模型能力的接口"
  - "continuation"
  - "ContinuationResult"
captured_at: "2026-04-17T01:47:46.724Z"
---

# ContinuationResult

流转管理入口返回的设备信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/C1DZjqrpT0iXJEsP_txaFw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=E7A9E50C1CD39E73159BF6E61A23D683DEAB4E5E7ABB59525C3922587A3D1DFD)

本模块首批接口从API version 8开始支持，从API version 22开始废弃，建议使用[分布式设备管理](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager)替代。

本模块接口仅可在Stage模型下使用。

#### ContinuationResult(deprecated)

ContinuationManager的[on](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-continuation-continuationmanager#continuationmanagerondeviceselecteddeprecated)接口返回此对象表示流转管理入口返回的设备信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/d4xtW5m8SAeA7b7BQVF1ew/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=41C7D6BF53F6C7151914F756719E51053085D27457AB70AD99DA4A1F3F701E32)

从API version 22开始废弃，建议使用[DeviceBasicInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager#devicebasicinfo)代替。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：以下各项对应的系统能力均为SystemCapability.Ability.DistributedAbilityManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| id | string | 否 | 否 | 表示设备标识。 |
| type | string | 否 | 否 | 表示设备类型。 |
| name | string | 否 | 否 | 表示设备名称。 |

---
title: "ContinuationExtraParams"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-continuation-continuationextraparams"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "Stage模型能力的接口"
  - "continuation"
  - "ContinuationExtraParams"
captured_at: "2026-04-17T01:47:46.727Z"
---

# ContinuationExtraParams

流转管理入口中设备选择模块所需的过滤参数，可以作为[startContinuationDeviceManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-continuation-continuationmanager#continuationmanagerstartcontinuationdevicemanagerdeprecated)的入参。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/kzpCBmKKQYGQjjOOp38HGg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=7868AC9FF7E098602185345DCA936DCBCB3AC838294C3933C321C5F968802615)

本模块首批接口从API version 8开始支持，从API version 22开始废弃，建议使用[分布式设备管理](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager)替代。

本模块接口仅可在Stage模型下使用。

#### ContinuationExtraParams(deprecated)

表示流转管理入口中设备选择模块所需的过滤参数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/utYOBuTqTKSdLN0w9i9NeQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=BA333F81A5A720EE98AECB7633455C168FDF66A95F4EACD23636A5003E7F1A53)

从API version 22开始废弃，建议使用[devicebasicinfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributeddevicemanager#devicebasicinfo)代替。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：以下各项对应的系统能力均为SystemCapability.Ability.DistributedAbilityManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| deviceType | Array<string> | 否 | 是 | 表示设备类型。 |
| targetBundle | string | 否 | 是 | 表示目标Bundle名称。 |
| description | string | 否 | 是 | 表示设备过滤的描述。 |
| filter | any | 否 | 是 | 表示设备过滤的参数。 |
| continuationMode | [continuationManager.ContinuationMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-continuation-continuationmanager#continuationmodedeprecated) | 否 | 是 | 表示协同的模式。 |
| authInfo | Record<string, Object> | 否 | 是 | 表示认证的信息。 |

---
title: "ElementName"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-elementname"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "已停止维护的接口"
  - "bundle"
  - "ElementName"
captured_at: "2026-04-17T01:47:48.335Z"
---

# ElementName

ElementName信息，通过接口[Context.getElementName](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-app-context#contextgetelementname7)获取。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/_UwyzSDqQKeAeZLoUWO26Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=77AAB1A80934F9AA9107746E77DC6B1752A03312383EC39F4D008E698744B473)

本模块首批接口从API version 7 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API version 9开始，该模块不再维护，建议使用[bundleManager-ElementName](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-elementname)替代。

#### ElementName(deprecated)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/R__v2xFSRQa_Tjyincl_ow/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=3D4D7E4EA362216E25EB5C1C05218DFE5FC0741679C5F64D28900CEB139E0EDD)

从API version 7开始支持，从API version 9开始废弃，建议使用[bundleManager-ElementName](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-elementname#elementname-1)替代。

ElementName信息，标识Ability的基本信息，通过接口[Context.getElementName](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-app-context#contextgetelementname7)获取。

**系统能力：** SystemCapability.BundleManager.BundleFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | 否 | 是 | 设备id值。 |
| bundleName | string | 否 | 否 | 应用Bundle的名称。 |
| abilityName | string | 否 | 否 | Ability的名称。 |
| uri | string | 否 | 是 | 资源标识符。 |
| shortName | string | 否 | 是 | Ability的短名称。 |

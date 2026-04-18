---
title: "HapModuleInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-hapmoduleinfo"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "已停止维护的接口"
  - "bundle"
  - "HapModuleInfo"
captured_at: "2026-04-17T01:47:48.390Z"
---

# HapModuleInfo

Hap模块信息，未做特殊说明的属性，均通过[bundle.getBundleInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle#bundlegetbundleinfodeprecated)获取。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/WDQ5yGYuSRqYZ1QTrYckww/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=F3200BEEA52BFE7F811363B2F3EDE57C2EA1AFCFDC2FAC4D8ACC8E6F0FF5FF36)

本模块首批接口从API version 7 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API version 9开始，该模块不再维护，建议使用[bundleManager-HapModuleInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-hapmoduleinfo)替代。

#### HapModuleInfo(deprecated)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/1gyGfZjaQjitxU7Pj-SXFQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=AA01B4794DA8FA6BAABFC9A88F408CB136A1D936338CD264822444D755BFE240)

从API version 7开始支持，从API version 9开始废弃，建议使用[bundleManager-HapModuleInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-hapmoduleinfo#hapmoduleinfo-1)替代。

**系统能力：** SystemCapability.BundleManager.BundleFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| name | string | 是 | 否 | 模块名称。 |
| description | string | 是 | 否 | 模块描述信息。 |
| descriptionId | number | 是 | 否 | 描述信息ID。 |
| icon | string | 是 | 否 | 模块图标。 |
| label | string | 是 | 否 | 模块标签。 |
| labelId | number | 是 | 否 | 模块标签ID。 |
| iconId | number | 是 | 否 | 模块图标ID。 |
| backgroundImg | string | 是 | 否 | 模块背景图片。 |
| supportedModes | number | 是 | 否 | 模块支持的模式。 |
| reqCapabilities | Array<string> | 是 | 否 | 模块运行需要的能力。 |
| deviceTypes | Array<string> | 是 | 否 | 支持运行的设备类型。 |
| abilityInfo | Array<[AbilityInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-abilityinfo)\> | 是 | 否 | Ability信息。 |
| moduleName | string | 是 | 否 | 模块名。 |
| mainAbilityName | string | 是 | 否 | 入口Ability名称。 |
| installationFree | boolean | 是 | 否 | 是否支持免安装，取值为true表示支持免安装，取值为false表示不支持免安装。 |

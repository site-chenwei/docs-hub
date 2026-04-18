---
title: "Metadata"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-metadata"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "接口依赖的元素及定义"
  - "bundleManager"
  - "Metadata"
captured_at: "2026-04-17T01:47:47.983Z"
---

# Metadata

元数据对象，可以通过[bundleManager.getBundleInfoForSelf](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager#bundlemanagergetbundleinfoforself)获取，其中参数bundleFlags至少包含GET\_BUNDLE\_INFO\_WITH\_METADATA。此对象在[ApplicationInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-applicationinfo)、[HapModuleInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-hapmoduleinfo)、[AbilityInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-abilityinfo)、[ExtensionAbilityInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-extensionabilityinfo)中均包含。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/IoMsejHaQfueh7oJ5wXojA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=7B9A3BC4E73EDBC052136D77B767A04B0A069D0930B5223DD51307A8310120ED)

本模块首批接口从API version 9 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

描述的module、uiAbility、extensionAbility配置信息，标签值为数组类型，该标签下的配置只对当前module、uiAbility或者extensionAbility生效。

#### 导入模块

```ts
import { bundleManager } from '@kit.AbilityKit';
```

#### Metadata

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**: SystemCapability.BundleManager.BundleFramework.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| name | string | 否 | 否 | 元数据名称。 |
| value | string | 否 | 否 | 元数据值。 |
| resource | string | 否 | 否 | 元数据资源描述符，参考示例$profile:config\_file，表示profile目录下配置了config\_file.json文件。 |
| valueId18+ | number | 是 | 是 | 元数据值id。当valueId不为0时，表示当前元数据值为自定义配置，需要使用valueId去资源管理获取对应的值。 当valueId为0时，表示当前元数据值为固定字符串。 |

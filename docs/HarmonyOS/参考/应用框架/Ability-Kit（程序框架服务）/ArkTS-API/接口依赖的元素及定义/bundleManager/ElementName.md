---
title: "ElementName"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-elementname"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "接口依赖的元素及定义"
  - "bundleManager"
  - "ElementName"
captured_at: "2026-04-17T01:47:47.868Z"
---

# ElementName

应用组件结构体，包含bundleName、moduleName和abilityName等。通常用于组件启动信息[AbilityRunningInfo.ability](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilityrunninginfo)和组件启动回调函数[connectOptions.onConnect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-connectoptions#onconnect)中。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/1W2hSuzvS0ep5q-QY_VYwQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=0384E48C4113FC79C830A99DC877A2491DB49DF822A789103A69F03C353DF517)

本模块首批接口从API version 9 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import { bundleManager } from '@kit.AbilityKit';
```

#### ElementName

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | 否 | 是 | 设备ID。 |
| bundleName | string | 否 | 否 | 应用Bundle名称。 |
| abilityName | string | 否 | 否 | Ability名称。 |
| uri | string | 否 | 是 | 资源标识符。 |
| shortName | string | 否 | 是 | Ability短名称，以“.”为开头的字符串。 |
| moduleName | string | 否 | 是 | Ability所属的HAP的模块名称。 |

---
title: "AppVersionInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-app-appversioninfo"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "FA模型能力的接口"
  - "app"
  - "AppVersionInfo"
captured_at: "2026-04-17T01:47:46.933Z"
---

# AppVersionInfo

应用版本信息，可以通过[getAppVersionInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-app-context#contextgetappversioninfo7)获取当前应用的版本信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/1AsMGy80RkqLav0shln0eg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=F040CE707BEFBFC5B2D06AFE5C41CE62B7DE2C3BBCB4C90E203AD13878231D48)

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在FA模型下使用。

#### 导入模块

```ts
import featureAbility from '@ohos.ability.featureAbility';
```

#### 属性

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| appName | string | 是 | 否 | 应用名称。 |
| versionCode | number | 是 | 否 | 应用版本编码。 |
| versionName | string | 是 | 否 | 应用版本名称。 |

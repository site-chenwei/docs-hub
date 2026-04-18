---
title: "KioskStatus (Kiosk状态信息)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-kioskstatus"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "接口依赖的元素及定义"
  - "application"
  - "KioskStatus (Kiosk状态信息)"
captured_at: "2026-04-17T01:47:47.649Z"
---

# KioskStatus (Kiosk状态信息)

表示Kiosk状态信息，包括系统是否处于Kiosk模式以及该模式下的应用信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/TikhvGU4Rui4b40J9DirRg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=6F41E29D4C8F59B2EB644275354443750D36CE3F07A400242DDF0808155E5509)

-   本模块首批接口从API version 20开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
-   本模块接口仅可在Stage模型下使用。

#### KioskStatus

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| isKioskMode | boolean | 否 | 否 | 当前系统是否处于Kiosk模式。true表示处于Kiosk模式，false表示不处于。 |
| kioskBundleName | string | 否 | 否 | 进入Kiosk模式的应用的名称。 |
| kioskBundleUid | number | 否 | 否 | 进入Kiosk模式的应用的UID。 |

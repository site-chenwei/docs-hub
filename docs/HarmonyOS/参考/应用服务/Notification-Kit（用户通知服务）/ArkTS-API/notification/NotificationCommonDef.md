---
title: "NotificationCommonDef"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-notification-notificationcommondef"
menu_path:
  - "参考"
  - "应用服务"
  - "Notification Kit（用户通知服务）"
  - "ArkTS API"
  - "notification"
  - "NotificationCommonDef"
captured_at: "2026-04-17T01:49:00.550Z"
---

# NotificationCommonDef

描述应用的包信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/1KwgrIyOT4ayi7u5Oswg2Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014900Z&HW-CC-Expire=86400&HW-CC-Sign=48CE2FAD265A690457030F64A7CBE21C9DA7CD69572D6E513B1584A271F5AFBC)

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### BundleOption

描述BundleOption信息，即应用的包信息。

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| bundle | string | 否 | 否 | 应用程序的包名。 |
| uid | number | 否 | 是 | 应用程序的UID。从[ApplicationInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-applicationinfo#applicationinfo-1)获取，默认为0。 应用分身场景下，此参数为必填项。 |

#### GrantedBundleInfo22+

描述已授权的包信息。

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| bundleName | string | 否 | 否 | 应用程序的包名。 |
| appIndex | number | 是 | 否 | 应用包的分身索引标识，仅在分身应用中生效。从[ApplicationInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-applicationinfo#applicationinfo-1)中appIndex获取。 |
| appName | string | 是 | 是 | 标识应用的名称。从[ApplicationInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-applicationinfo#applicationinfo-1)中label获取。 |

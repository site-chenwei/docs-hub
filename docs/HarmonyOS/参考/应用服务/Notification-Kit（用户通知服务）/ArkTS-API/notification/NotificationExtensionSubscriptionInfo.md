---
title: "NotificationExtensionSubscriptionInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/s-apis-inner-notificationextensionsubscriptioninfo"
menu_path:
  - "参考"
  - "应用服务"
  - "Notification Kit（用户通知服务）"
  - "ArkTS API"
  - "notification"
  - "NotificationExtensionSubscriptionInfo"
captured_at: "2026-04-17T01:49:00.702Z"
---

# NotificationExtensionSubscriptionInfo

用于描述通知扩展订阅的信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/NcRACam3QIuqepPzCMeTIg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014900Z&HW-CC-Expire=86400&HW-CC-Sign=ACAC9A1A823DEF78358D1A3C2BDAE4B8AC097419CD06DE80ECED8CFEB4F2A132)

本模块首批接口从API version 22开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### NotificationExtensionSubscriptionInfo

**系统能力：** SystemCapability.Notification.Notification

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| type | [notificationExtensionSubscription.SubscribeType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notificationextensionsubscription#subscribetype) | 否 | 否 | 表示订阅的类型，包括通过蓝牙订阅通知。 |
| addr | string | 否 | 否 | 表示设备的唯一标识符。例如："11:22:33:AA:BB:FF" |

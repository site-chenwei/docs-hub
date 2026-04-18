---
title: "NotificationInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-notification-notificationinfo"
menu_path:
  - "参考"
  - "应用服务"
  - "Notification Kit（用户通知服务）"
  - "ArkTS API"
  - "notification"
  - "NotificationInfo"
captured_at: "2026-04-17T01:49:00.551Z"
---

# NotificationInfo

通知订阅扩展能力中[onReceiveMessage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notificationsubscriberextensionability#onreceivemessage)回调的通知信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/1yrw3NsyRrik7lZyMau7mQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014900Z&HW-CC-Expire=86400&HW-CC-Sign=06A9768B6F1678CC4822A02E76B3AB11FA04606F7C77E46761A428A2C03121DD)

本模块首批接口从API version 22开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### NotificationInfo

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| hashCode | string | 是 | 否 | 通知的唯一标识符。 |
| notificationSlotType | [notificationManager.SlotType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notificationmanager#slottype) | 是 | 否 | 通知渠道类型。 |
| content | [NotificationExtensionContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/is-inner-notification-notificationextensioncontent) | 是 | 否 | 通知内容。 |
| bundleName | string | 是 | 否 | 创建通知的包名。 |
| appIndex | number | 是 | 否 | 创建通知的应用包的分身索引标识，仅在分身应用中生效。 |
| appName | string | 是 | 是 | 创建通知的应用程序名称。 |
| deliveryTime | number | 是 | 是 | 通知发布的时间戳（毫秒数）。 |
| groupName | string | 是 | 是 | 通知组名称。默认情况下此参数为空。 |

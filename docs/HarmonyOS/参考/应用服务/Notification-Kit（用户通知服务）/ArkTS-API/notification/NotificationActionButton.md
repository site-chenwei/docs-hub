---
title: "NotificationActionButton"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/s-apis-inner-notification-notificationactionbutton"
menu_path:
  - "参考"
  - "应用服务"
  - "Notification Kit（用户通知服务）"
  - "ArkTS API"
  - "notification"
  - "NotificationActionButton"
captured_at: "2026-04-17T01:49:00.547Z"
---

# NotificationActionButton

描述通知中显示的操作按钮。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/4n8Jb2wURc6OtFhZWaOiUw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014900Z&HW-CC-Expire=86400&HW-CC-Sign=3E0D0B7B5AFD815CB37FD4FA96D827160F686CDA24692B8BD099E7F72796A009)

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### NotificationActionButton

**系统能力：** SystemCapability.Notification.Notification

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| title | string | 否 | 否 | 按钮标题。字符串长度不超过200字节，超出部分会被截断；也不可为空字符串。 |
| wantAgent | [WantAgent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-wantagent) | 否 | 否 | 点击按钮时触发的WantAgent。 |
| extras | { \[key: string\]: any } | 否 | 是 | 按钮扩展信息。预留能力，暂未支持。 |
| userInput8+ | [NotificationUserInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-notification-notificationuserinput) | 否 | 是 | 用户输入对象实例，默认为空。表示用户输入时的标识。 |

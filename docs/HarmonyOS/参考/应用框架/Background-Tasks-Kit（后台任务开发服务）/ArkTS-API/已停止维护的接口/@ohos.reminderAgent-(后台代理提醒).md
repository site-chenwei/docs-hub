---
title: "@ohos.reminderAgent (后台代理提醒)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-reminderagent"
menu_path:
  - "参考"
  - "应用框架"
  - "Background Tasks Kit（后台任务开发服务）"
  - "ArkTS API"
  - "已停止维护的接口"
  - "@ohos.reminderAgent (后台代理提醒)"
captured_at: "2026-04-17T01:48:13.587Z"
---

# @ohos.reminderAgent (后台代理提醒)

本模块提供后台代理提醒的能力。

开发应用时，开发者可以调用相关接口创建定时提醒，包括倒计时、日历、闹钟这三类提醒类型。使用后台代理提醒能力后，应用被冻结或退出后，计时和弹出提醒的功能将被后台系统服务代理。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/i05AZ2v4TaGSF8RPSTHABg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=D08138FD1F41421E07EA629F41067D06E97D40FD0B2B6F2A5E85189944BA9A38)

从API version 7开始支持，从API version 9开始废弃，建议使用[@ohos.reminderAgentManager (后台代理提醒)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-reminderagentmanager)替代。

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import reminderAgent from'@ohos.reminderAgent';
```

#### reminderAgent.publishReminder(deprecated)

publishReminder(reminderReq: ReminderRequest, callback: AsyncCallback<number>): void

发布一个后台代理提醒，使用回调的方式实现异步调用，该方法需要申请通知弹窗权限[Notification.requestEnableNotification](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notification#notificationrequestenablenotification8)后才能调用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/4bNg6SK6QkmIwYkjbfKADg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=CF9F76F04AED859BF13EA504D910761F403E745522DE023FCDEBE19B7D7851BD)

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.publishReminder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-reminderagentmanager#reminderagentmanagerpublishreminder)替代。

**需要权限**：ohos.permission.PUBLISH\_AGENT\_REMINDER

**系统能力**：SystemCapability.Notification.ReminderAgent

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| reminderReq | [ReminderRequest](#reminderrequestdeprecated) | 是 | 需要发布的提醒实例。 |
| callback | AsyncCallback<number> | 是 | 异步回调，返回当前发布的提醒的id。 |

**示例**：

```ts
import { BusinessError } from '@ohos.base';

let timer:reminderAgent.ReminderRequestTimer = {
  reminderType: reminderAgent.ReminderType.REMINDER_TYPE_TIMER,
  triggerTimeInSeconds: 10
}

reminderAgent.publishReminder(timer, (err: BusinessError, reminderId: number) => {
  console.info("callback, reminderId = " + reminderId);
});
```

#### reminderAgent.publishReminder(deprecated)

publishReminder(reminderReq: ReminderRequest): Promise<number>

发布一个后台代理提醒，使用Promise方式实现异步调用，该方法需要申请通知弹窗权限[Notification.requestEnableNotification](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notification#notificationrequestenablenotification8)后才能调用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/KmS4HKBIQtevMkc12-U7DA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=CDA102DD387E3885E3A6FB45FCC6876C3FA66CF3D396EB145AFD1EA33B59FEB6)

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.publishReminder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-reminderagentmanager#reminderagentmanagerpublishreminder-1)替代。

**需要权限**：ohos.permission.PUBLISH\_AGENT\_REMINDER

**系统能力**：SystemCapability.Notification.ReminderAgent

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| reminderReq | [ReminderRequest](#reminderrequestdeprecated) | 是 | 需要发布的提醒实例。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | 返回提醒的Id。 |

**示例**：

```ts
let timer:reminderAgent.ReminderRequestTimer = {
  reminderType: reminderAgent.ReminderType.REMINDER_TYPE_TIMER,
  triggerTimeInSeconds: 10
}

reminderAgent.publishReminder(timer).then((reminderId: number) => {
  console.info("promise, reminderId = " + reminderId);
});
```

#### reminderAgent.cancelReminder(deprecated)

cancelReminder(reminderId: number, callback: AsyncCallback<void>): void

取消指定id的提醒，使用回调的方式实现异步调用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/3wkY4VJJRhSEnnR5TSmi-w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=E507B39CFF0FEE3B24A167D29D2EBF3E73F6C9AA058C971B1DDBB06752C66733)

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.cancelReminder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-reminderagentmanager#reminderagentmanagercancelreminder)替代。

**系统能力**： SystemCapability.Notification.ReminderAgent

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| reminderId | number | 是 | 目标reminder的id号。 |
| callback | AsyncCallback<void> | 是 | 异步回调。 |

**示例**：

```ts
import { BusinessError } from '@ohos.base';

reminderAgent.cancelReminder(1, (err: BusinessError, data: void) => {
  console.info("cancelReminder callback");
});
```

#### reminderAgent.cancelReminder(deprecated)

cancelReminder(reminderId: number): Promise<void>

取消指定id的提醒，使用Promise方式实现异步调用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/fyC4CQDxQzuVjZDW1-XWiw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=5868AF7452D299EA520F2509442F6CC1EF4084F0BAE2B443518D2E6E47209E19)

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.cancelReminder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-reminderagentmanager#reminderagentmanagercancelreminder-1)替代。

**系统能力**： SystemCapability.Notification.ReminderAgent

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| reminderId | number | 是 | 目标reminder的id号。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise类型异步回调。 |

**示例**：

```ts
reminderAgent.cancelReminder(1).then(() => {
    console.info("cancelReminder promise");
});
```

#### reminderAgent.getValidReminders(deprecated)

getValidReminders(callback: AsyncCallback<Array<ReminderRequest>>): void

获取当前应用已设置的所有有效（未过期）的提醒，使用回调的方式实现异步调用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/kCVU5nMyRcaFsKfnGgWMIg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=48C484578383B4E37BDF518FC4DFDB3153F9B30742260B37858C1D7783A644CB)

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.getValidReminders](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-reminderagentmanager#reminderagentmanagergetvalidreminders)替代。

**系统能力**： SystemCapability.Notification.ReminderAgent

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[ReminderRequest](#reminderrequestdeprecated)\>> | 是 | 异步回调，返回当前应用已设置的所有有效（未过期）的提醒。 |

**示例**：

```ts
import { BusinessError } from '@ohos.base';

reminderAgent.getValidReminders((err: BusinessError, reminders: Array<reminderAgent.ReminderRequest>) => {
  console.info("callback, getValidReminders length = " + reminders.length);
  for (let i = 0; i < reminders.length; i++) {
    console.info("getValidReminders = " + reminders[i]);
    console.info("getValidReminders, reminderType = " + reminders[i].reminderType);
    const actionButton = reminders[i].actionButton || [];
    for (let j = 0; j < actionButton.length; j++) {
      console.info("getValidReminders, actionButton.title = " + actionButton[j]?.title);
      console.info("getValidReminders, actionButton.type = " + actionButton[j]?.type);
    }
    console.info("getValidReminders, wantAgent.pkgName = " + reminders[i].wantAgent?.pkgName);
    console.info("getValidReminders, wantAgent.abilityName = " + reminders[i].wantAgent?.abilityName);
    console.info("getValidReminders, ringDuration = " + reminders[i].ringDuration);
    console.info("getValidReminders, snoozeTimes = " + reminders[i].snoozeTimes);
    console.info("getValidReminders, timeInterval = " + reminders[i].timeInterval);
    console.info("getValidReminders, title = " + reminders[i].title);
    console.info("getValidReminders, content = " + reminders[i].content);
    console.info("getValidReminders, expiredContent = " + reminders[i].expiredContent);
    console.info("getValidReminders, snoozeContent = " + reminders[i].snoozeContent);
    console.info("getValidReminders, notificationId = " + reminders[i].notificationId);
    console.info("getValidReminders, slotType = " + reminders[i].slotType);
  }
})
```

#### reminderAgent.getValidReminders(deprecated)

getValidReminders(): Promise<Array<ReminderRequest>>

获取当前应用已设置的所有有效（未过期）的提醒，使用Promise方式实现异步调用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/42MEHcRVTimdaUAUeDO1yg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=F8FC476A3301485D312BA314B9DCB7AB5F5F15BC3A0BBFEE72F5B7908BA1B050)

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.getValidReminders](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-reminderagentmanager#reminderagentmanagergetvalidreminders-1)替代。

**系统能力**： SystemCapability.Notification.ReminderAgent

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<[ReminderRequest](#reminderrequestdeprecated)\>> | 返回当前应用已设置的所有有效（未过期）的提醒。 |

**示例**：

```ts
reminderAgent.getValidReminders().then((reminders: Array<reminderAgent.ReminderRequest>) => {
  console.info("promise, getValidReminders length = " + reminders.length);
  for (let i = 0; i < reminders.length; i++) {
    console.info("getValidReminders = " + reminders[i]);
    console.info("getValidReminders, reminderType = " + reminders[i].reminderType);
    const actionButton = reminders[i].actionButton || [];
    for (let j = 0; j < actionButton.length; j++) {
      console.info("getValidReminders, actionButton.title = " + actionButton[j]?.title);
      console.info("getValidReminders, actionButton.type = " + actionButton[j]?.type);
    }
    console.info("getValidReminders, wantAgent.pkgName = " + reminders[i].wantAgent?.pkgName);
    console.info("getValidReminders, wantAgent.abilityName = " + reminders[i].wantAgent?.abilityName);
    console.info("getValidReminders, ringDuration = " + reminders[i].ringDuration);
    console.info("getValidReminders, snoozeTimes = " + reminders[i].snoozeTimes);
    console.info("getValidReminders, timeInterval = " + reminders[i].timeInterval);
    console.info("getValidReminders, title = " + reminders[i].title);
    console.info("getValidReminders, content = " + reminders[i].content);
    console.info("getValidReminders, expiredContent = " + reminders[i].expiredContent);
    console.info("getValidReminders, snoozeContent = " + reminders[i].snoozeContent);
    console.info("getValidReminders, notificationId = " + reminders[i].notificationId);
    console.info("getValidReminders, slotType = " + reminders[i].slotType);
  }
})
```

#### reminderAgent.cancelAllReminders(deprecated)

cancelAllReminders(callback: AsyncCallback<void>): void

取消当前应用所有的提醒，使用回调的方式实现异步调用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/Xz4-anC7R8GWYKMO7xh1KQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=2C77088E3523CB73D7E0F9AD565844207B99BBF301C6A0DA9F073A384303A70E)

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.cancelAllReminders](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-reminderagentmanager#reminderagentmanagercancelallreminders)替代。

**系统能力**： SystemCapability.Notification.ReminderAgent

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | 是 | 异步回调。 |

**示例**：

```ts
import { BusinessError } from '@ohos.base';

reminderAgent.cancelAllReminders((err: BusinessError, data: void) =>{
  console.info("cancelAllReminders callback")
})
```

#### reminderAgent.cancelAllReminders(deprecated)

cancelAllReminders(): Promise<void>

取消当前应用所有的提醒，使用Promise方式实现异步调用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/1OBCbAflT5aRktV1JIecMQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=0E78B254B4B68928A487080C253A7825FCAF4511B1ABC48DF48536E37D00AC1B)

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.cancelAllReminders](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-reminderagentmanager#reminderagentmanagercancelallreminders-1)替代。

**系统能力**： SystemCapability.Notification.ReminderAgent

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise类型异步回调。 |

**示例**：

```ts
reminderAgent.cancelAllReminders().then(() => {
    console.info("cancelAllReminders promise")
})
```

#### reminderAgent.addNotificationSlot(deprecated)

addNotificationSlot(slot: NotificationSlot, callback: AsyncCallback<void>): void

添加一个NotificationSlot，使用回调的方式实现异步调用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/cAtvVjnSTGCJ_FWWE_ZN-w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=290F7CCD6710FA0821B5F5F66CF74001DB4CB91A52E5B1C251D5BB9A29A89BBB)

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.addNotificationSlot](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-reminderagentmanager#reminderagentmanageraddnotificationslot)替代。

**系统能力**： SystemCapability.Notification.ReminderAgent

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| slot | [NotificationSlot](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notification#notificationslot) | 是 | notification.slot实例，仅支持设置其type属性。 |
| callback | AsyncCallback<void> | 是 | 异步回调。 |

**示例**：

```ts
import notification from '@ohos.notificationManager'
import { BusinessError } from '@ohos.base';

let mySlot:notification.NotificationSlot = {
  type: notification.SlotType.SOCIAL_COMMUNICATION
}
reminderAgent.addNotificationSlot(mySlot, (err: BusinessError, data: void) => {
  console.info("addNotificationSlot callback");
});
```

#### reminderAgent.addNotificationSlot(deprecated)

addNotificationSlot(slot: NotificationSlot): Promise<void>

添加一个NotificationSlot，使用Promise方式实现异步调用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/qiffLxx2S8-nYV6JnRfNAQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=CD55725706248FDBE9A4329E1FCA819D4F98F4F3F23C7A1B22709DE45021EBFE)

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.addNotificationSlot](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-reminderagentmanager#reminderagentmanageraddnotificationslot-1)替代。

**系统能力**： SystemCapability.Notification.ReminderAgent

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| slot | [NotificationSlot](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notification#notificationslot) | 是 | notification.slot实例，仅支持设置其type属性。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise类型异步回调。 |

**示例**：

```ts
import notification from '@ohos.notificationManager'

let mySlot:notification.NotificationSlot = {
  type: notification.SlotType.SOCIAL_COMMUNICATION
}
reminderAgent.addNotificationSlot(mySlot).then(() => {
  console.info("addNotificationSlot promise");
});
```

#### reminderAgent.removeNotificationSlot(deprecated)

removeNotificationSlot(slotType: notification.SlotType, callback: AsyncCallback<void>): void

删除目标NotificationSlot，使用callback方式实现异步调用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/Xxoy1WT8TVmF1G5ClGdczw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=D71900D4950F765BE8442AD1E451424BDCF729E99D62872454F9A28B261A8D29)

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.removeNotificationSlot](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-reminderagentmanager#reminderagentmanagerremovenotificationslot)替代。

**系统能力**：SystemCapability.Notification.ReminderAgent

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| slotType | [notification.SlotType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notification#slottype) | 是 | 目标notification.slot的类型。 |
| callback | AsyncCallback<void> | 是 | 异步回调。 |

**示例**：

```ts
import notification from '@ohos.notification'
import { BusinessError } from '@ohos.base';

reminderAgent.removeNotificationSlot(notification.SlotType.CONTENT_INFORMATION, (err: BusinessError, data: void) => {
  console.info("removeNotificationSlot callback");
});
```

#### reminderAgent.removeNotificationSlot(deprecated)

removeNotificationSlot(slotType: notification.SlotType): Promise<void>

删除目标NotificationSlot，使用Promise方式实现异步调用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/jiTLAApZQVO9TDtn9vIzSQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=D93690DB3E138FEF85A03A41E616AFBE85B008BF3E65EB41516752BDBE4CEACF)

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.removeNotificationSlot](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-reminderagentmanager#reminderagentmanagerremovenotificationslot-1)替代。

**系统能力**：SystemCapability.Notification.ReminderAgent

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| slotType | [notification.SlotType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notification#slottype) | 是 | 目标notification.slot的类型。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise类型异步回调。 |

**示例**：

```ts
import notification from '@ohos.notification'

reminderAgent.removeNotificationSlot(notification.SlotType.CONTENT_INFORMATION).then(() => {
    console.info("removeNotificationSlot promise");
});
```

#### ActionButtonType(deprecated)

按钮的类型。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/5aY0nmitS0O--InhqXDVmA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=DF2A3FB8DE9F4190D1206422A1AE8129B7D6084C1CF54231DB50D91D05B20CA8)

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.ActionButtonType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-reminderagentmanager#actionbuttontype)替代。

**系统能力**：SystemCapability.Notification.ReminderAgent

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| ACTION\_BUTTON\_TYPE\_CLOSE | 0 | 表示关闭提醒的按钮。 |
| ACTION\_BUTTON\_TYPE\_SNOOZE | 1 | 表示延迟提醒的按钮。 |

#### ReminderType(deprecated)

提醒的类型。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/SEPuQgn6RIGQz4zCp3KyVw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=DD8A311C5C4A2FADB7B65E3CFFB4B67F3112D5DC17AFDBD21706A91E9E5832F6)

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.ReminderType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-reminderagentmanager#remindertype)替代。

**系统能力**：SystemCapability.Notification.ReminderAgent

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| REMINDER\_TYPE\_TIMER | 0 | 表示提醒类型：倒计时。 |
| REMINDER\_TYPE\_CALENDAR | 1 | 表示提醒类型：日历。 |
| REMINDER\_TYPE\_ALARM | 2 | 表示提醒类型：闹钟。 |

#### ActionButton(deprecated)

用于设置弹出的提醒通知信息上显示的按钮类型和标题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/ut4j7eQeQbSYcf_FUaxg-A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=4877D21CDB03FE59B9D19418672F9943223F45DE3CA129B2467BD2C9646C0361)

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.ActionButton](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-reminderagentmanager#actionbutton)替代。

**系统能力**：SystemCapability.Notification.ReminderAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| title | string | 否 | 否 | 按钮显示的标题。 |
| type | [ActionButtonType](#actionbuttontypedeprecated) | 否 | 否 | 按钮的类型。 |

#### WantAgent(deprecated)

点击提醒通知后跳转的目标ability信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/TtzInMQ6RFWcmpej9vcFHA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=306D0C56E7A183C47E413E511524B616BAB70D9AD2B9922E762825660E76B2DE)

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.WantAgent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-reminderagentmanager#wantagent)替代。

**系统能力**：SystemCapability.Notification.ReminderAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| pkgName | string | 否 | 否 | 指明点击提醒通知栏后跳转的目标HAP名。 |
| abilityName | string | 否 | 否 | 指明点击提醒通知栏后跳转的目标ability名称。 |

#### MaxScreenWantAgent(deprecated)

全屏显示提醒到达时自动拉起的目标ability信息，该接口预留。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/TBw9VOI0QFCrLb860qROKQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=1FBA22FD94E4ED99DF46FE3F95B383A2D69F6AB68AE10FF975BC1AD957A5520B)

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.MaxScreenWantAgent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-reminderagentmanager#maxscreenwantagent)替代。

**系统能力**：SystemCapability.Notification.ReminderAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| pkgName | string | 否 | 否 | 指明提醒到达时自动拉起的目标HAP名（如果设备在使用中，则只弹出通知横幅框）。 |
| abilityName | string | 否 | 否 | 指明提醒到达时自动拉起的目标ability名（如果设备在使用中，则只弹出通知横幅框）。 |

#### ReminderRequest(deprecated)

提醒实例对象，用于设置提醒类型、响铃时长等具体信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/0vQlP4aFTj2Ua879EcbKlA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=63AE870E3B91805F4263B99D1922ED3A43DE1FA8C3134ED877303D0832D2EC38)

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.ReminderRequest](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-reminderagentmanager#reminderrequest)替代。

**系统能力**：SystemCapability.Notification.ReminderAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| reminderType | [ReminderType](#remindertypedeprecated) | 否 | 否 | 指明提醒类型。 |
| actionButton | \[[ActionButton](#actionbuttondeprecated)?, [ActionButton](#actionbuttondeprecated)?\] | 否 | 是 | 弹出的提醒通知栏中显示的按钮（参数可选，支持0/1/2个按钮）。 |
| wantAgent | WantAgent | 否 | 是 | 点击通知后需要跳转的目标ability信息。 |
| maxScreenWantAgent | [MaxScreenWantAgent](#maxscreenwantagentdeprecated) | 否 | 是 | 提醒到达时跳转的目标包。如果设备正在使用中，则弹出一个通知框。 |
| ringDuration | number | 否 | 是 | 指明响铃时长（单位：秒），默认1秒。 |
| snoozeTimes | number | 否 | 是 | 指明延迟提醒次数，默认0次。 |
| timeInterval | number | 否 | 是 | 执行延迟提醒间隔（单位：秒），默认0秒。 |
| title | string | 否 | 是 | 指明提醒标题。 |
| content | string | 否 | 是 | 指明提醒内容。 |
| expiredContent | string | 否 | 是 | 指明提醒过期后需要显示的内容。 |
| snoozeContent | string | 否 | 是 | 指明延迟提醒时需要显示的内容。 |
| notificationId | number | 否 | 是 | 指明提醒使用的通知的id号，相同id号的提醒会覆盖。 |
| slotType | [notification.SlotType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notification#slottype) | 否 | 是 | 指明提醒的slot类型。 |

#### ReminderRequestCalendar(deprecated)

日历实例对象，用于设置提醒的时间。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/vXQFcfZ-T4yXaWy6iwKz2g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=ACEFF0ABB372EC44E61A1E880E2F4F41BA8407BF511617726CC76F4E08B95361)

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.ReminderRequestCalendar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-reminderagentmanager#reminderrequestcalendar)替代。

**系统能力**：SystemCapability.Notification.ReminderAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| dateTime | [LocalDateTime](#localdatetimedeprecated) | 否 | 否 | 指明提醒的目标时间。 |
| repeatMonths | Array<number> | 否 | 是 | 指明重复提醒的月份。 |
| repeatDays | Array<number> | 否 | 是 | 指明重复提醒的日期。 |

#### ReminderRequestAlarm(deprecated)

闹钟实例对象，用于设置提醒的时间。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/r0XjrjyVSPmPQJhY42bRhA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=6868031D022214F5662C31C1B10EA469C7195151E3C7E8565A4BF96FC91F54C9)

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.ReminderRequestAlarm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-reminderagentmanager#reminderrequestalarm)替代。

**系统能力**：SystemCapability.Notification.ReminderAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| hour | number | 否 | 否 | 指明提醒的目标时刻。 |
| minute | number | 否 | 否 | 指明提醒的目标分钟。 |
| daysOfWeek | Array<number> | 否 | 是 | 指明每周哪几天需要重复提醒。范围为周一到周末，对应数字为1到7。 |

#### ReminderRequestTimer(deprecated)

倒计时实例对象，用于设置提醒的时间。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/dyDOk4YaTEu5JWsNkiPz-g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=3A3702BE1FA8C06CB4D3C0060EE6149AA5009C101492202C2C2C8BEC062EA7D3)

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.ReminderRequestTimer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-reminderagentmanager#reminderrequesttimer)替代。

**系统能力**：SystemCapability.Notification.ReminderAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| triggerTimeInSeconds | number | 否 | 否 | 指明倒计时的秒数。 |

#### LocalDateTime(deprecated)

用于日历类提醒设置时指定时间信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/JUxKd4tFT7as-Eum_LWzdw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=C1778AE94E880ECD4D453982625DA1D1CF88F57C177A6E78874637BE5A8C0586)

从 API version 7开始支持，从API version 9开始废弃。建议使用[reminderAgentManager.LocalDateTime](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-reminderagentmanager#localdatetime)替代。

**系统能力**：SystemCapability.Notification.ReminderAgent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| year | number | 否 | 否 | 年 |
| month | number | 否 | 否 | 月 |
| day | number | 否 | 否 | 日 |
| hour | number | 否 | 否 | 时 |
| minute | number | 否 | 否 | 分 |
| second | number | 否 | 是 | 秒 |

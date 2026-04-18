---
title: "@ohos.application.NotificationSubscriberExtensionAbility (通知订阅扩展能力)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notificationsubscriberextensionability"
menu_path:
  - "参考"
  - "应用服务"
  - "Notification Kit（用户通知服务）"
  - "ArkTS API"
  - "@ohos.application.NotificationSubscriberExtensionAbility (通知订阅扩展能力)"
captured_at: "2026-04-17T01:49:00.382Z"
---

# @ohos.application.NotificationSubscriberExtensionAbility (通知订阅扩展能力)

NotificationSubscriberExtensionAbility 是通知订阅者扩展能力的基类，提供通知订阅的相关功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/_GClaWxJT8CMziJGFjNCYQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014900Z&HW-CC-Expire=86400&HW-CC-Sign=DCBBBF16BEA9B3EAB41A5D55814E0E59316A8DE087BDC08A35F08B2DFCC3B668)

本模块首批接口从API version 22开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ts
import { notificationExtensionSubscription, NotificationSubscriberExtensionAbility } from '@kit.NotificationKit';
```

#### NotificationSubscriberExtensionAbility

**系统能力**：SystemCapability.Notification.Notification

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| context | [NotificationSubscriberExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notificationsubscriberextensioncontext) | 否 | 否 | NotificationSubscriberExtensionAbility的上下文环境。 |

#### \[h2\]onDestroy

onDestroy(): void

通知订阅扩展被销毁时的回调。

**系统能力**：SystemCapability.Notification.Notification

**示例：**

```ts
const TAG = 'NotificationSubscriberExtAbility';

export default class NotificationSubscriberExtAbility extends NotificationSubscriberExtensionAbility {
  onDestroy(): void {
    console.info(`${TAG} onDestroy`);
  }
}
```

#### \[h2\]onReceiveMessage

onReceiveMessage(notificationInfo: NotificationInfo): void

收到通知时回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| notificationInfo | [NotificationInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-notification-notificationinfo) | 是 | 通知订阅扩展能力中[onReceiveMessage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notificationsubscriberextensionability#onreceivemessage)回调的通知信息。 |

**示例：**

```ts
const TAG = 'NotificationSubscriberExtAbility';

export default class NotificationSubscriberExtAbility extends NotificationSubscriberExtensionAbility {
  onReceiveMessage(notificationInfo: notificationExtensionSubscription.NotificationInfo): void {
    console.info(`${TAG} onReceiveMessage. notificationInfo: ${JSON.stringify(notificationInfo)}`);
  }
}
```

#### \[h2\]onCancelMessages

onCancelMessages(hashCodes: Array<string>): void

取消通知时的回调。

**系统能力**：SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| hashCodes | Array<string> | 是 | 要取消的通知的哈希码列表。 |

**示例：**

```ts
const TAG = 'NotificationSubscriberExtAbility';

export default class NotificationSubscriberExtAbility extends NotificationSubscriberExtensionAbility {
  onCancelMessages(hashCodes: Array<string>): void {
    console.info(`${TAG} onCancelMessages. hashCodes: ${JSON.stringify(hashCodes)}`);
  }
}
```

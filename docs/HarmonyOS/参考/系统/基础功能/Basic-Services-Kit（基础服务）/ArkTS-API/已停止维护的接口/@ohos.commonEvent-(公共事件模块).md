---
title: "@ohos.commonEvent (公共事件模块)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-commonevent"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "Basic Services Kit（基础服务）"
  - "ArkTS API"
  - "已停止维护的接口"
  - "@ohos.commonEvent (公共事件模块)"
captured_at: "2026-04-17T01:48:28.422Z"
---

# @ohos.commonEvent (公共事件模块)

本模块提供了公共事件的能力，包括公共事件的权限列表，发布公共事件，订阅或取消订阅公共事件，获取或修改公共事件结果代码、结果数据等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/wcQOy6EwSayNEcgwXoIc2A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=F7EE14257889D2B55C3C3AFB095A9362C06F2FBFA89A05D717D28CC2E53593B0)

-   从API Version 9开始，该接口不再维护，推荐使用新接口[@ohos.commonEventManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-commoneventmanager)。
    
-   本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
    

#### 导入模块

```ts
import commonEvent from '@ohos.commonEvent';
```

#### Support

系统公共事件是指由系统服务或系统应用发布的事件，订阅这些系统公共事件需要特定的权限。发布或订阅这些事件需要使用如下链接中的枚举定义。

全部系统公共事件枚举定义请参见[系统公共事件定义](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/commonevent-definitions)。

#### commonEvent.publish(deprecated)

publish(event: string, callback: AsyncCallback<void>): void

发布公共事件（回调形式）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/HJJELjbDTimTrjhCGlhuIg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=F9FB1BCF440E1ABEEE8C8FC6016B63A6987296463A409E8900E970C82433BBF1)

从 API version 7开始支持，从API version 9开始废弃。建议使用[commonEventManager.publish](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-commoneventmanager#commoneventmanagerpublish)替代。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| event | string | 是 | 表示要发送的公共事件。 |
| callback | AsyncCallback<void> | 是 | 表示指定的回调方法。 |

**示例：**

```ts
import Base from '@ohos.base';

//发布公共事件回调
function publishCB(err:Base.BusinessError) {
    if (err.code) {
        console.error(`publish failed, code is ${err.code}`);
    } else {
        console.info("publish");
    }
}

//发布公共事件
commonEvent.publish("event", publishCB);
```

#### commonEvent.publish(deprecated)

publish(event: string, options: CommonEventPublishData, callback: AsyncCallback<void>): void

以回调的形式发布公共事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/vYewBFzkSk-Bi9qcUdPItg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=3BC9329C1B95BFFFC54D3550B1A6B65871C319C781EDF1424F872B566984B0A7)

从 API version 7开始支持，从API version 9开始废弃。建议使用[commonEventManager.publish](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-commoneventmanager#commoneventmanagerpublish-1)替代。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| event | string | 是 | 表示要发布的公共事件。 |
| options | [CommonEventPublishData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-commonevent-commoneventpublishdata) | 是 | 表示发布公共事件的属性。 |
| callback | AsyncCallback<void> | 是 | 表示指定的回调方法。 |

**示例：**

```ts
import Base from '@ohos.base';
import CommonEventManager from '@ohos.commonEventManager';

//公共事件相关信息
let options:CommonEventManager.CommonEventPublishData = {
    code: 0,             //公共事件的初始代码
    data: "initial data",//公共事件的初始数据
    isOrdered: true  //有序公共事件
}

//发布公共事件回调
function publishCB(err:Base.BusinessError) {
    if (err.code) {
        console.error(`publish failed, code is ${err.code}`);
    } else {
        console.info("publish");
    }
}

//发布公共事件
commonEvent.publish("event", options, publishCB);
```

#### commonEvent.createSubscriber(deprecated)

createSubscriber(subscribeInfo: CommonEventSubscribeInfo, callback: AsyncCallback<CommonEventSubscriber>): void

以回调形式创建订阅者。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/oROglCGYR2Cd6fQ43JBeBQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=FB2A83E1C5712AB75F3A10EAC012E8C3DFCDD50D751ABD7AB53C03E76EFE3B81)

从 API version 7开始支持，从API version 9开始废弃。建议使用[commonEventManager.createSubscriber](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-commoneventmanager#commoneventmanagercreatesubscriber)替代。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| subscribeInfo | [CommonEventSubscribeInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-commonevent-commoneventsubscribeinfo) | 是 | 表示订阅信息。 |
| callback | AsyncCallback<[CommonEventSubscriber](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-commonevent-commoneventsubscriber)\> | 是 | 表示创建订阅者的回调方法。 |

**示例：**

```ts
import Base from '@ohos.base';
import CommonEventManager from '@ohos.commonEventManager';

let subscriber:CommonEventManager.CommonEventSubscriber; // 用于保存创建成功的订阅者对象，后续使用其完成订阅及退订的动作

// 订阅者信息
let subscribeInfo:CommonEventManager.CommonEventSubscribeInfo = {
    events: ["event"]
};

// 创建订阅者回调
function createCB(err:Base.BusinessError, commonEventSubscriber:CommonEventManager.CommonEventSubscriber) {
    if (err.code) {
        console.error(`createSubscriber failed, code is ${err.code}`);
    } else {
        console.info("createSubscriber");
        subscriber = commonEventSubscriber;
    }
}

// 创建订阅者
commonEvent.createSubscriber(subscribeInfo, createCB);
```

#### commonEvent.createSubscriber(deprecated)

createSubscriber(subscribeInfo: CommonEventSubscribeInfo): Promise<CommonEventSubscriber>

以Promise形式创建订阅者。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/2uAEIosqTKimNy-k1S2oWw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=4B61E601505E34DB2496EA769520671777C1E12BFA8DB0C05B2EF2535E45369A)

从 API version 7开始支持，从API version 9开始废弃。建议使用[commonEventManager.createSubscriber](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-commoneventmanager#commoneventmanagercreatesubscriber-1)替代。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| subscribeInfo | [CommonEventSubscribeInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-commonevent-commoneventsubscribeinfo) | 是 | 表示订阅信息。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[CommonEventSubscriber](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-commonevent-commoneventsubscriber)\> | 返回订阅者对象。 |

**示例：**

```ts
import Base from '@ohos.base';
import CommonEventManager from '@ohos.commonEventManager';

let subscriber:CommonEventManager.CommonEventSubscriber; // 用于保存创建成功的订阅者对象，后续使用其完成订阅及退订的动作

// 订阅者信息
let subscribeInfo:CommonEventManager.CommonEventSubscribeInfo = {
    events: ["event"]
};

// 创建订阅者
commonEvent.createSubscriber(subscribeInfo).then((commonEventSubscriber:CommonEventManager.CommonEventSubscriber) => {
    console.info("createSubscriber");
    subscriber = commonEventSubscriber;
}).catch((err:Base.BusinessError) => {
    console.error(`createSubscriber failed, code is ${err.code}`);
});
```

#### commonEvent.subscribe(deprecated)

subscribe(subscriber: CommonEventSubscriber, callback: AsyncCallback<CommonEventData>): void

以回调形式订阅公共事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/hN332AOgQGqboekay_5Ywg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=908BBD3261B5DA1FECBD75311F0418B253FA9B28800AD054A52E08083D72BF60)

从 API version 7开始支持，从API version 9开始废弃。建议使用[commonEventManager.subscribe](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-commoneventmanager#commoneventmanagersubscribe)替代。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| subscriber | [CommonEventSubscriber](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-commonevent-commoneventsubscriber) | 是 | 表示订阅者对象。 |
| callback | AsyncCallback<[CommonEventData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-commonevent-commoneventdata)\> | 是 | 表示接收公共事件数据的回调函数。 |

**示例：**

```ts
import Base from '@ohos.base';
import CommonEventManager from '@ohos.commonEventManager';

let subscriber:CommonEventManager.CommonEventSubscriber;// 用于保存创建成功的订阅者对象，后续使用其完成订阅及退订的动作

// 订阅者信息
let subscribeInfo:CommonEventManager.CommonEventSubscribeInfo = {
    events: ["event"]
};

// 订阅公共事件回调
function subscribeCB(err:Base.BusinessError, data:CommonEventManager.CommonEventData) {
    if (err.code) {
        console.error(`subscribe failed, code is ${err.code}`);
    } else {
        console.info("subscribe " + JSON.stringify(data));
    }
}

// 创建订阅者回调
function createCB(err:Base.BusinessError, commonEventSubscriber:CommonEventManager.CommonEventSubscriber) {
    if (err.code) {
        console.error(`createSubscriber failed, code is ${err.code}`);
    } else {
        console.info("createSubscriber");
        subscriber = commonEventSubscriber;
        // Subscribe to a common event.
        commonEvent.subscribe(subscriber, subscribeCB);
    }
}

// 创建订阅者
commonEvent.createSubscriber(subscribeInfo, createCB);
```

#### commonEvent.unsubscribe(deprecated)

unsubscribe(subscriber: CommonEventSubscriber, callback?: AsyncCallback<void>): void

以回调形式取消订阅公共事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/f8LhJuTGTQelaPnWw8449A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=8954AFD5CCC2C0EE1C57E2188951724A41BCEE382AAB88E4D383836CE7B65510)

从 API version 7开始支持，从API version 9开始废弃。建议使用[commonEventManager.unsubscribe](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-commoneventmanager#commoneventmanagerunsubscribe)替代。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| subscriber | [CommonEventSubscriber](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-commonevent-commoneventsubscriber) | 是 | 表示订阅者对象。 |
| callback | AsyncCallback<void> | 否 | 表示取消订阅的回调方法。 |

**示例：**

```ts
import Base from '@ohos.base';
import CommonEventManager from '@ohos.commonEventManager';

let subscriber:CommonEventManager.CommonEventSubscriber;    // 用于保存创建成功的订阅者对象，后续使用其完成订阅及退订的动作

// 订阅者信息
let subscribeInfo:CommonEventManager.CommonEventSubscribeInfo = {
    events: ["event"]
};

// 订阅公共事件回调
function subscribeCB(err:Base.BusinessError, data:CommonEventManager.CommonEventData) {
    if (err.code) {
        console.error(`subscribe failed, code is ${err.code}`);
    } else {
        console.info("subscribe " + JSON.stringify(data));
    }
}

// 创建订阅者回调
function createCB(err:Base.BusinessError, commonEventSubscriber:CommonEventManager.CommonEventSubscriber) {
    if (err.code) {
        console.error(`createSubscriber failed, code is ${err.code}`);
    } else {
        console.info("createSubscriber");
        subscriber = commonEventSubscriber;
        // Subscribe to a common event.
        commonEvent.subscribe(subscriber, subscribeCB);
    }
}

// 取消订阅公共事件回调
function unsubscribeCB(err:Base.BusinessError) {
    if (err.code) {
        console.error(`unsubscribe failed, code is ${err.code}`);
    } else {
        console.info("unsubscribe");
    }
}

// 创建订阅者
commonEvent.createSubscriber(subscribeInfo, createCB);

// 取消订阅公共事件
commonEvent.unsubscribe(subscriber, unsubscribeCB);
```

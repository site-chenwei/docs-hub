---
title: "ExtensionAbility如何与主进程通信"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-35"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "程序框架"
  - "程序框架（Ability）"
  - "ExtensionAbility如何与主进程通信"
captured_at: "2026-04-17T02:02:58.851Z"
---

# ExtensionAbility如何与主进程通信

实现步骤：

ExtensionAbility端发布事件：

import { commonEventManager } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Publish public event callbacks
function publishCB(err: BusinessError) {
  if (err) {
    console.error(\`Failed to publish common event. Code is ${err.code}, message is ${err.message}\`);
  } else {
    console.info(\`Succeeded in publishing common event.\`);
  }
}
// Publish public events
try {
  commonEventManager.publish("event", publishCB);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(\`Failed to publish common event. Code is ${err.code}, message is ${err.message}\`);
}

主进程端订阅事件：

import { BusinessError } from '@kit.BasicServicesKit';
import { commonEventManager } from '@kit.BasicServicesKit';

// Define subscribers to save successfully created subscriber objects, which can be used to complete subscription and unsubscribe actions in the future
let subscriber: commonEventManager.CommonEventSubscriber;
// Subscriber information
let subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
  events: \["event"\]
};
// Subscribe to public event callbacks
function SubscribeCB(err: BusinessError, data: commonEventManager.CommonEventData) {
  if (err) {
    console.error(\`Failed to subscribe. Code is ${err.code}, message is ${err.message}\`);
  } else {
    console.info(\`Succeeded in subscribing, data is \` + JSON.stringify(data));
  }
}
// Create subscriber callback
function createCB(err: BusinessError, commonEventSubscriber: commonEventManager.CommonEventSubscriber) {
  if(!err) {
    console.info(\`Succeeded in creating subscriber.\`);
    subscriber = commonEventSubscriber;
    // Subscribe to public events
    try {
      commonEventManager.subscribe(subscriber, SubscribeCB);
    } catch (error) {
      let err: BusinessError = error as BusinessError;
      console.error(\`Failed to subscribe. Code is ${err.code}, message is ${err.message}\`);
    }
  } else {
    console.error(\`Failed to create subscriber. Code is ${err.code}, message is ${err.message}\`);
  }
}
// Create subscribers
try {
  commonEventManager.createSubscriber(subscribeInfo, createCB);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(\`Failed to create subscriber. Code is ${err.code}, message is ${err.message}\`);
}

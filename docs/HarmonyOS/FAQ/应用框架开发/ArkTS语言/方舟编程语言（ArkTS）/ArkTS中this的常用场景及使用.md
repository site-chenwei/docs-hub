---
title: "ArkTS中this的常用场景及使用"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-55"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "ArkTS语言"
  - "方舟编程语言（ArkTS）"
  - "ArkTS中this的常用场景及使用"
captured_at: "2026-04-17T02:03:00.052Z"
---

# ArkTS中this的常用场景及使用

在ArkTS中，this 用于类中访问对象属性和方法，或在自定义组件的回调中使用UIContext.getHostContext(this)。

-   类中使用 this，this 实际指向实例化后的对象。
    
    class UserInfo {
      name: string = 'xxx';
    
      getName() {
        return this.name;
      }
    }
    
    const user: UserInfo = new UserInfo();
    
-   在自定义组件中使用 this，通常是在回调事件中，此时 this 指向自定义组件本身。常用的方法是通过UIContext.getHostContext(this)获取上下文。

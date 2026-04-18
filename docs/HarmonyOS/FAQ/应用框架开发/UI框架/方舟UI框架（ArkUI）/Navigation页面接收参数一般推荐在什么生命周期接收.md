---
title: "Navigation页面接收参数一般推荐在什么生命周期接收"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-419"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "UI框架"
  - "方舟UI框架（ArkUI）"
  - "Navigation页面接收参数一般推荐在什么生命周期接收"
captured_at: "2026-04-17T02:03:07.353Z"
---

# Navigation页面接收参数一般推荐在什么生命周期接收

-   页面新创建时，推荐在NavDestination的[onReady](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination#onready11)生命周期中处理参数。
-   API18及以下版本，单实例跳转场景需要开发者自行管理参数。
-   当同时实现onReady和onNewParam时，API version 9及以上版本会优先触发[onNewParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination#onnewparam19)回调。

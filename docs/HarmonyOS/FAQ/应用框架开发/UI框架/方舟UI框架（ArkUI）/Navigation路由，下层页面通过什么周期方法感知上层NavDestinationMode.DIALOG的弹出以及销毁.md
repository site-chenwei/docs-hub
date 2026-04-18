---
title: "Navigation路由，下层页面通过什么周期方法感知上层NavDestinationMode.DIALOG的弹出以及销毁"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-407"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "UI框架"
  - "方舟UI框架（ArkUI）"
  - "Navigation路由，下层页面通过什么周期方法感知上层NavDestinationMode.DIALOG的弹出以及销毁"
captured_at: "2026-04-17T02:03:07.200Z"
---

# Navigation路由，下层页面通过什么周期方法感知上层NavDestinationMode.DIALOG的弹出以及销毁

开发者可以使用observer对navDestination的生命周期进行统一管理，可参考：[on('navDestinationUpdate')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uiobserver#onnavdestinationupdate11)。

从API17开始，新增[onActive](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination#onactive17)、[onInactive](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination#oninactive17)生命周期，dialog销毁、弹出时会分别触发下层页面的onActive、onInactive生命周期。

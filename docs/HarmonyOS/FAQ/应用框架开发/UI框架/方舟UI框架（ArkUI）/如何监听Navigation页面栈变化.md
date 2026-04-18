---
title: "如何监听Navigation页面栈变化"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-414"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "UI框架"
  - "方舟UI框架（ArkUI）"
  - "如何监听Navigation页面栈变化"
captured_at: "2026-04-17T02:03:07.258Z"
---

# 如何监听Navigation页面栈变化

通过[uiObserver.on('navDestinationSwitch')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-observer#uiobserveronnavdestinationswitch12-1)方法，可以监听Navigation的页面切换事件，当Navigation组件发生页面跳转时触发该事件，典型场景包括页面访问统计、页面生命周期管理等。

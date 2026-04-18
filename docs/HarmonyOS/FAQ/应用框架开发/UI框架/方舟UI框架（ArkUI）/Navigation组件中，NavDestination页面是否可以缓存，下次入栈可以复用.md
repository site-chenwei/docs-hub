---
title: "Navigation组件中，NavDestination页面是否可以缓存，下次入栈可以复用"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-404"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "UI框架"
  - "方舟UI框架（ArkUI）"
  - "Navigation组件中，NavDestination页面是否可以缓存，下次入栈可以复用"
captured_at: "2026-04-17T02:03:07.122Z"
---

# Navigation组件中，NavDestination页面是否可以缓存，下次入栈可以复用

**问题描述**

NavDestination是否有缓存页面的功能，每次pushStack后都要刷新页面。

**解决措施**

NavDestination不支持缓存功能，页面出栈后会被销毁。

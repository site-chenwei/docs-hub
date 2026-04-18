---
title: "AppStorage是否支持线程间共享对象，如果不支持，推荐替代方案是什么"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-49"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "UI框架"
  - "方舟UI框架（ArkUI）"
  - "AppStorage是否支持线程间共享对象，如果不支持，推荐替代方案是什么"
captured_at: "2026-04-17T02:03:03.300Z"
---

# AppStorage是否支持线程间共享对象，如果不支持，推荐替代方案是什么

AppStorage 支持应用主线程中多个 UIAbility 实例之间的状态共享。AppStorage 是与 UI 相关的数据，必须在 UI 线程中运行，无法与其他线程共享。当前没有替代方案。

**参考链接**

[AppStorage：应用全局的UI状态存储](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-appstorage)

---
title: "使用Web组件，在哪个回调事件中可以设置自定义用户代理"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-62"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "Web框架"
  - "Web开发（ArkWeb）"
  - "使用Web组件，在哪个回调事件中可以设置自定义用户代理"
captured_at: "2026-04-17T02:03:15.711Z"
---

# 使用Web组件，在哪个回调事件中可以设置自定义用户代理

建议在[onControllerAttached](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#oncontrollerattached10)回调事件中，使用[setCustomUserAgent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#setcustomuseragent10)来设置自定义用户代理。

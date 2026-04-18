---
title: "Web组件的onLoadIntercept返回结果是否影响onInterceptRequest"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-2"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "Web框架"
  - "Web开发（ArkWeb）"
  - "Web组件的onLoadIntercept返回结果是否影响onInterceptRequest"
captured_at: "2026-04-17T02:03:15.212Z"
---

# Web组件的onLoadIntercept返回结果是否影响onInterceptRequest

Web组件的onLoadIntercept的不同返回结果对应不同的操作：

-   onLoadIntercept返回true时，直接拦截URL请求。
-   onLoadIntercept返回false时，系统将触发onInterceptRequest回调。

**参考链接**

[onLoadIntercept](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onloadintercept10)

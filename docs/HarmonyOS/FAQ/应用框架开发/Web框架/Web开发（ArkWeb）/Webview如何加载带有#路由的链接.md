---
title: "Webview如何加载带有#路由的链接"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-86"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "Web框架"
  - "Web开发（ArkWeb）"
  - "Webview如何加载带有#路由的链接"
captured_at: "2026-04-17T02:03:15.951Z"
---

# Webview如何加载带有#路由的链接

Web组件的src使用'resource://rawfile/LoadWebLink.html#AAA'这种格式进行加载，具体可参考如下代码：

import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct LoadWebLink {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    RelativeContainer() {
      Web({ src: 'resource://rawfile/LoadWebLink.html#AAA', controller: this.controller })
    }
    .height('100%')
    .width('100%')
  }
}

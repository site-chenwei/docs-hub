---
title: "PDF预览如何隐藏PDF操作按钮栏"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-54"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "Web框架"
  - "Web开发（ArkWeb）"
  - "PDF预览如何隐藏PDF操作按钮栏"
captured_at: "2026-04-17T02:03:15.622Z"
---

# PDF预览如何隐藏PDF操作按钮栏

**解决措施**

在URL中加入#toolbar=0&navpanes=0参数即可隐藏PDF操作栏按钮。

**参考代码**

import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct HidePDFToolbar {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      // Hide the toolbar (toolbar=0) and navigation pane (navpanes=0) through URL parameters
      Web({ src: 'resource://rawfile/test.pdf#toolbar=0&navpanes=0', controller: this.controller })
        .domStorageAccess(true)
        .width('100%')
        .height('100%')
    }
    .width('100%')
    .height('100%')
  }
}

---
title: "返回的html里包含数学公式，怎么合理渲染到页面"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-97"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "Web框架"
  - "Web开发（ArkWeb）"
  - "返回的html里包含数学公式，怎么合理渲染到页面"
captured_at: "2026-04-17T02:03:16.100Z"
---

# 返回的html里包含数学公式，怎么合理渲染到页面

HarmonyOS目前没有提供专门的数学公式渲染组件，可以使用WebView组件来加载支持数学公式渲染的网页。

示例代码如下：

import { webview } from "@kit.ArkWeb"

@Component
export struct CourseLearning {
  private webviewController: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile('Mathematics.html'), controller: this.webviewController })
        .domStorageAccess(true)
        .javaScriptAccess(true)
    }
  }
}

示例代码中提供的html可参考[Mathematics.html](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/b39fe4e5abece291bdac1b844563003b397ce87d/ArkWebKit/entry/src/main/resources/rawfile/Mathematics.html)。

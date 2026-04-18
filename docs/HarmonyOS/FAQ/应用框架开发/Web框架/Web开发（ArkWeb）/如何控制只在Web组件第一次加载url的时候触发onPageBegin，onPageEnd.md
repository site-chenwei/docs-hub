---
title: "如何控制只在Web组件第一次加载url的时候触发onPageBegin，onPageEnd"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-34"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "Web框架"
  - "Web开发（ArkWeb）"
  - "如何控制只在Web组件第一次加载url的时候触发onPageBegin，onPageEnd"
captured_at: "2026-04-17T02:03:15.421Z"
---

# 如何控制只在Web组件第一次加载url的时候触发onPageBegin，onPageEnd

使用onAppear事件控制仅在首次加载URL时触发onPageBegin和onPageEnd，参考代码如下：

import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct OnlyOnTheFirstTrigger {
  controller: webview.WebviewController = new webview.WebviewController();
  isFirst: boolean = false;

  build() {
    Column() {
      Web({
        src: 'www.example.com', controller: this.controller
      })
        .onAppear(() => {
          this.isFirst = true;
        })
        .onPageBegin(() => {
          if (this.isFirst) {
            this.isFirst = false;
            console.info('First page loading triggered');
          }
        })
    }
    .width('100%')
    .height('100%')
  }
}

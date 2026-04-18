---
title: "Navigation容器中，如何设置子组件的高度为100%，撑满父容器"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-263"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "UI框架"
  - "方舟UI框架（ArkUI）"
  - "Navigation容器中，如何设置子组件的高度为100%，撑满父容器"
captured_at: "2026-04-17T02:03:05.481Z"
---

# Navigation容器中，如何设置子组件的高度为100%，撑满父容器

参考代码如下：

import { window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0x0000;
const TAG = 'FullNavigationSubComponent';

@Entry
@Component
struct FullNavigationSubComponent {
  context = this.getUIContext();

  onPageShow(): void {
    window.getLastWindow(this.context.getHostContext(), (err, win) => {
      if (err != null) {
        hilog.error(DOMAIN, TAG, \`getLastWindow failed  code:${err.code};message:${err.message}\`);
      } else {
        win.setWindowLayoutFullScreen(true);
      }
    })
  }

  build() {
    Navigation() {
      Column() {
      }
      .width('100%')
      .height('100%')
      .backgroundColor(Color.Black)
    }
    .width('100%')
    .height('100%')
    .title('Personalization Settings')
    .titleMode(NavigationTitleMode.Mini)
    .backgroundColor(Color.Grey)
  }
}

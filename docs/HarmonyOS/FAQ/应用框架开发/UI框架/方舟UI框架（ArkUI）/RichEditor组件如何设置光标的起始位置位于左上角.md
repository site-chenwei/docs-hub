---
title: "RichEditor组件如何设置光标的起始位置位于左上角"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-14"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "UI框架"
  - "方舟UI框架（ArkUI）"
  - "RichEditor组件如何设置光标的起始位置位于左上角"
captured_at: "2026-04-17T02:03:02.934Z"
---

# RichEditor组件如何设置光标的起始位置位于左上角

可以通过align属性传入参数Alignment.TopStart，来设置光标位置位于左上角。示例代码如下：

// xxx.ets
@Entry
@Component
struct RichEditorExample {
  controller: RichEditorController = new RichEditorController();

  build() {
    Column() {
      RichEditor({ controller: this.controller })
        .align(Alignment.TopStart) // Set the starting position of the cursor to the upper left corner
        .height(200)
        .borderWidth(1)
        .borderColor(Color.Red)
        .width('100%')
    }
  }
}

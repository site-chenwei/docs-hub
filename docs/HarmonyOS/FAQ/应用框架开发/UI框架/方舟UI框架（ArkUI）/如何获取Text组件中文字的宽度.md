---
title: "如何获取Text组件中文字的宽度"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-57"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "UI框架"
  - "方舟UI框架（ArkUI）"
  - "如何获取Text组件中文字的宽度"
captured_at: "2026-04-17T02:03:03.386Z"
---

# 如何获取Text组件中文字的宽度

使用@ohos.measure中的measureText()方法计算指定文本单行布局下的宽度。具体可参考如下代码：

@Entry
@Component
struct IndexTest {
  @State textWidth: number = this.getUIContext().getMeasureUtils().measureText({
    textContent: "Hello World",
    fontSize: '50px'
  })

  build() {
    Row() {
      Column() {
        Text(\`The width of 'Hello World': ${this.textWidth}\`)
      }
      .width('100%')
    }
    .height('100%')
  }
}

**参考链接**

[@ohos.measure (文本计算)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-measure)

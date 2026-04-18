---
title: "如何实现Tabs高度自适应内容"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-475"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "UI框架"
  - "方舟UI框架（ArkUI）"
  - "如何实现Tabs高度自适应内容"
captured_at: "2026-04-17T02:03:07.975Z"
---

# 如何实现Tabs高度自适应内容

可以给Tabs设置height('auto')。参考示例如下：

@Entry
@Component
struct Index {
  build() {
    Column() {
      Tabs() {
        TabContent() {
          Row() {
            Text('hello')
          }
          .width('100%')
        }
      }
      .height('auto')
      .barBackgroundColor(Color.Orange)
      .barHeight(0)
    }
    .height('100%')
    .width('100%')
  }
}

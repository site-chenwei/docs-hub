---
title: "如何解决Text组件文本为中文、数字、英文混合时显示省略号截断异常的问题"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-347"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "UI框架"
  - "方舟UI框架（ArkUI）"
  - "如何解决Text组件文本为中文、数字、英文混合时显示省略号截断异常的问题"
captured_at: "2026-04-17T02:03:06.341Z"
---

# 如何解决Text组件文本为中文、数字、英文混合时显示省略号截断异常的问题

文本截断按语言单位进行：中文按字，英文默认按单词，若需按字母截断，可在字母间添加零宽空格：\\u200B。

从API 11开始，建议优先使用将 wordBreak 属性设置为 WordBreak.BREAK\_ALL 的方式，以实现按字母截断。示例代码如下：

@Entry
@Component
struct TextEllipsisDemo {
  @State text: string = '2 years · VIP membership for 3 months · 8GB · 230mm · Product color';

  build() {
    RelativeContainer() {
      Text(this.text)
        .width(200)// Set maximum number of rows
        .maxLines(1)
        .textOverflow({ overflow: TextOverflow.Ellipsis })// Long text display ellipsis
        .ellipsisMode(EllipsisMode.END)// Set the line breaking rule WordBreak.BREAK\_ALL and implement truncation on a letter by letter basis
        .wordBreak(WordBreak.BREAK\_ALL)// API11+ required, for letter-level truncation
        .textAlign(TextAlign.JUSTIFY)
        .backgroundColor(Color.Green)
        .fontSize(16)
    }
    .height('100%')
    .width('100%')
  }
}

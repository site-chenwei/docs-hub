---
title: "@performance/hp"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-use-row-column-to-replace-flex"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "性能规则@performance"
  - "@performance/hp-arkui-use-row-column-to-replace-flex"
captured_at: "2026-04-17T01:36:47.203Z"
---

# @performance/hp-arkui-use-row-column-to-replace-flex

建议使用Column/Row替代Flex。

通用丢帧场景下，建议优先修改。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@performance/hp-arkui-use-row-column-to-replace-flex": "suggestion",
  }
}

#### 选项

该规则无需配置额外选项。

#### 正例

@Entry
@Component
struct MyComponent {
  build() {
    // Replace Flex with Column/Row
    Column() {
      Text('Replace Flex with Column/Row')
        .fontSize(12)
        .height('16')
        .margin({
          top: 5,
          bottom: 10
        })
      Flex().width(300).height(200).backgroundColor(Color.Pink)
      Flex().width(300).height(200).backgroundColor(Color.Yellow)
      Flex().width(300).height(200).backgroundColor(Color.Grey)
      Flex().width(300).height(200).backgroundColor(Color.Pink)
      Flex().width(300).height(200).backgroundColor(Color.Yellow)
      Flex().width(300).height(200).backgroundColor(Color.Grey)
    }.height(200)
  }
}

#### 反例

@Entry
@Component
struct MyComponent {
  build() {
    // Flex Nesting
    Flex({ direction: FlexDirection.Column }) {
      Text('Replace Flex with Column/Row')
        .fontSize(12)
        .height('16')
        .margin({
          top: 5,
          bottom: 10
        })
      Flex().width(300).height(200).backgroundColor(Color.Pink)
      Flex().width(300).height(200).backgroundColor(Color.Yellow)
      Flex().width(300).height(200).backgroundColor(Color.Grey)
      Flex().width(300).height(200).backgroundColor(Color.Pink)
      Flex().width(300).height(200).backgroundColor(Color.Yellow)
      Flex().width(300).height(200).backgroundColor(Color.Grey)
    }.height(200)
  }
}

#### 规则集

plugin:@performance/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。

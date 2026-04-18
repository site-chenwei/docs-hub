---
title: "如何一键清空TextInput、TextArea组件内容"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-80"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "UI框架"
  - "方舟UI框架（ArkUI）"
  - "如何一键清空TextInput、TextArea组件内容"
captured_at: "2026-04-17T02:03:03.504Z"
---

# 如何一键清空TextInput、TextArea组件内容

通过将状态变量绑定到TextInput或TextArea的text属性，点击清空按钮时更新状态变量为空字符串即可实现内容清除。参考代码如下：

@Entry
@Component
struct Index {
  @State text: string = 'Hello World';
  controller: TextInputController = new TextInputController();

  build() {
    Row() {
      Column() {
        TextInput({ placeholder: 'Please input your words.', text: this.text,
          controller:this.controller}).onChange((value) => {
          this.text = value;
        })
        Button('Clear TextInput').onClick(() => {
          this.text = '';
        })
      }
      .width('100%')
    }
    .height('100%')
  }
}

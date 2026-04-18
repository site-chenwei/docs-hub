---
title: "Button组件无法设置字体最大、最小值"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-361"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "UI框架"
  - "方舟UI框架（ArkUI）"
  - "Button组件无法设置字体最大、最小值"
captured_at: "2026-04-17T02:03:06.547Z"
---

# Button组件无法设置字体最大、最小值

Button组件的[labelStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-button#labelstyle10)属性可以设置按钮标签文本和字体的样式。示例代码如下

@Entry
@Component
struct FontSizeButtonExample {
  @State text: string = 'hello';
  @State widthShortSize: number = 300;

  build() {
    Row() {
      Button(this.text)
        .width(this.widthShortSize)
        .height(100)
        //// Set the font size range to 20-40vp，Automatically adjust during actual rendering.
        .labelStyle({
          overflow: TextOverflow.Clip,
          maxLines: 1,
          minFontSize: 20,
          maxFontSize: 40,
          font: {
            size: 30,
            weight: FontWeight.Bolder,
            family: 'cursive',
            style: FontStyle.Italic
          }
        })
    }
  }
}

**参考链接**

[Button](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-button)

---
title: "如何通过key获取对象值"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-108"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "ArkTS语言"
  - "方舟编程语言（ArkTS）"
  - "如何通过key获取对象值"
captured_at: "2026-04-17T02:03:00.592Z"
---

# 如何通过key获取对象值

ArkTS中不支持通过索引访问字段，要使用索引的话可以考虑Record<key, value>，参考代码如下：

class Student {
  data: Record<string, string> = { 'name': 'aaa', 'age': 'bbb' };
}

@Entry
@Component
struct KeyObject {
  build() {
    Column() {
      Button('click')
        .onClick(() => {
          let student = new Student();
          console.info(\`${student.data\['name'\]}\`);
        })
    }
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center)
    .width('100%')
    .height('100%')
  }
}

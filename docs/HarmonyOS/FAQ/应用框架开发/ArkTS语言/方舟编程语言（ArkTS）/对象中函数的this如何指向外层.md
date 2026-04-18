---
title: "对象中函数的this如何指向外层"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-139"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "ArkTS语言"
  - "方舟编程语言（ArkTS）"
  - "对象中函数的this如何指向外层"
captured_at: "2026-04-17T02:03:00.925Z"
---

# 对象中函数的this如何指向外层

通过箭头函数实现。参考代码如下：

interface T {
  start: () => number
}
@Component
struct PointingOuterLayer {
  @State num: number = 1
  obj: T = {
    start: () => {
      return this.num
    }
  }

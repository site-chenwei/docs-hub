---
title: "struct和class的区别是什么"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-284"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "UI框架"
  - "方舟UI框架（ArkUI）"
  - "struct和class的区别是什么"
captured_at: "2026-04-17T02:03:05.723Z"
---

# struct和class的区别是什么

在ArkUI框架中，struct只在自定义组件中使用，@Component装饰的struct构成的自定义组件实例，与class生成的实例具有不同的类型特性。如果开发者需要使用组件作为参数在组件之间传递，可以使用[自定义占位节点](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-user-defined-place-holder)。

---
title: "TextInput的visibility属性设置为Hidden或者None之后是否可获焦"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-269"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "UI框架"
  - "方舟UI框架（ArkUI）"
  - "TextInput的visibility属性设置为Hidden或者None之后是否可获焦"
captured_at: "2026-04-17T02:03:05.584Z"
---

# TextInput的visibility属性设置为Hidden或者None之后是否可获焦

设置visibility属性为Hidden后，仍占据布局空间但组件会从页面中消失，因此无法获得焦点。可以通过将textInput的opacity属性设置为0来隐藏组件，不改变布局特性的同时不影响焦点的获取。

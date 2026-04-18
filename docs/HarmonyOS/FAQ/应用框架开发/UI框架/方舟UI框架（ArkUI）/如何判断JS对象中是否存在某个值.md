---
title: "如何判断JS对象中是否存在某个值"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-192"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "UI框架"
  - "方舟UI框架（ArkUI）"
  - "如何判断JS对象中是否存在某个值"
captured_at: "2026-04-17T02:03:04.637Z"
---

# 如何判断JS对象中是否存在某个值

Object.values(对象名).indexOf(待检测值)，若返回-1表示不包含对应值；返回值不等于-1则表示包含。

var res = array.indexOf(val)

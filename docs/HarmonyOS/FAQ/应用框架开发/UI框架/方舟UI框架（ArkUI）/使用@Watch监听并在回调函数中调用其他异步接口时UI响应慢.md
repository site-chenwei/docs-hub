---
title: "使用@Watch监听并在回调函数中调用其他异步接口时UI响应慢"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-185"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "UI框架"
  - "方舟UI框架（ArkUI）"
  - "使用@Watch监听并在回调函数中调用其他异步接口时UI响应慢"
captured_at: "2026-04-17T02:03:04.635Z"
---

# 使用@Watch监听并在回调函数中调用其他异步接口时UI响应慢

@Watch用于快速计算，在UI重新渲染之前执行。不建议在@Watch函数中调用async和await，因为异步行为会延迟组件的重新渲染，可能导致性能问题。

**参考链接**

[@Watch装饰器：状态变量更改通知](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-watch)

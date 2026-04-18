---
title: "当前ArkTS是否采用类Node.js的异步I/O机制"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-132"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "ArkTS语言"
  - "方舟编程语言（ArkTS）"
  - "当前ArkTS是否采用类Node.js的异步I/O机制"
captured_at: "2026-04-17T02:03:00.843Z"
---

# 当前ArkTS是否采用类Node.js的异步I/O机制

Node.js使用事件循环机制处理异步操作，支持回调函数和Promise。ArkTS使用基于协程的异步I/O机制，I/O事件分发到I/O线程，不阻塞JS线程，支持回调函数、Promise和async/await。

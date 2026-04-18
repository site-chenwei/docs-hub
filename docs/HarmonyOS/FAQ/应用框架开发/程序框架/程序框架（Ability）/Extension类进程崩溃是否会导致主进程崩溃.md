---
title: "Extension类进程崩溃是否会导致主进程崩溃"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-32"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "程序框架"
  - "程序框架（Ability）"
  - "Extension类进程崩溃是否会导致主进程崩溃"
captured_at: "2026-04-17T02:02:58.872Z"
---

# Extension类进程崩溃是否会导致主进程崩溃

子进程的崩溃不会直接导致主进程崩溃。只有当子进程的崩溃导致主进程在使用部分功能时抛出了未被应用捕获的异常，才会间接导致主进程崩溃。

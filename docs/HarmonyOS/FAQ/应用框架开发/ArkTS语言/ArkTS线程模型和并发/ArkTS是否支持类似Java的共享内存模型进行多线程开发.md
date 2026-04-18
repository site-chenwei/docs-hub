---
title: "ArkTS是否支持类似Java的共享内存模型进行多线程开发"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-37"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "ArkTS语言"
  - "ArkTS线程模型和并发"
  - "ArkTS是否支持类似Java的共享内存模型进行多线程开发"
captured_at: "2026-04-17T02:03:01.276Z"
---

# ArkTS是否支持类似Java的共享内存模型进行多线程开发

无法通过加锁的方式实现多个线程同时对同一个内存对象进行操作。

ArkTS采用Actor并发模型，线程间内存隔离，目前仅支持SharedArrayBuffer和Native层对象的共享。

**参考链接**

[多线程并发概述](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multi-thread-concurrency-overview)

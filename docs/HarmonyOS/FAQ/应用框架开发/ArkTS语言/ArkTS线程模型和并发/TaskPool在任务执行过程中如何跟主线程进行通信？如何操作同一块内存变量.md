---
title: "TaskPool在任务执行过程中如何跟主线程进行通信？如何操作同一块内存变量"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-40"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "ArkTS语言"
  - "ArkTS线程模型和并发"
  - "TaskPool在任务执行过程中如何跟主线程进行通信？如何操作同一块内存变量"
captured_at: "2026-04-17T02:03:01.294Z"
---

# TaskPool在任务执行过程中如何跟主线程进行通信？如何操作同一块内存变量

TaskPool的任务通过sendData接口触发主线程的onReceiveData回调，目前不支持主线程向子线程通信。

多个线程可以通过SharedArrayBuffer操作同一块内存。

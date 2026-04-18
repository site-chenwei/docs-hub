---
title: "线程间JS对象通过序列化方式进行数据通信，是否存在性能问题"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-24"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "ArkTS语言"
  - "ArkTS线程模型和并发"
  - "线程间JS对象通过序列化方式进行数据通信，是否存在性能问题"
captured_at: "2026-04-17T02:03:01.154Z"
---

# 线程间JS对象通过序列化方式进行数据通信，是否存在性能问题

线程间对象的数据通信依赖于序列化和反序列化，耗时与数据量成正比。为了提高效率，建议控制传输的数据量，或者使用ArrayBuffer或SharedArrayBuffer进行数据转移或共享。

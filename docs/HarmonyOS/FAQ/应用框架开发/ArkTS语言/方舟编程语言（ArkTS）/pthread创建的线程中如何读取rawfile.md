---
title: "pthread创建的线程中如何读取rawfile"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-23"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "ArkTS语言"
  - "方舟编程语言（ArkTS）"
  - "pthread创建的线程中如何读取rawfile"
captured_at: "2026-04-17T02:02:59.882Z"
---

# pthread创建的线程中如何读取rawfile

可在线程安全函数中读取。

1.  在UI主线程中获取并保存资源文件对象。
2.  创建线程安全的函数。
3.  在非UI主线程中调用线程安全函数。
4.  在线程安全函数中，读取rawfile目录下的文件资源。

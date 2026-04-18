---
title: "以libstd为例，C++的标准库放在哪里了，有没有打到hap包中"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-48"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "ArkTS语言"
  - "方舟编程语言（ArkTS）"
  - "以libstd为例，C++的标准库放在哪里了，有没有打到hap包中"
captured_at: "2026-04-17T02:02:59.955Z"
---

# 以libstd为例，C++的标准库放在哪里了，有没有打到hap包中

libc++\_shared.so被打包到应用目录下，每个应用都有一份独立的文件。

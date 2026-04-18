---
title: "A持有B，B引用A的场景会不会导致内存泄漏"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-107"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "ArkTS语言"
  - "方舟编程语言（ArkTS）"
  - "A持有B，B引用A的场景会不会导致内存泄漏"
captured_at: "2026-04-17T02:03:00.594Z"
---

# A持有B，B引用A的场景会不会导致内存泄漏

方舟虚拟机的内存管理和GC使用根可达算法，该算法能解决循环引用问题，避免A引用B、B引用A的内存泄漏。

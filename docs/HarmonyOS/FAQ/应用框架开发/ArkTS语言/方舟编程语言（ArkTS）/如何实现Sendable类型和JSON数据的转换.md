---
title: "如何实现Sendable类型和JSON数据的转换"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-102"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "ArkTS语言"
  - "方舟编程语言（ArkTS）"
  - "如何实现Sendable类型和JSON数据的转换"
captured_at: "2026-04-17T02:03:00.508Z"
---

# 如何实现Sendable类型和JSON数据的转换

可以通过从API version 12开始支持的，ArkTS新增的[ArkTSUtils.ASON](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-utils-ason)工具实现。

ASON支持解析JSON字符串并生成共享数据，用于跨并发域传输。ASON还支持将共享数据转换为JSON字符串。

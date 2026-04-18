---
title: "是否可以在TaskPool中动态加载模块（HAR、HSP、SO）"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-47"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "ArkTS语言"
  - "ArkTS线程模型和并发"
  - "是否可以在TaskPool中动态加载模块（HAR、HSP、SO）"
captured_at: "2026-04-17T02:03:01.337Z"
---

# 是否可以在TaskPool中动态加载模块（HAR、HSP、SO）

TaskPool的动态加载能力与主线程相同。然而，TaskPool线程加载后，由于模块化线程隔离，无法被主线程复用。

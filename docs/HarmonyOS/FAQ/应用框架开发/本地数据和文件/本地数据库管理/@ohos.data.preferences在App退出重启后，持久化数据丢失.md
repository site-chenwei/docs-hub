---
title: "@ohos.data.preferences在App退出重启后，持久化数据丢失"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-28"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "本地数据和文件"
  - "本地数据库管理"
  - "@ohos.data.preferences在App退出重启后，持久化数据丢失"
captured_at: "2026-04-17T02:03:08.689Z"
---

# @ohos.data.preferences在App退出重启后，持久化数据丢失

数据持久化需要在调用preferences.put(key, value)后调用preferences.flush()接口以实现数据持久化。若不调用flush()，数据可能仅保存在内存中而不会写入持久化存储，导致应用退出后数据丢失。

**参考链接**

[通过用户首选项实现数据持久化 (ArkTS)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-persistence-by-preferences)

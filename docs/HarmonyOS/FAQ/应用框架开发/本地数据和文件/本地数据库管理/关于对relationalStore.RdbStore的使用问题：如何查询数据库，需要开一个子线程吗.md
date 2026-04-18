---
title: "关于对relationalStore.RdbStore的使用问题：如何查询数据库，需要开一个子线程吗"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-47"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "本地数据和文件"
  - "本地数据库管理"
  - "关于对relationalStore.RdbStore的使用问题：如何查询数据库，需要开一个子线程吗"
captured_at: "2026-04-17T02:03:09.502Z"
---

# 关于对relationalStore.RdbStore的使用问题：如何查询数据库，需要开一个子线程吗

查询数据库可以使用[@ohos.data.relationalStore](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-relationalstore)模块提供的[query](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-rdbstore#query10)方法，该方法是异步方法，因此对于查询数据库操作，不需要开子线程。

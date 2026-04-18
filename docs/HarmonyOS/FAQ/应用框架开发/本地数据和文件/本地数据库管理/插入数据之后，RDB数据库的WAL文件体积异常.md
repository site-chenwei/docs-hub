---
title: "插入数据之后，RDB数据库的WAL文件体积异常"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-34"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "本地数据和文件"
  - "本地数据库管理"
  - "插入数据之后，RDB数据库的WAL文件体积异常"
captured_at: "2026-04-17T02:03:08.884Z"
---

# 插入数据之后，RDB数据库的WAL文件体积异常

**解决措施**

在开启读事务或结果集未关闭的情况下持续执行增删改操作，会导致WAL文件大小超过默认上限，此时系统会抛出错误码14800047。

处理该错误码时，检查结果集或事务状态。

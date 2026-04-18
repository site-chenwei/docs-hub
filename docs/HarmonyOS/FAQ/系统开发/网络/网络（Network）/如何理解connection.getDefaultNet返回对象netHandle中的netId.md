---
title: "如何理解connection.getDefaultNet返回对象netHandle中的netId"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-5"
menu_path:
  - "FAQ"
  - "系统开发"
  - "网络"
  - "网络（Network）"
  - "如何理解connection.getDefaultNet返回对象netHandle中的netId"
captured_at: "2026-04-17T02:03:16.975Z"
---

# 如何理解connection.getDefaultNet返回对象netHandle中的netId

**问题现象**

netId的值0表示未联网，100表示已联网。

**解决措施**

在正常情况下，netHandle中的netId为0表示未连接网络，大于等于100表示已连接网络。

**参考链接**

[NetHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection#nethandle)

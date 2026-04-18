---
title: "HAR包是否支持依赖传递"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-38"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "程序包结构"
  - "HAR包是否支持依赖传递"
captured_at: "2026-04-17T02:02:58.249Z"
---

# HAR包是否支持依赖传递

**问题现象**

例如，有三个HAR分别为A、B、C，A依赖B，B依赖C。A可以直接引用C的资源。

**解决措施**

A不能直接引用C的资源。A需直接依赖C，才能进行引用。

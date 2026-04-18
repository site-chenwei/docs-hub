---
title: "GET请求的bodySign是对谁签名得到的？"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-faq-3"
menu_path:
  - "指南"
  - "应用服务"
  - "Payment Kit（鸿蒙支付服务）"
  - "Payment Kit常见问题"
  - "GET请求的bodySign是对谁签名得到的？"
captured_at: "2026-04-17T01:36:19.962Z"
---

# GET请求的bodySign是对谁签名得到的？

GET请求需要对path url进行签名，例如[查询支付订单](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/payment-sys-query-order)的待签名内容是：“/api/v2/aggr/transactions/orders/{sysTransOrderNo}”。

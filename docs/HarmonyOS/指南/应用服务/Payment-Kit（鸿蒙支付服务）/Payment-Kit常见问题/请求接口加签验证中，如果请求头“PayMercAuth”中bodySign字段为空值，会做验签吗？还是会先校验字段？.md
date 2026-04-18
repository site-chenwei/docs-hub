---
title: "请求接口加签验证中，如果请求头“PayMercAuth”中bodySign字段为空值，会做验签吗？还是会先校验字段？"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-faq-21"
menu_path:
  - "指南"
  - "应用服务"
  - "Payment Kit（鸿蒙支付服务）"
  - "Payment Kit常见问题"
  - "请求接口加签验证中，如果请求头“PayMercAuth”中bodySign字段为空值，会做验签吗？还是会先校验字段？"
captured_at: "2026-04-17T01:36:20.157Z"
---

# 请求接口加签验证中，如果请求头“PayMercAuth”中bodySign字段为空值，会做验签吗？还是会先校验字段？

鉴权请求头“PayMercAuth”会先校验相关字段再做验签。bodySign字段设置为空值，Payment Kit服务器不会做验签，直接响应异常给商户。

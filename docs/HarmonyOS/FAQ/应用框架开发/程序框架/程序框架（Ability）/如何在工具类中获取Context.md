---
title: "如何在工具类中获取Context"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-74"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "程序框架"
  - "程序框架（Ability）"
  - "如何在工具类中获取Context"
captured_at: "2026-04-17T02:02:59.170Z"
---

# 如何在工具类中获取Context

工具类中无法直接获取Context。可以在EntryAbility中获取Context并保存至AppStorage。工具类中使用AppStorage获取Context。

**参考链接**

[AppStorage：应用全局的UI状态存储](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-appstorage)

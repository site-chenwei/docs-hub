---
title: "如何将Resource资源对象转成string类型"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-localization-7"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "无障碍和本地化"
  - "本地化开发（Localization）"
  - "如何将Resource资源对象转成string类型"
captured_at: "2026-04-17T02:03:15.058Z"
---

# 如何将Resource资源对象转成string类型

Resource 为字符串，支持使用 this.context.resourceManager.getStringSync($r('app.string.test').id)同步转换为字符串，也支持使用 $r('app.string.test', 2) 进行格式化。

**参考链接**

[getStringSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resource-manager#getstringsync10)

---
title: "如何获取应用级别的temp路径和files路径"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-15"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "程序框架"
  - "程序框架（Ability）"
  - "如何获取应用级别的temp路径和files路径"
captured_at: "2026-04-17T02:02:58.750Z"
---

# 如何获取应用级别的temp路径和files路径

通过上下文 context 获取。例如：

-   temp路径：通过 this.context.getApplicationContext().tempDir 获取。
-   文件路径：可通过 this.context.getApplicationContext().filesDir 获取。

**参考链接**

[获取应用文件路径](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-context-stage#获取应用文件路径)

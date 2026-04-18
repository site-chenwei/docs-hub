---
title: "ohpm ERROR: JSON5: invalid end of input at 1:1"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-command-line-tool-5"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "命令行工具"
  - "ohpm ERROR: JSON5: invalid end of input at 1:1"
captured_at: "2026-04-17T02:03:25.638Z"
---

# ohpm ERROR: JSON5: invalid end of input at 1:1

**问题描述**

电脑无网络，升级到600后出现错误：ohpm ERROR: JSON5: invalid end of input at 1:1。

**解决方案**

删除工程下的oh-package-lock.json5文件后，执行ohpm clean、ohpm cache clean和ohpm install --all。

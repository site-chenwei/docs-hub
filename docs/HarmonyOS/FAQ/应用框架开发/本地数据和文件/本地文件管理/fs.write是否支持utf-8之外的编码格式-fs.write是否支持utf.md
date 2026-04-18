---
title: "fs.write是否支持utf"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-11"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "本地数据和文件"
  - "本地文件管理"
  - "fs.write是否支持utf-8之外的编码格式"
captured_at: "2026-04-17T02:03:13.003Z"
---

# fs.write是否支持utf-8之外的编码格式

**问题描述**

1.希望fs.write支持utf-8之外的编码格式，目前只支持utf-8。

2.TextEncoder等工具类支持多种编码格式，与其他API保持一致。

**解决措施**

当前不支持其他格式。API能力允许开发者通过编写代码在内存中进行编码转换，并将结果直接存储到ArrayBuffer中，然后保存到文件中。

---
title: "从FilePicker返回的图片地址uri是不是只是在一定的时间内有访问权限"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-26"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "本地数据和文件"
  - "本地文件管理"
  - "从FilePicker返回的图片地址uri是不是只是在一定的时间内有访问权限"
captured_at: "2026-04-17T02:03:14.287Z"
---

# 从FilePicker返回的图片地址uri是不是只是在一定的时间内有访问权限

重启应用后，URI失效是正常现象。系统通过Picker生成的URI具有临时访问权限，应用被终止后（包括重启）该权限将失效。因此，需要重新通过Picker选择来生成新的URI。

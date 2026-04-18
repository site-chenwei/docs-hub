---
title: "hilog日志如何设置为只打印当前应用的日志"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-2"
menu_path:
  - "FAQ"
  - "应用质量"
  - "技术质量"
  - "运维"
  - "hilog日志如何设置为只打印当前应用的日志"
captured_at: "2026-04-17T02:02:57.110Z"
---

# hilog日志如何设置为只打印当前应用的日志

使用hilog命令行工具来过滤保留当前应用的日志。

```text
hilog -T xxx 按tag过滤; 
hilog –D xxx 按domain过滤; 
hilog -e 对日志内容匹配，支持正则表达式。支持tag, domain, pid等多重过滤,组合过滤以及反向过滤;
```

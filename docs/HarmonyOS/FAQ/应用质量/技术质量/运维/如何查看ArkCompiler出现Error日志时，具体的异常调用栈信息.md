---
title: "如何查看ArkCompiler出现Error日志时，具体的异常调用栈信息"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-29"
menu_path:
  - "FAQ"
  - "应用质量"
  - "技术质量"
  - "运维"
  - "如何查看ArkCompiler出现Error日志时，具体的异常调用栈信息"
captured_at: "2026-04-17T02:02:57.355Z"
---

# 如何查看ArkCompiler出现Error日志时，具体的异常调用栈信息

Native抛异常，如需查看backtrace，运行以下命令。

打开异常栈：

```powershell
hdc shell param set persist.ark.properties 0x125c 
hdc shell reboot
```

恢复默认值：

```powershell
hdc shell param set persist.ark.properties 0x105c 
hdc shell reboot
```

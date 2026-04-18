---
title: "如何解决编译报错“ERROR: ArkTS Compiler Error ERROR: /bin/sh: \"xxxx/es2abc\": Operation not permitted”的问题"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-130"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "如何解决编译报错“ERROR: ArkTS Compiler Error ERROR: /bin/sh: \"xxxx/es2abc\": Operation not permitted”的问题"
captured_at: "2026-04-17T02:03:22.693Z"
---

# 如何解决编译报错“ERROR: ArkTS Compiler Error ERROR: /bin/sh: "xxxx/es2abc": Operation not permitted”的问题

**问题现象**

编译报错“ERROR: ArkTS Compiler Error ERROR: /bin/sh: "xxxx/es2abc": Operation not permitted”。

**问题原因**

获取SDK后，Mac的安全设置会为可执行文件添加“来源于网络”的标识（com.apple.quarantine），导致文件无法执行。

**解决方案**

删除可执行文件的com.apple.quarantine标识。

```powershell
xattr -d com.apple.quarantine /path/to/es2abc
```

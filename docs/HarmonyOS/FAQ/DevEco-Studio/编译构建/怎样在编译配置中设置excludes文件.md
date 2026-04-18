---
title: "怎样在编译配置中设置excludes文件"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-57"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "怎样在编译配置中设置excludes文件"
captured_at: "2026-04-17T02:03:21.783Z"
---

# 怎样在编译配置中设置excludes文件

在模块级build-profile.json5中如下进行配置：

"nativeLib": {
  "debugSymbol": {
    "strip": true,
    "exclude": \[
      "\*\*/3.so"
    \]
  }
},

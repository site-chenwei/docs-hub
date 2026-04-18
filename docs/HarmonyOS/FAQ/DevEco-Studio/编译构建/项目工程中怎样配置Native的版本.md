---
title: "项目工程中怎样配置Native的版本"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-55"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "项目工程中怎样配置Native的版本"
captured_at: "2026-04-17T02:03:21.719Z"
---

# 项目工程中怎样配置Native的版本

在工程级build-profile.json5的app.products中如下进行配置：

"products": \[
  {
    "name": "default",
    "signingConfig": "default",
    "compatibleSdkVersion": "5.0.5(17)",
    "targetSdkVersion": "5.0.5(17)",
    "runtimeOS": "HarmonyOS",
  }
\],

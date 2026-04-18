---
title: "编译打包CPU架构设置"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-86"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "编译打包CPU架构设置"
captured_at: "2026-04-17T02:03:22.129Z"
---

# 编译打包CPU架构设置

**问题描述**

在编译打包时，若需移除v7a，可以参考以下配置文档。

**解决方案**

可参考 [bm工具](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/bm-tool)

"externalNativeOptions": {
  "path": "./src/main/cpp/CMakeLists.txt",
  //CMake configuration file, providing CMake build scripts
  "arguments": "",
  //Optional compilation parameters passed to CMake
  "abiFilters": \[
    "x86\_64",
    "arm64-v8a"
  \],
  //Used to set up the local ABI compilation environment
  "cppFlags": ""
  //Set optional parameters for the C++ compiler
},

---
title: "armeabi"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-91"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "armeabi-v7a是否支持Neon指令扩展"
captured_at: "2026-04-17T02:03:22.188Z"
---

# armeabi-v7a是否支持Neon指令扩展

**问题描述**

使用CMake编译现有工程为armeabi-v7a架构时出现问题。

D:/DeveloperTools/Huawei/SDK/default/base/native/llvm/lib/clang/15.0.4/include/arm\_neon.h:28:2: error: “NEON intrinsics not available with the soft-float ABI. Please use -mfloat-abi=softfp or -mfloat-abi=hard”#error “NEON intrinsics not available with the soft-float ABI. Please use -mfloat-abi=softfp or -mfloat-abi=hard”

**解决方案**

可以进行如下验证：Neon指令集的引入方案如下：

在entry目录的build-profile.json5文件中，externalNativeOptions节点添加配置项：

"externalNativeOptions": {
  "path": "./src/main/cpp/CMakeLists.txt",
  "arguments": "",
  "abiFilters": \[
    "x86\_64",
    "arm64-v8a"
  \],
  // This is a configuration item to be added
  "cppFlags": "-mfloat-abi=hard",
  // This is a configuration item to be added
},

引入头文件#include <arm\_neon.h>

---
title: "C/C++内存错误检测"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/debug-asan"
menu_path:
  - "指南"
  - "NDK开发"
  - "调试和性能分析"
  - "C/C++内存错误检测"
captured_at: "2026-04-17T01:36:41.971Z"
---

# C/C++内存错误检测

为追求C/C++的更优性能，编译器和OS(Windows/Linux/Mac)运行框架不会对内存操作进行安全检测。针对该场景，DevEco Studio集成ASan（Address-Sanitizer）为开发者提供面向C/C++的地址越界检测能力，并通过FaultLog展示错误的堆栈详情及导致错误的代码行。

关于ASan的使用说明请参见[C/C++内存错误检测](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-asan)。

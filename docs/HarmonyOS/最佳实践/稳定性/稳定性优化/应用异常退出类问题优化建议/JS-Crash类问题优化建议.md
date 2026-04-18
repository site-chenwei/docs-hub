---
title: "JS Crash类问题优化建议"
source_url: "https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-js-crash-opt"
menu_path:
  - "最佳实践"
  - "稳定性"
  - "稳定性优化"
  - "应用异常退出类问题优化建议"
  - "JS Crash类问题优化建议"
captured_at: "2026-04-17T01:54:19.894Z"
---

# JS Crash类问题优化建议

#### 优化建议1：Source Maps归档保存

生产环境归档SourceMap便于后续源码还原，遇到JS Crash应先进行[堆栈轨迹分析](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V5/ide-release-app-stack-analysis-V5)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/6ibOTyeqQuOCLDfm7sgXMQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T015422Z&HW-CC-Expire=86400&HW-CC-Sign=E18801D1EDB8260479C7F6A160AD5F18AF15808F305C50C73706FDCE99DA516C)

编译时SourceMap的获取位置详见：[sourceMap归档位置介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-exception-stack-parsing-principle#section666114451518)。

#### 优化建议2：崩溃预防机制

可使用errorManager注册错误观测器。注册后可以捕获到应用产生的JS Crash，应用崩溃时进程不会退出。详见[errorManager使用指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/errormanager-guidelines)。

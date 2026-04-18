---
title: "HarmonyOS是否限制App进程fork子进程，是否允许app里自带的可执行文件运行（fork+exec）执行，并通过ptrace方式读取自身进程？这种方式以后是否会限制并禁止"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-112"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "程序框架"
  - "程序框架（Ability）"
  - "HarmonyOS是否限制App进程fork子进程，是否允许app里自带的可执行文件运行（fork+exec）执行，并通过ptrace方式读取自身进程？这种方式以后是否会限制并禁止"
captured_at: "2026-04-17T02:02:59.427Z"
---

# HarmonyOS是否限制App进程fork子进程，是否允许app里自带的可执行文件运行（fork+exec）执行，并通过ptrace方式读取自身进程？这种方式以后是否会限制并禁止

**解决方案**

系统限制普通应用直接进行Fork进程操作；手机产品不允许普通应用直接创建进程。

---
title: "如何查询应用进程的pid信息"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-81"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "程序框架"
  - "程序框架（Ability）"
  - "如何查询应用进程的pid信息"
captured_at: "2026-04-17T02:02:59.290Z"
---

# 如何查询应用进程的pid信息

可以通过以下两种方式获取：

-   方式一：通过以下命令查询应用进程信息。
    
    执行hdc shell命令，进入设备的命令行。执行“ps -ef”命令，查看所有正在运行的进程信息。
    
-   方式二：通过调用[process](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-process)相关接口查询。
    
    import { process } from '@kit.ArkTS';
    
    let pid = process.pid;

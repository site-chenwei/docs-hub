---
title: "如何解决构建流水线提示Couldn't find hvigor/hvigor"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-75"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "如何解决构建流水线提示Couldn't find hvigor/hvigor-wrapper.js的问题"
captured_at: "2026-04-17T02:03:21.989Z"
---

# 如何解决构建流水线提示Couldn't find hvigor/hvigor-wrapper.js的问题

1.  hvigorw脚本依赖于hvigor-wrapper.js。
2.  在工程外部使用脚本进行编译时：
    1.  确认hvigor-wrapper.js文件是否位于工程的hvigor文件夹中。
    2.  根据文档：[搭建流水线](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-command-line-building-app#section14397105115226)，需要先cd到工程的根目录，再调用.hvigorw的各种命令。

---
title: "ohpm"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-command-line-tool-4"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "命令行工具"
  - "ohpm-repo使用mysqlDB插件连mysql时，报错“decrypt data failed. error: Unsupported state or unable to authenticate data”"
captured_at: "2026-04-17T02:03:25.598Z"
---

# ohpm-repo使用mysqlDB插件连mysql时，报错“decrypt data failed. error: Unsupported state or unable to authenticate data”

删除ohpm-repo私仓根目录下的.deploy\_root文件，重新指定加密组件，执行start操作。

**参考链接**

[ohpm-repo start](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-start)

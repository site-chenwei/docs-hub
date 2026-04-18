---
title: "hdc工具导出/导入文件等常用hdc命令有哪些"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-31"
menu_path:
  - "FAQ"
  - "应用质量"
  - "技术质量"
  - "运维"
  - "hdc工具导出/导入文件等常用hdc命令有哪些"
captured_at: "2026-04-17T02:02:57.341Z"
---

# hdc工具导出/导入文件等常用hdc命令有哪些

导出文件：hdc file recv 手机路径

电脑路径导入文件：hdc file send 电脑路径

查看已连接设备：hdc list targets

手机常亮：hdc shell power-shell setmode 602

查看OUC进程：ps -ef|grep com.huawei.hmos.ouccom.ohos.updateapp

查看DUE进程：ps -ef|grep updater\_sa

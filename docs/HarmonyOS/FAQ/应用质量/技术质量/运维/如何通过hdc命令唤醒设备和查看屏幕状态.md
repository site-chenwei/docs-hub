---
title: "如何通过hdc命令唤醒设备和查看屏幕状态"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-52"
menu_path:
  - "FAQ"
  - "应用质量"
  - "技术质量"
  - "运维"
  - "如何通过hdc命令唤醒设备和查看屏幕状态"
captured_at: "2026-04-17T02:02:57.560Z"
---

# 如何通过hdc命令唤醒设备和查看屏幕状态

唤醒设备：hdc shell power-shell wakeup。

查看屏幕状态：hdc shell hidumper -s 3301 -a

查询手机IMEI：首先，进入fastboot模式（hdc target boot bootloader），然后使用fastboot命令查询（fastboot oem get-psid）。

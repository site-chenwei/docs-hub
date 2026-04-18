---
title: "如何在多设备情况下使用hdc"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-48"
menu_path:
  - "FAQ"
  - "应用质量"
  - "技术质量"
  - "运维"
  - "如何在多设备情况下使用hdc"
captured_at: "2026-04-17T02:02:57.455Z"
---

# 如何在多设备情况下使用hdc

**问题场景**

启动模拟器并连接真机，然后调用hdc命令获取udid。此时仅打印一条模拟器的udid。

**解决措施**

多设备环境下执行hdc shell会失败，需要指定设备执行hdc -t xx shell。否则，会报错。

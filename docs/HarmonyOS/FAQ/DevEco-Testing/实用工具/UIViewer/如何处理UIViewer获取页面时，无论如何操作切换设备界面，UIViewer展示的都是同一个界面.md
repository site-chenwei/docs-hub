---
title: "如何处理UIViewer获取页面时，无论如何操作切换设备界面，UIViewer展示的都是同一个界面"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-utilities-uiviewer-1"
menu_path:
  - "FAQ"
  - "DevEco Testing"
  - "实用工具"
  - "UIViewer"
  - "如何处理UIViewer获取页面时，无论如何操作切换设备界面，UIViewer展示的都是同一个界面"
captured_at: "2026-04-17T02:03:26.972Z"
---

# 如何处理UIViewer获取页面时，无论如何操作切换设备界面，UIViewer展示的都是同一个界面

打开cmd窗口，在设备上执行hdc指令删除该文件：

```powershell
hdc shell rm -r /data/local/tmp/latestScreen.jpeg
```

重试设备投屏。如果获取页面仍然显示同一界面，请重启设备后再次尝试。

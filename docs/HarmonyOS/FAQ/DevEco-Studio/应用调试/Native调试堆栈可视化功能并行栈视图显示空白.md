---
title: "Native调试堆栈可视化功能并行栈视图显示空白"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-56"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "应用调试"
  - "Native调试堆栈可视化功能并行栈视图显示空白"
captured_at: "2026-04-17T02:03:24.832Z"
---

# Native调试堆栈可视化功能并行栈视图显示空白

**问题现象**

使用Native调试堆栈可视化功能时，如果在任意两个页签之间来回切换，可能会遇到并行栈视图界面显示为空白的情况。

**解决措施**

导致该问题的原因可能是电脑GPU不兼容，或在云桌面的场景下使用DevEco Studio。

在DevEco Studio中**双击Shift**，在弹出的窗口中搜索**Registry**，**在Registry**页面中勾选**ide.browser.jcef.gpu.disable**项，关闭窗口并重启DevEco Studio即可。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/8tsmtOHqRJmSF3mOx8zzyQ/zh-cn_image_0000002521308425.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=CC4B01EE0937AC36A31C36F49C4BC8C81EE8751C22B49BD364D79EACB86FB49E)

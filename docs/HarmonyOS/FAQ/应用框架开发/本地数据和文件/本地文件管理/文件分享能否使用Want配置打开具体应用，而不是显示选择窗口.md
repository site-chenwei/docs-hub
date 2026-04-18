---
title: "文件分享能否使用Want配置打开具体应用，而不是显示选择窗口"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-9"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "本地数据和文件"
  - "本地文件管理"
  - "文件分享能否使用Want配置打开具体应用，而不是显示选择窗口"
captured_at: "2026-04-17T02:03:12.919Z"
---

# 文件分享能否使用Want配置打开具体应用，而不是显示选择窗口

目前不支持使用Want配置打开具体应用。当前拉起的打开方式是通过设备内应用配置action: "ohos.want.action.sendData"来识别的，不能由业务自行指定。

**参考链接**

[应用文件分享](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-app-file)

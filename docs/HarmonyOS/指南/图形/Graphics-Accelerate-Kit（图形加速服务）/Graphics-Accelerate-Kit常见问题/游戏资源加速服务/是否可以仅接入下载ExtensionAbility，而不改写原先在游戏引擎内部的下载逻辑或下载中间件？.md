---
title: "是否可以仅接入下载ExtensionAbility，而不改写原先在游戏引擎内部的下载逻辑或下载中间件？"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-assetdownload-faq-6"
menu_path:
  - "指南"
  - "图形"
  - "Graphics Accelerate Kit（图形加速服务）"
  - "Graphics Accelerate Kit常见问题"
  - "游戏资源加速服务"
  - "是否可以仅接入下载ExtensionAbility，而不改写原先在游戏引擎内部的下载逻辑或下载中间件？"
captured_at: "2026-04-17T01:36:10.019Z"
---

# 是否可以仅接入下载ExtensionAbility，而不改写原先在游戏引擎内部的下载逻辑或下载中间件？

可以，支持仅接入下载ExtensionAbility。

但建议在应用进入前台时，通过[removeAllAssetDownloadTasks](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/graphics-accelerate-assetdownloadmanager#assetdownloadmanagerremoveallassetdownloadtasks)移除系统中的所有下载任务，对于已完成下载的任务可以复用，避免重复下载。对于未完成下载的任务建议使用应用自身下载器进行重新下载。

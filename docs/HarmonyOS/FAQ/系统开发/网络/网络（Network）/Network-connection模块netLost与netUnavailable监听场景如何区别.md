---
title: "Network connection模块netLost与netUnavailable监听场景如何区别"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-62"
menu_path:
  - "FAQ"
  - "系统开发"
  - "网络"
  - "网络（Network）"
  - "Network connection模块netLost与netUnavailable监听场景如何区别"
captured_at: "2026-04-17T02:03:17.573Z"
---

# Network connection模块netLost与netUnavailable监听场景如何区别

[on('netLost')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection#onnetlost)事件监听用于网络状态丢失。例如：Wi-Fi或移动网络断开时。

[on('netUnavailable')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection#onnetunavailable)事件监听为网络连接成功但是发生异常无法正常访问互联网。例如：设备上显示桌面Wi-Fi图标有“!”。

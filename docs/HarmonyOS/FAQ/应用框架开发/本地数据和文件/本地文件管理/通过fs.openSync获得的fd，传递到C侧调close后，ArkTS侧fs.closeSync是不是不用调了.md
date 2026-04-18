---
title: "通过fs.openSync获得的fd，传递到C侧调close后，ArkTS侧fs.closeSync是不是不用调了"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-21"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "本地数据和文件"
  - "本地文件管理"
  - "通过fs.openSync获得的fd，传递到C侧调close后，ArkTS侧fs.closeSync是不是不用调了"
captured_at: "2026-04-17T02:03:13.768Z"
---

# 通过fs.openSync获得的fd，传递到C侧调close后，ArkTS侧fs.closeSync是不是不用调了

需要调用ArkTS侧的fs.openSync方法获取文件描述符（fd），并将该fd传递给C侧。C侧使用完fd后需要单独调用close关闭。同时，ArkTS侧在使用完文件对象后，仍需调用fs.closeSync关闭文件。由于跨语言边界传递的文件描述符需要双方各自管理资源，建议在关闭后设置null值避免重复操作。

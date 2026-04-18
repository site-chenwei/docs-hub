---
title: "Image或者ImageSpan传入一个string类型的路径时无法加载图片"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-153"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "UI框架"
  - "方舟UI框架（ArkUI）"
  - "Image或者ImageSpan传入一个string类型的路径时无法加载图片"
captured_at: "2026-04-17T02:03:04.275Z"
---

# Image或者ImageSpan传入一个string类型的路径时无法加载图片

目前规格上只支持常量，需要把string提取出来用$r( )包裹。例如：

localImageName = $r( 'app.media.icon' )

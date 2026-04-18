---
title: "ArkUI中icon资源锯齿感严重"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-114"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "UI框架"
  - "方舟UI框架（ArkUI）"
  - "ArkUI中icon资源锯齿感严重"
captured_at: "2026-04-17T02:03:03.836Z"
---

# ArkUI中icon资源锯齿感严重

**解决方案**

Image组件的插值效果interpolation默认为ImageInterpolation.None，可能会导致锯齿问题，因此可以通过设置interpolation为High/Medium/Low来减少锯齿效果。

**参考链接**

[ImageInterpolation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#imageinterpolation)

---
title: "Navigation中pushPathByName与pushDestinationByName的区别"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-264"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "UI框架"
  - "方舟UI框架（ArkUI）"
  - "Navigation中pushPathByName与pushDestinationByName的区别"
captured_at: "2026-04-17T02:03:05.472Z"
---

# Navigation中pushPathByName与pushDestinationByName的区别

[pushDestinationByName](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#pushdestinationbyname11)绑定上下文对象，调用时验证上下文是否一致，而[pushPathByName](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#pushpathbyname10)不进行验证。

不同的窗口，运行的UIContext不同。在单窗口场景下使用时，两者仅返回值存在差异；跨窗口使用时需注意UIContext的匹配性。

---
title: "Tabs组件，TabContent页面加载耗时，预加载未生效，怎么解决"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-452"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "UI框架"
  - "方舟UI框架（ArkUI）"
  - "Tabs组件，TabContent页面加载耗时，预加载未生效，怎么解决"
captured_at: "2026-04-17T02:03:07.720Z"
---

# Tabs组件，TabContent页面加载耗时，预加载未生效，怎么解决

**问题分析**

[aboutToAppear()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-custom-component-lifecycle#abouttoappear)被调用的时候Tabs组件尚未完成渲染，这会导致preloadItems方法预加载不存在的索引。

**解决方案**

TabContent中的[onWillShow()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabcontent#onwillshow12)方法能够实现预加载功能，但是Tabs每次切换时都会触发onWillShow()回调，需要做节流处理。

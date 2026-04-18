---
title: "Swiper左滑为什么会显示空白"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-467"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "UI框架"
  - "方舟UI框架（ArkUI）"
  - "Swiper左滑为什么会显示空白"
captured_at: "2026-04-17T02:03:07.817Z"
---

# Swiper左滑为什么会显示空白

由于[cachedCount](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#cachedcount15)的isShown设为true，预加载节点进行绘制，当缓存数大于swiper实际包含的子组件数量时，会把空白内容渲染在右节点树，导致左滑时出现空白，把cachedCount的isShown设为false可以解决该问题。

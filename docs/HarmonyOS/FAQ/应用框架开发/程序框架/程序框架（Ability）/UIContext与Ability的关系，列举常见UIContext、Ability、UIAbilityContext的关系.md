---
title: "UIContext与Ability的关系，列举常见UIContext、Ability、UIAbilityContext的关系"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-118"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "程序框架"
  - "程序框架（Ability）"
  - "UIContext与Ability的关系，列举常见UIContext、Ability、UIAbilityContext的关系"
captured_at: "2026-04-17T02:02:59.556Z"
---

# UIContext与Ability的关系，列举常见UIContext、Ability、UIAbilityContext的关系

1.  Ability的上下文是AbilityContext。ArkUI实例的上下文是[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface)，由窗口创建并管理所有UI对象。窗口可以通过[windowStage.loadContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#loadcontent9)拉起ArkUI实例。
2.  Ability是应用管理生命周期的对象，持有window对象。
3.  UIAbility的上下文是UIAbilityContext。UIContext与UIAbilityContext没有直接联系，无法互相转化。

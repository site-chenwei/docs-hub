---
title: "通过$r访问应用资源是否支持嵌套形式"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-102"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "UI框架"
  - "方舟UI框架（ArkUI）"
  - "通过$r访问应用资源是否支持嵌套形式"
captured_at: "2026-04-17T02:03:03.690Z"
---

# 通过$r访问应用资源是否支持嵌套形式

$r当前不支持嵌套。第二个参数需使用ResourceManager获取应用资源的字符串。参考代码如下：

@Entry
@Component
struct Page16 {
  context = this.getUIContext();

  build() {
    Row() {
      Column() {
        Text($r('app.string.EntryAbility1\_label2',
          this.context.getHostContext()!.resourceManager.getStringSync($r('app.string.EntryAbility\_label'))))// path: resources\\base\\element\\string.json
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
    }
    .height('100%')
  }
}

**参考链接**

[ResourceManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resource-manager#resourcemanager)

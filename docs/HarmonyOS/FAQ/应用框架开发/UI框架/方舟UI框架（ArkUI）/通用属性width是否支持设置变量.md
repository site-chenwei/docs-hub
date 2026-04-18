---
title: "通用属性width是否支持设置变量"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-191"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "UI框架"
  - "方舟UI框架（ArkUI）"
  - "通用属性width是否支持设置变量"
captured_at: "2026-04-17T02:03:04.638Z"
---

# 通用属性width是否支持设置变量

通用属性width支持设置变量。

@Entry
@Component
struct Page1 {
  @State message: string = 'Hello';
  @State widthNum: number = 300;

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .width(this.widthNum)
          .backgroundColor(Color.Blue)
      }
      .width('100%')
    }
    .height('100%')
  }
}

效果如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/n9Qqh76eT0e734qUCU14QQ/zh-cn_image_0000002194158632.png?HW-CC-KV=V1&HW-CC-Date=20260417T020306Z&HW-CC-Expire=86400&HW-CC-Sign=730AA6AA15231017B8AF856F934A57ED43FF5D81C2384A25E756E9ED42067F1B "点击放大")

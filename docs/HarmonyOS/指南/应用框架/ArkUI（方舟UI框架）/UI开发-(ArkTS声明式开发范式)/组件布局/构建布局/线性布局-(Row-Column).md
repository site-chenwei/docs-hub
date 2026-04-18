---
title: "线性布局 (Row/Column)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-linear"
menu_path:
  - "指南"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "UI开发 (ArkTS声明式开发范式)"
  - "组件布局"
  - "构建布局"
  - "线性布局 (Row/Column)"
captured_at: "2026-04-17T01:35:37.408Z"
---

# 线性布局 (Row/Column)

#### 概述

线性布局（LinearLayout）是开发中最常用的布局，通过线性容器[Row](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-row)和[Column](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column)构建。线性布局是其他布局的基础，其子元素在线性方向上（水平方向和垂直方向）依次排列。线性布局的排列方向由所选容器组件决定，Row容器内子元素按照水平方向排列，Column容器内子元素按照垂直方向排列。根据不同的排列方向，开发者可选择使用Row或Column容器创建线性布局。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/xzkpSkO7Tm-R5Om-aBzb7A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=ED20A873A1C6A7AD349BC0FB0575FA0FBD86C626FC1C7B64F91683B535205961)

在复杂界面中使用多组件嵌套时，若布局组件的嵌套层数过深或嵌套的组件数量过多，将会产生额外开销。建议通过移除冗余节点、利用布局边界减少布局计算、合理采用渲染控制语法及布局组件方法来优化性能。最佳实践请参考[布局优化指导](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-improve-layout-performance)。

**图1** Column容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/IXb5qfFJT9O-00pn_EdxuQ/zh-cn_image_0000002569018331.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=EB9FB1B35B772794D56F1F65C0D57D8C75E616953BC37E8E3B4E66A25DA1FB97)

**图2** Row容器内子元素排列示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/ioME4x-tT0GHuvUbjmDjoQ/zh-cn_image_0000002568898323.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=67BBAEE7D2335863D976D0B4744364A48CF60483B9804C040773799CA04BBD26)

#### 基本概念

-   布局容器：具有布局能力的容器组件，可以承载其他元素作为其子元素，布局容器会对其子元素进行尺寸计算和布局排列。
    
-   布局子元素：布局容器内部的元素。
    
-   主轴：线性布局容器在布局方向上的轴线，子元素默认沿主轴排列。Row容器主轴为水平方向，Column容器主轴为垂直方向（图示可参考弹性布局[基本概念](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-flex-layout#基本概念)中的主轴）。
    
-   交叉轴：垂直于主轴方向的轴线。Row容器交叉轴为垂直方向，Column容器交叉轴为水平方向（图示可参考弹性布局[基本概念](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-flex-layout#基本概念)中的交叉轴）。
    
-   间距：布局子元素的间距。
    

#### 布局子元素在排列方向上的间距

在布局容器内，可以通过space属性设置排列方向上子元素的间距，使各子元素在排列方向上有等间距效果。

#### \[h2\]Column容器内排列方向上的间距

**图3** Column容器内排列方向的间距图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/WoW_rtuzTX-PsLCkicX-5Q/zh-cn_image_0000002538018618.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=D701B9E6A2D44788929E9EAF9337543156EC2479A939F12C430FAEEBB56DCD64)

Column({ space: 20 }) {
  Text('space: 20').fontSize(15).fontColor(Color.Gray).width('90%')
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
  Row().width('90%').height(50).backgroundColor(0xD2B48C)
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
}.width('100%')

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/XO0hptAxSpOvm8mF0juNoQ/zh-cn_image_0000002538178544.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=8DE664439B6BC8E24D1723B65304B2444A18D53CDFD56196F1D716BD13BD2474)

#### \[h2\]Row容器内排列方向上的间距

**图4** Row容器内排列方向的间距图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/SFTeCZSyR-a0zv3MfO2rZA/zh-cn_image_0000002569018333.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=45CC55DABF7EB94060D0D73A578A461DD2CCE7C8BC4E60950220BC2DDAAB1DEA)

Row({ space: 35 }) {
  Text('space: 35').fontSize(15).fontColor(Color.Gray)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
  Row().width('10%').height(150).backgroundColor(0xD2B48C)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
}.width('90%')

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/fkHcXgEgR-Wmj1R7W9Wfiw/zh-cn_image_0000002568898325.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=EC24B161CFF20ECD3A196E70E3FA2984E372AC8BFCF30E0981816E2567CABABF)

#### 布局子元素在主轴上的排列方式

在布局容器内，可以通过[justifyContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column#justifycontent8)属性设置子元素在容器主轴上的排列方式。可以从主轴起始位置开始排布，也可以从主轴结束位置开始排布，或者均匀分割主轴的空间。

#### \[h2\]Column容器内子元素在垂直方向上的排列

**图5** Column容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/NVmH9DpbTa6H-KiP0EI6EA/zh-cn_image_0000002538018620.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=EE22728EF6F1E1149F15E35696B6189552532F74DD2ABE3EDE432733493A6FBE)

-   justifyContent(FlexAlign.Start，默认值)：元素在垂直方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。
    
    Column({}) {
      Column() {
      }.width('80%').height(50).backgroundColor(0xF5DEB3)
    
      Column() {
      }.width('80%').height(50).backgroundColor(0xD2B48C)
    
      Column() {
      }.width('80%').height(50).backgroundColor(0xF5DEB3)
    }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/-jA3EJ-oRcekwJkTRP5vtQ/zh-cn_image_0000002538178546.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=65A9D477949C3DA6CC923D282A0E701C59B2836AEDA57252918F8C737EF45904)
    
-   justifyContent(FlexAlign.Center)：元素在垂直方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。
    
    Column({}) {
      Column() {
      }.width('80%').height(50).backgroundColor(0xF5DEB3)
    
      Column() {
      }.width('80%').height(50).backgroundColor(0xD2B48C)
    
      Column() {
      }.width('80%').height(50).backgroundColor(0xF5DEB3)
    }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/jq51uIehR3qcJAnsvza3yg/zh-cn_image_0000002569018335.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=668D6A6E1039ADF95FA9FA1E3ACD5E09962016D25125FF791498AA9A73286D93)
    
-   justifyContent(FlexAlign.End)：元素在垂直方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。
    
    Column({}) {
      Column() {
      }.width('80%').height(50).backgroundColor(0xF5DEB3)
    
      Column() {
      }.width('80%').height(50).backgroundColor(0xD2B48C)
    
      Column() {
      }.width('80%').height(50).backgroundColor(0xF5DEB3)
    }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/wm8Fc9XbRTiXlAqoEzEGuw/zh-cn_image_0000002568898327.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=5AF0925CB14378CC56A3DE1D6BB35A30D1E40E82E811D2A695986A8968C8AEF5)
    
-   justifyContent(FlexAlign.SpaceBetween)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。
    
    Column({}) {
      Column() {
      }.width('80%').height(50).backgroundColor(0xF5DEB3)
    
      Column() {
      }.width('80%').height(50).backgroundColor(0xD2B48C)
    
      Column() {
      }.width('80%').height(50).backgroundColor(0xF5DEB3)
    }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/7f-9IrbVSmyUmzWt_ZJPeA/zh-cn_image_0000002538018622.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=6CBFA2091771E05C72CC53C20059AD5A48F287D73EB087FC530C5630001C9D58)
    
-   justifyContent(FlexAlign.SpaceAround)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。
    
    Column({}) {
      Column() {
      }.width('80%').height(50).backgroundColor(0xF5DEB3)
    
      Column() {
      }.width('80%').height(50).backgroundColor(0xD2B48C)
    
      Column() {
      }.width('80%').height(50).backgroundColor(0xF5DEB3)
    }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/ZfFRz3aSRISIS22h1OSM4g/zh-cn_image_0000002538178550.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=5513D13DB3975235777D4A9E1A36F4806082F5C44019BF853E3C8FE6FC6BA6C4)
    
-   justifyContent(FlexAlign.SpaceEvenly)：垂直方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。
    
    Column({}) {
      Column() {
      }.width('80%').height(50).backgroundColor(0xF5DEB3)
    
      Column() {
      }.width('80%').height(50).backgroundColor(0xD2B48C)
    
      Column() {
      }.width('80%').height(50).backgroundColor(0xF5DEB3)
    }.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/Uli84bQVQSCVR65YCTDrng/zh-cn_image_0000002569018337.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=804FE10FCF8E9E6FB95FA973099C71EBC2F9A2B72FB8E29383990F5FB4AC03DD)
    

#### \[h2\]Row容器内子元素在水平方向上的排列

**图6** Row容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/1rVSCc3IQfm4Z2jTEqvdCA/zh-cn_image_0000002568898329.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=01C1BFDF06B1C32F06D9144EABF0147F8F8BFDC20F9AF7CC6F3E42CF9F269DBD)

-   justifyContent(FlexAlign.Start，默认值)：元素在水平方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。
    
    Row({}) {
      Column() {
      }.width('20%').height(30).backgroundColor(0xF5DEB3)
    
      Column() {
      }.width('20%').height(30).backgroundColor(0xD2B48C)
    
      Column() {
      }.width('20%').height(30).backgroundColor(0xF5DEB3)
    }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/HoKqrFKORuCKcRaxQ4g8Aw/zh-cn_image_0000002538018624.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=53CA8787ED5D0F108B8661515077D0265F51FB1475CAC2FBA6473B0E2B62FD94)
    
-   justifyContent(FlexAlign.Center)：元素在水平方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。
    
    Row({}) {
      Column() {
      }.width('20%').height(30).backgroundColor(0xF5DEB3)
    
      Column() {
      }.width('20%').height(30).backgroundColor(0xD2B48C)
    
      Column() {
      }.width('20%').height(30).backgroundColor(0xF5DEB3)
    }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/RFZ6Z57STxKKE7yRbSrw9Q/zh-cn_image_0000002538178552.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=6BAEEF47DC6DE50DA4CFCE2FF28EEDF4B9EBE0F0ABDBEB289C2F454C241EFEDD)
    
-   justifyContent(FlexAlign.End)：元素在水平方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。
    
    Row({}) {
      Column() {
      }.width('20%').height(30).backgroundColor(0xF5DEB3)
    
      Column() {
      }.width('20%').height(30).backgroundColor(0xD2B48C)
    
      Column() {
      }.width('20%').height(30).backgroundColor(0xF5DEB3)
    }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/fiBrTH0cQxKGhqdx3w8GUw/zh-cn_image_0000002569018339.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=76B0ADE85A81B9A78BAEBE987EFAD612E19C8C0F6705D27692C65FA3E9AFC415)
    
-   justifyContent(FlexAlign.SpaceBetween)：水平方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。
    
    Row({}) {
      Column() {
      }.width('20%').height(30).backgroundColor(0xF5DEB3)
    
      Column() {
      }.width('20%').height(30).backgroundColor(0xD2B48C)
    
      Column() {
      }.width('20%').height(30).backgroundColor(0xF5DEB3)
    }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/0pcXd7PtS-CXO1wEA_svFQ/zh-cn_image_0000002568898331.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=FF07F924E0D0A061E5C9DD42B0BDEA5A971C790F6C8F1F70ED56E55AEE46568A)
    
-   justifyContent(FlexAlign.SpaceAround)：水平方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。
    
    Row({}) {
      Column() {
      }.width('20%').height(30).backgroundColor(0xF5DEB3)
    
      Column() {
      }.width('20%').height(30).backgroundColor(0xD2B48C)
    
      Column() {
      }.width('20%').height(30).backgroundColor(0xF5DEB3)
    }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/IHLn9tOzTdOBKAAhl5Hj_Q/zh-cn_image_0000002538018626.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=31F3326071A648CADF084FBDCF975047D60A1DA0A913394C51B8AE6267E5AF2B)
    
-   justifyContent(FlexAlign.SpaceEvenly)：水平方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。
    
    Row({}) {
      Column() {
      }.width('20%').height(30).backgroundColor(0xF5DEB3)
    
      Column() {
      }.width('20%').height(30).backgroundColor(0xD2B48C)
    
      Column() {
      }.width('20%').height(30).backgroundColor(0xF5DEB3)
    }.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/CacMz1opR_OAHuMziIbisA/zh-cn_image_0000002538178554.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=66489095C2C9754F768E742FAAB7AB7E6AC211FFC0E5BD138C821FF4CF9CCE4B)
    

#### 布局子元素在交叉轴上的对齐方式

在布局容器内，可以通过[alignItems](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column#alignitems)属性设置子元素在交叉轴（排列方向的垂直方向）上的对齐方式，且在各类尺寸屏幕中表现一致。其中，交叉轴为垂直方向时，取值为[VerticalAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#verticalalign)类型，水平方向取值为[HorizontalAlign](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#horizontalalign)类型。

[alignSelf](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout#alignself)属性用于控制单个子元素在容器交叉轴上的对齐方式，其优先级高于alignItems属性，如果设置了alignSelf属性，则在单个子元素上会覆盖alignItems属性。

#### \[h2\]Column容器内子元素在水平方向上的排列

**图7** Column容器内子元素在水平方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/7Vx9NyfXRJGVPULGizdXZw/zh-cn_image_0000002569018341.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=026DB4EF2FE1F1638D4AF0EE6E47C054C0DB88FA709DDA9C7E30556518FFBE6C)

-   HorizontalAlign.Start：子元素在水平方向左对齐。
    
    Column({}) {
      Column() {
      }.width('80%').height(50).backgroundColor(0xF5DEB3)
    
      Column() {
      }.width('80%').height(50).backgroundColor(0xD2B48C)
    
      Column() {
      }.width('80%').height(50).backgroundColor(0xF5DEB3)
    }.width('100%').alignItems(HorizontalAlign.Start).backgroundColor('rgb(242,242,242)')
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/ZQbwvVFzQDe55FI7wQYnLA/zh-cn_image_0000002568898333.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=FFE0EA87F5D2E57BB640D6C0294A008900E8374C540A9501532BF7862B3E78A5)
    
-   HorizontalAlign.Center（默认值）：子元素在水平方向居中对齐。
    
    Column({}) {
      Column() {
      }.width('80%').height(50).backgroundColor(0xF5DEB3)
    
      Column() {
      }.width('80%').height(50).backgroundColor(0xD2B48C)
    
      Column() {
      }.width('80%').height(50).backgroundColor(0xF5DEB3)
    }.width('100%').alignItems(HorizontalAlign.Center).backgroundColor('rgb(242,242,242)')
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/tEnxCqoWR62m2W5A1nYYcA/zh-cn_image_0000002538018628.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=681EBC79395E447C5654DFC3CBA222F9A3452061913266D0B929ED8A9EE296A3)
    
-   HorizontalAlign.End：子元素在水平方向右对齐。
    
    Column({}) {
      Column() {
      }.width('80%').height(50).backgroundColor(0xF5DEB3)
    
      Column() {
      }.width('80%').height(50).backgroundColor(0xD2B48C)
    
      Column() {
      }.width('80%').height(50).backgroundColor(0xF5DEB3)
    }.width('100%').alignItems(HorizontalAlign.End).backgroundColor('rgb(242,242,242)')
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/y3WO2wlsQfa3LpF5RS7aIA/zh-cn_image_0000002538178556.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=B7EC9AF796F632A4D020BDB29EA5EA4348F192E3CD5176639888C89A38FD4164)
    

#### \[h2\]Row容器内子元素在垂直方向上的排列

**图8** Row容器内子元素在垂直方向上的排列图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/F_0eFT8sQD6MuBWDidWndA/zh-cn_image_0000002569018343.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=6E54125CBAB05FD8B093FD1CE0C1EC8BAC38EDDB6D75B8928FB25C5E8F452E7A)

-   VerticalAlign.Top：子元素在垂直方向顶部对齐。
    
    Row({}) {
      Column() {
      }.width('20%').height(30).backgroundColor(0xF5DEB3)
    
      Column() {
      }.width('20%').height(30).backgroundColor(0xD2B48C)
    
      Column() {
      }.width('20%').height(30).backgroundColor(0xF5DEB3)
    }.width('100%').height(200).alignItems(VerticalAlign.Top).backgroundColor('rgb(242,242,242)')
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/7YDX-OhrTOS-iZwxeVdJtg/zh-cn_image_0000002568898335.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=E903B6D593A89750BD97618AB554E3B9744978696FA708B403B0835DD07CD43A)
    
-   VerticalAlign.Center（默认值）：子元素在垂直方向居中对齐。
    
    Row({}) {
      Column() {
      }.width('20%').height(30).backgroundColor(0xF5DEB3)
    
      Column() {
      }.width('20%').height(30).backgroundColor(0xD2B48C)
    
      Column() {
      }.width('20%').height(30).backgroundColor(0xF5DEB3)
    }.width('100%').height(200).alignItems(VerticalAlign.Center).backgroundColor('rgb(242,242,242)')
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/9ORRGBDPTV-94-nqEa4R0g/zh-cn_image_0000002538018630.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=52AF6B703264B19F4AD880E145AFAA7F32ED898C2F817D9CDBE95AE962B0FA10)
    
-   VerticalAlign.Bottom：子元素在垂直方向底部对齐。
    
    Row({}) {
      Column() {
      }.width('20%').height(30).backgroundColor(0xF5DEB3)
    
      Column() {
      }.width('20%').height(30).backgroundColor(0xD2B48C)
    
      Column() {
      }.width('20%').height(30).backgroundColor(0xF5DEB3)
    }.width('100%').height(200).alignItems(VerticalAlign.Bottom).backgroundColor('rgb(242,242,242)')
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/odbUgAMWTfqhpVtGteynxA/zh-cn_image_0000002538178558.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=60147463978836A9D960B8D5502241DE189159D46FF2BBDCAB0E6E1C6DC38FAF)
    

#### 自适应拉伸

在线性布局下，常用空白填充组件[Blank](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-blank)，在容器主轴方向自动填充空白空间，达到自适应拉伸效果。Row和Column作为容器，只需要添加宽高为百分比，当屏幕宽高发生变化时，会产生自适应效果。

@Entry
@Component
struct BlankExample {
  build() {
    Column() {
      Row() {
        Text('Bluetooth').fontSize(18)
        Blank()
        Toggle({ type: ToggleType.Switch, isOn: true })
      }.backgroundColor(0xFFFFFF).borderRadius(15).padding({ left: 12 }).width('100%')
    }.backgroundColor(0xEFEFEF).padding(20).width('100%')
  }
}

**图9** 竖屏（自适应屏幕窄边）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/mo42soZ9T1-0GiDrD5IhDg/zh-cn_image_0000002569018345.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=D9BE1B6F60E0BEA35FF124F3E5CF8DC613577F0DDAA8E884F5102E01533BB597)

**图10** 横屏（自适应屏幕宽边）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/ceOX-gWBQ02d2hMdH7LsNw/zh-cn_image_0000002568898337.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=D2F49E6508965D15378A8D1FF18121F80C5C2B45ADF5D1990ACAEE2B2F519ADE)

#### 自适应缩放

自适应缩放是指子元素随容器尺寸的变化而按照预设的比例自动调整尺寸，适应各种不同大小的设备。在线性布局中，可以使用以下两种方法实现自适应缩放。

-   父容器尺寸确定时，使用[layoutWeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#layoutweight)属性设置子元素和兄弟元素在主轴上的权重，忽略元素本身尺寸设置，使它们在任意尺寸的设备下自适应占满剩余空间。
    
    @Entry
    @Component
    struct LayoutWeightExample {
      build() {
        Column() {
          Text('1:2:3').width('100%')
          Row() {
            Column() {
              Text('layoutWeight(1)')
                .textAlign(TextAlign.Center)
            }.layoutWeight(1).backgroundColor(0xF5DEB3).height('100%')
    
            Column() {
              Text('layoutWeight(2)')
                .textAlign(TextAlign.Center)
            }.layoutWeight(2).backgroundColor(0xD2B48C).height('100%')
    
            Column() {
              Text('layoutWeight(3)')
                .textAlign(TextAlign.Center)
            }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')
    
          }.backgroundColor(0xffd306).height('30%')
    
          Text('2:5:3').width('100%')
          Row() {
            Column() {
              Text('layoutWeight(2)')
                .textAlign(TextAlign.Center)
            }.layoutWeight(2).backgroundColor(0xF5DEB3).height('100%')
    
            Column() {
              Text('layoutWeight(5)')
                .textAlign(TextAlign.Center)
            }.layoutWeight(5).backgroundColor(0xD2B48C).height('100%')
    
            Column() {
              Text('layoutWeight(3)')
                .textAlign(TextAlign.Center)
            }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')
          }.backgroundColor(0xffd306).height('30%')
        }
      }
    }
    
    **图11** 横屏
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/uC9jiiduTEyyuz50fk-kMA/zh-cn_image_0000002538018632.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=4D639B165D0279ED18085B37E19DEBB2112237AA0DA7C6B91E97AF9E33D6482B)
    
    **图12** 竖屏
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/9smATudCRhqPU6k2xL3LdA/zh-cn_image_0000002538178560.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=40F1059E6D00E6D533B35DF565A3D1ACA62B0E43E68DECDE399D004B60D8CD9D)
    
-   父容器尺寸确定时，使用百分比设置子元素和兄弟元素的宽度，使他们在任意尺寸的设备下保持固定的自适应占比。
    
    @Entry
    @Component
    struct WidthExample {
      build() {
        Column() {
          Row() {
            Column() {
              Text('left width 20%')
                .textAlign(TextAlign.Center)
            }.width('20%').backgroundColor(0xF5DEB3).height('100%')
    
            Column() {
              Text('center width 50%')
                .textAlign(TextAlign.Center)
            }.width('50%').backgroundColor(0xD2B48C).height('100%')
    
            Column() {
              Text('right width 30%')
                .textAlign(TextAlign.Center)
            }.width('30%').backgroundColor(0xF5DEB3).height('100%')
          }.backgroundColor(0xffd306).height('30%')
        }
      }
    }
    
    **图13** 横屏
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/spR4cmbKQOeWWsN5mKitww/zh-cn_image_0000002569018347.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=086EDB02A5979E16751210A11A4D4483371C9762CADC54B521811CBD4B28DDAE)
    
    **图14** 竖屏
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/VmcNRd4RRcaKLY-DwNX0yQ/zh-cn_image_0000002568898339.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=644F81652B9D4F471D4ADE08237090B20634FC55B3A6BE3E663212E3DC2A0DC6)
    

#### 自适应延伸

自适应延伸是指在不同尺寸设备下，当页面的内容超出屏幕大小而无法完全显示时，可以通过滚动条进行拖动展示。对于线性布局，这种方法适用于容器中内容无法一屏展示的场景。通常有以下两种实现方式。

-   [在List中添加滚动条](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-list#添加滚动条)：当List子项过多一屏放不下时，可以将每一项子元素放置在不同的组件中，通过滚动条进行拖动展示。可以通过[scrollBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#scrollbar)属性设置滚动条的常驻状态，[edgeEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll#edgeeffect)属性设置拖动到内容最末端的回弹效果。
    
-   使用[Scroll](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll)组件：在线性布局中，开发者可以进行垂直方向或者水平方向的布局。当一屏无法完全显示时，可以在Column或Row组件的外层包裹一个可滚动的容器组件Scroll来实现可滑动的线性布局。
    
    垂直方向布局中使用Scroll组件：
    
    @Entry
    @Component
    struct ScrollVerticalExample {
      scroller: Scroller = new Scroller();
      private arr: number\[\] = \[0, 1, 2, 3, 4, 5, 6, 7, 8, 9\];
    
      build() {
        Scroll(this.scroller) {
          Column() {
            ForEach(this.arr, (item?:number|undefined) => {
              if(item != undefined){
                Text(item.toString())
                  .width('90%')
                  .height(150)
                  .backgroundColor(0xFFFFFF)
                  .borderRadius(15)
                  .fontSize(16)
                  .textAlign(TextAlign.Center)
                  .margin({ top: 10 })
              }
            }, (item:number) => item.toString())
          }.width('100%')
        }
        .backgroundColor(0xDCDCDC)
        .scrollable(ScrollDirection.Vertical) // 滚动方向为垂直方向
        .scrollBar(BarState.On) // 滚动条常驻显示
        .scrollBarColor(Color.Gray) // 滚动条颜色
        .scrollBarWidth(10) // 滚动条宽度
        .edgeEffect(EdgeEffect.Spring) // 滚动到边沿后回弹
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/D2uMAg70SimweT2LCiE01Q/zh-cn_image_0000002538018634.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=22FA277EB8EF5D299531C0710BCE86777EB960B9CA451E2BFC8965D7B8050819)
    
    水平方向布局中使用Scroll组件：
    
    @Entry
    @Component
    struct ScrollHorizontalExample {
      scroller: Scroller = new Scroller();
      private arr: number\[\] = \[0, 1, 2, 3, 4, 5, 6, 7, 8, 9\];
    
      build() {
        Scroll(this.scroller) {
          Row() {
            ForEach(this.arr, (item?:number|undefined) => {
              if(item != undefined){
                Text(item.toString())
                  .height('90%')
                  .width(150)
                  .backgroundColor(0xFFFFFF)
                  .borderRadius(15)
                  .fontSize(16)
                  .textAlign(TextAlign.Center)
                  .margin({ left: 10 })
              }
            })
          }.height('100%')
        }
        .backgroundColor(0xDCDCDC)
        .scrollable(ScrollDirection.Horizontal) // 滚动方向为水平方向
        .scrollBar(BarState.On) // 滚动条常驻显示
        .scrollBarColor(Color.Gray) // 滚动条颜色
        .scrollBarWidth(10) // 滚动条宽度
        .edgeEffect(EdgeEffect.Spring) // 滚动到边沿后回弹
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/AnlH95ubTUetdSdp-Nr3VQ/zh-cn_image_0000002538178562.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=82834B6B4CFE022C8327E6ECC2F5D641EC5D57C4DF0CA40F1C5D3CF5E0AF62EB)

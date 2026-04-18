---
title: "弹性布局 (Flex)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-flex-layout"
menu_path:
  - "指南"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "UI开发 (ArkTS声明式开发范式)"
  - "组件布局"
  - "构建布局"
  - "弹性布局 (Flex)"
captured_at: "2026-04-17T01:35:37.422Z"
---

# 弹性布局 (Flex)

#### 概述

弹性布局（[Flex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex)）提供更加有效的方式对容器中的子元素进行排列、对齐和分配剩余空间。常用于页面头部导航栏的均匀分布、页面框架的搭建、多行数据的排列等。

容器默认存在主轴与交叉轴，子元素默认沿主轴排列，子元素在主轴方向的尺寸称为主轴尺寸，在交叉轴方向的尺寸称为交叉轴尺寸。

**图1** 主轴为水平方向的Flex容器示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/YQ9xoboYSvqy2_2i0X8Pfw/zh-cn_image_0000002538018638.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=92BDA1C9100192F40AF842D29C6BA0C9F67A8DCBF13805D0279B1DABB8646FDB)

#### 基本概念

-   主轴：Flex组件布局方向的轴线，子元素默认沿着主轴排列。主轴开始的位置称为主轴起始点，结束位置称为主轴结束点。
    
-   交叉轴：垂直于主轴方向的轴线。交叉轴开始的位置称为交叉轴起始点，结束位置称为交叉轴结束点。
    

#### 布局方向

在弹性布局中，容器的子元素可以按照任意方向排列。通过设置[FlexOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex#flexoptions对象说明)的参数direction，可以决定主轴的方向，从而控制子元素的排列方向。

**图2** 弹性布局方向图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/Gkko1mV1TZuA1EozhaqpNw/zh-cn_image_0000002538178566.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=45DFE2F83499CB6F713E5396B3554B0B80E6B6607B3D8CB9DCD76C32B0244742)

-   FlexDirection.Row（默认值）：主轴为水平方向，子元素从起始端沿着水平方向开始排布。
    
    Flex({ direction: FlexDirection.Row }) {
      Text('1').width('33%').height(50).backgroundColor('#F5DEB3')
      Text('2').width('33%').height(50).backgroundColor('#D2B48C')
      Text('3').width('33%').height(50).backgroundColor('#F5DEB3')
    }
    .height(70)
    .width('90%')
    .padding(10)
    .backgroundColor('#AFEEEE')
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/fHg3c4KaQ7ivQanoSzcqyQ/zh-cn_image_0000002569018353.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=E836F1F05097CD71BE8C825A7F43DEDD4130803BE23102AF327D6A32CEAF018E)
    
-   FlexDirection.RowReverse：主轴为水平方向，子元素从终点端沿着FlexDirection.Row相反的方向开始排布。
    
    Flex({ direction: FlexDirection.RowReverse }) {
      Text('1').width('33%').height(50).backgroundColor('#F5DEB3')
      Text('2').width('33%').height(50).backgroundColor('#D2B48C')
      Text('3').width('33%').height(50).backgroundColor('#F5DEB3')
    }
    .height(70)
    .width('90%')
    .padding(10)
    .backgroundColor('#AFEEEE')
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/ZqINLxxxSvGYYoGCzDmD3w/zh-cn_image_0000002568898345.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=215AF5A099C4FC63356D1CD19770CE9C0E43093650F03EB406CA1B7A2D5C136E)
    
-   FlexDirection.Column：主轴为垂直方向，子元素从起始端沿着垂直方向开始排布。
    
    Flex({ direction: FlexDirection.Column }) {
      Text('1').width('100%').height(50).backgroundColor('#F5DEB3')
      Text('2').width('100%').height(50).backgroundColor('#D2B48C')
      Text('3').width('100%').height(50).backgroundColor('#F5DEB3')
    }
    .height(70)
    .width('90%')
    .padding(10)
    .backgroundColor('#AFEEEE')
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/5FXKZ2stQDazE6A5WSmGvg/zh-cn_image_0000002538018640.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=D2F31A8EE7323D83E5D390301509347072DD7C14D5F8E6D6DD069177FA73C8AD)
    
-   FlexDirection.ColumnReverse：主轴为垂直方向，子元素从终点端沿着FlexDirection.Column相反的方向开始排布。
    
    Flex({ direction: FlexDirection.ColumnReverse }) {
      Text('1').width('100%').height(50).backgroundColor('#F5DEB3')
      Text('2').width('100%').height(50).backgroundColor('#D2B48C')
      Text('3').width('100%').height(50).backgroundColor('#F5DEB3')
    }
    .height(70)
    .width('90%')
    .padding(10)
    .backgroundColor('#AFEEEE')
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/K9LcaU_hTS-9Rzl0Ns1hcA/zh-cn_image_0000002538178568.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=B092AACC79DD79AB192FA491765C66432DAD940F32EB4D27D16887187FA432D7)
    

#### 布局换行

弹性布局分为单行布局和多行布局。默认情况下，Flex容器中的子元素都排在一条线（又称“轴线”）上。wrap属性控制当子元素主轴尺寸之和大于容器主轴尺寸时，Flex是单行布局还是多行布局。在多行布局时，通过交叉轴方向，确认新行排列方向。

-   FlexWrap.NoWrap（默认值）：不换行。如果子元素的宽度总和大于父元素的宽度，则子元素会被压缩宽度。
    
    Flex({ wrap: FlexWrap.NoWrap }) {
      Text('1').width('50%').height(50).backgroundColor('#F5DEB3')
      Text('2').width('50%').height(50).backgroundColor('#D2B48C')
      Text('3').width('50%').height(50).backgroundColor('#F5DEB3')
    }
    .width('90%')
    .padding(10)
    .backgroundColor('#AFEEEE')
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/AhSZbBNiStSHEYw8fgNmdg/zh-cn_image_0000002569018355.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=F9B9173502AFB776562B25DF914CECD27DE7541FECF48704EDE93CF0F4AA853C)
    
-   FlexWrap.Wrap：换行，每一行子元素按照主轴方向排列。
    
    Flex({ wrap: FlexWrap.Wrap }) {
      Text('1').width('50%').height(50).backgroundColor('#F5DEB3')
      Text('2').width('50%').height(50).backgroundColor('#D2B48C')
      Text('3').width('50%').height(50).backgroundColor('#D2B48C')
    }
    .width('90%')
    .padding(10)
    .backgroundColor('#AFEEEE')
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/IiMQrCVdRsy1uCpKALY4Pw/zh-cn_image_0000002568898347.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=0022BA0450EF89CF452C65C73C2284D428D6D197D5915A7D6C5AF3A2AAC80F17)
    
-   FlexWrap.WrapReverse：换行，每一行子元素按照主轴反方向排列。
    
    Flex({ wrap: FlexWrap.WrapReverse}) {
      Text('1').width('50%').height(50).backgroundColor('#F5DEB3')
      Text('2').width('50%').height(50).backgroundColor('#D2B48C')
      Text('3').width('50%').height(50).backgroundColor('#F5DEB3')
    }
    .width('90%')
    .padding(10)
    .backgroundColor('#AFEEEE')
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/yPHTi7gGT9CVE9G5kZKelA/zh-cn_image_0000002538018642.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=0B4F63F000FDDCBFC1004CB0E28405532D80D46B27A5ED90EE4EE9BDDE7663AE)
    

#### 主轴对齐方式

通过justifyContent参数设置子元素在主轴方向的对齐方式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/MK18RnDpRaOUUFnjgTbRoQ/zh-cn_image_0000002538178570.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=96CE3522C366D6639070E2A44A3A2B77CDB9E44B9BED3B90E40F0D1C8A899DCE)

-   FlexAlign.Start（默认值）：子元素在主轴方向起始端对齐， 第一个子元素与父元素边沿对齐，其他元素与前一个元素对齐。
    
    Flex({ justifyContent: FlexAlign.Start }) {
      Text('1').width('20%').height(50).backgroundColor('#F5DEB3')
      Text('2').width('20%').height(50).backgroundColor('#D2B48C')
      Text('3').width('20%').height(50).backgroundColor('#F5DEB3')
    }
    .width('90%')
    .padding({ top: 10, bottom: 10 })
    .backgroundColor('#AFEEEE')
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/54XW0-y0Q9O5PjL_bnDjQA/zh-cn_image_0000002569018357.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=C4BBD45B070344964468C9DD8C250F4BB4BEEB33EBC96771AF52224807975C28)
    
-   FlexAlign.Center：子元素在主轴方向居中对齐。
    
    Flex({ justifyContent: FlexAlign.Center }) {
      Text('1').width('20%').height(50).backgroundColor('#F5DEB3')
      Text('2').width('20%').height(50).backgroundColor('#D2B48C')
      Text('3').width('20%').height(50).backgroundColor('#F5DEB3')
    }
    .width('90%')
    .padding({ top: 10, bottom: 10 })
    .backgroundColor('#AFEEEE')
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/JuaLGM_ESiGCrfHffySfpw/zh-cn_image_0000002568898349.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=7CB4E6555F00BFB193FF86F24FB49A4A7915FFB7AAD8DD412F19204C3C482200)
    
-   FlexAlign.End：子元素在主轴方向终点端对齐，最后一个子元素与父元素边沿对齐，其他元素与后一个元素对齐。
    
    Flex({ justifyContent: FlexAlign.End }) {
      Text('1').width('20%').height(50).backgroundColor('#F5DEB3')
      Text('2').width('20%').height(50).backgroundColor('#D2B48C')
      Text('3').width('20%').height(50).backgroundColor('#F5DEB3')
    }
    .width('90%')
    .padding({ top: 10, bottom: 10 })
    .backgroundColor('#AFEEEE')
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/BtYVB4zyQMeDsf-78EpmIA/zh-cn_image_0000002538018644.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=88778AA73FAF7C822DB4CD63276195C865966EAE88C3B350E7EFC5FC8B989063)
    
-   FlexAlign.SpaceBetween：Flex主轴方向均匀分配弹性元素，相邻子元素之间距离相同。第一个子元素和最后一个子元素与父元素边沿对齐。
    
    Flex({ justifyContent: FlexAlign.SpaceBetween }) {
      Text('1').width('20%').height(50).backgroundColor('#F5DEB3')
      Text('2').width('20%').height(50).backgroundColor('#D2B48C')
      Text('3').width('20%').height(50).backgroundColor('#F5DEB3')
    }
    .width('90%')
    .padding({ top: 10, bottom: 10 })
    .backgroundColor('#AFEEEE')
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/Y031X0ofTbGuLposilveKA/zh-cn_image_0000002538178572.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=3F95E5C00219CE0305FA29CF9A3856A5F1BABA3F94830AFA2FA8A3C16543C07D)
    
-   FlexAlign.SpaceAround：Flex主轴方向均匀分配弹性元素，相邻子元素之间距离相同。第一个子元素到主轴起始端的距离和最后一个子元素到主轴终点端的距离是相邻元素之间距离的一半。
    
    Flex({ justifyContent: FlexAlign.SpaceAround }) {
      Text('1').width('20%').height(50).backgroundColor('#F5DEB3')
      Text('2').width('20%').height(50).backgroundColor('#D2B48C')
      Text('3').width('20%').height(50).backgroundColor('#F5DEB3')
    }
    .width('90%')
    .padding({ top: 10, bottom: 10 })
    .backgroundColor('#AFEEEE')
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/Ev5bzVyQSg-E6KyiWQMEzw/zh-cn_image_0000002569018359.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=05706E1F2C4000ED78EDCC5327B9041BEC834A60744E26D7C81E8EE80BA5634C)
    
-   FlexAlign.SpaceEvenly：Flex主轴方向元素等间距布局，相邻子元素之间的间距、第一个子元素与主轴起始端的间距、最后一个子元素到主轴终点端的间距均相等。
    
    Flex({ justifyContent: FlexAlign.SpaceEvenly }) {
      Text('1').width('20%').height(50).backgroundColor('#F5DEB3')
      Text('2').width('20%').height(50).backgroundColor('#D2B48C')
      Text('3').width('20%').height(50).backgroundColor('#F5DEB3')
    }
    .width('90%')
    .padding({ top: 10, bottom: 10 })
    .backgroundColor('#AFEEEE')
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/tzOmfbF0QlqM_fMELFkgjw/zh-cn_image_0000002568898351.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=3CFE538F6039884367B334CDC24059F28FF5DF1D63FB6182B4278EA4F35051D4)
    

#### 交叉轴对齐方式

容器和子元素都可以设置交叉轴对齐方式，且子元素设置的对齐方式优先级较高。

#### \[h2\]容器组件设置交叉轴对齐

可以通过设置[FlexOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex#flexoptions对象说明)的参数alignItems，设置子元素在交叉轴的对齐方式。

-   ItemAlign.Auto：使用Flex容器中默认配置。
    
    Flex({ alignItems: ItemAlign.Auto }) {
      Text('1').width('33%').height(30).backgroundColor('#F5DEB3')
      Text('2').width('33%').height(40).backgroundColor('#D2B48C')
      Text('3').width('33%').height(50).backgroundColor('#F5DEB3')
    }
    .size({ width: '90%', height: 80 })
    .padding(10)
    .backgroundColor('#AFEEEE')
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/zICnaDgNQfuB0G8bOf2zGg/zh-cn_image_0000002538018646.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=E2FF3CEEF50CE3FE326BAF9457DE5A2B7E10C5D06514681D4B298F9F3DB6CB16)
    
-   ItemAlign.Start：交叉轴方向首部对齐。
    
    Flex({ alignItems: ItemAlign.Start }) {
      Text('1').width('33%').height(30).backgroundColor('#F5DEB3')
      Text('2').width('33%').height(40).backgroundColor('#D2B48C')
      Text('3').width('33%').height(50).backgroundColor('#F5DEB3')
    }
    .size({ width: '90%', height: 80 })
    .padding(10)
    .backgroundColor('#AFEEEE')
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/DpjcndXdRaajdXp7l_DAZA/zh-cn_image_0000002538178574.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=0A1732CFAA2A3E5D6B0BDB3A229D56425C6E4240953B84E1E68F2EFBF92E50D6)
    
-   ItemAlign.Center：交叉轴方向居中对齐。
    
    Flex({ alignItems: ItemAlign.Center }) {
      Text('1').width('33%').height(30).backgroundColor('#F5DEB3')
      Text('2').width('33%').height(40).backgroundColor('#D2B48C')
      Text('3').width('33%').height(50).backgroundColor('#F5DEB3')
    }
    .size({ width: '90%', height: 80 })
    .padding(10)
    .backgroundColor('#AFEEEE')
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/qdic7oJJREisw8hzeZbchQ/zh-cn_image_0000002569018361.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=3E617C30C80C21D0132DD31964BECA6203579A881DEBAEAF5B2CDAEED51AD819)
    
-   ItemAlign.End：交叉轴方向底部对齐。
    
    Flex({ alignItems: ItemAlign.End }) {
      Text('1').width('33%').height(30).backgroundColor('#F5DEB3')
      Text('2').width('33%').height(40).backgroundColor('#D2B48C')
      Text('3').width('33%').height(50).backgroundColor('#F5DEB3')
    }
    .size({ width: '90%', height: 80 })
    .padding(10)
    .backgroundColor('#AFEEEE')
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/BtyVmZ_ST4u1390EiMCOig/zh-cn_image_0000002568898353.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=2C6279E456EDAE48A9F53DF54F41872B4118C79DE9D179C90ADBF455D4076D60)
    
-   ItemAlign.Stretch：交叉轴方向拉伸填充，在未设置尺寸时，拉伸到容器尺寸。元素在Flex容器中，沿交叉轴方向拉伸填充。容器为Flex且设置[FlexWrap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#flexwrap)为FlexWrap.Wrap或FlexWrap.WrapReverse时，元素拉伸到与当前行或列交叉轴长度最长的元素尺寸。其余情况下，无论元素尺寸是否设置，均拉伸到容器尺寸。
    
    Flex({ alignItems: ItemAlign.Stretch }) {
      Text('1').width('33%').backgroundColor('#F5DEB3')
      Text('2').width('33%').backgroundColor('#D2B48C')
      Text('3').width('33%').backgroundColor('#F5DEB3')
    }
    .size({ width: '90%', height: 80 })
    .padding(10)
    .backgroundColor('#AFEEEE')
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/RoiqzcYaQ5GxPFEJGJqIBA/zh-cn_image_0000002538018648.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=ECE42BFC870719F3ACF36A3B09A60D75673996DAD5A353748DDBDA913E011B0E)
    
-   ItemAlign.Baseline：交叉轴方向文本基线对齐。
    
    Flex({ alignItems: ItemAlign.Baseline }) {
      Text('1').width('33%').height(30).backgroundColor('#F5DEB3')
      Text('2').width('33%').height(40).backgroundColor('#D2B48C')
      Text('3').width('33%').height(50).backgroundColor('#F5DEB3')
    }
    .size({ width: '90%', height: 80 })
    .padding(10)
    .backgroundColor('#AFEEEE')
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/e3aFHsg7SPKvpV3y3h5csA/zh-cn_image_0000002538178576.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=C018CCDA20B1D5E5FAD83ABB6E018ABA8C4487056F2189E6E1EA30BD34BC963A)
    

#### \[h2\]子元素设置交叉轴对齐

子元素的[alignSelf](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout#alignself)属性也可以设置子元素在父容器交叉轴的对齐方式，且会覆盖Flex布局容器中alignItems配置。如下例所示：

Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Center }) { // 容器组件设置子元素居中
  Text('alignSelf Start').width('25%').height(80)
    .alignSelf(ItemAlign.Start)
    .backgroundColor('#F5DEB3')
  Text('alignSelf Baseline')
    .alignSelf(ItemAlign.Baseline)
    .width('25%')
    .height(80)
    .backgroundColor('#D2B48C')
  Text('alignSelf Baseline').width('25%').height(100)
    .backgroundColor('#F5DEB3')
    .alignSelf(ItemAlign.Baseline)
  Text('no alignSelf').width('25%').height(100)
    .backgroundColor('#D2B48C')
  Text('no alignSelf').width('25%').height(100)
    .backgroundColor('#F5DEB3')

}.width('90%').height(220).backgroundColor('#AFEEEE')

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/p6cyHwISQouoIbVb9Mx6RA/zh-cn_image_0000002569018363.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=C0E3736062FB6DACA512F272BADD52EBA38C7FEE29848646EB930E6D27B6CE35)

上例中，Flex容器中alignItems设置交叉轴子元素的对齐方式为居中，子元素自身设置了alignSelf属性的情况，覆盖父组件的alignItems值，表现为alignSelf的定义。

#### \[h2\]内容对齐

可以通过[alignContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex#flexoptions对象说明)参数设置子元素各行在交叉轴剩余空间内的对齐方式，只在多行的Flex布局中生效，可选值有：

-   FlexAlign.Start：子元素各行与交叉轴起点对齐。
    
    Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.Start }) {
      Text('1').width('30%').height(20).backgroundColor('#F5DEB3')
      Text('2').width('60%').height(20).backgroundColor('#D2B48C')
      Text('3').width('40%').height(20).backgroundColor('#D2B48C')
      Text('4').width('30%').height(20).backgroundColor('#F5DEB3')
      Text('5').width('20%').height(20).backgroundColor('#D2B48C')
    }
    .width('90%')
    .height(100)
    .backgroundColor('#AFEEEE')
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/65D5ylsAQ7ugzQ_9V9ZBWQ/zh-cn_image_0000002568898355.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=D5D50D9B38C728CF87E1E4F8F89FEA6FA7DAC5B0229686AAEA50BC8853774A76)
    
-   FlexAlign.Center：子元素各行在交叉轴方向居中对齐。
    
    Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.Center }) {
      Text('1').width('30%').height(20).backgroundColor('#F5DEB3')
      Text('2').width('60%').height(20).backgroundColor('#D2B48C')
      Text('3').width('40%').height(20).backgroundColor('#D2B48C')
      Text('4').width('30%').height(20).backgroundColor('#F5DEB3')
      Text('5').width('20%').height(20).backgroundColor('#D2B48C')
    }
    .width('90%')
    .height(100)
    .backgroundColor('#AFEEEE')
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/TZHcAlANSeaJFaPSHWhXYA/zh-cn_image_0000002538018650.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=B63E68FAF23998CFB62493B4D709FFC44EB69C26681F6682ED68AC21E829837E)
    
-   FlexAlign.End：子元素各行与交叉轴终点对齐。
    
    Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.End }) {
      Text('1').width('30%').height(20).backgroundColor('#F5DEB3')
      Text('2').width('60%').height(20).backgroundColor('#D2B48C')
      Text('3').width('40%').height(20).backgroundColor('#D2B48C')
      Text('4').width('30%').height(20).backgroundColor('#F5DEB3')
      Text('5').width('20%').height(20).backgroundColor('#D2B48C')
    }
    .width('90%')
    .height(100)
    .backgroundColor('#AFEEEE')
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/TIerhuISRrC3MGb1Rz3TdA/zh-cn_image_0000002538178578.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=56A4AAE31A7153D7454F9995CE5FC5E0C28B4A36B17E4F23C6FB980D0FE21DC5)
    
-   FlexAlign.SpaceBetween：子元素各行与交叉轴两端对齐，各行间垂直间距平均分布。
    
    Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.SpaceBetween }) {
      Text('1').width('30%').height(20).backgroundColor('#F5DEB3')
      Text('2').width('60%').height(20).backgroundColor('#D2B48C')
      Text('3').width('40%').height(20).backgroundColor('#D2B48C')
      Text('4').width('30%').height(20).backgroundColor('#F5DEB3')
      Text('5').width('20%').height(20).backgroundColor('#D2B48C')
    }
    .width('90%')
    .height(100)
    .backgroundColor('#AFEEEE')
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/kmK7x21ZQH-vOjh1-NcTMA/zh-cn_image_0000002569018365.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=DF4E74D140C7A1D7898844B11EA7FD92A5979A8BC3F6C69D8B544C23A58CD1C0)
    
-   FlexAlign.SpaceAround：子元素各行间距相等，是元素首尾行与交叉轴两端距离的两倍。
    
    Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.SpaceAround }) {
      Text('1').width('30%').height(20).backgroundColor('#F5DEB3')
      Text('2').width('60%').height(20).backgroundColor('#D2B48C')
      Text('3').width('40%').height(20).backgroundColor('#D2B48C')
      Text('4').width('30%').height(20).backgroundColor('#F5DEB3')
      Text('5').width('20%').height(20).backgroundColor('#D2B48C')
    }
    .width('90%')
    .height(100)
    .backgroundColor('#AFEEEE')
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/t4b2h3VxTMWEg6J1hZks0w/zh-cn_image_0000002568898357.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=D2EB17F6FC2650AF8A333398D731490C0157C5F9C94961D46F4D6A43F1F8A9A9)
    
-   FlexAlign.SpaceEvenly: 子元素各行间距，子元素首尾行与交叉轴两端距离都相等。
    
    Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.SpaceEvenly }) {
      Text('1').width('30%').height(20).backgroundColor('#F5DEB3')
      Text('2').width('60%').height(20).backgroundColor('#D2B48C')
      Text('3').width('40%').height(20).backgroundColor('#D2B48C')
      Text('4').width('30%').height(20).backgroundColor('#F5DEB3')
      Text('5').width('20%').height(20).backgroundColor('#D2B48C')
    }
    .width('90%')
    .height(100)
    .backgroundColor('#AFEEEE')
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/lddTGoHBSPu2_y8IuIdWFQ/zh-cn_image_0000002538018652.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=129ABF83F4B2B84F4DA3D6B7CEAF63269C899D03C187622C29070ABC115BDAE2)
    

#### 自适应拉伸

在弹性布局父组件尺寸过小时，通过子元素的以下属性设置其在父容器的占比，达到自适应布局。

-   [flexBasis](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout#flexbasis)：设置子元素在父容器主轴方向上的基准尺寸。如果设置了该属性，则子项占用的空间为该属性所设置的值；如果没设置该属性，那子项的空间为width/height的值。
    
    Flex() {
      Text('flexBasis("auto")')
        .flexBasis('auto')// 未设置width以及flexBasis值为auto，内容自身宽度
        .height(100)
        .backgroundColor('#F5DEB3')
      Text('flexBasis("auto")'+' width("40%")')
        .width('40%')
        .flexBasis('auto')// 设置width以及flexBasis值auto，使用width的值
        .height(100)
        .backgroundColor('#D2B48C')
    
      Text('flexBasis(100)') // 未设置width以及flexBasis值为100，宽度为100vp
        .flexBasis(100)
        .height(100)
        .backgroundColor('#F5DEB3')
    
      Text('flexBasis(100)')
        .flexBasis(100)
        .width(200)// flexBasis值为100，覆盖width的设置值，宽度为100vp
        .height(100)
        .backgroundColor('#D2B48C')
    }.width('90%').height(120).padding(10).backgroundColor('#AFEEEE')
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/xTJvEJP9TJCxJcAyNZikoQ/zh-cn_image_0000002538178580.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=8CB6A65A80BD428FAF1DC5521CC6BF81BD0D854FD177B68357401A9D17707417)
    
-   [flexGrow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout#flexgrow)：设置父容器的剩余空间分配给此属性所在组件的比例，用于分配父组件的剩余空间。
    
    Flex() {
      Text('flexGrow(1)')
        .flexGrow(1)
        .width(100)
        .height(100)
        .backgroundColor('#F5DEB3')
      Text('flexGrow(4)')
        .flexGrow(4)
        .width(100)
        .height(100)
        .backgroundColor('#D2B48C')
    
      Text('no flexGrow')
        .width(100)
        .height(100)
        .backgroundColor('#F5DEB3')
    }.width(360).height(120).padding(10).backgroundColor('#AFEEEE')
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/jnmT0j9HR_O5BObTr0e5tg/zh-cn_image_0000002569018367.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=DE36A12C265080723AE61875883648D072D8BC163E8C9EAE70936A0DCD04237E)
    
    父容器宽度360vp，三个子元素原始宽度均为100vp，左右padding为20vp，总和320vp，剩余空间40vp根据flexGrow值的占比分配给子元素，未设置flexGrow的子元素不参与分配。
    
    第一个元素以及第二个元素以1:4分配剩下的40vp。第一个元素为100vp+40vp \* 1/5=108vp，第二个元素为100vp+40vp \* 4/5=132vp。
    
-   [flexShrink](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout#flexshrink): 当父容器空间不足时，子元素的压缩比例。
    
    Flex({ direction: FlexDirection.Row }) {
      Text('flexShrink(3)')
        .flexShrink(3)
        .width(200)
        .height(100)
        .backgroundColor('#F5DEB3')
    
      Text('no flexShrink')
        .width(200)
        .height(100)
        .backgroundColor('#D2B48C')
    
      Text('flexShrink(2)')
        .flexShrink(2)
        .width(200)
        .height(100)
        .backgroundColor('#F5DEB3')
    }.width(400).height(120).padding(10).backgroundColor('#AFEEEE')
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/sM3AQRaMTVC8cJ9Z-7x5Mg/zh-cn_image_0000002568898359.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=06888F65661DE3304CB84E0CA1DEA2BAE08057E68C0F14706F30E5A10A5AF510)
    
    父容器宽度400vp，三个子元素原始宽度为200vp，左右padding为20vp，父容器给子元素的布局空间为380vp，超出父容器空间220vp。
    
    将第一个元素和第三个元素以3:2的压缩比例进行压缩，直至不再超出父容器提供的布局空间。第一个元素为200vp - (220vp / 5) \* 3=68vp，第三个元素为200vp - (220vp / 5) \* 2=112vp。
    

#### 场景示例

使用弹性布局，可以实现子元素沿水平方向排列，两端对齐，子元素间距平分，垂直方向上子元素居中的效果。

@Entry
@Component
struct FlexExample {
  build() {
    Column() {
      Column({ space: 5 }) {
        Flex({
          direction: FlexDirection.Row,
          wrap: FlexWrap.NoWrap,
          justifyContent: FlexAlign.SpaceBetween,
          alignItems: ItemAlign.Center
        }) {
          Text('1').width('30%').height(50).backgroundColor('#F5DEB3')
          Text('2').width('30%').height(50).backgroundColor('#D2B48C')
          Text('3').width('30%').height(50).backgroundColor('#F5DEB3')
        }
        .height(70)
        .width('90%')
        .backgroundColor('#AFEEEE')
      }.width('100%').margin({ top: 5 })
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/vm_WyztsT_WqDlF4iN_EfA/zh-cn_image_0000002538018654.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=FF7018153446A17C84AF36C0919A83D24E3EF948555AB1CC8D5B10E58CC4AD09)

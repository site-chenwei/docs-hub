---
title: "层叠布局 (Stack)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-stack-layout"
menu_path:
  - "指南"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "UI开发 (ArkTS声明式开发范式)"
  - "组件布局"
  - "构建布局"
  - "层叠布局 (Stack)"
captured_at: "2026-04-17T01:35:37.411Z"
---

# 层叠布局 (Stack)

#### 概述

层叠布局（StackLayout）用于在屏幕上预留一块区域来显示组件中的元素，提供元素可以重叠的布局。层叠布局通过[Stack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-stack)容器组件实现位置的固定定位与层叠，容器中的子元素依次入栈，后一个子元素覆盖前一个子元素，子元素可以叠加，也可以设置位置。

层叠布局具有较强的页面层叠、位置定位能力，其使用场景有广告、卡片层叠效果等。

如图1，Stack作为容器，容器内的子元素的顺序为Item1->Item2->Item3。

**图1** 层叠布局

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/Hv8oQAoiQpGCwuRShdoaMw/zh-cn_image_0000002569018349.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=4D50D8857AEECE2AC51AFA62BF993BB4CDC346394B388FFCD6C96B86819EADEC)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/GAFkxj8KSmS8usHBp52rlA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=CA3F2E17D7FC3D2DE909A9716131FAFC52385FBA80A95503E27D60E509CA02A3)

过多的嵌套组件数会导致性能劣化。在部分场景中，直接使用组件属性或借助系统API的能力可以替代层叠布局的效果，减少了嵌套组件数进而优化性能。最佳实践请参考[组件嵌套优化-优先使用组件属性代替嵌套组件](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-component-nesting-optimization#section78181114123811)。

#### 开发布局

Stack组件为容器组件，容器内可包含各种子元素。其中子元素默认进行居中堆叠。子元素被约束在Stack下，进行自己的样式定义以及排列。

// xxx.ets
let mTop:Record<string,number> = { 'top': 50 }

@Entry
@Component
struct StackLayoutExample {
  build() {
    Column(){
      Stack({ }) {
        Column(){}.width('90%').height('100%').backgroundColor('#ff58b87c')
        Text('text').width('60%').height('60%').backgroundColor('#ffc3f6aa')
        Button('button').width('30%').height('30%').backgroundColor('#ff8ff3eb').fontColor('#000')
      }.width('100%').height(150).margin(mTop)
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/q1gwJilMR9a0wQcJJpnPYA/zh-cn_image_0000002568898341.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=CAADB7D1347F4BE47FD030CAA4893CFF76C2B9B83919B69221C19D4A460E38E7)

#### 对齐方式

Stack组件通过[alignContent参数](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-stack#aligncontent)实现位置的相对移动。如图2所示，支持九种对齐方式。

**图2** Stack容器内元素的对齐方式

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/Db6ggxodTNyqkoQVQGydIw/zh-cn_image_0000002538018636.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=31594DB74EA3C959E8D2521B2FBB34BB5C401BA52B23D35343A20FFCE8561000)

// xxx.ets
@Entry
@Component
struct StackAlignContentExample {
  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      Text('Stack').width('90%').height('100%').backgroundColor('#e1dede').align(Alignment.BottomEnd)
      Text('Item 1').width('70%').height('80%').backgroundColor(0xd2cab3).align(Alignment.BottomEnd)
      Text('Item 2').width('50%').height('60%').backgroundColor(0xc1cbac).align(Alignment.BottomEnd)
    }.width('100%').height(150).margin({ top: 5 })
  }
}

#### Z序控制

Stack容器中兄弟组件显示层级关系可以通过[Z序控制](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-z-order)的zIndex属性改变。zIndex值越大，显示层级越高，即zIndex值大的组件会覆盖在zIndex值小的组件上方。

在层叠布局中，如果后面子元素尺寸大于前面子元素尺寸，则前面子元素完全隐藏。

Stack({ alignContent: Alignment.BottomStart }) {
  Column() {
    // 请将$r('app.string.stack\_num1')替换为实际资源文件，在本示例中该资源文件的value值为"Stack子元素1"
    Text($r('app.string.stack\_num1')).textAlign(TextAlign.End).fontSize(20)
  }.width(100).height(100).backgroundColor(0xffd306)

  Column() {
    // 请将$r('app.string.stack\_num2')替换为实际资源文件，在本示例中该资源文件的value值为"Stack子元素2"
    Text($r('app.string.stack\_num2')).fontSize(20)
  }.width(150).height(150).backgroundColor(Color.Pink)

  Column() {
    // 请将$r('app.string.stack\_num3')替换为实际资源文件，在本示例中该资源文件的value值为"Stack子元素3"
    Text($r('app.string.stack\_num3')).fontSize(20)
  }.width(200).height(200).backgroundColor(Color.Grey)
}.width(350).height(350).backgroundColor(0xe0e0e0)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/bE641X-lR7GuYx1tBKRHMw/zh-cn_image_0000002538178564.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=ED1B8CAAB03F3A01FC0709FE910EA509E216FFF7011534E672D1F01BE3929695)

上图中，最后的子元素3的尺寸大于前面的所有子元素，所以，前面两个元素完全隐藏。改变子元素1、子元素2的zIndex属性后，可以将元素展示出来。

Stack({ alignContent: Alignment.BottomStart }) {
  Column() {
    // 请将$r('app.string.stack\_num1')替换为实际资源文件，在本示例中该资源文件的value值为"Stack子元素1"
    Text($r('app.string.stack\_num1')).fontSize(20)
  }.width(100).height(100).backgroundColor(0xffd306).zIndex(2)

  Column() {
    // 请将$r('app.string.stack\_num2')替换为实际资源文件，在本示例中该资源文件的value值为"Stack子元素2"
    Text($r('app.string.stack\_num2')).fontSize(20)
  }.width(150).height(150).backgroundColor(Color.Pink).zIndex(1)

  Column() {
    // 请将$r('app.string.stack\_num3')替换为实际资源文件，在本示例中该资源文件的value值为"Stack子元素3"
    Text($r('app.string.stack\_num3')).fontSize(20)
  }.width(200).height(200).backgroundColor(Color.Grey)
}.width(350).height(350).backgroundColor(0xe0e0e0)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/m0nbfIMiQXqpgXuoVqdsSQ/zh-cn_image_0000002569018351.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=1223E9C0F03C2C05649BBF611C98692DC5D3F2C927A77C1CD1941376749A54D9)

#### 场景示例

使用层叠布局快速搭建页面。

@Entry
@Component
struct StackSample {
  private arr: string\[\] = \['APP1', 'APP2', 'APP3', 'APP4', 'APP5', 'APP6', 'APP7', 'APP8'\];

  build() {
    Stack({ alignContent: Alignment.Bottom }) {
      Flex({ wrap: FlexWrap.Wrap }) {
        ForEach(this.arr, (item:string) => {
          Text(item)
            .width(100)
            .height(100)
            .fontSize(16)
            .margin(10)
            .textAlign(TextAlign.Center)
            .borderRadius(10)
            .backgroundColor(0xFFFFFF)
        }, (item:string):string => item)
      }.width('100%').height('100%')

      Flex({ justifyContent: FlexAlign.SpaceAround, alignItems: ItemAlign.Center }) {
        // 请将$r('app.string.contacts')替换为实际资源文件，在本示例中该资源文件的value值为"联系人"
        Text($r('app.string.contacts')).fontSize(16)
        // 请将$r('app.string.setting')替换为实际资源文件，在本示例中该资源文件的value值为"设置"
        Text($r('app.string.setting')).fontSize(16)
        // 请将$r('app.string.text\_message')替换为实际资源文件，在本示例中该资源文件的value值为"短信"
        Text($r('app.string.text\_message')).fontSize(16)
      }
      .width('50%')
      .height(50)
      .backgroundColor('#16302e2e')
      .margin({ bottom: 15 })
      .borderRadius(15)
    }.width('100%').height('100%').backgroundColor('#CFD0CF')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/PnprNNcXT4apiuWLiyccJw/zh-cn_image_0000002568898343.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=DABD0106E8B1EC0B5C7A4C409058BA313AB64AD611EBB529D87D38F9BDBE9AA4)

#### 示例代码

-   [组件堆叠](https://gitcode.com/HarmonyOS_Samples/component-stack)

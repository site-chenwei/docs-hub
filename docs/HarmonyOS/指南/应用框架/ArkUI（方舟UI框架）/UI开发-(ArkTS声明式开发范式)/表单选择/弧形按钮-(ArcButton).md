---
title: "弧形按钮 (ArcButton)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-advanced-components-arcbutton"
menu_path:
  - "指南"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "UI开发 (ArkTS声明式开发范式)"
  - "表单选择"
  - "弧形按钮 (ArcButton)"
captured_at: "2026-04-17T01:35:37.851Z"
---

# 弧形按钮 (ArcButton)

从API version 18开始支持ArcButton。ArcButton是弧形按钮组件，推荐用于圆形屏幕。为用户提供强调、普通、警告等样式按钮。具体用法请参考[ArcButton](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton)。

#### 创建按钮

ArcButton通过调用以下接口来创建。

ArcButton({
  options: new ArcButtonOptions({
    label: 'OK',
    position: ArcButtonPosition.TOP\_EDGE,
    styleMode: ArcButtonStyleMode.EMPHASIZED\_LIGHT,
  // ···
  })
})

其中，[label](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)设置按钮文字，[position](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)设置按钮类型，[styleMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)设置按钮样式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/1x81nsE7RMm2lpeEINimRw/zh-cn_image_0000002568898509.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=719E2F154CB11A1C3D3881836E3E8A7A5CFB400814D4166BB4372A182CF0548E)

#### 设置按钮类型

ArcButton有上弧形按钮和下弧形按钮两种类型。使用[position](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)设置按钮类型。

-   下弧形按钮（默认类型）。
    
    通过将[position](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)属性设置为ArcButtonPosition.BOTTOM\_EDGE，可以将按钮设置为下弧形按钮。
    
    ArcButton({
      options: new ArcButtonOptions({
        label: 'OK',
        position: ArcButtonPosition.BOTTOM\_EDGE,
        styleMode: ArcButtonStyleMode.EMPHASIZED\_LIGHT,
      // ···
      })
    
    })
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/wjm2uWAfQXWX17wgMb8WIA/zh-cn_image_0000002538018804.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=05936D7D1C2EEBFF896CD0EDD72D1C9F20C8AD6843A3D0B00621BEF6D462681B)
    
-   上弧形按钮。
    
    通过将[position](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)属性设置为ArcButtonPosition.TOP\_EDGE，可以将按钮设置为上弧形按钮。
    
    ArcButton({
      options: new ArcButtonOptions({
        label: 'OK',
        position: ArcButtonPosition.TOP\_EDGE,
        styleMode: ArcButtonStyleMode.EMPHASIZED\_LIGHT,
      // ···
      })
    })
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/V521zKdGTvCl0QJeIDAXmQ/zh-cn_image_0000002538178732.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=3E712116BB75ADE7F8CA258551F8E797301E15C9EC754075F0CF317CC4271904)
    

#### 自定义样式

-   设置背景色。
    
    使用[backgroundColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)属性设置按钮的背景色。
    
    ArcButton({
      options: new ArcButtonOptions({
        label: 'OK',
        styleMode: ArcButtonStyleMode.CUSTOM,
        backgroundColor: ColorMetrics.resourceColor('#707070')
      })
    })
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/JfpuMifxQBGLdyd5grFAkg/zh-cn_image_0000002569018521.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=01F5990646E44EADB604A75BCC49829ED0567B8B03544DB0AE8636CF39D2ABC3)
    
-   设置文本颜色。
    
    使用[fontColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)属性设置按钮的文本颜色。
    
    ArcButton({
      options: new ArcButtonOptions({
        label: 'OK',
        styleMode: ArcButtonStyleMode.CUSTOM,
        backgroundColor: ColorMetrics.resourceColor('#E84026'),
        fontColor: ColorMetrics.resourceColor('#707070')
      })
    })
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/wB0Uh6BrQtiyQSvxvG2PYA/zh-cn_image_0000002568898511.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=A3299C1D259B43ECD7E36382241941CADE60330647EB644182D3703C841CBEF2)
    
-   设置阴影颜色。
    
    使用[shadowEnabled](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)属性启用按钮阴影，并通过[shadowColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton#arcbuttonoptions)属性设置按钮的阴影颜色。
    
    ArcButton({
      options: new ArcButtonOptions({
        label: 'OK',
        shadowEnabled: true,
        shadowColor: ColorMetrics.resourceColor('#ffec1022')
      })
    })
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/D8Ecvzs_Q8Oaedq9qG6T7A/zh-cn_image_0000002538018806.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=7E06F280CE8BC6EB9A4B64805BBEFD1A2FF7DEAC9330C9C69733E2276B8B3C9D)
    

#### 添加事件

-   绑定onClick事件来响应点击操作后的自定义行为。
    
    ArcButton({
      options: new ArcButtonOptions({
        label: 'OK',
      // ···
        onClick: () => {
          hilog.info(DOMAIN, TAG, 'ArcButton onClick');
        },
      })
    })
    
-   绑定onTouch事件来响应触摸操作后的自定义行为。
    
    ArcButton({
      options: new ArcButtonOptions({
        label: 'OK',
      // ···
        onTouch: (event: TouchEvent) => {
          hilog.info(DOMAIN, TAG, 'ArcButton onTouch');
        }
      })
    
    })
    

#### 场景示例

在亮度设置界面，进度条显示当前亮度为30%。点击重置后，亮度值将被重置为默认的50%。

运行该示例推荐在Wearable设备上以获得最佳显示效果，同时支持在其他设备上运行。若要在Wearable设备上运行，在src/main目录下的工程配置文件[module.json5](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)中[deviceTypes标签](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file#devicetypes标签)内配置wearable。

"module": {
  // ···
  "deviceTypes": \[
    "wearable"
  \],
  // ···
}

import { LengthMetrics, LengthUnit, ArcButton, ArcButtonOptions, ArcButtonStyleMode } from '@kit.ArkUI';

const BRIGHT\_NESS\_VALUE = 30;
const BRIGHT\_NESS\_VALUE\_DEFAULT = 50;

@Entry
@ComponentV2
struct BrightnessPage {
  @Local brightnessValue: number = BRIGHT\_NESS\_VALUE;
  private defaultBrightnessValue: number = BRIGHT\_NESS\_VALUE\_DEFAULT;

  build() {
    RelativeContainer() {
      // 请将$r('app.string.Brightness')替换为实际资源文件，在本示例中该资源文件的value值为"设置亮度"
      Text($r('app.string.Brightness'))
        .fontColor(Color.White)
        .id('id\_brightness\_set\_text')
        .fontSize(24)
        .margin({ top: 16 })
        .alignRules({
          middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
        })

      Text(\`${this.brightnessValue} %\`)
        .fontColor(Color.White)
        .id('id\_brightness\_min\_text')
        .margin({ left: 16 })
        .alignRules({
          start: { anchor: '\_\_container\_\_', align: HorizontalAlign.Start },
          center: { anchor: '\_\_container\_\_', align: VerticalAlign.Center }
        })

      Slider({
        value: this.brightnessValue,
        min: 0,
        max: 100,
        style: SliderStyle.InSet
      })
        .blockColor('#191970')
        .trackColor('#ADD8E6')
        .selectedColor('#4169E1')
        .width(150)
        .id('id\_brightness\_slider')
        .margin({ left: 16, right: 16 })
        .onChange((value: number, mode: SliderChangeMode) => {
          this.brightnessValue = value;
        })
        .alignRules({
          center: { anchor: 'id\_brightness\_min\_text', align: VerticalAlign.Center },
          start: { anchor: 'id\_brightness\_min\_text', align: HorizontalAlign.End }
        })

      ArcButton({
        options: new ArcButtonOptions({
          // 请将$r('app.string.Reset')替换为实际资源文件，在本示例中该资源文件的value值为"重置"
          label: $r('app.string.Reset'),
          styleMode: ArcButtonStyleMode.EMPHASIZED\_LIGHT,
          fontSize: new LengthMetrics(19, LengthUnit.FP),
          onClick: () => {
            this.brightnessValue = this.defaultBrightnessValue;
          }
        })
      })
        .alignRules({
          middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center },
          bottom: { anchor: '\_\_container\_\_', align: VerticalAlign.Bottom }
        })
    }
    .height('100%')
    .width('100%')
    .backgroundColor(Color.Black)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/p6i3O9IwSZ2-7Y6Csv4DPA/zh-cn_image_0000002538178734.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=F2E914A432368FFA9B0347EB219D5787F1D63510194167EA349DD9DCD2B022C5)

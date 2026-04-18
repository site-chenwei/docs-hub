---
title: "stateStyles：多态样式"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-statestyles"
menu_path:
  - "指南"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "UI开发 (ArkTS声明式开发范式)"
  - "学习UI范式基本语法"
  - "组件扩展"
  - "stateStyles：多态样式"
captured_at: "2026-04-17T01:35:36.014Z"
---

# stateStyles：多态样式

@Styles仅应用于静态页面的样式复用，stateStyles可以依据组件的内部状态的不同，快速设置不同样式。这就是我们本章要介绍的内容stateStyles（又称为：多态样式）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/sY4i64pUSJiefgXQdzRAyA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013536Z&HW-CC-Expire=86400&HW-CC-Sign=5EA8C2671495B08FEEB5EEEE8856ED81837136E6B9EF8B6E340472C6E4E42927)

多态样式仅支持通用属性。如果多态样式不生效，则该属性可能为组件的私有属性，例如：[fontColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-button#fontcolor)、[TextInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput)组件的[backgroundColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-background#backgroundcolor)等。此时，可以通过[attributeModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#attributemodifier)动态设置组件属性来解决此问题。

#### 概述

stateStyles是属性方法，可以根据UI内部状态来设置样式，类似于css伪类，但语法不同。ArkUI提供以下六种状态：

-   focused：获焦态。
    
-   normal：正常态。
    
-   pressed：按压态。
    
-   disabled：不可用态。
    
-   clicked：点击态。
    
-   selected10+：选中态。
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/NfcebjyoSA-ss-Q-8yJr3Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013536Z&HW-CC-Expire=86400&HW-CC-Sign=7941490D7EB049892FF45D1838D1F2CC0222C6F8C7A4C72A3A5FADE55B1CE7E5)

获焦态目前仅支持通过外接键盘的Tab键或方向键触发，不支持在嵌套滚动组件场景下通过按键触发。

#### 使用场景

#### \[h2\]基础场景

下面的示例展示了stateStyles最基本的使用场景。Button1处于第一个组件，Button2处于第二个组件。按压时显示为pressed态指定的黑色。使用Tab键走焦，Button1获焦并显示为focused态指定的粉色。当Button2获焦的时候，Button2显示为focused态指定的粉色，Button1失焦显示normal态指定的蓝色。

@Entry
@Component
struct StateStylesSample {
  build() {
    Column() {
      Button('Button1')
        .stateStyles({
          focused: {
            .backgroundColor('#ffffeef0')
          },
          pressed: {
            .backgroundColor('#ff707070')
          },
          normal: {
            .backgroundColor('#ff2787d9')
          }
        })
        .margin(20)
      Button('Button2')
        .stateStyles({
          focused: {
            .backgroundColor('#ffffeef0')
          },
          pressed: {
            .backgroundColor('#ff707070')
          },
          normal: {
            .backgroundColor('#ff2787d9')
          }
        })
    }.margin('30%')
  }
}

**图1** 获焦态和按压态

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/Px8AKsBpS46uCAi03x-3Bw/zh-cn_image_0000002538018502.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013536Z&HW-CC-Expire=86400&HW-CC-Sign=A8F1ECA036A04029E8695F4749FD42CF213A7CF7C28163C8C6D9FD37D41F1D30)

#### \[h2\]@Styles和stateStyles联合使用

以下示例通过@Styles指定stateStyles的不同状态。

@Entry
@Component
struct MyComponent {
  @Styles normalStyle() {
    .backgroundColor(Color.Gray)
  }

  @Styles pressedStyle() {
    .backgroundColor(Color.Red)
  }
  build() {
    Column() {
      Text('Text1')
        .fontSize(50)
        .fontColor(Color.White)
        .stateStyles({
          normal: this.normalStyle,
          pressed: this.pressedStyle,
        })
    }
  }
}

**图2** 正常态和按压态

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/e9OeOI5BTjyUb1rzIhvKuQ/zh-cn_image_0000002538178430.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013536Z&HW-CC-Expire=86400&HW-CC-Sign=98325D97410BAE38ADEAC7C23B716D9BE1EFDAB7E2611D7DB64346BBCE927EA5)

#### \[h2\]在stateStyles里使用常规变量和状态变量

stateStyles可以通过this绑定组件内的常规变量和状态变量。

@Entry
@Component
struct CompWithInlineStateStyles {
  @State focusedColor: Color = 0xD5D5D5;
  normalColor: Color = 0x004AAF;

  build() {
    Column() {
      Button('clickMe')
        .height(100)
        .width(100)
        .stateStyles({
          normal: {
            .backgroundColor(this.normalColor)
          },
          focused: {
            .backgroundColor(this.focusedColor)
          }
        })
        .onClick(() => {
          this.focusedColor = 0x707070;
        })
        .margin('30%')
    }
  }
}

Button默认normal态显示蓝色，第一次按下Tab键让Button获焦显示为focus态的浅灰色，点击事件触发后，再次按下Tab键让Button获焦，focus态变为深灰色。

**图3** 点击改变获焦态样式

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/HULoaQT1RXGLklJMWJ8N0w/zh-cn_image_0000002569018217.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013536Z&HW-CC-Expire=86400&HW-CC-Sign=25F551A99210D5906B196567A055E3F0AC5BF78218BD995E4D32BC89C3D142A6)

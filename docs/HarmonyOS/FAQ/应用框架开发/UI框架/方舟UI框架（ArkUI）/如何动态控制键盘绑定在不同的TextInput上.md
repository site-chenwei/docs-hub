---
title: "如何动态控制键盘绑定在不同的TextInput上"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-215"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "UI框架"
  - "方舟UI框架（ArkUI）"
  - "如何动态控制键盘绑定在不同的TextInput上"
captured_at: "2026-04-17T02:03:04.982Z"
---

# 如何动态控制键盘绑定在不同的TextInput上

软键盘的收起和弹出与输入框的获焦和失焦相关。可以通过 focusControl 动态控制输入框焦点的转移，从而控制软键盘的显示和隐藏。将焦点转移到目标输入框可以实现键盘的动态切换。参考代码如下：

@Entry
@Component
struct DynamicControlKeyboard {
  // Whether focus is on "key1" TextInput
  private flag: boolean = true;
  @Builder
  customKeyboardBuilder() {
    Row() {
      Text('Customize keyboard')
    }
    .justifyContent(FlexAlign.Center)
    .width('1260px')
    .height('1161px')
    .backgroundColor(Color.Brown)
  }
  build() {
    Column({space: 10}) {
      TextInput()
        .key('key1')
        .onAppear(() => {
          focusControl.requestFocus('key1');
        })
        .defaultFocus(true)
      TextInput()
        .key('key2')
        .customKeyboard(this.customKeyboardBuilder())
      Button('Switch TextInput')
        .onClick(() => {
          if (this.flag) {
            console.info('TextInput2 ==> ' + focusControl.requestFocus('key2'));
          } else {
            console.info('TextInput1 ==> ' + focusControl.requestFocus('key1'));
          }
          this.flag = !this.flag;
        })
      Button()
        .width(0)
        .height(0)
        .key('key3')
    }
    .padding({ top: 20 })
    .width('100%')
    .height('100%')
    .onClick(() => {
      focusControl.requestFocus('key3');
    })
  }
}

效果如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/0i-VxZFlTFSyF3p1So9bUw/zh-cn_image_0000002426207326.png?HW-CC-KV=V1&HW-CC-Date=20260417T020307Z&HW-CC-Expire=86400&HW-CC-Sign=D86CF110691BD071A744C0A435AD9DF0F07991AC85F86ADA48D7E861DE97B813)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/g4Se3eHrQHqX4toJL_HdWg/zh-cn_image_0000002426218940.png?HW-CC-KV=V1&HW-CC-Date=20260417T020307Z&HW-CC-Expire=86400&HW-CC-Sign=1C32D26736E6875430F7F85CB8B2C8F3D313C33082B8F284967FB74080AEED22 "点击放大")

**参考链接**

[focusControl](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-focus#focuscontrol9)

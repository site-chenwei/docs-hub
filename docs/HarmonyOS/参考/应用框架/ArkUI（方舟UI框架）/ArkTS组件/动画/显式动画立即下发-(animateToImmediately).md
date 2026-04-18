---
title: "显式动画立即下发 (animateToImmediately)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-explicit-animatetoimmediately"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "ArkTS组件"
  - "动画"
  - "显式动画立即下发 (animateToImmediately)"
captured_at: "2026-04-17T01:47:58.611Z"
---

# 显式动画立即下发 (animateToImmediately)

animateToImmediately接口用来提供[显式动画](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-explicit-animation)立即下发功能。同时加载多个属性动画的情况下，使用该接口可以立即执行闭包代码中状态变化导致的过渡动效。

与[animateTo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#animateto)相比，animateToImmediately能即时将生成的动画指令发送至渲染层执行，无需等待vsync信号，从而在视觉效果上实现部分动画的优先呈现。当应用的主线程存在耗时操作，且需提前更新部分用户界面时，此接口可有效缩短应用的响应延迟。需要注意的是，animateToImmediately仅支持渲染层上的属性动画提前执行，无法用于UI侧的逐帧动画。

此外，该接口会将调用前的状态和新生成的动画一并发送至渲染层，因此渲染结果可能会基于调用时的状态进行。务必确保调用时的状态完整，否则前几帧可能出现渲染异常。

因此，建议开发者优先使用[animateTo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#animateto)，以防止干扰框架的显示时序，避免在动画启动时因状态设置不完整而导致的显示错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/oke0trYqQ2yn-64VfLSyOA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014801Z&HW-CC-Expire=86400&HW-CC-Sign=C56570945F478E2CDF3830EA7EEF2FEBCE9AB7C2CC1CF23F699232A0D17D7EB2)

从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 接口

#### animateToImmediately

animateToImmediately(value: AnimateParam , event: () => void): void

提供显式动画立即下发功能。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| value | [AnimateParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-explicit-animation#animateparam对象说明) | 是 | 设置动画效果相关参数。 |
| event | () => void | 是 | 指定显示动效的闭包函数，在闭包函数中导致的状态变化系统会自动插入过渡动画。 |

#### 示例

该示例主要演示通过[animateToImmediately](#animatetoimmediately)接口来实现显式动画立即下发。

```ts
// xxx.ets
@Entry
@Component
struct AnimateToImmediatelyExample {
  @State widthSize: number = 250;
  @State heightSize: number = 100;
  @State opacitySize: number = 0;
  private flag: boolean = true;

  build() {
    Column() {
      Column()
      .width(this.widthSize)
      .height(this.heightSize)
      .backgroundColor(Color.Green)
      .opacity(this.opacitySize)
      Button('change size')
        .margin(30)
        .onClick(() => {
          if (this.flag) {
            animateToImmediately({
              delay: 0,
              duration: 1000
            }, () => {
              this.opacitySize = 1;
            })
            this.getUIContext()?.animateTo({
              delay: 1000,
              duration: 1000
            }, () => {
              this.widthSize = 150;
              this.heightSize = 60;
            })
          } else {
            animateToImmediately({
              delay: 0,
              duration: 1000
            }, () => {
              this.widthSize = 250;
              this.heightSize = 100;
            })
            this.getUIContext()?.animateTo({
              delay: 1000,
              duration: 1000
            }, () => {
              this.opacitySize = 0;
            })
          }
          this.flag = !this.flag;
        })
    }.width('100%').margin({ top: 5 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/4dMVcFCdTZmU-8tde2tpiQ/zh-cn_image_0000002568900687.gif?HW-CC-KV=V1&HW-CC-Date=20260417T014801Z&HW-CC-Expire=86400&HW-CC-Sign=FF0831D685D1F450630D36A65A36C17C4BEB1C1ADC2DD9EE25BB832450CC4BBF)

---
title: "如何在自定义组件的构建流程里跟踪组件数据或者状态，如在build里增加日志跟踪状态变量等"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-50"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "UI框架"
  - "方舟UI框架（ArkUI）"
  - "如何在自定义组件的构建流程里跟踪组件数据或者状态，如在build里增加日志跟踪状态变量等"
captured_at: "2026-04-17T02:03:03.293Z"
---

# 如何在自定义组件的构建流程里跟踪组件数据或者状态，如在build里增加日志跟踪状态变量等

使用@Watch回调来监测状态变量的变化。如果回调函数执行，说明在下一次VSync信号发送时，使用该状态变量的UI会刷新绘制。

参考代码如下：

@Component
struct TotalView {
  @Prop @Watch('onCountUpdated') count: number = 0;
  @State total: number = 0;
  // @Watch callback
  onCountUpdated(propName: string): void {
    this.total += this.count;
  }

  build() {
    Text(\`Total: ${this.total}\`)
  }
}

@Entry
@Component
struct CountModifier {
  @State count: number = 0;

  build() {
    Column() {
      Button('add to basket')
        .onClick(() => {
          this.count++;
        })
      TotalView({ count: this.count })
    }
  }
}

**参考链接**

[watch和自定义组件更新](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-watch#watch和自定义组件更新)

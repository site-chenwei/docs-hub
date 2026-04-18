---
title: "如何修改bindPopup绑定的弹窗圆角大小和箭头颜色"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-349"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "UI框架"
  - "方舟UI框架（ArkUI）"
  - "如何修改bindPopup绑定的弹窗圆角大小和箭头颜色"
captured_at: "2026-04-17T02:03:06.359Z"
---

# 如何修改bindPopup绑定的弹窗圆角大小和箭头颜色

通过radius参数调整圆角大小，但箭头颜色需通过popupColor间接设置。示例代码如下：

@Entry
@Component
struct BindPopupDemo {
  @State handlePopup: boolean = false;
  @State customPopup: boolean = false;

  // Popup constructor defines the content of the popup box
  @Builder
  popupBuilder() {
    Row({ space: 2 }) {
      Image($r('app.media.startIcon'))
        .width(24)
        .height(24)
        .margin({ left: -5 })
      Text('Custom Popup')
        .fontSize(10)
    }
    .width(100)
    .height(50)
    .padding(5)
  }

  build() {
    RelativeContainer() {
      Button('CustomPopupOptions')
        .onClick(() => {
          this.customPopup = !this.customPopup;
        })
        .bindPopup(this.customPopup, {
          builder: this.popupBuilder,
          radius: 30,
          popupColor: Color.Yellow,
          enableArrow: true,
          onStateChange: (e) => {
            if (!e.isVisible) {
              this.customPopup = false;
            }
          }
        })
    }
  }
}

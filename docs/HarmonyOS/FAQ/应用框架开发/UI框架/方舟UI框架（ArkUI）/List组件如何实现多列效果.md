---
title: "List组件如何实现多列效果"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-27"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "UI框架"
  - "方舟UI框架（ArkUI）"
  - "List组件如何实现多列效果"
captured_at: "2026-04-17T02:03:03.043Z"
---

# List组件如何实现多列效果

设置[List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)组件的lanes属性，以实现交叉轴上的多列布局。示例代码如下：

// xxx.ets
@Entry
@Component
struct ListExample {
  @State arr: string\[\] = \['1', '2', '3', '4', '5', '6', '7', '8', '9'\];

  build() {
    Column() {
      List() {
        ForEach(this.arr, (item: string) => {
          ListItem() {
            Row() {
              Text(item)
                .fontColor(Color.Red)
                .fontSize(40)
            }
          }
          .width('100%')
          .border({
            width: 1,
            color: Color.Black,
            radius: 5
          })
        })
      }
      .lanes(3)
      .alignListItem(ListItemAlign.Center)
    }
    .padding({ top: 30 })
  }
}

效果如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/-Os-fRjWTxO_MK3Eu0OLsA/zh-cn_image_0000002194158740.png?HW-CC-KV=V1&HW-CC-Date=20260417T020305Z&HW-CC-Expire=86400&HW-CC-Sign=46CACB697C2082FDC7895BDEA3977B893EA128ED6D55062ED627F2ECF0923F1D "点击放大")

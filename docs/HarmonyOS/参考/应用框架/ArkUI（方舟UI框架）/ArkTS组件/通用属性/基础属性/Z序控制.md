---
title: "Z序控制"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-z-order"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "ArkTS组件"
  - "通用属性"
  - "基础属性"
  - "Z序控制"
captured_at: "2026-04-17T01:47:54.645Z"
---

# Z序控制

组件的Z序，设置同一容器中兄弟组件的堆叠顺序。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/NlRX2rWzQyGN0ZwMXDs4CQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014756Z&HW-CC-Expire=86400&HW-CC-Sign=9861EEEA52FCF3F89FB1EDE1BC8752F4383898EE8CF03710E41268AD9E9DB865)

从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### zIndex

zIndex(value: number): T

设置组件的堆叠顺序。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| value | number | 是 | 同一容器中兄弟组件显示层级关系。zIndex值越大，显示层级越高，即zIndex值大的组件会覆盖在zIndex值小的组件上方。当不涉及新增或减少兄弟节点，动态改变zIndex时会在zIndex改变前层级顺序的基础上进行稳定排序。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| T | 返回当前组件。 |

#### 示例

#### \[h2\]示例1（设置组件堆叠顺序）

该示例通过zIndex设置组件堆叠顺序。

```ts
// xxx.ets
@Entry
@Component
struct ZIndexExample {
  build() {
    Column() {
      Stack() {
        // Stack会重叠组件，默认后定义的在最上面，具有较高zIndex值的元素在zIndex较小的元素前面
        // Text1设置zIndex值为2
        Text('1, zIndex(2)')
          .size({ width: '40%', height: '30%' }).backgroundColor(0xbbb2cb)
          .zIndex(2)
        // Text2设置zIndex值为1
        Text('2, default zIndex(1)')
          .size({ width: '70%', height: '50%' }).backgroundColor(0xd2cab3).align(Alignment.TopStart)
          .zIndex(1)
        // Text3设置zIndex值为0
        Text('3, zIndex(0)')
          .size({ width: '90%', height: '80%' }).backgroundColor(0xc1cbac).align(Alignment.TopStart)
          .zIndex(0)
      }.width('100%').height(200)
    }.width('100%').height(200)
  }
}
```

Stack容器内子组件不设置zIndex的效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/UmMY0kIGQpqZxB1zg_QfSw/zh-cn_image_0000002568900137.png?HW-CC-KV=V1&HW-CC-Date=20260417T014756Z&HW-CC-Expire=86400&HW-CC-Sign=66C2911E669987680639439338ED4C62B23538A06D9ECACDFA616B81624F8EB6)

Stack容器子组件设置zIndex后的效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/jULKJDIAR_2EriBsv4HXGQ/zh-cn_image_0000002538020434.png?HW-CC-KV=V1&HW-CC-Date=20260417T014756Z&HW-CC-Expire=86400&HW-CC-Sign=0E0E995E085F8CC9FBD946FF38E846379D6DB3B1065729A97B5D1157CF21E6B0)

#### \[h2\]示例2（动态修改zIndex属性）

该示例使用Button组件动态修改zIndex属性。

```ts
// xxx.ets
@Entry
@Component
struct ZIndexExample {
  @State zIndex_: number = 0

  build() {
    Column() {
      // 点击Button改变zIndex后，在点击Button前的层级顺序上根据zIndex进行稳定排序。
      Button("change Text2 zIndex")
        .onClick(() => {
          this.zIndex_ = (this.zIndex_ + 1) % 3;
        })
      Stack() {
        // Text1设置zIndex值为1
        Text('1, zIndex(1)')
          .size({ width: '70%', height: '50%' }).backgroundColor(0xd2cab3).align(Alignment.TopStart)
          .zIndex(1)
        // Text2设置zIndex默认值为0
        Text('2, default zIndex(0), now zIndex:' + this.zIndex_)
          .size({ width: '90%', height: '80%' }).backgroundColor(0xc1cbac).align(Alignment.TopStart)
          .zIndex(this.zIndex_)
      }.width('100%').height(200)
    }.width('100%').height(200)
  }
}
```

不点击Button修改zIndex值的效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/0vXaz_kzQ7yPplsvYEnpOw/zh-cn_image_0000002538180360.png?HW-CC-KV=V1&HW-CC-Date=20260417T014756Z&HW-CC-Expire=86400&HW-CC-Sign=758E4779451096DF8BBA3CB34D6A974C32104060C9335097DBAB3FD37EC7CEDE)

点击Button动态修改zIndex，使Text1和Text2的zIndex相等，因为在点击Button前的层级顺序上根据zIndex进行稳定排序，层级顺序不发生改变。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/2dGqj70ASC-AvZ_udWpsgQ/zh-cn_image_0000002569020147.png?HW-CC-KV=V1&HW-CC-Date=20260417T014756Z&HW-CC-Expire=86400&HW-CC-Sign=6DFC7AA5E4F3BB9B72240EBE95F15A928EBA3CA2266C1F60E138F675E1D4512E)

点击Button动态修改zIndex，使Text2的zIndex大于Text1，层级顺序发生改变。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/m7jEsisWQsC-lr-M5I0FAQ/zh-cn_image_0000002568900139.png?HW-CC-KV=V1&HW-CC-Date=20260417T014756Z&HW-CC-Expire=86400&HW-CC-Sign=7006BECB1BCBFFD175C9B24797317C75399381E5EB68CFFF10CEED13605817F6)

#### \[h2\]示例3（设置不同容器内组件的zIndex属性）

该示例在不同容器内设置zIndex属性。其中，Text1、Text2和Text3在不同的Stack容器内。虽然Text3的zIndex值最小，但Text1、Text2仍无法按照预期显示在Text3的上方。

```ts
// xxx.ets
@Entry
@Component
struct ZIndexExample {
  build() {
    Stack() {
      Stack() {
        // Text1设置zIndex值为2
        Text('1, zIndex(2)')
          .size({ width: '40%', height: '30%' }).backgroundColor(0xbbb2cb)
          .zIndex(2)
        // Text2设置zIndex值为1
        Text('2, default zIndex(1)')
          .size({ width: '70%', height: '50%' }).backgroundColor(0xd2cab3).align(Alignment.TopStart)
          .zIndex(1)
      }.width('100%').height(200)

      Stack() {
        // zIndex在不同容器的组件中无法生效，Text3会显示在最上方
        // Text3设置zIndex值为0
        Text('3, zIndex(0)')
          .size({ width: '90%', height: '80%' }).backgroundColor(0xc1cbac).align(Alignment.TopStart)
          .zIndex(0)
      }.width('100%').height(200)
    }.width('100%').height(200)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/EoAnuB2DSEK8bgoyZqpYaQ/zh-cn_image_0000002538020436.png?HW-CC-KV=V1&HW-CC-Date=20260417T014756Z&HW-CC-Expire=86400&HW-CC-Sign=51444B5EE23E6436D65BD30F6C3E4859EB1CAD0B3530CB1D6E1BB5CD1B2B78C6)

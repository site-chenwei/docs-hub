---
title: "ColumnSplit"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-columnsplit"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "ArkTS组件"
  - "栅格与分栏"
  - "ColumnSplit"
captured_at: "2026-04-17T01:47:56.014Z"
---

# ColumnSplit

将子组件纵向布局，并在每个子组件之间插入横向分割线。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/TEdAu5LlS4W6ITvcczmIjg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014758Z&HW-CC-Expire=86400&HW-CC-Sign=5C644A3DDB02AF02A64A5D85126D9D39AC544F337008EA92B8846CB8F4CB1B61)

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 子组件

可以包含子组件。

ColumnSplit通过分割线限制子组件的高度。初始化时，分割线位置根据子组件的高度来计算。初始化后，动态修改子组件的高度不生效，分割线位置保持不变，可通过拖动相邻分割线改变子组件高度。

初始化后，动态修改[margin](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#margin)、[border](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-border#border)、[padding](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#padding)通用属性导致子组件尺寸大于相邻分割线间距的异常情况下，不支持拖动分割线改变子组件的高度。

#### 接口

ColumnSplit()

带分割线的子组件纵向布局。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### 属性

除支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)外，还支持以下属性：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/kWfI0KCyQByLayHW7YDabA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014758Z&HW-CC-Expire=86400&HW-CC-Sign=FA56BB283485F2DC7DDE66F036FE9CE77416F3D36F79F0A1BD494DB8715C86BB)

ColumnSplit组件[形状裁剪](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-sharp-clipping)的默认值为true。

#### \[h2\]resizeable

resizeable(value: boolean)

设置分割线是否可拖拽。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| value | boolean | 是 | 
分割线是否可拖拽。设置为true时表示分割线可拖拽，设置为false时表示分割线不可拖拽。

默认值：false

非法值：按默认值处理。

 |

#### \[h2\]divider10+

divider(value: ColumnSplitDividerStyle | null)

设置分割线的margin。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| value | [ColumnSplitDividerStyle](#columnsplitdividerstyle10对象说明) | null | 是 | 
分割线的margin，即设置分割线与子组件的距离。

默认值：null。当设置为null时，分割线与子组件的距离为0vp。

非法值：按默认值处理。

 |

#### ColumnSplitDividerStyle10+对象说明

设置子组件与上下分割线的距离。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| startMargin | [Dimension](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#dimension10) | 否 | 是 | 
子组件与其上方分割线的距离。

默认值：0vp

非法值：按默认值处理，此时[getInspectorByKey()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-component-id#getinspectorbykey9)接口获取到的属性值为undefined。

 |
| endMargin | [Dimension](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#dimension10) | 否 | 是 | 

子组件与其下方分割线的距离。

默认值：0vp

非法值：按默认值处理，此时[getInspectorByKey()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-component-id#getinspectorbykey9)接口获取到的属性值为undefined。

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/4sd4BO8TRd6XumBxvUJz5g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014758Z&HW-CC-Expire=86400&HW-CC-Sign=A241E7633701F2989E52E83940425B84D880F2C4E1761E6A0D25B210BF9503CA)

与[RowSplit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-rowsplit)相同，ColumnSplit的分割线可调整上下两侧子组件的高度，子组件的高度调整范围受其最大最小高度限制。

支持[clip](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-sharp-clipping#clip12)、[margin](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#margin)等通用属性，未设置clip属性时，其默认值为true。

#### 事件

支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-events)。

#### 示例

#### \[h2\]示例1（设置可拖动的ColumnSplit组件）

本示例展示如何设置可拖动的ColumnSplit组件及其效果。

```ts
// xxx.ets
@Entry
@Component
struct ColumnSplitExample {
  build() {
    Column() {
      Text('The dividing line can be dragged').fontSize(9).fontColor(0xCCCCCC).width('90%')
      ColumnSplit() {
        Text('1').width('100%').height(50).backgroundColor(0xF5DEB3).textAlign(TextAlign.Center)
        Text('2').width('100%').height(50).backgroundColor(0xD2B48C).textAlign(TextAlign.Center)
        Text('3').width('100%').height(50).backgroundColor(0xF5DEB3).textAlign(TextAlign.Center)
        Text('4').width('100%').height(50).backgroundColor(0xD2B48C).textAlign(TextAlign.Center)
        Text('5').width('100%').height(50).backgroundColor(0xF5DEB3).textAlign(TextAlign.Center)
      }
      .borderWidth(1)
      .resizeable(true) // 可拖动
      .width('90%').height('60%')
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/q3bucfwsRsiGQP8Sg64R1g/zh-cn_image_0000002538180478.gif?HW-CC-KV=V1&HW-CC-Date=20260417T014758Z&HW-CC-Expire=86400&HW-CC-Sign=73FFF3B8FF7AD4E0254B0CDDAD2FE73165E4BAE54593FE1818D43C66F1F67375)

#### \[h2\]示例2（设置带有间隔的ColumnSplit组件）

本示例展示如何设置带有间隔的ColumnSplit组件及其效果。

```ts
// xxx.ets
@Entry
@Component
struct ColumnSplitDividerExample {
  build() {
    Column() {
      Text('The dividing line can be dragged').fontSize(9).fontColor(0xCCCCCC).width('90%')
      ColumnSplit() {
        Text('1').width('100%').height(50).backgroundColor(0xF5DEB3).textAlign(TextAlign.Center)
        Text('2').width('100%').height(50).backgroundColor(0xD2B48C).textAlign(TextAlign.Center)
        Text('3').width('100%').height(50).backgroundColor(0xF5DEB3).textAlign(TextAlign.Center)
        Text('4').width('100%').height(50).backgroundColor(0xD2B48C).textAlign(TextAlign.Center)
        Text('5').width('100%').height(50).backgroundColor(0xF5DEB3).textAlign(TextAlign.Center)
      }
      .borderWidth(1)
      .divider({ startMargin: 5, endMargin: 5 }) // 设置间隔
      .width('90%')
      .height('60%')
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/OqrUjn0NR2qtVDzc8gxOug/zh-cn_image_0000002569020265.png?HW-CC-KV=V1&HW-CC-Date=20260417T014758Z&HW-CC-Expire=86400&HW-CC-Sign=EEA93ECE963FE25183A2990EA5A84F573A98373924593D3AA3CB22A23A34F46C)

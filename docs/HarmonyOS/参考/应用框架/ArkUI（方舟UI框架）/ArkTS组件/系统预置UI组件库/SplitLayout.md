---
title: "SplitLayout"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-splitlayout"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "ArkTS组件"
  - "系统预置UI组件库"
  - "SplitLayout"
captured_at: "2026-04-17T01:47:59.762Z"
---

# SplitLayout

上下结构布局介绍了常用的页面布局样式。主要分为上下文本和上下图文两种类型。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/H8eQ6V61TW2S3o5XPxT_Dg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014802Z&HW-CC-Expire=86400&HW-CC-Sign=3BED2A4D11B9E31EA07335B9ABD08CA0476FDE74F20944239698BD869FDA7BBC)

-   该组件从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
    
-   该组件仅可在Stage模型下使用。
    
-   如果SplitLayout设置[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)和[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-events)，编译工具链会额外生成节点\_\_Common\_\_，并将通用属性或通用事件挂载在\_\_Common\_\_上，而不是直接应用到SplitLayout本身。这可能导致开发者设置的通用属性或通用事件不生效或不符合预期，因此，不建议SplitLayout设置通用属性和通用事件。
    

#### 导入模块

```ts
import { SplitLayout } from '@kit.ArkUI';
```

#### 子组件

无

#### SplitLayout

SplitLayout({mainImage: Resource, primaryText: string, secondaryText?: string, tertiaryText?: string, container: () => void })

**装饰器类型：**@Component

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| mainImage | [ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr) | 是 | @State | 传入图片。 |
| primaryText | [ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr) | 是 | @Prop | 标题内容。 |
| secondaryText | [ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr) | 否 | @Prop | 副标题内容。当需要在标题下方显示副标题时传入，不传入时取默认值，不显示副标题。 |
| tertiaryText | [ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr) | 否 | @Prop | 辅助文本。当需要显示辅助文本时传入，不传入时取默认值，不显示辅助文本。 |
| container | () => void | 是 | @BuilderParam | 容器内组件。 |

#### 事件

不支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-events)。

#### 示例

该示例通过SplitLayout实现了页面布局，并具备自适应能力。

```ts
import { SplitLayout } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State demoImage: Resource = $r("app.media.background");

  build() {
    Column() {
      SplitLayout({
        mainImage: this.demoImage,
        primaryText: '新歌推荐',
        secondaryText: '私人订制新歌精选站，为你推荐专属优质新歌;',
        tertiaryText: '每日更新',
      }) {
        Text('示例：空白区域容器内可添加组件')
          .margin({ top: 36 })
      }
    }
    .justifyContent(FlexAlign.SpaceBetween)
    .height('100%')
    .width('100%')
  }
}
```

小于等于600vp布局：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/EOEBQL6-SL-gEdgxp3n3zw/zh-cn_image_0000002569020793.png?HW-CC-KV=V1&HW-CC-Date=20260417T014802Z&HW-CC-Expire=86400&HW-CC-Sign=EC426FF38BF68A6552F447666664A8F38F73B7B5EE58C7F236709529403D6BFB)

大于600vp且小于等于840vp的布局：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/9dSHFWiAQ3ml7gmGe_hDYw/zh-cn_image_0000002568900783.png?HW-CC-KV=V1&HW-CC-Date=20260417T014802Z&HW-CC-Expire=86400&HW-CC-Sign=4BFD8FBAD7FB9166970535B9B761759F00CAF8DC59D6D0AA682682E7A8604C3A)

大于840vp布局：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/gRJRn0DdS66IBL5e3oAfsg/zh-cn_image_0000002538021082.png?HW-CC-KV=V1&HW-CC-Date=20260417T014802Z&HW-CC-Expire=86400&HW-CC-Sign=8F1D9888AFF882544F4C6DAE328F351A7935E662D4DBD4D19A36707656A8C051)

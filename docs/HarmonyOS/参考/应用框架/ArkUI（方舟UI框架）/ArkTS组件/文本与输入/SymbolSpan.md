---
title: "SymbolSpan"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "ArkTS组件"
  - "文本与输入"
  - "SymbolSpan"
captured_at: "2026-04-17T01:47:57.263Z"
---

# SymbolSpan

作为Text组件的子组件，用于显示图标小符号的组件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/dyjBDJFGTjalz9th9uLY_A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=4F11CB72CAF194820630942722F8324E9C28AA59670F8ED9502F042892083AE8)

-   该组件从API version 11开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
    
-   该组件支持继承父组件Text的属性，即如果子组件未设置属性且父组件设置属性，则继承父组件设置的全部属性。
    
-   SymbolSpan拖拽不会置灰显示。
    

#### 子组件

不支持子组件。

#### 接口

SymbolSpan(value: Resource)

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| value | [Resource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resource) | 是 | SymbolSpan组件的资源名，如 $r('sys.symbol.ohos\_wifi')。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/iqQWn7NdRgOfT3ACqeuKFw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=6A8B733A1356D7F8B9E85D70E97E55086A0D32088C40EA0C85D3198462524209)

$r('sys.symbol.ohos\_wifi')中引用的资源为系统预置，SymbolSpan仅支持系统预置的symbol资源名，引用非symbol资源将显示异常。

#### 属性

不支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)，支持以下属性：

#### \[h2\]fontColor

fontColor(value: Array<ResourceColor>)

设置SymbolSpan组件颜色。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/qNy78NwQTiKkUuy6UFwGMQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=288DFBDF92FC06DC11EFEB6B80425F8431C1E36E14F30C4F9329FFA8C52F67C4)

从API version 12开始，该接口支持在[attributeModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#attributemodifier)中调用。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| value | Array<[ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor)\> | 是 | 
SymbolSpan组件颜色。

默认值：不同渲染策略下默认值不同。

 |

#### \[h2\]fontSize

fontSize(value: number | string | Resource)

设置SymbolSpan组件大小。设置string类型时，支持number类型取值的字符串形式，可以附带单位，例如"10"、"10fp"。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/z_gP5K_nQjyOOqMFE4CrgA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=C55A9E293A11A15C9A71F7A0B0ABCFBD0981709A3B1217676CFCDAFD0F954BF3)

从API version 12开始，该接口支持在[attributeModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#attributemodifier)中调用。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| value | number | string | [Resource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resource) | 是 | 
SymbolSpan组件大小。

默认值：16fp

单位：[fp](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-pixel-units)

 |

#### \[h2\]fontWeight

fontWeight(value: number | FontWeight | string)

设置SymbolSpan组件粗细。number类型取值\[100,900\]，取值间隔为100，默认为400，取值越大，字体越粗。string类型仅支持number类型取值的字符串形式，例如“400”，以及“bold”、“bolder”、“lighter”、“regular” 、“medium”分别对应FontWeight中相应的枚举值。

sys.symbol.ohos\_lungs图标不支持设置fontWeight。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/pbPJKtL8T-W-mjbAdEQfsw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=FEBFAE1FCD3357D8502B4DFBC3A5379A6C540FB20A22AF4A3CF84D6F376B155B)

从API version 12开始，该接口支持在[attributeModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#attributemodifier)中调用。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| value | number | [FontWeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#fontweight) | string | 是 | 
SymbolSpan组件粗细。

默认值：FontWeight.Normal

 |

#### \[h2\]renderingStrategy

renderingStrategy(value: SymbolRenderingStrategy)

设置SymbolSpan渲染策略。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/FC1ePTtqRx2Eeikfo3GwXg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=F669157D0AE7E1DE5DA223919F381444AFEA6D8457D25AAD6A728A078EF1C8EA)

从API version 12开始，该接口支持在[attributeModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#attributemodifier)中调用。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| value | [SymbolRenderingStrategy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#symbolrenderingstrategy11枚举说明) | 是 | 
SymbolSpan渲染策略。

默认值：SymbolRenderingStrategy.SINGLE

 |

不同渲染策略效果可参考以下示意图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/pCM4YLc-RhaOHzGjsNgGWQ/zh-cn_image_0000002538020766.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=83D57070A45B50D7FB03FA66B1C2161A231A2B0627414F0741C4889EFEB1EF07)

#### \[h2\]effectStrategy

effectStrategy(value: SymbolEffectStrategy)

设置SymbolSpan动效策略。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/g9jPp6sFTd6_oOVg3PJElg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=AC2B9C587029B1D8D21554E6B6346CEC9D5584927D8AF198FEAD3BB332B0465B)

从API version 12开始，该接口支持在[attributeModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#attributemodifier)中调用。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| value | [SymbolEffectStrategy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#symboleffectstrategy11枚举说明) | 是 | 
SymbolSpan动效策略。

默认值：SymbolEffectStrategy.NONE

 |

#### \[h2\]attributeModifier12+

attributeModifier(modifier: AttributeModifier<SymbolSpanAttribute>)

设置组件的动态属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| modifier | [AttributeModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#attributemodifiert)<SymbolSpanAttribute> | 是 | 动态设置组件的属性。 |

#### 事件

不支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-events)。

#### 示例

#### \[h2\]示例1（设置渲染和动效策略）

从API version 11开始，该示例通过[renderingStrategy](#renderingstrategy)、[effectStrategy](#effectstrategy)属性展示了不同的渲染和动效策略。

```ts
// xxx.ets
@Entry
@Component
struct Index {
  build() {
    Column() {
      Row() {
        Column() {
          Text("Light")
          Text() {
            SymbolSpan($r('sys.symbol.ohos_trash'))
              .fontWeight(FontWeight.Lighter)
              .fontSize(96)
          }
        }

        Column() {
          Text("Normal")
          Text() {
            SymbolSpan($r('sys.symbol.ohos_trash'))
              .fontWeight(FontWeight.Normal)
              .fontSize(96)
          }
        }

        Column() {
          Text("Bold")
          Text() {
            SymbolSpan($r('sys.symbol.ohos_trash'))
              .fontWeight(FontWeight.Bold)
              .fontSize(96)
          }
        }
      }

      Row() {
        Column() {
          Text("单色")
          Text() {
            SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))
              .fontSize(96)
              .renderingStrategy(SymbolRenderingStrategy.SINGLE)
              .fontColor([Color.Black, Color.Green, Color.White])
          }
        }

        Column() {
          Text("多色")
          Text() {
            SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))
              .fontSize(96)
              .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
              .fontColor([Color.Black, Color.Green, Color.White])
          }
        }

        Column() {
          Text("分层")
          Text() {
            SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))
              .fontSize(96)
              .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_OPACITY)
              .fontColor([Color.Black, Color.Green, Color.White])
          }
        }
      }

      Row() {
        Column() {
          Text("无动效")
          Text() {
            SymbolSpan($r('sys.symbol.ohos_wifi'))
              .fontSize(96)
              .effectStrategy(SymbolEffectStrategy.NONE)
          }
        }

        Column() {
          Text("整体缩放动效")
          Text() {
            SymbolSpan($r('sys.symbol.ohos_wifi'))
              .fontSize(96)
              .effectStrategy(SymbolEffectStrategy.SCALE)
          }
        }

        Column() {
          Text("层级动效")
          Text() {
            SymbolSpan($r('sys.symbol.ohos_wifi'))
              .fontSize(96)
              .effectStrategy(SymbolEffectStrategy.HIERARCHICAL)
          }
        }
      }
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/7baRJDwpQFaBooSem-8m-g/zh-cn_image_0000002538180692.gif?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=0579ACDBBE5541984C4FFEB315EC427F29304A805E6F8668802C7F721AF957DE)

#### \[h2\]示例2（设置动态属性）

从API version 12开始，该示例通过[attributeModifier](#attributemodifier12)属性创建指定样式图标。

```ts
import { SymbolSpanModifier } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State modifier: SymbolSpanModifier =
    new SymbolSpanModifier($r("sys.symbol.ohos_wifi")).fontColor([Color.Blue]).fontSize(100);

  build() {
    Row() {
      Column() {
        Text() {
          SymbolSpan(undefined).attributeModifier(this.modifier)
        }

        Button('更改SymbolSpanModifier')
          .onClick(() => {
            this.modifier = new SymbolSpanModifier($r("sys.symbol.ohos_trash")).fontColor([Color.Red]).fontSize(100);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/YkGKEniZSNSUhZK0Dv4FCA/zh-cn_image_0000002569020479.gif?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=773A1920E31237005C81F9648992B88876A71BC8162F7822EB9ECB2D3CD8519C)

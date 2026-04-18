---
title: "动态SymbolGlyphModifier属性设置"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/universal-attributes-attribute-symbolglyphmodifier"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "ArkTS组件"
  - "通用属性"
  - "动态属性与自定义"
  - "动态SymbolGlyphModifier属性设置"
captured_at: "2026-04-17T01:47:55.548Z"
---

# 动态SymbolGlyphModifier属性设置

SymbolGlyphModifier用于动态设置SymbolGlyph组件的属性和样式，支持使用if/else语句进行设置。[SymbolGlyph](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph)是一个用于展示图标符号的组件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/7pZ1FQTMQIOcR1bJNZdtyw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014757Z&HW-CC-Expire=86400&HW-CC-Sign=99F3FA8FA17AA4F7F232FFDB5D73B8EE0ED3F1515420D1C0B91445FE7570F55E)

从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### SymbolGlyphModifier

定义SymbolGlyphModifier。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]constructor

constructor(src?: Resource)

SymbolGlyphModifier的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| src | [Resource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resource) | 否 | 资源信息。 |

#### \[h2\]applyNormalAttribute

applyNormalAttribute?(instance: SymbolGlyphAttribute): void

组件普通状态时的样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| instance | [SymbolGlyphAttribute](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph) | 是 | 动态设置SymbolGlyph组件的属性。 |

#### 示例

该示例通过[SymbolGlyphModifier](#symbolglyphmodifier)和TextInput组件的[cancelButton](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#cancelbutton18)属性展示了自定义右侧symbol类型清除按钮样式的效果。

```ts
import { SymbolGlyphModifier } from '@kit.ArkUI';

// xxx.ets
@Entry
@Component
struct Index {
  @State text: string = '';
  symbolModifier: SymbolGlyphModifier =
    new SymbolGlyphModifier($r('sys.symbol.trash')).fontColor([Color.Red]).fontSize(16).fontWeight(FontWeight.Regular);

  build() {
    Column() {
      TextInput({ text: this.text, placeholder: 'input your word...' })
        .height(50)
        .cancelButton({
          style: CancelButtonStyle.CONSTANT,
          icon: this.symbolModifier // 从API version 18开始支持symbol类型
        })
    }.margin(10)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/r1rze3fxSDqOxaCj7zuz8g/zh-cn_image_0000002538180454.png?HW-CC-KV=V1&HW-CC-Date=20260417T014757Z&HW-CC-Expire=86400&HW-CC-Sign=E1FBCD4754470DAA10239C7A106F8E99F3542F70FD703F91E24E115610521938)

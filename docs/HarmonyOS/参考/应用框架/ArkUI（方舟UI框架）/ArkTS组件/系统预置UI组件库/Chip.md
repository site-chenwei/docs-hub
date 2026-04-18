---
title: "Chip"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-chip"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "ArkTS组件"
  - "系统预置UI组件库"
  - "Chip"
captured_at: "2026-04-17T01:47:59.486Z"
---

# Chip

Chip用于搜索框历史记录、邮件发送列表等场景。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/i-StA_OlQFmhzqpR8JryKw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014801Z&HW-CC-Expire=86400&HW-CC-Sign=D776136E5034A6520B8790D2197C9954B9C88E4A24C548AD2B4BCA4179590586)

该组件从API version 11开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 导入模块

```ts
import { Chip, ChipOptions, ChipSize } from '@kit.ArkUI';
```

#### 子组件

无

#### Chip

Chip(options:ChipOptions): void

**装饰器类型：**@Builder

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常， 异常信息中提示接口未定义，在其他设备中可正常调用。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [ChipOptions](#chipoptions) | 是 | 定义Chip组件的参数。 |

#### ChipOptions

ChipOptions定义Chip的样式及具体式样参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| size | [ChipSize](#chipsize) | [SizeOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#sizeoptions) | 否 | 是 | 
Chip尺寸。

默认值：ChipSize.NORMAL

SizeOptions类型参数不支持百分比设置，异常值按默认值处理。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**说明**：[适老化](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkui-support-for-aging-adaptation)在size指定具体宽高时不生效，size设置为{ height: 0, width: 0 }除外。

 |
| enabled | boolean | 否 | 是 | 

Chip是否可选中。

默认值：true。

true：操作块可选中；false：操作块不可选中。

值为undefined时，按默认值处理。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| activated12+ | boolean | 否 | 是 | 

Chip是否为激活态。

默认值：false。

true：操作块为激活态；false：操作块为非激活态。

值为undefined时，按默认值处理。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| prefixIcon | [PrefixIconOptions](#prefixiconoptions) | 否 | 是 | 

前缀图标属性。

默认值：不显示前缀图标。

值为undefined时，按默认值处理。

prefixIcon和prefixSymbol同时设置时，显示prefixSymbol的效果，prefixIcon无效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| prefixSymbol12+ | [ChipSymbolGlyphOptions](#chipsymbolglyphoptions12) | 否 | 是 | 

前缀图标属性，symbol类型。

默认值：不显示前缀图标。

值为undefined时，按默认值处理。

prefixIcon和prefixSymbol同时设置时，显示prefixSymbol的效果，prefixIcon无效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| label | [LabelOptions](#labeloptions) | 否 | 否 | 

文本属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| suffixIcon | [SuffixIconOptions](#suffixiconoptions) | 否 | 是 | 

后缀图标属性。

默认值：不显示后缀图标。

值为undefined时，按默认值处理。

suffixIcon和suffixSymbol同时设置时，显示suffixSymbol的效果，suffixIcon无效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| suffixSymbol12+ | [ChipSymbolGlyphOptions](#chipsymbolglyphoptions12) | 否 | 是 | 

后缀图标属性，symbol类型。

默认值：不显示后缀图标。

值为undefined时，按默认值处理。

suffixIcon和suffixSymbol同时设置时，显示suffixSymbol的效果，suffixIcon无效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| suffixSymbolOptions14+ | [ChipSuffixSymbolGlyphOptions](#chipsuffixsymbolglyphoptions14) | 否 | 是 | 

symbol类型后缀图标属性的无障碍朗读功能属性。

默认值：不显示后缀图标。

值为undefined时，按默认值处理。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

 |
| backgroundColor | [ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor) | 否 | 是 | 

Chip背景颜色。

默认值：$r('sys.color.ohos\_id\_color\_button\_normal')。

值为undefined时，按默认值处理。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| activatedBackgroundColor12+ | [ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor) | 否 | 是 | 

Chip激活时的背景颜色。

默认值：$r('sys.color.ohos\_id\_color\_emphasize')。

值为undefined时，按默认值处理。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| borderRadius | [Dimension](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#dimension10) | 否 | 是 | 

Chip背景圆角半径大小，不支持百分比。

默认值：$r('sys.float.ohos\_id\_corner\_radius\_button')。

值为undefined时，按默认值处理。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| allowClose | boolean | 否 | 是 | 

关闭图标是否显示。

默认值：true

true：删除图标显示；false：删除图标不显示。

值为undefined时，按默认值处理。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| onClose | ()=>void | 否 | 是 | 

默认关闭图标点击事件。

值为undefined时，关闭图标点击事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| onClicked12+ | Callback<void> | 否 | 是 | 

Chip点击事件。

值为undefined时，Chip不能被点击。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| direction12+ | [Direction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#direction) | 否 | 是 | 

布局方向。

默认值：Direction.Auto。

值为undefined时，按默认值处理。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| closeOptions14+ | [CloseOptions](#closeoptions14) | 否 | 是 | 

默认关闭图标的无障碍朗读功能属性。

值为undefined时，按默认值处理。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

 |
| accessibilityDescription14+ | [ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr) | 否 | 是 | 

Chip组件的无障碍描述。此描述用于向用户详细解释当前组件，开发人员应为组件的这一属性提供较为详尽的文本说明，以协助用户理解即将执行的操作及其可能产生的结果。特别是当这些结果无法仅从组件的属性和无障碍文本中直接获知时。如果组件同时具备文本属性和无障碍说明属性，当组件被选中时，系统将首先播报组件的文本属性，随后播报无障碍说明属性的内容。

默认值：空字符串。

值为undefined时，按默认值处理。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

 |
| accessibilityLevel14+ | string | 否 | 是 | 

Chip组件无障碍重要性。用于控制后缀图标是否可被无障碍辅助服务所识别。

支持的值为:

"auto"：当前组件会转化为"yes"。

"yes"：当前组件可被无障碍辅助服务所识别。

"no"：当前组件不可被无障碍辅助服务所识别。

"no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。

默认值："auto"。

值为undefined时，按默认值处理。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

 |
| accessibilitySelectedType14+ | [AccessibilitySelectedType](#accessibilityselectedtype14) | 否 | 是 | 

Chip组件选中态类型。

默认值：当设置了activated属性但未指定accessibilitySelectedType时，默认使用CHECKED类型。当未设置activated属性时，默认使用CLICKED类型。

值为undefined时，按默认值处理。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

 |
| maxFontScale23+ | number | [Resource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resource) | 否 | 是 | 

Chip组件文本与图标的最大的字体缩放倍数。

取值范围：\[1, +∞)

设置的值小于1时，按值为1处理。异常值默认不生效。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

 |
| minFontScale23+ | number | [Resource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resource) | 否 | 是 | 

Chip组件文本与图标的最小的字体缩放倍数。

取值范围：\[0, 1\]

设置的值小于0时，按值为0处理。设置的值大于1时，按值为1处理。异常值默认不生效。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

 |
| padding23+ | [LocalizedPadding](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#localizedpadding12) | 否 | 是 | 

Chip组件的内边距。

默认值：

\- size为ChipSize.SMALL并且activated为true时，默认值：{ start: LengthMetrics.resource('sys.float.chip\_activated\_small\_text\_padding'), end: LengthMetrics.resource('sys.float.chip\_activated\_small\_text\_padding'), top: LengthMetrics.vp(4), bottom: LengthMetrics.vp(4)}

\- size为ChipSize.SMALL并且activated为false时，默认值：{ start: LengthMetrics.resource('sys.float.chip\_small\_text\_padding'), end: LengthMetrics.resource('sys.float.chip\_small\_text\_padding'), top: LengthMetrics.vp(4), bottom: LengthMetrics.vp(4)}

\- size不为ChipSize.SMALL并且activated为true时，默认值：{ start: LengthMetrics.resource('sys.float.chip\_activated\_normal\_text\_padding'), end: LengthMetrics.resource('sys.float.chip\_activated\_normal\_text\_padding'), top: LengthMetrics.vp(4), bottom: LengthMetrics.vp(4)}

\- size不为ChipSize.SMALL并且activated为false时，默认值：{ start: LengthMetrics.resource('sys.float.chip\_normal\_text\_padding'), end: LengthMetrics.resource('sys.float.chip\_normal\_text\_padding'), top: LengthMetrics.vp(4), bottom: LengthMetrics.vp(4)}

值为undefined时，按默认值处理。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

 |
| fontSize23+ | [Dimension](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#dimension10) | 否 | 是 | 

统一设置Chip组件的文本与图标的字体大小，不支持百分比。

该fontSize的优先级低于prefixSymbol、label、suffixSymbol和closeOptions中的fontSize属性。

默认值：

\- size为ChipSize.SMALL时，文本默认值：$r('sys.float.chip\_small\_font\_size')；图标默认值：$r('sys.float.chip\_small\_icon\_size')

\- 其他情况下，文本默认值：$r('sys.float.chip\_normal\_font\_size')；图标默认值：$r('sys.float.chip\_normal\_icon\_size')

值为undefined时，按默认值处理。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/piFByWGcRguxcPRivvgXsw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014801Z&HW-CC-Expire=86400&HW-CC-Sign=7D2A35E87244A2FDEF66B599E82D5C7E47FB9F0263154D4A0DC794157BDD734F)

1.  当suffixSymbol有传入参数时，suffixIcon和allowClose不生效；当suffixSymbol没有传入参数而suffixIcon有传入参数时，allowClose不生效；当suffixSymbol和suffixIcon都没有传入参数时，allowClose决定是否显示删除图标。
    
2.  backgroundColor和activatedBackgroundColor赋值为undefined时，显示默认背景颜色；赋值为非法值时，背景颜色透明。
    
3.  prefixSymbol/suffixSymbol的fontColor默认值为：normalFontColor: \[$r('sys.color.ohos\_id\_color\_primary')\]、activatedFontColor: \[$r('sys.color.ohos\_id\_color\_text\_primary\_contrary')\]。fontColor默认值为16。
    
4.  prefixIcon的fillColor默认值为：$r('sys.color.ohos\_id\_color\_secondary')，suffixIcon的fillColor默认值为：$r('sys.color.ohos\_id\_color\_primary')。fillColor对颜色的解析与Image组件保持一致。
    
5.  prefixIcon和suffixIcon的activatedFillColor默认值均为：$r('sys.color.ohos\_id\_color\_text\_primary\_contrary')。activatedFillColor对颜色的解析与Image组件保持一致。
    

#### ChipSize

ChipSize是Chip可指定的尺寸类型，如普通型Chip。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| NORMAL | "NORMAL" | normal尺寸操作块。 |
| SMALL | "SMALL" | small尺寸操作块。 |

#### AccessibilitySelectedType14+

AccessibilitySelectedType是Chip可指定的选中态类型，用于控制无障碍服务如何向用户传达组件的选中状态。不同的选中态类型提供了不同的语义和用户体验。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| CLICKED | 0 | 单击型。组件不向无障碍服务报告任何选中状态，仅作为可单击组件使用。适用于执行某个操作但不保持状态的场景，如普通按钮。 |
| CHECKED | 1 | 复选型。组件通过 [accessibilityChecked](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-accessibility#accessibilitychecked13) 属性向无障碍服务报告选中状态。适用于多选场景，如标签筛选、属性选择等。 |
| SELECTED | 2 | 单选型。组件通过 [accessibilitySelected](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-accessibility#accessibilityselected13) 属性向无障碍服务报告选中状态。适用于表示当前选中项的场景，如导航栏标签、单选列表项等。 |

#### IconCommonOptions

IconCommonOptions定义图标的共通属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| src | [ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr) | 否 | 否 | 图标图片或图片地址引用。 |
| size | [SizeOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#sizeoptions) | 否 | 是 | 
图标大小，不支持百分比。

默认值：

\- 当ChipOptions.size为ChipSize.SMALL时，默认值为：{width: $r('sys.float.chip\_small\_icon\_size'), height: $r('sys.float.chip\_small\_icon\_size')}

\- 当ChipOptions.size为ChipSize.NORMAL时，默认值为：{width: $r('sys.float.chip\_normal\_icon\_size'), height: $r('sys.float.chip\_normal\_icon\_size')}

单位：vp

值为undefined时，按默认值处理。

 |
| fillColor | [ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor) | 否 | 是 | 

图标填充颜色。

默认值：$r('sys.color.chip\_usually\_icon\_color')

值为undefined时，按默认值处理。

 |
| activatedFillColor12+ | [ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor) | 否 | 是 | 

操作块激活时图标填充颜色。

默认值：$r('sys.color.chip\_active\_icon\_color')

值为undefined时，按默认值处理。

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/rDqpPEIYR_G0OA94_ry7iA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014801Z&HW-CC-Expire=86400&HW-CC-Sign=8D4AC7DF67931FD5ACA639D7E68E6C1391D15F04B531A9772FD2C5700C656788)

仅在图片格式为SVG时，fillColor和activatedFillColor属性才生效。

#### PrefixIconOptions

PrefixIconOptions定义前缀图标的属性。

继承于[IconCommonOptions](#iconcommonoptions)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

#### SuffixIconOptions

SuffixIconOptions定义后缀图标的属性。

继承于[IconCommonOptions](#iconcommonoptions)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| action | () => void | 否 | 是 | 
后缀图标设定事件。

值为undefined时，不设定后缀图标事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| accessibilityText14+ | [ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr) | 否 | 是 | 

后缀图标无障碍文本属性。当后缀图标不包含文本属性时，屏幕朗读选中后缀图标时不播报，使用者无法清楚地知道当前是否选中了后缀图标。为了解决此场景，开发人员可为不包含文字信息的后缀图标设置无障碍文本，当屏幕朗读选中后缀图标时播报无障碍文本的内容，帮助屏幕朗读的使用者清楚地知道自己是否选中了后缀图标。

默认值：‘ ’

值为undefined时，按默认值处理。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

 |
| accessibilityDescription14+ | [ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr) | 否 | 是 | 

后缀图标的无障碍描述。此描述用于向用户详细解释后缀图标，开发人员应为后缀图标的这一属性提供较为详尽的文本说明，以协助用户理解即将执行的操作及其可能产生的后果。特别是当这些后果无法仅从后缀图标的属性和无障碍文本中直接获知时。如果后缀图标同时具备文本属性和无障碍说明属性，当后缀图标被选中时，系统将首先播报后缀图标的文本属性，随后播报无障碍说明属性的内容。

默认值：‘ ’

值为undefined时，按默认值处理。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

 |
| accessibilityLevel14+ | string | 否 | 是 | 

后缀图标的无障碍重要性。用于控制后缀图标是否可被无障碍辅助服务识别。

支持的值为:

"auto"：当前组件存在action时转化为"yes"，不存在action时，转化为"no"。

"yes"：当前组件可被无障碍辅助服务所识别。

"no"：当前组件不可被无障碍辅助服务所识别。

"no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。

默认值："auto"。

值为undefined时，按默认值处理。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

 |

#### AccessibilityOptions14+

后缀图标的无障碍朗读功能属性。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| accessibilityText | [ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr) | 否 | 是 | 
无障碍文本属性。当组件无文本属性时，屏幕朗读选中此组件不会播报，导致使用者无法清楚了解当前选中的组件。开发人员可为此类组件设置无障碍文本，屏幕朗读时将播报该文本，帮助使用者明确选中了什么组件。

默认值：‘ ’

值为undefined时，按默认值处理。

 |
| accessibilityDescription | [ResourceStr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcestr) | 否 | 是 | 

无障碍描述。此描述用于向用户详细解释当前组件，开发人员应提供详尽的文本说明，以协助用户理解即将执行的操作及其后果。特别是当这些后果无法仅从组件的属性和无障碍文本中直接获知时。如果组件同时具备文本属性和无障碍说明属性，当组件被选中时，系统将首先播报组件的文本属性，随后播报无障碍说明属性的内容。

默认值：‘ ’

值为undefined时，按默认值处理。

 |
| accessibilityLevel | string | 否 | 是 | 

无障碍重要性。用于控制组件是否可被无障碍辅助服务识别。

支持的值为:

"auto"：当前组件会转换为"yes"。

"yes"：当前组件可被无障碍辅助服务所识别。

"no"：当前组件不可被无障碍辅助服务所识别。

"no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。

默认值："auto"。

值为undefined时，按默认值处理。

 |

#### ChipSuffixSymbolGlyphOptions14+

symbol类型后缀图标属性的无障碍朗读功能属性类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| action | [VoidCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#voidcallback12) | 否 | 是 | 
后缀图标设定事件。

默认值：undefined

 |
| normalAccessibility | [AccessibilityOptions](#accessibilityoptions14) | 否 | 是 | 

非激活态无障碍朗读功能属性。

默认值：undefined

 |
| activatedAccessibility | [AccessibilityOptions](#accessibilityoptions14) | 否 | 是 | 

激活态无障碍朗读功能属性。

默认值：undefined

 |

#### ChipSymbolGlyphOptions12+

ChipSymbolGlyphOptions定义前缀图标和后缀图标的属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| normal | [SymbolGlyphModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/universal-attributes-attribute-symbolglyphmodifier#symbolglyphmodifier) | 否 | 是 | 
非激活时图标设定。

默认值：不显示前缀图标或后缀图标

值为undefined时，按默认值处理。

 |
| activated | [SymbolGlyphModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/universal-attributes-attribute-symbolglyphmodifier#symbolglyphmodifier) | 否 | 是 | 

激活时图标设定。

默认值：不显示前缀图标或后缀图标

值为undefined时，按默认值处理。

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/9jY3xWx0SAKgm4kSYG357w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014801Z&HW-CC-Expire=86400&HW-CC-Sign=E3C3DE6D1F1B599849C501ECAA11FD0E6566A3AEBCF182D4ACBA83E85F7F524F)

不支持使用[SymbolEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#symboleffect12对象说明)修改动效类型及effectStrategy设置动效。

#### LabelOptions

LabelOptions定义文本属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| text | string | 否 | 否 | 文本文字内容。 |
| fontSize | [Dimension](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#dimension10) | 否 | 是 | 
文字字号，不支持百分比。

默认值：$r('sys.float.ohos\_id\_text\_size\_button2')

值为undefined时，按默认值处理。

 |
| fontColor | [ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor) | 否 | 是 | 

文字颜色。

默认值：$r('sys.color.ohos\_id\_color\_text\_primary')

值为undefined时，按默认值处理。

 |
| activatedFontColor12+ | [ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor) | 否 | 是 | 

操作块激活时的文字颜色。

默认值：$r('sys.color.ohos\_id\_color\_text\_primary\_contrary')

值为undefined时，按默认值处理。

 |
| fontFamily | string | 否 | 是 | 

文字字体。

默认值："HarmonyOS Sans"

值为undefined时，按默认值处理。

 |
| labelMargin | [LabelMarginOptions](#labelmarginoptions) | 否 | 是 | 

文本与左右侧图标之间间距。

默认值：

size为ChipSize.SMALL时，默认值：{ left: 4, right: 4 }

size为ChipSize.NORMAL时，默认值：{ left: 6, right: 6 }

单位：vp

值为undefined时，按默认值处理。

 |
| localizedLabelMargin12+ | [LocalizedLabelMarginOptions](#localizedlabelmarginoptions12) | 否 | 是 | 

本地化文本与左右侧图标之间间距。

默认值：

size为ChipSize.SMALL时，默认值：

{ start: LengthMetrics.resource($r('sys.float.chip\_small\_text\_margin')), end: LengthMetrics.resource($r('sys.float.chip\_small\_text\_margin')) }

size为ChipSize.NORMAL时，默认值：

{ start: LengthMetrics.resource($r('sys.float.chip\_normal\_text\_margin')), end: LengthMetrics.resource($r('sys.float.chip\_normal\_text\_margin')) }

值为undefined时，按默认值处理。

 |

#### CloseOptions14+

CloseOptions用于定义Chip组件默认的关闭图标功能属性，包括无障碍功能属性，其中accessibilityText默认为"删除"。

继承于[AccessibilityOptions](#accessibilityoptions14)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| fontSize23+ | [Dimension](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#dimension10) | 否 | 是 | 
设置Chip组件默认关闭图标的大小，不支持百分比。

默认值：

size为ChipSize.SMALL时，默认值：$r('sys.float.chip\_small\_font\_size')

其他情况默认值：$r('sys.float.chip\_normal\_font\_size')

值为undefined时，按默认值处理。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

 |

#### LabelMarginOptions

LabelMarginOptions用于定义文本与左右侧图标之间间距。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| left | [Dimension](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#dimension10) | 否 | 是 | 
文本与左侧图标之间间距，不支持百分比。

默认值：

size为ChipSize.SMALL时，left默认值：4

size为ChipSize.NORMAL时，left默认值：6

单位：vp

超出取值范围按默认值处理。

取值范围：\[0, +∞)

 |
| right | [Dimension](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#dimension10) | 否 | 是 | 

文本与右侧图标之间间距，不支持百分比。

默认值：

size为ChipSize.SMALL时，right默认值：4

size为ChipSize.NORMAL时，right默认值：6

单位：vp

超出取值范围按默认值处理。

取值范围：\[0, +∞)

 |

#### LocalizedLabelMarginOptions12+

LocalizedLabelMarginOptions用于定义本地化文本与左右侧图标之间间距。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| start | [LengthMetrics](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-graphics#lengthmetrics12) | 否 | 是 | 
文本与左侧图标之间间距，不支持百分比。

默认值：

size为ChipSize.SMALL时，start默认值:

LengthMetrics.resource($r('sys.float.chip\_small\_text\_margin'))

size为ChipSize.NORMAL时，start默认值：

LengthMetrics.resource($r('sys.float.chip\_normal\_text\_margin'))

值为undefined时，按默认值处理。

 |
| end | [LengthMetrics](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-graphics#lengthmetrics12) | 否 | 是 | 

文本与右侧图标之间间距，不支持百分比。

默认值：

size为ChipSize.SMALL时，end默认值：

LengthMetrics.resource($r('sys.float.chip\_small\_text\_margin'))

size为ChipSize.NORMAL时，end默认值:

LengthMetrics.resource($r('sys.float.chip\_normal\_text\_margin'))

值为undefined时，按默认值处理。

 |

#### 示例

#### \[h2\]示例1（自定义后缀图标）

通过配置suffixIcon实现自定义操作块的后缀图标。

```ts
import { Chip, ChipSize, LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    Column({ space: 10 }) {
      Chip({
        // 设置前缀图标属性。
        prefixIcon: {
          // 'app.media.chips'仅作示例，请替换为实际使用图片。
          src: $r('app.media.chips'),
          size: { width: 16, height: 16 },
          fillColor: Color.Red
        },
        // 设置文本属性。
        label: {
          text: '操作块',
          fontSize: 12,
          fontColor: Color.Blue,
          fontFamily: 'HarmonyOS Sans',
          labelMargin: { left: 20, right: 30 }
        },
        // 设置后缀图标属性。
        suffixIcon: {
          // 'app.media.close'仅作示例，请替换为实际使用图片。
          src: $r('app.media.close'),
          size: { width: 16, height: 16 },
          fillColor: Color.Red
        },
        size: ChipSize.NORMAL,
        allowClose: false,
        enabled: true,
        backgroundColor: $r('sys.color.ohos_id_color_button_normal'),
        borderRadius: $r('sys.float.ohos_id_corner_radius_button'),
        minFontScale: 0.2,
        maxFontScale: 2,
        padding: {
          start: LengthMetrics.vp(20),
          end: LengthMetrics.vp(20)
        },
        fontSize: 12
      })
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/0vDQVhZ6SpShhtQ4x15HHQ/zh-cn_image_0000002538021046.png?HW-CC-KV=V1&HW-CC-Date=20260417T014801Z&HW-CC-Expire=86400&HW-CC-Sign=8FFD0BAD413ECB04967B6998F0B47CF301A837AEE49A538DC2A1ACDAC79E3FAF)

#### \[h2\]示例2（设置默认后缀图标）

配置allowClose为true，显示后缀移除图标。

```ts
import { Chip, ChipSize, LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    Column({ space: 10 }) {
      Chip({
        // 设置前缀图标属性。
        prefixIcon: {
          // 'app.media.chips'仅作示例，请替换为实际使用图片。
          src: $r('app.media.chips'),
          size: { width: 16, height: 16 },
          fillColor: Color.Blue
        },
        // 设置文本属性。
        label: {
          text: '操作块',
          fontSize: 12,
          fontColor: Color.Blue,
          fontFamily: 'HarmonyOS Sans',
          labelMargin: { left: 20, right: 30 }
        },
        size: ChipSize.NORMAL,
        allowClose: true,
        closeOptions: {fontSize: 12},
        enabled: true,
        backgroundColor: $r('sys.color.ohos_id_color_button_normal'),
        borderRadius: $r('sys.float.ohos_id_corner_radius_button'),
        minFontScale: 0.2,
        maxFontScale: 2,
        padding: {
          start: LengthMetrics.vp(20),
          end: LengthMetrics.vp(20)
        },
        fontSize: 12
      })
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/oPgj3EMHSZeHWY9MPOKwNg/zh-cn_image_0000002538180972.png?HW-CC-KV=V1&HW-CC-Date=20260417T014801Z&HW-CC-Expire=86400&HW-CC-Sign=F21E98130CCB9C92F92E3E8E7F91C449067477FCC9CE3C773BB9AADE67FDFFC2)

#### \[h2\]示例3（不显示后缀图标）

配置allowClose为false，隐藏后缀移除图标。

```ts
import { Chip, ChipSize, LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    Column({ space: 10 }) {
      Chip({
        // 设置前缀图标属性。
        prefixIcon: {
          // 'app.media.chips'仅作示例，请替换为实际使用图片。
          src: $r('app.media.chips'),
          size: { width: 16, height: 16 },
          fillColor: Color.Blue
        },
        // 设置文本属性。
        label: {
          text: '操作块',
          fontSize: 12,
          fontColor: Color.Blue,
          fontFamily: 'HarmonyOS Sans',
          labelMargin: { left: 20, right: 30 }
        },
        size: ChipSize.SMALL,
        allowClose: false,
        enabled: true,
        backgroundColor: $r('sys.color.ohos_id_color_button_normal'),
        borderRadius: $r('sys.float.ohos_id_corner_radius_button'),
        onClose: () => {
          console.info('chip on close');
        },
        minFontScale: 0.2,
        maxFontScale: 2,
        padding: {
          start: LengthMetrics.vp(20),
          end: LengthMetrics.vp(20)
        },
        fontSize: 12
      })
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/mr5Ejn4UQ9GTtq3kWmGIYQ/zh-cn_image_0000002569020759.png?HW-CC-KV=V1&HW-CC-Date=20260417T014801Z&HW-CC-Expire=86400&HW-CC-Sign=C18067B515C1D561ADCB8DF458C76A711DB2E88317E0D7A6741E7D340B0CCA8C)

#### \[h2\]示例4（激活态操作块）

该示例通过配置activated实现激活态操作块。

```ts
import { Chip, ChipSize } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State isActivated: boolean = false;

  build() {
    Column({ space: 10 }) {
      Chip({
        // 设置前缀图标属性。
        prefixIcon: {
          // 'app.media.chips'仅作示例，请替换为实际使用图片。
          src: $r('app.media.chips'),
          size: { width: 16, height: 16 },
          fillColor: Color.Blue,
          activatedFillColor: $r('sys.color.ohos_id_color_text_primary_contrary')
        },
        // 设置文本属性。
        label: {
          text: '操作块',
          fontSize: 12,
          fontColor: Color.Blue,
          activatedFontColor: $r('sys.color.ohos_id_color_text_primary_contrary'),
          fontFamily: 'HarmonyOS Sans',
          labelMargin: { left: 20, right: 30 }
        },
        size: ChipSize.NORMAL,
        allowClose: true,
        enabled: true,
        activated: this.isActivated,
        backgroundColor: $r('sys.color.ohos_id_color_button_normal'),
        activatedBackgroundColor: $r('sys.color.ohos_id_color_emphasize'),
        borderRadius: $r('sys.float.ohos_id_corner_radius_button'),
        onClose: () => {
          console.info('chip on close');
        },
        onClicked: () => {
          console.info('chip on clicked');
        }
      })
       // 点击“改变激活状态”，用于控制操作块的激活与关闭。
      Button('改变激活状态')
        .onClick(() => {
          this.isActivated = !this.isActivated;
        })
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/jkP1EpnGTFaH83P1YtMfEw/zh-cn_image_0000002568900749.gif?HW-CC-KV=V1&HW-CC-Date=20260417T014801Z&HW-CC-Expire=86400&HW-CC-Sign=589A35623779331D9CD6D11E3A9B602C7230278FB2C5527B9E9F61E4F76D8E69)

#### \[h2\]示例5（设置symbol类型图标）

Chip组件的前缀图标使用symbol类型资源展示。

```ts
import { Chip, ChipSize, SymbolGlyphModifier } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State isActivated: boolean = false;

  build() {
    Column({ space: 10 }) {
      Chip({
        // 设置前缀图标属性，symbol类型。
        prefixSymbol: {
          normal: new SymbolGlyphModifier($r('sys.symbol.ohos_star')).fontSize(16).fontColor([Color.Green]),
          activated: new SymbolGlyphModifier($r('sys.symbol.ohos_star')).fontSize(16).fontColor([Color.Red]),
        },
        // 设置文本属性。
        label: {
          text: '操作块',
          fontSize: 12,
          fontColor: Color.Blue,
          activatedFontColor: $r('sys.color.ohos_id_color_text_primary_contrary'),
          fontFamily: 'HarmonyOS Sans',
          labelMargin: { left: 20, right: 30 },
        },
        size: ChipSize.NORMAL,
        allowClose: true,
        enabled: true,
        activated: this.isActivated,
        backgroundColor: $r('sys.color.ohos_id_color_button_normal'),
        activatedBackgroundColor: $r('sys.color.ohos_id_color_emphasize'),
        borderRadius: $r('sys.float.ohos_id_corner_radius_button'),
        onClose: () => {
          console.info('chip on close');
        },
        onClicked: () => {
          console.info('chip on clicked');
        }
      })

      Button('改变激活状态')
        .onClick(() => {
          this.isActivated = !this.isActivated;
        })
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/1-ZS8SSMTk6Vbv0r-ytBnQ/zh-cn_image_0000002538021048.gif?HW-CC-KV=V1&HW-CC-Date=20260417T014801Z&HW-CC-Expire=86400&HW-CC-Sign=A8E779CB21A09133E14CE162C8F08EDA9934BAE5CB379B21AA28ADA82EFD126E)

#### \[h2\]示例6（设置镜像效果）

配置direction实现Chip布局镜像化展示。

```ts
import { Chip, ChipSize, LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct ChipPage {
  build() {
    Column() {
      Chip({
        direction: Direction.Rtl,
        // 设置前缀图标属性。
        prefixIcon: {
          // 'app.media.chips'仅作示例，请替换为实际使用图片。
          src: $r('app.media.chips'),
          size: { width: 16, height: 16 },
          fillColor: Color.Red,
        },
        // 设置文本属性。
        label: {
          text: '操作块',
          fontSize: 12,
          fontColor: Color.Blue,
          fontFamily: 'HarmonyOS Sans',
          localizedLabelMargin: { start: LengthMetrics.vp(20), end: LengthMetrics.vp(20) },
        },
        // 设置后缀图标属性。
        suffixIcon: {
          // 'app.media.close'仅作示例，请替换为实际使用图片。
          src: $r('app.media.close'),
          size: { width: 16, height: 16 },
          fillColor: Color.Red,
        },
        size: ChipSize.NORMAL,
        allowClose: false,
        enabled: true,
        backgroundColor: $r('sys.color.ohos_id_color_button_normal'),
        borderRadius: $r('sys.float.ohos_id_corner_radius_button')
      })
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/6P4oNp5ORBS_ZXShnUoiRQ/zh-cn_image_0000002538180974.png?HW-CC-KV=V1&HW-CC-Date=20260417T014801Z&HW-CC-Expire=86400&HW-CC-Sign=84C73BE3C19DCFDDA5A186C9D56E94F7713DE8985CD4945BB4804CD9287D925B)

#### \[h2\]示例7（Image类型无障碍朗读）

该示例代码实现Chip组件Image类型后缀图标的无障碍朗读功能，点击后缀图标播报“图标，按钮，新手提醒”。

```ts
import { Chip } from '@kit.ArkUI';

@Builder
function DefaultFunction(): void {
}

@Component
struct SectionGroup {
  @Prop
  @Require
  title: ResourceStr;
  @BuilderParam
  @Require
  content: () => void = DefaultFunction;

  build() {
    Column({ space: 4 }) {
      Text(this.title)
        .fontColor('#FF666666')
        .fontSize(12)
      Column({ space: 8 }) {
        this.content()
      }
    }
    .alignItems(HorizontalAlign.Start)
    .width('100%')
  }
}

@Component
struct SectionItem {
  @Prop
  @Require
  title: ResourceStr;
  @BuilderParam
  @Require
  content: () => void = DefaultFunction;

  build() {
    Column({ space: 12 }) {
      Text(this.title)
      this.content()
    }
    .backgroundColor('#FFFFFFFF')
    .borderRadius(12)
    .padding(12)
    .width('100%')
  }
}

@Entry
@Component
struct ChipExample2 {
  @State activated: boolean = false;

  build() {
    NavDestination() {
      Scroll() {
        SectionGroup({ title: '后缀图标播报' }) {
          SectionItem({ title: '自定义播报' }) {
            Chip({
              label: { text: '操作块' },
              suffixIcon: {
                src: $r('sys.media.ohos_ic_public_cut'),
                accessibilityText: '图标', // 播报“图标，按钮，新手提醒”
                accessibilityDescription: '新手提醒',
                action: () => {
                  this.getUIContext().getPromptAction().showToast({
                    message: '后缀图标被点击！'
                  });
                }
              },
              onClicked: () => {
                this.getUIContext().getPromptAction().showToast({
                  message: '操作块被点击！'
                });
              }
            })
          }
        }
      }
    }
  }
}
```

#### \[h2\]示例8（symbol类型无障碍朗读）

该示例代码实现Chip组件symbol类型后缀图标的无障碍朗读功能，点击后缀图标播报“音乐，按钮，新手提醒”。

```ts
import { Chip, SymbolGlyphModifier } from '@kit.ArkUI';

@Builder
function DefaultFunction(): void {
}

@Component
struct SectionGroup {
  @Prop
  @Require
  title: ResourceStr;
  @BuilderParam
  @Require
  content: () => void = DefaultFunction;

  build() {
    Column({ space: 4 }) {
      Text(this.title)
        .fontColor('#FF666666')
        .fontSize(12)
      Column({ space: 8 }) {
        this.content()
      }
    }
    .alignItems(HorizontalAlign.Start)
    .width('100%')
  }
}

@Component
struct SectionItem {
  @Prop
  @Require
  title: ResourceStr;
  @BuilderParam
  @Require
  content: () => void = DefaultFunction;

  build() {
    Column({ space: 12 }) {
      Text(this.title)
      this.content()
    }
    .backgroundColor('#FFFFFFFF')
    .borderRadius(12)
    .padding(12)
    .width('100%')
  }
}

@Entry
@Component
struct ChipExample2 {
  @State activated: boolean = false;

  build() {
    NavDestination() {
      Scroll() {
        SectionGroup({ title: '后缀Symbol播报' }) {
          SectionItem({ title: 'activatedAccessibility' }) {
            Chip({
              label: { text: '操作块' },
              activated: true,
              suffixSymbol: {
                activated: new SymbolGlyphModifier($r('sys.symbol.media_sound'))
                  .fontSize(72),
              },
              suffixSymbolOptions: {
                activatedAccessibility: {
                  accessibilityText: '音乐', // 播报“音乐，按钮，新手提醒”
                  accessibilityDescription: '新手提醒'
                },
                action: () => {
                  this.getUIContext().getPromptAction().showToast({
                    message: '后缀Symbol被点击！'
                  });
                }
              },
              onClicked: () => {
                this.getUIContext().getPromptAction().showToast({
                  message: '操作块被点击！'
                });
              }
            })
          }

          SectionItem({ title: 'normalAccessibility' }) {
            Chip({
              label: { text: '操作块' },
              suffixSymbol: {
                normal: new SymbolGlyphModifier($r('sys.symbol.media_sound'))
                  .fontSize(72),
              },
              suffixSymbolOptions: {
                normalAccessibility: {
                  accessibilityText: '音乐', // 播报“音乐，按钮，新手提醒”
                  accessibilityDescription: '新手提醒'
                },
                action: () => {
                  this.getUIContext().getPromptAction().showToast({
                    message: '后缀Symbol被点击！'
                  });
                }
              },
              onClicked: () => {
                this.getUIContext().getPromptAction().showToast({
                  message: '操作块被点击！'
                });
              }
            })
          }
        }
      }
    }
    .padding({
      top: 8,
      bottom: 8,
      left: 16,
      right: 16,
    })
  }
}
```

#### \[h2\]示例9（Chip组件无障碍朗读）

示例展示Chip组件的无障碍属性设置，包括不同的accessibilitySelectedType类型和各种无障碍属性。

```ts
import { AccessibilitySelectedType, Chip, ChipSize } from '@kit.ArkUI';

@Entry
@Component
struct ChipAccessibilityExample {
  @State clickedChipActivated: boolean = false;
  @State checkedChipActivated: boolean = false;
  @State selectedChipActivated: boolean = false;

  build() {
    Column({ space: 20 }) {
      Text('Chip组件无障碍属性示例').fontSize(20).fontWeight(FontWeight.Bold)

      // 点击型Chip - CLICKED类型
      Chip({
        label: { text: '点击型Chip' },
        prefixIcon: {
          src: $r('sys.media.ohos_app_icon'),
          fillColor: Color.Blue
        },
        size: ChipSize.NORMAL,
        accessibilitySelectedType: AccessibilitySelectedType.CLICKED, // 点击型
        accessibilityDescription: '这是一个点击型Chip', // 整体无障碍描述
        accessibilityLevel: 'yes', // 确保可被无障碍服务识别
        closeOptions: {
          accessibilityDescription: '删除此Chip，此操作无法撤销' // 为删除按钮提供详细说明
        },
        activated: this.clickedChipActivated,
        onClicked: () => {
          this.clickedChipActivated = !this.clickedChipActivated;
          this.getUIContext().getPromptAction().showToast({ message: '点击型Chip被点击' });
        },
        onClose: () => {
          this.getUIContext().getPromptAction().showToast({ message: '点击型Chip的关闭按钮被点击' });
        }
      })

      // 复选型Chip - CHECKED类型
      Chip({
        label: { text: '复选型Chip' },
        prefixIcon: {
          src: $r('sys.media.ohos_app_icon'),
          fillColor: Color.Green
        },
        size: ChipSize.NORMAL,
        accessibilitySelectedType: AccessibilitySelectedType.CHECKED, // 复选型
        accessibilityDescription: '这是一个复选型Chip', // 整体无障碍描述
        activated: this.checkedChipActivated,
        onClicked: () => {
          this.checkedChipActivated = !this.checkedChipActivated;
          this.getUIContext().getPromptAction().showToast({
            message: this.checkedChipActivated ? '复选型Chip被选中' : '复选型Chip被取消选中'
          });
        }
      })

      // 单选型Chip - SELECTED类型
      Chip({
        label: { text: '单选型Chip' },
        prefixIcon: {
          src: $r('sys.media.ohos_app_icon'),
          fillColor: Color.Red
        },
        size: ChipSize.NORMAL,
        accessibilitySelectedType: AccessibilitySelectedType.SELECTED, // 单选型
        accessibilityDescription: '这是一个单选型Chip', // 整体无障碍描述
        activated: this.selectedChipActivated,
        onClicked: () => {
          this.selectedChipActivated = !this.selectedChipActivated;
          this.getUIContext().getPromptAction().showToast({
            message: this.selectedChipActivated ? '单选型Chip被选中' : '单选型Chip被取消选中'
          });
        }
      })

      // 无障碍级别设置示例
      Chip({
        label: { text: '无障碍级别为no' },
        size: ChipSize.NORMAL,
        accessibilityLevel: 'no', // 此Chip不能被无障碍服务识别
        closeOptions: {
          accessibilityLevel: 'no'
        },
        backgroundColor: '#CCCCCC',
        onClicked: () => {
          this.getUIContext().getPromptAction().showToast({ message: '此Chip无法被无障碍服务识别' });
        }
      })
    }
    .width('100%')
    .padding(16)
  }
}
```

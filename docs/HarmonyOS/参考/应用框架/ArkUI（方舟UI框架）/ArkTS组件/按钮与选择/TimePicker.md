---
title: "TimePicker"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-timepicker"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "ArkTS组件"
  - "按钮与选择"
  - "TimePicker"
captured_at: "2026-04-17T01:47:56.895Z"
---

# TimePicker

滑动选择时间的组件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/DgC9RMHRSBK60RkQvoPw-w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=EB87C84A88B06523D6B5813C4BE2F356E8E416C35A32CF9EF4B09F67143FFD8B)

-   该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
    
-   该组件不建议开发者在动效过程中修改属性数据。
    
-   最大显示行数在横、竖屏模式下存在差异。竖屏时默认为5行，横屏时依赖系统配置，未配置时默认显示为3行。可通过如下参数查看具体配置值$r('sys.float.ohos\_id\_picker\_show\_count\_landscape')。
    

#### 子组件

无

#### 接口

TimePicker(options?: TimePickerOptions)

创建滑动选择器，默认使用24小时的时间区间。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [TimePickerOptions](#timepickeroptions对象说明) | 否 | 配置时间选择组件的参数。 |

#### TimePickerOptions对象说明

时间选择器组件的参数说明。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| selected | Date | 否 | 是 | 
设置选中项的时间。

默认值：当前系统时间

从API version 10开始，该参数支持[$$](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-two-way-sync)双向绑定变量。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| format11+ | [TimePickerFormat](#timepickerformat11枚举说明) | 否 | 是 | 

指定需要显示的TimePicker的格式。

默认值：TimePickerFormat.HOUR\_MINUTE

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| start18+ | Date | 否 | 是 | 

指定时间选择组件的起始时间。

默认值：Date(0, 0, 0, 0, 0, 0)

**说明：**

1\. 仅设置的小时和分钟生效。

2\. 设置了start且为非默认值的场景下，loop不生效。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

 |
| end18+ | Date | 否 | 是 | 

指定时间选择组件的结束时间。

默认值：Date(0, 0, 0, 23, 59, 59)

**说明：**

1\. 仅设置的小时和分钟生效。

2\. 设置了end且为非默认值的场景下，loop不生效。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

 |

在TimePicker组件滑动过程中修改TimePickerOptions中的属性，会导致这些属性无法生效。

Date对象用于处理日期和时间，使用方式如下。

**方式1：** new Date()

获取系统当前日期和时间。

**方式2：** new Date(value: number | string)

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| value | number | string | 是 | 
设置日期格式。

number：毫秒，自1970年1月1日00:00:00开始的毫秒数。

string：时间格式的字符串，如‘2025-02-20 08:00:00’或‘2025-02-20T08:00:00’。

 |

**方式3：** new Date(year: number, monthIndex: number, date?: number, hours?: number, minutes?: number, seconds?: number, ms?: number)

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| year | number | 是 | 设置年份，例如2025。 |
| monthIndex | number | 是 | 设置月份索引，例如2，代表3月份。 |
| date | number | 否 | 设置日期，例如10（如果设置hours，则date不能省略）。 |
| hours | number | 否 | 设置小时，例如15（如果设置minutes，则hours不能省略）。 |
| minutes | number | 否 | 设置分钟，例如20（如果设置seconds，则minutes不能省略）。 |
| seconds | number | 否 | 设置秒，例如20（如果设置ms，则seconds不能省略）。 |
| ms | number | 否 | 设置毫秒，例如10。 |

**起始时间和结束时间的异常情形说明：**

| 异常情形 | 对应结果 |
| :-- | :-- |
| 起始时间晚于结束时间。 | 起始时间、结束时间都为默认值。 |
| 选中时间早于起始时间。 | 选中时间为起始时间。 |
| 选中时间晚于结束时间。 | 选中时间为结束时间。 |
| 起始时间晚于当前系统时间，选中时间未设置。 | 选中时间为起始时间。 |
| 结束时间早于当前系统时间，选中时间未设置。 | 选中时间为结束时间。 |
| 时间格式不符合规范，如'01:61:61'。 | 取默认值。 |

#### TimePickerFormat11+枚举说明

时间选择器的数据格式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| HOUR\_MINUTE | 0 | 按照小时和分钟进行显示。 |
| HOUR\_MINUTE\_SECOND | 1 | 按照小时、分钟和秒进行显示。 |

#### 属性

除支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)外，还支持以下属性：

#### \[h2\]useMilitaryTime

useMilitaryTime(value: boolean)

设置时间是否以24小时制展示，未通过该接口设置时，默认跟随系统设置展示。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| value | boolean | 是 | 
时间是否以24小时制展示。

\- true：时间以24小时制展示。

\- false：时间以12小时制展示。

 |

#### \[h2\]useMilitaryTime18+

useMilitaryTime(isMilitaryTime: Optional<boolean>)

设置展示时间是否为24小时制，未通过该接口设置时，默认跟随系统设置展示。与[useMilitaryTime](#usemilitarytime)相比，isMilitaryTime参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| isMilitaryTime | [Optional](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-custom-property#optionalt)<boolean> | 是 | 
展示时间是否为24小时制。

\- true：展示时间为24小时制。

\- false：展示时间为12小时制。

当isMilitaryTime的值为undefined时，跟随系统设置。

 |

#### \[h2\]disappearTextStyle10+

disappearTextStyle(value: PickerTextStyle)

设置边缘项（以选中项为基准向上或向下的第二项）的文本颜色、字号、字体粗细。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| value | [PickerTextStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-picker-common#pickertextstyle对象说明) | 是 | 
边缘项的文本颜色、字号和字体粗细。

默认值：

{

color: '#ff182431',

font: {

size: '14fp',

weight: FontWeight.Regular

}

}

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/vFNsghQaTc2k8NTZldYJOg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=797BB472895C47F3E2B5754355B00CD2D4E11E0236C15E99916F59B23F2B0411)

若选中项向上或向下的可视项数低于两项则无对应边缘项。

#### \[h2\]disappearTextStyle18+

disappearTextStyle(style: Optional<PickerTextStyle>)

设置边缘项（以选中项为基准向上或向下的第二项）的文本颜色、字号、字体粗细。与[disappearTextStyle10+](#disappeartextstyle10)相比，style参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| style | [Optional](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-custom-property#optionalt)<[PickerTextStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-picker-common#pickertextstyle对象说明)\> | 是 | 
边缘项的文本颜色、字号、字体粗细。

默认值：

{

color: '#ff182431',

font: {

size: '14fp',

weight: FontWeight.Regular

}

}

当style的值为undefined时，使用默认值。

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/0CHQalORSdqrwIU3UuoPbQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=01B724B1603BC786084D11914CA2A3914C5F73046C9446990436693F0912DD41)

若选中项向上或向下的可视项数低于两项则无对应边缘项。

#### \[h2\]textStyle10+

textStyle(value: PickerTextStyle)

设置待选项（以选中项为基准向上或向下的第一项）的文本颜色、字号、字体粗细。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| value | [PickerTextStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-picker-common#pickertextstyle对象说明) | 是 | 
待选项的文本颜色、字号、字体粗细。

默认值：

{

color: '#ff182431',

font: {

size: '16fp',

weight: FontWeight.Regular

}

}

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/MNGuag_4TL-acTHwqPbydg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=DD0576BA9941A6BA07A18CA0A8DB2BDD13592882C29C0DB3867105A03C8F20A2)

若选中项向上或向下可视项数低于一项则无对应待选项。

#### \[h2\]textStyle18+

textStyle(style: Optional<PickerTextStyle>)

设置待选项（以选中项为基准向上或向下的第一项）的文本颜色、字号、字体粗细。与[textStyle10+](#textstyle10)相比，style参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| style | [Optional](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-custom-property#optionalt)<[PickerTextStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-picker-common#pickertextstyle对象说明)\> | 是 | 
待选项的文本颜色、字号、字体粗细。

默认值：

{

color: '#ff182431',

font: {

size: '16fp',

weight: FontWeight.Regular

}

}

当style的值为undefined时，使用默认值。

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/Tj0OweoNTwykYAOYXMwlDA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=B3F7C2B23CBD24FA2901DDBA4C05BFF48D5CB2FFD69ED6D9102629F85A08C0A4)

若选中项向上或向下可视项数低于一项则无对应待选项。

#### \[h2\]selectedTextStyle10+

selectedTextStyle(value: PickerTextStyle)

设置选中项的文本颜色、字号和字体粗细。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该属性在Wearable设备上使用无效果，在其他设备中可正常生效。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| value | [PickerTextStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-picker-common#pickertextstyle对象说明) | 是 | 
选中项的文本颜色、字号、字体粗细。

默认值：

{

color: '#ff007dff',

font: {

size: '20fp',

weight: FontWeight.Medium

}

}

 |

#### \[h2\]selectedTextStyle18+

selectedTextStyle(style: Optional<PickerTextStyle>)

设置选中项的文本颜色、字号及字体粗细。与[selectedTextStyle10+](#selectedtextstyle10)相比，style参数新增了对undefined类型的支持

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该属性在Wearable设备上使用无效果，在其他设备中可正常生效。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| style | [Optional](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-custom-property#optionalt)<[PickerTextStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-picker-common#pickertextstyle对象说明)\> | 是 | 
选中项的文本颜色、字号、字体粗细。

默认值：

{

color: '#ff007dff',

font: {

size: '20fp',

weight: FontWeight.Medium

}

}

当style的值为undefined时，使用默认值。

 |

#### \[h2\]loop11+

loop(value: boolean)

设置是否启用循环模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| value | boolean | 是 | 
是否启用循环模式。

\- true：启用循环模式。

\- false：不启用循环模式。

默认值：true

 |

#### \[h2\]loop18+

loop(isLoop: Optional<boolean>)

设置是否启用循环模式。与[loop11+](#loop11)相比，isLoop参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| isLoop | [Optional](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-custom-property#optionalt)<boolean> | 是 | 
是否启用循环模式。

\- true：启用循环模式。

\- false：不启用循环模式。

默认值：true

当isLoop的值为undefined时，使用默认值。

 |

#### \[h2\]dateTimeOptions12+

dateTimeOptions(value: DateTimeOptions)

设置时分秒是否显示前导0。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| value | [DateTimeOptions](#datetimeoptions12类型说明) | 是 | 
设置时分秒是否显示前导0。

默认值：

hour: 24小时制默认为"2-digit"，设置hour是否按照2位数字显示，如果实际数值小于10，则会补充前导0并显示，即为"0X"；12小时制默认为"numeric"，即没有前导0。

minute: 默认为"2-digit"，设置minute是否按照2位数字显示，如果实际数值小于10，则会补充前导0并显示，即为"0X"。

second: 默认为"2-digit"，设置second是否按照2位数字显示，如果实际数值小于10，则会补充前导0并显示，即为"0X"。

当hour、minute、second的值设置为undefined时，显示效果与其默认值规则一致。

 |

#### \[h2\]dateTimeOptions18+

dateTimeOptions(timeFormat: Optional<DateTimeOptions>)

设置时分秒是否显示前导0。与[dateTimeOptions12+](#datetimeoptions12)相比，timeFormat参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| timeFormat | [Optional](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-custom-property#optionalt)<[DateTimeOptions](#datetimeoptions12类型说明)\> | 是 | 
设置时分秒是否显示前导0，目前只支持设置hour、minute和second参数。

默认值：

hour: 24小时制默认为"2-digit"，设置hour是否按照2位数字显示，如果实际数值小于10，则会补充前导0并显示，即为"0X"；12小时制默认为"numeric"，即没有前导0。

minute: 默认为"2-digit"，设置minute是否按照2位数字显示，如果实际数值小于10，则会补充前导0并显示，即为"0X"。

second: 默认为"2-digit"，设置second是否按照2位数字显示，如果实际数值小于10，则会补充前导0并显示，即为"0X"。

当hour、minute、second的值设置为undefined时，显示效果与其默认值规则一致。

 |

#### \[h2\]enableHapticFeedback12+

enableHapticFeedback(enable: boolean)

设置是否支持触控反馈。

开启触控反馈时，需要在工程的src/main/module.json5文件的"module"内配置requestPermissions字段开启振动权限，配置如下：

```json
"requestPermissions": [
   {
      "name": "ohos.permission.VIBRATE",
   }
]
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/8HUQFwXvRUmRVjKjn5hu6A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=9887FA683FD8ED3420E2A9CF299EC701C133A147C7EB338AED2EAB0E7F89BC5F)

从API version 18开始，该接口支持在[attributeModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| enable | boolean | 是 | 
设置是否开启触控反馈。

\- true：开启触控反馈。

\- false：不开启触控反馈。

默认值：true

设置为true后，其生效情况取决于系统的硬件是否支持。

 |

#### \[h2\]enableHapticFeedback18+

enableHapticFeedback(enable: Optional<boolean>)

设置是否支持触控反馈。与[enableHapticFeedback12+](#enablehapticfeedback12)相比，enable参数新增了对undefined类型的支持。

开启触控反馈时，需要在工程的src/main/module.json5文件的"module"内配置requestPermissions字段开启振动权限，配置如下：

```json
"requestPermissions": [
  {
    "name": "ohos.permission.VIBRATE",
  }
]
```

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| enable | [Optional](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-custom-property#optionalt)<boolean> | 是 | 
设置是否开启触控反馈。

\- true：开启触控反馈。

\- false：不开启触控反馈。

默认值：true

当enable的值为undefined时，使用默认值。

设置为true后，其生效情况取决于系统的硬件是否支持。

 |

#### \[h2\]enableCascade18+

enableCascade(enabled: boolean)

设置上午和下午的标识是否根据小时数自动切换，仅在[useMilitaryTime](#usemilitarytime)设置为false时生效。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| enabled | boolean | 是 | 
上午和下午的标识是否根据小时数自动切换，仅在useMilitaryTime设置为false时生效。

\- true：自动切换。

\- false：不自动切换。

默认值：false

当enabled设置为true时，仅在loop参数同时为true时生效。

 |

#### \[h2\]digitalCrownSensitivity18+

digitalCrownSensitivity(sensitivity: Optional<CrownSensitivity>)

设置表冠灵敏度。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| sensitivity | [Optional](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-custom-property#optionalt)<[CrownSensitivity](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#crownsensitivity18)\> | 是 | 
表冠响应灵敏度。

默认值：CrownSensitivity.MEDIUM，表示响应速度适中。

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/eaGu6HVOT52WvrVfoQBBxA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=E85ED16C64BC2B3EBFE76224E96F2A8327F0A3140B76712CC77FBAA13B3D5B3A)

用于圆形屏幕的穿戴设备。组件响应[表冠事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-crown)，需要先获取焦点。

#### 事件

除支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-events)外，还支持以下事件：

#### \[h2\]onChange

onChange(callback: (value: TimePickerResult ) => void)

滑动TimePicker后，时间选项归位至选中项位置时，触发该回调。不能通过双向绑定的状态变量触发。

回调会在滑动动画结束后触发，如果需要快速获取索引值变化，建议使用[onEnterSelectedArea](#onenterselectedarea18)接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| value | [TimePickerResult](#timepickerresult对象说明) | 是 | 24小时制时间。 |

#### \[h2\]onChange18+

onChange(callback: Optional<OnTimePickerChangeCallback>)

滑动TimePicker后，时间选项归位至选中项位置时，触发该回调。不能通过双向绑定的状态变量触发。与[onChange](#onchange)相比，callback参数新增了对undefined类型的支持。

回调会在滑动动画结束后触发，如果需要快速获取索引值变化，建议使用[onEnterSelectedArea](#onenterselectedarea18)接口。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | [Optional](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-custom-property#optionalt)<[OnTimePickerChangeCallback](#ontimepickerchangecallback18)\> | 是 | 
选择时间时触发该回调。

当callback的值为undefined时，不使用回调函数。

 |

#### \[h2\]onEnterSelectedArea18+

onEnterSelectedArea(callback: Callback<TimePickerResult>)

滑动TimePicker过程中，选项进入分割线区域内，触发该回调。

与[onChange](#onchange)事件的差别在于，该事件的触发时机早于[onChange](#onchange)事件，当当前滑动列滑动距离超过选中项高度的一半时，选项此时已经进入分割线区域内，会触发该事件。当[enableCascade](#enablecascade18)设置为true时，由于上午/下午列与小时列存在联动关系，不建议使用该回调。该回调标识的是滑动过程中选项进入分割线区域内的节点，而联动变化的选项并不涉及滑动，因此，回调的返回值中，仅当前滑动列的值会正常变化，其余未滑动列的值保持不变。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/vFRaUrfQRu-cknyIIQ438Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=FE699BFBF45B83535E3A9768790766DF2B683E16E3792462C38C3986AAB8C19C)

该接口不支持在[attributeModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#attributemodifier)中调用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | Callback<[TimePickerResult](#timepickerresult对象说明)\> | 是 | 滑动TimePicker过程中，选项进入分割线区域时触发的回调。 |

#### DateTimeOptions12+类型说明

type DateTimeOptions = DateTimeOptions

时间、日期格式化时可设置的配置项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| :-- | :-- |
| [DateTimeOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-intl#datetimeoptionsdeprecated) | 创建时间、日期格式化对象时可设置的配置项。 |

#### OnTimePickerChangeCallback18+

type OnTimePickerChangeCallback = (result: TimePickerResult) => void

选择时间时触发该事件。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| result | [TimePickerResult](#timepickerresult对象说明) | 是 | 24小时制时间。 |

#### TimePickerResult对象说明

返回24小时制时间。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| hour | number | 否 | 否 | 
选中时间的时。

取值范围：\[0-23\]

 |
| minute | number | 否 | 否 | 

选中时间的分。

取值范围：\[0-59\]

 |
| second11+ | number | 否 | 否 | 

选中时间的秒。

取值范围：\[0-59\]

 |

#### 示例

#### \[h2\]示例1（设置文本样式）

该示例通过配置[disappearTextStyle](#disappeartextstyle10)、[textStyle](#textstyle10)和[selectedTextStyle](#selectedtextstyle10)实现文本选择器中的文本样式。

```ts
// xxx.ets
@Entry
@Component
struct TimePickerExample {
  private selectedTime: Date = new Date('2022-07-22T08:00:00');

  build() {
    TimePicker({
      selected: this.selectedTime
    })
      .disappearTextStyle({ color: '#004aaf', font: { size: 24, weight: FontWeight.Lighter } })
      .textStyle({ color: Color.Black, font: { size: 26, weight: FontWeight.Normal } })
      .selectedTextStyle({ color: Color.Blue, font: { size: 30, weight: FontWeight.Bolder } })
      .onChange((value: TimePickerResult) => {
        if (value.hour >= 0) {
          this.selectedTime.setHours(value.hour, value.minute);
          console.info('select current date is: ' + JSON.stringify(value));
        }
      })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/3cGwmbA2Qlmr217m6yT-2g/zh-cn_image_0000002568900369.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=919942FAD5F414285D38E83A2D3A023F8BF1C4A2CB82C784B635C82FADDDBB1C)

#### \[h2\]示例2（切换小时制）

该示例通过配置useMilitaryTime实现12小时制、24小时制的切换。

```ts
// xxx.ets
@Entry
@Component
struct TimePickerExample {
  @State isMilitaryTime: boolean = false;
  private selectedTime: Date = new Date('2022-07-22T08:00:00');

  build() {
    Column() {
      Button('切换12小时制/24小时制')
        .margin(30)
        .onClick(() => {
          this.isMilitaryTime = !this.isMilitaryTime;
        })

      TimePicker({
        selected: this.selectedTime
      })
        .useMilitaryTime(this.isMilitaryTime)
        .onChange((value: TimePickerResult) => {
          if (value.hour >= 0) {
            this.selectedTime.setHours(value.hour, value.minute);
            console.info('select current time is: ' + JSON.stringify(value));
          }
        })
        .onEnterSelectedArea((value: TimePickerResult) => {
            console.info('item enter selected area, time is: ' + JSON.stringify(value));
        })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/FzQ9Xu9USdC1r3JXSae0Ow/zh-cn_image_0000002538020666.gif?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=C163EBD4072C4D73BD912C9401D81BADF770ABE3507CD05B303151A2F91D8AE3)

#### \[h2\]示例3（设置时间格式）

该示例使用format和dateTimeOptions设置TimePicker时间格式。

```ts
// xxx.ets
@Entry
@Component
struct TimePickerExample {
  private selectedTime: Date = new Date('2022-07-22T08:00:00');

  build() {
    Column() {
      TimePicker({
        selected: this.selectedTime,
        format: TimePickerFormat.HOUR_MINUTE_SECOND
      })
        .dateTimeOptions({ hour: "numeric", minute: "2-digit", second: "2-digit" })
        .onChange((value: TimePickerResult) => {
          if (value.hour >= 0) {
            this.selectedTime.setHours(value.hour, value.minute);
            console.info('select current date is: ' + JSON.stringify(value));
          }
        })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/7ZCpwewdRLaiJkyF9IZsJg/zh-cn_image_0000002538180592.gif?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=399B3782D38C9AA9AB7B273B662522EC18EC4DACB46947A1C089917853E64D2F)

#### \[h2\]示例4（设置循环滚动）

该示例通过配置[loop](#loop11)设置TimePicker是否循环滚动。

```ts
// xxx.ets
@Entry
@Component
struct TimePickerExample {
  @State isLoop: boolean = true;
  @State selectedTime: Date = new Date('2022-07-22T12:00:00');

  build() {
    Column() {
      TimePicker({
        selected: this.selectedTime
      })
        .loop(this.isLoop)
        .onChange((value: TimePickerResult) => {
          if (value.hour >= 0) {
            this.selectedTime.setHours(value.hour, value.minute);
            console.info('select current date is: ' + JSON.stringify(value));
          }
        })

      Row() {
        Text('循环滚动').fontSize(20)

        Toggle({ type: ToggleType.Switch, isOn: true })
          .onChange((isOn: boolean) => {
            this.isLoop = isOn;
          })
      }.position({ x: '60%', y: '40%' })

    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/hV4F7k8OTB20XbtPNWbPqA/zh-cn_image_0000002569020379.gif?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=F407CC14147BF9FDE929BEB90A8FF5A74F4CA69E14438BABFBAF196622A9B544)

#### \[h2\]示例5（设置时间选择组件的起始时间）

该示例设置TimePicker的起始时间。

```ts
// xxx.ets
@Entry
@Component
struct TimePickerExample {
  private selectedTime: Date = new Date('2022-07-22T08:50:00');

  build() {
    Column() {
      TimePicker({
        selected: this.selectedTime,
        format: TimePickerFormat.HOUR_MINUTE_SECOND,
        start: new Date('2022-07-22T08:30:00')
      })
        .dateTimeOptions({ hour: "numeric", minute: "2-digit", second: "2-digit" })
        .onChange((value: TimePickerResult) => {
          if (value.hour >= 0) {
            this.selectedTime.setHours(value.hour, value.minute);
            console.info('select current date is: ' + JSON.stringify(value));
          }
        })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/QogTmmpJQ8mCiRtu6GycIw/zh-cn_image_0000002568900371.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=FB04F4CDB6A44C84E8B44B325B1E912761A0C1F876F6E8D9E6354EA7F7A8A333)

#### \[h2\]示例6（设置时间选择组件的结束时间）

该示例设置TimePicker的结束时间。

```ts
// xxx.ets
@Entry
@Component
struct TimePickerExample {
  private selectedTime: Date = new Date('2022-07-22T08:50:00');

  build() {
    Column() {
      TimePicker({
        selected: this.selectedTime,
        format: TimePickerFormat.HOUR_MINUTE_SECOND,
        end: new Date('2022-07-22T15:20:00'),
      })
        .dateTimeOptions({ hour: "numeric", minute: "2-digit", second: "2-digit" })
        .onChange((value: TimePickerResult) => {
          if (value.hour >= 0) {
            this.selectedTime.setHours(value.hour, value.minute);
            console.info('select current date is: ' + JSON.stringify(value));
          }
        })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/uRRoACZMQMe7bkRuvvAxnA/zh-cn_image_0000002538020668.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=DAC2BFE60B2B8F278CD01DFBC74D2FD961FE9061BE0D30CF07916B9312AC5532)

#### \[h2\]示例7（设置上午下午跟随时间联动）

该示例通过配置[enableCascade](#enablecascade18)、[loop](#loop11)实现12小时制时上午下午跟随时间联动。

从API version 18开始，新增enableCascade接口。

```ts
// xxx.ets
@Entry
@Component
struct TimePickerExample {
  private selectedTime: Date = new Date('2022-07-22T08:00:00');

  build() {
    Column() {
      TimePicker({
        selected: this.selectedTime,
      })
        .enableCascade(true)
        .loop(true)
        .onChange((value: TimePickerResult) => {
          if (value.hour >= 0) {
            this.selectedTime.setHours(value.hour, value.minute);
            console.info('select current date is: ' + JSON.stringify(value));
          }
        })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/UUvnU_aOSh2FNK0ghY3IbA/zh-cn_image_0000002538180594.gif?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=F2512DFC6148D04FF192537EC13B1E43653CBE3A368E84C2FA87546824EE6BA2)

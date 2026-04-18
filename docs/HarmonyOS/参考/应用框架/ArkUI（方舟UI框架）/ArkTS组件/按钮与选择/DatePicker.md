---
title: "DatePicker"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-datepicker"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "ArkTS组件"
  - "按钮与选择"
  - "DatePicker"
captured_at: "2026-04-17T01:47:56.843Z"
---

# DatePicker

滑动选择日期的组件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/hkZQo-maRIy5cee1UUbRfQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=42F71AFF79DF411B069EE7CE4B785F5A913FEDBEC1EBF6C100AE07CE8D6E9218)

-   该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
    
-   该组件不建议开发者在动效过程中修改属性数据。
    
-   最大显示行数在横、竖屏模式下存在差异。竖屏时默认为5行，横屏时依赖系统配置，未配置时默认显示为3行。可通过如下参数查看具体配置值$r('sys.float.ohos\_id\_picker\_show\_count\_landscape')。
    

#### 子组件

无

#### 接口

DatePicker(options?: DatePickerOptions)

根据指定日期范围创建日期选择器。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [DatePickerOptions](#datepickeroptions对象说明) | 否 | 配置日期选择器组件的参数。 |

#### DatePickerOptions对象说明

日期选择器组件的参数说明。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| start | Date | 否 | 是 | 
指定选择器的起始日期。

默认值：Date('1970-1-1')

取值范围：\[Date('1900-01-31'), Date('2100-12-31')\]

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| end | Date | 否 | 是 | 

指定选择器的结束日期。

默认值：Date('2100-12-31')

取值范围：\[Date('1900-01-31'), Date('2100-12-31')\]

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| selected | Date | 否 | 是 | 

设置选中项的日期。

默认值：当前系统日期。

取值范围：\[Date('1900-01-31'), Date('2100-12-31')\]

从API version 10开始，该参数支持[$$](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-two-way-sync)双向绑定变量。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| mode18+ | [DatePickerMode](#datepickermode18枚举说明) | 否 | 是 | 

设置日期展示模式。

默认值：DatePickerMode.DATE，显示年、月、日三列。

在[DatePickerDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-datepicker-dialog)中，当[DatePickerDialogOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-datepicker-dialog#datepickerdialogoptions对象说明)的showTime设置为true时，此参数不生效，默认显示年、月、日三列。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/QqJALfM7Si-WpNrdoPgCFQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=90B1009D6DA6E4A8E5E11A04D7A8D96D61B6A92B5E81E104835181BCE0749788)

-   Date的使用请参考[TimePickerOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-timepicker#timepickeroptions对象说明)。
    
-   在DatePicker组件滑动过程中修改DatePickerOptions中的属性，会导致这些属性无法生效。
    

**起始日期、结束日期和选中日期的异常情形说明：**

| 异常情形 | 对应结果 |
| :-- | :-- |
| 起始日期晚于结束日期，选中日期未设置。 | 起始日期、结束日期和选中日期都为默认值。 |
| 起始日期晚于结束日期，选中日期早于起始日期默认值。 | 起始日期、结束日期都为默认值，选中日期为起始日期默认值。 |
| 起始日期晚于结束日期，选中日期晚于结束日期默认值。 | 起始日期、结束日期都为默认值，选中日期为结束日期默认值。 |
| 起始日期晚于结束日期，选中日期在起始日期与结束日期默认值范围内。 | 起始日期、结束日期都为默认值，选中日期为设置的值。 |
| 选中日期早于起始日期。 | 选中日期为起始日期。 |
| 选中日期晚于结束日期。 | 选中日期为结束日期。 |
| 起始日期晚于当前系统日期，选中日期未设置。 | 选中日期为起始日期。 |
| 结束日期早于当前系统日期，选中日期未设置。 | 选中日期为结束日期。 |
| 日期格式不符合规范，如‘1999-13-32’。 | 取默认值。 |
| 起始日期或结束日期早于系统有效范围。 | 起始日期或结束日期取起始日期默认值。 |
| 起始日期或结束日期晚于系统有效范围。 | 起始日期或结束日期取结束日期默认值。 |
| 起始日期与结束日期同时早于系统有效范围。 | 起始日期与结束日期取系统有效范围最早日期。 |
| 起始日期与结束日期同时晚于系统有效范围。 | 起始日期与结束日期取系统有效范围最晚日期。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/bba6dPWlTnSoBX3i6xsJ1g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=188890086F138A90A5095CEB5A61FC61FF4B1A3AC8D62F57B1A43626D7AA4896)

先处理起始日期与结束日期的异常情形，再处理选中日期的异常情形。

#### DatePickerMode18+枚举说明

设置日期展示模式。

**元服务API：** 从API version 18开始，该类型支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| DATE | 0 | 显示年、月、日三列。 |
| YEAR\_AND\_MONTH | 1 | 显示年、月二列。 |
| MONTH\_AND\_DAY | 2 | 
显示月、日二列。

在此模式下，年份始终保持不变。

 |

#### 属性

除支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)外，还支持以下属性：

#### \[h2\]lunar

lunar(value: boolean)

设置日期是否显示为农历。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/-5gSwuu3Qe26n3usNyVPww/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=A32313A8E308EC5F565641FED2A4AC47711068BE21137FB6FE3A6904F4147135)

仅在简体中文和繁体中文语言环境下生效，其他语言环境下设置该属性无效果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| value | boolean | 是 | 
日期是否显示为农历。

\- true：显示为农历。

\- false：不显示为农历。

默认值：false

 |

#### \[h2\]lunar18+

lunar(isLunar: Optional<boolean>)

设置弹窗的日期是否显示为农历。与[lunar](#lunar)相比，isLunar参数新增了对undefined类型的支持。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/MtBpc0n_Th-P9PnGRW0hcA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=D993B304B3F2263F019CC02D26131977953E34C6886CDEF86A39C637E51AC4CA)

仅在简体中文和繁体中文语言环境下生效，其他语言环境下设置该属性无效果。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| isLunar | [Optional](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-custom-property#optionalt)<boolean> | 是 | 
日期是否显示为农历。

\- true：显示为农历。

\- false：不显示为农历。

默认值：false

当isLunar的值为undefined时，使用默认值。

 |

#### \[h2\]disappearTextStyle10+

disappearTextStyle(value: PickerTextStyle)

设置边缘项（以选中项为基准向上或向下的第二项）的文本样式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| value | [PickerTextStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-picker-common#pickertextstyle对象说明) | 是 | 
边缘项的文本颜色、字号、字体粗细。

默认值：

{

color: '#ff182431',

font: {

size: '14fp',

weight: FontWeight.Regular

}

}

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/dst6U5LRS7KevIwmuXoroQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=C98B53B4E6E49914EB81EAFE28AAE78743EFF93AACC17518D8B3598641E0CA24)

若选中项向上或向下的可视项数低于两项则无对应边缘项。

#### \[h2\]disappearTextStyle18+

disappearTextStyle(style: Optional<PickerTextStyle>)

设置边缘项（以选中项为基准向上或向下的第二项）的文本样式。与[disappearTextStyle10+](#disappeartextstyle10)相比，style参数新增了对undefined类型的支持。

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/TftaOy4RRkK6gdAIl5_j_A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=5BA302FA9B944158EDD38468445C356D99175DF747501B9194F7B013DA7CC50C)

若选中项向上或向下的可视项数低于两项则无对应边缘项。

#### \[h2\]textStyle10+

textStyle(value: PickerTextStyle)

设置待选项（以选中项为基准向上或向下的第一项）的文本样式。

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/oSnvqhyzSbmpUZpInvrqqA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=FFA8A7B6FEE019837B386486DB64DBF0C1920AABC6E577EFCB6AAD16EA4C701C)

若选中项向上或向下可视项数低于一项则无对应待选项。

#### \[h2\]textStyle18+

textStyle(style: Optional<PickerTextStyle>)

设置待选项（以选中项为基准向上或向下的第一项）的文本样式。与[textStyle10+](#textstyle10)相比，style参数新增了对undefined类型的支持。

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/nnWRsKJJRk-EM_W6sK0JXg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=DF582B92C8A8B26158A14FB1D83FE1EAFB4559DE3AC43EDDF4E235024EEDC766)

若选中项向上或向下可视项数低于一项则无对应待选项。

#### \[h2\]selectedTextStyle10+

selectedTextStyle(value: PickerTextStyle)

设置选中项的文本样式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

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

设置选中项的文本样式。与[selectedTextStyle10+](#selectedtextstyle10)相比，style参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

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

#### \[h2\]enableHapticFeedback18+

enableHapticFeedback(enable: Optional<boolean>)

设置是否开启触控反馈。

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

设置为true后，其生效情况取决于系统的硬件是否支持。

当enable的值为undefined时，使用默认值。

 |

开启触控反馈时，需要在工程的src/main/module.json5文件的"module"内配置requestPermissions字段开启振动权限，配置如下：

```json
"requestPermissions": [
   {
      "name": "ohos.permission.VIBRATE",
   }
]
```

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

默认值：CrownSensitivity.MEDIUM，响应速度适中。

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/m439tbHSQ-SaMCAL05S5Hw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=9D98BC66C2300139472677E86FCFC4A9AD49A3E3ACF3E35BC393981B787B9939)

用于穿戴设备圆形屏幕使用。组件响应[表冠事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-crown)，需要先获取焦点。

#### \[h2\]canLoop20+

canLoop(isLoop: Optional<boolean>)

设置是否可循环滚动。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| isLoop | [Optional](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-custom-property#optionalt)<boolean> | 是 | 
是否可循环滚动。

\- true：可循环滚动，年份随着月份的循环滚动进行联动加减，月份随着日的循环滚动进行联动加减。

\- false：不可循环滚动，年、月、日到达本列的顶部或底部时，无法再进行滚动，年、月、日之间也无法再联动加减。

默认值：true

当isLoop的值为undefined时，使用默认值。

 |

#### 事件

除支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-events)外，还支持以下事件：

#### \[h2\]onChange(deprecated)

onChange(callback: (value: DatePickerResult) => void)

滑动DatePicker文本内容后，选项完全归位至选中项位置时，触发该回调。不能通过双向绑定的状态变量触发。

从API version 8开始支持，从API version 10开始废弃，建议使用[onDateChange](#ondatechange10)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | (value: [DatePickerResult](#datepickerresult对象说明)) => void | 是 | 返回选中的时间。 |

#### \[h2\]onDateChange10+

onDateChange(callback: Callback<Date>)

滑动DatePicker文本内容后，选项完全归位至选中项位置时，触发该回调。不能通过双向绑定的状态变量触发。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | [Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#callback12)<Date> | 是 | 返回选中的时间，年、月、日为选中的日期，时、分取决于当前系统时间的时、分，秒恒为00。 |

#### \[h2\]onDateChange18+

onDateChange(callback: Optional<Callback<Date>>)

滑动DatePicker文本内容后，选项完全归位至选中项位置时，触发该回调。不能通过双向绑定的状态变量触发。与[onDateChange10+](#ondatechange10)相比，callback参数新增了对undefined类型的支持。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/0fwiZOgKTNq2wxAmFHh9DQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=07F82ADEC786C25CD7A72BF0D5CF7CA65747560FBD9AEBCBD887698CC4FDE719)

从API version 20开始，该接口支持在[attributeModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#attributemodifier)中调用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | [Optional](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-custom-property#optionalt)<[Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#callback12)<Date>> | 是 | 
返回选中的时间，年、月、日为选中的日期，时、分取决于当前系统时间的时、分，秒恒为00。

当callback的值为undefined时，不使用回调函数。

 |

#### DatePickerResult对象说明

日期选择器返回的时间格式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| year | number | 否 | 是 | 
选中日期的年。

取值范围：与设置的start、end有关，如果没有设置start、end，取值范围为\[1970, 2100\]。

 |
| month | number | 否 | 是 | 

选中日期的月的索引值，索引从0开始，0表示1月，11表示12月。

取值范围：与设置的start、end有关，如果没有设置start、end，取值范围为\[0, 11\]。

 |
| day | number | 否 | 是 | 

选中日期的日。

取值范围：与设置的start、end有关，如果没有设置start、end，取值范围为\[1, 31\]。

 |

#### 示例

#### \[h2\]示例1（切换公历农历）

该示例实现了日期选择器组件，点击按钮可以切换公历农历。

```ts
// xxx.ets
@Entry
@Component
struct DatePickerExample {
  @State isLunar: boolean = false;
  private selectedDate: Date = new Date('2021-08-08');

  build() {
    Column() {
      Button('切换公历农历')
        .margin({ top: 30, bottom: 30 })
        .onClick(() => {
          this.isLunar = !this.isLunar;
        })
      DatePicker({
        start: new Date('1970-1-1'),
        end: new Date('2100-1-1'),
        selected: this.selectedDate
      })
        .lunar(this.isLunar)
        .onDateChange((value: Date) => {
          this.selectedDate = value;
          console.info('select current date is: ' + value.toString());
        })

    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/ewtfbdIoRwCGAXxSkMik-A/zh-cn_image_0000002538020658.gif?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=DFCAC9A36DDFE2A537248942D3ECAB34FC1199AB202C50D39B8F38E8A18115AB)

#### \[h2\]示例2（设置文本样式）

该示例通过配置[disappearTextStyle](#disappeartextstyle10)、[textStyle](#textstyle10)、[selectedTextStyle](#selectedtextstyle10)设置文本样式。

```ts
// xxx.ets
@Entry
@Component
struct DatePickerExample {
  private selectedDate: Date = new Date('2021-08-08');

  build() {
    Column() {
      DatePicker({
        start: new Date('1970-1-1'),
        end: new Date('2100-1-1'),
        selected: this.selectedDate
      })
        .disappearTextStyle({ color: Color.Gray, font: { size: '16fp', weight: FontWeight.Bold } })
        .textStyle({ color: '#ff182431', font: { size: '18fp', weight: FontWeight.Normal } })
        .selectedTextStyle({ color: '#ff0000FF', font: { size: '26fp', weight: FontWeight.Regular, family: "HarmonyOS Sans", style: FontStyle.Normal } })
        .onDateChange((value: Date) => {
          this.selectedDate = value;
          console.info('select current date is: ' + value.toString());
        })

    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/Ksy_EtL9RDqUBIyiKcJfMw/zh-cn_image_0000002538180584.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=F5D22E7257FF354DAB929956071A77325A23C45B692FA505D7C021EFFC2FD1F0)

#### \[h2\]示例3（设置显示年、月和月、日列）

该示例通过配置mode参数实现显示年、月和月、日列。

从API version 18开始，新增了[DatePickerOptions](#datepickeroptions对象说明)的mode属性。

```ts
// xxx.ets
@Entry
@Component
struct DatePickerExample {
  @State isLunar: boolean = false;
  private selectedDate: Date = new Date('2025-01-15');
  @State datePickerModeList: (DatePickerMode)[] = [
    DatePickerMode.DATE,
    DatePickerMode.YEAR_AND_MONTH,
    DatePickerMode.MONTH_AND_DAY,
  ];
  @State datePickerModeIndex: number = 0;

  build() {
    Column() {
      Button('切换公历农历')
        .margin({ top: 30, bottom: 30 })
        .onClick(() => {
          this.isLunar = !this.isLunar;
        })
      DatePicker({
        start: new Date('1970-1-1'),
        end: new Date('2100-1-1'),
        selected: this.selectedDate,
        mode:this.datePickerModeList[this.datePickerModeIndex]
      })
        .lunar(this.isLunar)
        .onDateChange((value: Date) => {
          this.selectedDate = value;
          console.info('select current date is: ' + value.toString());
        })

      Button('mode :' + this.datePickerModeIndex).margin({ top: 20 })
        .onClick(() => {
          this.datePickerModeIndex++;
          if(this.datePickerModeIndex >= this.datePickerModeList.length){
            this.datePickerModeIndex = 0;
          }
        })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/5qwRyLJZSgOvX5pD_Ag48A/zh-cn_image_0000002569020371.gif?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=8156563C8C17285C0C2C0416F1085BA8F43D5DEBB6BDEA9F33993D7C414E24EC)

#### \[h2\]示例4（设置循环滚动）

从API version 20开始，可以通过配置[canLoop](#canloop20)参数设置DatePicker是否循环滚动。

```ts
// xxx.ets
@Entry
@Component
struct DatePickerExample {
  @State isLoop: boolean = true;
  selectedDate: Date = new Date("2010-1-1");

  build() {
    Column() {
      DatePicker({
        start: new Date("2000-1-1"),
        end: new Date("2100-12-31"),
        selected: this.selectedDate,
      })
        .canLoop(this.isLoop)
        .onDateChange((value: Date) => {
            console.info("DatePicker:onDateChange()" + value.toString());
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/Fu9-MjXCTbmVUin8N2D1ag/zh-cn_image_0000002568900363.gif?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=65BBDEF00668349E1FA4F8552F4C33F6E342476B3773B47ED55AC4D8DFCEE729)

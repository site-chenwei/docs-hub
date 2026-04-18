---
title: "时间滑动选择器弹窗 (TimePickerDialog)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-timepicker-dialog"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "ArkTS组件"
  - "弹窗"
  - "时间滑动选择器弹窗 (TimePickerDialog)"
captured_at: "2026-04-17T01:47:58.760Z"
---

# 时间滑动选择器弹窗 (TimePickerDialog)

以24小时的时间区间创建时间滑动选择器，展示在弹窗上。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/eBBqenxzQxu-ziYRaLZiFg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014801Z&HW-CC-Expire=86400&HW-CC-Sign=49AF6246A31AC96B3FBEECC162AE1A7ECD74E2019E14E4ECDF649E6D3F5F6273)

-   该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
    
-   本模块功能依赖UI的执行上下文，不可在[UI上下文不明确](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface#ui上下文不明确)的地方使用，参见[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)说明。
    
-   本模块不支持深浅色模式热更新，如果需要进行深浅色模式切换，请重新打开弹窗。
    
-   最大显示行数在横、竖屏模式下存在差异。竖屏时默认为5行，横屏时依赖系统配置，未配置时默认显示为3行。可通过如下参数查看具体配置值$r('sys.float.ohos\_id\_picker\_show\_count\_landscape')。
    

#### TimePickerDialog

#### \[h2\]show(deprecated)

static show(options?: TimePickerDialogOptions)

定义时间滑动选择器弹窗并弹出。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/Esl_90O5Tf-rc1x_BxvKpw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014801Z&HW-CC-Expire=86400&HW-CC-Sign=F8BF8BED3A6E543E944368579492F9D1C8C32A5F98D8E04DF3C5CBE49727B347)

从API version 8开始支持，从API version 18开始废弃，建议使用[showTimePickerDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#showtimepickerdialog)替代。showTimePickerDialog需先获取[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)实例后再进行调用。

从API version 10开始，可以通过使用[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[showTimePickerDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#showtimepickerdialog)来明确UI的执行上下文。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [TimePickerDialogOptions](#timepickerdialogoptions对象说明) | 否 | 配置时间选择器弹窗的参数。 |

#### TimePickerDialogOptions对象说明

时间选择器弹窗选项。

继承自[TimePickerOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-timepicker#timepickeroptions对象说明)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| useMilitaryTime | boolean | 否 | 是 | 
时间是否以24小时制展示。

\- true：时间以24小时制展示。

\- false：时间以12小时制展示。

默认值：false

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| disappearTextStyle10+ | [PickerTextStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-picker-common#pickertextstyle对象说明) | 否 | 是 | 

设置边缘项（以选中项为基准向上或向下的第二项）的文本颜色、字号、字体粗细。

默认值：

{

color: '#ff182431',

font: {

size: '14fp',

weight: FontWeight.Regular

}

}

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| textStyle10+ | [PickerTextStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-picker-common#pickertextstyle对象说明) | 否 | 是 | 

设置待选项（以选中项为基准向上或向下的第一项）的文本颜色、字号、字体粗细。

默认值：

{

color: '#ff182431',

font: {

size: '16fp',

weight: FontWeight.Regular

}

}

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| selectedTextStyle10+ | [PickerTextStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-picker-common#pickertextstyle对象说明) | 否 | 是 | 

设置选中项的文本颜色、字号、字体粗细。

默认值：

{

color: '#ff007dff',

font: {

size: '20fp',

weight: FontWeight.Medium

}

}

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| acceptButtonStyle12+ | [PickerDialogButtonStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-picker-common#pickerdialogbuttonstyle12对象说明) | 否 | 是 | 

设置确认按钮显示样式、样式和重要程度、角色、背景色、圆角、文本颜色、字号、字体粗细、字体样式、字体列表、按钮是否默认响应Enter键。

**说明：**

1.acceptButtonStyle与cancelButtonStyle中最多只能有一个primary字段配置为true，如果同时设置为true，则primary字段不生效，保持默认值false。

2.按钮高度默认40vp，在关怀模式-大字体场景下高度不变，即使按钮样式设置为圆角矩形[ROUNDED\_RECTANGLE](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-button#buttontype枚举说明)，呈现效果依然是胶囊型按钮[Capsule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-button#buttontype枚举说明)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| cancelButtonStyle12+ | [PickerDialogButtonStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-picker-common#pickerdialogbuttonstyle12对象说明) | 否 | 是 | 

设置取消按钮显示样式、样式和重要程度、角色、背景色、圆角、文本颜色、字号、字体粗细、字体样式、字体列表、按钮是否默认响应Enter键。

**说明：**

1.acceptButtonStyle与cancelButtonStyle中最多只能有一个primary字段配置为true，如果同时设置为true，则primary字段不生效，保持默认值false。

2.按钮高度默认40vp，在关怀模式-大字体场景下高度不变，即使按钮样式设置为圆角矩形[ROUNDED\_RECTANGLE](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-button#buttontype枚举说明)，呈现效果依然是胶囊型按钮[Capsule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-button#buttontype枚举说明)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| alignment10+ | [DialogAlignment](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-alert-dialog-box#dialogalignment枚举说明) | 否 | 是 | 

设置弹窗在垂直方向上的对齐方式。

默认值：DialogAlignment.Default

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| offset10+ | [Offset](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#offset) | 否 | 是 | 

设置弹窗相对alignment所在位置的偏移量。

默认值：{ dx: 0 , dy: 0 }

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| maskRect10+ | [Rectangle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-alert-dialog-box#rectangle8类型说明) | 否 | 是 | 

弹窗遮蔽层区域，在遮蔽层区域内的事件不透传，在遮蔽层区域外的事件透传。

默认值：{ x: 0, y: 0, width: '100%', height: '100%' }

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| onAccept | (value: [TimePickerResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-timepicker#timepickerresult对象说明)) => void | 否 | 是 | 

点击弹窗中的“确定”按钮时触发该回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| onCancel | () => void | 否 | 是 | 

点击弹窗中的“取消”按钮时触发该回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| onChange | (value: [TimePickerResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-timepicker#timepickerresult对象说明)) => void | 否 | 是 | 

滑动弹窗中的选择器后，选项归位至选中项位置时，触发该回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| backgroundColor11+ | [ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor) | 否 | 是 | 

弹窗背板颜色。

默认值：Color.Transparent

**说明：**

当设置了backgroundColor为非透明色时，backgroundBlurStyle需要设置为BlurStyle.NONE，否则显示的颜色将不符合预期效果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| backgroundBlurStyle11+ | [BlurStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-background#blurstyle9) | 否 | 是 | 

弹窗背板模糊材质。

默认值：BlurStyle.COMPONENT\_ULTRA\_THICK

**说明：**

设置为BlurStyle.NONE即可关闭背景虚化。当设置了backgroundBlurStyle为非NONE值时，则不要设置backgroundColor，否则显示的颜色将不符合预期效果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| backgroundBlurStyleOptions19+ | [BackgroundBlurStyleOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-background#backgroundblurstyleoptions10对象说明) | 否 | 是 | 

背景模糊效果。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

 |
| backgroundEffect19+ | [BackgroundEffectOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-background#backgroundeffectoptions11) | 否 | 是 | 

背景效果参数。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

 |
| onDidAppear12+ | () => void | 否 | 是 | 

弹窗弹出后的事件回调。

**说明：**

1.正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange)>>onWillDisappear>>onDidDisappear。

2.在onDidAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。

3.快速点击弹出，消失弹窗时，存在onWillDisappear在onDidAppear前生效。

4\. 当弹窗入场动效未完成时关闭弹窗，该回调不会触发。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| onDidDisappear12+ | () => void | 否 | 是 | 

弹窗消失后的事件回调。

**说明：**

1.正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange)>>onWillDisappear>>onDidDisappear。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| onWillAppear12+ | () => void | 否 | 是 | 

弹窗显示动效前的事件回调。

**说明：**

1.正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange)>>onWillDisappear>>onDidDisappear。

2.在onWillAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| onWillDisappear12+ | () => void | 否 | 是 | 

弹窗退出动效前的事件回调。

**说明：**

1.正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange)>>onWillDisappear>>onDidDisappear。

2.快速点击弹出，消失弹窗时，存在onWillDisappear在onDidAppear前生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| shadow12+ | [ShadowOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-image-effect#shadowoptions对象说明) | [ShadowStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-image-effect#shadowstyle10枚举说明) | 否 | 是 | 

设置弹窗背板的阴影。

**说明：**

当设备为2in1时，默认场景下获焦阴影值为ShadowStyle.OUTER\_FLOATING\_MD，失焦为ShadowStyle.OUTER\_FLOATING\_SM。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| dateTimeOptions12+ | [DateTimeOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-intl#datetimeoptionsdeprecated) | 否 | 是 | 

设置时分是否显示前导0，目前只支持设置hour和minute参数。

默认值：

hour: 24小时制默认为"2-digit"，设置hour是否按照2位数字显示，如果实际数值小于10，则会补充前导0并显示，即为"0X"；12小时制默认为"numeric"，即没有前导0。

minute: 默认为"2-digit"，设置minute是否按照2位数字显示，如果实际数值小于10，则会补充前导0并显示，即为"0X"。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| enableHoverMode14+ | boolean | 否 | 是 | 

是否响应悬停态。

\- true：响应悬停态。

\- false：不响应悬停态。

默认值：false

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

 |
| hoverModeArea14+ | [HoverModeAreaType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-sheet-transition#hovermodeareatype14) | 否 | 是 | 

悬停态下弹窗默认展示区域。

默认值：HoverModeAreaType.BOTTOM\_SCREEN

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

 |
| onEnterSelectedArea18+ | Callback<[TimePickerResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-timepicker#timepickerresult对象说明)\> | 否 | 是 | 

滑动过程中，选项进入分割线区域内，触发该回调。与onChange事件的差别在于，该事件的触发时机早于onChange事件，当当前滑动列滑动距离超过选中项高度的一半时，选项此时已经进入分割线区域内，会触发该事件。

**说明：**

当enableCascade设置为true时，由于上午/下午列与小时列存在联动关系，不建议使用该回调。该回调标识的是滑动过程中选项进入分割线区域内的节点，而联动变化的选项并不涉及滑动，因此，回调的返回值中，仅当前滑动列的值会正常变化，其余未滑动列的值保持不变。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

 |
| enableCascade18+ | boolean | 否 | 是 | 

设置上午和下午的标识是否根据小时数自动切换，仅在useMilitaryTime设置为false时生效。

\- true：自动切换。

\- false：不自动切换。

默认值：false

当enableCascade设置为true时，仅在loop参数同时为true时生效。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

 |
| enableHapticFeedback18+ | boolean | 否 | 是 | 

设置是否开启触控反馈。

\- true：开启触控反馈。

\- false：不开启触控反馈。

默认值：true

**说明**：

1\. 设置为true后，其生效情况取决于系统的硬件是否支持。

2\. 开启触控反馈时，需要在工程的src/main/module.json5文件的"module"内配置requestPermissions字段开启振动权限，配置如下：

"requestPermissions": \[{"name": "ohos.permission.VIBRATE"}\]

**元服务API**： 从API version 18开始，该接口支持在元服务中使用。

 |

#### 示例

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/sxH8ojeoQhW2MltwWgtB8w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014801Z&HW-CC-Expire=86400&HW-CC-Sign=59DD5812831E2CAAC8902C8F9E3A7B5F4857FB6F7FC6A756A7E09CD2D9615D23)

推荐通过使用[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[showTimePickerDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#showtimepickerdialog)来明确UI的执行上下文。

#### \[h2\]示例1（设置时间格式）

该示例通过useMilitaryTime、dateTimeOptions、format设置时间格式。

```ts
@Entry
@Component
struct TimePickerDialogExample {
  private selectTime: Date = new Date('2020-12-25T08:30:00');

  build() {
    Column() {
      Button('TimePickerDialog 12小时制')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showTimePickerDialog({
            selected: this.selectTime,
            format: TimePickerFormat.HOUR_MINUTE,
            useMilitaryTime: false,
            dateTimeOptions: { hour: 'numeric', minute: '2-digit' },
            onAccept: (value: TimePickerResult) => {
              // 设置selectTime为按下确定按钮时的时间，这样当弹窗再次弹出时显示选中的为上一次确定的时间
              if (value.hour != undefined && value.minute != undefined) {
                this.selectTime.setHours(value.hour, value.minute);
                console.info('TimePickerDialog:onAccept()' + JSON.stringify(value));
              }
            },
            onCancel: () => {
              console.info('TimePickerDialog:onCancel()');
            },
            onChange: (value: TimePickerResult) => {
              console.info('TimePickerDialog:onChange()' + JSON.stringify(value));
            },
            onDidAppear: () => {
              console.info('TimePickerDialog:onDidAppear()');
            },
            onDidDisappear: () => {
              console.info('TimePickerDialog:onDidDisappear()');
            },
            onWillAppear: () => {
              console.info('TimePickerDialog:onWillAppear()');
            },
            onWillDisappear: () => {
              console.info('TimePickerDialog:onWillDisappear()');
            }
          });
        })
      Button('TimePickerDialog 24小时制')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showTimePickerDialog({
            selected: this.selectTime,
            format: TimePickerFormat.HOUR_MINUTE_SECOND,
            useMilitaryTime: true,
            onAccept: (value: TimePickerResult) => {
              if (value.hour != undefined && value.minute != undefined) {
                this.selectTime.setHours(value.hour, value.minute);
                console.info('TimePickerDialog:onAccept()' + JSON.stringify(value));
              }
            },
          })
        })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/1A2MvhrrT8GfgtQ_JQjfGA/zh-cn_image_0000002568900711.gif?HW-CC-KV=V1&HW-CC-Date=20260417T014801Z&HW-CC-Expire=86400&HW-CC-Sign=F79581BCAC8E2E78E527DDA62E40C7E0868F4160CB332735411FFAEBECF0E3C0)

#### \[h2\]示例2（自定义样式）

该示例通过配置disappearTextStyle、textStyle、selectedTextStyle、acceptButtonStyle、cancelButtonStyle实现了自定义文本以及按钮样式。

```ts
// xxx.ets
@Entry
@Component
struct TimePickerDialogExample {
  private selectTime: Date = new Date('2020-12-25T08:30:00');

  build() {
    Column() {
      Button('TimePickerDialog 12小时制')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showTimePickerDialog({
            disappearTextStyle: { color: '#297bec', font: { size: 15, weight: FontWeight.Lighter } },
            textStyle: { color: Color.Black, font: { size: 20, weight: FontWeight.Normal } },
            selectedTextStyle: { color: Color.Blue, font: { size: 30, weight: FontWeight.Bolder } },
            acceptButtonStyle: {
              type: ButtonType.Normal,
              style: ButtonStyleMode.NORMAL,
              role: ButtonRole.NORMAL,
              fontColor: 'rgb(81, 81, 216)',
              fontSize: '26fp',
              fontWeight: FontWeight.Bolder,
              fontStyle: FontStyle.Normal,
              fontFamily: 'sans-serif',
              backgroundColor: '#A6ACAF',
              borderRadius: 20
            },
            cancelButtonStyle: {
              type: ButtonType.Normal,
              style: ButtonStyleMode.NORMAL,
              role: ButtonRole.NORMAL,
              fontColor: Color.Blue,
              fontSize: '16fp',
              fontWeight: FontWeight.Normal,
              fontStyle: FontStyle.Italic,
              fontFamily: 'sans-serif',
              backgroundColor: '#50182431',
              borderRadius: 10
            },
            onAccept: (value: TimePickerResult) => {
              if (value.hour != undefined && value.minute != undefined) {
                this.selectTime.setHours(value.hour, value.minute);
                console.info('TimePickerDialog:onAccept()' + JSON.stringify(value));
              }
            }
          });
        })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/nGmEVis6TJeti1R7VG9MEA/zh-cn_image_0000002538021010.png?HW-CC-KV=V1&HW-CC-Date=20260417T014801Z&HW-CC-Expire=86400&HW-CC-Sign=66C4DA880FCA09439160E738FAEFBC657FA67CD172C8E2AE8CB208393F8AF49C)

#### \[h2\]示例3（悬停态弹窗）

该示例展示了在折叠屏悬停态下设置dialog布局区域的效果。

```ts
@Entry
@Component
struct TimePickerDialogExample {
  private selectTime: Date = new Date('2020-12-25T08:30:00');

  build() {
    Column() {
      Button('TimePickerDialog 12小时制')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showTimePickerDialog({
            selected: this.selectTime,
            disappearTextStyle: { color: Color.Red, font: { size: 15, weight: FontWeight.Lighter } },
            textStyle: { color: Color.Black, font: { size: 20, weight: FontWeight.Normal } },
            selectedTextStyle: { color: Color.Blue, font: { size: 30, weight: FontWeight.Bolder } },
            onAccept: (value: TimePickerResult) => {
              // 设置selectTime为按下确定按钮时的时间，这样当弹窗再次弹出时显示选中的为上一次确定的时间
              if (value.hour != undefined && value.minute != undefined) {
                this.selectTime.setHours(value.hour, value.minute);
                console.info('TimePickerDialog:onAccept()' + JSON.stringify(value));
              }
            },
            onCancel: () => {
              console.info('TimePickerDialog:onCancel()');
            },
            onChange: (value: TimePickerResult) => {
              console.info('TimePickerDialog:onChange()' + JSON.stringify(value));
            },
            onDidAppear: () => {
              console.info('TimePickerDialog:onDidAppear()');
            },
            onDidDisappear: () => {
              console.info('TimePickerDialog:onDidDisappear()');
            },
            onWillAppear: () => {
              console.info('TimePickerDialog:onWillAppear()');
            },
            onWillDisappear: () => {
              console.info('TimePickerDialog:onWillDisappear()');
            },
            enableHoverMode: true,
            hoverModeArea: HoverModeAreaType.TOP_SCREEN
          });
        })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/E_JmjVy2SNKvtXb1-iuDBQ/zh-cn_image_0000002538180936.gif?HW-CC-KV=V1&HW-CC-Date=20260417T014801Z&HW-CC-Expire=86400&HW-CC-Sign=A1A3A0D58C691BE0529B89E06DAB785C889B006FF80465B71EB3EFAF735B20A7)

#### \[h2\]示例4（设置弹窗位置）

该示例通过alignment和offset设置弹窗的位置。

```ts
// xxx.ets
@Entry
@Component
struct TimePickerDialogExample {
  private selectTime: Date = new Date('2020-12-25T08:30:00');

  build() {
    Column() {
      Button('TimePickerDialog')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showTimePickerDialog({
            alignment: DialogAlignment.Center,
            offset: { dx: 20 , dy: 0 },
            onAccept: (value: TimePickerResult) => {
              // 设置selectTime为按下确定按钮时的时间，这样当弹窗再次弹出时显示选中的为上一次确定的时间
              if (value.hour != undefined && value.minute != undefined) {
                this.selectTime.setHours(value.hour, value.minute);
                console.info('TimePickerDialog:onAccept()' + JSON.stringify(value));
              }
            }
          });
        })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/zAd6nvf3RBWZatk89McFXQ/zh-cn_image_0000002569020723.png?HW-CC-KV=V1&HW-CC-Date=20260417T014801Z&HW-CC-Expire=86400&HW-CC-Sign=367A065AFFDABA8110720B554CD567E173F513A8CCB2919761FB6D3179BB39DF)

#### \[h2\]示例5（设置遮蔽区）

该示例通过maskRect设置遮蔽区。

```ts
// xxx.ets
@Entry
@Component
struct TimePickerDialogExample {
  private selectTime: Date = new Date('2020-12-25T08:30:00');

  build() {
    Column() {
      Button('TimePickerDialog')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showTimePickerDialog({
            maskRect: { x: 30, y: 60, width: '100%', height: '60%' },
            onAccept: (value: TimePickerResult) => {
              // 设置selectTime为按下确定按钮时的时间，这样当弹窗再次弹出时显示选中的为上一次确定的时间
              if (value.hour != undefined && value.minute != undefined) {
                this.selectTime.setHours(value.hour, value.minute);
                console.info('TimePickerDialog:onAccept()' + JSON.stringify(value));
              }
            }
          });
        })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/3o-TWqOeQyKe_j5LnwdHUw/zh-cn_image_0000002568900713.png?HW-CC-KV=V1&HW-CC-Date=20260417T014801Z&HW-CC-Expire=86400&HW-CC-Sign=47D15B2F8B9C5715353FC5B69161D78E95982FF489ACE45732A116165C63E3FE)

#### \[h2\]示例6（设置弹窗背板）

该示例通过maskRect设置弹窗背板。

```ts
// xxx.ets
@Entry
@Component
struct TimePickerDialogExample {
  private selectTime: Date = new Date('2020-12-25T08:30:00');

  build() {
    Column() {
      Button('TimePickerDialog')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showTimePickerDialog({
            backgroundColor: 'rgb(204, 226, 251)',
            backgroundBlurStyle: BlurStyle.NONE,
            shadow: ShadowStyle.OUTER_FLOATING_SM,
            onAccept: (value: TimePickerResult) => {
              // 设置selectTime为按下确定按钮时的时间，这样当弹窗再次弹出时显示选中的为上一次确定的时间
              if (value.hour != undefined && value.minute != undefined) {
                this.selectTime.setHours(value.hour, value.minute);
                console.info('TimePickerDialog:onAccept()' + JSON.stringify(value));
              }
            }
          });
        })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/PptFTyP6TxCM6se8xcFsyw/zh-cn_image_0000002538021012.png?HW-CC-KV=V1&HW-CC-Date=20260417T014801Z&HW-CC-Expire=86400&HW-CC-Sign=3F124135F16019E7A161C54F27162FCC90A7FB7FFFC58248F65D4B68C76A1A01)

#### \[h2\]示例7（设置时间滑动选择器弹窗的起始时间）

该示例设置TimePickerDialog的起始时间。

```ts
// xxx.ets
@Entry
@Component
struct TimePickerDialogExample {
  private selectTime: Date = new Date('2022-07-22T08:50:00');

  build() {
    Column() {
      Button('TimePickerDialog')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showTimePickerDialog({
            useMilitaryTime: false,
            selected: this.selectTime,
            format: TimePickerFormat.HOUR_MINUTE_SECOND,
            start: new Date('2022-07-22T08:30:00'),
            onAccept: (value: TimePickerResult) => {
              // 设置selectTime为按下确定按钮时的时间，这样当弹窗再次弹出时显示选中的为上一次确定的时间
              if (value.hour != undefined && value.minute != undefined) {
                this.selectTime.setHours(value.hour, value.minute);
                console.info('TimePickerDialog:onAccept()' + JSON.stringify(value));
              }
            }
          });
        })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/gQjzhzm3TDCUI3PfjcYQfA/zh-cn_image_0000002538180938.png?HW-CC-KV=V1&HW-CC-Date=20260417T014801Z&HW-CC-Expire=86400&HW-CC-Sign=1A789FE1C76E6B98F6EA769DA6FEBA9427EE4A67E19C78B40D8781C1A464A47C)

#### \[h2\]示例8（设置时间滑动选择器弹窗的结束时间）

该示例设置TimePickerDialog的结束时间。

```ts
// xxx.ets
@Entry
@Component
struct TimePickerDialogExample {
  private selectTime: Date = new Date('2022-07-22T08:50:00');

  build() {
    Column() {
      Button('TimePickerDialog')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showTimePickerDialog({
            useMilitaryTime: false,
            selected: this.selectTime,
            format: TimePickerFormat.HOUR_MINUTE_SECOND,
            end: new Date('2022-07-22T15:20:00'),
            onAccept: (value: TimePickerResult) => {
              // 设置selectTime为按下确定按钮时的时间，这样当弹窗再次弹出时显示选中的为上一次确定的时间
              if (value.hour != undefined && value.minute != undefined) {
                this.selectTime.setHours(value.hour, value.minute);
                console.info('TimePickerDialog:onAccept()' + JSON.stringify(value));
              }
            }
          });
        })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/hieW8a-6QmSEP2xW8ll3qA/zh-cn_image_0000002569020725.png?HW-CC-KV=V1&HW-CC-Date=20260417T014801Z&HW-CC-Expire=86400&HW-CC-Sign=AE69B5C274CFC16601CD090972999C21BD584E5DD8BEC6073CBBC5EE99595AA7)

#### \[h2\]示例9（设置上午下午跟随时间联动）

该示例通过配置enableCascade实现12小时制时上午下午跟随时间联动。

```ts
// xxx.ets
@Entry
@Component
struct TimePickerDialogExample {
  private selectTime: Date = new Date('2022-07-22T08:00:00');

  build() {
    Column() {
      Button('TimePickerDialog')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showTimePickerDialog({
            useMilitaryTime: false,
            selected: this.selectTime,
            enableCascade:true,
            onAccept: (value: TimePickerResult) => {
              // 设置selectTime为按下确定按钮时的时间，这样当弹窗再次弹出时显示选中的为上一次确定的时间
              if (value.hour != undefined && value.minute != undefined) {
                this.selectTime.setHours(value.hour, value.minute);
                console.info('TimePickerDialog:onAccept()' + JSON.stringify(value));
              }
            }
          });
        })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/Y-2gkSayQkGNsZfyWVNpsg/zh-cn_image_0000002568900715.gif?HW-CC-KV=V1&HW-CC-Date=20260417T014801Z&HW-CC-Expire=86400&HW-CC-Sign=0B26CD7843640CC7E366A527B57012FB3565CFF73ED45D6BA0A3195D90B758C8)

#### \[h2\]示例10（自定义背景模糊效果参数）

从API version 19开始，该示例通过配置[backgroundBlurStyleOptions](#timepickerdialogoptions对象说明)，实现自定义背景模糊效果。

```ts
@Entry
@Component
struct TimePickerDialogExample {
  build() {
    Stack({ alignContent: Alignment.Top }) {
      // $r('app.media.bg')需要替换为开发者所需的图像资源文件。
      Image($r('app.media.bg'))
      Column() {
        Button('TimePickerDialog')
          .margin(20)
          .onClick(() => {
            this.getUIContext().showTimePickerDialog({
              backgroundColor: undefined,
              backgroundBlurStyle: BlurStyle.Thin,
              backgroundBlurStyleOptions: {
                colorMode: ThemeColorMode.LIGHT,
                adaptiveColor: AdaptiveColor.AVERAGE,
                scale: 1,
                blurOptions: { grayscale: [20, 20] },
              },
            });
          })
      }.width('100%')
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/1mhTO4yTSpKMf_t8gX7RRg/zh-cn_image_0000002538021014.png?HW-CC-KV=V1&HW-CC-Date=20260417T014801Z&HW-CC-Expire=86400&HW-CC-Sign=B38909E77F4439AFC7259ACF0CC5DDFB5996A90034E3F6663009EDA50EE0CD51)

#### \[h2\]示例11（自定义背景效果参数）

从API version 19开始，该示例通过配置[backgroundEffect](#timepickerdialogoptions对象说明)，实现自定义背景效果。

```ts
@Entry
@Component
struct TimePickerDialogExample {
  build() {
    Stack({ alignContent: Alignment.Top }) {
      // $r('app.media.bg')需要替换为开发者所需的图像资源文件。
      Image($r('app.media.bg'))
      Column() {
        Button('TimePickerDialog')
          .margin(20)
          .onClick(() => {
            this.getUIContext().showTimePickerDialog({
              backgroundColor: undefined,
              backgroundBlurStyle: BlurStyle.Thin,
              backgroundEffect: {
                radius: 60,
                saturation: 0,
                brightness: 1,
                color: Color.White,
                blurOptions: { grayscale: [20, 20] }
              },
            });
          })
      }.width('100%')
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/SybpMPWnTdmfB4pCIQPu6Q/zh-cn_image_0000002538180940.png?HW-CC-KV=V1&HW-CC-Date=20260417T014801Z&HW-CC-Expire=86400&HW-CC-Sign=E09E4AA96952BEDB4C3D4A6F47CA8EE7B88FA64946E375CF137A935BB17477F3)

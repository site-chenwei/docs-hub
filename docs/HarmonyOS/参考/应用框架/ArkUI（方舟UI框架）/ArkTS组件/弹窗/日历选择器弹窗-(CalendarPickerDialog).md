---
title: "日历选择器弹窗 (CalendarPickerDialog)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-calendarpicker-dialog"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "ArkTS组件"
  - "弹窗"
  - "日历选择器弹窗 (CalendarPickerDialog)"
captured_at: "2026-04-17T01:47:58.675Z"
---

# 日历选择器弹窗 (CalendarPickerDialog)

点击日期弹出日历选择器弹窗，可在弹窗内选择日期。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/N4ZeInJTTfiyOIC99B12_A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014801Z&HW-CC-Expire=86400&HW-CC-Sign=CE9B543D4DD3A52E841EB7FF5B71B81A589F036E2F101C54F672264434E43075)

-   该组件从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
    
-   本模块功能依赖UI的执行上下文，不可在[UI上下文不明确](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface#ui上下文不明确)的地方使用，参见[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)说明。
    
-   本模块不支持深浅色模式热更新，如果需要进行深浅色模式切换，请重新打开弹窗。
    

#### CalendarPickerDialog

#### \[h2\]show

static show(options?: CalendarDialogOptions): void

定义日历选择器弹窗。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [CalendarDialogOptions](#calendardialogoptions对象说明) | 否 | 配置日历选择器弹窗参数。 |

#### CalendarDialogOptions对象说明

日历选择器弹窗选项。

继承自[CalendarOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-calendarpicker#calendaroptions对象说明)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| onAccept | [Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#callback12)<Date> | 否 | 是 | 
点击弹窗中的“确定”按钮时触发该回调。

回调函数的参数表示选中的日期值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| onCancel | [VoidCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#voidcallback12) | 否 | 是 | 

点击弹窗中的“取消”按钮时触发该回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| onChange | [Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#callback12)<Date> | 否 | 是 | 

选择弹窗中日期使当前选中项改变时触发该回调。

回调函数的参数表示选中的日期值。

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
| acceptButtonStyle12+ | [PickerDialogButtonStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-picker-common#pickerdialogbuttonstyle12对象说明) | 否 | 是 | 

设置确认按钮显示样式、样式和重要程度、角色、背景色、圆角、文本颜色、字号、字体粗细、字体样式、字体列表、按钮是否默认响应Enter键。

**说明：**

acceptButtonStyle与cancelButtonStyle中最多只能有一个primary字段配置为true，二者primary字段均配置为true时均不生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| cancelButtonStyle12+ | [PickerDialogButtonStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-picker-common#pickerdialogbuttonstyle12对象说明) | 否 | 是 | 

设置取消按钮显示样式、样式和重要程度、角色、背景色、圆角、文本颜色、字号、字体粗细、字体样式、字体列表、按钮是否默认响应Enter键。

**说明：**

acceptButtonStyle与cancelButtonStyle中最多只能有一个primary字段配置为true，二者primary字段均配置为true时均不生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| onDidAppear12+ | [VoidCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#voidcallback12) | 否 | 是 | 

弹窗弹出后的事件回调。

**说明：**

1.正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange)>>onWillDisappear>>onDidDisappear。

2.在onDidAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。

3.快速点击弹出，消失弹窗时，存在onWillDisappear在onDidAppear前生效。

4\. 当弹窗入场动效未完成时关闭弹窗，该回调不会触发。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| onDidDisappear12+ | [VoidCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#voidcallback12) | 否 | 是 | 

弹窗消失后的事件回调。

**说明：**

1.正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange)>>onWillDisappear>>onDidDisappear。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| onWillAppear12+ | [VoidCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#voidcallback12) | 否 | 是 | 

弹窗显示动效前的事件回调。

**说明：**

1.正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange)>>onWillDisappear>>onDidDisappear。

2.在onWillAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| onWillDisappear12+ | [VoidCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#voidcallback12) | 否 | 是 | 

弹窗退出动效前的事件回调。

**说明：**

1.正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange)>>onWillDisappear>>onDidDisappear。

2.快速点击弹出，消失弹窗时，存在onWillDisappear在onDidAppear前生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |
| shadow12+ | [ShadowOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-image-effect#shadowoptions对象说明) | [ShadowStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-image-effect#shadowstyle10枚举说明) | 否 | 是 | 

设置弹窗背板的阴影。

当设备为2in1时，默认场景下，获焦时阴影值为ShadowStyle.OUTER\_FLOATING\_MD，失焦时为ShadowStyle.OUTER\_FLOATING\_SM。

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
| markToday19+ | boolean | 否 | 是 | 

设置日历选择器弹窗中系统当前日期是否保持高亮显示。

\- true：系统当前日期在日历选择器弹窗内保持高亮显示。

\- false：系统当前日期在日历选择器弹窗内不保持高亮显示。

默认值：false

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/wxk5Q006TvWlytgiK3xpiA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014801Z&HW-CC-Expire=86400&HW-CC-Sign=A8B9A70B5EDBACCF457D0E9DFCED5830CBF0785D32C6B095369E6EB84AA081AB)

在应用窗口缩小过程中，弹窗的宽度会被不断压缩，当缩小到一定程度时会导致其内容无法完整显示，保证CalendarPickerDialog内容能够完整显示的最小窗口宽度为386vp。

#### 示例

#### \[h2\]示例1（设置弹窗背板）

该示例通过[CalendarDialogOptions](#calendardialogoptions对象说明)的backgroundColor、backgroundBlurStyle、shadow设置日历选择器弹窗背板。

```ts
// xxx.ets
@Entry
@Component
struct CalendarPickerDialogExample {
  private selectedDate: Date = new Date('2024-03-24');

  build() {
    Column() {
      Button('Show CalendarPicker Dialog')
        .margin(20)
        .onClick(() => {
          console.info('CalendarDialog.show');
          CalendarPickerDialog.show({
            selected: this.selectedDate,
            backgroundColor: Color.Gray,
            backgroundBlurStyle: BlurStyle.NONE,
            shadow: ShadowStyle.OUTER_FLOATING_SM,
            onAccept: (value) => {
              // 点击弹窗中的“确定”按钮时触发该回调，value表示选中的日期值。
              this.selectedDate = value;
              console.info('calendar onAccept:' + JSON.stringify(value));
            },
            onCancel: () => {
              // 点击弹窗中的“取消”按钮时触发该回调。
              console.info('calendar onCancel');
            },
            onChange: (value) => {
              // 选择弹窗中日期使当前选中项改变时触发该回调，value表示选中的日期值。
              console.info('calendar onChange:' + JSON.stringify(value));
            },
            onDidAppear: () => {
              console.info('calendar onDidAppear');
            },
            onDidDisappear: () => {
              console.info('calendar onDidDisappear');
            },
            onWillAppear: () => {
              console.info('calendar onWillAppear');
            },
            onWillDisappear: () => {
              console.info('calendar onWillDisappear');
            }
          });
        })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/wZ5SJx1mR9SEbSPg1_ZwgQ/zh-cn_image_0000002538021000.gif?HW-CC-KV=V1&HW-CC-Date=20260417T014801Z&HW-CC-Expire=86400&HW-CC-Sign=0E6DD4FADC776BC94CFB36DF8FB3E85D54A6C8315FDE13642FAA46ED002DB6A0)

#### \[h2\]示例2（自定义按钮样式）

从API version 12开始，该示例通过配置[CalendarDialogOptions](#calendardialogoptions对象说明)的acceptButtonStyle、cancelButtonStyle实现自定义日历选择器弹窗按钮样式。

```ts
// xxx.ets
@Entry
@Component
struct CalendarPickerDialogExample {
  private selectedDate: Date = new Date();

  build() {
    Column() {
      Button('Show CalendarPicker Dialog')
        .margin(20)
        .onClick(() => {
          console.info('CalendarDialog.show');
          CalendarPickerDialog.show({
            selected: this.selectedDate,
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
            onAccept: (value) => {
              this.selectedDate = value;
              console.info('calendar onAccept:' + JSON.stringify(value));
            }
          });
        })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/z0tEyGdpSJO3HmZp5FY-PQ/zh-cn_image_0000002538180926.png?HW-CC-KV=V1&HW-CC-Date=20260417T014801Z&HW-CC-Expire=86400&HW-CC-Sign=272E5946293CC771AAF886C6CD4589ABC30A02459DE61596065CF2BE17443F2A)

#### \[h2\]示例3（悬停态弹窗）

从API version 14开始，该示例展示了在折叠屏悬停态下设置dialog布局区域的效果。

```ts
@Entry
@Component
struct CalendarPickerDialogExample {
  private selectedDate: Date = new Date('2024-04-23');

  build() {
    Column() {
      Button('Show CalendarPicker Dialog')
        .margin(20)
        .onClick(() => {
          console.info('CalendarDialog.show');
          CalendarPickerDialog.show({
            selected: this.selectedDate,
            onAccept: (value) => {
              console.info('calendar onAccept:' + JSON.stringify(value));
            },
            onCancel: () => {
              console.info('calendar onCancel');
            },
            onChange: (value) => {
              console.info('calendar onChange:' + JSON.stringify(value));
            },
            onDidAppear: () => {
              console.info('calendar onDidAppear');
            },
            onDidDisappear: () => {
              console.info('calendar onDidDisappear');
            },
            onWillAppear: () => {
              console.info('calendar onWillAppear');
            },
            onWillDisappear: () => {
              console.info('calendar onWillDisappear');
            },
            enableHoverMode: true,
            hoverModeArea: HoverModeAreaType.TOP_SCREEN,
          });
        })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/_JPnQGBVQZGJvVqYBOwbUg/zh-cn_image_0000002569020713.gif?HW-CC-KV=V1&HW-CC-Date=20260417T014801Z&HW-CC-Expire=86400&HW-CC-Sign=7B0B72A4A5EBD6514DEEEA746A2B7791A84A4B121A218909D922CCB1D280D43A)

#### \[h2\]示例4（设置日期选中态底板样式）

从API version 10开始，该示例通过[CalendarOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-calendarpicker#calendaroptions对象说明)的hintRadius设置日期选中态底板样式。

```ts
// xxx.ets
@Entry
@Component
struct CalendarPickerDialogExample {
  private selectedDate: Date = new Date('2024-04-23');

  build() {
    Column() {
      Button('Show CalendarPicker Dialog')
        .margin(20)
        .onClick(() => {
          console.info('CalendarDialog.show');
          CalendarPickerDialog.show({
            selected: this.selectedDate,
            hintRadius: 1,
            onAccept: (value) => {
              this.selectedDate = value;
              console.info('calendar onAccept:' + JSON.stringify(value));
            }
          });
        })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/6TRwwae4TCmUDN9fYRIJlQ/zh-cn_image_0000002568900703.png?HW-CC-KV=V1&HW-CC-Date=20260417T014801Z&HW-CC-Expire=86400&HW-CC-Sign=56A8B451294021D787C62136EBD087D52E9FD2CFEEAD2826394A0256EB940D20)

#### \[h2\]示例5（设置开始日期和结束日期）

从API version 18开始，该示例通过[CalendarOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-calendarpicker#calendaroptions对象说明)的start和end设置日历选择器弹窗的开始日期和结束日期。

```ts
// xxx.ets
@Entry
@Component
struct CalendarPickerDialogExample {
  private selectedDate: Date = new Date('2025-01-01');
  private startDate: Date = new Date('2024-01-10');
  private endDate: Date = new Date('2025-01-10');

  build() {
    Column() {
      Text('月历日期选择器').fontSize(30)
      Button('Show CalendarPicker Dialog')
        .margin(20)
        .onClick(() => {
          console.info('CalendarDialog.show');
          CalendarPickerDialog.show({
            start: this.startDate,
            end: this.endDate,
            selected: this.selectedDate,
          });
        })
    }.width('100%').margin({ top: 350 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/aI4WcCzBSZWXTuvu9FdIWA/zh-cn_image_0000002538021002.gif?HW-CC-KV=V1&HW-CC-Date=20260417T014801Z&HW-CC-Expire=86400&HW-CC-Sign=2B16F209FE36D2C503C25BD21CDE66F920016E1A3661F80A032452BA0FC410D9)

#### \[h2\]示例6（设置系统当前日期在日历选择器弹窗内保持高亮显示，并设置禁用日期区间）

从API version 19开始，该示例通过配置[CalendarDialogOptions](#calendardialogoptions对象说明)的markToday，使系统当前日期在日历选择器弹窗内保持高亮显示，并通过配置[CalendarOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-calendarpicker#calendaroptions对象说明)的disabledDateRange设置禁用的日期区间。

```ts
// xxx.ets
@Entry
@Component
struct CalendarPickerExample {
  private disabledDateRange: DateRange[] = [
    { start: new Date('2025-01-01'), end: new Date('2025-01-02') },
    { start: new Date('2025-01-09'), end: new Date('2025-01-10') },
    { start: new Date('2025-01-15'), end: new Date('2025-01-16') },
    { start: new Date('2025-01-19'), end: new Date('2025-01-19') },
    { start: new Date('2025-01-22'), end: new Date('2025-01-25') }
  ];

  build() {
    Column() {
      Button("Show CalendarPicker Dialog")
        .margin(20)
        .onClick(() => {
          console.info('CalendarDialog.show');
          CalendarPickerDialog.show({ markToday: true, disabledDateRange: this.disabledDateRange });
        })
    }.width('100%').margin({ top: 350 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/gNkwhG5_S7GNbEcIKTyL6w/zh-cn_image_0000002538180928.gif?HW-CC-KV=V1&HW-CC-Date=20260417T014801Z&HW-CC-Expire=86400&HW-CC-Sign=A8383838CCB0DF6DE4A0F9C522C2B439E3363C2A69C6E6BD198D709F2A88AC38)

#### \[h2\]示例7（自定义背景模糊效果参数）

从API version 19开始，该示例通过配置[backgroundBlurStyleOptions](#calendardialogoptions对象说明)，实现自定义背景模糊效果。

```ts
@Entry
@Component
struct CalendarPickerDialogExample {
  private selectedDate: Date = new Date('2025-08-05');

  build() {
    Stack({ alignContent: Alignment.Top }) {
      // $r('app.media.bg')需要替换为开发者所需的图像资源文件。
      Image($r('app.media.bg'))
      Column() {
        Button('Show CalendarPicker Dialog')
          .margin(20)
          .onClick(() => {
            CalendarPickerDialog.show({
              selected: this.selectedDate,
              hintRadius: 1,
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/Z1y_yJuURI2S1W6Iqboaag/zh-cn_image_0000002569020715.png?HW-CC-KV=V1&HW-CC-Date=20260417T014801Z&HW-CC-Expire=86400&HW-CC-Sign=A7418F64D4F24912C6893DF5D7D7F4DFED6CACE250FB6F5B23C58D90466B2E28)

#### \[h2\]示例8（自定义背景效果参数）

从API version 19开始，该示例通过配置[backgroundEffect](#calendardialogoptions对象说明)，实现自定义背景效果。

```ts
@Entry
@Component
struct CalendarPickerDialogExample {
  private selectedDate: Date = new Date('2025-08-05');

  build() {
    Stack({ alignContent: Alignment.Top }) {
      // $r('app.media.bg')需要替换为开发者所需的图像资源文件。
      Image($r('app.media.bg'))
      Column() {
        Button('Show CalendarPicker Dialog')
          .margin(20)
          .onClick(() => {
            CalendarPickerDialog.show({
              selected: this.selectedDate,
              hintRadius: 1,
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/JLHVQGnnREuHYAGFA8ZThQ/zh-cn_image_0000002568900705.png?HW-CC-KV=V1&HW-CC-Date=20260417T014801Z&HW-CC-Expire=86400&HW-CC-Sign=DAF5963C06EB7EA5978D441FC3A2D5A84301899F5F0F85B4E4D327848B7E2516)

---
title: "DownloadFileButton"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-downloadfilebutton"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "ArkTS组件"
  - "系统预置UI组件库"
  - "DownloadFileButton"
captured_at: "2026-04-17T01:47:59.519Z"
---

# DownloadFileButton

下载文件按钮，通过点击该下载按钮，可以获取到当前应用在Download公共目录中所属的存储路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/pV1J_U0oQSmSftHzedqISA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014802Z&HW-CC-Expire=86400&HW-CC-Sign=58143A62AF66280ECDC31C346D744C21D402629826E6B93F1C60D56DD6F05955)

该组件从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

该组件不支持在Wearable设备上使用。

#### 导入模块

```ts
import { DownloadFileButton } from '@kit.ArkUI';
```

#### 子组件

无

#### 属性

支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)。

#### DownloadFileButton

下载文件按钮组件，默认显示图标和文字。

**装饰器类型：**@Component

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| contentOptions | [DownloadContentOptions](#downloadcontentoptions) | 是 | @State | 创建包含指定元素内容的下载按钮。 |
| styleOptions | [DownloadStyleOptions](#downloadstyleoptions) | 是 | @State | 创建包含指定元素样式的下载按钮。 |

#### DownloadContentOptions

下载文件按钮中显示的内容。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| icon | [DownloadIconStyle](#downloadiconstyle) | 否 | 是 | 
设置下载按钮的图标风格。

不传入该参数表示没有图标，icon和text至少存在一个。

 |
| text | [DownloadDescription](#downloaddescription) | 否 | 是 | 

设置下载按钮的文本描述。

不传入该参数表示没有文字描述，icon和text至少存在一个。

 |

#### DownloadStyleOptions

下载文件按钮中图标和文字的样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| iconSize | [Dimension](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#dimension10) | 否 | 是 | 
下载控件上图标的尺寸，不支持百分比。

默认值：16vp

 |
| layoutDirection | [DownloadLayoutDirection](#downloadlayoutdirection) | 否 | 是 | 

下载控件上图标和文字分布的方向。

默认值：DownloadLayoutDirection.HORIZONTAL

 |
| fontSize | [Dimension](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#dimension10) | 否 | 是 | 

下载控件上文字的尺寸，不支持百分比。

默认值：16fp

 |
| fontStyle | [FontStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#fontstyle) | 否 | 是 | 

下载控件上文字的样式。

默认值：FontStyle.Normal

 |
| fontWeight | number|[FontWeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#fontweight)|string | 否 | 是 | 

下载控件上文字粗细，number类型取值\[100, 900\]，取值间隔为100，默认为400，取值越大，字体越粗。string类型仅支持number类型取值的字符串形式，例如"400"，以及"bold"、"bolder"、"lighter"、"regular"、"medium"，分别对应FontWeight中相应的枚举值。

默认值：FontWeight.Medium

 |
| fontFamily | string|[Resource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resource) | 否 | 是 | 

下载控件上文字的字体。

默认字体：'HarmonyOS Sans'

 |
| fontColor | [ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor) | 否 | 是 | 

下载控件上文字的颜色。

默认值：#ffffffff

 |
| iconColor | [ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor) | 否 | 是 | 

下载控件上图标的颜色。

默认值：#ffffffff

 |
| textIconSpace | [Dimension](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#dimension10) | 否 | 是 | 

下载控件中图标和文字的间距。

默认值：4vp

 |

#### DownloadIconStyle

下载文件按钮中图标的风格。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| FULL\_FILLED | 1 | 下载按钮展示填充样式图标。 |
| LINES | 2 | 下载按钮展示线条样式图标。 |

#### DownloadDescription

下载按钮中文字的内容。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| DOWNLOAD | 1 | 下载按钮的文字描述为“下载”。 |
| DOWNLOAD\_FILE | 2 | 下载按钮的文字描述为“下载文件”。 |
| SAVE | 3 | 下载按钮的文字描述为“保存”。 |
| SAVE\_IMAGE | 4 | 下载按钮的文字描述为“保存图片”。 |
| SAVE\_FILE | 5 | 下载按钮的文字描述为“保存文件”。 |
| DOWNLOAD\_AND\_SHARE | 6 | 下载按钮的文字描述为“下载分享”。 |
| RECEIVE | 7 | 下载按钮的文字描述为“接收”。 |
| CONTINUE\_TO\_RECEIVE | 8 | 下载按钮的文字描述为“继续接收”。 |

#### DownloadLayoutDirection

下载文件按钮中图标和文字的排列方式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| HORIZONTAL | 0 | 下载控件上图标和文字分布的方向为水平排列。 |
| VERTICAL | 1 | 下载控件上图标和文字分布的方向为垂直排列。 |

#### 事件

支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-events)。

#### 示例

```ts
// xxx.ets

import { picker } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { DownloadFileButton, DownloadLayoutDirection, DownloadIconStyle, DownloadDescription } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    Column() {
      DownloadFileButton({
        contentOptions: {
          icon: DownloadIconStyle.FULL_FILLED,
          text: DownloadDescription.DOWNLOAD
        },
        styleOptions: {
          iconSize: '16vp',
          layoutDirection: DownloadLayoutDirection.HORIZONTAL,
          fontSize: '16vp',
          fontStyle: FontStyle.Normal,
          fontWeight: FontWeight.Medium,
          fontFamily: 'HarmonyOS Sans',
          fontColor: '#ffffffff',
          iconColor: '#ffffffff',
          textIconSpace: '4vp'
        }
      })
        .backgroundColor('#007dff')
        .borderStyle(BorderStyle.Dotted)
        .borderWidth(0)
        .borderRadius('24vp')
        .position({ x: 0, y: 0 })
        .markAnchor({ x: 0, y: 0 })
        .offset({ x: 0, y: 0 })
        .constraintSize({})
        .padding({
          top: '12vp',
          bottom: '12vp',
          left: '24vp',
          right: '24vp'
        })
        .onClick(() => {
          this.downloadAction();
        })
    }
  }

  downloadAction() {
    try {
      const document = new picker.DocumentSaveOptions();
      document.pickerMode = picker.DocumentPickerMode.DOWNLOAD;
      new picker.DocumentViewPicker().save(document, (err: BusinessError, result: Array<string>) => {
        if (err) {
          return;
        }
        console.info(`downloadAction result:  ${JSON.stringify(result)}`);
      });
    } catch (e) {
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/Wi3TAYeTSS2W_lkNrPCaVQ/zh-cn_image_0000002568900755.png?HW-CC-KV=V1&HW-CC-Date=20260417T014802Z&HW-CC-Expire=86400&HW-CC-Sign=1F4910B7167D080168947438507EFC0604F4D9284A683E6AB43E429137800D60)

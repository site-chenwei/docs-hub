---
title: "Hyperlink"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-hyperlink"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "ArkTS组件"
  - "文本与输入"
  - "Hyperlink"
captured_at: "2026-04-17T01:47:57.322Z"
---

# Hyperlink

超链接组件，组件宽高范围内点击实现跳转。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/UHWnyUxzRpeKSJ7U0V7a0g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=3C8D64A7111625652E9D3A1F0D49CEC5B3A44D95985350213EDB677329BF9C43)

-   该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
-   该组件仅支持与系统浏览器配合使用。

#### 需要权限

跳转的目标应用使用网络时，需要申请权限ohos.permission.INTERNET。具体申请方式请参考[声明权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/declare-permissions)。

#### 子组件

可以包含[Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image)子组件。

#### 接口

Hyperlink(address: string | Resource, content?: string | Resource)

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| address | string | [Resource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resource) | 是 | Hyperlink组件跳转的网页。 |
| content | string | [Resource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resource) | 否 | 
Hyperlink组件中超链接显示文本。

**说明：**

组件内有子组件时，不显示超链接文本。

 |

#### 属性

除支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)外，还支持以下属性：

#### \[h2\]color

color(value: Color | number | string | Resource)

设置超链接文本的颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| value | [Color](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#color) | number | string | [Resource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resource) | 是 | 
超链接文本的颜色。

phone默认值为'#ff007dff'，wearable设备默认值'#1F71FF'，tv设备默认值为'#266EFB'，均显示为蓝色。

 |

#### 示例

该示例展示了超链接图片和文本跳转的效果。

```ts
@Entry
@Component
struct HyperlinkExample {
  build() {
    Column() {
      Column() {
        Hyperlink('https://example.com/') {
          // $r('app.media.bg')需要替换为开发者所需的图像资源文件。
          Image($r('app.media.bg'))
            .width(200)
            .height(100)
        }
      }

      Column() {
        Hyperlink('https://example.com/', 'Go to the developer website') {
        }
        .color(Color.Blue)
      }
    }.width('100%').height('100%').justifyContent(FlexAlign.Center)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/TKMAaFO8RSeYeu-BGeVFQA/zh-cn_image_0000002569020481.png?HW-CC-KV=V1&HW-CC-Date=20260417T014759Z&HW-CC-Expire=86400&HW-CC-Sign=BE8B1BC21FAC7D442C63C034CBBF1D97F6F95A4568F7C197699D1C0B22518A05)

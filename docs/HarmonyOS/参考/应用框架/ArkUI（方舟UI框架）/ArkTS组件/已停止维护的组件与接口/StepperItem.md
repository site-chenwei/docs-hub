---
title: "StepperItem"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-stepperitem"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "ArkTS组件"
  - "已停止维护的组件与接口"
  - "StepperItem"
captured_at: "2026-04-17T01:48:00.348Z"
---

# StepperItem

用作[Stepper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-stepper)组件的页面子组件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/xxxVAy30S7y-gmYODeKvcw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014802Z&HW-CC-Expire=86400&HW-CC-Sign=7CCA719F305422913C61C0F7A672D8373D6B4E2C4981B0BFDE8EC15DE31D19ED)

-   从API version 8开始支持，从API version 22开始废弃，建议使用[Swiper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper)替代。
    
-   该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
    

#### 子组件

支持单个子组件。

#### 接口

StepperItem()

创建[Stepper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-stepper)组件的页面子组件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/sBDl0AtLQ_SaX4UFWl2iKw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014802Z&HW-CC-Expire=86400&HW-CC-Sign=578E0122606F15D72C95B8005F80095C272A02AEFDB54A9A89C2E33555CAB42C)

从API version 8开始支持，从API version 22开始废弃，建议使用[Swiper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#属性)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### 属性

#### \[h2\]prevLabel(deprecated)

prevLabel(value: string)

设置左侧文本按钮内容，第一页没有左侧文本按钮，当步骤导航器大于一页时，除第一页外默认值都为“返回”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/GoA4_pZrRy2O0GEro0Df_w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014802Z&HW-CC-Expire=86400&HW-CC-Sign=199EE6900D4600DEC4D5404462AAB8336C266527F815675F9D2A035587CF69AB)

从API version 8开始支持，从API version 22开始废弃，建议使用[showPrevious](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#showprevious)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| value | string | 是 | 左侧文本按钮内容。字符串超长时，先缩小再换行（2行）最后截断。 |

#### \[h2\]nextLabel(deprecated)

nextLabel(value: string)

设置右侧文本按钮内容，最后一页默认值为“开始”，其余页默认值为“下一步”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/VCoyM-umT5KzRVacMdFlVA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014802Z&HW-CC-Expire=86400&HW-CC-Sign=27CC5FBF64A508D4C485739B0C566EFA51FF6EC100BA82078E076A1053A74DF8)

从API version 8开始支持，从API version 22开始废弃，建议使用[showNext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#shownext)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| value | string | 是 | 右侧文本按钮内容。字符串超长时，先缩小再换行（2行）最后截断。 |

#### \[h2\]status(deprecated)

status(value?: ItemState)

设置步骤导航器nextLabel的显示状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/Shno_8A3TqqqlZAdEI-qUA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014802Z&HW-CC-Expire=86400&HW-CC-Sign=7E00AAE0C9DC93A4AF1171EF221B432DAC060EF1D1EF518A297D150A2943CCC2)

从API version 8开始支持，从API version 22开始废弃，建议使用[indicatorInteractive](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#indicatorinteractive12)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| value | [ItemState](#itemstate枚举说明) | 否 | 
步骤导航器nextLabel的显示状态。

默认值：ItemState.Normal

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/0eGZoxh4Rl24oMAIdl0yBw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014802Z&HW-CC-Expire=86400&HW-CC-Sign=0DC4895CDA7ADF30891C60803EB2369BF3B7AEF4749B765E9A376905C9BF9EDD)

-   StepperItem组件不支持设置通用宽度属性，其宽度默认撑满Stepper父组件。
-   StepperItem组件不支持设置通用高度属性，其高度由Stepper父组件高度减去label按钮组件高度。
-   StepperItem组件不支持设置[aspectRatio](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-layout-constraints#aspectratio)/[constraintSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#constraintsize)影响长宽的属性。

#### ItemState枚举说明

步骤导航器nextLabel的显示状态。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| Normal | 0 | 
正常状态，右侧文本按钮正常显示，可点击进入下一个StepperItem。

**说明：**

从API version 8开始支持，从API version 22开始废弃，建议使用[index](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#index)替代。

 |
| Disabled | 1 | 

不可用状态，右侧文本按钮灰度显示，不可点击进入下一个StepperItem。

**说明：**

从API version 8开始支持，从API version 22开始废弃，建议使用[indicatorInteractive](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#indicatorinteractive12)替代。

 |
| Waiting | 2 | 

等待状态，右侧文本按钮不显示，显示等待进度条，不可点击进入下一个StepperItem。

**说明：**

从API version 8开始支持，从API version 22开始废弃，建议使用[Swiper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper)替代。

 |
| Skip | 3 | 

跳过状态，右侧文本按钮默认显示“跳过”，此时可在Stepper的onSkip回调中自定义相关逻辑。

**说明：**

从API version 8开始支持，从API version 22开始废弃，建议使用[index](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#index)替代。

 |

#### 示例

见[Stepper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-stepper)。

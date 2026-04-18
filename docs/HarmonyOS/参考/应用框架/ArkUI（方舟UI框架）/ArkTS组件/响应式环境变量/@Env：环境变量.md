---
title: "@Env：环境变量"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-env-system-property"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "ArkTS组件"
  - "响应式环境变量"
  - "@Env：环境变量"
captured_at: "2026-04-17T01:48:00.099Z"
---

# @Env：环境变量

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/R47wKQesTxyFr4DPgTkubQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014802Z&HW-CC-Expire=86400&HW-CC-Sign=DEDBDD612CF44A6A1C35DCB30523F5957676B7929197F6C497BBFCFF15A3EB42)

本模块首批接口从API version 22开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

开发者指南见：[@Env开发者指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-env-system-property)。

#### @Env

Env: EnvDecorator

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 说明 |
| :-- | :-- | :-- |
| Env | [EnvDecorator](#envdecorator) | 环境变量装饰器。 |

**示例：**

```ts
import { uiObserver } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @Env(SystemProperties.BREAK_POINT) breakpoint: uiObserver.WindowSizeLayoutBreakpointInfo;

  build() {}
}
```

#### EnvDecorator

type EnvDecorator = (value: SystemProperties) => PropertyDecorator

定义@Env装饰器类型。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| value | [SystemProperties](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-env-system-property#systemproperties) | 是 | 环境变量属性名。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| PropertyDecorator | 属性装饰器。 |

**错误码：**

详细介绍请参见[环境变量错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-env)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 140000 | Invalid key for @Env |

#### SystemProperties

定义环境变量枚举值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| BREAK\_POINT | 'system.arkui.breakpoint' | 
[@Env](#env)变量参数，通过@Env(SystemProperties.BREAK\_POINT)可获取[WindowSizeLayoutBreakpointInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-observer#windowsizelayoutbreakpointinfo22)实例。

当该装饰器声明在[@Component](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-create-custom-components#component)或[@ComponentV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-create-custom-components#componentv2)中时，用于获取当前自定义组件所在窗口的尺寸布局断点信息。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

 |
| WINDOW\_SIZE23+ | 'system.window.size' | 

[@Env](#env)变量参数，通过@Env(SystemProperties.WINDOW\_SIZE)可获取[SizeInVP](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-i#sizeinvp23)实例。

当该装饰器声明在[@Component](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-create-custom-components#component)或[@ComponentV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-create-custom-components#componentv2)中时，用于获取当前自定义组件所在窗口的大小信息，单位为vp。

**模型约束**：此接口仅可在Stage模型下使用。

 |
| WINDOW\_SIZE\_PX23+ | 'system.window.size.px' | 

[@Env](#env)变量参数，通过@Env(SystemProperties.WINDOW\_SIZE\_PX)可获取[Size](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-i#size7)实例。

当该装饰器声明在[@Component](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-create-custom-components#component)或[@ComponentV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-create-custom-components#componentv2)中时，用于获取当前自定义组件所在窗口的大小信息，单位为px。

**模型约束**：此接口仅可在Stage模型下使用。

 |
| WINDOW\_AVOID\_AREA23+ | 'system.window.avoidarea' | 

[@Env](#env)变量参数，通过@Env(SystemProperties.WINDOW\_AVOID\_AREA)可获取[UIEnvWindowAvoidAreaInfoVP](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-i#uienvwindowavoidareainfovp23)实例。

当该装饰器声明在[@Component](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-create-custom-components#component)或[@ComponentV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-create-custom-components#componentv2)中时，用于获取当前自定义组件所在窗口的避让区域信息，单位为vp。

**模型约束**：此接口仅可在Stage模型下使用。

 |
| WINDOW\_AVOID\_AREA\_PX23+ | 'system.window.avoidarea.px' | 

[@Env](#env)变量参数，通过@Env(SystemProperties.WINDOW\_AVOID\_AREA\_PX)可获取[UIEnvWindowAvoidAreaInfoPX](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-i#uienvwindowavoidareainfopx23)实例。

当该装饰器声明在[@Component](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-create-custom-components#component)或[@ComponentV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-create-custom-components#componentv2)中时，用于获取当前自定义组件所在窗口的避让区域信息，单位为px。

**模型约束**：此接口仅可在Stage模型下使用。

 |

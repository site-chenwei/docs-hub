---
title: "@ohos.app.ability.ConfigurationConstant (环境变量相关的常量定义)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-configurationconstant"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "通用能力的接口(推荐)"
  - "@ohos.app.ability.ConfigurationConstant (环境变量相关的常量定义)"
captured_at: "2026-04-17T01:47:47.084Z"
---

# @ohos.app.ability.ConfigurationConstant (环境变量相关的常量定义)

ConfigurationConstant模块提供了[Configuration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-configuration)操作相关的系统预置枚举。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/VMpEUhgJR7mJc164RHhVoQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=C7337308A3FC206206B27859F9BB31F9C6768CF170D5A5AE8E9707CFBB26BE5C)

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import { ConfigurationConstant } from '@kit.AbilityKit';
```

#### ColorMode

表示深浅色模式的枚举，用于[Configuration.colorMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-configuration#configuration)字段。开发者可以使用这些预置枚举设置或获取系统/应用的深浅色模式。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityBase

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| COLOR\_MODE\_NOT\_SET | \-1 | 表示未设置颜色模式。 |
| COLOR\_MODE\_DARK | 0 | 表示深色模式。 |
| COLOR\_MODE\_LIGHT | 1 | 表示浅色模式。 |

#### Direction

表示屏幕方向的枚举，用于[Configuration.direction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-configuration#configuration)字段。开发者可以使用这些预置枚举设置或获取系统/应用的显示方向。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityBase

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| DIRECTION\_NOT\_SET | \-1 | 表示未设置方向。 |
| DIRECTION\_VERTICAL | 0 | 表示垂直方向。 |
| DIRECTION\_HORIZONTAL | 1 | 表示水平方向。 |

#### ScreenDensity

表示屏幕像素密度的枚举，用于[Configuration.screenDensity](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-configuration#configuration)字段。开发者可以使用这些预置枚举设置或获取屏幕的像素密度。

字体显示大小与屏幕像素密度呈正相关关系。通过监听屏幕像素密度变化，可以感知字体显示大小的调整。通常情况下，对于相同的物理尺寸，屏幕像素密度越高，字体显示效果越大。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityBase

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| SCREEN\_DENSITY\_NOT\_SET | 0 | 表示未设置屏幕像素密度。 |
| SCREEN\_DENSITY\_SDPI | 120 | 表示屏幕像素密度为'SDPI'。 |
| SCREEN\_DENSITY\_MDPI | 160 | 表示屏幕像素密度为'MDPI'。 |
| SCREEN\_DENSITY\_LDPI | 240 | 表示屏幕像素密度为'LDPI'。 |
| SCREEN\_DENSITY\_XLDPI | 320 | 表示屏幕像素密度为'XLDPI'。 |
| SCREEN\_DENSITY\_XXLDPI | 480 | 表示屏幕像素密度为'XXLDPI'。 |
| SCREEN\_DENSITY\_XXXLDPI | 640 | 表示屏幕像素密度为'XXXLDPI'。 |

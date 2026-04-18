---
title: "@ohos.app.ability.Configuration (环境变量)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-configuration"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "通用能力的接口(推荐)"
  - "@ohos.app.ability.Configuration (环境变量)"
captured_at: "2026-04-17T01:47:47.044Z"
---

# @ohos.app.ability.Configuration (环境变量)

定义了应用运行时的环境变量，包含语言、深浅色、屏幕方向、字体等。开发者可以通过订阅环境变量，适配不同用户偏好，提升交互体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/_G1_0ipoRb2UUHqp3MKn8Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=F8758B664AC1704E41648B2F14DE82D33DCF8E5AE4D3C4FCBDE77CCE70545BD1)

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import { Configuration } from '@kit.AbilityKit';
```

#### Configuration

**系统能力**：SystemCapability.Ability.AbilityBase

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| language | string | 否 | 是 | 
表示应用当前语言，例如“zh"(中文)，“en”（英文）。

支持开发者[设置应用语言](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/subscribe-system-environment-variable-changes#设置应用语言)。

取值范围参考[获取系统支持的语言列表](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-i18n#getsystemlanguages9)。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

 |
| colorMode | [ConfigurationConstant.ColorMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-configurationconstant#colormode) | 否 | 是 | 

表示应用深浅色模式，默认为浅色。

支持开发者[设置应用或组件深浅色](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/subscribe-system-environment-variable-changes#设置深浅色模式)。

取值范围：

\- COLOR\_MODE\_NOT\_SET：未设置

\- COLOR\_MODE\_LIGHT：浅色模式

\- COLOR\_MODE\_DARK：深色模式

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

 |
| direction | [ConfigurationConstant.Direction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-configurationconstant#direction) | 否 | 是 | 

表示应用屏幕方向。

取值范围：

\- DIRECTION\_NOT\_SET：未设置

\- DIRECTION\_HORIZONTAL：水平方向

\- DIRECTION\_VERTICAL：垂直方向

该环境变量支持在[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)组件和[UIExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiextensionability)组件中订阅，不支持在[ApplicationContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-applicationcontext)和[AbilityStage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-abilitystage)组件容器中订阅。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

 |
| screenDensity | [ConfigurationConstant.ScreenDensity](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-configurationconstant#screendensity) | 否 | 是 | 

表示屏幕显示密度。

取值范围：

\- SCREEN\_DENSITY\_NOT\_SET：未设置

\- SCREEN\_DENSITY\_SDPI：120

\- SCREEN\_DENSITY\_MDPI：160

\- SCREEN\_DENSITY\_LDPI：240

\- SCREEN\_DENSITY\_XLDPI：320

\- SCREEN\_DENSITY\_XXLDPI：480

\- SCREEN\_DENSITY\_XXXLDPI：640

字体显示大小与屏幕像素密度呈正相关关系。通过监听屏幕像素密度变化，可以感知字体显示大小的调整。通常情况下，对于相同的物理尺寸，屏幕像素密度越高，字体显示效果越大。

该环境变量支持在[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)组件和[UIExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiextensionability)组件中订阅，不支持在[ApplicationContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-applicationcontext)和[AbilityStage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-abilitystage)组件容器中订阅。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

 |
| displayId | number | 否 | 是 | 

表示应用所在的物理屏幕ID。

该环境变量支持在[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)组件和[UIExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiextensionability)组件中订阅，不支持在[ApplicationContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-applicationcontext)和[AbilityStage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-abilitystage)组件容器中订阅。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

 |
| hasPointerDevice | boolean | 否 | 是 | 

表示指针设备是否已连接，如键鼠、触控板等。true表示设备已连接，false表示设备未连接。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

 |
| fontId14+ | string | 否 | 是 | 

表示应用字体的唯一ID。

**元服务API**：从API version 14开始，该接口支持在元服务中使用。

 |
| fontSizeScale12+ | number | 否 | 是 | 

表示字体大小缩放比例，取值为非负数，默认值为1。

支持开发者[设置应用字体大小](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/subscribe-system-environment-variable-changes#设置字体大小)。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

 |
| fontWeightScale12+ | number | 否 | 是 | 

表示字体粗细缩放比例，取值为非负数，默认值为1。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

 |
| mcc12+ | string | 否 | 是 | 

表示移动设备国家代码。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

 |
| mnc12+ | string | 否 | 是 | 

表示移动设备网络代码。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

 |
| locale20+ | [Intl.Locale](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale) | 否 | 是 | 

表示区域设置。

应用会根据当前的区域设置自动调整其行为，以符合用户的本地化需求。该属性可以通过设置系统语言、设置系统地区和设置应用偏好语言等方式设置。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

 |

**示例：**

```ts
import { UIAbility, AbilityConstant, EnvironmentCallback, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    let envCallback: EnvironmentCallback = {
      onConfigurationUpdated(config) {
        console.info(`envCallback onConfigurationUpdated success: ${JSON.stringify(config)}`);
        let language = config.language;
        let colorMode = config.colorMode;
        let direction = config.direction;
        let screenDensity = config.screenDensity;
        let displayId = config.displayId;
        let hasPointerDevice = config.hasPointerDevice;
        let fontId = config.fontId;
        let fontSizeScale = config.fontSizeScale;
        let fontWeightScale = config.fontWeightScale;
        let mcc = config.mcc;
        let mnc = config.mnc;
        let locale = config.locale;
      },
      onMemoryLevel(level) {
        console.info(`onMemoryLevel level: ${level}`);
      }
    };
    try {
      let applicationContext = this.context.getApplicationContext();
      let callbackId = applicationContext.on('environment', envCallback);
      console.info(`callbackId: ${callbackId}`);
    } catch (paramError) {
      console.error(`error: ${(paramError as BusinessError).code}, ${(paramError as BusinessError).message}`);
    }
  }
}
```

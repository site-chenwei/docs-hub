---
title: "@ohos.uiAppearance (用户界面外观)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-uiappearance"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "ArkTS API"
  - "UI界面"
  - "@ohos.uiAppearance (用户界面外观)"
captured_at: "2026-04-17T01:47:53.329Z"
---

# @ohos.uiAppearance (用户界面外观)

用户界面外观提供获取系统外观的一些基础能力，包括获取深浅色模式、字体大小缩放比例、字体粗细缩放比例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/M6NjD_vTQ0m0NVVNfN3jow/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=D5DFA18285D56B6AB99FB3159AE71FAFCAF9083CEF03085747B62E7A8684B8BC)

从API version 20开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

#### 导入模块

```ts
import { uiAppearance } from '@kit.ArkUI';
```

#### DarkMode

深色模式枚举。

**系统能力：** SystemCapability.ArkUI.UiAppearance

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| ALWAYS\_DARK | 0 | 系统始终为深色。 |
| ALWAYS\_LIGHT | 1 | 系统始终为浅色。 |

#### uiAppearance.getDarkMode

getDarkMode(): DarkMode

获取系统当前的深色模式配置。

**系统能力**：SystemCapability.ArkUI.UiAppearance

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [DarkMode](#darkmode) | 系统当前的深色模式配置。 |

**错误码：**

错误码详细介绍请参考[用户界面外观服务错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uiappearance)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 500001 | Internal error. |

**示例：**

```ts
import { uiAppearance } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let darkMode = uiAppearance.getDarkMode();
  console.info('Get dark-mode ' + darkMode);
} catch (error) {
  let message = (error as BusinessError).message;
  console.error('Get dark-mode failed, ' + message);
}
```

#### uiAppearance.getFontScale

getFontScale(): number

获取系统当前的字体大小缩放比例。

**系统能力**：SystemCapability.ArkUI.UiAppearance

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 系统当前的字体大小缩放比例。 |

**错误码：**

错误码详细介绍请参考[用户界面外观服务错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uiappearance)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 500001 | Internal error. |

**示例：**

```ts
import { uiAppearance } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let fontScale = uiAppearance.getFontScale();
  console.info('Get fontScale ' + fontScale);
} catch (error) {
  let message = (error as BusinessError).message;
  console.error('Get fontScale failed, ' + message);
}
```

#### uiAppearance.getFontWeightScale

getFontWeightScale(): number

获取系统当前的字体粗细缩放比例。

**系统能力**：SystemCapability.ArkUI.UiAppearance

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 系统当前的字体粗细缩放比例。 |

**错误码：**

错误码详细介绍请参考[用户界面外观服务错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uiappearance)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 500001 | Internal error. |

**示例：**

```ts
import { uiAppearance } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let fontWeightScale = uiAppearance.getFontWeightScale();
  console.info('Get fontScale ' + fontWeightScale);
} catch (error) {
  let message = (error as BusinessError).message;
  console.error('Get fontWeightScale failed, ' + message);
}
```

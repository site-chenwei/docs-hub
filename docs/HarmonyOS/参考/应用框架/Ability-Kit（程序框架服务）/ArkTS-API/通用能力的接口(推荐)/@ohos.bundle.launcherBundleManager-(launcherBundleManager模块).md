---
title: "@ohos.bundle.launcherBundleManager (launcherBundleManager模块)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-launcherbundlemanager"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "通用能力的接口(推荐)"
  - "@ohos.bundle.launcherBundleManager (launcherBundleManager模块)"
captured_at: "2026-04-17T01:47:47.258Z"
---

# @ohos.bundle.launcherBundleManager (launcherBundleManager模块)

本模块支持launcher应用（桌面有图标的应用）所需的查询能力，支持[LauncherAbilityInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-launcherabilityinfo)信息的查询。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/_5eEdCfORJO9exyxXLN8JQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=3F714719D114ABF7F27DB1D8B0A0FC720452504D52DBA010AE5E16BE3FB7D93C)

本模块首批接口从API version 18开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import { launcherBundleManager } from '@kit.AbilityKit';
```

#### launcherBundleManager.getLauncherAbilityInfoSync

getLauncherAbilityInfoSync(bundleName: string, userId: number) : Array<[LauncherAbilityInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-launcherabilityinfo)\>

查询指定bundleName及用户的[LauncherAbilityInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-launcherabilityinfo)。

**需要权限：** ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED

**系统能力：** SystemCapability.BundleManager.BundleFramework.Launcher

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| bundleName | string | 是 | 应用Bundle名称。 |
| userId | number | 是 | 被查询的用户ID，可以通过[getOsAccountLocalId接口](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-osaccount#getosaccountlocalid9)获取。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Array<[LauncherAbilityInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-launcherabilityinfo)\> | Array形式返回bundle包含的[LauncherAbilityInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-launcherabilityinfo)信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[ohos.bundle错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bundle)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Verify permission denied. |
| 801 | Capability not support. |
| 17700001 | The specified bundle name is not found. |
| 17700004 | The specified user ID is not found. |

**示例：**

```ts
import { launcherBundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = launcherBundleManager.getLauncherAbilityInfoSync("com.example.demo", 100);
  console.info("data is " + JSON.stringify(data));
} catch (errData) {
  let code = (errData as BusinessError).code;
  let message = (errData as BusinessError).message;
  console.error(`errData is errCode:${code}  message:${message}`);
}
```

#### LauncherAbilityInfo

type LauncherAbilityInfo = \_LauncherAbilityInfo

LauncherAbilityInfo信息。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Launcher

| 类型 | 说明 |
| :-- | :-- |
| [\_LauncherAbilityInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-launcherabilityinfo) | 桌面应用的Ability信息。 |

#### ShortcutInfo20+

type ShortcutInfo = \_ShortcutInfo

应用[module.json5配置文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file#shortcuts标签)中定义的快捷方式信息。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Launcher

| 类型 | 说明 |
| :-- | :-- |
| [\_ShortcutInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-shortcutinfo#shortcutinfo-1) | 应用module.json5配置文件中定义的快捷方式信息。 |

#### ShortcutWant20+

type ShortcutWant = \_ShortcutWant

快捷方式内定义的目标[wants](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file#wants标签)信息集合。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Launcher

| 类型 | 说明 |
| :-- | :-- |
| [\_ShortcutWant](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-shortcutinfo#shortcutwant) | 快捷方式内定义的目标[wants](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file#wants标签)信息集合。 |

#### ParameterItem20+

type ParameterItem = \_ParameterItem

快捷方式配置信息中的自定义数据。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Launcher

| 类型 | 说明 |
| :-- | :-- |
| [\_ParameterItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-shortcutinfo#parameteritem) | 快捷方式配置信息中的自定义数据。 |

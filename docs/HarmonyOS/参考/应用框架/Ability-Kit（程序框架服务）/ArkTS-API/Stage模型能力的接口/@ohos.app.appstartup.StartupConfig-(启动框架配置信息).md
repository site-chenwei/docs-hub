---
title: "@ohos.app.appstartup.StartupConfig (启动框架配置信息)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-appstartup-startupconfig"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "Stage模型能力的接口"
  - "@ohos.app.appstartup.StartupConfig (启动框架配置信息)"
captured_at: "2026-04-17T01:47:46.592Z"
---

# @ohos.app.appstartup.StartupConfig (启动框架配置信息)

本模块提供[应用启动框架](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-startup)配置信息的定义。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/nG6NxkvMTR-wUE0hGqvz8g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=5C2F78BE7BF892FD33771F9C596EBB3C55F64608E9601FFBA3BAA36F803FCE05)

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 导入模块

```js
import { StartupConfig } from '@kit.AbilityKit';
```

#### StartupConfig

用于配置任务超时时间和启动框架的监听器。详细使用方法可参考[设置启动参数](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-startup#设置启动参数)章节。

**系统能力**：SystemCapability.Ability.AppStartup

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| timeoutMs | number | 否 | 是 | 执行所有启动任务的超时时间（单位：毫秒），默认值为10000毫秒。 |
| startupListener | [StartupListener](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-appstartup-startuplistener) | 否 | 是 | 表示启动框架的监听器，该监听器将在所有启动任务完成时调用。 |

**示例：**

```ts
import { StartupConfig, StartupConfigEntry, StartupListener } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class MyStartupConfigEntry extends StartupConfigEntry {
  onConfig() {
    hilog.info(0x0000, 'testTag', `onConfig`);
    let onCompletedCallback = (error: BusinessError<void>) => {
      hilog.info(0x0000, 'testTag', `onCompletedCallback`);
      if (error) {
        hilog.error(0x0000, 'testTag', 'onCompletedCallback: %{public}d, message: %{public}s', error.code,
          error.message);
      } else {
        hilog.info(0x0000, 'testTag', `onCompletedCallback: success.`);
      }
    };
    let startupListener: StartupListener = {
      'onCompleted': onCompletedCallback
    };
    let config: StartupConfig = {
      'timeoutMs': 10000,
      'startupListener': startupListener
    };
    return config;
  }
}
```

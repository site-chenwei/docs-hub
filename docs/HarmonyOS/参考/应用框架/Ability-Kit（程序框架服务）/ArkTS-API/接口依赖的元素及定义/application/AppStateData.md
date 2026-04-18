---
title: "AppStateData"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-appstatedata"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "接口依赖的元素及定义"
  - "application"
  - "AppStateData"
captured_at: "2026-04-17T01:47:47.535Z"
---

# AppStateData

定义应用状态信息，使用接口[on](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-appmanager#appmanageronapplicationstate14)注册应用状态变化监听后，当应用、进程或组件的状态变化时，系统通过[ApplicationStateObserver](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-applicationstateobserver)的[onForegroundApplicationChanged](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-applicationstateobserver#applicationstateobserveronforegroundapplicationchanged)等方法回调给开发者。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/lj0_ClFpRPOMlFBE1cKfrQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=F26271B423841BA3A30C2B55D02F2C6EE8ACBAE60328202BF540BB094BA7A0AC)

本模块首批接口从API version 14 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import { appManager } from '@kit.AbilityKit';
```

#### 属性

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| bundleName | string | 否 | 否 | Bundle名称。 |
| uid | number | 否 | 否 | 应用程序的uid。 |
| state | number | 否 | 否 | 
应用状态。

0：初始化状态，应用正在初始化

1：就绪状态，应用已初始化完毕

2：前台状态，应用位于前台

3：获焦状态。（预留状态，当前暂不支持）

4：后台状态，应用位于后台

5：退出状态，应用已退出

 |
| isSplitScreenMode | boolean | 否 | 否 | 

判断应用是否处于分屏模式。

true:应用处于分屏模式。

false:应用不处于分屏模式。

 |
| isFloatingWindowMode | boolean | 否 | 否 | 

判断应用是否处于悬浮窗模式。

true:应用处于悬浮窗模式。

false:应用不处于悬浮窗模式。

 |

**示例：**

```ts
import { appManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let applicationStateObserver: appManager.ApplicationStateObserver = {
  onForegroundApplicationChanged(appStateData: appManager.AppStateData) {
    console.info(`[appManager] onForegroundApplicationChanged: ${JSON.stringify(appStateData)}`);
    console.info(`appStateData.bundleName: ${appStateData.bundleName}`);
    console.info(`appStateData.uid: ${appStateData.uid}`);
    console.info(`appStateData.state: ${appStateData.state}`);
    console.info(`appStateData.isSplitScreenMode: ${appStateData.isSplitScreenMode}`);
    console.info(`appStateData.isFloatingWindowMode: ${appStateData.isFloatingWindowMode}`);
  },
  onAbilityStateChanged(abilityStateData: appManager.AbilityStateData) {
    console.info(`[appManager] onAbilityStateChanged: ${JSON.stringify(abilityStateData)}`);
  },
  onProcessCreated(processData: appManager.ProcessData) {
    console.info(`[appManager] onProcessCreated: ${JSON.stringify(processData)}`);
  },
  onProcessDied(processData: appManager.ProcessData) {
    console.info(`[appManager] onProcessDied: ${JSON.stringify(processData)}`);
  },
  onProcessStateChanged(processData: appManager.ProcessData) {
    console.info(`[appManager] onProcessStateChanged: ${JSON.stringify(processData)}`);
  },
  onAppStarted(appStateData: appManager.AppStateData) {
    console.info(`[appManager] onAppStarted: ${JSON.stringify(appStateData)}`);
  },
  onAppStopped(appStateData: appManager.AppStateData) {
    console.info(`[appManager] onAppStopped: ${JSON.stringify(appStateData)}`);
  }
};

try {
  const observerId = appManager.on('applicationState', applicationStateObserver);
  console.info(`[appManager] observerCode: ${observerId}`);
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`[appManager] error code: ${code}, error msg: ${message}`);
}
```

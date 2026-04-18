---
title: "@ohos.app.ability.EnvironmentCallback (系统环境变化监听器)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-environmentcallback"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "Stage模型能力的接口"
  - "@ohos.app.ability.EnvironmentCallback (系统环境变化监听器)"
captured_at: "2026-04-17T01:47:46.363Z"
---

# @ohos.app.ability.EnvironmentCallback (系统环境变化监听器)

EnvironmentCallback模块提供对系统环境变化监听回调的能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/7M5DBmB3R-uriHK_QRpUMg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014747Z&HW-CC-Expire=86400&HW-CC-Sign=BB56BC69A2581DADC0877EEDF3865121B6B969073CE5F4B0466B94CA28E55663)

本模块首批接口从API version 9 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ts
import { EnvironmentCallback } from '@kit.AbilityKit';
```

#### EnvironmentCallback

#### \[h2\]onConfigurationUpdated

onConfigurationUpdated(config: Configuration): void

[注册系统环境变化的监听](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-applicationcontext#applicationcontextonenvironment)后，在系统环境变化时触发回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| config | [Configuration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-configuration) | 是 | 变化后的Configuration对象。 |

**示例：**

参见[EnvironmentCallback使用](#environmentcallback使用)。

#### \[h2\]onMemoryLevel

onMemoryLevel(level: AbilityConstant.MemoryLevel): void

[注册系统环境变化的监听](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-applicationcontext#applicationcontextonenvironment)后，在系统内存变化时触发回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/ovVkzUp-S_q7LDfRKCfy-A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014747Z&HW-CC-Expire=86400&HW-CC-Sign=3E83399F6B4F98406F3493D6269D8FA5B83FBB26419CF21FC17960ACA2736B84)

onMemoryLevel回调运行在当前进程的主线程中，如果在该回调中做耗时的UI组件释放，会阻塞主线程任务，因此不建议在该回调中释放UI组件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| level | [AbilityConstant.MemoryLevel](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-abilityconstant#memorylevel) | 是 | 整机可用内存级别，对应的触发场景详见[AbilityConstant.MemoryLevel](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-abilityconstant#memorylevel)。 |

**示例：**

参见[EnvironmentCallback使用](#environmentcallback使用)。

#### EnvironmentCallback使用

**示例：**

```ts
import { UIAbility, EnvironmentCallback } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let callbackId: number;

export default class MyAbility extends UIAbility {
  onCreate() {
    console.info('MyAbility onCreate');
    let environmentCallback: EnvironmentCallback  =  {
      onConfigurationUpdated(config){
        console.info(`onConfigurationUpdated config: ${JSON.stringify(config)}`);
      },

      onMemoryLevel(level){
        console.info(`onMemoryLevel level: ${JSON.stringify(level)}`);
      }
    };
    // 1.获取applicationContext
    let applicationContext = this.context.getApplicationContext();
    try {
      // 2.通过applicationContext注册监听应用内生命周期
      callbackId = applicationContext.on('environment', environmentCallback);
    } catch (paramError) {
      console.error(`error: ${(paramError as BusinessError).code}, ${(paramError as BusinessError).message}`);
    }
    console.info(`registerEnvironmentCallback number: ${JSON.stringify(callbackId)}`);
  }

  onDestroy() {
    let applicationContext = this.context.getApplicationContext();
    try {
      applicationContext.off('environment', callbackId, (error, data) => {
        if (error && error.code !== 0) {
          console.error(`unregisterEnvironmentCallback fail, error: ${JSON.stringify(error)}`);
        } else {
          console.info(`unregisterEnvironmentCallback success, data: ${JSON.stringify(data)}`);
        }
      });
    } catch (paramError) {
      console.error(`error: ${(paramError as BusinessError).code}, ${(paramError as BusinessError).message}`);
    }
  }
}
```

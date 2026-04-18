---
title: "ProcessInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-app-processinfo"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "FA模型能力的接口"
  - "app"
  - "ProcessInfo"
captured_at: "2026-04-17T01:47:46.934Z"
---

# ProcessInfo

定义进程信息，可以通过[getProcessInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-app-context#contextgetprocessinfo7)获取当前Ability运行的进程信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/j_vGUkpVTeaAwUuqCdVjtw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=959CF7BABE64E487533AFBFCBC465DD37DE69581D6091E95F7D81CE2637E0636)

本模块首批接口从API version 7开始支持，仅支持FA模型。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import featureAbility from '@ohos.ability.featureAbility';
```

#### 属性

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| pid | number | 否 | 否 | 进程ID。 |
| processName | string | 否 | 否 | 进程名称。 |

**示例：**

```ts
import featureAbility from '@ohos.ability.featureAbility';

let context = featureAbility.getContext();
context.getProcessInfo((error, data) => {
    if (error && error.code !== 0) {
        console.error(`getProcessInfo fail, error: ${JSON.stringify(error)}`);
    } else {
        console.info(`getProcessInfo success, data: ${JSON.stringify(data)}`);
        let pid = data.pid;
        let processName = data.processName;
    }
});
```

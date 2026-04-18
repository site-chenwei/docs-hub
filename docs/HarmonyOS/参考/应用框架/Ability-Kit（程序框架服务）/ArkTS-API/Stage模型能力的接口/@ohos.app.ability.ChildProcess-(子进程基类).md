---
title: "@ohos.app.ability.ChildProcess (子进程基类)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-childprocess"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "Stage模型能力的接口"
  - "@ohos.app.ability.ChildProcess (子进程基类)"
captured_at: "2026-04-17T01:47:46.202Z"
---

# @ohos.app.ability.ChildProcess (子进程基类)

开发者自定义子进程的基类。通过[childProcessManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-childprocessmanager)启动子进程时，需要继承此类并重写入口方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/kGyg6hFmTd67nc8KS5Dprg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014747Z&HW-CC-Expire=86400&HW-CC-Sign=A432B9CDFF5CCF6C0FBC839C0E1E3E47B755D6C06CA0FB9B36E2C9B03523D8FC)

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ts
import { ChildProcess } from '@kit.AbilityKit';
```

#### ChildProcess.onStart

onStart(args?: ChildProcessArgs): void

子进程的入口方法，通过[childProcessManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-childprocessmanager)启动子进程后调用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| args12+ | [ChildProcessArgs](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-childprocessargs) | 否 | 传递到子进程的参数。 |

**示例：**

```ts
import { ChildProcess, ChildProcessArgs } from '@kit.AbilityKit';

export default class DemoProcess extends ChildProcess {

  onStart(args?: ChildProcessArgs) {
    let entryParams = args?.entryParams;
    let fd = args?.fds?.key1;
    // ..
  }
}
```

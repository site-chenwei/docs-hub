---
title: "@ohos.app.ability.ChildProcessArgs (子进程参数)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-childprocessargs"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "Stage模型能力的接口"
  - "@ohos.app.ability.ChildProcessArgs (子进程参数)"
captured_at: "2026-04-17T01:47:46.239Z"
---

# @ohos.app.ability.ChildProcessArgs (子进程参数)

传递到子进程的参数。[childProcessManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-childprocessmanager)启动子进程时，可以通过ChildProcessArgs传递参数到子进程中。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/p_JH25JSTk2rUCCMglWvgA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014747Z&HW-CC-Expire=86400&HW-CC-Sign=0E69B526FCA3FE16C9A33F926040E73484EFB85B2EFFF79F6D32E7D7918C9D7A)

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ts
import { ChildProcessArgs } from '@kit.AbilityKit';
```

#### ChildProcessArgs

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| entryParams | string | 否 | 是 | 开发者自定义参数，透传到子进程中。可以在[ChildProcess.onStart](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-childprocess#childprocessonstart)方法中通过args.entryParams获取，entryParams支持传输的最大数据量为150KB。 |
| fds | Record<string, number> | 否 | 是 | 
文件描述符句柄集合，用于主进程和子进程通信，通过key-value的形式传入到子进程中，其中key为自定义字符串，value为文件描述符句柄。可以在[ChildProcess.onStart](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-childprocess#childprocessonstart)方法中通过args.fds获取fd句柄。

**说明：**

\- fds最多支持16组，每组key的最大长度为20字符。

\- 传递到子进程中句柄数字可能会变，但是指向的文件是一致的。

 |

**示例：**

示例中的context的获取方式请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
// 主进程中:
import { common, ChildProcessArgs, childProcessManager } from '@kit.AbilityKit';
import { fileIo } from '@kit.CoreFileKit';

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Text('Click')
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
            let path = context.filesDir + "/test.txt";
            let file = fileIo.openSync(path, fileIo.OpenMode.READ_ONLY | fileIo.OpenMode.CREATE);
            let args: ChildProcessArgs = {
              entryParams: "testParam",
              fds: {
                "key1": file.fd
              }
            };
            childProcessManager.startArkChildProcess("entry/./ets/process/DemoProcess.ets", args);
          });
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

```ts
// 子进程中:
import { ChildProcess, ChildProcessArgs } from '@kit.AbilityKit';

export default class DemoProcess extends ChildProcess {

  onStart(args?: ChildProcessArgs) {
    let entryParams = args?.entryParams;
    let fd = args?.fds?.key1;
    // ..
  }
}
```

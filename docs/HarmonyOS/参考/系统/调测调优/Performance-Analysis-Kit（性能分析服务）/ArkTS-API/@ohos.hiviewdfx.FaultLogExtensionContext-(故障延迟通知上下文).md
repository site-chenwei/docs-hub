---
title: "@ohos.hiviewdfx.FaultLogExtensionContext (故障延迟通知上下文)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiviewdfx-faultlogextensioncontext"
menu_path:
  - "参考"
  - "系统"
  - "调测调优"
  - "Performance Analysis Kit（性能分析服务）"
  - "ArkTS API"
  - "@ohos.hiviewdfx.FaultLogExtensionContext (故障延迟通知上下文)"
captured_at: "2026-04-17T01:48:34.582Z"
---

# @ohos.hiviewdfx.FaultLogExtensionContext (故障延迟通知上下文)

FaultLogExtensionContext是[FaultLogExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiviewdfx-faultlogextensionability)的上下文环境，继承自[ExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-extensioncontext)。

FaultLogExtensionContext模块提供访问[FaultLogExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiviewdfx-faultlogextensionability)的资源的能力，对于扩展的ExtensionAbility，可直接将ExtensionContext作为上下文环境，或者定义一个继承自ExtensionContext的类型作为上下文环境。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/tQQ4DgUTR9q83Qll-5Io1g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014836Z&HW-CC-Expire=86400&HW-CC-Sign=E5E553B58EC6041AAAA3E7EE8DB4F534A539494FA560DFDC390D9D21DD45C6C5)

-   本模块接口从API version 21开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
-   本模块接口仅可在Stage模型下使用。

#### 使用说明

通过FaultLogExtensionAbility子类实例来获取。

```ts
import { FaultLogExtensionAbility } from '@kit.PerformanceAnalysisKit';

export default class MyFaultLogExtension extends FaultLogExtensionAbility {
    onFaultReportReady() {
        let context = this.context; // 获取FaultLogExtensionContext
        console.info('cache dir is ' + context.cacheDir); // 访问context中的成员
    }
}
```

#### FaultLogExtensionContext

FaultLogExtensionContext是[FaultLogExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiviewdfx-faultlogextensionability)的上下文环境。

**系统能力**：SystemCapability.HiviewDFX.Hiview.FaultLogger

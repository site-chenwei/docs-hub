---
title: "@ohos.application.testRunner (TestRunner)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-testrunner"
menu_path:
  - "参考"
  - "系统"
  - "调测调优"
  - "Test Kit（应用测试服务）"
  - "ArkTS API"
  - "@ohos.application.testRunner (TestRunner)"
captured_at: "2026-04-17T01:48:35.456Z"
---

# @ohos.application.testRunner (TestRunner)

TestRunner模块提供了框架测试的能力。包括准备单元测试环境、运行测试用例。

如果您想实现自己的单元测试框架，您必须继承这个类并覆盖它的所有方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/P_zmq77iTUeP-XTINdt12g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=E7436D7AECCE81533192D1E00C7E6C7B6C9A9B0CC365B2BFD231DEF534D59A04)

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在[单元测试框架](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/unittest-guidelines)中使用。

#### 导入模块

```ts
import { TestRunner } from '@kit.TestKit';
```

#### TestRunner.onPrepare

onPrepare(): void

为运行测试用例准备单元测试环境。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**示例：**

```ts
import { TestRunner } from '@kit.TestKit';

export default class UserTestRunner implements TestRunner {
  onPrepare() {
    console.info('Trigger onPrepare');
  }

  onRun() {
  }
}
```

#### TestRunner.onRun

onRun(): void

运行测试用例。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**示例：**

```ts
import { TestRunner } from '@kit.TestKit';

export default class UserTestRunner implements TestRunner {
  onPrepare() {
  }

  onRun() {
    console.info('Trigger onRun');
  }
}
```

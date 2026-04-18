---
title: "@ohos.ability.errorCode (ErrorCode)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-ability-errorcode"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "已停止维护的接口"
  - "@ohos.ability.errorCode (ErrorCode)"
captured_at: "2026-04-17T01:47:48.108Z"
---

# @ohos.ability.errorCode (ErrorCode)

ErrorCode定义启动Ability时返回的错误码，包括无效的参数、权限拒绝等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/PyZt49e-Qg6LGhi_hnifew/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=C66E9A8220D7A29439608792F97F06C5756DC59579F7B9626D5B163B95C89A23)

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import { ErrorCode } from '@kit.AbilityKit';
```

#### ErrorCode

定义启动Ability时返回的错误码。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| NO\_ERROR | 0 | 启动成功，无错误。 |
| INVALID\_PARAMETER | \-1 | 无效的参数。 |
| ABILITY\_NOT\_FOUND | \-2 | 找不到Ability。 |
| PERMISSION\_DENY | \-3 | 权限拒绝。 |

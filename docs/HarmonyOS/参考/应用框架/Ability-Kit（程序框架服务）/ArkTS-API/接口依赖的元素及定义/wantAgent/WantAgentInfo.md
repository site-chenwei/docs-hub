---
title: "WantAgentInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-wantagent-wantagentinfo"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "接口依赖的元素及定义"
  - "wantAgent"
  - "WantAgentInfo"
captured_at: "2026-04-17T01:47:48.111Z"
---

# WantAgentInfo

定义触发WantAgent所需要的信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/4rmCPCQqTU6QV_duWet6GQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=8850350678D658CE6EE213FCD34256E3B57D2D0803B8BDA67B60C770F97D5931)

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import { wantAgent as abilityWantAgent } from '@kit.AbilityKit';
```

#### WantAgentInfo

定义触发WantAgent所需要的信息，可以作为[getWantAgent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-wantagent#wantagentgetwantagent)的入参创建指定的WantAgent对象。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| wants | Array<[Want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-want)\> | 否 | 否 | 
将被执行的动作列表。wants数组为预留能力，当前只支持一个want。传入多个时只取wants数组的第一个成员。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

 |
| operationType(deprecated) | [wantAgent.OperationType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wantagent#operationtype) | 否 | 是 | 

动作类型。

从API version 7 开始支持，从API version 11 开始废弃，建议使用actionType11+替代。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

 |
| actionType11+ | [abilityWantAgent.OperationType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-wantagent#operationtype) | 否 | 是 | 

动作类型。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

 |
| requestCode | number | 否 | 否 | 

开发者自定义的请求码，用于标识将被执行的动作。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

 |
| wantAgentFlags(deprecated) | Array<[wantAgent.WantAgentFlags](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wantagent#wantagentflags)\> | 否 | 是 | 

动作执行属性。

从API version 7 开始支持，从API version 11 开始废弃，建议使用actionFlags11+替代。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

 |
| actionFlags11+ | Array<[abilityWantAgent.WantAgentFlags](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-wantagent#wantagentflags)\> | 否 | 是 | 

动作执行属性。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

 |
| extraInfo | { \[key: string\]: any } | 否 | 是 | 

额外数据。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

 |
| extraInfos11+ | Record<string, Object> | 否 | 是 | 

额外数据。推荐使用该属性替代extraInfo，设置该属性后，extraInfo不再生效。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

 |

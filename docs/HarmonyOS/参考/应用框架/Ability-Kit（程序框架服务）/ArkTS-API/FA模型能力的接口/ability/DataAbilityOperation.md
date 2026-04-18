---
title: "DataAbilityOperation"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-dataabilityoperation"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "FA模型能力的接口"
  - "ability"
  - "DataAbilityOperation"
captured_at: "2026-04-17T01:47:46.843Z"
---

# DataAbilityOperation

定义DataAbility数据操作方式，可以作为[executeBatch](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-dataabilityhelper#dataabilityhelperexecutebatch)的入参，操作数据库的信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/raGKRJxjRPS-jq4LGf1AaA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=5D4AEC5A0A242A7BE4B7E0E4647ABC9094574CCD54D463BA3B12E7C9DA2263AF)

本接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

此接口仅可在FA模型下使用。

#### 导入模块

```ts
import ability from '@ohos.ability.ability';
```

#### 属性

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| uri | string | 否 | 否 | 指示待处理的DataAbility。例：'dataability:///com.example.xxx.xxxx'。 |
| type | [featureAbility.DataAbilityOperationType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-ability-featureability#dataabilityoperationtype7) | 否 | 否 | 指示数据操作类型。 |
| valuesBucket | [rdb.ValuesBucket](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-t#valuesbucket) | 否 | 是 | 指示要操作的数据值。 |
| valueBackReferences | [rdb.ValuesBucket](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-t#valuesbucket) | 否 | 是 | 指示包含一组键值对的valuesBucket对象。 |
| predicates | [dataAbility.DataAbilityPredicates](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-ability#dataabilitypredicates) | 否 | 是 | 指示要设置的筛选条件。如果此参数为空，则操作所有数据记录。 |
| predicatesBackReferences | Map<number, number> | 否 | 是 | 指示用作谓词中筛选条件的反向引用。 |
| interrupted | boolean | 否 | 是 | 指示是否可以中断批处理操作。true表示可以中断批处理操作，false表示不可中断批处理操作。 |
| expectedCount | number | 否 | 是 | 指示要更新或删除的预期行数。 |

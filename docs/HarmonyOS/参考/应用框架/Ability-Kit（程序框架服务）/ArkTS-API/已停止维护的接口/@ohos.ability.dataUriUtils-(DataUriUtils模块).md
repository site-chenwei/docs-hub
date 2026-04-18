---
title: "@ohos.ability.dataUriUtils (DataUriUtils模块)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-ability-datauriutils"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "已停止维护的接口"
  - "@ohos.ability.dataUriUtils (DataUriUtils模块)"
captured_at: "2026-04-17T01:47:48.089Z"
---

# @ohos.ability.dataUriUtils (DataUriUtils模块)

DataUriUtils模块提供用于处理uri对象的能力，包括获取、绑定、删除和更新指定uri对象的路径末尾的ID。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/m4DVHQayR7GTUq5FgWheIw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=F81191E514130B6E9C96282C6D58772C179C020F12A6ABAF1665EBD027A7CA53)

本模块首批接口从API version 7开始支持，从API version 9废弃，替换模块为[@ohos.app.ability.dataUriUtils](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-datauriutils)。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import dataUriUtils from '@ohos.ability.dataUriUtils';
```

#### dataUriUtils.getId

getId(uri: string): number

获取指定uri路径末尾的ID。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| uri | string | 是 | 表示uri对象。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回uri路径末尾的ID。 |

**示例：**

```ts
import dataUriUtils from '@ohos.ability.dataUriUtils';

let id = dataUriUtils.getId('com.example.dataUriUtils/1221');
```

#### dataUriUtils.attachId

attachId(uri: string, id: number): string

将ID附加到uri的路径末尾。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| uri | string | 是 | 表示uri对象。 |
| id | number | 是 | 表示要附加的ID。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 返回附加ID之后的uri对象。 |

**示例：**

```ts
import dataUriUtils from '@ohos.ability.dataUriUtils';

let id = 1122;
let uri = dataUriUtils.attachId(
    'com.example.dataUriUtils',
    id,
);
```

#### dataUriUtils.deleteId

deleteId(uri: string): string

删除指定uri路径末尾的ID。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| uri | string | 是 | 表示要从中删除ID的uri对象。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 返回删除ID之后的uri对象。 |

**示例：**

```ts
import dataUriUtils from '@ohos.ability.dataUriUtils';

let uri = dataUriUtils.deleteId('com.example.dataUriUtils/1221');
```

#### dataUriUtils.updateId

updateId(uri: string, id: number): string

更新指定uri中的ID。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| uri | string | 是 | 表示uri对象。 |
| id | number | 是 | 表示要更新的ID。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 返回更新ID之后的uri对象。 |

**示例：**

```ts
import dataUriUtils from '@ohos.ability.dataUriUtils';

let id = 1122;
let uri = dataUriUtils.updateId(
    'com.example.dataUriUtils/1221',
    id
);
```

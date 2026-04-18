---
title: "@ohos.bundleState (设备使用信息统计)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-deviceusagestatistics"
menu_path:
  - "参考"
  - "应用框架"
  - "Background Tasks Kit（后台任务开发服务）"
  - "ArkTS API"
  - "已停止维护的接口"
  - "@ohos.bundleState (设备使用信息统计)"
captured_at: "2026-04-17T01:48:13.577Z"
---

# @ohos.bundleState (设备使用信息统计)

本模块提供设备使用信息统计能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/jO931sZMTy2Rqx1Qq4Zp1w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014813Z&HW-CC-Expire=86400&HW-CC-Sign=82EA5111BED954C15A28EF3774F77DF0694077A29CA2384F353B70F89C0A2F2B)

从API version9开始，该接口不再维护，替代接口仅向系统应用开放。

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```js
import bundleState from '@ohos.bundleState'
```

#### bundleState.isIdleState(deprecated)

isIdleState(bundleName: string, callback: AsyncCallback<boolean>): void

从API version 7开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

判断指定bundleName的应用当前是否是空闲状态，三方应用只能查询自身的空闲状态。系统应用支持查询其他应用的空闲状态，查询前需要申请权限ohos.permission.BUNDLE\_ACTIVE\_INFO。使用Callback异步回调。

**系统能力**：SystemCapability.ResourceSchedule.UsageStatistics.AppGroup

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| bundleName | string | 是 | 应用的bundleName。 |
| callback | AsyncCallback<boolean> | 是 | 指定的callback回调方法。如果指定的bundleName有效，则返回指定bundleName的应用当前是否是空闲状态；否则返回null。 |

**示例**：

```ts
import { BusinessError } from '@ohos.base';
// 三方应用使用示例代码时，注意将bundleName更换为自己应用的bundleName
bundleState.isIdleState("com.ohos.camera", (err: BusinessError, res: boolean) => {
  if (err) {
    console.error('BUNDLE_ACTIVE isIdleState callback failed, because: ' + err.code);
  } else {
    console.info('BUNDLE_ACTIVE isIdleState callback succeeded, result: ' + JSON.stringify(res));
  }
});
```

#### bundleState.isIdleState(deprecated)

isIdleState(bundleName: string): Promise<boolean>

从API version 7开始支持，从API version 9开始废弃，替代接口仅向系统应用开放。

判断指定bundleName的应用当前是否是空闲状态，三方应用只能查询自身的空闲状态。系统应用支持查询其他应用的空闲状态，查询前需要申请权限ohos.permission.BUNDLE\_ACTIVE\_INFO，使用Promise异步回调。

**系统能力**：SystemCapability.ResourceSchedule.UsageStatistics.AppGroup

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| bundleName | string | 是 | 应用的bundleName。 |

**返回值**：

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | 指定的Promise回调方法。如果指定的bundleName有效，则返回指定bundleName的应用当前是否是空闲状态；否则返回null。 |

**示例**：

```ts
import { BusinessError } from '@ohos.base';
// 三方应用使用示例代码时，注意将bundleName更换为自己应用的bundleName
bundleState.isIdleState("com.ohos.camera").then((res: boolean) => {
  console.info('BUNDLE_ACTIVE isIdleState promise succeeded, result: ' + JSON.stringify(res));
}).catch((err: BusinessError) => {
  console.error('BUNDLE_ACTIVE isIdleState promise failed, because: ' + err.code);
});
```

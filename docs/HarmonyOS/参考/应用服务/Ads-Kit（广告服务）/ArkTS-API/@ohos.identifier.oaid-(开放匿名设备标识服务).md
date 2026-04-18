---
title: "@ohos.identifier.oaid (开放匿名设备标识服务)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-oaid"
menu_path:
  - "参考"
  - "应用服务"
  - "Ads Kit（广告服务）"
  - "ArkTS API"
  - "@ohos.identifier.oaid (开放匿名设备标识服务)"
captured_at: "2026-04-17T01:48:56.380Z"
---

# @ohos.identifier.oaid (开放匿名设备标识服务)

本模块提供开放匿名设备标识符（Open Anonymous Device Identifier, OAID，以下简称OAID）的获取和重置能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/vQQ2tPRnSEGfjNPiylCtww/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014856Z&HW-CC-Expire=86400&HW-CC-Sign=CFD1CBEFB21103FF69D30C911764289B5A9656360B932892561FCFFF0757E034)

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

使用获取开放匿名设备标识符接口，需[向用户申请授权](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/request-user-authorization)（默认开启权限）：ohos.permission.APP\_TRACKING\_CONSENT。

#### 导入模块

```typescript
import { identifier } from '@kit.AdsKit';
```

#### identifier.getOAID

getOAID(): Promise<string>

获取开放匿名设备标识符（OAID）。使用Promise异步回调。

**需要权限：** ohos.permission.APP\_TRACKING\_CONSENT

**系统能力：** SystemCapability.Advertising.OAID

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | 
Promise对象，返回开放匿名设备标识符（OAID）。

1.如应用已配置ohos.permission.APP\_TRACKING\_CONSENT权限，且“跨应用关联访问权限”为“允许”，则返回OAID。

2.如应用已配置ohos.permission.APP\_TRACKING\_CONSENT权限，且“跨应用关联访问权限”为“禁止”，则返回00000000-0000-0000-0000-000000000000。

3.如应用未配置ohos.permission.APP\_TRACKING\_CONSENT权限，则返回00000000-0000-0000-0000-000000000000。

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/4874fZJ4TWmE6JietbKWlA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014856Z&HW-CC-Expire=86400&HW-CC-Sign=04BB039D552AA2699E0C3F9DC91AA2A8784D1143668A23EAFF7F0D8AC7F38224)

设置项“跨应用关联访问权限”在HarmonyOS NEXT Developer Beta5及更早版本名称为“应用跟踪访问权限”。

**错误码：**

以下错误码的详细介绍请参见[开放匿名设备标识服务错误码参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-oaid)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17300001 | System internal error. |

**示例：**

```typescript
import { identifier } from '@kit.AdsKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

void identifier.getOAID().then((data: string) => {
  const oaid: string = data;
}).catch((error: BusinessError) => {
  hilog.error(0x0000, 'testTag', `Failed to get oaid. Code is ${error.code}, message is ${error.message}`);
});
```

#### identifier.getOAID

getOAID(callback: AsyncCallback<string>): void

获取开放匿名设备标识符（OAID）。使用callback异步回调。

**需要权限：** ohos.permission.APP\_TRACKING\_CONSENT

**系统能力：** SystemCapability.Advertising.OAID

**参数：**

| **参数**名 | **类型** | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<string> | 是 | 
回调函数，返回开放匿名设备标识符（OAID）。

1.如应用已配置ohos.permission.APP\_TRACKING\_CONSENT权限，且“跨应用关联访问权限”为“允许”，则返回OAID。

2.如应用已配置ohos.permission.APP\_TRACKING\_CONSENT权限，且“跨应用关联访问权限”为“禁止”，则返回00000000-0000-0000-0000-000000000000。

3.如应用未配置ohos.permission.APP\_TRACKING\_CONSENT权限，则返回00000000-0000-0000-0000-000000000000。

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/UGRCgZYgTlm0JQ60vY0-YA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014856Z&HW-CC-Expire=86400&HW-CC-Sign=0F6B9DE25410E294D87D803FFE85978D811DBACF229980B5D112F47F3124A69E)

设置项“跨应用关联访问权限”在HarmonyOS NEXT Developer Beta5及更早版本名称为“应用跟踪访问权限”。

**错误码：**

以下错误码的详细介绍请参见[开放匿名设备标识服务错误码参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-oaid)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17300001 | System internal error. |

**示例：**

```typescript
import { identifier } from '@kit.AdsKit';
import { BusinessError } from '@kit.BasicServicesKit';

identifier.getOAID((err: BusinessError, data: string) => {
  if (err.code) {
    return;
  }
  const oaid: string = data;
});
```

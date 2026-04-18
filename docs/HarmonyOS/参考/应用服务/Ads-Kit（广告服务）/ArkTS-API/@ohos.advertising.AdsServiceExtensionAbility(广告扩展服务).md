---
title: "@ohos.advertising.AdsServiceExtensionAbility(广告扩展服务)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-adsserviceextensionability"
menu_path:
  - "参考"
  - "应用服务"
  - "Ads Kit（广告服务）"
  - "ArkTS API"
  - "@ohos.advertising.AdsServiceExtensionAbility(广告扩展服务)"
captured_at: "2026-04-17T01:48:56.381Z"
---

# @ohos.advertising.AdsServiceExtensionAbility(广告扩展服务)

本模块为设备厂商提供广告扩展能力，设备厂商可自主实现请求广告的回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/NNfPuIt4TnGkrUKvpIopNA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014856Z&HW-CC-Expire=86400&HW-CC-Sign=DAFF0C793E1032CA62F19377783E0C713D2D71C0DB4F8615A35D2C16D566B662)

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```typescript
import { RespCallback } from '@kit.AdsKit';
```

#### RespCallback

(respData: Map<string, Array<advertising.Advertisement>>): void

广告请求回调。

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| **参数名** | **类型** | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| respData | Map<string, Array<advertising.[Advertisement](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-advertising#advertisement)\>> | 是 | 广告请求回调数据。 |

**示例：**

```typescript
import { advertising, RespCallback } from '@kit.AdsKit';

function setRespCallback(respCallback: RespCallback) {
  const respData: Map<string, Array<advertising.Advertisement>> = new Map();
  // 设置广告返回数据
  // ...
  respCallback(respData);
}
```

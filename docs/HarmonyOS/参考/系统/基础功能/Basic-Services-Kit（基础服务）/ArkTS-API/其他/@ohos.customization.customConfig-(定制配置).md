---
title: "@ohos.customization.customConfig (定制配置)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-customization-customconfig"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "Basic Services Kit（基础服务）"
  - "ArkTS API"
  - "其他"
  - "@ohos.customization.customConfig (定制配置)"
captured_at: "2026-04-17T01:48:28.303Z"
---

# @ohos.customization.customConfig (定制配置)

本模块接口为应用提供定制配置的获取能力，如渠道号等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/OIPHkyx_R0OFToPmLTgjfQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=875B62DCC3D5CF30F8A98EDE3BB34D27CE20AD8472265D69DEA3D5189678F939)

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import { customConfig } from '@kit.BasicServicesKit';
```

#### customConfig.getChannelId

getChannelId(): string

获取应用的预装渠道号。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

\*\*系统能力：\*\*SystemCapability.Customization.CustomConfig

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 渠道号 |

**示例：**

```ts
import { customConfig } from '@kit.BasicServicesKit';

let channelId: string = customConfig.getChannelId();
console.info('app channelId is ' + channelId);
```

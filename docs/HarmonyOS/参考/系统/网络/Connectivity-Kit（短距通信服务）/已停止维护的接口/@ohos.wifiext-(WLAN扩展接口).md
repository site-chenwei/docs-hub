---
title: "@ohos.wifiext (WLAN扩展接口)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifiext"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Connectivity Kit（短距通信服务）"
  - "已停止维护的接口"
  - "@ohos.wifiext (WLAN扩展接口)"
captured_at: "2026-04-17T01:48:21.988Z"
---

# @ohos.wifiext (WLAN扩展接口)

该模块主要提供WLAN扩展接口，供非通用类型产品使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/6BujNFKhQxSx-wlIR4yllA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=9FE295099C47A46C9E92F734164C65F055F7C77CA2A34D49E6DE5D518DB60A6B)

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

该文档中的接口只供非通用类型产品使用，如路由器等，对于常规类型产品，不应该使用这些接口。

从API Version 9开始，该接口不再维护，推荐使用[@ohos.wifiManagerExt（WLAN扩展接口）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanagerext)等相关接口。

#### 导入模块

```js
import wifiext from '@ohos.wifiext';
```

#### wifiext.enableHotspot(deprecated)

enableHotspot(): boolean;

使能WLAN热点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/GwLLqxavSrybGEJWvdaEiw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=064F2221D45A8E4D1D3DA2F8A55F16EAF18217DBE3FCA00E3DFBEE4DA624EC59)

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManagerExt.enableHotspot](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanagerext#wifimanagerextenablehotspotdeprecated)替代。

**需要权限：** ohos.permission.MANAGE\_WIFI\_HOTSPOT\_EXT

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 操作结果， true: 成功， false: 失败。 |

#### wifiext.disableHotspot(deprecated)

disableHotspot(): boolean;

去使能WLAN热点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/T8KneP9pQIynk9gZugPqtw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=4E15DEDF887DF810108100091976D04D9A98970BCCCC7257BE45B420A6174762)

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManagerExt.disableHotspot](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanagerext#wifimanagerextdisablehotspotdeprecated)替代。

**需要权限：** ohos.permission.MANAGE\_WIFI\_HOTSPOT\_EXT

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 操作结果， true: 成功， false: 失败。 |

#### wifiext.getSupportedPowerModel(deprecated)

getSupportedPowerModel(): Promise<Array<PowerModel>>

获取支持的功率模式。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/Ts2ZXq-WQQq6Ak088M5olQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=B278A7AEFCFA0A59DEB277CDECCB5A2A87515DA11EED218CAF0BC1FD214B2BDC)

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManagerExt.getSupportedPowerModel](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanagerext#wifimanagerextgetsupportedpowermode)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<[PowerModel](#powermodel)\>> | Promise对象。表示功率模式。 |

#### PowerModel

表示功率模式的枚举。

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| SLEEPING | 0 | 睡眠模式。 |
| GENERAL | 1 | 常规模式。 |
| THROUGH\_WALL | 2 | 穿墙模式。 |

#### wifiext.getSupportedPowerModel

getSupportedPowerModel(callback: AsyncCallback<Array<PowerModel>>): void

获取支持的功率模式。使用callback异步回调。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[PowerModel](#powermodel)\>> | 是 | 回调函数。当操作成功时，err为0，data表示支持的功率模式。如果err为非0，表示处理出现错误。 |

#### wifiext.getPowerModel(deprecated)

getPowerModel(): Promise<PowerModel>

获取功率模式，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/SThIGWo1QtyYos1Un4MIuw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=FBF5A33A19E432709EC3C5B3949BB59454FB94F99A45DF877962125B1043B3A4)

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManagerExt.getSupportedPowerModel](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanagerext#wifimanagerextgetpowermode)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[PowerModel](#powermodel)\> | Promise对象。表示功率模式。 |

#### wifiext.getPowerModel(deprecated)

getPowerModel(callback: AsyncCallback<PowerModel>): void

获取功率模式。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/f0ruHLS0SH-wJ93P-mXNBg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=EBA140DE093CF9AFDB10FB23934C79068084A6D6BFFC2E7C3892FB6D6E50E794)

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManagerExt.getSupportedPowerModel](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanagerext#wifimanagerextgetpowermode-1)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[PowerModel](#powermodel)\> | 是 | 回调函数。当操作成功时，err为0，data表示功率模式。如果err为非0，表示处理出现错误。 |

#### wifiext.setPowerModel

setPowerModel(model: PowerModel) : boolean;

设置功率模式。

**需要权限：** ohos.permission.MANAGE\_WIFI\_HOTSPOT\_EXT

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| model | [PowerModel](#powermodel) | 是 | 功率模式。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 操作结果， true: 成功， false: 失败。 |

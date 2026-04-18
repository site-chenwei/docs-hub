---
title: "@system.geolocation (地理位置)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-location"
menu_path:
  - "参考"
  - "应用服务"
  - "Location Kit（位置服务）"
  - "ArkTS API"
  - "已停止维护的接口"
  - "@system.geolocation (地理位置)"
captured_at: "2026-04-17T01:48:59.046Z"
---

# @system.geolocation (地理位置)

本模块仅提供GNSS定位、网络定位等基本功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/2Y9RE9d6S_a_UVwp6ANkNg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014859Z&HW-CC-Expire=86400&HW-CC-Sign=3A14D8279E5B7159F43DC94932F0341E1EC44D47CC2296D3DB0B7AF86D3CBC01)

-   本模块首批接口从API version 3开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
-   对于Lite Wearable设备类型，该模块长期维护，正常使用。
-   对于支持该模块的其他设备类型，该模块从API Version 9开始，该接口不再维护，推荐使用新接口[geoLocationManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-geolocationmanager)。

#### 导入模块

```js
import geolocation from '@system.geolocation';
```

#### 权限列表

ohos.permission.LOCATION

#### geolocation.getLocation(deprecated)

getLocation(options?: GetLocationOption): void

获取设备的地理位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/lbqIlNATROSnxeGG9hcNuA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014859Z&HW-CC-Expire=86400&HW-CC-Sign=CAE1421088B07B44E17545FA810FAEFBB81A6C857E7ECE1867C2DFFC7BC764AE)

除Lite Wearable外，从API version 9开始废弃，建议使用[geoLocationManager.getCurrentLocation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-geolocationmanager#geolocationmanagergetcurrentlocation)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力：** SystemCapability.Location.Location.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [GetLocationOption](#getlocationoptiondeprecated) | 否 | 单次定位请求的配置参数。 |

**JS示例：**

```xml
<div class="container">
  <text class="title" style="font-size: {{fontSize}}; color: {{fontColor}};">
    getLocation
  </text>
  <input type="button" value="获取设备的地理位置" style="width: 240px; height: 50px;" onclick="getLocation"></input>
</div>
```

```css
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  left: 0px;
  top: 0px;
  width: 454px;
  height: 454px;
}

.title {
  font-size: 100px;
  text-align: center;
  width: 200px;
  height: 100px;
}

.button {
  font-size: 30px;
  text-align: center;
  width: 200px;
  height: 100px;
}
```

```js
export default {
  getLocation() {
    geolocation.getLocation({
      success: function(data) {
        console.info('success get location data. latitude:' + data.latitude);
      },
      fail: function(data, code) {
        console.info('fail to get location. code:' + code + ', data:' + data);
      }
    });
  },
}
```

#### geolocation.getLocationType(deprecated)

getLocationType(options?: GetLocationTypeOption): void

获取当前设备支持的定位类型。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/Eb9SEgueTE-NL54O2pBBUg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014859Z&HW-CC-Expire=86400&HW-CC-Sign=23CC2C028D8BCCEF74D963A644F4784C320F6278DD69369F544D365D30F130B7)

除Lite Wearable外，从API version 9开始废弃。位置服务子系统仅支持gnss和network两种定位类型，后续不再提供接口查询支持的定位类型。

**系统能力：** SystemCapability.Location.Location.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [GetLocationTypeOption](#getlocationtypeoptiondeprecated) | 否 | 回调函数，用于接收查询结果，或者接收查询失败的结果。 |

**JS示例：**

```xml
<div class="container">
  <text class="title" style="font-size: {{fontSize}}; color: {{fontColor}};">
    getLocationType
  </text>
  <input type="button" value="获取当前设备支持的定位类型" style="width: 240px; height: 50px;" onclick="getLocationType"></input>
</div>
```

```css
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  left: 0px;
  top: 0px;
  width: 454px;
  height: 454px;
}

.title {
  font-size: 100px;
  text-align: center;
  width: 200px;
  height: 100px;
}

.button {
  font-size: 30px;
  text-align: center;
  width: 200px;
  height: 100px;
}
```

```js
export default {
  getLocationType() {
    geolocation.getLocationType({
      success: function(data) {
        console.info('success get location type:' + data.types[0]);
      },
      fail: function(data, code) {
        console.info('fail to get location. code:' + code + ', data:' + data);
       },
     });
  },
}
```

#### geolocation.subscribe(deprecated)

subscribe(options: SubscribeLocationOption): void

订阅设备的地理位置信息。多次调用的话，只有最后一次的调用生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/W65MOUylSf65MO-A4eDz_g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014859Z&HW-CC-Expire=86400&HW-CC-Sign=941CEF2FB336D0B24146FEBABE49A230DC87313F57DB93AA3B99A810A319CDB5)

除Lite Wearable外，从API version 9开始废弃，建议使用[geoLocationManager.on('locationChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-geolocationmanager#geolocationmanageronlocationchange)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力：** SystemCapability.Location.Location.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [SubscribeLocationOption](#subscribelocationoptiondeprecated) | 是 | 持续定位的配置参数。 |

**JS示例：**

```xml
<div class="container">
  <text class="title" style="font-size: {{fontSize}}; color: {{fontColor}};">
    subscribe
  </text>
  <input type="button" value="订阅设备的地理位置信息" style="width: 240px; height: 50px;" onclick="subscribe"></input>
</div>
```

```css
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  left: 0px;
  top: 0px;
  width: 454px;
  height: 454px;
}

.title {
  font-size: 100px;
  text-align: center;
  width: 200px;
  height: 100px;
}

.button {
  font-size: 30px;
  text-align: center;
  width: 200px;
  height: 100px;
}
```

```js
export default {
  subscribe() {
    geolocation.subscribe({
      success: function(data) {
        console.info('get location. latitude:' + data.latitude);
      },
      fail: function(data, code) {
        console.info('fail to get location. code:' + code + ', data:' + data);
      },
    });
  },
}
```

#### geolocation.unsubscribe(deprecated)

unsubscribe(): void

取消订阅设备的地理位置信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/cq3b7AWmRzmX0OwHdaz5wg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014859Z&HW-CC-Expire=86400&HW-CC-Sign=E8514D3E9A0A5C5D3246F04A78FB66FDD30094DBA3E754AFE23F0F1513860AB8)

除Lite Wearable外，从API version 9开始废弃，建议使用[geoLocationManager.off('locationChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-geolocationmanager#geolocationmanagerofflocationchange)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力：** SystemCapability.Location.Location.Lite

**JS示例：**

```xml
<div class="container">
  <text class="title" style="font-size: {{fontSize}}; color: {{fontColor}};">
    unsubscribe
  </text>
  <input type="button" value="取消订阅设备的地理位置信息" style="width: 240px; height: 50px;" onclick="unsubscribe"></input>
</div>
```

```css
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  left: 0px;
  top: 0px;
  width: 454px;
  height: 454px;
}

.title {
  font-size: 100px;
  text-align: center;
  width: 200px;
  height: 100px;
}

.button {
  font-size: 30px;
  text-align: center;
  width: 200px;
  height: 100px;
}
```

```js
export default {
  unsubscribe() {
    geolocation.unsubscribe();
  },
}
```

#### geolocation.getSupportedCoordTypes(deprecated)

getSupportedCoordTypes(): Array<string>

获取设备支持的坐标系类型。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/hbU1NoK-SZSsVjpVjLxI2Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014859Z&HW-CC-Expire=86400&HW-CC-Sign=EC6A715DA2B3B8A39C200A31EDF1CAF0BD728291C4EB27F30323E22AEA825AE8)

除Lite Wearable外，从API version 9开始废弃。位置服务子系统仅支持WGS-84坐标系，后续不再提供接口查询支持的坐标系类型。

**系统能力：** SystemCapability.Location.Location.Lite

**返回值：**

| 类型 | 非空 | 说明 |
| :-- | :-- | :-- |
| Array<string> | 是 | 表示坐标系类型，如\[wgs84, gcj02\]。 |

**JS示例：**

```xml
<div class="container">
  <text class="title" style="font-size: {{fontSize}}; color: {{fontColor}};">
    getSupportedCoordTypes
  </text>
  <input type="button" value="获取设备支持的坐标系类型" style="width: 240px; height: 50px;" onclick="getSupportedCoordTypes"></input>
</div>
```

```css
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  left: 0px;
  top: 0px;
  width: 454px;
  height: 454px;
}

.title {
  font-size: 100px;
  text-align: center;
  width: 200px;
  height: 100px;
}

.button {
  font-size: 30px;
  text-align: center;
  width: 200px;
  height: 100px;
}
```

```js
export default {
  getSupportedCoordTypes() {
    var types = geolocation.getSupportedCoordTypes();
    console.info('getSupportedCoordTypes:' types);
  },
}
```

#### GetLocationOption(deprecated)

单次定位请求的配置参数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/S98KjHx5QFicW_SrMtSlFw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014859Z&HW-CC-Expire=86400&HW-CC-Sign=D9A658F2E976F2C82707E68055BA04B30B78463FD8A9725234BF82F0DA703FC6)

除Lite Wearable外，从API version 9开始废弃，建议使用[geoLocationManager.CurrentLocationRequest](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-geolocationmanager#currentlocationrequest)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Lite

| 名称 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| timeout | number | 否 | 
超时时间，单位为ms，默认值为30000。

设置超时，是为了防止出现权限被系统拒绝、定位信号弱或者定位设置不当，导致请求阻塞的情况。超时后会使用fail回调函数。

取值范围为32位正整数。如果设置值小于等于0，系统按默认值处理。

 |
| coordType | string | 否 | 坐标系的类型，可通过getSupportedCoordTypes获取可选值，缺省值为wgs84。 |
| success | (data: [GeolocationResponse](#geolocationresponsedeprecated)) => void | 否 | 接口调用成功的回调函数。 |
| fail | (data: string, code: number) => void | 否 | 接口调用失败的回调函数。data为错误信息，code为错误码。 |
| complete | () => void | 否 | 接口调用结束的回调函数。 |

fail返回错误代码：

| 错误码 | 说明 |
| :-- | :-- |
| 601 | 获取定位权限失败，失败原因：用户拒绝。 |
| 602 | 权限未声明。 |
| 800 | 超时，失败原因：网络状况不佳或GNSS不可用。 |
| 801 | 系统位置开关未打开。 |
| 802 | 该次调用结果未返回前接口又被重新调用，该次调用失败返回错误码。 |

#### GeolocationResponse(deprecated)

位置信息，包含经度、纬度、定位精度等信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/SCYLSM4SRcqKDWF2THcKCw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014859Z&HW-CC-Expire=86400&HW-CC-Sign=18723FBFA936345006B50AE39A8F21417A134BDFB1E1EACD4DA501FC209DAF79)

除Lite Wearable外，从API version 9开始废弃，建议使用[geoLocationManager.Location](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-geolocationmanager#location)替代。

**系统能力**：SystemCapability.Location.Location.Lite

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| longitude | number | 否 | 否 | 设备位置信息：经度。 |
| latitude | number | 否 | 否 | 设备位置信息：纬度。 |
| altitude | number | 否 | 否 | 设备位置信息：海拔。 |
| accuracy | number | 否 | 否 | 设备位置信息：精确度。 |
| time | number | 否 | 否 | 设备位置信息：时间。 |

#### GetLocationTypeOption(deprecated)

查询定位类型接口的入参，用于存放回调函数，在查询成功或者失败时接收查询结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/lE6mT9GTTDyY1qkTyoL3Lw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014859Z&HW-CC-Expire=86400&HW-CC-Sign=A21F600D4FDD201DD8DEFF5BCF934CEFD285CD2D6F2D47EECB8415BA1FCA19D3)

除Lite Wearable外，从API version 9开始废弃。

**系统能力**：SystemCapability.Location.Location.Lite

| 名称 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| success | (data: [GetLocationTypeResponse](#getlocationtyperesponsedeprecated)) => void | 否 | 接口调用成功的回调函数。 |
| fail | (data: string, code: number) => void | 否 | 接口调用失败的回调函数。 |
| complete | () => void | 否 | 接口调用结束的回调函数。 |

#### GetLocationTypeResponse(deprecated)

当前设备支持的定位类型列表

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/tEsTAnl-RSGTBcQCmeZbVQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014859Z&HW-CC-Expire=86400&HW-CC-Sign=8B539B6D4D1325DEF4C84E73B71DDFC0522C9EBA066CD495BB1D8301240E92F2)

除Lite Wearable外，从API version 9开始废弃。

**系统能力**：SystemCapability.Location.Location.Lite

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| types | Array<string> | 否 | 否 | 可选的定位类型\['gps', 'network'\]。 |

#### SubscribeLocationOption(deprecated)

持续定位请求的配置参数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/sCPERdBhSJK9hl1A2Wf83w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014859Z&HW-CC-Expire=86400&HW-CC-Sign=1BDAC22D881F057F8C7ED209FB6AD9D5BC54921F3DBD223078AFF7228C8E034F)

除Lite Wearable外，从API version 9开始废弃，建议使用[geoLocationManager.CurrentLocationRequest](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-geolocationmanager#currentlocationrequest)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Lite

| 名称 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| coordType | string | 否 | 坐标系的类型，可通过getSupportedCoordTypes获取可选值，默认值为wgs84。 |
| success | (data: [GeolocationResponse](#geolocationresponsedeprecated)) => void | 是 | 位置信息发生变化的回调函数。 |
| fail | (data: string, code: number) => void | 否 | 接口调用失败的回调函数。 |

fail返回错误代码：

| 错误码 | 说明 |
| :-- | :-- |
| 601 | 获取定位权限失败，失败原因：用户拒绝。 |
| 602 | 权限未声明。 |
| 801 | 系统位置开关未打开。 |

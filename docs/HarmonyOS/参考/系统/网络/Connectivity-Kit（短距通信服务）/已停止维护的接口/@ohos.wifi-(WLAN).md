---
title: "@ohos.wifi (WLAN)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifi"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Connectivity Kit（短距通信服务）"
  - "已停止维护的接口"
  - "@ohos.wifi (WLAN)"
captured_at: "2026-04-17T01:48:22.046Z"
---

# @ohos.wifi (WLAN)

该模块主要提供WLAN基础功能、P2P（peer-to-peer）功能和WLAN消息通知的相应服务，让应用可以通过WLAN和其他设备互联互通。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/4ityevv_Q2OkDdMfMGbvog/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=C09D4A9B5FEDC65CFEA971144260FE25F55C84328ABAFE5042A385DE9E3DFCBF)

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API Version 9 开始，该接口不再维护，推荐使用[@ohos.wifiManager (WLAN)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager)等相关接口。

#### 导入模块

```ts
import wifi from '@ohos.wifi';
```

#### wifi.isWifiActive(deprecated)

isWifiActive(): boolean

查询WLAN是否已使能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/OGoXOWN6SwmtU6oTzO8ypw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=40C3CC9E09274AF463894B8707D8E2AD5DFC0D49F68169DDD3BDBBCA4255700D)

从API version 6开始支持，从API version 9开始废弃。建议使用[wifiManager.isWifiActive](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanageriswifiactive)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true:已使能， false:未使能。 |

**示例：**

```ts
import wifi from '@ohos.wifi';

try {
    let isWifiActive = wifi.isWifiActive();
    console.info("isWifiActive:" + isWifiActive);
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

#### wifi.scan(deprecated)

scan(): boolean

启动WLAN扫描。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/O43EJWIPQaquI-WE8uC9HA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=885E6C1E67E0FD5EF89B257BDCDD5B9E998C7CBA91FA8E0EA57E76E02727BC1B)

从API version 6开始支持，从API version 9开始废弃。建议使用[wifiManager.scan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanagerscandeprecated)替代。

**需要权限：** ohos.permission.SET\_WIFI\_INFO 和 ohos.permission.LOCATION

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true:扫描操作执行成功， false:扫描操作执行失败。 |

**示例：**

```ts
import wifi from '@ohos.wifi';

try {
    wifi.scan();
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

#### wifi.getScanInfos(deprecated)

getScanInfos(): Promise<Array<WifiScanInfo>>

获取扫描结果，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/qVxL6w2tQraR-mOWxssEQA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=E8DC4EF1CD0F16EC98E4083C88858E2BB55744BC48B081E2FBFAD4853FF36879)

从API version 6开始支持，从API version 9开始废弃。建议使用[wifiManager.getScanInfos](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanagergetscaninfolist10)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO 和 (ohos.permission.GET\_WIFI\_PEERS\_MAC 或 ohos.permission.LOCATION)

ohos.permission.GET\_WIFI\_PEERS\_MAC权限仅系统应用可申请。

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise< Array<[WifiScanInfo](#wifiscaninfodeprecated)\> > | Promise对象。返回扫描到的热点列表。 |

#### wifi.getScanInfos(deprecated)

getScanInfos(callback: AsyncCallback<Array<WifiScanInfo>>): void

获取扫描结果，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/J7E9k41hShKerINIcyoCSw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=BF191F978E81B688B46090318B355E8CE79A0AD1D569BEC8416332CE32D3A042)

从API version 6开始支持，从API version 9开始废弃。建议使用[wifiManager.getScanInfos](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanagergetscaninfolist10)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO 和 (ohos.permission.GET\_WIFI\_PEERS\_MAC 或 ohos.permission.LOCATION)

ohos.permission.GET\_WIFI\_PEERS\_MAC权限仅系统应用可申请。

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback< Array<[WifiScanInfo](#wifiscaninfodeprecated)\>> | 是 | 回调函数。当成功时，err为0，data为扫描到的热点；否则err为非0值，data为空。 |

**示例：**

```ts
import wifi from '@ohos.wifi';

wifi.getScanInfos().then(result => {
    let len = result.length;
    console.info("wifi received scan info: " + len);
    for (let i = 0; i < len; ++i) {
        console.info("ssid: " + result[i].ssid);
        console.info("bssid: " + result[i].bssid);
        console.info("capabilities: " + result[i].capabilities);
        console.info("securityType: " + result[i].securityType);
        console.info("rssi: " + result[i].rssi);
        console.info("band: " + result[i].band);
        console.info("frequency: " + result[i].frequency);
        console.info("channelWidth: " + result[i].channelWidth);
        console.info("timestamp: " + result[i].timestamp);
    }
});
```

#### WifiScanInfo(deprecated)

WLAN热点信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/hSVCmWEmSSKTAQZj0pPhpg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=82EA867913E23A58BC33C37487039D292EE35B551BE6D72A6E5B36982CBC7135)

从API version 6开始支持，从API version 9开始废弃。建议使用[WifiScanInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifiscaninfo)替代。

**系统能力：** SystemCapability.Communication.WiFi.STA

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| ssid | string | 否 | 否 | 热点的SSID，最大长度为32字节，编码格式为UTF-8。 |
| bssid | string | 否 | 否 | 热点的BSSID，例如：00:11:22:33:44:55。 |
| capabilities | string | 否 | 否 | 热点能力。 |
| securityType | [WifiSecurityType](#wifisecuritytypedeprecated) | 否 | 否 | WLAN加密类型。 |
| rssi | number | 否 | 否 | 热点的信号强度(dBm)。 |
| band | number | 否 | 否 | WLAN接入点的频段。1表示2.4GHZ；2表示5GHZ。 |
| frequency | number | 否 | 否 | WLAN接入点的频率。 |
| channelWidth | number | 否 | 否 | WLAN接入点的带宽。 |
| timestamp | number | 否 | 否 | 时间戳。 |

#### WifiSecurityType(deprecated)

表示加密类型的枚举。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/zpL8okr3TWWf9GPXbdWG_w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=4C018A3C28E5E133911A69D9A14BEF95FB563D7ED2843549570B97FC32BEF78C)

从API version 6开始支持，从API version 9开始废弃。建议使用[WifiSecurityType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifisecuritytype)替代。

**系统能力：** SystemCapability.Communication.WiFi.Core

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| WIFI\_SEC\_TYPE\_INVALID | 0 | 无效加密类型。 |
| WIFI\_SEC\_TYPE\_OPEN | 1 | 开放加密类型。 |
| WIFI\_SEC\_TYPE\_WEP | 2 | Wired Equivalent Privacy (WEP)加密类型。 |
| WIFI\_SEC\_TYPE\_PSK | 3 | Pre-shared key (PSK)加密类型。 |
| WIFI\_SEC\_TYPE\_SAE | 4 | Simultaneous Authentication of Equals (SAE)加密类型。 |

#### WifiDeviceConfig(deprecated)

WLAN配置信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/JYXhl37AS-WugdQB9NdNag/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=7BC4EB3462145AA7538ED379E8982117F9BD046489AFEBEAFAC2FB287A3F27AD)

从API version 6开始支持，从API version 9开始废弃。建议使用[WifiDeviceConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifideviceconfig)替代。

**系统能力：** SystemCapability.Communication.WiFi.STA

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| ssid | string | 否 | 否 | 热点的SSID，最大长度为32字节，编码格式为UTF-8。 |
| bssid | string | 否 | 否 | 热点的BSSID，例如：00:11:22:33:44:55。 |
| preSharedKey | string | 否 | 否 | 热点的密钥，最大长度为64字节。 |
| isHiddenSsid | boolean | 否 | 否 | 是否是隐藏网络。true:是隐藏网络，false:不是隐藏网络。 |
| securityType | [WifiSecurityType](#wifisecuritytypedeprecated) | 否 | 否 | 加密类型。 |

#### wifi.addUntrustedConfig(deprecated)

addUntrustedConfig(config: WifiDeviceConfig): Promise<boolean>

添加不可信网络配置，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/zhMZcWI_TfqeZ1KLgIB49Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=E4E77A52413E2731115780EBAE557F104F9AC169E2A989C4CD53C38E24A981BA)

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.addCandidateConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanageraddcandidateconfig)替代。

**需要权限：** ohos.permission.SET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| config | [WifiDeviceConfig](#wifideviceconfigdeprecated) | 是 | WLAN配置信息。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象。表示操作结果，true: 成功， false: 失败。 |

**示例：**

```ts
import wifi from '@ohos.wifi';

try {
    let config:wifi.WifiDeviceConfig = {
        ssid : "****",
        bssid:  "****",
        preSharedKey: "****",
        isHiddenSsid: false,
        securityType: 0,
        creatorUid: 0,
        disableReason: 0,
        netId: 0,
        randomMacType: 0,
        randomMacAddr:  "****",
        ipType: 0,
        staticIp: {
            ipAddress: 0,
            gateway: 0,
            dnsServers: [],
            domains: []
        }
    }
    wifi.addUntrustedConfig(config).then(result => {
        console.info("result:" + JSON.stringify(result));
    });
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

#### wifi.addUntrustedConfig(deprecated)

addUntrustedConfig(config: WifiDeviceConfig, callback: AsyncCallback<boolean>): void

添加不可信网络配置，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/iUWHIprjRBywt7ixQnMlJA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=59E99CD8F2C347F3D7FAC4EC124F582B88785036AE69BC7FBA661835FC7BDDC7)

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.addCandidateConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanageraddcandidateconfig-1)替代。

**需要权限：** ohos.permission.SET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| config | [WifiDeviceConfig](#wifideviceconfigdeprecated) | 是 | WLAN配置信息。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当操作成功时，err为0，data表示操作结果，true: 成功， false: 失败。如果error为非0，表示处理出现错误。 |

**示例：**

```ts
import wifi from '@ohos.wifi';

try {
    let config:wifi.WifiDeviceConfig = {
        ssid : "****",
        bssid:  "****",
        preSharedKey: "****",
        isHiddenSsid: false,
        securityType: 0,
        creatorUid: 0,
        disableReason: 0,
        netId: 0,
        randomMacType: 0,
        randomMacAddr:  "****",
        ipType: 0,
        staticIp: {
            ipAddress: 0,
            gateway: 0,
            dnsServers: [],
            domains: []
        }
    }
    wifi.addUntrustedConfig(config,(error,result) => {
        console.info("result:" + JSON.stringify(result));
    });
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

#### wifi.removeUntrustedConfig(deprecated)

removeUntrustedConfig(config: WifiDeviceConfig): Promise<boolean>

移除不可信网络配置，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/ueZZQtrZQ4mdOSL4e1gDdA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=563642B93334105C660628FA2916086BECB46C8F0694519DF3829DA66D4E6CCC)

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.removeCandidateConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanagerremovecandidateconfig)替代。

**需要权限：** ohos.permission.SET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| config | [WifiDeviceConfig](#wifideviceconfigdeprecated) | 是 | WLAN配置信息。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象。表示操作结果，true: 成功， false: 失败。 |

**示例：**

```ts
import wifi from '@ohos.wifi';

try {
    let config:wifi.WifiDeviceConfig = {
        ssid : "****",
        bssid:  "****",
        preSharedKey: "****",
        isHiddenSsid: false,
        securityType: 0,
        creatorUid: 0,
        disableReason: 0,
        netId: 0,
        randomMacType: 0,
        randomMacAddr:  "****",
        ipType: 0,
        staticIp: {
            ipAddress: 0,
            gateway: 0,
            dnsServers: [],
            domains: []
        }
    }
    wifi.removeUntrustedConfig(config).then(result => {
        console.info("result:" + JSON.stringify(result));
    });
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

#### wifi.removeUntrustedConfig(deprecated)

removeUntrustedConfig(config: WifiDeviceConfig, callback: AsyncCallback<boolean>): void

移除不可信网络配置，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/FGg284kkQzu-ksOlaLCsKA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=AB1E24CD95757646889246E0656F285022B6929A4FEA97D9AF1E24B0085430A9)

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.removeCandidateConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanagerremovecandidateconfig-1)替代。

**需要权限：** ohos.permission.SET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| config | [WifiDeviceConfig](#wifideviceconfigdeprecated) | 是 | WLAN配置信息。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当操作成功时，err为0，data表示操作结果，true: 成功， false: 失败。如果error为非0，表示处理出现错误。 |

**示例：**

```ts
import wifi from '@ohos.wifi';

try {
    let config:wifi.WifiDeviceConfig = {
        ssid : "****",
        bssid:  "****",
        preSharedKey: "****",
        isHiddenSsid: false,
        securityType: 0,
        creatorUid: 0,
        disableReason: 0,
        netId: 0,
        randomMacType: 0,
        randomMacAddr:  "****",
        ipType: 0,
        staticIp: {
            ipAddress: 0,
            gateway: 0,
            dnsServers: [],
            domains: []
        }
    }
    wifi.removeUntrustedConfig(config,(error,result) => {
    console.info("result:" + JSON.stringify(result));
    });
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

#### wifi.getSignalLevel(deprecated)

getSignalLevel(rssi: number, band: number): number

查询WLAN信号强度。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/wP2ECHQ-Tsq55-i4icpw6Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=39C8D3C724ED5B066ED5EF31B2D34C62549F594689E0D8F81BC2E0611BB29434)

从API version 6开始支持，从API version 9开始废弃。建议使用[wifiManager.getSignalLevel](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanagergetsignallevel)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| rssi | number | 是 | 热点的信号强度(dBm)。 |
| band | number | 是 | WLAN接入点的频段。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 信号强度，取值范围为\[0, 4\]。 |

**示例：**

```ts
import wifi from '@ohos.wifi';

try {
    let rssi = 0;
    let band = 0;
    let level = wifi.getSignalLevel(rssi,band);
    console.info("level:" + JSON.stringify(level));
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

#### wifi.getLinkedInfo(deprecated)

getLinkedInfo(): Promise<WifiLinkedInfo>

获取WLAN连接信息。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/mBjoEUbWQBqsGeFjn5Bquw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=BB1FB6585BA4AC6A59F348D3734E8CF58BB218EE66F65D356B388B57B5FEB00B)

从API version 6开始支持，从API version 9开始废弃。建议使用[wifiManager.getLinkedInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanagergetlinkedinfo)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[WifiLinkedInfo](#wifilinkedinfodeprecated)\> | Promise对象。表示WLAN连接信息。 |

#### wifi.getLinkedInfo(deprecated)

getLinkedInfo(callback: AsyncCallback<WifiLinkedInfo>): void

获取WLAN连接信息。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/15qxZCXaRFm91YDiX7_faA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=E115E6A1898F615353F0CF7930FCDD1CCE7EE8ED66F1A8B78A609CF8034BCBDF)

从API version 6开始支持，从API version 9开始废弃。建议使用[wifiManager.getLinkedInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanagergetlinkedinfo-1)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[WifiLinkedInfo](#wifilinkedinfodeprecated)\> | 是 | 回调函数。当获取成功时，err为0，data表示WLAN连接信息。如果error为非0，表示处理出现错误。 |

**示例：**

```ts
import wifi from '@ohos.wifi';

wifi.getLinkedInfo((err, data:wifi.WifiLinkedInfo) => {
    if (err) {
        console.error("get linked info error");
        return;
    }
    console.info("get wifi linked info: " + JSON.stringify(data));
});

wifi.getLinkedInfo().then(data => {
    console.info("get wifi linked info: " + JSON.stringify(data));
}).catch((error:number) => {
    console.info("get linked info error");
});
```

#### WifiLinkedInfo(deprecated)

提供WLAN连接的相关信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/tb5KJyVRQMKAdLzbpSnMlA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=9D610019231266253EB7BB8F3C03BCF3EDB1AC2291104C3A2B1680D7A0A0D0FC)

从API version 6开始支持，从API version 9开始废弃。建议使用[WifiLinkedInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifilinkedinfo)替代。

**系统能力：** SystemCapability.Communication.WiFi.STA

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| ssid | string | 否 | 否 | 热点的SSID，最大长度为32字节，编码格式为UTF-8。 |
| bssid | string | 否 | 否 | 热点的BSSID，例如：00:11:22:33:44:55。 |
| rssi | number | 否 | 否 | 热点的信号强度(dBm)。 |
| band | number | 否 | 否 | WLAN接入点的频段。1表示2.4GHZ；2表示5GHZ。 |
| linkSpeed | number | 否 | 否 | WLAN接入点的速度，单位Mbps。 |
| frequency | number | 否 | 否 | WLAN接入点的频率。 |
| isHidden | boolean | 否 | 否 | WLAN接入点是否是隐藏网络。true:是隐藏网络，false:不是隐藏网络。 |
| isRestricted | boolean | 否 | 否 | WLAN接入点是否限制数据量。true: 限制，false:不限制。 |
| macAddress | string | 否 | 否 | 设备的MAC地址。 |
| ipAddress | number | 否 | 否 | WLAN连接的IP地址。 |
| connState | [ConnState](#connstatedeprecated) | 否 | 否 | WLAN连接状态。 |

#### ConnState(deprecated)

表示WLAN连接状态的枚举。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/5c30vQmJQuuNckgpmWqvuQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=4E673F3F9471036BDDB80E61B042AEDE8015D686FD00C91DFA4FA133E8C82A2B)

从API version 6开始支持，从API version 9开始废弃。建议使用[ConnState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#connstate)替代。

**系统能力：** SystemCapability.Communication.WiFi.STA

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| SCANNING | 0 | 设备正在搜索可用的AP。 |
| CONNECTING | 1 | 正在建立WLAN连接。 |
| AUTHENTICATING | 2 | WLAN连接正在认证中。 |
| OBTAINING\_IPADDR | 3 | 正在获取WLAN连接的IP地址。 |
| CONNECTED | 4 | WLAN连接已建立。 |
| DISCONNECTING | 5 | WLAN连接正在断开。 |
| DISCONNECTED | 6 | WLAN连接已断开。 |
| UNKNOWN | 7 | WLAN连接建立失败。 |

#### wifi.isConnected(deprecated)

isConnected(): boolean

查询WLAN是否已连接。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/wR9KDoj-Qai6HT1d7gtb7Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=478050CA50FCD399E49E7EC313D5112FAB86F5FA619456AB802C5C931FC894F9)

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.isConnected](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanagerisconnected)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true:已连接， false:未连接。 |

#### wifi.isFeatureSupported(deprecated)

isFeatureSupported(featureId: number): boolean

判断设备是否支持相关WLAN特性。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/2Pno5nw8S5GGwYCQ2_fVvA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=EA1CCD9FCF58D9C9BD93B9180C4C58E64EF1C977778D82386A19C0DD42FDCC55)

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.isFeatureSupported](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanagerisfeaturesupported)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| featureId | number | 是 | 特性ID值。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true:支持， false:不支持。 |

**示例：**

```ts
import wifi from '@ohos.wifi';

try {
    let featureId = 0;
    let ret = wifi.isFeatureSupported(featureId);
    console.info("isFeatureSupported:" + ret);
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

#### wifi.getIpInfo(deprecated)

getIpInfo(): IpInfo

获取IP信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/qQfiFzbiTe25daEQESoehA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=73E0AA1937FFD35EC30EE600C14D5A0FDF4DC4816A0D3B81547FF95E537445CA)

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.getIpInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanagergetipinfo)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [IpInfo](#ipinfodeprecated) | IP信息。 |

**示例：**

```ts
import wifi from '@ohos.wifi';

try {
    let info = wifi.getIpInfo();
    console.info("info:" + JSON.stringify(info));
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

#### IpInfo(deprecated)

IP信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/PWkPFwM5QcqbehrmYlwCWg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=45E8C2BF77EE0580AE5DEE161A9165E2625E5CCA619DA160326BD9DA3F4477D0)

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.getIpInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanagergetipinfo)替代。

**系统能力：** SystemCapability.Communication.WiFi.AP.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| ipAddress | number | 否 | 否 | IP地址。 |
| gateway | number | 否 | 否 | 网关。 |
| netmask | number | 否 | 否 | 掩码。 |
| primaryDns | number | 否 | 否 | 主DNS服务器IP地址。 |
| secondDns | number | 否 | 否 | 备DNS服务器IP地址。 |
| serverIp | number | 否 | 否 | DHCP服务端IP地址。 |
| leaseDuration | number | 否 | 否 | IP地址租用时长。 |

#### wifi.getCountryCode(deprecated)

getCountryCode(): string

获取国家码信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/eLbSqzPITzS_WzYqjwiL1g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=9877939E769181D3142A6C00869C4C0903AECE9160776BD6346B1036CDD89515)

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.getCountryCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanagergetcountrycode)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 国家码。 |

**示例：**

```ts
import wifi from '@ohos.wifi';

try {
    let code = wifi.getCountryCode();
    console.info("code:" + code);
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

#### wifi.getP2pLinkedInfo(deprecated)

getP2pLinkedInfo(): Promise<WifiP2pLinkedInfo>

获取P2P连接信息。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/NY5pDg_jTlqvv_ZWCg9tyA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=8509E5C62A223BE52CF0FED047FF66D2B1D85925E501ED5AC7A0CA17A99F11D8)

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.getP2pLinkedInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanagergetp2plinkedinfo)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[WifiP2pLinkedInfo](#wifip2plinkedinfodeprecated)\> | Promise对象。表示P2P连接信息。 |

#### WifiP2pLinkedInfo(deprecated)

提供WLAN连接的相关信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/jgk2mYQnQtakd3x8TnNaWg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=DFECD2AC75F8EBA702AB80B2D5F7E8E0247A14394DE7F9E816F9720539C70ADE)

从API version 8开始支持，从API version 9开始废弃。建议使用[WifiP2pLinkedInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifip2plinkedinfo)替代。

**系统能力：** SystemCapability.Communication.WiFi.P2P

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| connectState | [P2pConnectState](#p2pconnectstatedeprecated) | 否 | 否 | P2P连接状态。 |
| isGroupOwner | boolean | 否 | 否 | 是否是群主。true:是群主，false:不是群主。 |
| groupOwnerAddr | string | 否 | 否 | 群组MAC地址。 |

#### P2pConnectState(deprecated)

表示P2P连接状态的枚举。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/7-jHon7lREiqCib4JCgJhQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=455CCC5989E8900086F74DBFAFBFFB45C66B639919C9B4A0DC73C5E770C7B567)

从API version 8开始支持，从API version 9开始废弃。建议使用[P2pConnectState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#p2pconnectstate)替代。

**系统能力：** SystemCapability.Communication.WiFi.P2P

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| DISCONNECTED | 0 | 断开状态。 |
| CONNECTED | 1 | 连接状态。 |

#### wifi.getP2pLinkedInfo(deprecated)

getP2pLinkedInfo(callback: AsyncCallback<WifiP2pLinkedInfo>): void

获取P2P连接信息。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/UPwft7egSXWPqlaFLjyr6w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=FF96A139F61F57747BCCE63D4F2B0A3288C7D0D34AFCB2FE58812F546284A370)

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.getP2pLinkedInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanagergetp2plinkedinfo-1)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[WifiP2pLinkedInfo](#wifip2plinkedinfodeprecated)\> | 是 | 回调函数。当操作成功时，err为0，data表示P2P连接信息。如果error为非0，表示处理出现错误。 |

**示例：**

```ts
import wifi from '@ohos.wifi';

wifi.getP2pLinkedInfo((err, data:wifi.WifiP2pLinkedInfo) => {
   if (err) {
       console.error("get p2p linked info error");
       return;
   }
    console.info("get wifi p2p linked info: " + JSON.stringify(data));
});

wifi.getP2pLinkedInfo().then(data => {
    console.info("get wifi p2p linked info: " + JSON.stringify(data));
});
```

#### wifi.getCurrentGroup(deprecated)

getCurrentGroup(): Promise<WifiP2pGroupInfo>

获取P2P当前组信息。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/lfWFW7OgQ6iza7bhWClhGQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=DA7FECD99E61D010040150B67BC5179472CF55164A97E3955488FD66666705EA)

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.getCurrentGroup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanagergetcurrentgroup)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO 和 ohos.permission.LOCATION

**系统能力：** SystemCapability.Communication.WiFi.P2P

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[WifiP2pGroupInfo](#wifip2pgroupinfodeprecated)\> | Promise对象。表示当前组信息。 |

#### wifi.getCurrentGroup(deprecated)

getCurrentGroup(callback: AsyncCallback<WifiP2pGroupInfo>): void

获取P2P当前组信息。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/leqnN9skRzi5lIybHPEHLA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=3F975E161CE4293E1590938B04052575C7779154E77A872385AF1C611DB4264F)

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.getCurrentGroup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanagergetcurrentgroup-1)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO 和 ohos.permission.LOCATION

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[WifiP2pGroupInfo](#wifip2pgroupinfodeprecated)\> | 是 | 回调函数。当操作成功时，err为0，data表示当前组信息。如果error为非0，表示处理出现错误。 |

**示例：**

```ts
import wifi from '@ohos.wifi';

wifi.getCurrentGroup((err, data:wifi.WifiP2pGroupInfo) => {
   if (err) {
       console.error("get current P2P group error");
       return;
   }
    console.info("get current P2P group: " + JSON.stringify(data));
});

wifi.getCurrentGroup().then(data => {
    console.info("get current P2P group: " + JSON.stringify(data));
});
```

#### wifi.getP2pPeerDevices(deprecated)

getP2pPeerDevices(): Promise<WifiP2pDevice\[\]>

获取P2P对端设备列表信息。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/BtUFmgaERpeU5w2PRiMovw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=764C280EFDD29DEA94677022CEBE6539634F93F4B66C651CB010E6E4BBD15708)

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.getP2pPeerDevices](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanagergetp2ppeerdevices)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO 和 ohos.permission.LOCATION

**系统能力：** SystemCapability.Communication.WiFi.P2P

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[WifiP2pDevice\[\]](#wifip2pdevicedeprecated)\> | Promise对象。表示对端设备列表信息。 |

#### wifi.getP2pPeerDevices(deprecated)

getP2pPeerDevices(callback: AsyncCallback<WifiP2pDevice\[\]>): void

获取P2P对端设备列表信息。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/HIsUHxG1S664SoIgwt_94w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=40E0EF7E4B35DBB18535DEAA8D83BEE7A95AABAE8C8F0AB98CC856A6F7568B71)

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.getP2pPeerDevices](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanagergetp2ppeerdevices-1)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO 和 ohos.permission.LOCATION

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[WifiP2pDevice\[\]](#wifip2pdevicedeprecated)\> | 是 | 回调函数。当操作成功时，err为0，data表示对端设备列表信息。如果error为非0，表示处理出现错误。 |

**示例：**

```ts
import wifi from '@ohos.wifi';

wifi.getP2pPeerDevices((err, data:wifi.WifiP2pDevice) => {
   if (err) {
       console.error("get P2P peer devices error");
       return;
   }
    console.info("get P2P peer devices: " + JSON.stringify(data));
});

wifi.getP2pPeerDevices().then(data => {
    console.info("get P2P peer devices: " + JSON.stringify(data));
});
```

#### WifiP2pDevice(deprecated)

表示P2P设备信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/ifECfs37RDOG8_SFZCMrBA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=197A6AD1B8BC7FCD50447A19BE1647675325861BC89E9504EA98E9516CEE214D)

从API version 8开始支持，从API version 9开始废弃。建议使用[WifiP2pDevice](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifip2pdevice)替代。

**系统能力：** SystemCapability.Communication.WiFi.P2P

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| deviceName | string | 否 | 否 | 设备名称。 |
| deviceAddress | string | 否 | 否 | 设备MAC地址。 |
| primaryDeviceType | string | 否 | 否 | 主设备类型。 |
| deviceStatus | [P2pDeviceStatus](#p2pdevicestatusdeprecated) | 否 | 否 | 设备状态。 |
| groupCapabilitys | number | 否 | 否 | 群组能力。 |

#### P2pDeviceStatus(deprecated)

表示设备状态的枚举。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/EeRghr6ISFm8RBdRap3a7Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=0EA452E4E8AD8AF1265CFFB22FE181819686D3798D2F1D543D49771982810CA0)

从API version 8开始支持，从API version 9开始废弃。建议使用[P2pDeviceStatus](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#p2pdevicestatus)替代。

**系统能力：** SystemCapability.Communication.WiFi.P2P

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| CONNECTED | 0 | 连接状态。 |
| INVITED | 1 | 邀请状态。 |
| FAILED | 2 | 失败状态。 |
| AVAILABLE | 3 | 可用状态。 |
| UNAVAILABLE | 4 | 不可用状态。 |

#### wifi.createGroup(deprecated)

createGroup(config: WifiP2PConfig): boolean

创建群组。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/1SXHA5FkRhGlAWh_kWq4Yw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=4F1C5D71EA3AA979692F9D4AD13B526CF5155684A28E1BAE0F58267246832D2B)

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.createGroup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanagercreategroup)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| config | [WifiP2PConfig](#wifip2pconfigdeprecated) | 是 | 群组配置信息。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true:创建群组操作执行成功， false:创建群组操作执行失败。 |

**示例：**

```ts
import wifi from '@ohos.wifi';

try {
    let config:wifi.WifiP2PConfig = {
        deviceAddress: "****",
        netId: 0,
        passphrase: "*****",
        groupName: "****",
        goBand: 0
    }
    wifi.createGroup(config);
    
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

#### WifiP2PConfig(deprecated)

表示P2P配置信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/U9Pt6vabTdGULSKw0wkxBg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=0B20A1D41771C92A91E45819F9032E4D3015077C257226A369B466948E87AE50)

从API version 8开始支持，从API version 9开始废弃。建议使用[WifiP2PConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifip2pconfig)替代。

**系统能力：** SystemCapability.Communication.WiFi.P2P

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| deviceAddress | string | 否 | 否 | 设备地址。 |
| netId | number | 否 | 否 | 网络ID。创建群组时-1表示创建临时组，-2表示创建永久组。 |
| passphrase | string | 否 | 否 | 群组密钥。 |
| groupName | string | 否 | 否 | 群组名称。 |
| goBand | [GroupOwnerBand](#groupownerbanddeprecated) | 否 | 否 | 群组带宽。 |

#### GroupOwnerBand(deprecated)

表示群组带宽的枚举。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/kAmw9IZzRESHP7VLuSYmOA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=AA4C18B2C88383EA92913B5640C145B733F12841FE27456127FCF9798A7245E9)

从API version 8开始支持，从API version 9开始废弃。建议使用[GroupOwnerBand](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#groupownerband)替代。

**系统能力：** SystemCapability.Communication.WiFi.P2P

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| GO\_BAND\_AUTO | 0 | 自动模式。 |
| GO\_BAND\_2GHZ | 1 | 2GHZ。 |
| GO\_BAND\_5GHZ | 2 | 5GHZ。 |

#### wifi.removeGroup(deprecated)

removeGroup(): boolean

移除群组。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/h2XkkaOsQA6un3sA3ne9Gw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=B50BCFED47D568EE84B51E46233428CB57FA3A6B04ADE3A4AC4378702C395C11)

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.removeGroup](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanagerremovegroup)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true:操作执行成功， false:操作执行失败。 |

**示例：**

```ts
import wifi from '@ohos.wifi';

try {
    wifi.removeGroup();
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

#### wifi.p2pConnect(deprecated)

p2pConnect(config: WifiP2PConfig): boolean

执行P2P连接。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/jQpj6qAkSVSvMCYyNUeayg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=BF216D34D204BF036FCAEE6D77766FC76B66F84E40FAEACDBC39FA345271E11A)

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.p2pConnect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanagerp2pconnect)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO 和 ohos.permission.LOCATION

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| config | [WifiP2PConfig](#wifip2pconfigdeprecated) | 是 | 连接配置信息。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true:操作执行成功， false:操作执行失败。 |

**示例：**

```ts
import wifi from '@ohos.wifi';

let recvP2pConnectionChangeFunc = (result:wifi.WifiP2pLinkedInfo) => {
    console.info("p2p connection change receive event: " + JSON.stringify(result));
    wifi.getP2pLinkedInfo((err, data:wifi.WifiP2pLinkedInfo) => {
        if (err) {
            console.error('failed to get getP2pLinkedInfo: ' + JSON.stringify(err));
            return;
        }
        console.info("get getP2pLinkedInfo: " + JSON.stringify(data));
    });
}
wifi.on("p2pConnectionChange", recvP2pConnectionChangeFunc);

let recvP2pDeviceChangeFunc = (result:wifi.WifiP2pDevice) => {
    console.info("p2p device change receive event: " + JSON.stringify(result));
}
wifi.on("p2pDeviceChange", recvP2pDeviceChangeFunc);

let recvP2pPeerDeviceChangeFunc = (result:wifi.WifiP2pDevice[]) => {
    console.info("p2p peer device change receive event: " + JSON.stringify(result));
    wifi.getP2pPeerDevices((err, data:wifi.WifiP2pDevice[]) => {
        if (err) {
            console.error('failed to get peer devices: ' + JSON.stringify(err));
            return;
        }
        console.info("get peer devices: " + JSON.stringify(data));
        let len = data.length;
        for (let i = 0; i < len; ++i) {
            if (data[i].deviceName === "my_test_device") {
                console.info("p2p connect to test device: " + data[i].deviceAddress);
                let config:wifi.WifiP2PConfig = {
                    deviceAddress:data[i].deviceAddress,
                    netId:-2,
                    passphrase:"",
                    groupName:"",
                    goBand:0,
                }
                wifi.p2pConnect(config);
            }
        }
    });
}
wifi.on("p2pPeerDeviceChange", recvP2pPeerDeviceChangeFunc);

let recvP2pPersistentGroupChangeFunc = () => {
    console.info("p2p persistent group change receive event");

    wifi.getCurrentGroup((err, data:wifi.WifiP2pGroupInfo) => {
        if (err) {
            console.error('failed to get current group: ' + JSON.stringify(err));
            return;
        }
        console.info("get current group: " + JSON.stringify(data));
    });
}
wifi.on("p2pPersistentGroupChange", recvP2pPersistentGroupChangeFunc);

setTimeout(() => {wifi.off("p2pConnectionChange", recvP2pConnectionChangeFunc);}, 125 * 1000);
setTimeout(() => {wifi.off("p2pDeviceChange", recvP2pDeviceChangeFunc);}, 125 * 1000);
setTimeout(() => {wifi.off("p2pPeerDeviceChange", recvP2pPeerDeviceChangeFunc);}, 125 * 1000);
setTimeout(() => {wifi.off("p2pPersistentGroupChange", recvP2pPersistentGroupChangeFunc);}, 125 * 1000);
console.info("start discover devices -> " + wifi.startDiscoverDevices());
```

#### wifi.p2pCancelConnect(deprecated)

p2pCancelConnect(): boolean

取消P2P连接。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/ozIldbZkQ3SHsZEjr6hn5A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=16BD60992C44642343CE5F7DFF881E740A19EC6189E61D9E3B2C7BF251F70CAF)

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.p2pCancelConnect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanagerp2pcancelconnect)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true:操作执行成功， false:操作执行失败。 |

**示例：**

```ts
import wifi from '@ohos.wifi';

try {
    wifi.p2pCancelConnect();
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

#### wifi.startDiscoverDevices(deprecated)

startDiscoverDevices(): boolean

开始发现设备。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/vMzpg-YRRX6pPL7dqiUabg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=129C3490E8C7C2CBD40516722DA20E40DE0F26EB7979553E8108A4D04BD50827)

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.startDiscoverDevices](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanagerstartdiscoverdevices)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO 和 ohos.permission.LOCATION

**系统能力：** SystemCapability.Communication.WiFi.P2P

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true:操作执行成功， false:操作执行失败。 |

**示例：**

```ts
import wifi from '@ohos.wifi';

try {
    wifi.startDiscoverDevices();
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

#### wifi.stopDiscoverDevices(deprecated)

stopDiscoverDevices(): boolean

停止发现设备。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/G9bTCxs-QZuQpg44xzzJ4A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=B44C295744CE9010125BD8B4F5EB2191BA59AF5018BE54C9321ABB335A4F7C91)

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.stopDiscoverDevices](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanagerstopdiscoverdevices)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true:操作执行成功 false:操作执行失败。 |

**示例：**

```ts
import wifi from '@ohos.wifi';

try {
    wifi.stopDiscoverDevices();
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

#### WifiP2pGroupInfo(deprecated)

表示P2P群组相关信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/7x86GTx2RWW8dDY22rIQVQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=87FFF1C438A8F00EB6D0437E3EF7FEBD34A0E1EADC3BDEE02192F9C8E1C3E713)

从API version 8开始支持，从API version 9开始废弃。建议使用[WifiP2pGroupInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifip2pgroupinfo)替代。

**系统能力：** SystemCapability.Communication.WiFi.P2P

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| isP2pGo | boolean | 否 | 否 | 是否是群主。true:是群主，false:不是群主。 |
| ownerInfo | [WifiP2pDevice](#wifip2pdevicedeprecated) | 否 | 否 | 群组的设备信息。 |
| passphrase | string | 否 | 否 | 群组密钥。 |
| interface | string | 否 | 否 | 接口名称。 |
| groupName | string | 否 | 否 | 群组名称。 |
| networkId | number | 否 | 否 | 网络ID。 |
| frequency | number | 否 | 否 | 群组的频率。 |
| clientDevices | [WifiP2pDevice\[\]](#wifip2pdevicedeprecated) | 否 | 否 | 接入的设备列表信息。 |
| goIpAddress | string | 否 | 否 | 群组IP地址。 |

#### wifi.on('wifiStateChange')(deprecated)

on(type: 'wifiStateChange', callback: Callback<number>): void

注册WLAN状态改变事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/92SFKNAHTXyuryP18j4bDw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=19A79C47BB0C226F5FCE4692BD70CE5065215B779EEBD085B2CA4D2C35207AAB)

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.on](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanageronwifistatechange)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 固定填"wifiStateChange"字符串。 |
| callback | Callback<number> | 是 | 状态改变回调函数。 |

**状态改变事件的枚举：**

| 枚举值 | 说明 |
| :-- | :-- |
| 0 | 未激活。 |
| 1 | 已激活。 |
| 2 | 激活中。 |
| 3 | 去激活中。 |

#### wifi.off('wifiStateChange')(deprecated)

off(type: 'wifiStateChange', callback?: Callback<number>): void

取消注册WLAN状态改变事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/fnvCdFvIShywoowBFFgRHg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=5AE8508BCC6A9D269AEAD5A69DE363C64D4EFE790BD81CBFDF4BBA3D1C473C69)

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.off](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanageroffwifistatechange)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 固定填"wifiStateChange"字符串。 |
| callback | Callback<number> | 否 | 状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。 |

**示例：**

```ts
import wifi from '@ohos.wifi';

let recvPowerNotifyFunc = (result:number) => {
    console.info("Receive power state change event: " + result);
}

// Register event
wifi.on("wifiStateChange", recvPowerNotifyFunc);

// Unregister event
wifi.off("wifiStateChange", recvPowerNotifyFunc);
```

#### wifi.on('wifiConnectionChange')(deprecated)

on(type: 'wifiConnectionChange', callback: Callback<number>): void

注册WLAN连接状态改变事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/mQz9lkXgQ8i2EHLmxpbCPg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=733CFC6B3E5835709527ACB7B6F8DCC4265694B53EBC80C886D73BC91C3FA968)

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.on](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanageronwificonnectionchange)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 固定填"wifiConnectionChange"字符串。 |
| callback | Callback<number> | 是 | 状态改变回调函数。 |

**连接状态改变事件的枚举：**

| 枚举值 | 说明 |
| :-- | :-- |
| 0 | 已断开。 |
| 1 | 已连接。 |

#### wifi.off('wifiConnectionChange')(deprecated)

off(type: 'wifiConnectionChange', callback?: Callback<number>): void

取消注册WLAN连接状态改变事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/jWCeFiQJSkmXX2UFx8KKtA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=0222C92ACAC5527AE5A552421352D5A0D29C384B3EF5F4F07C455E8488CFF1A0)

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.off](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanageroffwificonnectionchange)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 固定填"wifiConnectionChange"字符串。 |
| callback | Callback<number> | 否 | 连接状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。 |

**示例：**

```ts
import wifi from '@ohos.wifi';

let recvWifiConnectionChangeFunc = (result:number) => {
    console.info("Receive wifi connection change event: " + result);
}

// Register event
wifi.on("wifiConnectionChange", recvWifiConnectionChangeFunc);

// Unregister event
wifi.off("wifiConnectionChange", recvWifiConnectionChangeFunc);
```

#### wifi.on('wifiScanStateChange')(deprecated)

on(type: 'wifiScanStateChange', callback: Callback<number>): void

注册扫描状态改变事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/JHQuxJf9Q_-yvR5_aMe2PA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=05AB7FFD5684870F3EB6591A5327A0545E071617A071C335BF253C051F5DF901)

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.on](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanageronwifiscanstatechange)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 固定填"wifiScanStateChange"字符串。 |
| callback | Callback<number> | 是 | 状态改变回调函数。 |

**扫描状态改变事件的枚举：**

| 枚举值 | 说明 |
| :-- | :-- |
| 0 | 扫描失败。 |
| 1 | 扫描成功。 |

#### wifi.off('wifiScanStateChange')(deprecated)

off(type: 'wifiScanStateChange', callback?: Callback<number>): void

取消注册扫描状态改变事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/EoLiI0kvQNuNvPMv7qBcBw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=1AB866E245387C043A04F5BC9AFD9C68B1B3811E2DAE088B76016A9DEA8FF767)

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.off](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanageroffwifiscanstatechange)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 固定填"wifiScanStateChange"字符串。 |
| callback | Callback<number> | 否 | 状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。 |

**示例：**

```ts
import wifi from '@ohos.wifi';

let recvWifiScanStateChangeFunc = (result:number) => {
    console.info("Receive Wifi scan state change event: " + result);
}

// Register event
wifi.on("wifiScanStateChange", recvWifiScanStateChangeFunc);

// Unregister event
wifi.off("wifiScanStateChange", recvWifiScanStateChangeFunc);
```

#### wifi.on('wifiRssiChange')(deprecated)

on(type: 'wifiRssiChange', callback: Callback<number>): void

注册RSSI状态改变事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/PkhWnlSiSF6u4yUUinZFaw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=A0669628C9E4041D978B48D0E2E12ACDF48E59D2796F5AB844B16AD81EE93576)

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.on](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanageronwifirssichange)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 固定填"wifiRssiChange"字符串。 |
| callback | Callback<number> | 是 | 状态改变回调函数，返回以dBm为单位的RSSI值。 |

#### wifi.off('wifiRssiChange')(deprecated)

off(type: 'wifiRssiChange', callback?: Callback<number>): void

取消注册RSSI状态改变事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/g3_OBOVLSCKO0NvjvOrfWw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=8CDF83D9AE4DA0A5A1B3B5894A8FC3F1DD5170A07A33289A2ACBABF076D4D10D)

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.off](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanageroffwifirssichange)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 固定填"wifiRssiChange"字符串。 |
| callback | Callback<number> | 否 | 状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。 |

**示例：**

```ts
import wifi from '@ohos.wifi';

let recvWifiRssiChangeFunc = (result:number) => {
    console.info("Receive wifi rssi change event: " + result);
}

// Register event
wifi.on("wifiRssiChange", recvWifiRssiChangeFunc);

// Unregister event
wifi.off("wifiRssiChange", recvWifiRssiChangeFunc);
```

#### wifi.on('hotspotStateChange')(deprecated)

on(type: 'hotspotStateChange', callback: Callback<number>): void

注册热点状态改变事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/OsSNyoMSTTGISPVMnwUVDw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=14DA0C94EA2428BA47E901A953FFC326F546E346B321D5B7D3CF38F598709650)

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.on](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanageronhotspotstatechange)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.AP.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 固定填"hotspotStateChange"字符串。 |
| callback | Callback<number> | 是 | 状态改变回调函数。 |

**热点状态改变事件的枚举：**

| 枚举值 | 说明 |
| :-- | :-- |
| 0 | 未激活。 |
| 1 | 已激活。 |
| 2 | 激活中。 |
| 3 | 去激活中。 |

**示例：**

```ts
import wifi from '@ohos.wifi';

let recvHotspotStateChangeFunc = (result:number) => {
    console.info("Receive hotspot state change event: " + result);
}

// Register event
wifi.on("hotspotStateChange", recvHotspotStateChangeFunc);

// Unregister event
wifi.off("hotspotStateChange", recvHotspotStateChangeFunc);
```

#### wifi.off('hotspotStateChange')(deprecated)

off(type: 'hotspotStateChange', callback?: Callback<number>): void

取消注册热点状态改变事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/EbkOlMiCSYSL4-DhqcSszg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=5279A9077CFBFA11C1B75156D4F60638DF0FBA0F6CC2BEDA3357CFC7026CB2AF)

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.off](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanageroffhotspotstatechange)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.AP.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 固定填"hotspotStateChange"字符串。 |
| callback | Callback<number> | 否 | 状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。 |

#### wifi.on('p2pStateChange')(deprecated)

on(type: 'p2pStateChange', callback: Callback<number>): void

注册P2P开关状态改变事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/yWcrtaVIRRWoW43UiNd1Fw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=3B4D85AF873300B6EDF90FB9F35F8E2352EE1BBD0EB8E6899552635A8B698D63)

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.on](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanageronp2pstatechange)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 固定填"p2pStateChange"字符串。 |
| callback | Callback<number> | 是 | 状态改变回调函数。 |

**P2P状态改变事件的枚举：**

| 枚举值 | 说明 |
| :-- | :-- |
| 1 | 空闲。 |
| 2 | 打开中。 |
| 3 | 已打开。 |
| 4 | 关闭中。 |
| 5 | 已关闭。 |

#### wifi.off('p2pStateChange')(deprecated)

off(type: 'p2pStateChange', callback?: Callback<number>): void

取消注册P2P开关状态改变事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/x2acCoOFTMO9gY2mV7rmVQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=2CD30A0FD09831EF5FF9EAB9990D5E4576D967DC711E46A4393A738CC486D8BC)

从API version 7开始支持，从API version 9开始废弃。建议使用[wifiManager.off](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanageroffp2pstatechange)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 固定填"p2pStateChange"字符串。 |
| callback | Callback<number> | 否 | 状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。 |

**示例：**

```ts
import wifi from '@ohos.wifi';

let recvP2pStateChangeFunc = (result:number) => {
    console.info("Receive p2p state change event: " + result);
}

// Register event
wifi.on("p2pStateChange", recvP2pStateChangeFunc);

// Unregister event
wifi.off("p2pStateChange", recvP2pStateChangeFunc);
```

#### wifi.on('p2pConnectionChange')(deprecated)

on(type: 'p2pConnectionChange', callback: Callback<WifiP2pLinkedInfo>): void

注册P2P连接状态改变事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/fgx7k4KfT66VUfNChtJKBQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=68022A3628B16397140B4BCCCE762D44AB3CBC6B7ED9CE30E101B1083B75B876)

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.on](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanageronp2pconnectionchange)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 固定填"p2pConnectionChange"字符串。 |
| callback | Callback<[WifiP2pLinkedInfo](#wifip2plinkedinfodeprecated)\> | 是 | 状态改变回调函数。 |

#### wifi.off('p2pConnectionChange')(deprecated)

off(type: 'p2pConnectionChange', callback?: Callback<WifiP2pLinkedInfo>): void

取消注册P2P连接状态改变事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/X6n_VcBKTf-Mz6XoonLd2g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=A1068B40682191AA4A898DF51C21C5CB5D83E5D0C5E653BA03ABC0CADF4151CD)

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.off](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanageroffp2pconnectionchange)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 固定填"p2pConnectionChange"字符串。 |
| callback | Callback<[WifiP2pLinkedInfo](#wifip2plinkedinfodeprecated)\> | 否 | 状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。 |

**示例：**

```ts
import wifi from '@ohos.wifi';

let recvP2pConnectionChangeFunc = (result:wifi.WifiP2pLinkedInfo) => {
    console.info("Receive p2p connection change event: " + result);
}

// Register event
wifi.on("p2pConnectionChange", recvP2pConnectionChangeFunc);

// Unregister event
wifi.off("p2pConnectionChange", recvP2pConnectionChangeFunc);
```

#### wifi.on('p2pDeviceChange')(deprecated)

on(type: 'p2pDeviceChange', callback: Callback<WifiP2pDevice>): void

注册P2P设备状态改变事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/rouu_kBrQ7is2u3CheXNkg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=D4D85580F746266701420243AF9BD60F395CC0F9E62BC3FE3C22036526A686FB)

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.on](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanageronp2pdevicechange)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO 和 ohos.permission.LOCATION

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 固定填"p2pDeviceChange"字符串。 |
| callback | Callback<[WifiP2pDevice](#wifip2pdevicedeprecated)\> | 是 | 状态改变回调函数。 |

#### wifi.off('p2pDeviceChange')(deprecated)

off(type: 'p2pDeviceChange', callback?: Callback<WifiP2pDevice>): void

取消注册P2P设备状态改变事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/meocp5XhQiaAE-K7XkZu_Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=7C5D2FBB13A5F40752DAEAED69BDE3AE3D35C1891E72EDCB4E3EFE47B6F8D9F4)

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.off](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanageroffp2pdevicechange)替代。

**需要权限：** ohos.permission.LOCATION

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 固定填"p2pDeviceChange"字符串。 |
| callback | Callback<[WifiP2pDevice](#wifip2pdevicedeprecated)\> | 否 | 状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。 |

**示例：**

```ts
import wifi from '@ohos.wifi';

let recvP2pDeviceChangeFunc = (result:wifi.WifiP2pDevice) => {
    console.info("Receive p2p device change event: " + result);
}

// Register event
wifi.on("p2pDeviceChange", recvP2pDeviceChangeFunc);

// Unregister event
wifi.off("p2pDeviceChange", recvP2pDeviceChangeFunc);
```

#### wifi.on('p2pPeerDeviceChange')(deprecated)

on(type: 'p2pPeerDeviceChange', callback: Callback<WifiP2pDevice\[\]>): void

注册P2P对端设备状态改变事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/-GjFKzOeSRKiAINQWXHIPw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=B93C83EFE323C17EE1F6320731E69A4CE3E1CAF24E8C57E5F81C2E66A8F9A51D)

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.on](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanageronp2ppeerdevicechange)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO 和 ohos.permission.LOCATION

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 固定填"p2pPeerDeviceChange"字符串。 |
| callback | Callback<[WifiP2pDevice\[\]](#wifip2pdevicedeprecated)\> | 是 | 状态改变回调函数。 |

#### wifi.off('p2pPeerDeviceChange')(deprecated)

off(type: 'p2pPeerDeviceChange', callback?: Callback<WifiP2pDevice\[\]>): void

取消注册P2P对端设备状态改变事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/1f0IB7kZQXG-Ddnf42vaFw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=5FE9DA1B82E1F460B7A8C6E9195D29F7257E3863DB9AB0CB635E0FBB738A7E8E)

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.off](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanageroffp2ppeerdevicechange)替代。

**需要权限：** ohos.permission.LOCATION

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 固定填"p2pPeerDeviceChange"字符串。 |
| callback | Callback<[WifiP2pDevice\[\]](#wifip2pdevicedeprecated)\> | 否 | 状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。 |

**示例：**

```ts
import wifi from '@ohos.wifi';

let recvP2pPeerDeviceChangeFunc = (result:wifi.WifiP2pDevice[]) => {
    console.info("Receive p2p peer device change event: " + result);
}

// Register event
wifi.on("p2pPeerDeviceChange", recvP2pPeerDeviceChangeFunc);

// Unregister event
wifi.off("p2pPeerDeviceChange", recvP2pPeerDeviceChangeFunc);
```

#### wifi.on('p2pPersistentGroupChange')(deprecated)

on(type: 'p2pPersistentGroupChange', callback: Callback<void>): void

注册P2P永久组状态改变事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/EBE8CZIURtWVNn5UYd3mJQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=63155BD298F66FF439708320ECEB864AFA761C0D200CA5E108982AF771BEF47F)

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.on](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanageronp2ppersistentgroupchange)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 固定填"p2pPersistentGroupChange"字符串。 |
| callback | Callback<void> | 是 | 状态改变回调函数。 |

#### wifi.off('p2pPersistentGroupChange')(deprecated)

off(type: 'p2pPersistentGroupChange', callback?: Callback<void>): void

取消注册P2P永久组状态改变事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/_pAiVA4jQBuzH483EAcmiA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=93F88AEBB000C87F119DF1721A03EFF1BA78AA873DBEF16D82747BA71A838428)

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.off](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanageroffp2ppersistentgroupchange)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 固定填"p2pPersistentGroupChange"字符串。 |
| callback | Callback<void> | 否 | 状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。 |

**示例：**

```ts
import wifi from '@ohos.wifi';

let recvP2pPersistentGroupChangeFunc = (result:void) => {
    console.info("Receive p2p persistent group change event: " + result);
}

// Register event
wifi.on("p2pPersistentGroupChange", recvP2pPersistentGroupChangeFunc);

// Unregister event
wifi.off("p2pPersistentGroupChange", recvP2pPersistentGroupChangeFunc);
```

#### wifi.on('p2pDiscoveryChange')(deprecated)

on(type: 'p2pDiscoveryChange', callback: Callback<number>): void

注册发现设备状态改变事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/viHKbkapR1mCu2ywFThBDg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=6936392680A5EECBC28D99E79D3BA182C9C54BF8E94BC3A61C5B1ACF42F56CBB)

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.on](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanageronp2pdiscoverychange)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 固定填"p2pDiscoveryChange"字符串。 |
| callback | Callback<number> | 是 | 状态改变回调函数。 |

**发现设备状态改变事件的枚举：**

| 枚举值 | 说明 |
| :-- | :-- |
| 0 | 初始状态。 |
| 1 | 发现成功。 |

#### wifi.off('p2pDiscoveryChange')(deprecated)

off(type: 'p2pDiscoveryChange', callback?: Callback<number>): void

取消注册发现设备状态改变事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/Q_Op8Y8ARUWpN8eVUH_07Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=6C07F62CF9F1EBFEA15C43791F5A7ED2C017E3573C9F49058BDDB8474E1C68B4)

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManager.off](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanager#wifimanageroffp2pdiscoverychange)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.P2P

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 固定填"p2pDiscoveryChange"字符串。 |
| callback | Callback<number> | 否 | 状态改变回调函数。如果callback不填，将取消注册该事件关联的所有回调函数。 |

**示例：**

```ts
import wifi from '@ohos.wifi';

let recvP2pDiscoveryChangeFunc = (result:number) => {
    console.info("Receive p2p discovery change event: " + result);
}

// Register event
wifi.on("p2pDiscoveryChange", recvP2pDiscoveryChangeFunc);

// Unregister event
wifi.off("p2pDiscoveryChange", recvP2pDiscoveryChangeFunc);
```

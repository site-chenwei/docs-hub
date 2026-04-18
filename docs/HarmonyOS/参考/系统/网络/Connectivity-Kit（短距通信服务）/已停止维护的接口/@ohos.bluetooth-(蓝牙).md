---
title: "@ohos.bluetooth (蓝牙)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Connectivity Kit（短距通信服务）"
  - "已停止维护的接口"
  - "@ohos.bluetooth (蓝牙)"
captured_at: "2026-04-17T01:48:22.108Z"
---

# @ohos.bluetooth (蓝牙)

蓝牙模块提供了基础的传统蓝牙能力以及BLE的扫描、广播等功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/3wgL-ELWR1SIQcnMp02eOg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=9BAE5E2C965DB7819CA4809F09AF7E8758DC089410B89E9FB0CB7D758FFE16E5)

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API Version 9 开始，该接口不再维护，推荐使用[@ohos.bluetooth.ble](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble)等相关profile接口。

#### 导入模块

```js
import bluetooth from '@ohos.bluetooth';
```

#### bluetooth.enableBluetooth(deprecated)

enableBluetooth(): boolean

开启蓝牙。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/RdPB6BySR1utOVTcjatjtQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=DE9348733AA50478EA26A129524F24A5889C9CF64620F9D15C1671010F0126FF)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.enableBluetooth](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#bluetoothmanagerenablebluetoothdeprecated)替代。

**需要权限**：ohos.permission.DISCOVER\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 打开蓝牙，成功返回true，否则返回false。 |

**示例：**

```js
let enable : boolean = bluetooth.enableBluetooth();
```

#### bluetooth.disableBluetooth(deprecated)

disableBluetooth(): boolean

关闭蓝牙。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/j9ttDf-5SdSKTB4VoH6iSA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=1F6FEBC8C8974827D6F2532D79DC8EDE34AB3C02F98D86B2389CE8B46CF97E58)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.disableBluetooth](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#bluetoothmanagerdisablebluetoothdeprecated)替代。

**需要权限**：ohos.permission.DISCOVER\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 关闭蓝牙，成功返回true，否则返回false。 |

**示例：**

```js
let disable : boolean = bluetooth.disableBluetooth();
```

#### bluetooth.getLocalName(deprecated)

getLocalName(): string

获取蓝牙本地设备名称。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/K64hTek7QaWnUiA8G9P0BA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=5A4D159D7924E4692534302CEFCA50D006F24D2372010FA1DA55BEC71BF087B0)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.getLocalName](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#bluetoothmanagergetlocalnamedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 蓝牙本地设备名称。 |

**示例：**

```js
let localName : string = bluetooth.getLocalName();
```

#### bluetooth.getState(deprecated)

getState(): BluetoothState

获取蓝牙开关状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/5whirO23Q6KfzpRfoMSO_w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=8AE93AD9048F7D82BF5922CE262DAC6721F869BE33138AF89965B70720B9F5C6)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.getState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#bluetoothmanagergetstatedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [BluetoothState](#bluetoothstatedeprecated) | 表示蓝牙开关状态。 |

**示例：**

```js
let state : bluetooth.BluetoothState = bluetooth.getState();
```

#### bluetooth.getBtConnectionState(deprecated)

getBtConnectionState(): ProfileConnectionState

获取蓝牙本端的Profile连接状态，例如：任意一个支持的Profile连接状态为已连接，则此接口返回状态为已连接。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/Lli-ijoRS0iGoztTubGOuA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=6394D3DBDC9C44A22B083CEF657E7510880061DAF16DFB9CD0E60436E01AB3A7)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.getBtConnectionState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#bluetoothmanagergetbtconnectionstatedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [ProfileConnectionState](#profileconnectionstatedeprecated) | 表示蓝牙设备的Profile连接状态。 |

**示例：**

```js
let connectionState : bluetooth.ProfileConnectionState = bluetooth.getBtConnectionState();
```

#### bluetooth.setLocalName(deprecated)

setLocalName(name: string): boolean

设置蓝牙本地设备名称。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/lUsN7dJoRpa0YWaXNaTAHQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=E29CCD66D620E21EAE3CBC5C03CDF218300B6C9D637CBF5FA525EA3F711A5F09)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.setLocalName](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#bluetoothmanagersetlocalnamedeprecated)替代。

**需要权限**：ohos.permission.DISCOVER\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 要设置的蓝牙名称，最大长度为248字节数。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 设置蓝牙本地设备名称，成功返回true，否则返回false。 |

**示例：**

```js
let ret : boolean = bluetooth.setLocalName('device_name');
```

#### bluetooth.pairDevice(deprecated)

pairDevice(deviceId: string): boolean

发起蓝牙配对。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/_QH7YqgEQyKGL7q8GB-Kdg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=1F79A02979840DD7E48A40FFA084EC090072BA580873D482C23C1851E2C7580D)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.pairDevice](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#bluetoothmanagerpairdevicedeprecated)替代。

**需要权限**：ohos.permission.DISCOVER\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| deviceId | string | 是 | 表示配对的远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 发起蓝牙配对，成功返回true，否则返回false。 |

**示例：**

```js
// 实际的地址可由扫描流程获取
let result : boolean = bluetooth.pairDevice("XX:XX:XX:XX:XX:XX");
```

#### bluetooth.getProfileConnState(deprecated)

getProfileConnState(profileId: ProfileId): ProfileConnectionState

依据ProfileId获取指定profile的连接状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/vZcbYO0dT4WXYKkUTrb3ng/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=A53A9035262864D5BB7DA7C75A35349731428D03BE85F70A483B174AD803F582)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.getProfileConnectionState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#bluetoothmanagergetprofileconnectionstatedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| profileId | ProfileId | 是 | 表示profile的枚举值，例如：PROFILE\_A2DP\_SOURCE。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [ProfileConnectionState](#profileconnectionstatedeprecated) | profile的连接状态。 |

**示例：**

```js
let result : bluetooth.ProfileConnectionState = bluetooth.getProfileConnState(bluetooth.ProfileId.PROFILE_A2DP_SOURCE);
```

#### bluetooth.getRemoteDeviceName(deprecated)

getRemoteDeviceName(deviceId: string): string

获取对端蓝牙设备的名称。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/TSIao9kYTNOFO8MjKdE7Ig/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=F47CC57195F53786AF19CEBDB18DAE445944DEB69394DB84BE225CB3736C9A0E)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.getRemoteDeviceName](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#bluetoothmanagergetremotedevicenamedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| deviceId | string | 是 | 表示远程设备的地址，例如："XX:XX:XX:XX:XX:XX"。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 以字符串格式返回设备名称。 |

**示例：**

```js
let remoteDeviceName : string = bluetooth.getRemoteDeviceName("XX:XX:XX:XX:XX:XX");
```

#### bluetooth.getRemoteDeviceClass(deprecated)

getRemoteDeviceClass(deviceId: string): DeviceClass

获取对端蓝牙设备的类别。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/Eb6dHH2sR-6tazBsfaA7Iw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=89940EFD103887F19D4E23522AAA45368B22CAE4EAA9B9DBDE54161970A78600)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.getRemoteDeviceClass](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#bluetoothmanagergetremotedeviceclassdeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| deviceId | string | 是 | 表示远程设备的地址，例如："XX:XX:XX:XX:XX:XX"。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [DeviceClass](#deviceclassdeprecated) | 远程设备的类别。 |

**示例：**

```js
let remoteDeviceClass : bluetooth.DeviceClass = bluetooth.getRemoteDeviceClass("XX:XX:XX:XX:XX:XX");
```

#### bluetooth.getPairedDevices(deprecated)

getPairedDevices(): Array<string>

获取蓝牙配对列表。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/5C3_tcLjSbyIQpo0gn_zrQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=407755BF4CB4BF6B5F5F04BCFC38735BDCD075322A2BAA1055459F92B41E5B3F)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.getPairedDevices](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#bluetoothmanagergetpaireddevicesdeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Array<string> | 已配对蓝牙设备的地址列表。 |

**示例：**

```js
let devices : Array<string> = bluetooth.getPairedDevices();
```

#### bluetooth.setBluetoothScanMode(deprecated)

setBluetoothScanMode(mode: ScanMode, duration: number): boolean

设置蓝牙扫描模式，可以被远端设备发现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/PutT0cV1Quy032hnMqs5Og/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=F7B92C3D0AA068ADD66EE8A72037DA4C49EE17DF9ACF1BDD3132F79DBD877617)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.setBluetoothScanMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#bluetoothmanagersetbluetoothscanmodedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| mode | [ScanMode](#scanmodedeprecated) | 是 | 蓝牙扫描模式。 |
| duration | number | 是 | 设备可被发现的持续时间，单位为毫秒；设置为0则持续可发现。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 设置蓝牙扫描，成功返回true，否则返回false。 |

**示例：**

```js
// 设置为可连接可发现才可被远端设备扫描到，可以连接。
let result : boolean = bluetooth.setBluetoothScanMode(bluetooth.ScanMode
    .SCAN_MODE_CONNECTABLE_GENERAL_DISCOVERABLE, 100);
```

#### bluetooth.getBluetoothScanMode(deprecated)

getBluetoothScanMode(): ScanMode

获取蓝牙扫描模式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/bahwWcMJT4iZb3L9JoIj0g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=96FAC5DFA2A182610105D25885EEEF27A0379BB6928E1E461CC1C2FC611A60F2)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.getBluetoothScanMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#bluetoothmanagergetbluetoothscanmodedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [ScanMode](#scanmodedeprecated) | 蓝牙扫描模式。 |

**示例：**

```js
let scanMode : bluetooth.ScanMode = bluetooth.getBluetoothScanMode();
```

#### bluetooth.startBluetoothDiscovery(deprecated)

startBluetoothDiscovery(): boolean

开启蓝牙扫描，可以发现远端设备。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/7zFEfHbyQlmjerOFtN7VPQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=C81A934C7CF4ACA59622B546FF90ED29C357D60AB3C4C7F42021D3DB1E92394C)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.startBluetoothDiscovery](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#bluetoothmanagerstartbluetoothdiscoverydeprecated)替代。

**需要权限**：ohos.permission.DISCOVER\_BLUETOOTH 和 ohos.permission.LOCATION

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 开启蓝牙扫描，成功返回true，否则返回false。 |

**示例：**

```js
let deviceId : Array<string>;
function onReceiveEvent(data : Array<string>) {
    deviceId = data;
}
bluetooth.on('bluetoothDeviceFind', onReceiveEvent);
let result : boolean = bluetooth.startBluetoothDiscovery();
```

#### bluetooth.stopBluetoothDiscovery(deprecated)

stopBluetoothDiscovery(): boolean

关闭蓝牙扫描。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/VXlTc7bHRcGa8zXcbHIPEg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=BF5EA238BB4F44D8B50FCF80857765772B19F3F4FC31006D998365E16CB38FF8)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.stopBluetoothDiscovery](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#bluetoothmanagerstopbluetoothdiscoverydeprecated)替代。

**需要权限**：ohos.permission.DISCOVER\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 关闭蓝牙扫描，成功返回true，否则返回false。 |

**示例：**

```js
let result : boolean = bluetooth.stopBluetoothDiscovery();
```

#### bluetooth.setDevicePairingConfirmation(deprecated)

setDevicePairingConfirmation(device: string, accept: boolean): boolean

设置设备配对请求确认。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/PqWnFRfWRWWrZSmzkD7kWQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=14120B2024FF57E20238362D71F9F0400AD7FE576621B313914A54D1C434DE04)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.setDevicePairingConfirmation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#bluetoothmanagersetdevicepairingconfirmationdeprecated)替代。

**需要权限**：ohos.permission.MANAGE\_BLUETOOTH（该权限仅系统应用可申请）

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| device | string | 是 | 表示远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| accept | boolean | 是 | 接受配对请求设置为true，否则设置为false。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 设置设备配对确认，成功返回true，否则返回false。 |

**示例：**

```js
// 订阅“pinRequired”配对请求事件，收到远端配对请求后设置配对确认
function onReceivePinRequiredEvent(data : bluetooth.PinRequiredParam) { // data为配对请求的入参，配对请求参数
    console.info('pin required  = '+ JSON.stringify(data));
    bluetooth.setDevicePairingConfirmation(data.deviceId, true);
}
bluetooth.on("pinRequired", onReceivePinRequiredEvent);
```

#### bluetooth.on('bluetoothDeviceFind')(deprecated)

on(type: 'bluetoothDeviceFind', callback: Callback<Array<string>>): void

订阅蓝牙设备发现上报事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/ECvGkbOMS0O0H3tbXvudcQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=58792E17ABB63AA365B67B1B455ED1FC8426DE86B0F5667C14D0B22AA315A6E2)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.on('bluetoothDeviceFind')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#bluetoothmanageronbluetoothdevicefinddeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"bluetoothDeviceFind"字符串，表示蓝牙设备发现事件。 |
| callback | Callback<Array<string>> | 是 | 表示回调函数的入参，发现的设备集合。回调函数由用户创建通过该接口注册。 |

**返回值：**

无

**示例：**

```js
function onReceiveEvent(data : Array<string>) { // data为蓝牙设备地址集合
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
bluetooth.on('bluetoothDeviceFind', onReceiveEvent);
```

#### bluetooth.off('bluetoothDeviceFind')(deprecated)

off(type: 'bluetoothDeviceFind', callback?: Callback<Array<string>>): void

取消订阅蓝牙设备发现上报事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/-m8ubqsGRxWwr3eyljg8PQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=58555219FC25AF90B2E8825BFB27439FF235A0C56023944186EF50E2777B0F67)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.off('bluetoothDeviceFind')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#bluetoothmanageroffbluetoothdevicefinddeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"bluetoothDeviceFind"字符串，表示蓝牙设备发现事件。 |
| callback | Callback<Array<string>> | 否 | 表示取消订阅蓝牙设备发现事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**返回值：**

无

**示例：**

```js
function onReceiveEvent(data : Array<string>) {
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
bluetooth.on('bluetoothDeviceFind', onReceiveEvent);
bluetooth.off('bluetoothDeviceFind', onReceiveEvent);
```

#### bluetooth.on('pinRequired')(deprecated)

on(type: 'pinRequired', callback: Callback<PinRequiredParam>): void

订阅远端蓝牙设备的配对请求事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/nW3_WKd_S82onLHE7GhvEQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=3E40288285B54C4998B0341F4D1B4FDD34814132CA6B2E5110FBB24BE663EF37)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.on('pinRequired')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#bluetoothmanageronpinrequireddeprecated)替代。

**需要权限**：ohos.permission.DISCOVER\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"pinRequired"字符串，表示配对请求事件。 |
| callback | Callback<[PinRequiredParam](#pinrequiredparamdeprecated)\> | 是 | 表示回调函数的入参，配对请求。回调函数由用户创建通过该接口注册。 |

**返回值：**

无

**示例：**

```js
function onReceiveEvent(data : bluetooth.PinRequiredParam) { // data为配对请求参数
    console.info('pin required = '+ JSON.stringify(data));
}
bluetooth.on('pinRequired', onReceiveEvent);
```

#### bluetooth.off('pinRequired')(deprecated)

off(type: 'pinRequired', callback?: Callback<PinRequiredParam>): void

取消订阅远端蓝牙设备的配对请求事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/KYogi33LTV2_hxJk51LT9Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=230241D4E7AC9B0CC6B3D72BA34C3278706EDE104F70857CD480E3BE08EB2883)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.off('pinRequired')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#bluetoothmanageroffpinrequireddeprecated)替代。

**需要权限**：ohos.permission.DISCOVER\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"pinRequired"字符串，表示配对请求事件。 |
| callback | Callback<[PinRequiredParam](#pinrequiredparamdeprecated)\> | 否 | 表示取消订阅蓝牙配对请求事件上报，入参为配对请求参数。不填该参数则取消订阅该type对应的所有回调。 |

**返回值：**

无

**示例：**

```js
function onReceiveEvent(data : bluetooth.PinRequiredParam) {
    console.info('pin required = '+ JSON.stringify(data));
}
bluetooth.on('pinRequired', onReceiveEvent);
bluetooth.off('pinRequired', onReceiveEvent);
```

#### bluetooth.on('bondStateChange')(deprecated)

on(type: 'bondStateChange', callback: Callback<BondStateParam>): void

订阅蓝牙配对状态改变事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/zkyOWpd3S26Mr6KjmG78_A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=4BE5BA9EFDA97CDF52CD78C694311E12D99D1DAFB5AF5027ED46053DAA964878)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.on('bondStateChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#bluetoothmanageronbondstatechangedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"bondStateChange"字符串，表示蓝牙配对状态改变事件。 |
| callback | Callback<[BondStateParam](#bondstateparamdeprecated)\> | 是 | 表示回调函数的入参，配对的状态。回调函数由用户创建通过该接口注册。 |

**返回值：**

无

**示例：**

```js
function onReceiveEvent(data : bluetooth.BondStateParam) { // data为回调函数入参，表示配对的状态
    console.info('pair state = '+ JSON.stringify(data));
}
bluetooth.on('bondStateChange', onReceiveEvent);
```

#### bluetooth.off('bondStateChange')(deprecated)

off(type: 'bondStateChange', callback?: Callback<BondStateParam>): void

取消订阅蓝牙配对状态改变事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/cttletp2Q-m77ecUrRyCOw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=4918D945B242BCE62C1DFBE66FA63214050246479D4F27BB99E2BFAF20A2BCFD)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.off('bondStateChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#bluetoothmanageroffbondstatechangedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"bondStateChange"字符串，表示蓝牙配对状态改变事件。 |
| callback | Callback<[BondStateParam](#bondstateparamdeprecated)\> | 否 | 表示取消订阅蓝牙配对状态改变事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**返回值：**

无

**示例：**

```js
function onReceiveEvent(data : bluetooth.BondStateParam) {
    console.info('bond state = '+ JSON.stringify(data));
}
bluetooth.on('bondStateChange', onReceiveEvent);
bluetooth.off('bondStateChange', onReceiveEvent);
```

#### bluetooth.on('stateChange')(deprecated)

on(type: 'stateChange', callback: Callback<BluetoothState>): void

订阅蓝牙连接状态改变事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/Y5Ltu-sCRcqB-q4pmL6yCA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=9DB9EA4E0F7811DC2D8C2A2F6C887DF463637DE65079E626D5EDF31FB78B444C)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.on('stateChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#bluetoothmanageronstatechangedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"stateChange"字符串，表示蓝牙状态改变事件。 |
| callback | Callback<[BluetoothState](#bluetoothstatedeprecated)\> | 是 | 表示回调函数的入参，蓝牙状态。回调函数由用户创建通过该接口注册。 |

**返回值：**

无

**示例：**

```js
function onReceiveEvent(data : bluetooth.BluetoothState) {
    console.info('bluetooth state = '+ JSON.stringify(data));
}
bluetooth.on('stateChange', onReceiveEvent);
```

#### bluetooth.off('stateChange')(deprecated)

off(type: 'stateChange', callback?: Callback<BluetoothState>): void

取消订阅蓝牙连接状态改变事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/mGrn5ta5Sc27gFzk6VtD6A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=A087A354EE976981EDCDD11C821DF25DDFD0ECFFFE77346E085786B367FBC08B)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.off('stateChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#bluetoothmanageroffstatechangedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"stateChange"字符串，表示蓝牙状态改变事件。 |
| callback | Callback<[BluetoothState](#bluetoothstatedeprecated)\> | 否 | 表示取消订阅蓝牙状态改变事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**返回值：**

无

**示例：**

```js
function onReceiveEvent(data : bluetooth.BluetoothState) {
    console.info('bluetooth state = '+ JSON.stringify(data));
}
bluetooth.on('stateChange', onReceiveEvent);
bluetooth.off('stateChange', onReceiveEvent);
```

#### bluetooth.sppListen(deprecated)

sppListen(name: string, option: SppOption, callback: AsyncCallback<number>): void

创建一个服务端监听Socket。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/FnVkYXpxRR-ZYoVUe-drFQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=62ACF15C34E60C9CAF34E17ECC7DE74AD1F24FAED5AA70423C24CF124E88890C)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.sppListen](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#bluetoothmanagerspplistendeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 服务的名称。 |
| option | [SppOption](#sppoptiondeprecated) | 是 | spp监听配置参数。 |
| callback | AsyncCallback<number> | 是 | 表示回调函数的入参，服务端Socket的id。 |

**示例：**

```js
import { BusinessError } from '@kit.BasicServicesKit';
let serverNumber = -1;
function serverSocket(code : BusinessError, number : number) {
  console.info(`bluetooth error code: ${code.code}`);
  if (code.code == 0) {
    console.info(`bluetooth serverSocket Number: ${number}`);
    serverNumber = number;
  }
}

let sppOption : bluetooth.SppOption = {uuid: '00001810-0000-1000-8000-00805F9B34FB', secure: false, type: 0};
bluetooth.sppListen('server1', sppOption, serverSocket);
```

#### bluetooth.sppAccept(deprecated)

sppAccept(serverSocket: number, callback: AsyncCallback<number>): void

服务端监听socket等待客户端连接。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/GsAnCZdyRbqISlF3ykjRGg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=B853314810D93E8E7FB46F856611B1B8929A68A1C5BDBB6E2B90F3C4D6F32669)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.sppAccept](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#bluetoothmanagersppacceptdeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| serverSocket | number | 是 | 服务端socket的id。 |
| callback | AsyncCallback<number> | 是 | 表示回调函数的入参，客户端socket的id。 |

**示例：**

```js
import { BusinessError } from '@kit.BasicServicesKit';
let serverNumber = -1;
function serverSocket(code : BusinessError, number : number) {
  console.info(`bluetooth error code: ${code.code}`);
  if (code.code == 0) {
    console.info(`bluetooth serverSocket Number: ${number}`);
    serverNumber = number;
  }
}
let clientNumber = -1;
function acceptClientSocket(code : BusinessError, number : number) {
  console.info(`bluetooth error code: ${code.code}`);
  if (code.code == 0) {
    console.info(`bluetooth clientSocket Number: ${number}`);
    // 获取的clientNumber用作服务端后续读/写操作socket的id。
    clientNumber = number;
  }
}
bluetooth.sppAccept(serverNumber, acceptClientSocket);
```

#### bluetooth.sppConnect(deprecated)

sppConnect(device: string, option: SppOption, callback: AsyncCallback<number>): void

客户端向远端设备发起spp连接。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/7aiOXYgGSbm1hKDJOJAOEw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=90E4988075CD55BE69A816D60EB466BEA97DC44F126B25A492708DF428FE9299)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.sppConnect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#bluetoothmanagersppconnectdeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| device | string | 是 | 对端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| option | [SppOption](#sppoptiondeprecated) | 是 | spp客户端连接配置参数。 |
| callback | AsyncCallback<number> | 是 | 表示回调函数的入参，客户端socket的id。 |

**示例：**

```js
import { BusinessError } from '@kit.BasicServicesKit';
let clientNumber = -1;
function clientSocket(code : BusinessError, number : number) {
  if (code == null || code.code != 0) {
    return;
  }
  console.info(`bluetooth serverSocket Number: ${number}`);
  // 获取的clientNumber用作客户端后续读/写操作socket的id。
  clientNumber = number;
}
let sppOption : bluetooth.SppOption = {uuid: '00001810-0000-1000-8000-00805F9B34FB', secure: false, type: 0};
bluetooth.sppConnect('XX:XX:XX:XX:XX:XX', sppOption, clientSocket);
```

#### bluetooth.sppCloseServerSocket(deprecated)

sppCloseServerSocket(socket: number): void

关闭服务端监听Socket，入参socket由sppListen接口返回。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/YMmoe57iTQG8UtcsKFIGWA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=30F9A97BDEEB879B1079D92983B743036195BA7DD37C93EF77F50DE65A0A28A0)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.sppCloseServerSocket](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#bluetoothmanagersppcloseserversocketdeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| socket | number | 是 | 服务端监听socket的id。 |

**示例：**

```js
import { BusinessError } from '@kit.BasicServicesKit';
let serverNumber = -1;
function serverSocket(code : BusinessError, number : number) {
  console.info(`bluetooth error code: ${code.code}`);
  if (code.code == 0) {
    console.info(`bluetooth serverSocket Number: ${number}`);
    serverNumber = number;
  }
}
bluetooth.sppCloseServerSocket(serverNumber);
```

#### bluetooth.sppCloseClientSocket(deprecated)

sppCloseClientSocket(socket: number): void

关闭客户端socket，入参socket由sppAccept或sppConnect接口获取。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/Ia-tYbPFTGaNz1v_oZ_oww/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=62A0861FB916A719D736039ABC30006F8992F1197BB671512350C0B09E6A2E80)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.sppCloseClientSocket](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#bluetoothmanagersppcloseclientsocketdeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| socket | number | 是 | 客户端socket的id。 |

**示例：**

```js
import { BusinessError } from '@kit.BasicServicesKit';
let clientNumber = -1;
function clientSocket(code : BusinessError, number : number) {
  if (code == null || code.code != 0) {
    return;
  }
  console.info(`bluetooth serverSocket Number: ${number}`);
  // 获取的clientNumber用作客户端后续读/写操作socket的id。
  clientNumber = number;
}
bluetooth.sppCloseClientSocket(clientNumber);
```

#### bluetooth.sppWrite(deprecated)

sppWrite(clientSocket: number, data: ArrayBuffer): boolean

通过socket向远端发送数据，入参clientSocket由sppAccept或sppConnect接口获取 。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/c4U_p55uQ926CsxXRyxoMQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=516693DC43ED3D67CF3B424CDF4FB5A7BE6D6401D929F964BB5CF4F9BF4605B6)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.sppWrite](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#bluetoothmanagersppwritedeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| clientSocket | number | 是 | 客户端socket的id。 |
| data | ArrayBuffer | 是 | 写入的数据。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 写数据操作，成功返回true，否则返回false。 |

**示例：**

```js
import { BusinessError } from '@kit.BasicServicesKit';
let clientNumber = -1;
function clientSocket(code : BusinessError, number : number) {
  if (code == null || code.code != 0) {
    return;
  }
  console.info(`bluetooth serverSocket Number: ${number}`);
  // 获取的clientNumber用作客户端后续读/写操作socket的id。
  clientNumber = number;
}
let arrayBuffer = new ArrayBuffer(8);
let data = new Uint8Array(arrayBuffer);
data[0] = 123;
let ret : boolean = bluetooth.sppWrite(clientNumber, arrayBuffer);
if (ret) {
  console.info('spp write successfully');
} else {
  console.error('spp write failed');
}
```

#### bluetooth.on('sppRead')(deprecated)

on(type: 'sppRead', clientSocket: number, callback: Callback<ArrayBuffer>): void

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/--AKrwjHTGmJcdxHpwlLlw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=C03E4A3EEC2056483753DA08E2245AB1A7BCBF5C57011C54C26C873CF8D9A260)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.on('sppRead')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#bluetoothmanageronsppreaddeprecated)替代。

订阅spp读请求事件，入参clientSocket由sppAccept或sppConnect接口获取。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"sppRead"字符串，表示spp读请求事件。 |
| clientSocket | number | 是 | 客户端socket的id。 |
| callback | Callback<ArrayBuffer> | 是 | 表示回调函数的入参，读取到的数据。 |

**返回值：**

无

**示例：**

```js
import { BusinessError } from '@kit.BasicServicesKit';
let clientNumber = -1;
function clientSocket(code : BusinessError, number : number) {
  if (code == null || code.code != 0) {
    return;
  }
  console.info(`bluetooth serverSocket Number: ${number}`);
  // 获取的clientNumber用作客户端后续读/写操作socket的id。
  clientNumber = number;
}
function dataRead(dataBuffer : ArrayBuffer) {
  let data = new Uint8Array(dataBuffer);
}
bluetooth.on('sppRead', clientNumber, dataRead);
```

#### bluetooth.off('sppRead')(deprecated)

off(type: 'sppRead', clientSocket: number, callback?: Callback<ArrayBuffer>): void

取消订阅spp读请求事件，入参clientSocket由sppAccept或sppConnect接口获取。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/OSxKcQn8RAi9Pka3Zc6_7w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=81FF362C1A78A58EF916F38EFCF33C12502C3C10137E33A645F58BE775A10285)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.off('sppRead')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#bluetoothmanageroffsppreaddeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"sppRead"字符串，表示spp读请求事件。 |
| clientSocket | number | 是 | 客户端Socket的id。 |
| callback | Callback<ArrayBuffer> | 否 | 表示取消订阅spp读请求事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**返回值：**

无

**示例：**

```js
import { BusinessError } from '@kit.BasicServicesKit';
let clientNumber = -1;
function clientSocket(code : BusinessError, number : number) {
  if (code == null || code.code != 0) {
    return;
  }
  console.info(`bluetooth serverSocket Number: ${number}`);
  // 获取的clientNumber用作客户端后续读/写操作socket的id。
  clientNumber = number;
}
bluetooth.off('sppRead', clientNumber);
```

#### bluetooth.getProfile(deprecated)

getProfile(profileId: ProfileId): A2dpSourceProfile | HandsFreeAudioGatewayProfile

通过ProfileId，获取profile的对象实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/PHsc1s-gSFyqtPqL-D2DIQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=8FBB9875C436719C792CB1767178911ADF3FA7B9445DAC9CCCA3F6AF0A75BA62)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.getProfileInstance](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#bluetoothmanagergetprofileinstancedeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| profileId | [ProfileId](#profileiddeprecated) | 是 | 表示profile的枚举值，例如：PROFILE\_A2DP\_SOURCE。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [A2dpSourceProfile](#a2dpsourceprofile) | [HandsFreeAudioGatewayProfile](#handsfreeaudiogatewayprofile) | 对应的profile的对象实例，当前支持A2dpSourceProfile， HandsFreeAudioGatewayProfile。 |

**示例：**

```js
let a2dpSrc : bluetooth.A2dpSourceProfile = bluetooth.getProfile(bluetooth.ProfileId.PROFILE_A2DP_SOURCE) as bluetooth.A2dpSourceProfile;
```

#### BLE

#### \[h2\]createGattServer(deprecated)

createGattServer(): GattServer

创建一个可使用的GattServer实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/nka2Ouk6Sk60YOXjcAsOCA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=75B0E935A2FD22C1526EF0E3626ABDA206B16F1101F7401563D12EC806D71736)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.BLE.createGattServer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#creategattserverdeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [GattServer](#gattserver) | server端类，使用server端方法之前需要创建该类的实例进行操作。 |

**示例：**

```js
let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
```

#### \[h2\]createGattClientDevice(deprecated)

createGattClientDevice(deviceId: string): GattClientDevice

创建一个可使用的GattClientDevice实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/mxFyoiAHRgqia5pHEcd5Xw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=8B08A8098A10C1BF313DCA5F8C398F9F733D7F37A9614F2BB9CF7331990A91FD)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.BLE.createGattClientDevice](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#creategattclientdevicedeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| deviceId | string | 是 | 对端设备地址， 例如："XX:XX:XX:XX:XX:XX"。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [GattClientDevice](#gattclientdevice) | client端类，使用client端方法之前需要创建该类的实例进行操作。 |

**示例：**

```js
let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
```

#### \[h2\]getConnectedBLEDevices(deprecated)

getConnectedBLEDevices(): Array<string>

获取和当前设备连接的BLE设备。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/LFlWEOzHQUGTWPqhzAtpLQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=EB27E207EF3A36643171EC8D97720135AD4FAD5520077EA4A7BF719A35EADCF6)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.BLE.getConnectedBLEDevices](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#getconnectedbledevicesdeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Array<string> | 返回当前设备作为Server端时连接BLE设备地址集合。 |

**示例：**

```js
let result : Array<string> = bluetooth.BLE.getConnectedBLEDevices();
```

#### \[h2\]startBLEScan(deprecated)

startBLEScan(filters: Array<ScanFilter>, options?: ScanOptions): void

发起BLE扫描流程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/nEkhweOzREW39ZFWZkkNsQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=C4C08233112EF721DB7F41678EEC8F26D98082F463005C05DA8B34876BF268E8)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.BLE.startBLEScan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#startblescandeprecated)替代。

**需要权限**：ohos.permission.DISCOVER\_BLUETOOTH 和 ohos.permission.MANAGE\_BLUETOOTH（该权限仅系统应用可申请） 和 ohos.permission.LOCATION

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| filters | Array<[ScanFilter](#scanfilterdeprecated)\> | 是 | 表示扫描结果过滤策略集合，如果不使用过滤的方式，该参数设置为null。 |
| options | [ScanOptions](#scanoptionsdeprecated) | 否 | 表示扫描的参数配置，可选参数。 |

**返回值：**

无

**示例：**

```js
function onReceiveEvent(data : Array<bluetooth.ScanResult>) {
    console.info('BLE scan device find result = '+ JSON.stringify(data));
}
bluetooth.BLE.on("BLEDeviceFind", onReceiveEvent);
let scanOptions : bluetooth.ScanOptions = {
    interval: 500,
    dutyMode: bluetooth.ScanDuty.SCAN_MODE_LOW_POWER,
    matchMode: bluetooth.MatchMode.MATCH_MODE_AGGRESSIVE,
}

let scanFilter : bluetooth.ScanFilter = {
    deviceId:"XX:XX:XX:XX:XX:XX",
    name:"test",
    serviceUuid:"00001888-0000-1000-8000-00805f9b34fb"
}
bluetooth.BLE.startBLEScan(
    [scanFilter], scanOptions
);
```

#### \[h2\]stopBLEScan(deprecated)

stopBLEScan(): void

停止BLE扫描流程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/mjHOKSirR7WaKxf69Z7XuA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=0C6E3AC0DD53DA7130EFB0F31B1ABD8E584A1F040FA110CA5B5FCF25B6A55B23)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.BLE.stopBLEScan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#stopblescandeprecated)替代。

**需要权限**：ohos.permission.DISCOVER\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

无

**示例：**

```js
bluetooth.BLE.stopBLEScan();
```

#### \[h2\]on('BLEDeviceFind')(deprecated)

on(type: 'BLEDeviceFind', callback: Callback<Array<ScanResult>>): void

订阅BLE设备发现上报事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/zVLJuz4yTOirSo3qP5IlBg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=B0807ADE321C68127B2DAAC5737FEA7B09F274D7227013E9B0D58F97AE0F0C6A)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.BLE.on('BLEDeviceFind')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#onbledevicefinddeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"BLEDeviceFind"字符串，表示BLE设备发现事件。 |
| callback | Callback<Array<[ScanResult](#scanresultdeprecated)\>> | 是 | 表示回调函数的入参，发现的设备集合。回调函数由用户创建通过该接口注册。 |

**返回值：**

无

**示例：**

```js
function onReceiveEvent(data : Array<bluetooth.ScanResult>) {
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
bluetooth.BLE.on('BLEDeviceFind', onReceiveEvent);
```

#### \[h2\]off('BLEDeviceFind')(deprecated)

off(type: 'BLEDeviceFind', callback?: Callback<Array<ScanResult>>): void

取消订阅BLE设备发现上报事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/kYw6zRaQQAq2yGRL3XtTjA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=899D7E36FBF4AD90B4F53F8C369987231D5473A38A8751BB48470B66E5544FA8)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.BLE.off('BLEDeviceFind')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#offbledevicefinddeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"BLEDeviceFind"字符串，表示BLE设备发现事件。 |
| callback | Callback<Array<[ScanResult](#scanresultdeprecated)\>> | 否 | 表示取消订阅BLE设备发现事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**返回值：**

无

**示例：**

```js
function onReceiveEvent(data : Array<bluetooth.ScanResult>) {
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
bluetooth.BLE.on('BLEDeviceFind', onReceiveEvent);
bluetooth.BLE.off('BLEDeviceFind', onReceiveEvent);
```

#### BaseProfile

profile基类。

#### \[h2\]getConnectionDevices(deprecated)

getConnectionDevices(): Array<string>

获取已连接设备列表。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/Mk6UbYakSZecngWdYy11rA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=525A95EC053B4A91D5414B42A2D0928D23C590218B15F9EA9A2B4BE008A66554)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.BaseProfile.getConnectionDevices](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#getconnectiondevicesdeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Array<string> | 返回已连接设备的地址列表。 |

**示例：**

```js
let a2dpSrc : bluetooth.A2dpSourceProfile = bluetooth.getProfile(bluetooth.ProfileId.PROFILE_A2DP_SOURCE) as bluetooth.A2dpSourceProfile;
let retArray : Array<string> = a2dpSrc.getConnectionDevices();
```

#### \[h2\]getDeviceState(deprecated)

getDeviceState(device: string): ProfileConnectionState

获取设备profile的连接状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/-KWicE8_RVWKqh7BkgwcPA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=2CF8F1C0DC2208728F9D2D10AADC87F7BC55744CC7A93768CB5CF4CB2273F874)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.BaseProfile.getDeviceState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#getdevicestatedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| device | string | 是 | 远端设备地址。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [ProfileConnectionState](#profileconnectionstatedeprecated) | 返回profile的连接状态。 |

**示例：**

```js
let a2dpSrc : bluetooth.A2dpSourceProfile = bluetooth.getProfile(bluetooth.ProfileId.PROFILE_A2DP_SOURCE) as bluetooth.A2dpSourceProfile;
let ret : bluetooth.ProfileConnectionState = a2dpSrc.getDeviceState('XX:XX:XX:XX:XX:XX');
```

#### A2dpSourceProfile

使用A2dpSourceProfile方法之前需要创建该类的实例进行操作，通过getProfile()方法构造此实例。

#### \[h2\]connect(deprecated)

connect(device: string): boolean

发起设备的A2dp服务连接请求。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/T__oGXFuTa-KBWB7bAAM1w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=96FC1ABF2CB74F52ADC0B9F69B575AEA865867F90C37BBD8D29EF5E7877E1634)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.A2dpSourceProfile.connect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#connectdeprecated)替代。

**需要权限**：ohos.permission.DISCOVER\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| device | string | 是 | 远端设备地址。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 成功返回true，失败返回false。 |

**示例：**

```js
let a2dpSrc : bluetooth.A2dpSourceProfile = bluetooth.getProfile(bluetooth.ProfileId.PROFILE_A2DP_SOURCE) as bluetooth.A2dpSourceProfile;
let ret : boolean = a2dpSrc.connect('XX:XX:XX:XX:XX:XX');
```

#### \[h2\]disconnect(deprecated)

disconnect(device: string): boolean

断开设备的a2dp服务连接。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/Vn6hSSk8QHusU7QllhV8aQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=E88BBD1A4286CAED064BF9A95D25D5617F7E8A17CB954D341ABF31199C8ED875)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.A2dpSourceProfile.disconnect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#disconnectdeprecated)替代。

**需要权限**：ohos.permission.DISCOVER\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| device | string | 是 | 远端设备地址。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 成功返回true，失败返回false。 |

**示例：**

```js
let a2dpSrc : bluetooth.A2dpSourceProfile = bluetooth.getProfile(bluetooth.ProfileId.PROFILE_A2DP_SOURCE) as bluetooth.A2dpSourceProfile;
let ret : boolean = a2dpSrc.disconnect('XX:XX:XX:XX:XX:XX');
```

#### \[h2\]on('connectionStateChange')(deprecated)

on(type: 'connectionStateChange', callback: Callback<[StateChangeParam](#statechangeparamdeprecated)\>): void

订阅a2dp连接状态变化事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/L5bLgspORMWANFuXo9Uvvw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=F0A30549F8244470116C8697748438C080D154D3A79D08CB4D7493E7D4176390)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.A2dpSourceProfile.on('connectionStateChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#onconnectionstatechangedeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"connectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<[StateChangeParam](#statechangeparamdeprecated)\> | 是 | 表示回调函数的入参。 |

**返回值：**

无

**示例：**

```js
function onReceiveEvent(data : bluetooth.StateChangeParam) {
    console.info('a2dp state = '+ JSON.stringify(data));
}
let a2dpSrc : bluetooth.A2dpSourceProfile = bluetooth.getProfile(bluetooth.ProfileId.PROFILE_A2DP_SOURCE) as bluetooth.A2dpSourceProfile;
a2dpSrc.on('connectionStateChange', onReceiveEvent);
```

#### \[h2\]off('connectionStateChange')(deprecated)

off(type: 'connectionStateChange', callback?: Callback<[StateChangeParam](#statechangeparamdeprecated)\>): void

取消订阅a2dp连接状态变化事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/IdrnEIs-TqmTjU0RfEPZ6g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=6AF28ACFF385165396D5E70CF1F291376F3F68CE0331E18294C2511412626308)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.A2dpSourceProfile.off('connectionStateChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#offconnectionstatechangedeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"connectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<[StateChangeParam](#statechangeparamdeprecated)\> | 否 | 表示回调函数的入参。 |

**返回值：**

无

**示例：**

```js
function onReceiveEvent(data : bluetooth.StateChangeParam) {
    console.info('a2dp state = '+ JSON.stringify(data));
}
let a2dpSrc : bluetooth.A2dpSourceProfile = bluetooth.getProfile(bluetooth.ProfileId.PROFILE_A2DP_SOURCE) as bluetooth.A2dpSourceProfile;
a2dpSrc.on('connectionStateChange', onReceiveEvent);
a2dpSrc.off('connectionStateChange', onReceiveEvent);
```

#### \[h2\]getPlayingState(deprecated)

getPlayingState(device: string): PlayingState

获取设备的播放状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/o9M_4UsDRJ25PozxkhtPLA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=AB2E4F633D383C688CDE91CD9A1E83C158742251D32685B9DC23B3DBDA45A5EF)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.A2dpSourceProfile.getPlayingState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#getplayingstatedeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| device | string | 是 | 远端设备地址。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [PlayingState](#playingstatedeprecated) | 远端设备的播放状态。 |

**示例：**

```js
let a2dpSrc : bluetooth.A2dpSourceProfile = bluetooth.getProfile(bluetooth.ProfileId.PROFILE_A2DP_SOURCE) as bluetooth.A2dpSourceProfile;
let state : bluetooth.PlayingState = a2dpSrc.getPlayingState('XX:XX:XX:XX:XX:XX');
```

#### HandsFreeAudioGatewayProfile

使用HandsFreeAudioGatewayProfile方法之前需要创建该类的实例进行操作，通过getProfile()方法构造此实例。

#### \[h2\]connect(deprecated)

connect(device: string): boolean

连接设备的HFP服务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/j-NDSu4SQQeYLhiyZEx6mw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=7B3939E05B68EB8016E34DDB3846434E5691D815738C62AE1B51B34DBFACAEF5)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.HandsFreeAudioGatewayProfile.connect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#connectdeprecated-1)替代。

**需要权限**：ohos.permission.DISCOVER\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| device | string | 是 | 远端设备地址。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 成功返回true，失败返回false。 |

**示例：**

```js
let hfpAg : bluetooth.HandsFreeAudioGatewayProfile= bluetooth.getProfile(bluetooth.ProfileId
    .PROFILE_HANDS_FREE_AUDIO_GATEWAY);
let ret : boolean = hfpAg.connect('XX:XX:XX:XX:XX:XX');
```

#### \[h2\]disconnect(deprecated)

disconnect(device: string): boolean

断开连接设备的HFP服务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/MOO-xV8YSRGlgtIAJzShmA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=EBAD018B15B6676B705924090EA8F0D41F07811CB11156791D58085A34FB2649)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.HandsFreeAudioGatewayProfile.disconnect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#disconnectdeprecated-1)替代。

**需要权限**：ohos.permission.DISCOVER\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| device | string | 是 | 远端设备地址。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 成功返回true，失败返回false。 |

**示例：**

```js
let hfpAg : bluetooth.HandsFreeAudioGatewayProfile = bluetooth.getProfile(bluetooth.ProfileId
    .PROFILE_HANDS_FREE_AUDIO_GATEWAY);
let ret : boolean = hfpAg.disconnect('XX:XX:XX:XX:XX:XX');
```

#### \[h2\]on('connectionStateChange')(deprecated)

on(type: 'connectionStateChange', callback: Callback<[StateChangeParam](#statechangeparamdeprecated)\>): void

订阅HFP连接状态变化事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/DLXUuZu6S-mso3Tvi_IBDA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=0E8BAB0662F0971C58F2D8910058AE7C423B8729E83EACEE153BB823742FFDCB)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.HandsFreeAudioGatewayProfile.on('connectionStateChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#onconnectionstatechangedeprecated-1)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"connectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<[StateChangeParam](#statechangeparamdeprecated)\> | 是 | 表示回调函数的入参。 |

**返回值：**

无

**示例：**

```js
function onReceiveEvent(data : bluetooth.StateChangeParam) {
    console.info('hfp state = '+ JSON.stringify(data));
}
let hfpAg : bluetooth.HandsFreeAudioGatewayProfile= bluetooth.getProfile(bluetooth.ProfileId
    .PROFILE_HANDS_FREE_AUDIO_GATEWAY);
hfpAg.on('connectionStateChange', onReceiveEvent);
```

#### \[h2\]off('connectionStateChange')(deprecated)

off(type: 'connectionStateChange', callback?: Callback<[StateChangeParam](#statechangeparamdeprecated)\>): void

取消订阅HFP连接状态变化事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/vXIOqI1tRoWhbQ-kv7AK-Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=4170A96BEDAD682E2AEE5ADCCC3974E1D7D2FB42403986041F8F55FB09D7382A)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.HandsFreeAudioGatewayProfile.off('connectionStateChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#offconnectionstatechangedeprecated-1)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"connectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<[StateChangeParam](#statechangeparamdeprecated)\> | 否 | 表示回调函数的入参。 |

**返回值：**

无

**示例：**

```js
function onReceiveEvent(data : bluetooth.StateChangeParam) {
    console.info('hfp state = '+ JSON.stringify(data));
}
let hfpAg : bluetooth.HandsFreeAudioGatewayProfile= bluetooth.getProfile(bluetooth.ProfileId
    .PROFILE_HANDS_FREE_AUDIO_GATEWAY);
hfpAg.on('connectionStateChange', onReceiveEvent);
hfpAg.off('connectionStateChange', onReceiveEvent);
```

#### GattServer

server端类，使用server端方法之前需要创建该类的实例进行操作，通过createGattServer()方法构造此实例。

#### \[h2\]startAdvertising(deprecated)

startAdvertising(setting: AdvertiseSetting, advData: AdvertiseData, advResponse?: AdvertiseData): void

开始发送BLE广播。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/-xMDs3xASguPLDvioVi1IQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=8819EEC63402FC036A38CFBAA24979A887856882C5985008127C7CAD40EB0092)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattServer.startAdvertising](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#startadvertisingdeprecated)替代。

**需要权限**：ohos.permission.DISCOVER\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| setting | [AdvertiseSetting](#advertisesettingdeprecated) | 是 | BLE广播的相关参数。 |
| advData | [AdvertiseData](#advertisedatadeprecated) | 是 | BLE广播包内容。 |
| advResponse | [AdvertiseData](#advertisedatadeprecated) | 否 | BLE回复扫描请求回复响应。 |

**返回值：**

无

**示例：**

```js
let manufactureValueBuffer = new Uint8Array(4);
manufactureValueBuffer[0] = 1;
manufactureValueBuffer[1] = 2;
manufactureValueBuffer[2] = 3;
manufactureValueBuffer[3] = 4;

let serviceValueBuffer = new Uint8Array(4);
serviceValueBuffer[0] = 4;
serviceValueBuffer[1] = 6;
serviceValueBuffer[2] = 7;
serviceValueBuffer[3] = 8;
console.info('manufactureValueBuffer = '+ JSON.stringify(manufactureValueBuffer));
console.info('serviceValueBuffer = '+ JSON.stringify(serviceValueBuffer));
let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
let setting : bluetooth.AdvertiseSetting = {
    interval:150,
    txPower:60,
    connectable:true,
}

let manufactureData : bluetooth.ManufactureData = {
    manufactureId:4567,
    manufactureValue:manufactureValueBuffer.buffer
}

let serviceData : bluetooth.ServiceData = {
    serviceUuid:"00001888-0000-1000-8000-00805f9b34fb",
    serviceValue:serviceValueBuffer.buffer
}

let advData : bluetooth.AdvertiseData = {
    serviceUuids:["00001889-0000-1000-8000-00805f9b34fb"],
    manufactureData:[manufactureData],
    serviceData:[serviceData],
}

let advResponse : bluetooth.AdvertiseData = {
    serviceUuids:["00001889-0000-1000-8000-00805f9b34fb"],
    manufactureData:[manufactureData],
    serviceData:[serviceData],
}
gattServer.startAdvertising(setting, advData, advResponse);
```

#### \[h2\]stopAdvertising(deprecated)

stopAdvertising(): void

停止发送BLE广播。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/5yvKBnwTSYqmyI59v1VZMA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=DEAF6CBECB02372C36C01FC38D92CDD9722A93AC3157EDC7ED839C8C072F9BB9)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattServer.stopAdvertising](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#stopadvertisingdeprecated)替代。

**需要权限**：ohos.permission.DISCOVER\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

无

**示例：**

```js
let server : bluetooth.GattServer = bluetooth.BLE.createGattServer();
server.stopAdvertising();
```

#### \[h2\]addService(deprecated)

addService(service: GattService): boolean

server端添加服务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/SpKQSeDTT52ne2U49LkdkA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=942B1178AD4E3573A6350C0338846A0F07C6F3F64A988CF9BF58291E05FBA814)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattServer.addService](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#addservicedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| service | [GattService](#gattservicedeprecated) | 是 | 服务端的service数据。BLE广播的相关参数 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 添加服务操作，成功返回true，否则返回false。 |

**示例：**

```js
// 创建descriptors
let descriptors : Array<bluetooth.BLEDescriptor> = [];
let arrayBuffer = new ArrayBuffer(8);
let descV = new Uint8Array(arrayBuffer);
descV[0] = 11;
let descriptor : bluetooth.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
  descriptorUuid: '00002902-0000-1000-8000-00805F9B34FB', descriptorValue: arrayBuffer};
descriptors[0] = descriptor;

// 创建characteristics
let characteristics : Array<bluetooth.BLECharacteristic> = [];
let arrayBufferC = new ArrayBuffer(8);
let cccV = new Uint8Array(arrayBufferC);
cccV[0] = 1;
let characteristic : bluetooth.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB', characteristicValue: arrayBufferC, descriptors:descriptors};
let characteristicN : bluetooth.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001821-0000-1000-8000-00805F9B34FB', characteristicValue: arrayBufferC, descriptors:descriptors};
characteristics[0] = characteristic;

// 创建gattService
let gattService : bluetooth.GattService = {serviceUuid:'00001810-0000-1000-8000-00805F9B34FB', isPrimary: true, characteristics:characteristics, includeServices:[]};

let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
let ret : boolean = gattServer.addService(gattService);
if (ret) {
   console.info("add service successfully");
} else {
   console.error("add service failed");
}
```

#### \[h2\]removeService(deprecated)

removeService(serviceUuid: string): boolean

删除已添加的服务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/Yd56TVm-TFyhNynYAj7tmg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=7949B16FCC46409E57325A97933490ADFD43D63993E9DE32BDA7FB16DAEDFBCC)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattServer.removeService](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#removeservicedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| serviceUuid | string | 是 | service的UUID，例如“00001810-0000-1000-8000-00805F9B34FB”。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 删除服务操作，成功返回true，否则返回false。 |

**示例：**

```js
let server : bluetooth.GattServer = bluetooth.BLE.createGattServer();
server.removeService('00001810-0000-1000-8000-00805F9B34FB');
```

#### \[h2\]close(deprecated)

close(): void

关闭服务端功能，去注册server在协议栈的注册，调用该接口后[GattServer](#gattserver)实例将不能再使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/N1odBsX5RBWqqbR8C8djng/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=CF8945343CA7B7FE07E2A5F8CF31F271A941E2D5DB60642A5575614DB7A04CED)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattServer.close](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#closedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**示例：**

```js
let server : bluetooth.GattServer = bluetooth.BLE.createGattServer();
server.close();
```

#### \[h2\]notifyCharacteristicChanged(deprecated)

notifyCharacteristicChanged(deviceId: string, notifyCharacteristic: NotifyCharacteristic): boolean

server端特征值发生变化时，主动通知已连接的client设备。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/joMzxQpURoSYLFPvNH6nTQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=8EE8B8B54F9272829A88C72CE2DE4C188F919CE835DC53A7BBD66231D4D6165F)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattServer.notifyCharacteristicChanged](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#notifycharacteristicchangeddeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| deviceId | string | 是 | 接收通知的client端设备地址，例如“XX:XX:XX:XX:XX:XX”。 |
| notifyCharacteristic | [NotifyCharacteristic](#notifycharacteristicdeprecated) | 是 | 通知的特征值数据。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 通知操作，成功返回true，否则返回false。 |

**示例：**

```js
// 创建descriptors
let descriptors : Array<bluetooth.BLEDescriptor> = [];
let arrayBuffer = new ArrayBuffer(8);
let descV = new Uint8Array(arrayBuffer);
descV[0] = 11;
let descriptor : bluetooth.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
  descriptorUuid: '00002902-0000-1000-8000-00805F9B34FB', descriptorValue: arrayBuffer};
descriptors[0] = descriptor;
let arrayBufferC = new ArrayBuffer(8);
let characteristic : bluetooth.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB', characteristicValue: arrayBufferC, descriptors:descriptors};
let notifyCharacteristic : bluetooth.NotifyCharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001821-0000-1000-8000-00805F9B34FB', characteristicValue: characteristic.characteristicValue, confirm: false};
let server : bluetooth.GattServer = bluetooth.BLE.createGattServer();
server.notifyCharacteristicChanged('XX:XX:XX:XX:XX:XX', notifyCharacteristic);
```

#### \[h2\]sendResponse(deprecated)

sendResponse(serverResponse: ServerResponse): boolean

server端回复client端的读写请求。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/kCmvQ__GTmu3dmTLIoe-3Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=66EB1D3DB1659B312D3AA179090AB5719D97D1E7AC3C860CB9E8B52BEE4D0B30)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattServer.sendResponse](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#sendresponsedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| serverResponse | [ServerResponse](#serverresponsedeprecated) | 是 | server端回复的响应数据。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 回复响应操作，成功返回true，否则返回false。 |

**示例：**

```js
/* send response */
let arrayBufferCCC = new ArrayBuffer(8);
let cccValue = new Uint8Array(arrayBufferCCC);
cccValue[0] = 1;
let serverResponse : bluetooth.ServerResponse = {
    "deviceId": "XX:XX:XX:XX:XX:XX",
    "transId": 0,
    "status": 0,
    "offset": 0,
    "value": arrayBufferCCC,
};

let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
let ret : boolean = gattServer.sendResponse(serverResponse);
if (ret) {
  console.info('bluetooth sendResponse successfully');
} else {
  console.error('bluetooth sendResponse failed');
}
```

#### \[h2\]on('characteristicRead')(deprecated)

on(type: 'characteristicRead', callback: Callback<CharacteristicReadReq>): void

server端订阅特征值读请求事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/FRVbS5kTRx24q4tnvU5PYQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=76DDFCE8B43F868965B697E6FB979DFCE7E9964920FFE6607C12AA1603403F60)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattServer.on('characteristicRead')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#oncharacteristicreaddeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"characteristicRead"字符串，表示特征值读请求事件。 |
| callback | Callback<[CharacteristicReadReq](#characteristicreadreqdeprecated)\> | 是 | 表示回调函数的入参，client端发送的读请求数据。 |

**返回值：**

无

**示例：**

```js
let arrayBufferCCC = new ArrayBuffer(8);
let cccValue = new Uint8Array(arrayBufferCCC);
cccValue[0] = 1;
function ReadCharacteristicReq(CharacteristicReadReq : bluetooth.CharacteristicReadReq) {
  let deviceId : string = CharacteristicReadReq.deviceId;
  let transId : number = CharacteristicReadReq.transId;
  let offset : number = CharacteristicReadReq.offset;
  let characteristicUuid : string = CharacteristicReadReq.characteristicUuid;

  let serverResponse : bluetooth.ServerResponse = {deviceId: deviceId, transId: transId, status: 0,
  offset: offset, value:arrayBufferCCC};

  let ret : boolean = gattServer.sendResponse(serverResponse);
  if (ret) {
    console.info('bluetooth sendResponse successfully');
  } else {
    console.error('bluetooth sendResponse failed');
  }
}

let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
gattServer.on("characteristicRead", ReadCharacteristicReq);
```

#### \[h2\]off('characteristicRead')(deprecated)

off(type: 'characteristicRead', callback?: Callback<CharacteristicReadReq>): void

server端取消订阅特征值读请求事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/zmGZ0fNfQHmzxyYngdvHyw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=36F95F5B4721D80117A15881FA1A5EC27B9B6433FEB02BD4662F2F8637BA57A3)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattServer.off('characteristicRead')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#offcharacteristicreaddeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"characteristicRead"字符串，表示特征值读请求事件。 |
| callback | Callback<[CharacteristicReadReq](#characteristicreadreqdeprecated)\> | 否 | 表示取消订阅特征值读请求事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**返回值：**

无

**示例：**

```js
let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
gattServer.off("characteristicRead");
```

#### \[h2\]on('characteristicWrite')(deprecated)

on(type: 'characteristicWrite', callback: Callback<CharacteristicWriteReq>): void

server端订阅特征值写请求事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/aw3M3jTzRguaLioQlRZ3pA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=771BD2270A0E43507E1317617E62A1B05A110E9E1274251E776209E128A47CD8)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattServer.on('characteristicWrite')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#oncharacteristicwritedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"characteristicWrite"字符串，表示特征值写请求事件。 |
| callback | Callback<[CharacteristicWriteReq](#characteristicwritereqdeprecated)\> | 是 | 表示回调函数的入参，client端发送的写请求数据。 |

**返回值：**

无

**示例：**

```js
let arrayBufferCCC = new ArrayBuffer(8);
let cccValue = new Uint8Array(arrayBufferCCC);
function WriteCharacteristicReq(CharacteristicWriteReq : bluetooth.CharacteristicWriteReq) {
  let deviceId : string = CharacteristicWriteReq.deviceId;
  let transId : number = CharacteristicWriteReq.transId;
  let offset : number = CharacteristicWriteReq.offset;
  let isPrep : boolean = CharacteristicWriteReq.isPrep;
  let needRsp : boolean = CharacteristicWriteReq.needRsp;
  let value =  new Uint8Array(arrayBufferCCC);
  let characteristicUuid : string = CharacteristicWriteReq.characteristicUuid;

  cccValue.set(new Uint8Array(value));
  let serverResponse : bluetooth.ServerResponse = {deviceId: deviceId, transId: transId, status: 0,
  offset: offset, value:arrayBufferCCC};

  let ret : boolean = gattServer.sendResponse(serverResponse);
  if (ret) {
    console.info('bluetooth sendResponse successfully');
  } else {
    console.error('bluetooth sendResponse failed');
  }
}

let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
gattServer.on("characteristicWrite", WriteCharacteristicReq);
```

#### \[h2\]off('characteristicWrite')(deprecated)

off(type: 'characteristicWrite', callback?: Callback<CharacteristicWriteReq>): void

server端取消订阅特征值写请求事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/crEl-x4uQmGxXxu_APGP7w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=F96D082766CEA8D762BEFE544969973A5F9DA572BB70C8E28A0F772B8E5FB017)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattServer.off('characteristicWrite')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#offcharacteristicwritedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"characteristicWrite"字符串，表示特征值写请求事件。 |
| callback | Callback<[CharacteristicWriteReq](#characteristicwritereqdeprecated)\> | 否 | 表示取消订阅特征值写请求事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**返回值：**

无

**示例：**

```js
let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
gattServer.off("characteristicWrite");
```

#### \[h2\]on('descriptorRead')(deprecated)

on(type: 'descriptorRead', callback: Callback<DescriptorReadReq>): void

server端订阅描述符读请求事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/1WaT4KbSS6q56FQK0nbMFQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=A36A48963FE349D4800E2B715E69671D961B80272FD842BA6A7B60BC9E1E5FB0)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattServer.on('descriptorRead')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#ondescriptorreaddeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"descriptorRead"字符串，表示描述符读请求事件。 |
| callback | Callback<[DescriptorReadReq](#descriptorreadreqdeprecated)\> | 是 | 表示回调函数的入参，client端发送的读请求数据。 |

**返回值：**

无

**示例：**

```js
let arrayBufferDesc = new ArrayBuffer(8);
let descValue = new Uint8Array(arrayBufferDesc);
descValue[0] = 1;
function ReadDescriptorReq(DescriptorReadReq : bluetooth.DescriptorReadReq) {
  let deviceId : string = DescriptorReadReq.deviceId;
  let transId : number = DescriptorReadReq.transId;
  let offset : number = DescriptorReadReq.offset;
  let descriptorUuid : string = DescriptorReadReq.descriptorUuid;

  let serverResponse : bluetooth.ServerResponse = {deviceId: deviceId, transId: transId, status: 0,
  offset: offset, value:arrayBufferDesc};

  let ret : boolean = gattServer.sendResponse(serverResponse);
  if (ret) {
    console.info('bluetooth sendResponse successfully');
  } else {
    console.error('bluetooth sendResponse failed');
  }
}

let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
gattServer.on("descriptorRead", ReadDescriptorReq);
```

#### \[h2\]off('descriptorRead')(deprecated)

off(type: 'descriptorRead', callback?: Callback<DescriptorReadReq>): void

server端取消订阅描述符读请求事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/YmGO6YhDQ7q4kfL4glDqfQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=68C5D2565F03D369D8F9674C845B4A06DA7B35E89D058264293FFB3EDC8B5C83)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattServer.off('descriptorRead')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#offdescriptorreaddeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"descriptorRead"字符串，表示描述符读请求事件。 |
| callback | Callback<[DescriptorReadReq](#descriptorreadreqdeprecated)\> | 否 | 表示取消订阅描述符读请求事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**返回值：**

无

**示例：**

```js
let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
gattServer.off("descriptorRead");
```

#### \[h2\]on('descriptorWrite')(deprecated)

on(type: 'descriptorWrite', callback: Callback<DescriptorWriteReq>): void

server端订阅描述符写请求事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/Hat0cPsvTSSISzEj19_EgQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=AB21BCAF2B85C45853D3993212F343FA6961A3A7317A0070B42A11F4BC957FF4)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattServer.on('descriptorWrite')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#ondescriptorwritedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"descriptorWrite"字符串，表示描述符写请求事件。 |
| callback | Callback<[DescriptorWriteReq](#descriptorwritereqdeprecated)\> | 是 | 表示回调函数的入参，client端发送的写请求数据。 |

**返回值：**

无

**示例：**

```js
let arrayBufferDesc = new ArrayBuffer(8);
let descValue = new Uint8Array(arrayBufferDesc);
function WriteDescriptorReq(DescriptorWriteReq : bluetooth.DescriptorWriteReq) {
  let deviceId : string = DescriptorWriteReq.deviceId;
  let transId : number = DescriptorWriteReq.transId;
  let offset : number = DescriptorWriteReq.offset;
  let isPrep : boolean = DescriptorWriteReq.isPrep;
  let needRsp : boolean = DescriptorWriteReq.needRsp;
  let value = new Uint8Array(arrayBufferDesc);
  let descriptorUuid : string = DescriptorWriteReq.descriptorUuid;

  descValue.set(new Uint8Array(value));
  let serverResponse : bluetooth.ServerResponse = {deviceId: deviceId, transId: transId, status: 0, offset: offset, value:arrayBufferDesc};

  let ret : boolean = gattServer.sendResponse(serverResponse);
  if (ret) {
    console.info('bluetooth sendResponse successfully');
  } else {
    console.error('bluetooth sendResponse failed');
  }
}

let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
gattServer.on("descriptorWrite", WriteDescriptorReq);
```

#### \[h2\]off('descriptorWrite')(deprecated)

off(type: 'descriptorWrite', callback?: Callback<DescriptorWriteReq>): void

server端取消订阅描述符写请求事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/WA0noxOBSdagMs3MD4g-rw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=E2BFBE580DE465389718655F61C1119F89BB745C1198DA486E33FDF3A77B68C9)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattServer.off('descriptorWrite')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#offdescriptorwritedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"descriptorWrite"字符串，表示描述符写请求事件。 |
| callback | Callback<[DescriptorWriteReq](#descriptorwritereqdeprecated)\> | 否 | 表示取消订阅描述符写请求事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**返回值：**

无

**示例：**

```js
let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
gattServer.off("descriptorWrite");
```

#### \[h2\]on('connectStateChange')(deprecated)

on(type: 'connectStateChange', callback: Callback<BLEConnectChangedState>): void

server端订阅BLE连接状态变化事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/QCXS4TFuSZCzrVI7A0DBEw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=1E3EA6170603FC24F0E2EEB7783F6DBFC9EA9407A8AB0BC4FE360963A25CAD16)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattServer.on('connectStateChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#onconnectstatechangedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"connectStateChange"字符串，表示BLE连接状态变化事件。 |
| callback | Callback<[BLEConnectChangedState](#bleconnectchangedstatedeprecated)\> | 是 | 表示回调函数的入参，连接状态。 |

**返回值：**

无

**示例：**

```js
function Connected(BLEConnectChangedState : bluetooth.BLEConnectChangedState) {
  let deviceId : string = BLEConnectChangedState.deviceId;
  let status : bluetooth.ProfileConnectionState = BLEConnectChangedState.state;
}

let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
gattServer.on("connectStateChange", Connected);
```

#### \[h2\]off('connectStateChange')(deprecated)

off(type: 'connectStateChange', callback?: Callback<BLEConnectChangedState>): void

server端取消订阅BLE连接状态变化事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/qvlL6Ix9QPOuI-M6OdcJvQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=20BA3DFC30EE69946FDE09107F43672ECDB5AF8C0642BCAFCEFCD84454A966F3)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattServer.off('connectStateChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#offconnectstatechangedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"connectStateChange"字符串，表示BLE连接状态变化事件。 |
| callback | Callback<[BLEConnectChangedState](#bleconnectchangedstatedeprecated)\> | 否 | 表示取消订阅BLE连接状态变化事件。不填该参数则取消订阅该type对应的所有回调。 |

**返回值：**

无

**示例：**

```js
let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
gattServer.off("connectStateChange");
```

#### GattClientDevice

client端类，使用client端方法之前需要创建该类的实例进行操作，通过createGattClientDevice(deviceId: string)方法构造此实例。

#### \[h2\]connect(deprecated)

connect(): boolean

client端发起连接远端蓝牙低功耗设备。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/F4_vCSWuQGqmie1FZNbJhw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=80AFECABC853811CA97B8D6602D14CDB9F8C7F912D1539CA50946E50DAC0C9F1)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.connect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#connectdeprecated-1)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 连接操作成功返回true，操作失败返回false。 |

**示例：**

```js
let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
let ret : boolean = device.connect();
```

#### \[h2\]disconnect(deprecated)

disconnect(): boolean

client端断开与远端蓝牙低功耗设备的连接。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/Mjq_37SjTTKihUuNY6tc3A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=11A48FBF3EBEEAF4252FCC904E4CE262FA05E5260C01082738E0E549B73895F7)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.disconnect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#disconnectdeprecated-2)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 断开连接操作，成功返回true，操作失败返回false。 |

**示例：**

```js
let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
let ret : boolean = device.disconnect();
```

#### \[h2\]close(deprecated)

close(): boolean

关闭客户端功能，注销client在协议栈的注册，调用该接口后[GattClientDevice](#gattclientdevice)实例将不能再使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/QFBt5Fy5Suq6CXVa1GlFRw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=A80BEE0B44B32FB45A8BE20EE2EA70E62D272586C83455089E6AE02509BFD736)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.close](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#closedeprecated-1)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 关闭操作，成功返回true，操作失败返回false。 |

**示例：**

```js
let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
let ret : boolean = device.close();
```

#### \[h2\]getServices(deprecated)

getServices(callback: AsyncCallback<Array<GattService>>): void

client端获取蓝牙低功耗设备的所有服务，即服务发现 。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/N90XD9r2T1qVQgi-Z6VhQA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=452DAA6027F07D3A94B172BE0EB5019D01C6BF401A84603C17234F4EAC94C9E1)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.getServices](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#getservicesdeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[GattService](#gattservicedeprecated)\>> | 是 | client进行服务发现，通过注册回调函数获取。 |

**返回值：**

无

**示例：**

```js
import { BusinessError } from '@kit.BasicServicesKit';
// callback 模式
function getServices(code : BusinessError, gattServices : Array<bluetooth.GattService>) {
  if (code.code == 0) {
      console.info(`bluetooth code is ${code.code}`);
      console.info(`bluetooth services size is ${gattServices.length}`);

      for (let i = 0; i < gattServices.length; i++) {
        console.info(`bluetooth serviceUuid is ${gattServices[i].serviceUuid}`);
      }
  }
}

let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
device.connect();
device.getServices(getServices);
```

#### \[h2\]getServices(deprecated)

getServices(): Promise<Array<GattService>>

client端获取蓝牙低功耗设备的所有服务，即服务发现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/WfDTVS_nT3Wur9qoNSqmAw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=0EDD26C4214D3E87449160A138E2AC64554483D0CAD3B3DB7D9B819B1D628C3B)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.getServices](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#getservicesdeprecated-1)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<[GattService](#gattservicedeprecated)\>> | client进行服务发现，通过promise形式获取。 |

**示例：**

```js
// Promise 模式
let device : bluetooth.GattClientDevice= bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
device.connect();
device.getServices().then((result : Array<bluetooth.GattService>) => {
    console.info("getServices successfully:" + JSON.stringify(result));
});
```

#### \[h2\]readCharacteristicValue(deprecated)

readCharacteristicValue(characteristic: BLECharacteristic, callback: AsyncCallback<BLECharacteristic>): void

client端读取蓝牙低功耗设备特定服务的特征值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/_jCayVPIRvC8J9aFp2_Uag/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=9DA1B033A4F472A3421AFFEDC2C67601BC88CF1CE57ADB5036018DE93A146CCA)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.readCharacteristicValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#readcharacteristicvaluedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| characteristic | [BLECharacteristic](#blecharacteristicdeprecated) | 是 | 待读取的特征值。 |
| callback | AsyncCallback<[BLECharacteristic](#blecharacteristicdeprecated)\> | 是 | client读取特征值，通过注册回调函数获取。 |

**返回值：**

无

**示例：**

```js
import { BusinessError } from '@kit.BasicServicesKit';
function readCcc(code : BusinessError, BLECharacteristic : bluetooth.BLECharacteristic) {
  if (code.code != 0) {
      return;
  }
  console.info(`bluetooth characteristic uuid: ${BLECharacteristic.characteristicUuid}`);
  let value = new Uint8Array(BLECharacteristic.characteristicValue);
}

let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
let descriptors : Array<bluetooth.BLEDescriptor> = [];
let bufferDesc : ArrayBuffer = new ArrayBuffer(8);
let descV : Uint8Array = new Uint8Array(bufferDesc);
descV[0] = 11;
let descriptor : bluetooth.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB', descriptorValue: bufferDesc};
descriptors[0] = descriptor;

let bufferCCC = new ArrayBuffer(8);
let cccV = new Uint8Array(bufferCCC);
cccV[0] = 1;
let characteristic : bluetooth.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
characteristicValue: bufferCCC, descriptors:descriptors};

device.readCharacteristicValue(characteristic, readCcc);
```

#### \[h2\]readCharacteristicValue(deprecated)

readCharacteristicValue(characteristic: BLECharacteristic): Promise<BLECharacteristic>

client端读取蓝牙低功耗设备特定服务的特征值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/40m7enErQAe7Q1lvqJbO2A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=06FD73E17DC63C1ECFBD5DCBC3AD0E52930BC117CF18797B25AFA56E13050561)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.readCharacteristicValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#readcharacteristicvaluedeprecated-1)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| characteristic | [BLECharacteristic](#blecharacteristicdeprecated) | 是 | 待读取的特征值。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[BLECharacteristic](#blecharacteristicdeprecated)\> | client读取特征值，通过promise形式获取。 |

**示例：**

```js
let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
let descriptors : Array<bluetooth.BLEDescriptor> = [];
let bufferDesc = new ArrayBuffer(8);
let descV = new Uint8Array(bufferDesc);
descV[0] = 11;
let descriptor : bluetooth.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB', descriptorValue: bufferDesc};
descriptors[0] = descriptor;

let bufferCCC = new ArrayBuffer(8);
let cccV = new Uint8Array(bufferCCC);
cccV[0] = 1;
let characteristic : bluetooth.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
characteristicValue: bufferCCC, descriptors:descriptors};

device.readCharacteristicValue(characteristic);
```

#### \[h2\]readDescriptorValue(deprecated)

readDescriptorValue(descriptor: BLEDescriptor, callback: AsyncCallback<BLEDescriptor>): void

client端读取蓝牙低功耗设备特定的特征包含的描述符。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/3Ve_bpq7RBOk8lIC5RaJ0w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=8371560F0AAE03AADAF17C09C3378DD03CD27FF25611A38E18E0A6049E998900)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.readDescriptorValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#readdescriptorvaluedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| descriptor | [BLEDescriptor](#bledescriptordeprecated) | 是 | 待读取的描述符。 |
| callback | AsyncCallback<[BLEDescriptor](#bledescriptordeprecated)\> | 是 | client读取描述符，通过注册回调函数获取。 |

**返回值：**

无

**示例：**

```js
import { BusinessError } from '@kit.BasicServicesKit';
function readDesc(code : BusinessError, BLEDescriptor : bluetooth.BLEDescriptor) {
  if (code.code != 0) {
      return;
  }
  console.info(`bluetooth descriptor uuid: ${BLEDescriptor.descriptorUuid}`);
  let value = new Uint8Array(BLEDescriptor.descriptorValue);
}

let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
let bufferDesc = new ArrayBuffer(8);
let descV = new Uint8Array(bufferDesc);
descV[0] = 11;
let descriptor : bluetooth.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
  descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB', descriptorValue: bufferDesc};
device.readDescriptorValue(descriptor, readDesc);
```

#### \[h2\]readDescriptorValue(deprecated)

readDescriptorValue(descriptor: BLEDescriptor): Promise<BLEDescriptor>

client端读取蓝牙低功耗设备特定的特征包含的描述符。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/_rzwutaYTz2wGPKMef_m0A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=AD5FC1B940D061EC7E83DA687817DED606B2DA1C4F7EE6F71FA264D675E075EC)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.readDescriptorValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#readdescriptorvaluedeprecated-1)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| descriptor | [BLEDescriptor](#bledescriptordeprecated) | 是 | 待读取的描述符。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[BLEDescriptor](#bledescriptordeprecated)\> | client读取描述符，通过promise形式获取。 |

**示例：**

```js
let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
let bufferDesc = new ArrayBuffer(8);
let descV = new Uint8Array(bufferDesc);
descV[0] = 11;
let descriptor : bluetooth.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
  descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB', descriptorValue: bufferDesc};
device.readDescriptorValue(descriptor);
```

#### \[h2\]writeCharacteristicValue(deprecated)

writeCharacteristicValue(characteristic: BLECharacteristic): boolean

client端向低功耗蓝牙设备写入特定的特征值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/dF6pGM2dQPqs0TedN1OQOw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=71F758F00965A91F64D593221FF1DB27E4981BD03F7EC95429E14481FE7F9DC2)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.writeCharacteristicValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#writecharacteristicvaluedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| characteristic | [BLECharacteristic](#blecharacteristicdeprecated) | 是 | 蓝牙设备特征对应的二进制值及其它参数。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 写特征值操作成功返回true，操作失败返回false。 |

**示例：**

```js
let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
let descriptors : Array<bluetooth.BLEDescriptor> = [];
let bufferDesc = new ArrayBuffer(8);
let descV = new Uint8Array(bufferDesc);
descV[0] = 11;
let descriptor : bluetooth.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
  descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB', descriptorValue: bufferDesc};
descriptors[0] = descriptor;

let bufferCCC = new ArrayBuffer(8);
let cccV = new Uint8Array(bufferCCC);
cccV[0] = 1;
let characteristic : bluetooth.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
  characteristicValue: bufferCCC, descriptors:descriptors};
let retWriteCcc : boolean = device.writeCharacteristicValue(characteristic);
if (retWriteCcc) {
  console.info('write characteristic successfully');
} else {
  console.error('write characteristic failed');
}
```

#### \[h2\]writeDescriptorValue(deprecated)

writeDescriptorValue(descriptor: BLEDescriptor): boolean

client端向低功耗蓝牙设备特定的描述符写入二进制数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/jOeonx9uRqC2FuewDwlbBg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=7B1C5A0946756B1F76A4358400867A267DDE1A15026D5418BBD9CF0022FE6B2F)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.writeDescriptorValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#writedescriptorvaluedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| descriptor | [BLEDescriptor](#bledescriptordeprecated) | 是 | 蓝牙设备描述符的二进制值及其它参数。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 写描述符操作成功返回true，操作失败返回false。 |

**示例：**

```js
let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
let bufferDesc = new ArrayBuffer(8);
let descV = new Uint8Array(bufferDesc);
descV[0] = 22;
let descriptor : bluetooth.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
  descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB', descriptorValue: bufferDesc};
let retWriteDesc : boolean = device.writeDescriptorValue(descriptor);
if (retWriteDesc) {
  console.info('bluetooth write descriptor successfully');
} else {
  console.error('bluetooth write descriptor failed');
}
```

#### \[h2\]setBLEMtuSize(deprecated)

setBLEMtuSize(mtu: number): boolean

client协商远端蓝牙低功耗设备的最大传输单元（Maximum Transmission Unit, MTU），调用[connect](#connectdeprecated)接口连接成功后才能使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/2fRVOyk_SKmwmxC7quOS0A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=BC2560E0DDE49965C1EF8AFB50503EEE4993142FDC00CB4B0D5E04FD7BE30C73)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.setBLEMtuSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#setblemtusizedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| mtu | number | 是 | 设置范围为22~512字节。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | MTU协商操作成功返回true，操作失败返回false。 |

**示例：**

```js
let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
device.setBLEMtuSize(128);
```

#### \[h2\]setNotifyCharacteristicChanged(deprecated)

setNotifyCharacteristicChanged(characteristic: BLECharacteristic, enable: boolean): boolean

向服务端发送设置通知此特征值请求。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/AY5ZG7ghT0KZyo6PcJmWqw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=017CC7E1511F6DA634D5D93CAFAE2A1E9B67E9DE9F1C11C0F387B17365E72B66)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.setNotifyCharacteristicChanged](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#setnotifycharacteristicchangeddeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| characteristic | [BLECharacteristic](#blecharacteristicdeprecated) | 是 | 蓝牙低功耗特征。 |
| enable | boolean | 是 | 启用接收notify设置为true，否则设置为false。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 设置操作成功返回true，操作失败返回false。 |

**示例：**

```js
// 创建descriptors
let descriptors : Array<bluetooth.BLEDescriptor> = [];
let arrayBuffer = new ArrayBuffer(8);
let descV = new Uint8Array(arrayBuffer);
descV[0] = 11;
let descriptor : bluetooth.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
  descriptorUuid: '00002902-0000-1000-8000-00805F9B34FB', descriptorValue: arrayBuffer};
descriptors[0] = descriptor;
let arrayBufferC = new ArrayBuffer(8);
let characteristic : bluetooth.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB', characteristicValue: arrayBufferC, descriptors:descriptors};
let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
device.setNotifyCharacteristicChanged(characteristic, false);
```

#### \[h2\]on('BLECharacteristicChange')(deprecated)

on(type: 'BLECharacteristicChange', callback: Callback<BLECharacteristic>): void

订阅蓝牙低功耗设备的特征值变化事件。需要先调用setNotifyCharacteristicChanged接口才能接收server端的通知。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/_MRgB13TScal5cDZ9GwS9A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=89A74CBEB6DA1BCE26D70B5A9C986C9248483F267EB49E344D801A52C7E40C21)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.on('BLECharacteristicChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#onblecharacteristicchangedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"BLECharacteristicChange"字符串，表示特征值变化事件。 |
| callback | Callback<[BLECharacteristic](#blecharacteristicdeprecated)\> | 是 | 表示蓝牙低功耗设备的特征值变化事件的回调函数。 |

**返回值：**

无

**示例：**

```js
function CharacteristicChange(CharacteristicChangeReq : bluetooth.BLECharacteristic) {
  let serviceUuid : string = CharacteristicChangeReq.serviceUuid;
  let characteristicUuid : string = CharacteristicChangeReq.characteristicUuid;
  let value = new Uint8Array(CharacteristicChangeReq.characteristicValue);
}
let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
device.on('BLECharacteristicChange', CharacteristicChange);
```

#### \[h2\]off('BLECharacteristicChange')(deprecated)

off(type: 'BLECharacteristicChange', callback?: Callback<BLECharacteristic>): void

取消订阅蓝牙低功耗设备的特征值变化事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/UZEgR4C7Q6u96HbKnFXcPA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=CE7A138FF0095377E7C682E5F0C8BFF861A4A945F96631516E51BEA94CD0039B)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.off('BLECharacteristicChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#offblecharacteristicchangedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"BLECharacteristicChange"字符串，表示特征值变化事件。 |
| callback | Callback<[BLECharacteristic](#blecharacteristicdeprecated)\> | 否 | 表示取消订阅蓝牙低功耗设备的特征值变化事件。不填该参数则取消订阅该type对应的所有回调。 |

**返回值：**

无

**示例：**

```js
let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
device.off('BLECharacteristicChange');
```

#### \[h2\]on('BLEConnectionStateChange')(deprecated)

on(type: 'BLEConnectionStateChange', callback: Callback<BLEConnectChangedState>): void

client端订阅蓝牙低功耗设备的连接状态变化事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/aviFyWw8RtS0zCnEJ5UX3w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=35B4D897C771079DBD76297E38C0E4E0406B9E3ABE66FE73037997B973B4721A)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.on('BLEConnectionStateChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#onbleconnectionstatechangedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"BLEConnectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<[BLEConnectChangedState](#bleconnectchangedstatedeprecated)\> | 是 | 表示连接状态，已连接或断开。 |

**返回值：**

无

**示例：**

```js
function ConnectStateChanged(state : bluetooth.BLEConnectChangedState) {
  console.info('bluetooth connect state changed');
  let connectState : bluetooth.ProfileConnectionState = state.state;
}
let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
device.on('BLEConnectionStateChange', ConnectStateChanged);
```

#### \[h2\]off('BLEConnectionStateChange')(deprecated)

off(type: 'BLEConnectionStateChange', callback?: Callback<BLEConnectChangedState>): void

取消订阅蓝牙低功耗设备的连接状态变化事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/PtnGNnokTnSs1kgA723Yiw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=15A293F43F78D281738C1D6BE1EA3E9E41A84E3C33AEE4FEAA228BB847D8DF4D)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.off('BLEConnectionStateChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#offbleconnectionstatechangedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"BLEConnectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<[BLEConnectChangedState](#bleconnectchangedstatedeprecated)\> | 否 | 表示取消订阅蓝牙低功耗设备的连接状态变化事件。不填该参数则取消订阅该type对应的所有回调。 |

**返回值：**

无

**示例：**

```js
let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
device.off('BLEConnectionStateChange');
```

#### \[h2\]getDeviceName(deprecated)

getDeviceName(callback: AsyncCallback<string>): void

client获取远端蓝牙低功耗设备名。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/zLMe5_xTQJm1m69iHn3hgg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=3B565D6D7F21D815EFA48AB58AA5A178296AA8DB53C975AF3198BF697B4C9BF7)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.getDeviceName](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#getdevicenamedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<string> | 是 | client获取对端server设备名，通过注册回调函数获取。 |

**返回值：**

无

**示例：**

```js
import { BusinessError } from '@ohos.base';
// callback
let gattClient : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice("XX:XX:XX:XX:XX:XX");
let deviceName : void = gattClient.getDeviceName((err : BusinessError, data : string)=> {
    console.info('device name err ' + JSON.stringify(err));
    console.info('device name' + JSON.stringify(data));
})
```

#### \[h2\]getDeviceName(deprecated)

getDeviceName(): Promise<string>

client获取远端蓝牙低功耗设备名。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/vuptxuj0SIK-PiYAJFbqvQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=AC41B8BB05A9E999F8EBAF738ECF43E5379FF05C88D0CC64999213FACCBDFF38)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.getDeviceName](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#getdevicenamedeprecated-1)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | client获取对端server设备名，通过promise形式获取。 |

**示例：**

```js
// promise
let gattClient : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice("XX:XX:XX:XX:XX:XX");
gattClient.getDeviceName().then((data) => {
    console.info('device name' + JSON.stringify(data));
})
```

#### \[h2\]getRssiValue(deprecated)

getRssiValue(callback: AsyncCallback<number>): void

client获取远端蓝牙低功耗设备的信号强度 (Received Signal Strength Indication, RSSI)，调用[connect](#connectdeprecated)接口连接成功后才能使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/1r8zpNZQTzW4M1cFk3by1A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=78F11C5D468593ED64F17CFFCA3E8554C8E7BB9A4B232B210CE52184E7F61C69)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.getRssiValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#getrssivaluedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | 是 | 返回信号强度，单位 dBm，通过注册回调函数获取。 |

**返回值：**

无

**示例：**

```js
import { BusinessError } from '@ohos.base';
// callback
let gattClient : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice("XX:XX:XX:XX:XX:XX");
let ret : boolean = gattClient.connect();
gattClient.getRssiValue((err : BusinessError, data : number)=> {
    console.info('rssi err ' + JSON.stringify(err));
    console.info('rssi value' + JSON.stringify(data));
})
```

#### \[h2\]getRssiValue(deprecated)

getRssiValue(): Promise<number>

client获取远端蓝牙低功耗设备的信号强度 (Received Signal Strength Indication, RSSI)，调用[connect](#connectdeprecated)接口连接成功后才能使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/jn5zVX2oQLOlZyiBTzutMw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=A8756A7DD303DF790DAF73881D0C3154A547621A8C37FFE963155BBC4AA1D0B5)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.getRssiValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#getrssivaluedeprecated-1)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | 返回信号强度，单位 dBm，通过promise形式获取。 |

**示例：**

```js
// promise
let gattClient : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice("XX:XX:XX:XX:XX:XX");
gattClient.getRssiValue().then((data : number) => {
    console.info('rssi' + JSON.stringify(data));
})
```

#### ScanMode(deprecated)

枚举，扫描模式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/bLxtlPD6QJiXt4TMcJli8A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=40F8BF69995ED187E2AE087537113452AEE4D22479AB34BBC6401E76EF409245)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.ScanMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#scanmodedeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| SCAN\_MODE\_NONE | 0 | 没有扫描模式。 |
| SCAN\_MODE\_CONNECTABLE | 1 | 可连接扫描模式。 |
| SCAN\_MODE\_GENERAL\_DISCOVERABLE | 2 | general发现模式。 |
| SCAN\_MODE\_LIMITED\_DISCOVERABLE | 3 | limited发现模式。 |
| SCAN\_MODE\_CONNECTABLE\_GENERAL\_DISCOVERABLE | 4 | 可连接general发现模式。 |
| SCAN\_MODE\_CONNECTABLE\_LIMITED\_DISCOVERABLE | 5 | 可连接limited发现模式。 |

#### BondState(deprecated)

枚举，配对状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/rpOPIwAwQf2XJxzrenHNpA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=3A549A2F88B9E0A238606FAA873FDCDEB82A91AD52C43D1A63AD7042B7E8ABC2)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.BondState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#bondstatedeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| BOND\_STATE\_INVALID | 0 | 无效的配对。 |
| BOND\_STATE\_BONDING | 1 | 正在配对。 |
| BOND\_STATE\_BONDED | 2 | 已配对。 |

#### SppOption(deprecated)

描述spp的配置参数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/kSrfgffaTXOaZ3BkDsA9bw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=646B5649C361861E4774CC265980DECA378187FD4C2AC50C08724FE303FA3182)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.SppOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#sppoptiondeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| uuid | string | 否 | 否 | spp单据的uuid。 |
| secure | boolean | 否 | 否 | 是否是安全通道。 |
| type | [SppType](#spptypedeprecated) | 否 | 否 | Spp链路类型。 |

#### SppType(deprecated)

枚举，Spp链路类型。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/9kpL1wA3TFSbmDbPBxvN5A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=5D6923D1F43F74F72F8A55F5D6B8F6F5002E116E629324057CFDDC0AFADEDBCD)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.SppType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#spptypedeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| SPP\_RFCOMM | 0 | 表示rfcomm链路类型。 |

#### GattService(deprecated)

描述service的接口参数定义。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/jfMrmie6TVSHRGxxtLPgUQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=C4EC9EA94B482067E3D441E27DBDA0EB939722E7E8AD2EE4A4C6819F0BCBA028)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattService](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#gattservicedeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| serviceUuid | string | 否 | 否 | 特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |
| isPrimary | boolean | 否 | 否 | 如果是主服务设置为true，否则设置为false。 |
| characteristics | Array<[BLECharacteristic](#blecharacteristicdeprecated)\> | 否 | 否 | 当前服务包含的特征列表。 |
| includeServices | Array<[GattService](#gattservicedeprecated)\> | 否 | 是 | 当前服务依赖的其它服务。 |

#### BLECharacteristic(deprecated)

描述characteristic的接口参数定义 。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/X8pXSUrbRCqaMOgUDi00rw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=0FBF1411711721DDFC32CC0FBCB2065926EB3686FB1D84E4889988CA72818086)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.BLECharacteristic](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#blecharacteristicdeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| serviceUuid | string | 否 | 否 | 特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |
| characteristicUuid | string | 否 | 否 | 特定特征（characteristic）的UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| characteristicValue | ArrayBuffer | 否 | 否 | 特征对应的二进制值。 |
| descriptors | Array<[BLEDescriptor](#bledescriptordeprecated)\> | 否 | 否 | 特定特征的描述符列表。 |

#### BLEDescriptor(deprecated)

描述descriptor的接口参数定义 。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/k4TZqt7oRaayULEH5nN2Rw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=F3FAD2593AF78DC758741818FA6EDBFAF7D06C50095F21E62BA2954964F0254C)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.BLEDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#bledescriptordeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| serviceUuid | string | 否 | 否 | 特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |
| characteristicUuid | string | 否 | 否 | 特定特征（characteristic）的UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| descriptorUuid | string | 否 | 否 | 描述符（descriptor）的UUID，例如：00002902-0000-1000-8000-00805f9b34fb。 |
| descriptorValue | ArrayBuffer | 否 | 否 | 描述符对应的二进制值。 |

#### NotifyCharacteristic(deprecated)

描述server端特征值变化时发送的特征通知参数定义。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/0X9qj8v8Q9ar80nGkqoiMw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=0500DFA5CE1E29FE5B2C64B4C3E7E9A0299A00DE4F73DA7505471B30C1C19743)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.NotifyCharacteristic](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#notifycharacteristicdeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| serviceUuid | string | 否 | 否 | 特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |
| characteristicUuid | string | 否 | 否 | 特定特征（characteristic）的UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| characteristicValue | ArrayBuffer | 否 | 否 | 特征对应的二进制值。 |
| confirm | boolean | 否 | 否 | 如果是notification则对端回复确认设置为true，如果是indication则对端不需要回复确认设置为false。 |

#### CharacteristicReadReq(deprecated)

描述server端订阅后收到的特征值读请求事件参数结构。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/TjbeZTM9T12JWvo_p4zoAw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=13622E4F895854A9A0D6E3F7E4D209C7D9BD74ACC232D1EE51C87685C1297EDE)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.CharacteristicReadRequest](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#characteristicreadrequestdeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | 否 | 否 | 表示发送特征值读请求的远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| transId | number | 否 | 否 | 表示读请求的传输ID，server端回复响应时需填写相同的传输ID。 |
| offset | number | 否 | 否 | 表示读特征值数据的起始位置。例如：k表示从第k个字节开始读，server端回复响应时需填写相同的offset。 |
| characteristicUuid | string | 否 | 否 | 特定特征（characteristic）的UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| serviceUuid | string | 否 | 否 | 特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |

#### CharacteristicWriteReq(deprecated)

描述server端订阅后收到的特征值写请求事件参数结构。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/G24WjK6PRW-ECLUhJ9GrGQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=3113A3529FD605E383D2C5EA01914A08F3E9CA3045D8CAB417B75D05F07730A6)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.CharacteristicWriteRequest](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#characteristicwriterequestdeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | 否 | 否 | 表示发送特征值写请求的远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| transId | number | 否 | 否 | 表示写请求的传输ID，server端回复响应时需填写相同的传输ID。 |
| offset | number | 否 | 否 | 表示写特征值数据的起始位置。例如：k表示从第k个字节开始写，server端回复响应时需填写相同的offset。 |
| isPrep | boolean | 否 | 否 | 表示写请求是否立即执行。true表示立即执行。 |
| needRsp | boolean | 否 | 否 | 表示是否要给client端回复响应。true表示需要回复。 |
| value | ArrayBuffer | 否 | 否 | 表示写入的描述符二进制数据。 |
| characteristicUuid | string | 否 | 否 | 特定特征（characteristic）的UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| serviceUuid | string | 否 | 否 | 特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |

#### DescriptorReadReq(deprecated)

描述server端订阅后收到的描述符读请求事件参数结构。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/kTpl_JXYQtCSafSBZLmSdg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=128131080E69EE9D1D492EFFC563483595CBF17EF975DA6B6769373AFA4118A6)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.DescriptorReadRequest](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#descriptorreadrequestdeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | 否 | 否 | 表示发送描述符读请求的远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| transId | number | 否 | 否 | 表示读请求的传输ID，server端回复响应时需填写相同的传输ID。 |
| offset | number | 否 | 否 | 表示读描述符数据的起始位置。例如：k表示从第k个字节开始读，server端回复响应时需填写相同的offset。 |
| descriptorUuid | string | 否 | 否 | 表示描述符（descriptor）的UUID，例如：00002902-0000-1000-8000-00805f9b34fb。 |
| characteristicUuid | string | 否 | 否 | 特定特征（characteristic）的UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| serviceUuid | string | 否 | 否 | 特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |

#### DescriptorWriteReq(deprecated)

描述server端订阅后收到的描述符写请求事件参数结构。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/rBqOntuGS1OSBHJPmGC5OQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=878AB9245B413CC5D0994A8312F1F2D4B1309F4AD45DD5FF1084F926DA5B1733)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.DescriptorWriteRequest](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#descriptorwriterequestdeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | 否 | 否 | 表示发送描述符写请求的远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| transId | number | 否 | 否 | 表示写请求的传输ID，server端回复响应时需填写相同的传输ID。 |
| offset | number | 否 | 否 | 表示写描述符数据的起始位置。例如：k表示从第k个字节开始写，server端回复响应时需填写相同的offset。 |
| isPrep | boolean | 否 | 否 | 表示写请求是否立即执行。 |
| needRsp | boolean | 否 | 否 | 表示是否要给client端回复响应。 |
| value | ArrayBuffer | 否 | 否 | 表示写入的描述符二进制数据。 |
| descriptorUuid | string | 否 | 否 | 表示描述符（descriptor）的UUID，例如：00002902-0000-1000-8000-00805f9b34fb。 |
| characteristicUuid | string | 否 | 否 | 特定特征（characteristic）的UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| serviceUuid | string | 否 | 否 | 特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |

#### ServerResponse(deprecated)

描述server端回复client端读/写请求的响应参数结构。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/FVoKVWSiTbGCx5CwUu73SA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=1B92DFF5058C45028FF74C69CEBF12F619150AD88256ABBECC166FFB8C0E7F8A)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.ServerResponse](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#serverresponsedeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | 否 | 否 | 表示远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| transId | number | 否 | 否 | 表示请求的传输ID，与订阅的读/写请求事件携带的ID保持一致。 |
| status | number | 否 | 否 | 表示响应的状态，设置为0即可，表示正常。 |
| offset | number | 否 | 否 | 表示请求的读/写起始位置，与订阅的读/写请求事件携带的offset保持一致。 |
| value | ArrayBuffer | 否 | 否 | 表示回复响应的二进制数据。 |

#### BLEConnectChangedState(deprecated)

描述Gatt profile连接状态 。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/M8PEmQ39QbyNsyn6LL5keA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=CE40EC10620180B437F3ED106999F97C5563C9262C8D28A12F80DD140C533639)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.BLEConnectChangedState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#bleconnectchangedstatedeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | 否 | 否 | 表示远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| state | [ProfileConnectionState](#profileconnectionstatedeprecated) | 否 | 否 | 表示BLE连接状态的枚举。 |

#### ProfileConnectionState(deprecated)

枚举，蓝牙设备的profile连接状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/iJoX8gtZQkiqpKI29G7VhA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=B44D2925CB57EDA13E69DE5892227A7D889EC5925084C8172C6AFD7D7983A42E)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.ProfileConnectionState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#profileconnectionstatedeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| STATE\_DISCONNECTED | 0 | 表示profile已断连。 |
| STATE\_CONNECTING | 1 | 表示profile正在连接。 |
| STATE\_CONNECTED | 2 | 表示profile已连接。 |
| STATE\_DISCONNECTING | 3 | 表示profile正在断连。 |

#### ScanFilter(deprecated)

扫描过滤参数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/aElQHUcIQMm2LHota4SAPg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=5B195D19EDC1FC428BF2D5DA47F7F7E7D417551C7453CF84963FA82087486671)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.ScanFilter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#scanfilterdeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | 否 | 是 | 表示过滤的BLE设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| name | string | 否 | 是 | 表示过滤的BLE设备名。 |
| serviceUuid | string | 否 | 是 | 表示过滤包含该UUID服务的设备，例如：00001888-0000-1000-8000-00805f9b34fb。 |

#### ScanOptions(deprecated)

扫描的配置参数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/eIOe7TxoQgSndbawHQw88w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=119FBEE5AE62905B9C84E16C90486D17ECF94B5286411E01C6219F4EBB51D477)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.ScanOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#scanoptionsdeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| interval | number | 否 | 是 | 表示扫描结果上报延迟时间，默认值为0。 |
| dutyMode | [ScanDuty](#scandutydeprecated) | 否 | 是 | 表示扫描模式，默认值为SCAN\_MODE\_LOW\_POWER。 |
| matchMode | [MatchMode](#matchmodedeprecated) | 否 | 是 | 表示硬件的过滤匹配模式，默认值为MATCH\_MODE\_AGGRESSIVE。 |

#### ScanDuty(deprecated)

枚举，扫描模式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/gn3b5wQFQo29Ichui4vjcA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=8BC2E68557C2D23647204845EA3732DDD319A17449C785B2B6A76F5295714FEA)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.ScanDuty](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#scandutydeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| SCAN\_MODE\_LOW\_POWER | 0 | 表示低功耗模式，默认值。 |
| SCAN\_MODE\_BALANCED | 1 | 表示均衡模式。 |
| SCAN\_MODE\_LOW\_LATENCY | 2 | 表示低延迟模式。 |

#### MatchMode(deprecated)

枚举，硬件过滤匹配模式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/PgsZ_XaGT6eU26FqCPdLdQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=9D7AA393A6F05B64CDC2D5738F8C68ED5876530DB5A62976D11E14009910AF7F)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.MatchMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#matchmodedeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| MATCH\_MODE\_AGGRESSIVE | 1 | 表示硬件上报扫描结果门限较低，比如扫描到的功率较低或者一段时间扫描到的次数较少也触发上报，默认值。 |
| MATCH\_MODE\_STICKY | 2 | 表示硬件上报扫描结果门限较高，更高的功率门限以及扫描到多次才会上报。 |

#### ScanResult(deprecated)

扫描结果上报数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/jBujnwerQGe3CIa-ijCKWw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=925B35D21D1503FF086F9495DCC1CFF44BF892B436B5CA02C101573BCB384EE6)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.ScanResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#scanresultdeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | 否 | 否 | 表示扫描到的设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| rssi | number | 否 | 否 | 表示扫描到的设备的rssi值。 |
| data | ArrayBuffer | 否 | 否 | 表示扫描到的设备发送的广播包。 |

#### BluetoothState(deprecated)

枚举，蓝牙开关状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/yp0Rd2iYSF6i1m3YIj-VNQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=7700F8537B543852E4D59086E24415A26CCBC25F198C87E7424FDD811D71994E)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.BluetoothState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#bluetoothstatedeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| STATE\_OFF | 0 | 表示蓝牙已关闭。 |
| STATE\_TURNING\_ON | 1 | 表示蓝牙正在打开。 |
| STATE\_ON | 2 | 表示蓝牙已打开。 |
| STATE\_TURNING\_OFF | 3 | 表示蓝牙正在关闭。 |
| STATE\_BLE\_TURNING\_ON | 4 | 表示蓝牙正在打开LE-only模式。 |
| STATE\_BLE\_ON | 5 | 表示蓝牙正处于LE-only模式。 |
| STATE\_BLE\_TURNING\_OFF | 6 | 表示蓝牙正在关闭LE-only模式。 |

#### AdvertiseSetting(deprecated)

描述蓝牙低功耗设备发送广播的参数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/P5d6KsMbQ7WpDvGRAQFz9A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=45176581CED04B806E46DC55465A7B2A18A2A67759EF4A178D93DC7C48CFCAD6)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.AdvertiseSetting](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#advertisesettingdeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| interval | number | 否 | 是 | 表示广播间隔，最小值设置32个slot表示20ms，最大值设置16384个slot，默认值设置为1600个slot表示1s。 |
| txPower | number | 否 | 是 | 表示发送功率，最小值设置-127，最大值设置1，默认值设置-7，单位dbm。 |
| connectable | boolean | 否 | 是 | 表示是否是可连接广播，默认值设置为true。 |

#### AdvertiseData(deprecated)

描述BLE广播数据包的内容。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/s13I4v9-Rt2x-oLRQCLGUg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=F8AE96609AFF353FA35B8B0217A7048B11A2404BCA91D083CE443690E8482127)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.AdvertiseData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#advertisedatadeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| serviceUuids | Array<string> | 否 | 否 | 表示要广播的服务 UUID 列表。 |
| manufactureData | Array<[ManufactureData](#manufacturedatadeprecated)\> | 否 | 否 | 表示要广播的广播的制造商信息列表。 |
| serviceData | Array<[ServiceData](#servicedatadeprecated)\> | 否 | 否 | 表示要广播的服务数据列表。 |

#### ManufactureData(deprecated)

描述BLE广播数据包的内容。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/cjKUaMH4Q_in4if9p1prPg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=2DF03E03B7DE53FA3FFE8412CC70E21C45182D3398AC5B5B8CE16B89B59CCA42)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.ManufactureData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#manufacturedatadeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| manufactureId | number | 否 | 否 | 表示制造商的ID，由蓝牙SIG分配。 |
| manufactureValue | ArrayBuffer | 否 | 否 | 表示制造商发送的制造商数据。 |

#### ServiceData(deprecated)

描述广播包中服务数据内容。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/vvLM-EE8Svi0fe9QfiVb8Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=E306755D304CA157E141D86DC06542609D81E6D9790A091EFF74A532FCC5EB5C)

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.ServiceData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#servicedatadeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| serviceUuid | string | 否 | 否 | 表示服务的UUID。 |
| serviceValue | ArrayBuffer | 否 | 否 | 表示服务数据。 |

#### PinRequiredParam(deprecated)

描述配对请求参数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/eUHusq8yTSOjR3_yPQl3Hg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=DB779C1900DA27A968C2638090CA7AEE4730E88361EC745E81B2CF8A5E80AD45)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.PinRequiredParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#pinrequiredparamdeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | 否 | 否 | 表示要配对的设备ID。 |
| pinCode | string | 否 | 否 | 表示要配对的密钥。 |

#### BondStateParam(deprecated)

描述配对状态参数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/2Zb7H0lfTF6S1ha4ROP0FA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=39BD86E730B3406BAF8989FBA33F23EC80ABFFC27BF8F8795A264450A0FCFDD5)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.BondStateParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#bondstateparamdeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | 否 | 否 | 表示要配对的设备ID。 |
| state | BondState | 否 | 否 | 表示配对设备的状态。 |

#### StateChangeParam(deprecated)

描述profile状态改变参数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/G_IpSapASouQhBC_5d9NEg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=F653E56E258544A4C1DEC0646357F9DBC492A8380772E12D7319EBDED42854FF)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.StateChangeParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#statechangeparamdeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | 否 | 否 | 表示蓝牙设备地址。 |
| state | [ProfileConnectionState](#profileconnectionstatedeprecated) | 否 | 否 | 表示蓝牙设备的profile连接状态。 |

#### DeviceClass(deprecated)

描述蓝牙设备的类别。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/p7if9yeBQFCtKQkmxGQjaw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=0881D5D56DF05238628AD014667A64B985298C8A75ADE6533D543541779EE006)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.DeviceClass](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#deviceclassdeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| majorClass | [MajorClass](#majorclassdeprecated) | 否 | 否 | 表示蓝牙设备主要类别的枚举。 |
| majorMinorClass | [MajorMinorClass](#majorminorclassdeprecated) | 否 | 否 | 表示主要次要蓝牙设备类别的枚举。 |
| classOfDevice | number | 否 | 否 | 表示设备类别。 |

#### MajorClass(deprecated)

枚举，蓝牙设备主要类别。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/DLG-cukVSze_mXxAxJ4VHg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=058A9CF51A2D84E1DD98F237B66EA3D5F04ED377478B602623235FCED01A59E4)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.MajorClass](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#majorclassdeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| MAJOR\_MISC | 0x0000 | 表示杂项设备。 |
| MAJOR\_COMPUTER | 0x0100 | 表示计算机设备。 |
| MAJOR\_PHONE | 0x0200 | 表示手机设备。 |
| MAJOR\_NETWORKING | 0x0300 | 表示网络设备。 |
| MAJOR\_AUDIO\_VIDEO | 0x0400 | 表示音频和视频设备。 |
| MAJOR\_PERIPHERAL | 0x0500 | 表示外围设备。 |
| MAJOR\_IMAGING | 0x0600 | 表示成像设备。 |
| MAJOR\_WEARABLE | 0x0700 | 表示可穿戴设备。 |
| MAJOR\_TOY | 0x0800 | 表示玩具设备。 |
| MAJOR\_HEALTH | 0x0900 | 表示健康设备。 |
| MAJOR\_UNCATEGORIZED | 0x1F00 | 表示未分类设备。 |

#### MajorMinorClass(deprecated)

枚举，主要次要蓝牙设备类别。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/KFpsqTAXQYKmSDrzq7H4-g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=EE4788F4DE9107FD8EC0D38B836E11B502D32E1F867D176BFA12108B52DC2A8E)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.MajorMinorClass](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#majorminorclassdeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| COMPUTER\_UNCATEGORIZED | 0x0100 | 表示未分类计算机设备。 |
| COMPUTER\_DESKTOP | 0x0104 | 表示台式计算机设备。 |
| COMPUTER\_SERVER | 0x0108 | 表示服务器设备。 |
| COMPUTER\_LAPTOP | 0x010C | 表示便携式计算机设备。 |
| COMPUTER\_HANDHELD\_PC\_PDA | 0x0110 | 表示手持式计算机设备。 |
| COMPUTER\_PALM\_SIZE\_PC\_PDA | 0x0114 | 表示掌上电脑设备。 |
| COMPUTER\_WEARABLE | 0x0118 | 表示可穿戴计算机设备。 |
| COMPUTER\_TABLET | 0x011C | 表示平板电脑设备。 |
| PHONE\_UNCATEGORIZED | 0x0200 | 表示未分类手机设备。 |
| PHONE\_CELLULAR | 0x0204 | 表示便携式手机设备。 |
| PHONE\_CORDLESS | 0x0208 | 表示无线电话设备。 |
| PHONE\_SMART | 0x020C | 表示智能手机设备。 |
| PHONE\_MODEM\_OR\_GATEWAY | 0x0210 | 表示调制解调器或网关手机设备。 |
| PHONE\_ISDN | 0x0214 | 表示ISDN手机设备。 |
| NETWORK\_FULLY\_AVAILABLE | 0x0300 | 表示网络完全可用设备。 |
| NETWORK\_1\_TO\_17\_UTILIZED | 0x0320 | 表示使用网络1到17设备。 |
| NETWORK\_17\_TO\_33\_UTILIZED | 0x0340 | 表示使用网络17到33设备。 |
| NETWORK\_33\_TO\_50\_UTILIZED | 0x0360 | 表示使用网络33到50设备。 |
| NETWORK\_60\_TO\_67\_UTILIZED | 0x0380 | 表示使用网络60到67设备。 |
| NETWORK\_67\_TO\_83\_UTILIZED | 0x03A0 | 表示使用网络67到83设备。 |
| NETWORK\_83\_TO\_99\_UTILIZED | 0x03C0 | 表示使用网络83到99设备。 |
| NETWORK\_NO\_SERVICE | 0x03E0 | 表示网络无服务设备。 |
| AUDIO\_VIDEO\_UNCATEGORIZED | 0x0400 | 表示未分类音频视频设备。 |
| AUDIO\_VIDEO\_WEARABLE\_HEADSET | 0x0404 | 表示可穿戴式音频视频设备。 |
| AUDIO\_VIDEO\_HANDSFREE | 0x0408 | 表示免提音频视频设备。 |
| AUDIO\_VIDEO\_MICROPHONE | 0x0410 | 表示麦克风音频视频设备。 |
| AUDIO\_VIDEO\_LOUDSPEAKER | 0x0414 | 表示扬声器音频视频设备。 |
| AUDIO\_VIDEO\_HEADPHONES | 0x0418 | 表示头戴式音频视频设备。 |
| AUDIO\_VIDEO\_PORTABLE\_AUDIO | 0x041C | 表示便携式音频视频设备。 |
| AUDIO\_VIDEO\_CAR\_AUDIO | 0x0420 | 表示汽车音频视频设备。 |
| AUDIO\_VIDEO\_SET\_TOP\_BOX | 0x0424 | 表示机顶盒音频视频设备。 |
| AUDIO\_VIDEO\_HIFI\_AUDIO | 0x0428 | 表示高保真音响设备。 |
| AUDIO\_VIDEO\_VCR | 0x042C | 表示录像机音频视频设备。 |
| AUDIO\_VIDEO\_VIDEO\_CAMERA | 0x0430 | 表示照相机音频视频设备。 |
| AUDIO\_VIDEO\_CAMCORDER | 0x0434 | 表示摄像机音频视频设备。 |
| AUDIO\_VIDEO\_VIDEO\_MONITOR | 0x0438 | 表示监视器音频视频设备。 |
| AUDIO\_VIDEO\_VIDEO\_DISPLAY\_AND\_LOUDSPEAKER | 0x043C | 表示视频显示器和扬声器设备。 |
| AUDIO\_VIDEO\_VIDEO\_CONFERENCING | 0x0440 | 表示音频视频会议设备。 |
| AUDIO\_VIDEO\_VIDEO\_GAMING\_TOY | 0x0448 | 表示游戏玩具音频视频设备。 |
| PERIPHERAL\_NON\_KEYBOARD\_NON\_POINTING | 0x0500 | 表示非键盘非指向外围设备。 |
| PERIPHERAL\_KEYBOARD | 0x0540 | 表示外设键盘设备。 |
| PERIPHERAL\_POINTING\_DEVICE | 0x0580 | 表示定点装置外围设备。 |
| PERIPHERAL\_KEYBOARD\_POINTING | 0x05C0 | 表示键盘指向外围设备。 |
| PERIPHERAL\_UNCATEGORIZED | 0x0500 | 表示未分类外围设备。 |
| PERIPHERAL\_JOYSTICK | 0x0504 | 表示周边操纵杆设备。 |
| PERIPHERAL\_GAMEPAD | 0x0508 | 表示周边游戏板设备。 |
| PERIPHERAL\_REMOTE\_CONTROL | 0x05C0 | 表示远程控制外围设备。 |
| PERIPHERAL\_SENSING\_DEVICE | 0x0510 | 表示外围传感设备设备。 |
| PERIPHERAL\_DIGITIZER\_TABLET | 0x0514 | 表示外围数字化仪平板电脑设备。 |
| PERIPHERAL\_CARD\_READER | 0x0518 | 表示外围读卡器设备。 |
| PERIPHERAL\_DIGITAL\_PEN | 0x051C | 表示外设数码笔设备。 |
| PERIPHERAL\_SCANNER\_RFID | 0x0520 | 表示射频识别扫描仪外围设备。 |
| PERIPHERAL\_GESTURAL\_INPUT | 0x0522 | 表示手势输入外围设备。 |
| IMAGING\_UNCATEGORIZED | 0x0600 | 表示未分类的图像设备。 |
| IMAGING\_DISPLAY | 0x0610 | 表示图像显示设备。 |
| IMAGING\_CAMERA | 0x0620 | 表示成像照相机设备。 |
| IMAGING\_SCANNER | 0x0640 | 表示成像扫描仪设备。 |
| IMAGING\_PRINTER | 0x0680 | 表示成像打印机设备。 |
| WEARABLE\_UNCATEGORIZED | 0x0700 | 表示未分类的可穿戴设备。 |
| WEARABLE\_WRIST\_WATCH | 0x0704 | 表示可穿戴腕表设备。 |
| WEARABLE\_PAGER | 0x0708 | 表示可穿戴寻呼机设备。 |
| WEARABLE\_JACKET | 0x070C | 表示夹克可穿戴设备。 |
| WEARABLE\_HELMET | 0x0710 | 表示可穿戴头盔设备。 |
| WEARABLE\_GLASSES | 0x0714 | 表示可穿戴眼镜设备。 |
| TOY\_UNCATEGORIZED | 0x0800 | 表示未分类的玩具设备。 |
| TOY\_ROBOT | 0x0804 | 表示玩具机器人设备。 |
| TOY\_VEHICLE | 0x0808 | 表示玩具车设备。 |
| TOY\_DOLL\_ACTION\_FIGURE | 0x080C | 表示人形娃娃玩具设备。 |
| TOY\_CONTROLLER | 0x0810 | 表示玩具控制器设备。 |
| TOY\_GAME | 0x0814 | 表示玩具游戏设备。 |
| HEALTH\_UNCATEGORIZED | 0x0900 | 表示未分类健康设备。 |
| HEALTH\_BLOOD\_PRESSURE | 0x0904 | 表示血压健康设备。 |
| HEALTH\_THERMOMETER | 0x0908 | 表示温度计健康设备。 |
| HEALTH\_WEIGHING | 0x090C | 表示体重健康设备。 |
| HEALTH\_GLUCOSE | 0x0910 | 表示葡萄糖健康设备。 |
| HEALTH\_PULSE\_OXIMETER | 0x0914 | 表示脉搏血氧仪健康设备。 |
| HEALTH\_PULSE\_RATE | 0x0918 | 表示脉搏率健康设备。 |
| HEALTH\_DATA\_DISPLAY | 0x091C | 表示数据显示健康设备。 |
| HEALTH\_STEP\_COUNTER | 0x0920 | 表示阶梯计数器健康设备。 |
| HEALTH\_BODY\_COMPOSITION\_ANALYZER | 0x0924 | 表示身体成分分析仪健康设备。 |
| HEALTH\_PEAK\_FLOW\_MOITOR | 0x0928 | 表示湿度计健康设备。 |
| HEALTH\_MEDICATION\_MONITOR | 0x092C | 表示药物监视仪健康设备。 |
| HEALTH\_KNEE\_PROSTHESIS | 0x0930 | 表示膝盖假肢健康设备。 |
| HEALTH\_ANKLE\_PROSTHESIS | 0x0934 | 表示脚踝假肢健康设备。 |
| HEALTH\_GENERIC\_HEALTH\_MANAGER | 0x0938 | 表示通用健康管理设备。 |
| HEALTH\_PERSONAL\_MOBILITY\_DEVICE | 0x093C | 表示个人移动健康设备。 |

#### PlayingState(deprecated)

枚举，蓝牙A2DP 播放状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/_2GFVdM0S2eAv8V_R2bo9g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=6488714C207CDEF1C19E403B9A760A8D8E58DFEE5ED410FB99CF6BAC8073007D)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.PlayingState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#playingstatedeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| STATE\_NOT\_PLAYING | 0x0000 | 表示未播放。 |
| STATE\_PLAYING | 0x0001 | 表示正在播放。 |

#### ProfileId(deprecated)

蓝牙profile枚举，API9新增PROFILE\_HID\_HOST，PROFILE\_PAN\_NETWORK。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/YFgVAVvbQcyRV2SUDjbiRQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=5637749CBF8A979ECE12EBAB39D3890115DA30E95B057771B5D90C55DAC3D9E6)

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.ProfileId](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager#profileiddeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| PROFILE\_A2DP\_SOURCE | 1 | 表示A2DP profile。 |
| PROFILE\_HANDS\_FREE\_AUDIO\_GATEWAY | 4 | 表示HFP profile。 |

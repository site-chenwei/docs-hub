---
title: "@ohos.bluetoothManager (蓝牙)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Connectivity Kit（短距通信服务）"
  - "已停止维护的接口"
  - "@ohos.bluetoothManager (蓝牙)"
captured_at: "2026-04-17T01:48:22.235Z"
---

# @ohos.bluetoothManager (蓝牙)

蓝牙模块提供了基础的传统蓝牙能力以及BLE的扫描、广播等功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/w-vXN_uPRfKUMdqwCaKicQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=2165820971CB7B8C1A0F462FD94E2F68792210FF043581F91A37B734A373B582)

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API Version 10 开始，该接口不再维护，推荐使用[@ohos.bluetooth.ble](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble)等相关profile接口。

#### 导入模块

```js
import { bluetoothManager } from '@kit.ConnectivityKit';
```

#### bluetoothManager.enableBluetooth(deprecated)

enableBluetooth(): void

开启蓝牙。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/rvvzhCmtT-uKPk5nJaib7A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=2A90FFC7666EFD2F507B165524E4C7D912349A322D133F58099B38429CCD2311)

从API version 9开始支持，从API version 10开始废弃。建议使用[access.enableBluetooth](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-access#accessenablebluetooth)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
try {
    bluetoothManager.enableBluetooth();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.disableBluetooth(deprecated)

disableBluetooth(): void

关闭蓝牙。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/2kgIj9msS0K-V0bj4zdYAw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=70D3CCCE01B629E6846DE97A935D7BC8AA895FA53CB1EE9338834B47F3E21F8A)

从API version 9开始支持，从API version 10开始废弃。建议使用[access.disableBluetooth](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-access#accessdisablebluetooth)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
try {
    bluetoothManager.disableBluetooth();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ", errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.getLocalName(deprecated)

getLocalName(): string

获取蓝牙本地设备名称。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/sBJhvwm7T52qTyLg69P1NA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=EC9AA927F40C59304052B505CBC0322AF5A7F9B6D7601735F283DB1AA31AC9EC)

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.getLocalName](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-connection#connectiongetlocalname)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 蓝牙本地设备名称。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
try {
    let localName: string = bluetoothManager.getLocalName();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.getState(deprecated)

getState(): BluetoothState

获取蓝牙开关状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/r6kiHhTjQ0KN4kdd8BnO3A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=817437B19EF2A3C25CBD958449B49FC2EA56EA2282F0589D928917725D183ECB)

从API version 9开始支持，从API version 10开始废弃。建议使用[access.getState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-access#accessgetstate)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [BluetoothState](#bluetoothstatedeprecated) | 表示蓝牙开关状态。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
try {
    let state: bluetoothManager.BluetoothState = bluetoothManager.getState();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.getBtConnectionState(deprecated)

getBtConnectionState(): ProfileConnectionState

获取蓝牙本端的Profile连接状态，例如：任意一个支持的Profile连接状态为已连接，则此接口返回状态为已连接。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/f4AP-3IsRKyvJzVreC5LWA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=4EE7B1BE61ACFE7FE5116F707652129877CED61ABA7FF12BB392208F6FFC2E21)

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.getProfileConnectionState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-connection#connectiongetprofileconnectionstate)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [ProfileConnectionState](#profileconnectionstatedeprecated) | 表示蓝牙设备的Profile连接状态。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
try {
    let connectionState: bluetoothManager.ProfileConnectionState = bluetoothManager.getBtConnectionState();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.setLocalName(deprecated)

setLocalName(name: string): void

设置蓝牙本地设备名称。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/TqTjeMlCR1eKZKGtGZEJUA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=7EA9810FF0FD84A133E85AF9C499FAF6CD3B9F3CBC3B746990DC49F9DC7679E0)

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.setLocalName](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-connection#connectionsetlocalnamedeprecated)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 要设置的蓝牙名称，最大长度为248字节数。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
try {
    bluetoothManager.setLocalName('device_name');
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.pairDevice(deprecated)

pairDevice(deviceId: string): void

发起蓝牙配对。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/c-EXgkFBSs-kpMZD04vSoA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=6CB716DE78BA788066D49298731DE998380B8750694A21A1DB254218C800397E)

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.pairDevice](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-connection#connectionpairdevice)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| deviceId | string | 是 | 表示配对的远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
try {
    // 实际的地址可由扫描流程获取
    bluetoothManager.pairDevice("XX:XX:XX:XX:XX:XX");
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.getProfileConnectionState(deprecated)

getProfileConnectionState(profileId: ProfileId): ProfileConnectionState

依据ProfileId获取指定profile的连接状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/ranSA1e6Q6-FtVyBre7Hfw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=ECEA2C0D21C79BCA8298A73420A2E3FFC6B4588B3417E71FE0FCA7F7901C8B59)

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.getProfileConnectionState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-connection#connectiongetprofileconnectionstate)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| profileId | ProfileId | 是 | 表示profile的枚举值，例如：PROFILE\_A2DP\_SOURCE。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [ProfileConnectionState](#profileconnectionstatedeprecated) | profile的连接状态。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
try {
    let result: bluetoothManager.ProfileConnectionState = bluetoothManager.getProfileConnectionState(bluetoothManager.ProfileId.PROFILE_A2DP_SOURCE);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.getRemoteDeviceName(deprecated)

getRemoteDeviceName(deviceId: string): string

获取对端蓝牙设备的名称。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/9kkGqTpjQOGffXnN1Y9RGw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=54313EB7A6D6824DD5F9C912E7D520A54CC23A890950BE75D7A6FEBEEEA81A8D)

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.getRemoteDeviceName](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-connection#connectiongetremotedevicename)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| deviceId | string | 是 | 表示远程设备的地址，例如："XX:XX:XX:XX:XX:XX"。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 以字符串格式返回设备名称。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
try {
    let remoteDeviceName: string = bluetoothManager.getRemoteDeviceName("XX:XX:XX:XX:XX:XX");
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.getRemoteDeviceClass(deprecated)

getRemoteDeviceClass(deviceId: string): DeviceClass

获取对端蓝牙设备的类别。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/N1u0hHgFTMivcvho9DufPw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=5A2E96D95DA0A8813D2E701CAC9728D7D16B25BB07B9FC5F29EA35363C06AB34)

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.getRemoteDeviceClass](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-connection#connectiongetremotedeviceclass)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| deviceId | string | 是 | 表示远程设备的地址，例如："XX:XX:XX:XX:XX:XX"。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [DeviceClass](#deviceclassdeprecated) | 远程设备的类别。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
try {
    let remoteDeviceClass: bluetoothManager.DeviceClass  = bluetoothManager.getRemoteDeviceClass("XX:XX:XX:XX:XX:XX");
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.getPairedDevices(deprecated)

getPairedDevices(): Array<string>

获取蓝牙配对列表。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/iq6tDa0pRzeymEKbcgAIkg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=0D68F896AB3092356795DC5D0AC26CE75794EAC22023DE820FF1460FCD9C1AE1)

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.getPairedDevices](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-connection#connectiongetpaireddevices)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Array<string> | 已配对蓝牙设备的地址列表。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
try {
    let devices: Array<string> = bluetoothManager.getPairedDevices();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.setBluetoothScanMode(deprecated)

setBluetoothScanMode(mode: ScanMode, duration: number): void

设置蓝牙扫描模式，可以被远端设备发现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/6GXig4BpQt6fdKdL1ZnueQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=A75B38CA725157CDDED55B02D8659DB510A67F5B9FA0081CEB1356F496D7177D)

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.setBluetoothScanMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-connection#connectionsetbluetoothscanmode)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| mode | [ScanMode](#scanmodedeprecated) | 是 | 蓝牙扫描模式。 |
| duration | number | 是 | 设备可被发现的持续时间，单位为毫秒；设置为0则持续可发现。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
try {
    // 设置为可连接可发现才可被远端设备扫描到，可以连接。
    bluetoothManager.setBluetoothScanMode(bluetoothManager.ScanMode.SCAN_MODE_CONNECTABLE_GENERAL_DISCOVERABLE, 100);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.getBluetoothScanMode(deprecated)

getBluetoothScanMode(): ScanMode

获取蓝牙扫描模式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/E7EDyNiERgiVMlpqjzCk2Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=CA61634F504AD8FEC7E9E568FF834861B428713A82D88A6B7E94A8C6BA2E34D4)

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.getBluetoothScanMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-connection#connectiongetbluetoothscanmode)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [ScanMode](#scanmodedeprecated) | 蓝牙扫描模式。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
try {
    let scanMode: bluetoothManager.ScanMode = bluetoothManager.getBluetoothScanMode();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.startBluetoothDiscovery(deprecated)

startBluetoothDiscovery(): void

开启蓝牙扫描，可以发现远端设备。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/Ppq59PHGTbCp2pGHXn3-BA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=A2D247B23722F613247DC7B55B7201F6C542C7C373A0905122D5BC4110DE6DE8)

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.startBluetoothDiscovery](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-connection#connectionstartbluetoothdiscovery)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
let deviceId: Array<string>;
function onReceiveEvent(data: Array<string>) {
    deviceId = data;
}
try {
    bluetoothManager.on('bluetoothDeviceFind', onReceiveEvent);
    bluetoothManager.startBluetoothDiscovery();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.stopBluetoothDiscovery(deprecated)

stopBluetoothDiscovery(): void

关闭蓝牙扫描。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/6nnDSd-URDKLk4P7Ba8qNw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=C441EEAAAB39C0D3F50712464C7D95C13977EC6ED73C87180E7AA6573C457D79)

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.stopBluetoothDiscovery](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-connection#connectionstopbluetoothdiscovery)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
try {
    bluetoothManager.stopBluetoothDiscovery();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.setDevicePairingConfirmation(deprecated)

setDevicePairingConfirmation(device: string, accept: boolean): void

设置设备配对请求确认。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/kW0grM1WSTy2MTZm2w340Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=017F8522FB7E7ABD440B0452F25FDEC446814B6A175C56598B0B805FE7C9CA44)

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.setDevicePairingConfirmation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-connection#connectionsetdevicepairingconfirmation)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH 和 ohos.permission.MANAGE\_BLUETOOTH（该权限仅系统应用可申请）

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| device | string | 是 | 表示远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| accept | boolean | 是 | 接受配对请求设置为true，否则设置为false。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
// 订阅“pinRequired”配对请求事件，收到远端配对请求后设置配对确认
function onReceivePinRequiredEvent(data: bluetoothManager.PinRequiredParam) { // data为配对请求的入参，配对请求参数
    console.info('pin required  = '+ JSON.stringify(data));
    bluetoothManager.setDevicePairingConfirmation(data.deviceId, true);
}
try {
    bluetoothManager.on("pinRequired", onReceivePinRequiredEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.on('bluetoothDeviceFind')(deprecated)

on(type: 'bluetoothDeviceFind', callback: Callback<Array<string>>): void

订阅蓝牙设备发现上报事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/Tb7Huoy9ThetVBZRxNHfkQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=AD7D1ABE0FA1DF6ACA12D4436A4E782058C244673C7EC4E4C03FDD5AB1403C67)

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.on('bluetoothDeviceFind')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-connection#connectiononbluetoothdevicefind)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"bluetoothDeviceFind"字符串，表示蓝牙设备发现事件。 |
| callback | Callback<Array<string>> | 是 | 表示回调函数的入参，发现的设备集合。回调函数由用户创建通过该接口注册。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: Array<string>) { // data为蓝牙设备地址集合
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
try {
    bluetoothManager.on('bluetoothDeviceFind', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.off('bluetoothDeviceFind')(deprecated)

off(type: 'bluetoothDeviceFind', callback?: Callback<Array<string>>): void

取消订阅蓝牙设备发现上报事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/q451P0LrQXag9qh5AamvAQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=A8CDDDA1F455C9A103E41EAC867E1905C70DD903EDA21A1A410CFDA26B6569DC)

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.off('bluetoothDeviceFind')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-connection#connectionoffbluetoothdevicefind)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"bluetoothDeviceFind"字符串，表示蓝牙设备发现事件。 |
| callback | Callback<Array<string>> | 否 | 表示取消订阅蓝牙设备发现事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: Array<string>) {
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
try {
    bluetoothManager.on('bluetoothDeviceFind', onReceiveEvent);
    bluetoothManager.off('bluetoothDeviceFind', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.on('pinRequired')(deprecated)

on(type: 'pinRequired', callback: Callback<PinRequiredParam>): void

订阅远端蓝牙设备的配对请求事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/oWalK6uiSOeekv3diVwFig/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=EEA9EC6F95FD77F926D44CF78332129DC7B7A86BA1B83C932391C62C185C444D)

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.on('pinRequired')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-connection#connectiononpinrequired)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"pinRequired"字符串，表示配对请求事件。 |
| callback | Callback<[PinRequiredParam](#pinrequiredparamdeprecated)\> | 是 | 表示回调函数的入参，配对请求。回调函数由用户创建通过该接口注册。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.PinRequiredParam) { // data为配对请求参数
    console.info('pin required = '+ JSON.stringify(data));
}
try {
    bluetoothManager.on('pinRequired', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.off('pinRequired')(deprecated)

off(type: 'pinRequired', callback?: Callback<PinRequiredParam>): void

取消订阅远端蓝牙设备的配对请求事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/v0oCEMQSS2qme_Tp7okbPg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=00E0B9C979AA73656C625972554B3F2D4B13E7428E6E25E755C222E9E6E841FD)

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.off('pinRequired')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-connection#connectionoffpinrequired)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"pinRequired"字符串，表示配对请求事件。 |
| callback | Callback<[PinRequiredParam](#pinrequiredparamdeprecated)\> | 否 | 表示取消订阅蓝牙配对请求事件上报，入参为配对请求参数。不填该参数则取消订阅该type对应的所有回调。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.PinRequiredParam) {
    console.info('pin required = '+ JSON.stringify(data));
}
try {
    bluetoothManager.on('pinRequired', onReceiveEvent);
    bluetoothManager.off('pinRequired', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.on('bondStateChange')(deprecated)

on(type: 'bondStateChange', callback: Callback<BondStateParam>): void

订阅蓝牙配对状态改变事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/6oKNJPUiQdq1HLFHlfpefA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=FF854A81D5AAD3C8E1D50336E1F873349BE7844A1916D214F19351DBE99CBEF4)

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.on('bondStateChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-connection#connectiononbondstatechange)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"bondStateChange"字符串，表示蓝牙配对状态改变事件。 |
| callback | Callback<[BondStateParam](#bondstateparamdeprecated)\> | 是 | 表示回调函数的入参，配对的状态。回调函数由用户创建通过该接口注册。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.BondStateParam) { // data为回调函数入参，表示配对的状态
    console.info('pair state = '+ JSON.stringify(data));
}
try {
    bluetoothManager.on('bondStateChange', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.off('bondStateChange')(deprecated)

off(type: 'bondStateChange', callback?: Callback<BondStateParam>): void

取消订阅蓝牙配对状态改变事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/s8gu58nGRLaIO-4qG8fkyg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=2D185019B291B1CB13771BAFC153939B3E3A2DD82B6B294B02A7FA226532AF75)

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.off('bondStateChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-connection#connectionoffbondstatechange)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"bondStateChange"字符串，表示蓝牙配对状态改变事件。 |
| callback | Callback<[BondStateParam](#bondstateparamdeprecated)\> | 否 | 表示取消订阅蓝牙配对状态改变事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.BondStateParam) {
    console.info('bond state = '+ JSON.stringify(data));
}
try {
    bluetoothManager.on('bondStateChange', onReceiveEvent);
    bluetoothManager.off('bondStateChange', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.on('stateChange')(deprecated)

on(type: 'stateChange', callback: Callback<BluetoothState>): void

订阅蓝牙设备开关状态事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/EuNmb9RXQTyCLYFrmgdtYA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=6294A56583858C8E86AE8EEED9050B958744D1F19135E52B95987CBC45D6E9EA)

从API version 9开始支持，从API version 10开始废弃。建议使用[access.on('stateChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-access#accessonstatechange)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"stateChange"字符串，表示蓝牙状态改变事件。 |
| callback | Callback<[BluetoothState](#bluetoothstatedeprecated)\> | 是 | 表示回调函数的入参，蓝牙状态。回调函数由用户创建通过该接口注册。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.BluetoothState) {
    console.info('bluetooth state = '+ JSON.stringify(data));
}
try {
    bluetoothManager.on('stateChange', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.off('stateChange')(deprecated)

off(type: 'stateChange', callback?: Callback<BluetoothState>): void

取消订阅蓝牙设备开关状态事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/bj9-dKDFQ7efg1KODJqBLw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=3BE3FCEF1DF3C9F339B8D248F3A2F3A69542662B3C184C71EE48E3A80F01B31F)

从API version 9开始支持，从API version 10开始废弃。建议使用[access.off('stateChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-access#accessoffstatechange)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"stateChange"字符串，表示蓝牙状态改变事件。 |
| callback | Callback<[BluetoothState](#bluetoothstatedeprecated)\> | 否 | 表示取消订阅蓝牙状态改变事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.BluetoothState) {
    console.info('bluetooth state = '+ JSON.stringify(data));
}
try {
    bluetoothManager.on('stateChange', onReceiveEvent);
    bluetoothManager.off('stateChange', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.sppListen(deprecated)

sppListen(name: string, option: SppOption, callback: AsyncCallback<number>): void

创建一个服务端监听Socket。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/PAJguUlqRomos48AwneZxw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=8AB5DC3DB1E4E49C0CEB4F08D247F9BC943C0E882EEFCDE87A8C55965067D958)

从API version 9开始支持，从API version 10开始废弃。建议使用[socket.sppListen](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-socket#socketspplisten)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 服务的名称。 |
| option | [SppOption](#sppoptiondeprecated) | 是 | spp监听配置参数。 |
| callback | AsyncCallback<number> | 是 | 表示回调函数的入参，服务端Socket的id。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@kit.BasicServicesKit';
let serverNumber = -1;
function serverSocket(code: BusinessError, number: number) {
  console.info(`bluetooth error code: ${code.code}`);
  if (code.code == 0) {
    console.info(`bluetooth serverSocket Number: ${number}`);
    serverNumber = number;
  }
}

let sppOption: bluetoothManager.SppOption = {uuid: '00001810-0000-1000-8000-00805F9B34FB', secure: false, type: 0};
try {
    bluetoothManager.sppListen('server1', sppOption, serverSocket);
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```

#### bluetoothManager.sppAccept(deprecated)

sppAccept(serverSocket: number, callback: AsyncCallback<number>): void

服务端监听socket等待客户端连接。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/t-nqgfDJR06t6rCCsSYN-g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=A1C3F33094A1CA58D9E9349D23C6CEB899CE7B51D53E69AA075DA9C481153B63)

从API version 9开始支持，从API version 10开始废弃。建议使用[socket.sppAccept](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-socket#socketsppaccept)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| serverSocket | number | 是 | 服务端socket的id。 |
| callback | AsyncCallback<number> | 是 | 表示回调函数的入参，客户端socket的id。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@kit.BasicServicesKit';
let serverNumber = -1;
function serverSocket(code: BusinessError, number: number) {
  console.info(`bluetooth error code: ${code.code}`);
  if (code.code == 0) {
    console.info(`bluetooth serverSocket Number: ${number}`);
    serverNumber = number;
  }
}
let clientNumber = -1;
function acceptClientSocket(code: BusinessError, number: number) {
  console.info(`bluetooth error code: ${code.code}`);
  if (code.code == 0) {
    console.info(`bluetooth clientSocket Number: ${number}`);
    // 获取的clientNumber用作服务端后续读/写操作socket的id。
    clientNumber = number;
  }
}
try {
    bluetoothManager.sppAccept(serverNumber, acceptClientSocket);
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```

#### bluetoothManager.sppConnect(deprecated)

sppConnect(device: string, option: SppOption, callback: AsyncCallback<number>): void

客户端向远端设备发起spp连接。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/WIJFqn4MQdqaHmUmGaeyvg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=3454DBF38F0A09DDA02FEF1251DFCA99966DC6E029A40BB8D241D26F8A03B569)

从API version 9开始支持，从API version 10开始废弃。建议使用[socket.sppConnect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-socket#socketsppconnect)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| device | string | 是 | 对端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| option | [SppOption](#sppoptiondeprecated) | 是 | spp客户端连接配置参数。 |
| callback | AsyncCallback<number> | 是 | 表示回调函数的入参，客户端socket的id。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@kit.BasicServicesKit';

let clientNumber = -1;
function clientSocket(code: BusinessError, number: number) {
  if (code == null || code.code != 0) {
    return;
  }
  console.info(`bluetooth serverSocket Number: ${number}`);
  // 获取的clientNumber用作客户端后续读/写操作socket的id。
  clientNumber = number;
}
let sppOption: bluetoothManager.SppOption = {uuid: '00001810-0000-1000-8000-00805F9B34FB', secure: false, type: 0};
try {
    bluetoothManager.sppConnect('XX:XX:XX:XX:XX:XX', sppOption, clientSocket);
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```

#### bluetoothManager.sppCloseServerSocket(deprecated)

sppCloseServerSocket(socket: number): void

关闭服务端监听Socket，入参socket由sppListen接口返回。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/0QOTxvkbQqCjRjjnAtEv1w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=B3C826921F70B43843230F833E458CB487D8E55244EC2A6A48D69D617F528CFF)

从API version 9开始支持，从API version 10开始废弃。建议使用[socket.sppCloseServerSocket](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-socket#socketsppcloseserversocket)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| socket | number | 是 | 服务端监听socket的id。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@kit.BasicServicesKit';
let serverNumber = -1;
function serverSocket(code: BusinessError, number: number) {
  console.info(`bluetooth error code: ${code.code}`);
  if (code.code == 0) {
    console.info(`bluetooth serverSocket Number: ${number}`);
    serverNumber = number;
  }
}
try {
    bluetoothManager.sppCloseServerSocket(serverNumber);
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```

#### bluetoothManager.sppCloseClientSocket(deprecated)

sppCloseClientSocket(socket: number): void

关闭客户端socket，入参socket由sppAccept或sppConnect接口获取。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/uwQSh4QbQ4CajevHWkhriA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=83D36E10B340B648AA9F66C1C0E8EE9631DEE8977D69980103EA96713DB5E453)

从API version 9开始支持，从API version 10开始废弃。建议使用[socket.sppCloseClientSocket](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-socket#socketsppcloseclientsocket)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| socket | number | 是 | 客户端socket的id。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@kit.BasicServicesKit';
let clientNumber = -1;
function clientSocket(code: BusinessError, number: number) {
  if (code == null || code.code != 0) {
    return;
  }
  console.info(`bluetooth serverSocket Number: ${number}`);
  // 获取的clientNumber用作客户端后续读/写操作socket的id。
  clientNumber = number;
}
try {
    bluetoothManager.sppCloseClientSocket(clientNumber);
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```

#### bluetoothManager.sppWrite(deprecated)

sppWrite(clientSocket: number, data: ArrayBuffer): void

通过socket向远端发送数据，入参clientSocket由sppAccept或sppConnect接口获取。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/ML3VOah0TpC2uJm9phuAUg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=F41E570C597B6F04351E807F14D960EFCBE72AD72F16DBC838C8AF5D9D96F657)

从API version 9开始支持，从API version 10开始废弃。建议使用[socket.sppWrite](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-socket#socketsppwrite)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| clientSocket | number | 是 | 客户端socket的id。 |
| data | ArrayBuffer | 是 | 写入的数据。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2901054 | IO error. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@kit.BasicServicesKit';
let clientNumber = -1;
function clientSocket(code: BusinessError, number: number) {
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
try {
    bluetoothManager.sppWrite(clientNumber, arrayBuffer);
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```

#### bluetoothManager.on('sppRead')(deprecated)

on(type: 'sppRead', clientSocket: number, callback: Callback<ArrayBuffer>): void

订阅spp读请求事件，入参clientSocket由sppAccept或sppConnect接口获取。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/9W6w2T4MQiqRGIE3X3NtrQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=78CA44A96E5045E0B083890A423AAB759F6A4437FBD2B24889DAFE1B72A03802)

从API version 9开始支持，从API version 10开始废弃。建议使用[socket.on('sppRead')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-socket#socketonsppread)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"sppRead"字符串，表示spp读请求事件。 |
| clientSocket | number | 是 | 客户端socket的id。 |
| callback | Callback<ArrayBuffer> | 是 | 表示回调函数的入参，读取到的数据。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2901054 | IO error. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@kit.BasicServicesKit';
let clientNumber = -1;
function clientSocket(code: BusinessError, number: number) {
  if (code == null || code.code != 0) {
    return;
  }
  console.info(`bluetooth serverSocket Number: ${number}`);
  // 获取的clientNumber用作客户端后续读/写操作socket的id。
  clientNumber = number;
}
function dataRead(dataBuffer: ArrayBuffer) {
  let data = new Uint8Array(dataBuffer);
  console.info(`bluetooth data is: ${data[0]}`);
}
try {
    bluetoothManager.on('sppRead', clientNumber, dataRead);
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```

#### bluetoothManager.off('sppRead')(deprecated)

off(type: 'sppRead', clientSocket: number, callback?: Callback<ArrayBuffer>): void

取消订阅spp读请求事件，入参clientSocket由sppAccept或sppConnect接口获取。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/H90DghkQSQW4m4IeVKJJPQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=BCD8FD3769E3AFF144A1AA245C8B451291C95A27A39F7D52E02B159F23D99D58)

从API version 9开始支持，从API version 10开始废弃。建议使用[socket.off('sppRead')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-socket#socketoffsppread)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"sppRead"字符串，表示spp读请求事件。 |
| clientSocket | number | 是 | 客户端Socket的id。 |
| callback | Callback<ArrayBuffer> | 否 | 表示取消订阅spp读请求事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**示例：**

```js
import { BusinessError } from '@kit.BasicServicesKit';
let clientNumber = -1;
function clientSocket(code: BusinessError, number: number) {
  if (code == null || code.code != 0) {
    return;
  }
  console.info(`bluetooth serverSocket Number: ${number}`);
  // 获取的clientNumber用作客户端后续读/写操作socket的id。
  clientNumber = number;
}
try {
    bluetoothManager.off('sppRead', clientNumber);
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```

#### bluetoothManager.getProfileInstance(deprecated)

getProfileInstance(profileId: ProfileId): A2dpSourceProfile | HandsFreeAudioGatewayProfile | HidHostProfile | PanProfile

通过ProfileId，获取profile的对象实例，API9新增了HidHostProfile，PanProfile。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/k_Q-ufw-RlKdnkXZ5Ze_qg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=F80546499E0660AF988D0F1D6405E6FEA7315762504D1D348F1B73F86C882FCA)

从API version 9开始支持，从API version 10开始废弃。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| profileId | [ProfileId](#profileiddeprecated) | 是 | 表示profile的枚举值，例如：PROFILE\_A2DP\_SOURCE。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [A2dpSourceProfile](#a2dpsourceprofile) | [HandsFreeAudioGatewayProfile](#handsfreeaudiogatewayprofiledeprecated) | [HidHostProfile](#hidhostprofiledeprecated) | [PanProfile](#panprofile) | 对应的profile的对象实例，当前支持A2dpSourceProfile/HandsFreeAudioGatewayProfile/HidHostProfile/PanProfile。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
try {
    let hidHost: bluetoothManager.HidHostProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_HID_HOST);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### BLE

BLE模块提供了对蓝牙操作和管理的方法。

#### \[h2\]createGattServer(deprecated)

createGattServer(): GattServer

创建一个可使用的GattServer实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/xkRZZL4HQiu6H7cEBoiIcg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=A8B8C5E2F0F0EFC38E642258CF2031464CA1C2ADD7BD730B0E85A5F0EC3A1F2E)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.createGattServer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#blecreategattserver)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [GattServer](#gattserver) | server端类，使用server端方法之前需要创建该类的实例进行操作。 |

**示例：**

```js
let gattServer: bluetoothManager.GattServer  = bluetoothManager.BLE.createGattServer();
```

#### \[h2\]createGattClientDevice(deprecated)

createGattClientDevice(deviceId: string): GattClientDevice

创建一个可使用的GattClientDevice实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/_pkbh9cmT7qvE-oZnIKYlQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=58B2E0B192F0350A3E8E80E062FDB0EFD726289553606ADCB04BF7D60BB02092)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.createGattClientDevice](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#blecreategattclientdevice)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| deviceId | string | 是 | 对端设备地址， 例如："XX:XX:XX:XX:XX:XX"。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [GattClientDevice](#gattclientdevice) | client端类，使用client端方法之前需要创建该类的实例进行操作。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
try {
    let device: bluetoothManager.GattClientDevice = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]getConnectedBLEDevices(deprecated)

getConnectedBLEDevices(): Array<string>

获取和当前设备连接的BLE设备。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/7TQ4AVU2QDGMe0MbM-50cA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=7A6750B9DA23B688B39FF033D3D3B1D7349D43CA2939FC7DE68156D758330753)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.getConnectedBLEDevices](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#blegetconnectedbledevices)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Array<string> | 返回当前设备作为Server端时连接BLE设备地址集合。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
try {
    let result: Array<string>  = bluetoothManager.BLE.getConnectedBLEDevices();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]startBLEScan(deprecated)

startBLEScan(filters: Array<ScanFilter>, options?: ScanOptions): void

发起BLE扫描流程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/669aVS3RRpGOiuI30X4khg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=00DF65922D67C103CE2F36BBCF43D40C5D0D99B85E683176CE3B520AE49100A5)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.startBLEScan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#blestartblescan)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| filters | Array<[ScanFilter](#scanfilterdeprecated)\> | 是 | 表示扫描结果过滤策略集合，如果不使用过滤的方式，该参数设置为null。 |
| options | [ScanOptions](#scanoptionsdeprecated) | 否 | 表示扫描的参数配置，可选参数。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: Array<bluetoothManager.ScanResult>) {
    console.info('BLE scan device find result = '+ JSON.stringify(data));
}
try {
    bluetoothManager.BLE.on("BLEDeviceFind", onReceiveEvent);
    let scanfilter: bluetoothManager.ScanFilter = {
        deviceId:"XX:XX:XX:XX:XX:XX",
        name:"test",
        serviceUuid:"00001888-0000-1000-8000-00805f9b34fb"
    };
    let scanoptions: bluetoothManager.ScanOptions = {
        interval: 500,
        dutyMode: bluetoothManager.ScanDuty.SCAN_MODE_LOW_POWER,
        matchMode: bluetoothManager.MatchMode.MATCH_MODE_AGGRESSIVE,
    }
    bluetoothManager.BLE.startBLEScan([scanfilter], scanoptions);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]stopBLEScan(deprecated)

stopBLEScan(): void

停止BLE扫描流程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/ke-N4qX-Q4ya24mjnmo1aA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=49B204DE94279A95D967D2AB257DC5102C7CD256335939F3C1808114081DB031)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.stopBLEScan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#blestopblescan)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
try {
    bluetoothManager.BLE.stopBLEScan();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]on('BLEDeviceFind')(deprecated)

on(type: 'BLEDeviceFind', callback: Callback<Array<ScanResult>>): void

订阅BLE设备发现上报事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/xZ6Czq0ATwKdaUtlVpBckQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=44C6C7D2205D829319BC909F3D89C6364B19E8E960CE712F97B6F4E676D20A06)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.on('BLEDeviceFind')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#bleonbledevicefind)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"BLEDeviceFind"字符串，表示BLE设备发现事件。 |
| callback | Callback<Array<[ScanResult](#scanresultdeprecated)\>> | 是 | 表示回调函数的入参，发现的设备集合。回调函数由用户创建通过该接口注册。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: Array<bluetoothManager.ScanResult>) {
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
try {
    bluetoothManager.BLE.on('BLEDeviceFind', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]off('BLEDeviceFind')(deprecated)

off(type: 'BLEDeviceFind', callback?: Callback<Array<ScanResult>>): void

取消订阅BLE设备发现上报事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/aWNEewt4QnON1HsjdQc_yA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=47F7BAEBAEB684353FA7E68FE1410CB689C468E860EF5B72E87437E7304722A3)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.off('BLEDeviceFind')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#bleoffbledevicefind)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"BLEDeviceFind"字符串，表示BLE设备发现事件。 |
| callback | Callback<Array<[ScanResult](#scanresultdeprecated)\>> | 否 | 表示取消订阅BLE设备发现事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: Array<bluetoothManager.ScanResult>) {
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
try {
    bluetoothManager.BLE.on('BLEDeviceFind', onReceiveEvent);
    bluetoothManager.BLE.off('BLEDeviceFind', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### BaseProfile

profile基类。

#### \[h2\]getConnectionDevices(deprecated)

getConnectionDevices(): Array<string>

获取已连接设备列表。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/uLjaVuUYRZq9Rwq9zvrlGw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=BB2AD3F9462369AE20F26B80933E983A0A6307AFB5AFE376A7F109F457C8C461)

从API version 9开始支持，从API version 10开始废弃。建议使用[baseProfile.getConnectedDevices](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-baseprofile#baseprofilegetconnecteddevices)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Array<string> | 返回已连接设备的地址列表。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
try {
    let a2dpSrc: bluetoothManager.A2dpSourceProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_A2DP_SOURCE) as bluetoothManager.A2dpSourceProfile;
    let retArray: Array<string> = a2dpSrc.getConnectionDevices();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]getDeviceState(deprecated)

getDeviceState(device: string): ProfileConnectionState

获取设备profile的连接状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/W_YNvqFCQCu3rGNcvuan4A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=ECDB67506289FA5F48EDDF710A6246E2880744D7FFBA13BED93DA667E21C586A)

从API version 9开始支持，从API version 10开始废弃。建议使用[baseProfile.getConnectionState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-baseprofile#baseprofilegetconnectionstate)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| device | string | 是 | 远端设备地址。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [ProfileConnectionState](#profileconnectionstatedeprecated) | 返回profile的连接状态。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
try {
    let a2dpSrc: bluetoothManager.A2dpSourceProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_A2DP_SOURCE) as bluetoothManager.A2dpSourceProfile;
    let ret: bluetoothManager.ProfileConnectionState = a2dpSrc.getDeviceState('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### A2dpSourceProfile

使用A2dpSourceProfile方法之前需要创建该类的实例进行操作，通过getProfile()方法构造此实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/cuwUH52PQReakF91NjPHCg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=F915B65AB327388C01001314EFFE707DAD5E8B93C863DA4F83F49DB13A1B5245)

从API version 9开始支持，从API version 10开始废弃。建议使用[a2dp.A2dpSourceProfile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-a2dp#a2dpsourceprofile)替代。

#### \[h2\]connect(deprecated)

connect(device: string): void

发起设备的A2dp服务连接请求。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/VyjBt3x8T2G2eS3vP0pOjg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=0C1F9083AEC1C1863A4D9FA8674EDE46E36B8D8E5F9FDFDA93E55009099F6027)

从API version 9开始支持，从API version 10开始废弃。替代接口仅向系统应用开放。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| device | string | 是 | 远端设备地址。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
try {
    let a2dpSrc: bluetoothManager.A2dpSourceProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_A2DP_SOURCE) as bluetoothManager.A2dpSourceProfile;
    a2dpSrc.connect('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]disconnect(deprecated)

disconnect(device: string): void

断开设备的a2dp服务连接。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/_m3yTSwIQQ6R6WHEVgrLmw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=48612A43EAF4C9597D2016733757C7F19CA714E7BE539F51729FA4A8C3BBF646)

从API version 9开始支持，从API version 10开始废弃。替代接口仅向系统应用开放。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| device | string | 是 | 远端设备地址。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
try {
    let a2dpSrc: bluetoothManager.A2dpSourceProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_A2DP_SOURCE) as bluetoothManager.A2dpSourceProfile;
    a2dpSrc.disconnect('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]on('connectionStateChange')(deprecated)

on(type: 'connectionStateChange', callback: Callback<[StateChangeParam](#statechangeparamdeprecated)\>): void

订阅a2dp连接状态变化事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/f7NETpbBTLO6hdDQLHL1Ow/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=083DC890A073EA5C9AD265F11F478B2EB8449790EB88BA0D85F67E68540B6017)

从API version 9开始支持，从API version 10开始废弃。建议使用[baseProfile.on('connectionStateChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-baseprofile#baseprofileonconnectionstatechange)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"connectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<[StateChangeParam](#statechangeparamdeprecated)\> | 是 | 表示回调函数的入参。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.StateChangeParam) {
    console.info('a2dp state = '+ JSON.stringify(data));
}
try {
let a2dpSrc: bluetoothManager.A2dpSourceProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_A2DP_SOURCE) as bluetoothManager.A2dpSourceProfile;
a2dpSrc.on('connectionStateChange', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### \[h2\]off('connectionStateChange')(deprecated)

off(type: 'connectionStateChange', callback?: Callback<[StateChangeParam](#statechangeparamdeprecated)\>): void

取消订阅a2dp连接状态变化事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/3ZkwOHYcSSuSpWDoyLKG4g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=EDCD45F59CB8F30025F498E6F861D944294D61DF5E7EA8389970DC5837B18587)

从API version 9开始支持，从API version 10开始废弃。建议使用[baseProfile.off('connectionStateChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-baseprofile#baseprofileoffconnectionstatechange)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"connectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<[StateChangeParam](#statechangeparamdeprecated)\> | 否 | 表示回调函数的入参。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.StateChangeParam) {
    console.info('a2dp state = '+ JSON.stringify(data));
}
try {
let a2dpSrc: bluetoothManager.A2dpSourceProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_A2DP_SOURCE) as bluetoothManager.A2dpSourceProfile;
a2dpSrc.on('connectionStateChange', onReceiveEvent);
a2dpSrc.off('connectionStateChange', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### \[h2\]getPlayingState(deprecated)

getPlayingState(device: string): PlayingState

获取设备的播放状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/ftFtebf4SNGGEpfJKuTQJg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=7AA17AB950A57C7D37F7ABF44E8E5749517E645038143AEF748042187C001E8F)

从API version 9开始支持，从API version 10开始废弃。建议使用[getPlayingState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-a2dp#getplayingstate)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| device | string | 是 | 远端设备地址。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [PlayingState](#playingstatedeprecated) | 远端设备的播放状态。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
try {
    let a2dpSrc: bluetoothManager.A2dpSourceProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_A2DP_SOURCE) as bluetoothManager.A2dpSourceProfile;
    let state: bluetoothManager.PlayingState  = a2dpSrc.getPlayingState('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### HandsFreeAudioGatewayProfile(deprecated)

使用HandsFreeAudioGatewayProfile方法之前需要创建该类的实例进行操作，通过getProfile()方法构造此实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/Q8SMuorxTICaoZEWMtE49Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=90FE059CB3BA66F7830B25593BBFA94FC8E6044F31BA7BE11A46F2818502573E)

从API version 9开始支持，从API version 10开始废弃。建议使用[hfp.HandsFreeAudioGatewayProfile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-hfp#handsfreeaudiogatewayprofile)替代。

#### \[h2\]connect(deprecated)

connect(device: string): void

连接设备的HFP服务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/qvU4fWuKRrCT7mci79ZVfw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=763338B08FDA43A0D0BB5C8042D0AD3730CC655E8F05F17130907B91ABF4AEA1)

从API version 9开始支持，从API version 10开始废弃。替代接口仅向系统应用开放。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| device | string | 是 | 远端设备地址。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
try {
    let hfpAg: bluetoothManager.HandsFreeAudioGatewayProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_HANDS_FREE_AUDIO_GATEWAY) as bluetoothManager.HandsFreeAudioGatewayProfile;
    hfpAg.connect('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]disconnect(deprecated)

disconnect(device: string): void

断开连接设备的HFP服务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/tLRpbGi3RPicsjIiReXsww/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=0ACC1762C4685033A068565BD8F65E4EF28DDCAFAEC51F96A7024558B3C9AB89)

从API version 9开始支持，从API version 10开始废弃。替代接口仅向系统应用开放。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| device | string | 是 | 远端设备地址。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
try {
    let hfpAg: bluetoothManager.HandsFreeAudioGatewayProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_HANDS_FREE_AUDIO_GATEWAY) as bluetoothManager.HandsFreeAudioGatewayProfile;
    hfpAg.disconnect('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]on('connectionStateChange')(deprecated)

on(type: 'connectionStateChange', callback: Callback<[StateChangeParam](#statechangeparamdeprecated)\>): void

订阅HFP连接状态变化事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/71WIJRTsSc-mQdzcuz1QGg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=BF39CE9360BA8AC6B5963664ECC279D4FDF8B38592ACD326F97A46878045B72F)

从API version 9开始支持，从API version 10开始废弃。建议使用[baseProfile.on('connectionStateChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-baseprofile#baseprofileonconnectionstatechange)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"connectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<[StateChangeParam](#statechangeparamdeprecated)\> | 是 | 表示回调函数的入参。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.StateChangeParam) {
    console.info('hfp state = '+ JSON.stringify(data));
}
try {
let hfpAg: bluetoothManager.HandsFreeAudioGatewayProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_HANDS_FREE_AUDIO_GATEWAY) as
  bluetoothManager.HandsFreeAudioGatewayProfile;
hfpAg.on('connectionStateChange', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]off('connectionStateChange')(deprecated)

off(type: 'connectionStateChange', callback?: Callback<[StateChangeParam](#statechangeparamdeprecated)\>): void

取消订阅HFP连接状态变化事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/geU_J9UUTZOc6xcs4dcsAQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=0900FE0F7E7B0037E5CE9318B5BDD5BA05A3DC5A5F42A5F359B914814F5065DE)

从API version 9开始支持，从API version 10开始废弃。建议使用[baseProfile.off('connectionStateChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-baseprofile#baseprofileoffconnectionstatechange)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"connectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<[StateChangeParam](#statechangeparamdeprecated)\> | 否 | 表示回调函数的入参。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| **示例：** |  |

```js
import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.StateChangeParam) {
    console.info('hfp state = '+ JSON.stringify(data));
}
try {
let hfpAg: bluetoothManager.HandsFreeAudioGatewayProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_HANDS_FREE_AUDIO_GATEWAY) as
  bluetoothManager.HandsFreeAudioGatewayProfile;
hfpAg.on('connectionStateChange', onReceiveEvent);
hfpAg.off('connectionStateChange', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### HidHostProfile(deprecated)

使用HidHostProfile方法之前需要创建该类的实例进行操作，通过getProfile()方法构造此实例。

#### \[h2\]on('connectionStateChange')(deprecated)

on(type: 'connectionStateChange', callback: Callback<[StateChangeParam](#statechangeparamdeprecated)\>): void

订阅HidHost连接状态变化事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/Vqmdwe_FSjeRPiMblH6NoA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=34DEA790A21DE58697E6CAB43DA72BC391DE7483E2F0600C627068397B651761)

从API version 9开始支持，从API version 10开始废弃。建议使用[baseProfile.on('connectionStateChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-baseprofile#baseprofileonconnectionstatechange)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"connectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<[StateChangeParam](#statechangeparamdeprecated)\> | 是 | 表示回调函数的入参。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.StateChangeParam) {
    console.info('hidHost state = '+ JSON.stringify(data));
}
try {
let hidHost: bluetoothManager.HidHostProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_HID_HOST) as bluetoothManager.HidHostProfile;
hidHost.on('connectionStateChange', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]off('connectionStateChange')(deprecated)

off(type: 'connectionStateChange', callback?: Callback<[StateChangeParam](#statechangeparamdeprecated)\>): void

取消订阅HidHost连接状态变化事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/rtgKy9JtTMuOHaXfyRp7Gg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=A65FF0473B29487FBB80DD09FB205B6446494BBFF9B16D6E1D06362312588D20)

从API version 9开始支持，从API version 10开始废弃。建议使用[baseProfile.off('connectionStateChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-baseprofile#baseprofileoffconnectionstatechange)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"connectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<[StateChangeParam](#statechangeparamdeprecated)\> | 否 | 表示回调函数的入参。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.StateChangeParam) {
    console.info('hidHost state = '+ JSON.stringify(data));
}
try {
let hidHost: bluetoothManager.HidHostProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_HID_HOST) as bluetoothManager.HidHostProfile;
hidHost.on('connectionStateChange', onReceiveEvent);
hidHost.off('connectionStateChange', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### PanProfile

使用PanProfile方法之前需要创建该类的实例进行操作，通过getProfile()方法构造此实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/UGI1xj1BRfK7RA99PnWceg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=B16960C936488069D5DF474020219EF30B273201CB739F847638F81E1F9EE3DF)

从API version 9开始支持，从API version 10开始废弃。建议使用[pan.createPanProfile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-pan#pancreatepanprofile)替代。

#### \[h2\]on('connectionStateChange')(deprecated)

on(type: 'connectionStateChange', callback: Callback<[StateChangeParam](#statechangeparamdeprecated)\>): void

订阅Pan连接状态变化事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/BzsC7I8yTCCPS-2tc04ORg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=5317A8537209C2B1FBE735F0AC3EEE48A536E5BB9F20C18C525BAE8D45D3A073)

从API version 9开始支持，从API version 10开始废弃。建议使用[baseProfile.on('connectionStateChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-baseprofile#baseprofileonconnectionstatechange)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"connectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<[StateChangeParam](#statechangeparamdeprecated)\> | 是 | 表示回调函数的入参。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.StateChangeParam) {
    console.info('pan state = '+ JSON.stringify(data));
}
try {
let panProfile: bluetoothManager.PanProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_PAN_NETWORK) as bluetoothManager.PanProfile;
panProfile.on('connectionStateChange', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]off('connectionStateChange')(deprecated)

off(type: 'connectionStateChange', callback?: Callback<[StateChangeParam](#statechangeparamdeprecated)\>): void

取消订阅Pan连接状态变化事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/15x6-XtDQiuNlV4i50dAeQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=8BA98BE8F7227E4EE87583B0174916DEEB686A8E210A8F11F6465378CBACFAA4)

从API version 9开始支持，从API version 10开始废弃。建议使用[baseProfile.off('connectionStateChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-baseprofile#baseprofileoffconnectionstatechange)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"connectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<[StateChangeParam](#statechangeparamdeprecated)\> | 否 | 表示回调函数的入参。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.StateChangeParam) {
    console.info('pan state = '+ JSON.stringify(data));
}
try {
let panProfile: bluetoothManager.PanProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_PAN_NETWORK) as bluetoothManager.PanProfile;
panProfile.on('connectionStateChange', onReceiveEvent);
panProfile.off('connectionStateChange', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### GattServer

server端类，使用server端方法之前需要创建该类的实例进行操作，通过createGattServer()方法构造此实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/C4JxxHkqTcS1oQDblGFmnA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=A57156A41D1A433FA4F1723AC5E304835015E084577C51D85881429C7B42D562)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#gattserver)替代。

#### \[h2\]startAdvertising(deprecated)

startAdvertising(setting: AdvertiseSetting, advData: AdvertiseData, advResponse?: AdvertiseData): void

开始发送BLE广播。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/K3Q1IbuxRBqAlQUOvX-dXg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=47FAEB864959DCCBD2047BC6B2D9322E41A0EEAE53F54787536A57D286A838B2)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.startAdvertising](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#blestartadvertising)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| setting | [AdvertiseSetting](#advertisesettingdeprecated) | 是 | BLE广播的相关参数。 |
| advData | [AdvertiseData](#advertisedatadeprecated) | 是 | BLE广播包内容。 |
| advResponse | [AdvertiseData](#advertisedatadeprecated) | 否 | BLE回复扫描请求回复响应。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
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
let gattServer = bluetoothManager.BLE.createGattServer();
try {
    let setting: bluetoothManager.AdvertiseSetting = {
        interval:150,
        txPower:0,
        connectable:true,
    };
    let manufactureDataUnit: bluetoothManager.ManufactureData = {
        manufactureId:4567,
        manufactureValue:manufactureValueBuffer.buffer
    };
    let serviceDataUnit: bluetoothManager.ServiceData = {
        serviceUuid:"00001888-0000-1000-8000-00805f9b34fb",
        serviceValue:serviceValueBuffer.buffer
    };
    let advData: bluetoothManager.AdvertiseData = {
        serviceUuids:["00001888-0000-1000-8000-00805f9b34fb"],
        manufactureData:[manufactureDataUnit],
        serviceData:[serviceDataUnit],
    };
    let advResponse: bluetoothManager.AdvertiseData = {
        serviceUuids:["00001888-0000-1000-8000-00805f9b34fb"],
        manufactureData:[manufactureDataUnit],
        serviceData:[serviceDataUnit],
    };
    gattServer.startAdvertising(setting, advData ,advResponse);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]stopAdvertising(deprecated)

stopAdvertising(): void

停止发送BLE广播。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/LPzQDeVQTAqvRL9exRhvcw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=F9A77DFF2D345A30DAF69CB8531128343B13C280F1508000BA54F6DD43AAD510)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.stopAdvertising](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#blestopadvertising)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
let server = bluetoothManager.BLE.createGattServer();
try {
    server.stopAdvertising();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]addService(deprecated)

addService(service: GattService): void

server端添加服务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/SCzugQ9EQLiS0cxgpciWEQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=7E66CBBFF5DDF0647A3B9FA190FF1D7A3DAC99B20172924C9D1B79493F243028)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#addService](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#addservice)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| service | [GattService](#gattservicedeprecated) | 是 | 服务端的service数据。BLE广播的相关参数 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
// 创建descriptors
let descriptors: Array<bluetoothManager.BLEDescriptor> = [];
let arrayBuffer = new ArrayBuffer(8);
let descV = new Uint8Array(arrayBuffer);
descV[0] = 11;
let descriptor: bluetoothManager.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
    descriptorUuid: '00002902-0000-1000-8000-00805F9B34FB', descriptorValue: arrayBuffer};
descriptors[0] = descriptor;

// 创建characteristics
let characteristics: Array<bluetoothManager.BLECharacteristic> = [];
let arrayBufferC = new ArrayBuffer(8);
let cccV = new Uint8Array(arrayBufferC);
cccV[0] = 1;
let characteristic: bluetoothManager.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB', characteristicValue: arrayBufferC, descriptors:descriptors};
let characteristicN: bluetoothManager.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001821-0000-1000-8000-00805F9B34FB', characteristicValue: arrayBufferC, descriptors:descriptors};
characteristics[0] = characteristic;

// 创建gattService
let gattService: bluetoothManager.GattService = {serviceUuid:'00001810-0000-1000-8000-00805F9B34FB', isPrimary: true, characteristics:characteristics, includeServices:[]};

let gattServer  = bluetoothManager.BLE.createGattServer();
try {
    gattServer.addService(gattService);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]removeService(deprecated)

removeService(serviceUuid: string): void

删除已添加的服务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/M66SFwkER0SQ9Ux9ks61LQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=FE7E2EF2B51813791F3723E6BACAEE3B6B4955DA115E1E5C4EA9564D5D49336A)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#removeService](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#removeservice)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| serviceUuid | string | 是 | service的UUID，例如“00001810-0000-1000-8000-00805F9B34FB”。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
let server = bluetoothManager.BLE.createGattServer();
try {
    server.removeService('00001810-0000-1000-8000-00805F9B34FB');
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]close(deprecated)

close(): void

关闭服务端功能，去注册server在协议栈的注册，调用该接口后[GattServer](#gattserver)实例将不能再使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/zbSfvuqcRVuQpI0O6yinog/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=63E79AEEFA6111D16E7C8E00031218B9EB9010823B92C92D944E43F64C45C252)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#close](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#close)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
let server = bluetoothManager.BLE.createGattServer();
try {
    server.close();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]notifyCharacteristicChanged(deprecated)

notifyCharacteristicChanged(deviceId: string, notifyCharacteristic: NotifyCharacteristic): void

server端特征值发生变化时，主动通知已连接的client设备。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/9UyluYaBSXm_pRafJ9yyAA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=802D8E08ECB8D2F1CF192C8870ADD793D7F179AA0BE25197D8FC8E9C6FACFC26)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#notifyCharacteristicChanged](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#notifycharacteristicchanged)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| deviceId | string | 是 | 接收通知的client端设备地址，例如“XX:XX:XX:XX:XX:XX”。 |
| notifyCharacteristic | [NotifyCharacteristic](#notifycharacteristicdeprecated) | 是 | 通知的特征值数据。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
// 创建descriptors
let descriptors: Array<bluetoothManager.BLEDescriptor> = [];
let arrayBuffer = new ArrayBuffer(8);
let descV = new Uint8Array(arrayBuffer);
descV[0] = 11;
let descriptor: bluetoothManager.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
    descriptorUuid: '00002902-0000-1000-8000-00805F9B34FB', descriptorValue: arrayBuffer};
descriptors[0] = descriptor;
let arrayBufferC = new ArrayBuffer(8);
let characteristic: bluetoothManager.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB', characteristicValue: arrayBufferC, descriptors:descriptors};
let notifyCharacteristic: bluetoothManager.NotifyCharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001821-0000-1000-8000-00805F9B34FB', characteristicValue: characteristic.characteristicValue, confirm: false};
let server = bluetoothManager.BLE.createGattServer();
try {
    server.notifyCharacteristicChanged('XX:XX:XX:XX:XX:XX', notifyCharacteristic);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]sendResponse(deprecated)

sendResponse(serverResponse: ServerResponse): void

server端回复client端的读写请求。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/sTxhoy8QRVWg-rB3r3Hncg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=22959932D6964553180BDCB8DE08605B7CDEC43CAFD7FD93E419065BDE974691)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#sendResponse](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#sendresponse)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| serverResponse | [ServerResponse](#serverresponsedeprecated) | 是 | server端回复的响应数据。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
/* send response */
let arrayBufferCCC = new ArrayBuffer(8);
let cccValue = new Uint8Array(arrayBufferCCC);
cccValue[0] = 1;
let serverResponse: bluetoothManager.ServerResponse = {
    deviceId: 'XX:XX:XX:XX:XX:XX',
    transId: 0,
    status: 0,
    offset: 0,
    value: arrayBufferCCC,
};

let gattServer = bluetoothManager.BLE.createGattServer();
try {
    gattServer.sendResponse(serverResponse);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]on('characteristicRead')(deprecated)

on(type: 'characteristicRead', callback: Callback<CharacteristicReadRequest>): void

server端订阅特征值读请求事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/NZ3a8GJcSMGWJVnCNZ610A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=EFCA83435B1003521A5F0B8DB5A720CEF7C417DDEC17C8FF60C1F193327F60F1)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#on('characteristicRead')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#oncharacteristicread)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"characteristicRead"字符串，表示特征值读请求事件。 |
| callback | Callback<[CharacteristicReadRequest](#characteristicreadrequestdeprecated)\> | 是 | 表示回调函数的入参，client端发送的读请求数据。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
let arrayBufferCCC = new ArrayBuffer(8);
let cccValue = new Uint8Array(arrayBufferCCC);
cccValue[0] = 1;
function ReadCharacteristicReq(characteristicReadRequest: bluetoothManager.CharacteristicReadRequest) {
    let deviceId: string = characteristicReadRequest.deviceId;
    let transId: number = characteristicReadRequest.transId;
    let offset: number = characteristicReadRequest.offset;
    let characteristicUuid: string = characteristicReadRequest.characteristicUuid;

    let serverResponse: bluetoothManager.ServerResponse = {deviceId: deviceId, transId: transId, status: 0, offset: offset, value:arrayBufferCCC};

    try {
        gattServer.sendResponse(serverResponse);
    } catch (err) {
        console.error('errCode: ' + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
    }
}

let gattServer = bluetoothManager.BLE.createGattServer();
gattServer.on("characteristicRead", ReadCharacteristicReq);
```

#### \[h2\]off('characteristicRead')(deprecated)

off(type: 'characteristicRead', callback?: Callback<CharacteristicReadRequest>): void

server端取消订阅特征值读请求事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/zrJEqEKzTBqrwYy4GmtOyg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=A1DFF850BE42C626B40AD66DA5CCF63B73D636AD8F94E3CB75ABA244DC02ED23)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#off('characteristicRead')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#offcharacteristicread)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"characteristicRead"字符串，表示特征值读请求事件。 |
| callback | Callback<[CharacteristicReadRequest](#characteristicreadrequestdeprecated)\> | 否 | 表示取消订阅特征值读请求事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
try {
let gattServer = bluetoothManager.BLE.createGattServer();
gattServer.off("characteristicRead");
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]on('characteristicWrite')(deprecated)

on(type: 'characteristicWrite', callback: Callback<CharacteristicWriteRequest>): void

server端订阅特征值写请求事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/PyydIHW6QTeYW1FwxZEUXw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=642BCB916CFDC5FCD3F7529D89523F31052D6972411FCAB1C5A0B58332AFDA53)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#on('characteristicWrite')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#oncharacteristicwrite)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"characteristicWrite"字符串，表示特征值写请求事件。 |
| callback | Callback<[CharacteristicWriteRequest](#characteristicwriterequestdeprecated)\> | 是 | 表示回调函数的入参，client端发送的写请求数据。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
let arrayBufferCCC = new ArrayBuffer(8);
let cccValue = new Uint8Array(arrayBufferCCC);
function WriteCharacteristicReq(characteristicWriteRequest: bluetoothManager.CharacteristicWriteRequest) {
    let deviceId: string = characteristicWriteRequest.deviceId;
    let transId: number = characteristicWriteRequest.transId;
    let offset: number = characteristicWriteRequest.offset;
    let isPrep: boolean = characteristicWriteRequest.isPrep;
    let needRsp: boolean = characteristicWriteRequest.needRsp;
    let value: Uint8Array =  new Uint8Array(characteristicWriteRequest.value);
    let characteristicUuid: string = characteristicWriteRequest.characteristicUuid;

    cccValue[0] = value[0];
    let serverResponse: bluetoothManager.ServerResponse = {deviceId: deviceId, transId: transId, status: 0, offset: offset, value:arrayBufferCCC};

    try {
        gattServer.sendResponse(serverResponse);
    } catch (err) {
        console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
}

let gattServer = bluetoothManager.BLE.createGattServer();
gattServer.on("characteristicWrite", WriteCharacteristicReq);
```

#### \[h2\]off('characteristicWrite')(deprecated)

off(type: 'characteristicWrite', callback?: Callback<CharacteristicWriteRequest>): void

server端取消订阅特征值写请求事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/KLEmzMqtRPKQZOmKF1DYDQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=6815E46FC5415B60D0BA0318F7074D748772B5C97CAFE303E795CC0FD22D7B53)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#off('characteristicWrite')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#offcharacteristicwrite)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"characteristicWrite"字符串，表示特征值写请求事件。 |
| callback | Callback<[CharacteristicWriteRequest](#characteristicwriterequestdeprecated)\> | 否 | 表示取消订阅特征值写请求事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
try {
let gattServer = bluetoothManager.BLE.createGattServer();
gattServer.off("characteristicWrite");
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]on('descriptorRead')(deprecated)

on(type: 'descriptorRead', callback: Callback<DescriptorReadRequest>): void

server端订阅描述符读请求事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/NXlQfug8S1icbkzBOjkftQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=8EDEDED21CA3C4B7F4D7FB600095F0196AF2C7993375018EB92EA7F6BA1EF24B)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#on('descriptorRead')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#ondescriptorread)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"descriptorRead"字符串，表示描述符读请求事件。 |
| callback | Callback<[DescriptorReadRequest](#descriptorreadrequestdeprecated)\> | 是 | 表示回调函数的入参，client端发送的读请求数据。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```js
import { BusinessError } from '@kit.BasicServicesKit';
let arrayBufferDesc = new ArrayBuffer(8);
let descValue = new Uint8Array(arrayBufferDesc);
descValue[0] = 1;
function ReadDescriptorReq(descriptorReadRequest: bluetoothManager.DescriptorReadRequest) {
    let deviceId: string = descriptorReadRequest.deviceId;
    let transId: number = descriptorReadRequest.transId;
    let offset: number = descriptorReadRequest.offset;
    let descriptorUuid: string = descriptorReadRequest.descriptorUuid;

    let serverResponse: bluetoothManager.ServerResponse = {deviceId: deviceId, transId: transId, status: 0, offset: offset, value:arrayBufferDesc};

    try {
        gattServer.sendResponse(serverResponse);
    } catch (err) {
        console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
}

let gattServer = bluetoothManager.BLE.createGattServer();
gattServer.on("descriptorRead", ReadDescriptorReq);
```

#### \[h2\]off('descriptorRead')(deprecated)

off(type: 'descriptorRead', callback?: Callback<DescriptorReadRequest>): void

server端取消订阅描述符读请求事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/DtNrWxHoTqiG_NGYXQT-RQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=7D4CB8480FD4BB5365F2797550943802E9FEE4E7D45F54F26BD0571F03285FC0)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#off('descriptorRead')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#offdescriptorread)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"descriptorRead"字符串，表示描述符读请求事件。 |
| callback | Callback<[DescriptorReadRequest](#descriptorreadrequestdeprecated)\> | 否 | 表示取消订阅描述符读请求事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
try {
let gattServer = bluetoothManager.BLE.createGattServer();
gattServer.off("descriptorRead");
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]on('descriptorWrite')(deprecated)

on(type: 'descriptorWrite', callback: Callback<DescriptorWriteRequest>): void

server端订阅描述符写请求事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/Erbn48fCStOc078Tu3ulww/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=4531DEE95974328058A9442ECE9F8553D75F368405311E4E91A3FAD9385DFAF7)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#on('descriptorWrite')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#ondescriptorwrite)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"descriptorWrite"字符串，表示描述符写请求事件。 |
| callback | Callback<[DescriptorWriteRequest](#descriptorwriterequestdeprecated)\> | 是 | 表示回调函数的入参，client端发送的写请求数据。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
let arrayBufferDesc = new ArrayBuffer(8);
let descValue = new Uint8Array(arrayBufferDesc);
function WriteDescriptorReq(descriptorWriteRequest: bluetoothManager.DescriptorWriteRequest) {
    let deviceId: string = descriptorWriteRequest.deviceId;
    let transId: number = descriptorWriteRequest.transId;
    let offset: number = descriptorWriteRequest.offset;
    let isPrep: boolean = descriptorWriteRequest.isPrep;
    let needRsp: boolean = descriptorWriteRequest.needRsp;
    let value: Uint8Array = new Uint8Array(descriptorWriteRequest.value);
    let descriptorUuid: string = descriptorWriteRequest.descriptorUuid;

    descValue[0] = value[0];
    let serverResponse: bluetoothManager.ServerResponse = {deviceId: deviceId, transId: transId, status: 0, offset: offset, value:arrayBufferDesc};

    try {
        gattServer.sendResponse(serverResponse);
    } catch (err) {
        console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
}

let gattServer = bluetoothManager.BLE.createGattServer();
gattServer.on("descriptorWrite", WriteDescriptorReq);
```

#### \[h2\]off('descriptorWrite')(deprecated)

off(type: 'descriptorWrite', callback?: Callback<DescriptorWriteRequest>): void

server端取消订阅描述符写请求事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/aLAW0LkURLiPdb4bwTV9Ww/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=EF69FB05C3813988BD9C35DA618F59FFAD09E706129BFE6F95A88E9ED70200EB)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#off('descriptorWrite')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#offdescriptorwrite)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"descriptorWrite"字符串，表示描述符写请求事件。 |
| callback | Callback<[DescriptorWriteRequest](#descriptorwriterequestdeprecated)\> | 否 | 表示取消订阅描述符写请求事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
try {
let gattServer = bluetoothManager.BLE.createGattServer();
gattServer.off("descriptorWrite");
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]on('connectStateChange')(deprecated)

on(type: 'connectStateChange', callback: Callback<BLEConnectChangedState>): void

server端订阅BLE连接状态变化事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/nVzUoUg0QEu3GboqRZzzIw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=5C708D27C3907C55F401A9B392F2E3C7ABCDFD76AB8EC691B27441AA97C08647)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#on('connectionStateChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#onconnectionstatechange)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"connectStateChange"字符串，表示BLE连接状态变化事件。 |
| callback | Callback<[BLEConnectChangedState](#bleconnectchangedstatedeprecated)\> | 是 | 表示回调函数的入参，连接状态。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
function Connected(BLEConnectChangedState: bluetoothManager.BLEConnectChangedState) {
  let deviceId: string = BLEConnectChangedState.deviceId;
  let status: bluetoothManager.ProfileConnectionState  = BLEConnectChangedState.state;
}
try {
let gattServer = bluetoothManager.BLE.createGattServer();
gattServer.on("connectStateChange", Connected);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]off('connectStateChange')(deprecated)

off(type: 'connectStateChange', callback?: Callback<BLEConnectChangedState>): void

server端取消订阅BLE连接状态变化事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/qEYf7p5yToiAd3yKhr8Qng/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=95365F2303E700568792B76F0874DA8FEB014BF7967D512BB3DAA7CAB1506B12)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#off('connectionStateChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#offconnectionstatechange)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"connectStateChange"字符串，表示BLE连接状态变化事件。 |
| callback | Callback<[BLEConnectChangedState](#bleconnectchangedstatedeprecated)\> | 否 | 表示取消订阅BLE连接状态变化事件。不填该参数则取消订阅该type对应的所有回调。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
try {
let gattServer = bluetoothManager.BLE.createGattServer();
gattServer.off("connectStateChange");
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### GattClientDevice

client端类，使用client端方法之前需要创建该类的实例进行操作，通过createGattClientDevice(deviceId: string)方法构造此实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/MtmM5Z9ARqySnOPfunEjRA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=9D8485141AC66F51B6D4622F83FF566EDBF77718253C3FFF352CC69B1AA4829D)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#gattclientdevice)替代。

#### \[h2\]connect(deprecated)

connect(): void

client端发起连接远端蓝牙低功耗设备。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/qMtNIRd7QyG-TukxJShqaw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=5C780F75F588F841671E11CF454DC79015EC5DEB6F1C2EAA9343916598AD04D1)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#connect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#connect)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.connect();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]disconnect(deprecated)

disconnect(): void

client端断开与远端蓝牙低功耗设备的连接。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/vO3OPkSuQy6Kt_Ed1e41xQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=2C6E3846E0BA10B9F44627AE0938BC5F036A5216749FE4B5685C760C3DD1B135)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#disconnect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#disconnect)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.disconnect();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]close(deprecated)

close(): void

关闭客户端功能，注销client在协议栈的注册，调用该接口后[GattClientDevice](#gattclientdevice)实例将不能再使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/lWmeOZVWQwak45PaX7io6g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=5735541C557C02CBB4811325349AD1A1CE9EED1ED56FE61630515E9640FF05F9)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#close](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#close)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.close();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]getServices(deprecated)

getServices(callback: AsyncCallback<Array<GattService>>): void

client端获取蓝牙低功耗设备的所有服务，即服务发现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/KSCb8YX6RfqzNTl6kXn_EA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=0813CF11FD1C066EEC6DB255DD86F7FD6DEB8345BBFB7CCDED31066D76F41668)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#getServices](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#getservices)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[GattService](#gattservicedeprecated)\>> | 是 | client进行服务发现，通过注册回调函数获取。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@kit.BasicServicesKit';
// callback 模式
function getServices(code: BusinessError, gattServices: Array<bluetoothManager.GattService>) {
  if (code.code == 0) {
      let services: Array<bluetoothManager.GattService> = gattServices;
      console.info(`bluetooth code is ${code.code}`);
      console.info(`bluetooth services size is ${services.length}`);

      for (let i = 0; i < services.length; i++) {
        console.info(`bluetooth serviceUuid is ${services[i].serviceUuid}`);
      }
  }
}

try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.connect();
    device.getServices(getServices);
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```

#### \[h2\]getServices(deprecated)

getServices(): Promise<Array<GattService>>

client端获取蓝牙低功耗设备的所有服务，即服务发现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/s4jWpm-2Q7CVWvjH9GT2cw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=8EB0C5B850B6DFEFB699778E296376EB15F83A7C0E2D6340E94CB7818B84AFFE)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#getServices](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#getservices-1)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<[GattService](#gattservicedeprecated)\>> | client进行服务发现，通过promise形式获取。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
// Promise 模式
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.connect();
    device.getServices().then(result => {
        console.info("getServices successfully:" + JSON.stringify(result));
    });
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]readCharacteristicValue(deprecated)

readCharacteristicValue(characteristic: BLECharacteristic, callback: AsyncCallback<BLECharacteristic>): void

client端读取蓝牙低功耗设备特定服务的特征值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/ila3B461Sv6YvfVmT-WNKw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=C92C73F6BC306D87398E1CEB29BB9F5CB6405BD6D5DF4E7FED00EDFDB3CEE15A)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#readCharacteristicValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#readcharacteristicvalue)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| characteristic | [BLECharacteristic](#blecharacteristicdeprecated) | 是 | 待读取的特征值。 |
| callback | AsyncCallback<[BLECharacteristic](#blecharacteristicdeprecated)\> | 是 | client读取特征值，通过注册回调函数获取。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2901000 | Read forbidden. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@kit.BasicServicesKit';
function readCcc(code: BusinessError, BLECharacteristic: bluetoothManager.BLECharacteristic) {
    if (code.code != 0) {
        return;
    }
    console.info(`bluetooth characteristic uuid: ${BLECharacteristic.characteristicUuid}`);
    let value = new Uint8Array(BLECharacteristic.characteristicValue);
    console.info(`value length: ${value.length}`);
}

let descriptors: Array<bluetoothManager.BLEDescriptor> = [];
let bufferDesc = new ArrayBuffer(8);
let descV = new Uint8Array(bufferDesc);
descV[0] = 11;
let descriptor: bluetoothManager.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
    descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB', descriptorValue: bufferDesc};
descriptors[0] = descriptor;

let bufferCCC = new ArrayBuffer(8);
let cccV = new Uint8Array(bufferCCC);
cccV[0] = 1;
let characteristic: bluetoothManager.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
    characteristicValue: bufferCCC, descriptors:descriptors};

try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.readCharacteristicValue(characteristic, readCcc);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]readCharacteristicValue(deprecated)

readCharacteristicValue(characteristic: BLECharacteristic): Promise<BLECharacteristic>

client端读取蓝牙低功耗设备特定服务的特征值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/shzd2zRRTTqakmXIV3B3UA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=93710A37AF0479EB9C3B1B10458B351BEEB2816134A0C44563F11CAB78C55102)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#readCharacteristicValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#readcharacteristicvalue-1)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| characteristic | [BLECharacteristic](#blecharacteristicdeprecated) | 是 | 待读取的特征值。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[BLECharacteristic](#blecharacteristicdeprecated)\> | client读取特征值，通过promise形式获取。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2901000 | Read forbidden. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
let descriptors: Array<bluetoothManager.BLEDescriptor> = [];
let bufferDesc = new ArrayBuffer(8);
let descV = new Uint8Array(bufferDesc);
descV[0] = 11;
let descriptor: bluetoothManager.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
    descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB', descriptorValue: bufferDesc};
descriptors[0] = descriptor;

let bufferCCC = new ArrayBuffer(8);
let cccV = new Uint8Array(bufferCCC);
cccV[0] = 1;
let characteristic: bluetoothManager.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
    characteristicValue: bufferCCC, descriptors:descriptors};

try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.readCharacteristicValue(characteristic);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]readDescriptorValue(deprecated)

readDescriptorValue(descriptor: BLEDescriptor, callback: AsyncCallback<BLEDescriptor>): void

client端读取蓝牙低功耗设备特定的特征包含的描述符。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/Xdd51C4kTdibH6IPDOYuAQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=4220A40147C31E649B3E5E2F2925C7F795882E37B456EAECF7F34E19D8E61F63)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#readDescriptorValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#readdescriptorvalue)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| descriptor | [BLEDescriptor](#bledescriptordeprecated) | 是 | 待读取的描述符。 |
| callback | AsyncCallback<[BLEDescriptor](#bledescriptordeprecated)\> | 是 | client读取描述符，通过注册回调函数获取。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2901000 | Read forbidden. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@kit.BasicServicesKit';
function readDesc(code: BusinessError, BLEDescriptor: bluetoothManager.BLEDescriptor) {
    if (code.code != 0) {
        return;
    }
    console.info(`bluetooth descriptor uuid: ${BLEDescriptor.descriptorUuid}`);
    let value = new Uint8Array(BLEDescriptor.descriptorValue);
}

let bufferDesc = new ArrayBuffer(8);
let descV = new Uint8Array(bufferDesc);
descV[0] = 11;
let descriptor: bluetoothManager.BLEDescriptor = {
    serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
    descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB',
    descriptorValue: bufferDesc
};
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.readDescriptorValue(descriptor, readDesc);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]readDescriptorValue(deprecated)

readDescriptorValue(descriptor: BLEDescriptor): Promise<BLEDescriptor>

client端读取蓝牙低功耗设备特定的特征包含的描述符。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/H_oP-NuxTxe2sXUD39c2ig/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=AEECA22EF6E3279CA036451D701CF77170AD754702013E4ADFA32A597697E3CE)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#readDescriptorValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#readdescriptorvalue-1)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| descriptor | [BLEDescriptor](#bledescriptordeprecated) | 是 | 待读取的描述符。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[BLEDescriptor](#bledescriptordeprecated)\> | client读取描述符，通过promise形式获取。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2901000 | Read forbidden. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
let bufferDesc = new ArrayBuffer(8);
let descV = new Uint8Array(bufferDesc);
descV[0] = 11;
let descriptor: bluetoothManager.BLEDescriptor = {
    serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
    descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB',
    descriptorValue: bufferDesc
};
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.readDescriptorValue(descriptor);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]writeCharacteristicValue(deprecated)

writeCharacteristicValue(characteristic: BLECharacteristic): void

client端向低功耗蓝牙设备写入特定的特征值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/4QhZMo9dQ2aADY4EmYqWWA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=067359683AF60279922E68CFB2226D7DCC5206468CC8996C186C75746D5E5860)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#writeCharacteristicValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#writecharacteristicvalue)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| characteristic | [BLECharacteristic](#blecharacteristicdeprecated) | 是 | 蓝牙设备特征对应的二进制值及其它参数。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2901001 | Write forbidden. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
let descriptors: Array<bluetoothManager.BLEDescriptor> = [];
let bufferDesc = new ArrayBuffer(8);
let descV = new Uint8Array(bufferDesc);
descV[0] = 11;
let descriptor: bluetoothManager.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
    descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB', descriptorValue: bufferDesc};
descriptors[0] = descriptor;

let bufferCCC = new ArrayBuffer(8);
let cccV = new Uint8Array(bufferCCC);
cccV[0] = 1;
let characteristic: bluetoothManager.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
    characteristicValue: bufferCCC, descriptors:descriptors};
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.writeCharacteristicValue(characteristic);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]writeDescriptorValue(deprecated)

writeDescriptorValue(descriptor: BLEDescriptor): void

client端向低功耗蓝牙设备特定的描述符写入二进制数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/EWyU2e15Qfe7Icgpif7gsQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=4A97C5F358FACE543AE9350B12071048D23E4E93AAC6C6BD661637B1332D2FD4)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#writeDescriptorValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#writedescriptorvalue)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| descriptor | [BLEDescriptor](#bledescriptordeprecated) | 是 | 蓝牙设备描述符的二进制值及其它参数。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2901001 | Write forbidden. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
let bufferDesc = new ArrayBuffer(8);
let descV = new Uint8Array(bufferDesc);
descV[0] = 22;
let descriptor: bluetoothManager.BLEDescriptor = {
    serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
    descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB',
    descriptorValue: bufferDesc
};
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.writeDescriptorValue(descriptor);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]setBLEMtuSize(deprecated)

setBLEMtuSize(mtu: number): void

client协商远端蓝牙低功耗设备的最大传输单元（Maximum Transmission Unit, MTU），调用[connect](#connectdeprecated-1)接口连接成功后才能使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/uvE8_THyRH20ItOwDQNGvw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=68863D47C564DF414A7DC0AB643790541EE6F39CC05D741E63BE82904E5FEC4A)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#setBLEMtuSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#setblemtusize)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| mtu | number | 是 | 设置范围为22~512字节。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.setBLEMtuSize(128);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]setNotifyCharacteristicChanged(deprecated)

setNotifyCharacteristicChanged(characteristic: BLECharacteristic, enable: boolean): void

向服务端发送设置通知此特征值请求。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/U_1I8NkITL-35mUFyOmhMg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=C551D6CEAE3262F6123EE1EC045BF3565D326EFD2506E3B97190F27EC298611E)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#setCharacteristicChangeNotification](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#setcharacteristicchangenotification)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| characteristic | [BLECharacteristic](#blecharacteristicdeprecated) | 是 | 蓝牙低功耗特征。 |
| enable | boolean | 是 | 启用接收notify设置为true，否则设置为false。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
// 创建descriptors
let descriptors: Array<bluetoothManager.BLEDescriptor> = [];
let bufferDesc = new ArrayBuffer(8);
let descV = new Uint8Array(bufferDesc);
descV[0] = 11;
let descriptor: bluetoothManager.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
    descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB', descriptorValue: bufferDesc};
descriptors[0] = descriptor;

let bufferCCC = new ArrayBuffer(8);
let cccV = new Uint8Array(bufferCCC);
cccV[0] = 1;
let characteristic: bluetoothManager.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
    characteristicValue: bufferCCC, descriptors:descriptors};
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.setNotifyCharacteristicChanged(characteristic, false);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]on('BLECharacteristicChange')(deprecated)

on(type: 'BLECharacteristicChange', callback: Callback<BLECharacteristic>): void

订阅蓝牙低功耗设备的特征值变化事件。需要先调用setNotifyCharacteristicChanged接口才能接收server端的通知。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/XQ0oN-5TQbODKrYC_A8Q3g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=F9E5CAC1477BC68F367F5B334A426B05EC4328A6DF94116CFA19D5A3187E53B0)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#on('BLECharacteristicChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#onblecharacteristicchange)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"BLECharacteristicChange"字符串，表示特征值变化事件。 |
| callback | Callback<[BLECharacteristic](#blecharacteristicdeprecated)\> | 是 | 表示蓝牙低功耗设备的特征值变化事件的回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
function CharacteristicChange(characteristicChangeReq: ble.BLECharacteristic) {
    let serviceUuid: string = characteristicChangeReq.serviceUuid;
    let characteristicUuid: string = characteristicChangeReq.characteristicUuid;
    let value: Uint8Array = new Uint8Array(characteristicChangeReq.characteristicValue);
}
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.on('BLECharacteristicChange', CharacteristicChange);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]off('BLECharacteristicChange')(deprecated)

off(type: 'BLECharacteristicChange', callback?: Callback<BLECharacteristic>): void

取消订阅蓝牙低功耗设备的特征值变化事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/CaKPSVZoR6iUl1EkRIO7XA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=AB9D9EF272B19516CA3D501FA4159268BD7B366BF58B5EB687EF753D1AB84527)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#off('BLECharacteristicChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#offblecharacteristicchange)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"BLECharacteristicChange"字符串，表示特征值变化事件。 |
| callback | Callback<[BLECharacteristic](#blecharacteristicdeprecated)\> | 否 | 表示取消订阅蓝牙低功耗设备的特征值变化事件。不填该参数则取消订阅该type对应的所有回调。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.off('BLECharacteristicChange');
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]on('BLEConnectionStateChange')(deprecated)

on(type: 'BLEConnectionStateChange', callback: Callback<BLEConnectChangedState>): void

client端订阅蓝牙低功耗设备的连接状态变化事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/qRbMXYgIQMiY-AQ-wowvkg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=B853E773F5D2E7EC0B31E51CA3BDFE265C48443C2EA4DAE36B388C764275683A)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#on('BLEConnectionStateChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#onbleconnectionstatechange)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"BLEConnectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<[BLEConnectChangedState](#bleconnectchangedstatedeprecated)\> | 是 | 表示连接状态，已连接或断开。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**示例：**

```js
import { BusinessError } from '@kit.BasicServicesKit';
function ConnectStateChanged(state: bluetoothManager.BLEConnectChangedState) {
    console.info('bluetooth connect state changed');
    let connectState: bluetoothManager.ProfileConnectionState = state.state;
}
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.on('BLEConnectionStateChange', ConnectStateChanged);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]off('BLEConnectionStateChange')(deprecated)

off(type: 'BLEConnectionStateChange', callback?: Callback<BLEConnectChangedState>): void

取消订阅蓝牙低功耗设备的连接状态变化事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/4JPaCFYdTVmtS-j0F2ArKg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=AEE3B6B3818B28D02FB5CBCD52B7D8DB9137C64C97E8A01761808B1C12C8A043)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#off('BLEConnectionStateChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#offbleconnectionstatechange)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 填写"BLEConnectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<[BLEConnectChangedState](#bleconnectchangedstatedeprecated)\> | 否 | 表示取消订阅蓝牙低功耗设备的连接状态变化事件。不填该参数则取消订阅该type对应的所有回调。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.off('BLEConnectionStateChange');
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]getDeviceName(deprecated)

getDeviceName(callback: AsyncCallback<string>): void

client获取远端蓝牙低功耗设备名。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/hiKWxiWUTvyCnbCKJ93Lxg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=999F5DEF50DEE4AD7E047D9935CE224B1E05573BBAC717DEEA8F83AF86CD15A7)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#getDeviceName](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#getdevicename)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<string> | 是 | client获取对端server设备名，通过注册回调函数获取。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
// callback
try {
    let gattClient = bluetoothManager.BLE.createGattClientDevice("XX:XX:XX:XX:XX:XX");
    gattClient.connect();
    let deviceName = gattClient.getDeviceName((err, data)=> {
        console.info('device name err ' + JSON.stringify(err));
        console.info('device name' + JSON.stringify(data));
    })
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]getDeviceName(deprecated)

getDeviceName(): Promise<string>

client获取远端蓝牙低功耗设备名。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/U1o4NKdGTlaK3zGcKuAqLw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=9B222AECD078AC72EB04BFF33756BD6451F17E148BCA8B91581491151FE9C98E)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#getDeviceName](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#getdevicename-1)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | client获取对端server设备名，通过promise形式获取。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
// promise
try {
    let gattClient = bluetoothManager.BLE.createGattClientDevice("XX:XX:XX:XX:XX:XX");
    gattClient.connect();
    let deviceName = gattClient.getDeviceName().then((data) => {
        console.info('device name' + JSON.stringify(data));
    })
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]getRssiValue(deprecated)

getRssiValue(callback: AsyncCallback<number>): void

client获取远端蓝牙低功耗设备的信号强度 (Received Signal Strength Indication, RSSI)，调用[connect](#connectdeprecated-1)接口连接成功后才能使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/e-UA8shrR8K8HgHZYUjofQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=0B0FC64DF59E15E8C9B870B2FF2593DF17C8BE97E4D0B2DB088FDFF9AE4CE5EF)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#getRssiValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#getrssivalue)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | 是 | 返回信号强度，单位 dBm，通过注册回调函数获取。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
// callback
try {
    let gattClient = bluetoothManager.BLE.createGattClientDevice("XX:XX:XX:XX:XX:XX");
    gattClient.connect();
    let rssi = gattClient.getRssiValue((err: BusinessError, data: number)=> {
        console.info('rssi err ' + JSON.stringify(err));
        console.info('rssi value' + JSON.stringify(data));
    })
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### \[h2\]getRssiValue(deprecated)

getRssiValue(): Promise<number>

client获取远端蓝牙低功耗设备的信号强度 (Received Signal Strength Indication, RSSI)，调用[connect](#connectdeprecated-1)接口连接成功后才能使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/qscjWHBURpKGS7fczPWHEQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=3B4481A4B671AAB21F9A8931035790C7A22FAF5E9D4631C483B3047E7CF84C19)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#getRssiValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#getrssivalue-1)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | 返回信号强度，单位 dBm，通过promise形式获取。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bluetoothmanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```js
import { BusinessError } from '@ohos.base';
// promise
try {
    let gattClient = bluetoothManager.BLE.createGattClientDevice("XX:XX:XX:XX:XX:XX");
    let rssi = gattClient.getRssiValue().then((data: number) => {
        console.info('rssi' + JSON.stringify(data));
    })
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### ScanMode(deprecated)

枚举，扫描模式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/StndF3duToaUiqBUkMjxZg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=7D462A582778F371A869BADE918DF165A4591CB67388A6A28D4B0B9B531C1782)

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.ScanMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-connection#scanmode)替代。

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/rvJYJgcBRg69uj7bZWxclw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=207E6497D3EB9B0E7F066D20504FD9F50FE526089E9DFE0E7A08B01466B9E496)

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.BondState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-connection#bondstate)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| BOND\_STATE\_INVALID | 0 | 无效的配对。 |
| BOND\_STATE\_BONDING | 1 | 正在配对。 |
| BOND\_STATE\_BONDED | 2 | 已配对。 |

#### SppOption(deprecated)

描述spp的配置参数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/4dLe2x9LRkO9D7q9GX_EbQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=742E8AC4567A6577CD91120CF50EB91F634FE4B693A84D46631984562B76E7F9)

从API version 9开始支持，从API version 10开始废弃。建议使用[socket.SppOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-socket#sppoptions)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| uuid | string | 否 | 否 | spp单据的uuid。 |
| secure | boolean | 否 | 否 | 是否是安全通道。 |
| type | [SppType](#spptypedeprecated) | 否 | 否 | Spp链路类型。 |

#### SppType(deprecated)

枚举，Spp链路类型。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/s_iSFTaeTryFtglyYodRMw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=0A72B5E4C7442E4F458C432740D641112000AFB90289CDE646300599A86A884F)

从API version 9开始支持，从API version 10开始废弃。建议使用[socket.SppType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-socket#spptype)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| SPP\_RFCOMM | 0 | 表示rfcomm链路类型。 |

#### GattService(deprecated)

描述service的接口参数定义。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/Mvtpiq_ESkGdRXhOQC0K4w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=5130FF4B3236FDABA7975596C28E937251C00B29B0E0B553A902B647BA7A7158)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattService](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#gattservice)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| serviceUuid | string | 否 | 否 | 特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |
| isPrimary | boolean | 否 | 否 | 如果是主服务设置为true，否则设置为false。 |
| characteristics | Array<[BLECharacteristic](#blecharacteristicdeprecated)\> | 否 | 否 | 当前服务包含的特征列表。 |
| includeServices | Array<[GattService](#gattservicedeprecated)\> | 否 | 是 | 当前服务依赖的其它服务。 |

#### BLECharacteristic(deprecated)

描述characteristic的接口参数定义。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/IO8YdxJoQUSduTHVanHjrg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=ADB8423ECDB36E2DA559FF9A1F893E63B41BE4F3C7D834B28DB38A1F1B3BAEDD)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.BLECharacteristic](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#blecharacteristic)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| serviceUuid | string | 否 | 否 | 特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |
| characteristicUuid | string | 否 | 否 | 特定特征（characteristic）的UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| characteristicValue | ArrayBuffer | 否 | 否 | 特征对应的二进制值。 |
| descriptors | Array<[BLEDescriptor](#bledescriptordeprecated)\> | 否 | 否 | 特定特征的描述符列表。 |

#### BLEDescriptor(deprecated)

描述descriptor的接口参数定义。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/1LHQlAdBSVG5hinueLQN8A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=FC757081178EA2947D77EF9C0DD30EB1CE9D2CDCF2CE289227218B0612D7DB8F)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.BLEDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#bledescriptor)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| serviceUuid | string | 否 | 否 | 特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |
| characteristicUuid | string | 否 | 否 | 特定特征（characteristic）的UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| descriptorUuid | string | 否 | 否 | 描述符（descriptor）的UUID，例如：00002902-0000-1000-8000-00805f9b34fb。 |
| descriptorValue | ArrayBuffer | 否 | 否 | 描述符对应的二进制值。 |

#### NotifyCharacteristic(deprecated)

描述server端特征值变化时发送的特征通知参数定义。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/w_dyMMc0Q5i2K6e1UYT0KQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=39F69BD6F90BFADF4C7BC267683DE34880FEFFA0B44854D91F36DEA63F736349)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.NotifyCharacteristic](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#notifycharacteristic)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| serviceUuid | string | 否 | 否 | 特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |
| characteristicUuid | string | 否 | 否 | 特定特征（characteristic）的UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| characteristicValue | ArrayBuffer | 否 | 否 | 特征对应的二进制值。 |
| confirm | boolean | 否 | 否 | 如果是notification则对端回复确认设置为true，如果是indication则对端不需要回复确认设置为false。 |

#### CharacteristicReadRequest(deprecated)

描述server端订阅后收到的特征值读请求事件参数结构。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/yv9AWFN5Sky0LO1iWr1KfQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=838257140DCAFCA7E82A4BE35F7922057829C90A7277CE7B9CE0EF38A5F474D4)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.CharacteristicReadRequest](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#characteristicreadrequest)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | 否 | 否 | 表示发送特征值读请求的远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| transId | number | 否 | 否 | 表示读请求的传输ID，server端回复响应时需填写相同的传输ID。 |
| offset | number | 否 | 否 | 表示读特征值数据的起始位置。例如：k表示从第k个字节开始读，server端回复响应时需填写相同的offset。 |
| characteristicUuid | string | 否 | 否 | 特定特征（characteristic）的UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| serviceUuid | string | 否 | 否 | 特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |

#### CharacteristicWriteRequest(deprecated)

描述server端订阅后收到的特征值写请求事件参数结构。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/HcDjqk2ZSri63MGcJaO3Xw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=6714AA0F03AF2D3D823624F25014A8FA31C669EBF0B04FC63F1A17686ECA536D)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.CharacteristicWriteRequest](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#characteristicwriterequest)替代。

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

#### DescriptorReadRequest(deprecated)

描述server端订阅后收到的描述符读请求事件参数结构。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/FtEM16TjT1SK8tBhHGBFlg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=539F8387B275A44A8D399784731EF4F117AFC3D4CEA2B2F3DDFD48307CA5A3B4)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.DescriptorReadRequest](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#descriptorreadrequest)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | 否 | 否 | 表示发送描述符读请求的远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| transId | number | 否 | 否 | 表示读请求的传输ID，server端回复响应时需填写相同的传输ID。 |
| offset | number | 否 | 否 | 表示读描述符数据的起始位置。例如：k表示从第k个字节开始读，server端回复响应时需填写相同的offset。 |
| descriptorUuid | string | 否 | 否 | 表示描述符（descriptor）的UUID，例如：00002902-0000-1000-8000-00805f9b34fb。 |
| characteristicUuid | string | 否 | 否 | 特定特征（characteristic）的UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| serviceUuid | string | 否 | 否 | 特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |

#### DescriptorWriteRequest(deprecated)

描述server端订阅后收到的描述符写请求事件参数结构。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/XwSz6NBGSbegtedXKd_JEg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=7FB5F873E962FEE2B15EEC855CF4EB23A258C9F9A3714CA0AE85406914A566D2)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.DescriptorWriteRequest](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#descriptorwriterequest)替代。

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/nfuVIEl8RRKvqv1ZVH__Cw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=68088A7B65C35B60CA2C5921B54F883F3E11C0DF0A90DFA8658A0A5041B787FD)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.ServerResponse](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#serverresponse)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | 否 | 否 | 表示远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| transId | number | 否 | 否 | 表示请求的传输ID，与订阅的读/写请求事件携带的ID保持一致。 |
| status | number | 否 | 否 | 表示响应的状态，设置为0即可，表示正常。 |
| offset | number | 否 | 否 | 表示请求的读/写起始位置，与订阅的读/写请求事件携带的offset保持一致。 |
| value | ArrayBuffer | 否 | 否 | 表示回复响应的二进制数据。 |

#### BLEConnectChangedState(deprecated)

描述Gatt profile连接状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/tnGvVp9sS2eeVVC0Xocv0A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=A82375945D4FC9922F16338068A69A11F9A3366977783569E457F7B285F896F1)

从API version 9开始支持，从API version 10开始废弃。建议使用[BLEConnectionChangeState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#bleconnectionchangestate)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | 否 | 否 | 表示远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| state | [ProfileConnectionState](#profileconnectionstatedeprecated) | 否 | 否 | 表示BLE连接状态的枚举。 |

#### ProfileConnectionState(deprecated)

枚举，蓝牙设备的profile连接状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/II9TreSOTx-dMnIW_I9ceA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=A8E91FF4475802709300F473B4AEC6F9DCF33FCFD48005745D409A7B3F8FAF30)

从API version 9开始支持，从API version 10开始废弃。建议使用[constant.ProfileConnectionState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-constant#profileconnectionstate)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| STATE\_DISCONNECTED | 0 | 表示profile已断连。 |
| STATE\_CONNECTING | 1 | 表示profile正在连接。 |
| STATE\_CONNECTED | 2 | 表示profile已连接。 |
| STATE\_DISCONNECTING | 3 | 表示profile正在断连。 |

#### ScanFilter(deprecated)

扫描过滤参数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/TVpSRmbsRomdEejSUdmiAA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=29329931A384B275BC8E3BCF2C6A34EB5733048245B2CDC90B048D23A0A4227A)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.ScanFilter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#scanfilter)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | 否 | 是 | 表示过滤的BLE设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| name | string | 否 | 是 | 表示过滤的BLE设备名。 |
| serviceUuid | string | 否 | 是 | 表示过滤包含该UUID服务的设备，例如：00001888-0000-1000-8000-00805f9b34fb。 |
| serviceUuidMask | string | 否 | 是 | 表示过滤包含该UUID服务掩码的设备，例如：FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF。 |
| serviceSolicitationUuid | string | 否 | 是 | 表示过滤包含该UUID服务请求的设备，例如：00001888-0000-1000-8000-00805F9B34FB。 |
| serviceSolicitationUuidMask | string | 否 | 是 | 表示过滤包含该UUID服务请求掩码的设备，例如：FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF。 |
| serviceData | ArrayBuffer | 否 | 是 | 表示过滤包含该服务相关数据的设备，例如：\[0x90,0x00,0xF1,0xF2\]。 |
| serviceDataMask | ArrayBuffer | 否 | 是 | 表示过滤包含该服务相关数据掩码的设备，例如：\[0xFF,0xFF,0xFF,0xFF\]。 |
| manufactureId | number | 否 | 是 | 表示过滤包含该制造商ID的设备，例如：0x0006。 |
| manufactureData | ArrayBuffer | 否 | 是 | 表示过滤包含该制造商相关数据的设备，例如：\[0x1F,0x2F,0x3F\]。 |
| manufactureDataMask | ArrayBuffer | 否 | 是 | 表示过滤包含该制造商相关数据掩码的设备，例如：\[0xFF,0xFF,0xFF\]。 |

#### ScanOptions(deprecated)

扫描的配置参数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/rdPQJrT4RPSi-MJUKHld4g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=3571CFBC8D42EA593C1D1F89A4FEF27FDC6DA6A8EA21FE997CB0010017FE53A6)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.ScanOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#scanoptions)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| interval | number | 否 | 是 | 表示扫描结果上报延迟时间，默认值为0。 |
| dutyMode | [ScanDuty](#scandutydeprecated) | 否 | 是 | 表示扫描模式，默认值为SCAN\_MODE\_LOW\_POWER。 |
| matchMode | [MatchMode](#matchmodedeprecated) | 否 | 是 | 表示硬件的过滤匹配模式，默认值为MATCH\_MODE\_AGGRESSIVE。 |

#### ScanDuty(deprecated)

枚举，扫描模式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/bge9uUyOQ2SOMAfwfxFjLA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=78829CE796226A4D22AF51AA7B3C7D56927C20265F16CD3BEEB16D7C38E1FB14)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.ScanDuty](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#scanduty)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| SCAN\_MODE\_LOW\_POWER | 0 | 表示低功耗模式，默认值。 |
| SCAN\_MODE\_BALANCED | 1 | 表示均衡模式。 |
| SCAN\_MODE\_LOW\_LATENCY | 2 | 表示低延迟模式。 |

#### MatchMode(deprecated)

枚举，硬件过滤匹配模式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/fV8UpM4PTTqKSPQFK9xJVA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=AACB956728113030EE9D463B286C74D5C8FA6AD5CE9308F7BFCA9D35D6574394)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.MatchMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#matchmode)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| MATCH\_MODE\_AGGRESSIVE | 1 | 表示硬件上报扫描结果门限较低，比如扫描到的功率较低或者一段时间扫描到的次数较少也触发上报，默认值。 |
| MATCH\_MODE\_STICKY | 2 | 表示硬件上报扫描结果门限较高，更高的功率门限以及扫描到多次才会上报。 |

#### ScanResult(deprecated)

扫描结果上报数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/sS38d3zNRJWrKYvNkwCHuQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=B6E13635972DA7F7B7CCEB4EE825674CA0E9AF875FC3E9B39D86AC4795E664ED)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.ScanResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#scanresult)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | 否 | 否 | 表示扫描到的设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| rssi | number | 否 | 否 | 表示扫描到的设备的rssi值。 |
| data | ArrayBuffer | 否 | 否 | 表示扫描到的设备发送的广播包。 |

#### BluetoothState(deprecated)

枚举，蓝牙开关状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/CuCTGXzlSQiL6ASLVR1dCQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=EB632B4C648123D45704E20C43225098817025F0BDD6114CA3DEB501260524D2)

从API version 9开始支持，从API version 10开始废弃。建议使用[access.BluetoothState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-access#bluetoothstate)替代。

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/Vg5sU5cxTw6_O7RlTjD-EQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=E29FD2941DB1EBEF29A96E90414A297DCA2E44CBEAB53349CB821C499290E595)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.AdvertiseSetting](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#advertisesetting)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| interval | number | 否 | 是 | 表示广播间隔，最小值设置32个slot表示20ms，最大值设置16384个slot，默认值设置为1600个slot表示1s。 |
| txPower | number | 否 | 是 | 表示发送功率，最小值设置-127，最大值设置1，默认值设置-7，单位dbm。 |
| connectable | boolean | 否 | 是 | 表示是否是可连接广播，默认值设置为true。 |

#### AdvertiseData(deprecated)

描述BLE广播数据包的内容。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/fLHf8fLkT6GE7jNDhOzkNw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=586AD2B1AA50AD1E9BA37230E5E14BEF58325B3EBA2C2DC2E163A098E05EAAEC)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.AdvertiseData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#advertisedata)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| serviceUuids | Array<string> | 否 | 否 | 表示要广播的服务 UUID 列表。 |
| manufactureData | Array<[ManufactureData](#manufacturedatadeprecated)\> | 否 | 否 | 表示要广播的广播的制造商信息列表。 |
| serviceData | Array<[ServiceData](#servicedatadeprecated)\> | 否 | 否 | 表示要广播的服务数据列表。 |

#### ManufactureData(deprecated)

描述BLE广播数据包的内容。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/q3EVqnNyTxahtVniN2WJAQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=378C4FBDBCB52864C1148D1A66807C17E7EBC48BE19D033894F494F887A1362D)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.ManufactureData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#manufacturedata)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| manufactureId | number | 否 | 否 | 表示制造商的ID，由蓝牙SIG分配。 |
| manufactureValue | ArrayBuffer | 否 | 否 | 表示制造商发送的制造商数据。 |

#### ServiceData(deprecated)

描述广播包中服务数据内容。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/ZnlYmSxKR96lCsJ-PcQ33w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=397210497023CD00FC1F25F4612EF1653931D661904409F43DB64EB53317AA66)

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.ServiceData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble#servicedata)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| serviceUuid | string | 否 | 否 | 表示服务的UUID。 |
| serviceValue | ArrayBuffer | 否 | 否 | 表示服务数据。 |

#### PinRequiredParam(deprecated)

描述配对请求参数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/rabeFOelS9S4NsrW1AR-fg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=D27AB29F2FAD452C6681EAE7A8EC54F16F511E193C15753BD6391C35CF70DE6C)

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.PinRequiredParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-connection#pinrequiredparam)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | 否 | 否 | 表示要配对的设备ID。 |
| pinCode | string | 否 | 否 | 表示要配对的密钥。 |

#### BondStateParam(deprecated)

描述配对状态参数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/Z_XIxTTiTE2x7Jsr1aA1lA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=D7239277943B3F5D72010EAF16610C41DF473E36CE39E6D3049C600B03472A7C)

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.BondStateParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-connection#bondstateparam)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | 否 | 否 | 表示要配对的设备ID。 |
| state | BondState | 否 | 否 | 表示配对设备的状态。 |

#### StateChangeParam(deprecated)

描述profile状态改变参数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/T-Gsp9TVS4mthMDiBnl-eg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=68E4E39611631AD39C28EA0BCE8B8BE442BB8F0B63F5BED963B848D5CE9AE721)

从API version 9开始支持，从API version 10开始废弃。建议使用[baseProfile.StateChangeParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-baseprofile#statechangeparam)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | 否 | 否 | 表示蓝牙设备地址。 |
| state | [ProfileConnectionState](#profileconnectionstatedeprecated) | 否 | 否 | 表示蓝牙设备的profile连接状态。 |

#### DeviceClass(deprecated)

描述蓝牙设备的类别。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/uNbzbAN4Rbe56caX4vuA4g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=931C0DCF08B6A4C3854BE7B8E92B6535AE64010841FBE44F61082DA37874B862)

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.DeviceClass](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-connection#deviceclass)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| majorClass | [MajorClass](#majorclassdeprecated) | 否 | 否 | 表示蓝牙设备主要类别的枚举。 |
| majorMinorClass | [MajorMinorClass](#majorminorclassdeprecated) | 否 | 否 | 表示主要次要蓝牙设备类别的枚举。 |
| classOfDevice | number | 否 | 否 | 表示设备类别。 |

#### MajorClass(deprecated)

枚举，蓝牙设备主要类别。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/BcRSYyLgR7SDjXqVJRJfyw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=621B5CC1A97D00B025983794DA9CED9E9FB01BCE73D2CFFDFC8E1B371AA0A918)

从API version 9开始支持，从API version 10开始废弃。建议使用[constant.MajorClass](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-constant#majorclass)替代。

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/1EgMkDQkSXyUcdcfnVtNag/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=B002B51551ECA477A44AF0B2FAAED43743E028125A60D3F4C2EF0BF3A9A6D096)

从API version 9开始支持，从API version 10开始废弃。建议使用[constant.MajorMinorClass](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-constant#majorminorclass)替代。

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
| HEALTH\_PEAK\_FLOW\_MONITOR | 0x0928 | 表示湿度计健康设备。 |
| HEALTH\_MEDICATION\_MONITOR | 0x092C | 表示药物监视仪健康设备。 |
| HEALTH\_KNEE\_PROSTHESIS | 0x0930 | 表示膝盖假肢健康设备。 |
| HEALTH\_ANKLE\_PROSTHESIS | 0x0934 | 表示脚踝假肢健康设备。 |
| HEALTH\_GENERIC\_HEALTH\_MANAGER | 0x0938 | 表示通用健康管理设备。 |
| HEALTH\_PERSONAL\_MOBILITY\_DEVICE | 0x093C | 表示个人移动健康设备。 |

#### PlayingState(deprecated)

枚举，蓝牙A2DP 播放状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/FoRQFnjiTNm5X9m1ISlpMQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=B2D4E92D022788A27AF04C49DA048811CAC9B1F07A6783324901E2D7F4E0CAEE)

从API version 9开始支持，从API version 10开始废弃。建议使用[a2dp.PlayingState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-a2dp#playingstate)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| STATE\_NOT\_PLAYING | 0x0000 | 表示未播放。 |
| STATE\_PLAYING | 0x0001 | 表示正在播放。 |

#### ProfileId(deprecated)

蓝牙profile枚举，API9新增PROFILE\_HID\_HOST，PROFILE\_PAN\_NETWORK。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/n2GTLrviTd6us_vxKJ5ngw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=026F5A17FE887D36479205CE305D57D3520C2B7C98CA47EEE7853DEC9B57572C)

从API version 9开始支持，从API version 10开始废弃。建议使用[constant.ProfileId](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-constant#profileid)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| PROFILE\_A2DP\_SOURCE | 1 | 表示A2DP profile。 |
| PROFILE\_HANDS\_FREE\_AUDIO\_GATEWAY | 4 | 表示HFP profile。 |
| PROFILE\_HID\_HOST | 6 | 表示HID profile。 |
| PROFILE\_PAN\_NETWORK | 7 | 表示PAN profile。 |

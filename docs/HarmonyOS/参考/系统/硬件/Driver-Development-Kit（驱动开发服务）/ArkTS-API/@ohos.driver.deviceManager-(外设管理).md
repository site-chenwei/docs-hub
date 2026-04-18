---
title: "@ohos.driver.deviceManager (外设管理)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-driver-devicemanager"
menu_path:
  - "参考"
  - "系统"
  - "硬件"
  - "Driver Development Kit（驱动开发服务）"
  - "ArkTS API"
  - "@ohos.driver.deviceManager (外设管理)"
captured_at: "2026-04-17T01:48:32.362Z"
---

# @ohos.driver.deviceManager (外设管理)

本模块主要提供管理外部设备的相关功能，包括查询设备列表、绑定设备和解除绑定设备。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/y9eRhnlEQHW5YdRWhLqltA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014833Z&HW-CC-Expire=86400&HW-CC-Sign=98293659FA51F38BF4DE86490D0105EE337AFF7A110944B2BB5301BDD9DC8AF9)

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import { deviceManager } from '@kit.DriverDevelopmentKit';
```

#### deviceManager.queryDevices

queryDevices(busType?: number): Array<Readonly<Device>>

获取接入主设备的外部设备列表。如果没有设备接入，那么将会返回一个空的列表。

**需要权限：** ohos.permission.ACCESS\_EXTENSIONAL\_DEVICE\_DRIVER

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| busType | number | 否 | 由[BusType](#bustype)约定的设备总线类型，不填则查找所有类型设备。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Array<Readonly<[Device](#device)\>> | 设备信息列表。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[驱动错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-devicemanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | The permission check failed. |
| 22900001 | ExternalDeviceManager service exception or busType parameter error. |

**示例：**

```ts
import { deviceManager } from '@kit.DriverDevelopmentKit';

try {
  let devices : Array<deviceManager.Device> = deviceManager.queryDevices(deviceManager.BusType.USB);
  for (let item of devices) {
    let device : deviceManager.USBDevice = item as deviceManager.USBDevice;
    console.info(`Device id is ${device.deviceId}`);
  }
} catch (error) {
  console.error(`Failed to query device. Code is ${error.code}, message is ${error.message}`);
}
```

#### deviceManager.bindDriverWithDeviceId19+

bindDriverWithDeviceId(deviceId: number, onDisconnect: AsyncCallback<number>): Promise<RemoteDeviceDriver>

根据queryDevices()返回的设备信息绑定设备。使用Promise异步回调。

需要调用[deviceManager.queryDevices](#devicemanagerquerydevices)获取设备信息列表。

**需要权限：** ohos.permission.ACCESS\_DDK\_DRIVERS

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| deviceId | number | 是 | 设备ID，通过queryDevices获得。 |
| onDisconnect | AsyncCallback<number> | 是 | 回调函数。当绑定设备断开时，err为undefined，data为解绑的设备ID；否则为错误对象。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[RemoteDeviceDriver](#remotedevicedriver11)\> | Promise对象，返回RemoteDeviceDriver对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[驱动错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-devicemanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | The permission check failed. |
| 26300001 | ExternalDeviceManager service exception. |
| 26300002 | The driver service does not allow any client to bind. |

**示例：**

```ts
import { deviceManager } from '@kit.DriverDevelopmentKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 12345678为示例deviceId，应用开发时可通过queryDevices查询到相应设备的deviceId作为入参
  deviceManager.bindDriverWithDeviceId(12345678, (error : BusinessError, data : number) => {
    console.error(`Device is disconnected`);
  }).then((data: deviceManager.RemoteDeviceDriver) => {
    console.info(`bindDriverWithDeviceId success, Device_Id is ${data.deviceId}.
    remote is ${data.remote != null ? data.remote.getDescriptor() : "null"}`);
  }, (error: BusinessError) => {
    console.error(`bindDriverWithDeviceId async fail. Code is ${error.code}, message is ${error.message}`);
  });
} catch (error) {
  console.error(`bindDriverWithDeviceId fail. Code is ${error.code}, message is ${error.message}`);
}
```

#### deviceManager.unbindDriverWithDeviceId19+

unbindDriverWithDeviceId(deviceId: number): Promise<number>

解除设备绑定。使用Promise异步回调。

**需要权限**：ohos.permission.ACCESS\_DDK\_DRIVERS

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| deviceId | number | 是 | 设备ID，通过[queryDevices](#devicemanagerquerydevices)获得。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | Promise对象，返回解除绑定的设备ID。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[驱动错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-devicemanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | The permission check failed. |
| 26300001 | ExternalDeviceManager service exception. |
| 26300003 | There is no binding relationship. |

**示例：**

```ts
import { deviceManager } from '@kit.DriverDevelopmentKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 12345678为示例deviceId，应用开发时可通过queryDevices查询到相应设备的deviceId作为入参
  deviceManager.unbindDriverWithDeviceId(12345678).then((data : number) => {
    console.info(`unbindDriverWithDeviceId success, Device_Id is ${data}.`);
  }, (error : BusinessError) => {
    console.error(`unbindDriverWithDeviceId async fail. Code is ${error.code}, message is ${error.message}`);
  });
} catch (error) {
  console.error(`unbindDriverWithDeviceId fail. Code is ${error.code}, message is ${error.message}`);
}
```

#### deviceManager.bindDevice(deprecated)

bindDevice(deviceId: number, onDisconnect: AsyncCallback<number>, callback: AsyncCallback<{deviceId: number; remote: rpc.IRemoteObject;}>): void

根据queryDevices()返回的设备信息绑定设备。

需要调用[deviceManager.queryDevices()](#devicemanagerquerydevices)获取设备信息以及device。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/5n5Si_gxTreWZUlSSHtGEw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014833Z&HW-CC-Expire=86400&HW-CC-Sign=31E45DEDA0006D5B79C2E73D8D7C3FAAB9265866BCBACB9CCA22516A7BA55201)

从 API version 10开始支持，从API version 19开始废弃。建议使用[deviceManager.bindDriverWithDeviceId](#devicemanagerbinddriverwithdeviceid19)替代。

**需要权限：** ohos.permission.ACCESS\_EXTENSIONAL\_DEVICE\_DRIVER

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| deviceId | number | 是 | 设备ID，通过queryDevices获得。 |
| onDisconnect | AsyncCallback<number> | 是 | 回调函数。当绑定设备断开时，err为undefined，data为解绑的设备ID；否则为错误对象。 |
| callback | AsyncCallback<{deviceId: number; remote: [rpc.IRemoteObject](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-rpc#iremoteobject);}> | 是 | 回调函数。当绑定设备成功时，err为undefined，data包含设备ID和绑定设备驱动通信对象；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[驱动错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-devicemanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | The permission check failed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 22900001 | ExternalDeviceManager service exception. |

**示例：**

```ts
import { deviceManager } from '@kit.DriverDevelopmentKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { rpc } from '@kit.IPCKit';

interface DataType {
  deviceId : number;
  remote : rpc.IRemoteObject;
}

try {
  // 12345678为示例deviceId，应用开发时可通过queryDevices查询到相应设备的deviceId作为入参
  deviceManager.bindDevice(12345678, (error : BusinessError, data : number) => {
    console.error(`Device is disconnected`);
  }, (error : BusinessError, data : DataType) => {
    if (error) {
      console.error(`bindDevice async fail. Code is ${error.code}, message is ${error.message}`);
      return;
    }
    console.info(`bindDevice success`);
  });
} catch (error) {
  console.error(`bindDevice fail. Code is ${error.code}, message is ${error.message}`);
}
```

#### deviceManager.bindDeviceDriver(deprecated)

bindDeviceDriver(deviceId: number, onDisconnect: AsyncCallback<number>, callback: AsyncCallback<RemoteDeviceDriver>): void

根据queryDevices()返回的设备信息绑定设备。

需要调用[deviceManager.queryDevices()](#devicemanagerquerydevices)获取设备信息以及device。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/Kr6B6_wqRHifJ5TjxahSeg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014833Z&HW-CC-Expire=86400&HW-CC-Sign=2253B4D6EB50A1354147288D51754F5B3A797ED389F8CE1208A9BE43B6696C9E)

从 API version 11开始支持，从API version 19开始废弃。建议使用[deviceManager.bindDriverWithDeviceId](#devicemanagerbinddriverwithdeviceid19)替代。

**需要权限：** ohos.permission.ACCESS\_EXTENSIONAL\_DEVICE\_DRIVER

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| deviceId | number | 是 | 设备ID，通过queryDevices获得。 |
| onDisconnect | AsyncCallback<number> | 是 | 回调函数。当绑定设备断开时，err为undefined，data为解绑的设备ID；否则为错误对象。 |
| callback | AsyncCallback<[RemoteDeviceDriver](#remotedevicedriver11)\> | 是 | 回调函数。当绑定设备驱动成功时，err为undefined，data为包括设备ID和远程对象的[RemoteDeviceDriver](#remotedevicedriver11)对象；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[驱动错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-devicemanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | The permission check failed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 22900001 | ExternalDeviceManager service exception. |

**示例：**

```ts
import { deviceManager } from '@kit.DriverDevelopmentKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 12345678为示例deviceId，应用开发时可通过queryDevices查询到相应设备的deviceId作为入参
  deviceManager.bindDeviceDriver(12345678, (error : BusinessError, data : number) => {
    console.error(`Device is disconnected`);
  }, (error : BusinessError, data : deviceManager.RemoteDeviceDriver) => {
    if (error) {
      console.error(`bindDeviceDriver async fail. Code is ${error.code}, message is ${error.message}`);
      return;
    }
    console.info(`bindDeviceDriver success`);
  });
} catch (error) {
  console.error(`bindDeviceDriver fail. Code is ${error.code}, message is ${error.message}`);
}
```

#### deviceManager.bindDevice(deprecated)

bindDevice(deviceId: number, onDisconnect: AsyncCallback<number>): Promise<{deviceId: number; remote: rpc.IRemoteObject;}>;

根据queryDevices()返回的设备信息绑定设备。

需要调用[deviceManager.queryDevices](#devicemanagerquerydevices)获取设备信息以及device。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/QSt8p7xJTfiHx99DrN01ZA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014833Z&HW-CC-Expire=86400&HW-CC-Sign=79DB4CA5B930073B6C8716DFD8A263B8CC3E15089398D5D9A8B271B8F48D8E89)

从 API version 10开始支持，从API version 19开始废弃。建议使用[deviceManager.bindDriverWithDeviceId](#devicemanagerbinddriverwithdeviceid19)替代。

**需要权限：** ohos.permission.ACCESS\_EXTENSIONAL\_DEVICE\_DRIVER

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| deviceId | number | 是 | 设备ID，通过queryDevices获得。 |
| onDisconnect | AsyncCallback<number> | 是 | 回调函数。当绑定设备断开时，err为undefined，data为解绑的设备ID；否则为错误对象。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<{deviceId: number; remote: [rpc.IRemoteObject](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-rpc#iremoteobject);}> | Promise对象，返回一个包含设备ID和IRemoteObject的对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[驱动错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-devicemanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | The permission check failed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 22900001 | ExternalDeviceManager service exception. |

**示例：**

```ts
import { deviceManager } from '@kit.DriverDevelopmentKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 12345678为示例deviceId，应用开发时可通过queryDevices查询到相应设备的deviceId作为入参
  deviceManager.bindDevice(12345678, (error : BusinessError, data : number) => {
    console.error(`Device is disconnected`);
  }).then(data => {
    console.info(`bindDevice success, Device_Id is ${data.deviceId}.
    remote is ${data.remote != null ? data.remote.getDescriptor() : "null"}`);
  }, (error: BusinessError) => {
    console.error(`bindDevice async fail. Code is ${error.code}, message is ${error.message}`);
  });
} catch (error) {
  console.error(`bindDevice fail. Code is ${error.code}, message is ${error.message}`);
}
```

#### deviceManager.bindDeviceDriver(deprecated)

bindDeviceDriver(deviceId: number, onDisconnect: AsyncCallback<number>): Promise<RemoteDeviceDriver>;

根据queryDevices()返回的设备信息绑定设备。

需要调用[deviceManager.queryDevices](#devicemanagerquerydevices)获取设备信息以及device。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/KesDgRcUQPucUJTGdzQSjQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014833Z&HW-CC-Expire=86400&HW-CC-Sign=0B8B0F864DC05C56B3ADE7F179B61A96E956D625E4CDFFFF188CE9239B034C89)

从 API version 11开始支持，从API version 19开始废弃。建议使用[deviceManager.bindDriverWithDeviceId](#devicemanagerbinddriverwithdeviceid19)替代。

**需要权限：** ohos.permission.ACCESS\_EXTENSIONAL\_DEVICE\_DRIVER

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| deviceId | number | 是 | 设备ID，通过queryDevices获得。 |
| onDisconnect | AsyncCallback<number> | 是 | 回调函数。当绑定设备断开时，err为undefined，data为解绑的设备ID；否则为错误对象。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[RemoteDeviceDriver](#remotedevicedriver11)\> | Promise对象，返回RemoteDeviceDriver对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[驱动错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-devicemanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | The permission check failed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 22900001 | ExternalDeviceManager service exception. |

**示例：**

```ts
import { deviceManager } from '@kit.DriverDevelopmentKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 12345678为示例deviceId，应用开发时可通过queryDevices查询到相应设备的deviceId作为入参
  deviceManager.bindDeviceDriver(12345678, (error : BusinessError, data : number) => {
    console.error(`Device is disconnected`);
  }).then((data: deviceManager.RemoteDeviceDriver) => {
    console.info(`bindDeviceDriver success, Device_Id is ${data.deviceId}.
    remote is ${data.remote != null ? data.remote.getDescriptor() : "null"}`);
  }, (error: BusinessError) => {
    console.error(`bindDeviceDriver async fail. Code is ${error.code}, message is ${error.message}`);
  });
} catch (error) {
  console.error(`bindDeviceDriver fail. Code is ${error.code}, message is ${error.message}`);
}
```

#### deviceManager.unbindDevice(deprecated)

unbindDevice(deviceId: number, callback: AsyncCallback<number>): void

解除设备绑定。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/lmaZ3bX-RJKI18y-Ggi18w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014833Z&HW-CC-Expire=86400&HW-CC-Sign=0BD254DA4BE560B9C388D8FEFEEA39295FA78B8B162DE166F5EA759C548637DC)

从 API version 10开始支持，从API version 19开始废弃。建议使用[deviceManager.unbindDriverWithDeviceId](#devicemanagerunbinddriverwithdeviceid19)替代。

**需要权限**：ohos.permission.ACCESS\_EXTENSIONAL\_DEVICE\_DRIVER

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| deviceId | number | 是 | 设备ID，通过queryDevices获得。 |
| callback | AsyncCallback<number> | 是 | 回调函数。当解绑设备成功时，err为undefined，data为设备ID；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[驱动错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-devicemanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | The permission check failed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 22900001 | ExternalDeviceManager service exception. |

**示例：**

```ts
import { deviceManager } from '@kit.DriverDevelopmentKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 12345678为示例deviceId，应用开发时可通过queryDevices查询到相应设备的deviceId作为入参
  deviceManager.unbindDevice(12345678, (error : BusinessError, data : number) => {
    if (error) {
      console.error(`unbindDevice async fail. Code is ${error.code}, message is ${error.message}`);
      return;
    }
    console.info(`unbindDevice success`);
  });
} catch (error) {
  console.error(`unbindDevice fail. Code is ${error.code}, message is ${error.message}`);
}
```

#### deviceManager.unbindDevice(deprecated)

unbindDevice(deviceId: number): Promise<number>

解除设备绑定。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/gufr_vxPQaiwcI4ltdvwIg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014833Z&HW-CC-Expire=86400&HW-CC-Sign=34B1278244698FACA201E1B4250A4D406369A8F8A25EA59D6758985FF8DC5B61)

从 API version 10开始支持，从API version 19开始废弃。建议使用[deviceManager.unbindDriverWithDeviceId](#devicemanagerunbinddriverwithdeviceid19)替代。

**需要权限**：ohos.permission.ACCESS\_EXTENSIONAL\_DEVICE\_DRIVER

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| deviceId | number | 是 | 设备ID，通过queryDevices获得。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[驱动错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-devicemanager)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | The permission check failed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 22900001 | ExternalDeviceManager service exception. |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | Promise对象，返回解除绑定的设备ID。 |

**示例：**

```ts
import { deviceManager } from '@kit.DriverDevelopmentKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 12345678为示例deviceId，应用开发时可通过queryDevices查询到相应设备的deviceId作为入参
  deviceManager.unbindDevice(12345678).then((data : number) => {
    console.info(`unbindDevice success, Device_Id is ${data}.`);
  }, (error : BusinessError) => {
    console.error(`unbindDevice async fail. Code is ${error.code}, message is ${error.message}`);
  });
} catch (error) {
  console.error(`unbindDevice fail. Code is ${error.code}, message is ${error.message}`);
}
```

#### Device

外设信息。

**系统能力：** SystemCapability.Driver.ExternalDevice

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| busType | [BusType](#bustype) | 否 | 否 | 总线类型。 |
| deviceId | number | 否 | 否 | 设备ID。 |
| description | string | 否 | 否 | 设备描述。 |

#### USBDevice

USB设备信息，继承自[Device](#device)。

**系统能力：** SystemCapability.Driver.ExternalDevice

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| vendorId | number | 否 | 否 | USB设备Vendor ID。 |
| productId | number | 否 | 否 | USB设备Product ID。 |

#### BusType

设备总线类型。

**系统能力：** SystemCapability.Driver.ExternalDevice

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| USB | 1 | USB总线类型。 |

#### RemoteDeviceDriver11+

远程设备驱动。

**系统能力：** SystemCapability.Driver.ExternalDevice

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| deviceId11+ | number | 否 | 否 | 设备ID。 |
| remote11+ | [rpc.IRemoteObject](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-rpc#iremoteobject) | 否 | 否 | 远程驱动程序对象。 |

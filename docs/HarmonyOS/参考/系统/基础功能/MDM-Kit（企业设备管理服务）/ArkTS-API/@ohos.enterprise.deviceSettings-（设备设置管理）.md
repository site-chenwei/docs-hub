---
title: "@ohos.enterprise.deviceSettings （设备设置管理）"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-devicesettings"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "MDM Kit（企业设备管理服务）"
  - "ArkTS API"
  - "@ohos.enterprise.deviceSettings （设备设置管理）"
captured_at: "2026-04-17T01:48:31.788Z"
---

# @ohos.enterprise.deviceSettings （设备设置管理）

本模块提供企业设备设置能力，包括设置、获取设备息屏时间等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/4yWSTNnjTXWFVOzkNoM39A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014833Z&HW-CC-Expire=86400&HW-CC-Sign=99E0895120657B1F691EEE83D40FA4DB9C06B78D4BC5CE8EF5DC64A1E4287F86)

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-guide)。

#### 导入模块

```ts
import { deviceSettings } from '@kit.MDMKit';
```

#### deviceSettings.setValue

setValue(admin: Want, item: string, value: string): void

设置设备策略。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SETTINGS

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [配置](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-multi-mdm#规则3配置)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| admin | [Want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-want) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| item | string | 是 | 
设备设置策略类型。

\- screenOff：设备息屏策略，对于PC/2in1设备，仅支持设置电池供电下的息屏策略。

\- dateTime：设置系统时间。

\- powerPolicy：设备电源策略，对于PC/2in1设备，仅支持设置电池供电下的电源策略。

\- eyeComfort：从API version 23开始支持，设置护眼模式开关状态，仅支持全天开启和关闭护眼模式。

\- defaultInputMethod：从API version 23开始支持，设置默认输入法。

 |
| value | string | 是 | 

策略类型值。

当item为screenOff时，value为设备息屏时间（单位：毫秒）。

当item为dateTime时，value为要设置的系统时间（单位：毫秒）。

当item为powerPolicy时，value为JSON字符串，格式：{"powerScene":xx,"powerPolicy":{"powerPolicyAction":xx,"delayTime":xx}}。powerScene为电源策略场景；delayTime为延迟时间（单位：毫秒），不支持设置为30000毫秒；powerPolicyAction为休眠策略。

电源策略场景：

\- 0：超时场景。

休眠策略：

\- 0：不执行动作。

\- 1：自动进入睡眠。

\- 2：强制进入睡眠。

\- 3：进入休眠，该策略暂不生效。

\- 4：关机。

当item为eyeComfort时，value为护眼模式开关状态的字符串。

\- on：全天开启护眼模式。

\- off：关闭护眼模式。

当item为defaultInputMethod时，value为输入法应用包名字符串。

\- 可以通过[getCurrentInputMethod](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod#inputmethodgetcurrentinputmethod9)获取当前输入法应用包名。

 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-enterprisedevicemanager)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { deviceSettings } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 需根据实际情况进行替换
  deviceSettings.setValue(wantTemp, 'screenOff', '3000');
  console.info(`Succeeded in setting screen off time.`);
} catch (err) {
  console.error(`Failed to set screen off time. Code: ${err.code}, message: ${err.message}`);
}
```

#### deviceSettings.getValue

getValue(admin: Want, item: string): string

获取设备设置策略。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SETTINGS

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| admin | [Want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-want) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| item | string | 是 | 
设备设置策略类型。

\- screenOff：设备息屏策略，对于PC/2in1设备，仅支持查询电池供电下的息屏策略。

\- powerPolicy：设备电源策略，对于PC/2in1设备，仅支持查询电池供电下的电源策略。

\- eyeComfort：从API version 23开始支持，护眼模式开关状态。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 
策略类型值。

当item为screenOff时，返回设备息屏时间（单位：毫秒），对于PC/2in1设备，返回设备电池供电下的息屏时间（单位：毫秒）。

当item为powerPolicy时，返回电源策略，对于PC/2in1设备，返回设备电池供电下的电源策略，格式为JSON字符串:{"powerScene":xx,"powerPolicy":{"powerPolicyAction":xx,"delayTime":xx}}。powerScene为电源策略场景；delayTime为延迟时间（单位：毫秒）；powerPolicyAction为休眠策略。

电源策略场景：

\- 0：超时场景。

休眠策略：

\- 0：不执行动作。

\- 1：自动进入睡眠。

\- 2：强制进入睡眠。

\- 3：进入休眠，该策略暂不生效。

\- 4：关机。

当item为eyeComfort时，value为护眼模式开关状态的字符串。

\- on：全天开启护眼模式。

\- off：关闭护眼模式。

\- unknown：其他模式。

 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-enterprisedevicemanager)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { deviceSettings } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 参数需根据实际情况进行替换
  let result: string = deviceSettings.getValue(wantTemp, 'screenOff');
  console.info(`Succeeded in getting screen off time, result : ${result}`);
} catch (err) {
  console.error(`Failed to get screen off time. Code: ${err.code}, message: ${err.message}`);
}
```

#### deviceSettings.setHomeWallpaper20+

setHomeWallpaper(admin: Want, fd: number): Promise<void>

设置桌面壁纸，使用Promise异步回调。

**需要权限：** ohos.permission.ENTERPRISE\_SET\_WALLPAPER

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**冲突规则：** [配置](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-multi-mdm#规则3配置)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| admin | [Want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-want) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| fd | number | 是 | 需要设置为桌面壁纸图片的文件描述符，可以通过file.fs的[openSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileioopensync)接口获取应用沙箱目录下的图片文件描述符。壁纸图片大小不能超过100MB。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。当设置桌面壁纸失败后会抛出错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-enterprisedevicemanager)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ts
import { deviceSettings } from '@kit.MDMKit';
import { common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs }  from '@kit.CoreFileKit';

let wantTemp: Want = {
  // 请根据实际情况修改
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
// 参数根据实际情况进行替换
let filename: string = "homewallpaper.jpg";
let filePath: string = context.filesDir + '/' + filename;
let fd: number = fs.openSync(filePath, fs.OpenMode.READ_WRITE).fd;
deviceSettings.setHomeWallpaper(wantTemp, fd).then(() => {
  console.info('Succeeded in setting home wallpaper');
}).catch((err: BusinessError) => {
  console.error(`Failed to set home wallpaper. Code: ${err.code}, message: ${err.message}`);
}).finally(() => {
  fs.closeSync(fd);
});
```

#### deviceSettings.setUnlockWallpaper20+

setUnlockWallpaper(admin: Want, fd: number): Promise<void>

设置锁屏壁纸，使用Promise异步回调。

**需要权限：** ohos.permission.ENTERPRISE\_SET\_WALLPAPER

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**冲突规则：** [配置](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-multi-mdm#规则3配置)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| admin | [Want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-want) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| fd | number | 是 | 需要设置为锁屏壁纸图片的文件描述符，可以通过file.fs的[openSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs#fileioopensync)接口获取应用沙箱目录下的图片文件描述符。壁纸图片大小不能超过100MB。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。当设置锁屏壁纸失败后会抛出错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-enterprisedevicemanager)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ts
import { deviceSettings } from '@kit.MDMKit';
import { common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs }  from '@kit.CoreFileKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
// 参数根据实际情况进行替换
let filename: string = "lockwallpaper.jpg";
let filePath: string = context.filesDir + '/' + filename;
let fd: number = fs.openSync(filePath, fs.OpenMode.READ_WRITE).fd;
deviceSettings.setUnlockWallpaper(wantTemp, fd).then(() => {
  console.info('Succeeded in setting lock wallpaper');
}).catch((err: BusinessError) => {
  console.error(`Failed to set lock wallpaper. Code: ${err.code}, message: ${err.message}`);
});
```

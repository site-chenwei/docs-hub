---
title: "@ohos.enterprise.locationManager（位置服务管理）"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-locationmanager"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "MDM Kit（企业设备管理服务）"
  - "ArkTS API"
  - "@ohos.enterprise.locationManager（位置服务管理）"
captured_at: "2026-04-17T01:48:31.792Z"
---

# @ohos.enterprise.locationManager（位置服务管理）

本模块提供设备位置服务策略管理的能力，包括设置和查询位置服务开关策略等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/NVN6zv7hR96e8B-Z2QEh8A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014833Z&HW-CC-Expire=86400&HW-CC-Sign=7DCA5BAD87633F0699A40B19634A0BE6385904C6D316435466F4BA4DD1C78BD9)

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-guide)。

#### 导入模块

```ts
import { locationManager } from '@kit.MDMKit';
```

#### locationManager.setLocationPolicy

setLocationPolicy(admin: Want, policy: LocationPolicy): void

设置位置服务管理策略。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_LOCATION

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [独占](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-multi-mdm#规则2独占)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| admin | [Want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-want) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| policy | [LocationPolicy](#locationpolicy) | 是 | 
位置服务策略。

\- 0：默认策略。

\- 1：禁用。

\- 2：强制启用。

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
import { locationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
    locationManager.setLocationPolicy(wantTemp, locationManager.LocationPolicy.DISALLOW_LOCATION_SERVICE);
    console.info(`Succeeded in setting location patch tag.`);
} catch(err) {
    console.error(`Failed to get location patch tag. Code: ${err.code}, message: ${err.message}`);
}
```

#### locationManager.getLocationPolicy

getLocationPolicy(admin: Want): LocationPolicy

查询位置服务管理策略。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_LOCATION

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| admin | [Want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-want) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [LocationPolicy](#locationpolicy) | 位置服务策略枚举值。0：默认策略。1：禁用。2：强制启用。 |

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
import { locationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
    let result: locationManager.LocationPolicy = locationManager.getLocationPolicy(wantTemp);
    console.info(`Succeeded in getting location policy. policy: ${result}`);
} catch(err) {
    console.error(`Failed to get location policy. Code: ${err.code}, message: ${err.message}`);
}
```

#### LocationPolicy

位置服务策略值。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| DEFAULT\_LOCATION\_SERVICE | 0 | 默认策略。 |
| DISALLOW\_LOCATION\_SERVICE | 1 | 禁用位置服务策略。 |
| FORCE\_OPEN\_LOCATION\_SERVICE | 2 | 强制开启位置服务策略。 |

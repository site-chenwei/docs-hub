---
title: "@ohos.enterprise.common（Enterprise公共模块）"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-common"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "MDM Kit（企业设备管理服务）"
  - "ArkTS API"
  - "@ohos.enterprise.common（Enterprise公共模块）"
captured_at: "2026-04-17T01:48:31.664Z"
---

# @ohos.enterprise.common（Enterprise公共模块）

本模块提供MDM Kit中常用公共能力的纯类型定义，包含枚举类型和数据结构。本模块仅导出类型声明，不包含具体实现逻辑或可执行代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/COgQK9KeQiqn1IGteQyyLA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014833Z&HW-CC-Expire=86400&HW-CC-Sign=731EE3393C556659BAFD90AA48E5B34044BF5F5AEA0AA1431CC16E7CAA4EE0DC)

本模块首批接口从API version 22开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ts
import { common } from '@kit.MDMKit';
```

#### ManagedPolicy

企业设备管控策略。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| DEFAULT | 0 | 默认，无管控策略。 |
| DISALLOW | 1 | 禁用。 |
| FORCE\_OPEN | 2 | 强制开启。 |

#### ApplicationInstance

应用的实例数据。

该接口目前在[addUserNonStopApps](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-applicationmanager#applicationmanageraddusernonstopapps22)、[removeUserNonStopApps](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-applicationmanager#applicationmanagerremoveusernonstopapps22)、[addFreezeExemptedApps](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-applicationmanager#applicationmanageraddfreezeexemptedapps22)、[removeFreezeExemptedApps](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-applicationmanager#applicationmanagerremovefreezeexemptedapps22)接口中作为入参使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| appIdentifier | string | 否 | 否 | 应用[唯一标识符](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-bundleinfo#signatureinfo)，可以通过接口[bundleManager.getBundleInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager#bundlemanagergetbundleinfo14-2)获取bundleInfo.signatureInfo.appIdentifier。 |
| accountId | number | 否 | 否 | 
用户ID。取值范围：大于等于0的整数。

accountId可以通过[getOsAccountLocalId](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-osaccount#getosaccountlocalid9-1)接口获取。

 |
| appIndex | number | 否 | 否 | 

应用分身索引。取值范围：大于等于0的整数。

appIndex可以通过[getAppCloneIdentity](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager#bundlemanagergetappcloneidentity14)接口获取。

 |

#### InstallationResult

应用安装结果。

该对象目前在[EnterpriseAdminExtensionAbility.onMarketAppInstallResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterpriseadminextensionability#onmarketappinstallresult22)作为回调入参使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| result | [Result](#result) | 否 | 否 | 应用安装结果码。 |
| message | string | 否 | 否 | 应用安装结果消息。 |

#### Result

应用安装结果码。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| SUCCESS | 0 | 应用安装成功。 |
| FAIL | \-1 | 应用安装失败。 |

#### EnterpriseAdminExtensionContext23+

type EnterpriseAdminExtensionContext = \_EnterpriseAdminExtensionContext.default

EnterpriseAdminExtensionContext是[EnterpriseAdminExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterpriseadminextensionability)的上下文环境，继承自[ExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-extensioncontext)。

**系统能力**: SystemCapability.Customization.EnterpriseDeviceManager

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| :-- | :-- |
| [\_EnterpriseAdminExtensionContext.default](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/s-apis-application-enterpriseadminextensioncontext) | EnterpriseAdminExtensionAbility组件的上下文。 |

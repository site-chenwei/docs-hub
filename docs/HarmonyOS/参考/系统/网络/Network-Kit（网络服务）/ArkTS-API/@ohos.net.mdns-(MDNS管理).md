---
title: "@ohos.net.mdns (MDNS管理)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-mdns"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Network Kit（网络服务）"
  - "ArkTS API"
  - "@ohos.net.mdns (MDNS管理)"
captured_at: "2026-04-17T01:48:22.661Z"
---

# @ohos.net.mdns (MDNS管理)

MDNS即多播DNS（Multicast DNS），提供局域网内的本地服务添加、移除、发现、解析等能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/UneFBGj7ToesMhW_rU19mw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=D56783FE12E29D600192D6C70EF3861C79334FAB874FC4AFF402DECF16C96ED6)

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import { mdns } from '@kit.NetworkKit';
```

#### mdns.addLocalService

addLocalService(context: Context, serviceInfo: LocalServiceInfo, callback: AsyncCallback<LocalServiceInfo>): void

添加一个MDNS服务，使用callback方式作为异步方法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| context | Context | 是 | 
应用的上下文。

FA模型的应用Context定义见[Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-app-context)。

Stage模型的应用Context定义见[Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)。

 |
| serviceInfo | [LocalServiceInfo](#localserviceinfo) | 是 | mDNS服务的信息。 |
| callback | AsyncCallback<[LocalServiceInfo](#localserviceinfo)\> | 是 | 回调函数。成功添加时error为undefined，data为添加到本地的MDNS服务信息。 |

**错误码：**

以下错误码的详细介绍请参见[MDNS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-mdns)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 2204003 | Callback duplicated. |
| 2204008 | Failed to delete the service instance. |
| 2204010 | Failed to send the message. |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/jpn714GETxyOYvoRq0aAjA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=ECDBE17C7CBAE54114AC50B653DB37DDF028256EEC0C52641294415F579430A8)

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

Stage模型示例：

```ts
import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

let localServiceInfo: mdns.LocalServiceInfo = {
  serviceType: "_print._tcp",
  serviceName: "servicename",
  port: 5555,
  host: {
  address: "10.14.**.***",
  },
  serviceAttribute: [{key: "111", value: [1]}]
}

mdns.addLocalService(context, localServiceInfo, (error:BusinessError, data:mdns.LocalServiceInfo) =>  {
  console.error(JSON.stringify(error));
  console.info(JSON.stringify(data));
});
```

#### mdns.addLocalService

addLocalService(context: Context, serviceInfo: LocalServiceInfo): Promise<LocalServiceInfo>

添加一个MDNS服务，使用Promise方式作为异步方法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| context | Context | 是 | 
应用的上下文。

FA模型的应用Context定义见[Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-app-context)。

Stage模型的应用Context定义见[Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)。

 |
| serviceInfo | [LocalServiceInfo](#localserviceinfo) | 是 | MDNS服务的信息。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[LocalServiceInfo](#localserviceinfo)\> | 以Promise形式返回添加的MDNS服务信息。 |

**错误码：**

以下错误码的详细介绍请参见[MDNS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-mdns)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 2204003 | Callback duplicated. |
| 2204008 | Failed to delete the service instance. |
| 2204010 | Failed to send the message. |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/U7Emo2ArTh23ha8f3iuVUg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=F78310EC18966834070EB02B359593F2D0342D96356A65DE5FE893EB1150599B)

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

Stage模型示例：

```ts
import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

let localServiceInfo: mdns.LocalServiceInfo = {
  serviceType: "_print._tcp",
  serviceName: "servicename",
  port: 5555,
  host: {
    address: "10.14.**.***",
  },
  serviceAttribute: [{key: "111", value: [1]}]
}

mdns.addLocalService(context, localServiceInfo).then((data: mdns.LocalServiceInfo) => {
  console.info(JSON.stringify(data));
});
```

#### mdns.removeLocalService

removeLocalService(context: Context, serviceInfo: LocalServiceInfo, callback: AsyncCallback<LocalServiceInfo>): void

移除一个MDNS服务，使用callback方式作为异步方法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.Communication.NetManager.MDNS

**参数**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| context | Context | 是 | 
应用的上下文。

FA模型的应用Context定义见[Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-app-context)。

Stage模型的应用Context定义见[Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)。

 |
| serviceInfo | [LocalServiceInfo](#localserviceinfo) | 是 | MDNS服务的信息。 |
| callback | AsyncCallback<[LocalServiceInfo](#localserviceinfo)\> | 是 | 回调函数。成功移除error为undefined，data为移除本地的MDNS服务信息。 |

**错误码：**

以下错误码的详细介绍请参见[MDNS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-mdns)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 2204002 | Callback not found. |
| 2204008 | Failed to delete the service instance. |
| 2204010 | Failed to send the message. |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/085xPfCuT1C4Vq-3V9VHVw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=64ECE8B3CC7C8A0F2FC42A50E392EB4C9ECF62C9DB278B039A40CCA1FE88B457)

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

Stage模型示例：

```ts
import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

let localServiceInfo: mdns.LocalServiceInfo = {
  serviceType: "_print._tcp",
  serviceName: "servicename",
  port: 5555,
  host: {
  address: "10.14.**.***",
  },
  serviceAttribute: [{key: "111", value: [1]}]
}

mdns.removeLocalService(context, localServiceInfo, (error: BusinessError, data: mdns.LocalServiceInfo) =>  {
  console.error(JSON.stringify(error));
  console.info(JSON.stringify(data));
});
```

#### mdns.removeLocalService

removeLocalService(context: Context, serviceInfo: LocalServiceInfo): Promise<LocalServiceInfo>

移除一个MDNS服务，使用Promise方式作为异步方法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.Communication.NetManager.MDNS

**参数**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| context | Context | 是 | 
应用的上下文。

FA模型的应用Context定义见[Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-app-context)。

Stage模型的应用Context定义见[Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)。

 |
| serviceInfo | [LocalServiceInfo](#localserviceinfo) | 是 | MDNS服务的信息。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[LocalServiceInfo](#localserviceinfo)\> | 以Promise形式返回移除的MDNS服务信息。 |

**错误码：**

以下错误码的详细介绍请参见[MDNS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-mdns)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 2204002 | Callback not found. |
| 2204008 | Failed to delete the service instance. |
| 2204010 | Failed to send the message. |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/HRQwR0opT42rTnqYbWASXQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=29449ACFAC4A6095A37C2ABE96A9545BAE335BFE5F765053C4CB957561D979C4)

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

Stage模型示例：

```ts
import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

let localServiceInfo: mdns.LocalServiceInfo = {
  serviceType: "_print._tcp",
  serviceName: "servicename",
  port: 5555,
  host: {
  address: "10.14.**.***",
  },
  serviceAttribute: [{key: "111", value: [1]}]
}

mdns.removeLocalService(context, localServiceInfo).then((data: mdns.LocalServiceInfo) => {
  console.info(JSON.stringify(data));
});
```

#### mdns.createDiscoveryService

createDiscoveryService(context: Context, serviceType: string): DiscoveryService

返回一个DiscoveryService对象，该对象用于发现指定服务类型（serviceType）的MDNS服务。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| context | Context | 是 | 
应用的上下文。

FA模型的应用Context定义见[Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-app-context)。

Stage模型的应用Context定义见[Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)。

 |
| serviceType | string | 是 | 需要发现的MDNS服务类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| DiscoveryService | 基于指定服务类型（serviceType）和Context的发现服务对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/a7j7dJ5zRYmBRkAuEcpquA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=C276991DA1C8954065A357E27A5906A87FE6AED5AD785DE144679AFB2834E5D5)

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

Stage模型示例：

```ts
import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

let serviceType = "_print._tcp";
let discoveryService : Object = mdns.createDiscoveryService(context, serviceType);
```

#### mdns.resolveLocalService

resolveLocalService(context: Context, serviceInfo: LocalServiceInfo, callback: AsyncCallback<LocalServiceInfo>): void

解析一个MDNS服务，使用callback方式作为异步方法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.Communication.NetManager.MDNS

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| context | Context | 是 | 
应用的上下文。

FA模型的应用Context定义见[Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-app-context)。

Stage模型的应用Context定义见[Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)。

 |
| serviceInfo | [LocalServiceInfo](#localserviceinfo) | 是 | MDNS服务的信息。 |
| callback | AsyncCallback<[LocalServiceInfo](#localserviceinfo)\> | 是 | 回调函数。成功移除error为undefined，data为解析的MDNS服务信息。 |

**错误码：**

以下错误码的详细介绍请参见[MDNS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-mdns)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 2204003 | Callback duplicated. |
| 2204006 | Request timeout. |
| 2204010 | Failed to send the message. |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/5KnY4ng4RvObhYGgZdzbXA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=7A3F81B9683AD1A9A59F0354954B4EE3B963F2FEA98ED519E06A56CC5C70A4C3)

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

Stage模型示例：

```ts
import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

let localServiceInfo: mdns.LocalServiceInfo = {
  serviceType: "_print._tcp",
  serviceName: "servicename",
  port: 5555,
  host: {
  address: "10.14.**.***",
  },
  serviceAttribute: [{key: "111", value: [1]}]
}

mdns.resolveLocalService(context, localServiceInfo, (error: BusinessError, data: mdns.LocalServiceInfo) =>  {
  console.error(JSON.stringify(error));
  console.info(JSON.stringify(data));
});
```

#### mdns.resolveLocalService

resolveLocalService(context: Context, serviceInfo: LocalServiceInfo): Promise<LocalServiceInfo>

解析一个MDNS服务，使用Promise方式作为异步方法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.Communication.NetManager.MDNS

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| context | Context | 是 | 
应用的上下文。

FA模型的应用Context定义见[Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-app-context)。

Stage模型的应用Context定义见[Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)。

 |
| serviceInfo | [LocalServiceInfo](#localserviceinfo) | 是 | MDNS服务的信息。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[LocalServiceInfo](#localserviceinfo)\> | 以Promise形式返回解析的MDNS服务信息。 |

**错误码：**

以下错误码的详细介绍请参见[MDNS错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-mdns)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 2204003 | Callback duplicated. |
| 2204006 | Request timeout. |
| 2204010 | Failed to send the message. |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/unhww81yQ1yYerQ4oF4e1w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=45803585DD7BA096E2504221A12FC51958B2986F17D27AE43AB106F50E66A105)

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

Stage模型示例：

```ts
import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

let localServiceInfo: mdns.LocalServiceInfo = {
  serviceType: "_print._tcp",
  serviceName: "servicename",
  port: 5555,
  host: {
  address: "10.14.**.***",
  },
  serviceAttribute: [{key: "111", value: [1]}]
}

mdns.resolveLocalService(context, localServiceInfo).then((data: mdns.LocalServiceInfo) => {
  console.info(JSON.stringify(data));
});
```

#### DiscoveryService

指定服务类型的发现服务对象。

#### \[h2\]startSearchingMDNS

startSearchingMDNS(): void

开始搜索局域网内的MDNS服务。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/HJ0ZnsWkSHaZ6b6phFza3g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=E163DFE5D6F6E959B30BC6EE3F033665288A48FCF16495D0656CAD947DD62268)

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

Stage模型示例：

```ts
import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let serviceType = "_print._tcp";
let discoveryService = mdns.createDiscoveryService(context, serviceType);
discoveryService.startSearchingMDNS();
```

#### \[h2\]stopSearchingMDNS

stopSearchingMDNS(): void

停止搜索局域网内的MDNS服务。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/wlXmz7xOR2imR75m7ki28Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=1013CEB535D75C289D0B85BCCFC07091B730A6539D658CC1EAD9F09B8292E0EB)

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

Stage模型示例：

```ts
import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let serviceType = "_print._tcp";
let discoveryService = mdns.createDiscoveryService(context, serviceType);
discoveryService.stopSearchingMDNS();
```

#### \[h2\]on('discoveryStart')

on(type: 'discoveryStart', callback: Callback<DiscoveryEventInfo>): void

订阅开启监听mDNS服务的通知。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 
订阅事件，固定为'discoveryStart'。

discoveryStart：开始搜索局域网内的MDNS服务事件。

 |
| callback | Callback<[DiscoveryEventInfo](#discoveryeventinfo11)\> | 是 | MDNS服务的信息和事件错误信息。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/cp2zIFq3Qrie4xokG713HA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=C0A50C65274C7BF8AAE5A79821E6439072434EEEA2E6DE7D4A0B5E152A72EAC4)

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 参考mdns.createDiscoveryService。
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let serviceType = "_print._tcp";
let discoveryService = mdns.createDiscoveryService(context, serviceType);
discoveryService.startSearchingMDNS();

discoveryService.on('discoveryStart', (data: mdns.DiscoveryEventInfo) => {
  console.info(JSON.stringify(data));
});

discoveryService.stopSearchingMDNS();
```

#### \[h2\]off('discoveryStart')

off(type: 'discoveryStart', callback?: Callback<DiscoveryEventInfo>): void

取消开启监听MDNS服务的通知。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 
取消订阅的事件，固定为'discoveryStart'。

discoveryStart：开始搜索局域网内的MDNS服务事件。

 |
| callback | Callback<[DiscoveryEventInfo](#discoveryeventinfo11)\> | 否 | MDNS服务的信息和事件错误信息。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/6zyz4ivMQYWc-FI4MDb-Pw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=3162222F06B7E128AE2329131CF31707341D36BDB7D015EDF86E017674CCC906)

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 参考mdns.createDiscoveryService。
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let serviceType = "_print._tcp";
let discoveryService = mdns.createDiscoveryService(context, serviceType);
discoveryService.startSearchingMDNS();

discoveryService.on('discoveryStart', (data: mdns.DiscoveryEventInfo) => {
  console.info(JSON.stringify(data));
});

discoveryService.stopSearchingMDNS();

discoveryService.off('discoveryStart', (data: mdns.DiscoveryEventInfo) => {
  console.info(JSON.stringify(data));
});
```

#### \[h2\]on('discoveryStop')

on(type: 'discoveryStop', callback: Callback<DiscoveryEventInfo>): void

订阅停止监听MDNS服务的通知。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 
订阅事件，固定为'discoveryStop'。

discoveryStop：停止搜索局域网内的MDNS服务事件。

 |
| callback | Callback<[DiscoveryEventInfo](#discoveryeventinfo11)\> | 是 | MDNS服务的信息和事件错误信息。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/1HJfswifRc2Kr4ep-t6kDw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=AD2D167E22A1AF47439D2453C3958227A5919B2A7CD94E6EFC583A568D09FCF0)

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 参考mdns.createDiscoveryService。
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let serviceType = "_print._tcp";
let discoveryService = mdns.createDiscoveryService(context, serviceType);
discoveryService.startSearchingMDNS();

discoveryService.on('discoveryStop', (data: mdns.DiscoveryEventInfo) => {
  console.info(JSON.stringify(data));
});

discoveryService.stopSearchingMDNS();
```

#### \[h2\]off('discoveryStop')

off(type: 'discoveryStop', callback?: Callback<[DiscoveryEventInfo](#discoveryeventinfo11)\>): void

取消订阅停止监听MDNS服务的通知。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 
取消订阅的事件'discoveryStop'。

discoveryStop：停止搜索局域网内的MDNS服务事件。

 |
| callback | Callback<[DiscoveryEventInfo](#discoveryeventinfo11)\> | 否 | MDNS服务的信息和事件错误信息。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/7wboWiXWQXye4aZt6bPu9A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=A838D7DBCF4917FB340E8BD64658B7D40C4E0A568C68D9E54E1A8CE69790F117)

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 参考mdns.createDiscoveryService。
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let serviceType = "_print._tcp";
let discoveryService = mdns.createDiscoveryService(context, serviceType);
discoveryService.startSearchingMDNS();

discoveryService.on('discoveryStop', (data: mdns.DiscoveryEventInfo) => {
  console.info(JSON.stringify(data));
});

discoveryService.stopSearchingMDNS();

discoveryService.off('discoveryStop', (data: mdns.DiscoveryEventInfo) => {
  console.info(JSON.stringify(data));
});
```

#### \[h2\]on('serviceFound')

on(type: 'serviceFound', callback: Callback<LocalServiceInfo>): void

订阅发现MDNS服务的通知。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 
订阅事件，固定为'serviceFound'。

serviceFound：发现MDNS服务事件。

 |
| callback | Callback<[LocalServiceInfo](#localserviceinfo)\> | 是 | MDNS服务的信息，需调用resolveLocalService解析这个MDNS服务信息。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/GLvxXlvmTC-KyU0Y16PmUw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=31DB015E0E8A20EAA21B624401246BE0EDC0AB593CFA7B0EA93815BD6C796015)

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 参考mdns.createDiscoveryService。
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let serviceType = "_print._tcp";
let discoveryService = mdns.createDiscoveryService(context, serviceType);
discoveryService.startSearchingMDNS();

discoveryService.on('serviceFound', (data: mdns.LocalServiceInfo) => {
  console.info('serviceFound', JSON.stringify(data));
  mdns.resolveLocalService(context, data, (error: BusinessError, resolveData: mdns.LocalServiceInfo) =>  {
    console.info('serviceFound', JSON.stringify(resolveData));
  });
});

discoveryService.stopSearchingMDNS();
```

#### \[h2\]off('serviceFound')

off(type: 'serviceFound', callback?: Callback<LocalServiceInfo>): void

取消订阅发现MDNS服务的通知。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 
取消订阅的事件，固定为'serviceFound'。

serviceFound：发现MDNS服务事件。

 |
| callback | Callback<[LocalServiceInfo](#localserviceinfo)\> | 否 | MDNS服务的信息。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/4A8YDz0WS3SJ4iYranPt9g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=EA16DC0AB6C331E43C13ADBA0B1951C8CDADBBBA4826B83CEFA52EE69B23A0C5)

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 参考mdns.createDiscoveryService。
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let serviceType = "_print._tcp";
let discoveryService = mdns.createDiscoveryService(context, serviceType);
discoveryService.startSearchingMDNS();

discoveryService.on('serviceFound', (data: mdns.LocalServiceInfo) => {
  console.info('serviceFound', JSON.stringify(data));
  mdns.resolveLocalService(context, data, (error: BusinessError, resolveData: mdns.LocalServiceInfo) =>  {
    console.info('serviceFound', JSON.stringify(resolveData));
  });
});

discoveryService.stopSearchingMDNS();

discoveryService.off('serviceFound', (data: mdns.LocalServiceInfo) => {
  console.info(JSON.stringify(data));
});
```

#### \[h2\]on('serviceLost')

on(type: 'serviceLost', callback: Callback<LocalServiceInfo>): void

订阅移除MDNS服务的通知。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 
订阅事件，固定为'serviceLost'。

serviceLost：移除MDNS服务事件。

 |
| callback | Callback<[LocalServiceInfo](#localserviceinfo)\> | 是 | MDNS服务的信息。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/kA1hZi8eS8KP_FCOr7Ym4g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=823412BA008A252AB206B92E2858C8C28990814D82AEE75CA6D6CC01686DC738)

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 参考mdns.createDiscoveryService。
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let serviceType = "_print._tcp";
let discoveryService = mdns.createDiscoveryService(context, serviceType);
discoveryService.startSearchingMDNS();

discoveryService.on('serviceLost', (data: mdns.LocalServiceInfo) => {
  console.info(JSON.stringify(data));
});

discoveryService.stopSearchingMDNS();
```

#### \[h2\]off('serviceLost')

off(type: 'serviceLost', callback?: Callback<LocalServiceInfo>): void

取消订阅移除MDNS服务的通知。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 
取消订阅的事件，固定为'serviceLost'。

serviceLost：移除MDNS服务事件。

 |
| callback | Callback<[LocalServiceInfo](#localserviceinfo)\> | 否 | MDNS服务的信息。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/_cs1Hv8fQDqdTZq_lzpcdg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=34AB1DB40242699A8E7D3548750E5E9EF12AB6A752FDDA78FF8381CA6C6D5CC9)

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 参考mdns.createDiscoveryService。
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let serviceType = "_print._tcp";
let discoveryService = mdns.createDiscoveryService(context, serviceType);
discoveryService.startSearchingMDNS();

discoveryService.on('serviceLost', (data: mdns.LocalServiceInfo) => {
  console.info(JSON.stringify(data));
});

discoveryService.stopSearchingMDNS();

discoveryService.off('serviceLost', (data: mdns.LocalServiceInfo) => {
  console.info(JSON.stringify(data));
});
```

#### LocalServiceInfo

MDNS服务信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| serviceType | string | 否 | 否 | MDNS服务的类型。格式：\_<name>.<\_tcp/\_udp>，name长度小于63字符并且不能包含字符'.'。 |
| serviceName | string | 否 | 否 | MDNS服务的名字。 |
| port | number | 否 | 是 | MDNS服务的端口号。取值范围\[0，65535\]。 |
| host | [NetAddress](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection#netaddress) | 否 | 是 | MDNS服务设备的IP地址。采用设备的IP，添加服务和移除服务时候不生效。 |
| serviceAttribute | Array<[ServiceAttribute](#serviceattribute)\> | 否 | 是 | MDNS服务属性信息。 |

#### ServiceAttribute

MDNS服务属性信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| key | string | 否 | 否 | MDNS服务属性键值，键值长度应该小于9个字符。 |
| value | Array<number> | 否 | 否 | MDNS服务属性值。 |

#### DiscoveryEventInfo11+

监听到的MDNS服务事件信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| serviceInfo | LocalServiceInfo | 否 | 否 | MDNS服务信息。 |
| errorCode | MdnsError | 否 | 是 | MDNS错误信息。 |

#### MdnsError

MDNS错误信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| INTERNAL\_ERROR | 0 | 内部错误导致操作失败。 |
| ALREADY\_ACTIVE | 1 | 服务已经存在导致操作失败。 |
| MAX\_LIMIT | 2 | 请求超过最大限制导致操作失败。 |

#### NetAddress

type NetAddress = connection.NetAddress

获取网络地址。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 类型 | 说明 |
| :-- | :-- |
| connection.NetAddress | 定义网络地址。 |

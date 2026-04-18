---
title: "@ohos.router (页面路由)(不推荐)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-router"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "ArkTS API"
  - "UI界面"
  - "@ohos.router (页面路由)(不推荐)"
captured_at: "2026-04-17T01:47:53.384Z"
---

# @ohos.router (页面路由)(不推荐)

本模块提供通过不同的url访问不同的页面，包括跳转到应用内的指定页面、同应用内的某个页面替换当前页面、返回上一页面或指定的页面等。

推荐使用[Navigation组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-navigation-architecture)作为应用路由框架。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/MjQ2AZsISaCpIITehNZwGA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=45AEA68F86A4A7E7F54317478F1147299DC4CE040CF39CFFE300772803A6033B)

-   本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
    
-   页面路由需要在页面渲染完成之后才能调用，在onInit和onReady生命周期中页面还处于渲染阶段，禁止调用页面路由方法。
    
-   本模块功能依赖UI的执行上下文，不可在[UI上下文不明确](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface#ui上下文不明确)的地方使用，参见[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)说明。
    
-   如果使用传入callback形式的[pushUrl](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router#pushurl-1)或[pushNamedRoute](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router#pushnamedroute-1)接口，callback中通过[getLength](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router#getlengthdeprecated)等接口获取的栈信息为中间态的栈信息，可能与栈操作完全结束后，再通过[getLength](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router#getlengthdeprecated)等接口获取的栈信息不一致。
    

#### 导入模块

```ts
import { router } from '@kit.ArkUI';
```

#### router.pushUrl(deprecated)

pushUrl(options: RouterOptions): Promise<void>

跳转到应用内的指定页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/bmJXVof7SQyqfpFWLI8dWQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=A9D84965F8FB13832C628D94B361ADFF28EBE8AF4BDE65A2A75334F6B42F784B)

-   从API version 9开始支持，从API version 18开始废弃，建议使用[pushUrl](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router#pushurl)替代。pushUrl需先通过[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)获取[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)实例，然后通过该实例进行调用。
    
-   从API version 10开始，可以通过使用[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)方法获取当前UI上下文关联的[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)对象。
    

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [RouterOptions](#routeroptions) | 是 | 跳转页面描述信息。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 异常返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)、[页面路由错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-router)和[接口调用异常错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-internal)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/E_IxNMmGRgCPIKy6iGxwDQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=341A86D735059DC48A2EED94D011EE74622A3C2953E9E293A8373B9C66FEA459)

该接口返回的以下错误码均为string类型。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100002 | Uri error. The URI of the page to redirect is incorrect or does not exist. |
| 100003 | Page stack error. Too many pages are pushed. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

class innerParams {
  data3: number[];

  constructor(tuple: number[]) {
    this.data3 = tuple;
  }
}

class RouterParams {
  data1: string;
  data2: innerParams;

  constructor(str: string, tuple: number[]) {
    this.data1 = str;
    this.data2 = new innerParams(tuple);
  }
}

router.pushUrl({
  url: 'pages/routerpage2',
  params: new RouterParams('message', [123, 456, 789])
})
  .then(() => {
    console.error(`pushUrl finish`);
  })
  .catch((err: ESObject) => {
    console.error(`pushUrl failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}`);
  })
```

#### router.pushUrl(deprecated)

pushUrl(options: RouterOptions, callback: AsyncCallback<void>): void

跳转到应用内的指定页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/Eloa8mTQQDmHJVntqKeAng/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=EC4147155D06C28F1768DA48BD9BF12FA4F25547BA31B36CE23690FC76F48AF3)

-   从API version 9开始支持，从API version 18开始废弃，建议使用[pushUrl](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router#pushurl-1)替代。pushUrl需先通过[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)获取[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)实例，然后通过该实例进行调用。
    
-   从API version 10开始，可以通过使用[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)方法获取当前UI上下文关联的[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)对象。
    

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [RouterOptions](#routeroptions) | 是 | 跳转页面描述信息。 |
| callback | AsyncCallback<void> | 是 | 异常响应回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)、[页面路由错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-router)和[接口调用异常错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-internal)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/FZMXs2ioRo6w5bnTQMclkg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=7DC242813F0B050F6C5B46BF3B5906455A8CF79F931F16BE537A460D58945392)

该接口返回的以下错误码均为string类型。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100002 | Uri error. The URI of the page to redirect is incorrect or does not exist. |
| 100003 | Page stack error. Too many pages are pushed. |

**示例：**

```ts
class innerParams {
  data3: number[];

  constructor(tuple: number[]) {
    this.data3 = tuple;
  }
}

class RouterParams {
  data1: string;
  data2: innerParams;

  constructor(str: string, tuple: number[]) {
    this.data1 = str;
    this.data2 = new innerParams(tuple);
  }
}

router.pushUrl({
  url: 'pages/routerpage2',
  params: new RouterParams('message', [123, 456, 789])
}, (err) => {
  if (err) {
    console.error(`pushUrl failed, code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('pushUrl success');
})
```

#### router.pushUrl(deprecated)

pushUrl(options: RouterOptions, mode: RouterMode): Promise<void>

跳转到应用内的指定页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/TE99nn7HSEeF6R3VZxHAXA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=99835240F59CCCFBD7BC75BA66EC33DDA066796DFC2B9DCC9B0132FA1D6BBA3A)

-   从API version 9开始支持，从API version 18开始废弃，建议使用[pushUrl](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router#pushurl-2)替代。pushUrl需先通过[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)获取[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)实例，然后通过该实例进行调用。
    
-   从API version 10开始，可以通过使用[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)方法获取当前UI上下文关联的[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)对象。
    

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [RouterOptions](#routeroptions) | 是 | 跳转页面描述信息。 |
| mode | [RouterMode](#routermode9) | 是 | 跳转页面使用的模式。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 异常返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)、[页面路由错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-router)和[接口调用异常错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-internal)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/i-06-OpKTUm473TX6l_KrA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=DD7CE07C4E1F1187D00688F367FAE9D6A261FEAC7AF688F49CDA9C620124AF56)

该接口返回的以下错误码均为string类型。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100002 | Uri error. The URI of the page to redirect is incorrect or does not exist. |
| 100003 | Page stack error. Too many pages are pushed. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

class innerParams {
  data3: number[];

  constructor(tuple: number[]) {
    this.data3 = tuple;
  }
}

class RouterParams {
  data1: string;
  data2: innerParams;

  constructor(str: string, tuple: number[]) {
    this.data1 = str;
    this.data2 = new innerParams(tuple);
  }
}

router.pushUrl({
  url: 'pages/routerpage2',
  params: new RouterParams('message', [123, 456, 789])
}, router.RouterMode.Standard)
  .then(() => {
    console.error(`pushUrl finish`);
  })
  .catch((err: ESObject) => {
    console.error(`pushUrl failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}`);
  })
```

#### router.pushUrl(deprecated)

pushUrl(options: RouterOptions, mode: RouterMode, callback: AsyncCallback<void>): void

跳转到应用内的指定页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/lh67IagqR8iS6TROLwos6A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=5163D2130C33E8C5536B7C6F68A928CE13F4157337EF712F270334461FCA466A)

-   从API version 9开始支持，从API version 18开始废弃，建议使用[pushUrl](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router#pushurl-3)替代。pushUrl需先通过[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)获取[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)实例，然后通过该实例进行调用。
    
-   从API version 10开始，可以通过使用[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)方法获取当前UI上下文关联的[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)对象。
    

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [RouterOptions](#routeroptions) | 是 | 跳转页面描述信息。 |
| mode | [RouterMode](#routermode9) | 是 | 跳转页面使用的模式。 |
| callback | AsyncCallback<void> | 是 | 异常响应回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)、[页面路由错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-router)和[接口调用异常错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-internal)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/j3g_8MTVR6K2F_TMikFlRA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=969E8C5E2C79C1EF88AD5C5AE260D7FDF60F0CE8798212F91ACD21CEAF2EE940)

该接口返回的以下错误码均为string类型。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100002 | Uri error. The URI of the page to redirect is incorrect or does not exist. |
| 100003 | Page stack error. Too many pages are pushed. |

**示例：**

```ts
class innerParams {
  data3: number[];

  constructor(tuple: number[]) {
    this.data3 = tuple;
  }
}

class RouterParams {
  data1: string;
  data2: innerParams;

  constructor(str: string, tuple: number[]) {
    this.data1 = str;
    this.data2 = new innerParams(tuple);
  }
}

router.pushUrl({
  url: 'pages/routerpage2',
  params: new RouterParams('message', [123, 456, 789])
}, router.RouterMode.Standard, (err) => {
  if (err) {
    console.error(`pushUrl failed, code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('pushUrl success');
})
```

#### router.replaceUrl(deprecated)

replaceUrl(options: RouterOptions): Promise<void>

用应用内的某个页面替换当前页面，并销毁被替换的页面。不支持设置页面转场动效，如需设置，推荐使用[Navigation组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-navigation-architecture)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/4oh5t8SeQBCBwVFX5-W1Qw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=BCAE3FB325D5D346A7613BA30D34F0EA2F76C653325FAD82CCD2EAF37621E58A)

-   从API version 9开始支持，除Lite Wearable外，从API version 18开始废弃，建议使用[replaceUrl](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router#replaceurl)替代。replaceUrl需先通过[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)获取[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)实例，然后通过该实例进行调用。
    
-   从API version 10开始，可以通过使用[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)方法获取当前UI上下文关联的[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)对象。
    

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [RouterOptions](#routeroptions) | 是 | 替换页面描述信息。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 异常返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)、[页面路由错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-router)和[接口调用异常错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-internal)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/Z5dyoGtWSBOW4QeyrxyTwQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=1686C335B821C7C55AB275AF77B2542B617CBE09225EB90EFEB325A0E9AE3569)

该接口返回的以下错误码均为string类型。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | The UI execution context is not found. This error code is thrown only in the standard system. |
| 200002 | Uri error. The URI of the page to be used for replacement is incorrect or does not exist. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

class RouterParams {
  data1: string;

  constructor(str: string) {
    this.data1 = str;
  }
}

router.replaceUrl({
  url: 'pages/detail',
  params: new RouterParams('message')
})
  .then(() => {
    console.error(`replaceUrl finish`);
  })
  .catch((err: ESObject) => {
    console.error(`replaceUrl failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}`);
  })
```

#### router.replaceUrl(deprecated)

replaceUrl(options: RouterOptions, callback: AsyncCallback<void>): void

用应用内的某个页面替换当前页面，并销毁被替换的页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/mf0H_X6fSVKrGiy7v80evw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=28943CED3A5D781A015A9AFDBC3E00CE9A0703A96218494B1E92D976194BC43C)

-   从API version 9开始支持，除Lite Wearable外，从API version 18开始废弃，建议使用[replaceUrl](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router#replaceurl-1)替代。replaceUrl需先通过[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)获取[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)实例，然后通过该实例进行调用。
    
-   从API version 10开始，可以通过使用[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)方法获取当前UI上下文关联的[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)对象。
    

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [RouterOptions](#routeroptions) | 是 | 替换页面描述信息。 |
| callback | AsyncCallback<void> | 是 | 异常响应回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)、[页面路由错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-router)和[接口调用异常错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-internal)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/2-YEGwq_R5aOPAKFZE8ROA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=60CF6E5154B5301FAA5626DAA7DBCF442820641D00588B2745BEA698FC7B6113)

该接口返回的以下错误码均为string类型。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | The UI execution context is not found. This error code is thrown only in the standard system. |
| 200002 | Uri error. The URI of the page to be used for replacement is incorrect or does not exist. |

**示例：**

```ts
class RouterParams {
  data1: string;

  constructor(str: string) {
    this.data1 = str;
  }
}

router.replaceUrl({
  url: 'pages/detail',
  params: new RouterParams('message')
}, (err) => {
  if (err) {
    console.error(`replaceUrl failed, code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('replaceUrl success');
})
```

#### router.replaceUrl(deprecated)

replaceUrl(options: RouterOptions, mode: RouterMode): Promise<void>

用应用内的某个页面替换当前页面，并销毁被替换的页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/kxstqdhiR7-4-ScTU_DSzA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=A3698763E610C1ABE5470585AB46C915A73B90A97D9A3E38B07191BB77554BAD)

-   从API version 9开始支持，除Lite Wearable外，从API version 18开始废弃，建议使用[replaceUrl](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router#replaceurl-2)替代。replaceUrl需先通过[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)获取[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)实例，然后通过该实例进行调用。
    
-   从API version 10开始，可以通过使用[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)方法获取当前UI上下文关联的[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)对象。
    

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [RouterOptions](#routeroptions) | 是 | 替换页面描述信息。 |
| mode | [RouterMode](#routermode9) | 是 | 跳转页面使用的模式。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 异常返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)、[页面路由错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-router)和[接口调用异常错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-internal)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/f80FVGqMTIG7red0xCRAfw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=75E4880D0846F835AE4BEC90D0527E7C851180532857BEBBBE3E7E5F25B1D6EE)

该接口返回的以下错误码均为string类型。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Failed to get the delegate. This error code is thrown only in the standard system. |
| 200002 | Uri error. The URI of the page to be used for replacement is incorrect or does not exist. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

class RouterParams {
  data1:string;

  constructor(str:string) {
    this.data1 = str;
  }
}

router.replaceUrl({
  url: 'pages/detail',
  params: new RouterParams('message')
}, router.RouterMode.Standard)
  .then(() => {
    console.error(`replaceUrl finish`);
  })
  .catch((err: ESObject) => {
    console.error(`replaceUrl failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}`);
  })
```

#### router.replaceUrl(deprecated)

replaceUrl(options: RouterOptions, mode: RouterMode, callback: AsyncCallback<void>): void

用应用内的某个页面替换当前页面，并销毁被替换的页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/IUOeJrDFRFqUmUUdcMs7bA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=3B11E33550DCD701AEC40A8F4BF7A43FFA52B022A07860B1C6C4A711E523A6FD)

-   从API version 9开始支持，除Lite Wearable外，从API version 18开始废弃，建议使用[replaceUrl](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router#replaceurl-3)替代。replaceUrl需先通过[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)获取[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)实例，然后通过该实例进行调用。
    
-   从API version 10开始，可以通过使用[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)方法获取当前UI上下文关联的[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)对象。
    

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [RouterOptions](#routeroptions) | 是 | 替换页面描述信息。 |
| mode | [RouterMode](#routermode9) | 是 | 跳转页面使用的模式。 |
| callback | AsyncCallback<void> | 是 | 异常响应回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)、[页面路由错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-router)和[接口调用异常错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-internal)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/YduwDO2HTReL7hrNie_-Xg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=82FCC1EFE4458B547EAED9E02CF3890CF3E42C9A60EA1F9523233BEB68102C21)

该接口返回的以下错误码均为string类型。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | The UI execution context is not found. This error code is thrown only in the standard system. |
| 200002 | Uri error. The URI of the page to be used for replacement is incorrect or does not exist. |

**示例：**

```ts
class RouterParams {
  data1: string;

  constructor(str: string) {
    this.data1 = str;
  }
}

router.replaceUrl({
  url: 'pages/detail',
  params: new RouterParams('message')
}, router.RouterMode.Standard, (err) => {
  if (err) {
    console.error(`replaceUrl failed, code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('replaceUrl success');
});
```

#### router.pushNamedRoute(deprecated)

pushNamedRoute(options: NamedRouterOptions): Promise<void>

跳转到指定的命名路由页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/8OdwckAAQjORb3mnaLdvkw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=196CAB7A041437D3DCBE9810023EC0C846C9B83A842C67929F3A6C59B6C62A70)

-   从API version 10开始支持，从API version 18开始废弃，建议使用[pushNamedRoute](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router#pushnamedroute)替代。pushNamedRoute需先通过[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)获取[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)实例，然后通过该实例进行调用。
    
-   从API version 10开始，可以通过使用[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)方法获取当前UI上下文关联的[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)对象。
    

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [NamedRouterOptions](#namedrouteroptions10) | 是 | 跳转页面描述信息。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 异常返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)、[页面路由错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-router)和[接口调用异常错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-internal)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/EaPhZSDjRvOrWjIbf1bg4w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=A43F9B0D9F5AB75ADFDDECEF75C1A4D30D84344EA7BE6B5BE486BF18FA1EE692)

该接口返回的以下错误码均为string类型。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100003 | Page stack error. Too many pages are pushed. |
| 100004 | Named route error. The named route does not exist. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

class innerParams {
  data3: number[];

  constructor(tuple: number[]) {
    this.data3 = tuple;
  }
}

class RouterParams {
  data1: string;
  data2: innerParams;

  constructor(str: string, tuple: number[]) {
    this.data1 = str;
    this.data2 = new innerParams(tuple);
  }
}

router.pushNamedRoute({
  name: 'myPage',
  params: new RouterParams('message', [123, 456, 789])
})
  .then(() => {
    console.error(`pushNamedRoute finish`);
  })
  .catch((err: ESObject) => {
    console.error(`pushNamedRoute failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}`);
  })
```

详细示例请参考：[UI开发-命名路由](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-routing#命名路由)

#### router.pushNamedRoute(deprecated)

pushNamedRoute(options: NamedRouterOptions, callback: AsyncCallback<void>): void

跳转到指定的命名路由页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/EBlXCxOES6q1ftWNYmDUlA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=BE919D9D7D886AEC36C399068B8200F271ED5B1A5C024A272B0987EA9B308DDA)

-   从API version 10开始支持，从API version 18开始废弃，建议使用[pushNamedRoute](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router#pushnamedroute-1)替代。pushNamedRoute需先通过[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)获取[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)实例，然后通过该实例进行调用。
    
-   从API version 10开始，可以通过使用[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)方法获取当前UI上下文关联的[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)对象。
    

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [NamedRouterOptions](#namedrouteroptions10) | 是 | 跳转页面描述信息。 |
| callback | AsyncCallback<void> | 是 | 异常响应回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)、[页面路由错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-router)和[接口调用异常错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-internal)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/qqsU-TmARm2n625AXGCE8g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=514D633C9BD74A16C382FBCEA3DADB7C2B9962975FF651C512CBFC37A9CE99B7)

该接口返回的以下错误码均为string类型。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100003 | Page stack error. Too many pages are pushed. |
| 100004 | Named route error. The named route does not exist. |

**示例：**

```ts
class innerParams {
  data3: number[];

  constructor(tuple: number[]) {
    this.data3 = tuple;
  }
}

class RouterParams {
  data1: string;
  data2: innerParams;

  constructor(str: string, tuple: number[]) {
    this.data1 = str;
    this.data2 = new innerParams(tuple);
  }
}

router.pushNamedRoute({
  name: 'myPage',
  params: new RouterParams('message', [123, 456, 789])
}, (err) => {
  if (err) {
    console.error(`pushNamedRoute failed, code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('pushNamedRoute success');
})
```

#### router.pushNamedRoute(deprecated)

pushNamedRoute(options: NamedRouterOptions, mode: RouterMode): Promise<void>

跳转到指定的命名路由页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/b5jl4a_DS2C9muSeOJRAgA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=4C46CCD4AF74B58C2A7B361617175216E14F7F3E80E855042143BE29805EF16A)

-   从API version 10开始支持，从API version 18开始废弃，建议使用[pushNamedRoute](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router#pushnamedroute-2)替代。pushNamedRoute需先通过[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)获取[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)实例，然后通过该实例进行调用。
    
-   从API version 10开始，可以通过使用[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)方法获取当前UI上下文关联的[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)对象。
    

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [NamedRouterOptions](#namedrouteroptions10) | 是 | 跳转页面描述信息。 |
| mode | [RouterMode](#routermode9) | 是 | 跳转页面使用的模式。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 异常返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)、[页面路由错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-router)和[接口调用异常错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-internal)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/sw5Z8FqyQLy4R4MVbjq9Kg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=1926BFE5795FBE72E3792E837E8799ACE4F96B241A804C26C713B82D102A1E80)

该接口返回的以下错误码均为string类型。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100003 | Page stack error. Too many pages are pushed. |
| 100004 | Named route error. The named route does not exist. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

class innerParams {
  data3: number[];

  constructor(tuple: number[]) {
    this.data3 = tuple;
  }
}

class RouterParams {
  data1: string;
  data2: innerParams;

  constructor(str: string, tuple: number[]) {
    this.data1 = str
    this.data2 = new innerParams(tuple)
  }
}

router.pushNamedRoute({
  name: 'myPage',
  params: new RouterParams('message', [123, 456, 789])
}, router.RouterMode.Standard)
  .then(() => {
    console.error(`pushNamedRoute finish`);
  })
  .catch((err: ESObject) => {
    console.error(`pushNamedRoute failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}`);
  })
```

#### router.pushNamedRoute(deprecated)

pushNamedRoute(options: NamedRouterOptions, mode: RouterMode, callback: AsyncCallback<void>): void

跳转到指定的命名路由页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/-zIYqJSGTmamfj7WPe-dSg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=CE48D7432382AF66DA99EABFA5B99447B169F47BAC923A83B6FF87F9F92C209F)

-   从API version 10开始支持，从API version 18开始废弃，建议使用[pushNamedRoute](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router#pushnamedroute-3)替代。pushNamedRoute需先通过[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)获取[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)实例，然后通过该实例进行调用。
    
-   从API version 10开始，可以通过使用[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)方法获取当前UI上下文关联的[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)对象。
    

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [NamedRouterOptions](#namedrouteroptions10) | 是 | 跳转页面描述信息。 |
| mode | [RouterMode](#routermode9) | 是 | 跳转页面使用的模式。 |
| callback | AsyncCallback<void> | 是 | 异常响应回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)、[页面路由错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-router)和[接口调用异常错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-internal)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/wjplWauGRR2vcJRFo8q5OA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=3E910AEF3D32FCC26207E045C485DE6B264A05AD212B12FA1EAD6B1FEE118D91)

该接口返回的以下错误码均为string类型。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100003 | Page stack error. Too many pages are pushed. |
| 100004 | Named route error. The named route does not exist. |

**示例：**

```ts
class innerParams {
  data3: number[];

  constructor(tuple: number[]) {
    this.data3 = tuple;
  }
}

class RouterParams {
  data1: string;
  data2: innerParams;

  constructor(str: string, tuple: number[]) {
    this.data1 = str;
    this.data2 = new innerParams(tuple);
  }
}

router.pushNamedRoute({
  name: 'myPage',
  params: new RouterParams('message', [123, 456, 789])
}, router.RouterMode.Standard, (err) => {
  if (err) {
    console.error(`pushNamedRoute failed, code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('pushNamedRoute success');
})
```

#### router.replaceNamedRoute(deprecated)

replaceNamedRoute(options: NamedRouterOptions): Promise<void>

用指定的命名路由页面替换当前页面，并销毁被替换的页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/ggus6aXOQPK7IZ0tM8_2hQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=E213BC8A0182BFA00111882232504D8C5A3EF925EDCB4673482114CFDA44890B)

-   从API version 10开始支持，从API version 18开始废弃，建议使用[replaceNamedRoute](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router#replacenamedroute)替代。replaceNamedRoute需先通过[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)获取[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)实例，然后通过该实例进行调用。
    
-   从API version 10开始，可以通过使用[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)方法获取当前UI上下文关联的[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)对象。
    

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [NamedRouterOptions](#namedrouteroptions10) | 是 | 替换页面描述信息。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 异常返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)、[页面路由错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-router)和[接口调用异常错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-internal)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/y-AwvinDSY673qOxMbLYxA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=05241A2A2DAC3A13F698663F821B17EE9009EDE33FC091F3D04D0E464006DE3C)

该接口返回的以下错误码均为string类型。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | The UI execution context is not found. This error code is thrown only in the standard system. |
| 100004 | Named route error. The named route does not exist. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

class RouterParams {
  data1: string;

  constructor(str: string) {
    this.data1 = str;
  }
}

router.replaceNamedRoute({
  name: 'myPage',
  params: new RouterParams('message')
})
  .then(() => {
    console.error(`replaceNamedRoute finish`);
  })
  .catch((err: ESObject) => {
    console.error(`replaceNamedRoute failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}`);
  })
```

#### router.replaceNamedRoute(deprecated)

replaceNamedRoute(options: NamedRouterOptions, callback: AsyncCallback<void>): void

用指定的命名路由页面替换当前页面，并销毁被替换的页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/SffTaJ7wTmK2hGYlRM6PMg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=F87CDE51E89B37D83A7E01D04B46DA8FDA818D3433C3DAF59DF001C7B045D315)

-   从API version 10开始支持，从API version 18开始废弃，建议使用[replaceNamedRoute](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router#replacenamedroute-1)替代。replaceNamedRoute需先通过[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)获取[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)实例，然后通过该实例进行调用。
    
-   从API version 10开始，可以通过使用[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)方法获取当前UI上下文关联的[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)对象。
    

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [NamedRouterOptions](#namedrouteroptions10) | 是 | 替换页面描述信息。 |
| callback | AsyncCallback<void> | 是 | 异常响应回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)、[页面路由错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-router)和[接口调用异常错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-internal)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/R39lHH64Rm-Jp7Rj45fb5A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=862131723FDF07329ECEE5942557CF610BCC73F517E0DA6F7F1DCEB19C8BC79C)

该接口返回的以下错误码均为string类型。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | The UI execution context is not found. This error code is thrown only in the standard system. |
| 100004 | Named route error. The named route does not exist. |

**示例：**

```ts
class RouterParams {
  data1: string;

  constructor(str: string) {
    this.data1 = str;
  }
}

router.replaceNamedRoute({
  name: 'myPage',
  params: new RouterParams('message')
}, (err) => {
  if (err) {
    console.error(`replaceNamedRoute failed, code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('replaceNamedRoute success');
})
```

#### router.replaceNamedRoute(deprecated)

replaceNamedRoute(options: NamedRouterOptions, mode: RouterMode): Promise<void>

用指定的命名路由页面替换当前页面，并销毁被替换的页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/O380MVmDQDWUO2DJdhY3xw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=F559092B8B5D81D6DD00371C4C20022DB86A9D2250E8137F5DF9D0A156A94576)

-   从API version 10开始支持，从API version 18开始废弃，建议使用[replaceNamedRoute](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router#replacenamedroute-2)替代。replaceNamedRoute需先通过[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)获取[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)实例，然后通过该实例进行调用。
    
-   从API version 10开始，可以通过使用[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)方法获取当前UI上下文关联的[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)对象。
    

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [NamedRouterOptions](#namedrouteroptions10) | 是 | 替换页面描述信息。 |
| mode | [RouterMode](#routermode9) | 是 | 跳转页面使用的模式。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 异常返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)、[页面路由错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-router)和[接口调用异常错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-internal)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/1bXYxRmiRdK3Kez1FSK5jg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=B0F93E37C27CCDE9B7BC49C6A877665BA3DF55A821435AE12330717459563943)

该接口返回的以下错误码均为string类型。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Failed to get the delegate. This error code is thrown only in the standard system. |
| 100004 | Named route error. The named route does not exist. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

class RouterParams {
  data1: string;

  constructor(str: string) {
    this.data1 = str;
  }
}

router.replaceNamedRoute({
  name: 'myPage',
  params: new RouterParams('message')
}, router.RouterMode.Standard)
  .then(() => {
    console.error(`replaceNamedRoute finish`);
  })
  .catch((err: ESObject) => {
    console.error(`replaceNamedRoute failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}`);
  })
```

#### router.replaceNamedRoute(deprecated)

replaceNamedRoute(options: NamedRouterOptions, mode: RouterMode, callback: AsyncCallback<void>): void

用指定的命名路由页面替换当前页面，并销毁被替换的页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/012wW2VwQXaRCrPnJ3-zJg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=980E1BA48E5A93F9EA16F4F276C0C947511F41151890EA28B56A1992161D67EE)

-   从API version 10开始支持，从API version 18开始废弃，建议使用[replaceNamedRoute](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router#replacenamedroute-3)替代。replaceNamedRoute需先通过[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)获取[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)实例，然后通过该实例进行调用。
    
-   从API version 10开始，可以通过使用[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)方法获取当前UI上下文关联的[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)对象。
    

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [NamedRouterOptions](#namedrouteroptions10) | 是 | 替换页面描述信息。 |
| mode | [RouterMode](#routermode9) | 是 | 跳转页面使用的模式。 |
| callback | AsyncCallback<void> | 是 | 异常响应回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)、[页面路由错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-router)和[接口调用异常错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-internal)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/MxoWW9YAT0Ke3IfWPjei-Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=AD329E8454505BF905162A11F630D4FFF10D321ABF92F47B1D7D1F884503C06D)

该接口返回的以下错误码均为string类型。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | The UI execution context is not found. This error code is thrown only in the standard system. |
| 100004 | Named route error. The named route does not exist. |

**示例：**

```ts
class RouterParams {
  data1: string;

  constructor(str: string) {
    this.data1 = str;
  }
}

router.replaceNamedRoute({
  name: 'myPage',
  params: new RouterParams('message')
}, router.RouterMode.Standard, (err) => {
  if (err) {
    console.error(`replaceNamedRoute failed, code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('replaceNamedRoute success');
});
```

#### router.back(deprecated)

back(options?: RouterOptions ): void

返回上一页面或指定的页面，会删除当前页面与指定页面之间的所有页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/4BPTPW58TmCvn-XEzM8amg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=84EA878DEC95560200131909D3CBF234BAA5A4655729F79E3FCCAAA6C42B842B)

-   从API version 8开始支持，从API version 18开始废弃，建议使用[back](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router#back)替代。back需先通过[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)获取[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)实例，然后通过该实例进行调用。
    
-   从API version 10开始，可以通过使用[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)方法获取当前UI上下文关联的[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)对象。
    

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [RouterOptions](#routeroptions) | 否 | 返回页面描述信息，其中参数url指路由跳转时会返回到指定url的界面，如果页面栈上没有url页面，则不响应该情况。如果url未设置，则返回上一页，页面不会重新构建，页面栈里面的page不会回收，出栈后会被回收。back是返回接口，url设置为特殊值"/"不生效。如果是用命名路由的方式跳转，传入的url需是命名路由的名称。 |

**示例：**

```ts
this.getUIContext().getRouter().back({ url: 'pages/detail' });
```

#### router.back(deprecated)

back(index: number, params?: Object): void;

返回指定的页面，会删除当前页面与指定页面之间的所有页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/gzqZELo_SxunhPsBH3eU4A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=25D5A15D1F2829C2F92DE4D8BF65D186D74CF2B9D425635A27D7FEBA4349844E)

-   从API version 12开始支持，从API version 18开始废弃，建议使用[back](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router#back12)替代。back需先通过[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)获取[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)实例，然后通过该实例进行调用。
    
-   从API version 12开始，可以通过使用[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)方法获取当前UI上下文关联的[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)对象。
    

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| index | number | 是 | 跳转目标页面的索引值。 从栈底到栈顶，index从1开始递增。 |
| params | Object | 否 | 页面返回时携带的参数。 |

**示例：**

```ts
this.getUIContext().getRouter().back(1);
```

```ts
this.getUIContext().getRouter().back(1, { info: '来自Home页' }); //携带参数返回
```

#### router.clear(deprecated)

clear(): void

清空页面栈中的所有历史页面，仅保留当前页面作为栈顶页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/f_gkO-E2RR2ZtbLcLYLHWg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=6A2B712A951D0662B6CB6467CA2B985511BB723940F363170F7290DF02C7A967)

-   从API version 8开始支持，从API version 18开始废弃，建议使用[clear](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router#clear)替代。clear需先通过[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)获取[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)实例，然后通过该实例进行调用。
    
-   从API version 10开始，可以通过使用[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)方法获取当前UI上下文关联的[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)对象。
    

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ts
this.getUIContext().getRouter().clear();
```

#### router.getLength(deprecated)

getLength(): string

获取当前在页面栈内的页面数量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/DMRWKiZ7SUG1klyA7xxRcA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=7394FAEF3AF73D1518892165515D30E6A4BAC592A7B0E521B30C8AB11575275F)

-   从API version 8开始支持，从API version 18开始废弃，建议使用[getLength](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router#getlengthdeprecated)替代。getLength需先通过[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)获取[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)实例，然后通过该实例进行调用。
    
-   从API version 10开始，可以通过使用[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)方法获取当前UI上下文关联的[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)对象。
    

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 页面数量，页面栈支持最大数值是32。 |

**示例：**

```ts
let size = this.getUIContext().getRouter().getLength();
console.info('pages stack size = ' + size);
```

#### router.getState(deprecated)

getState(): RouterState

获取栈顶页面的状态信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/Au5yikuISMWGZbsztkXGOQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=960E379B240B028F7469C8EDA837430FDAAFACBCBE877BCA1F5FCB098523D601)

-   从API version 8开始支持，从API version 18开始废弃，建议使用[getState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router#getstate)替代。getLength需先通过[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)获取[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)实例，然后通过该实例进行调用。
    
-   从API version 10开始，可以通过使用[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)方法获取当前UI上下文关联的[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)对象。
    

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [RouterState](#routerstate) | 页面状态信息。 |

**示例：**

```ts
let page = this.getUIContext().getRouter().getState();
console.info('current index = ' + page.index);
console.info('current name = ' + page.name);
console.info('current path = ' + page.path);
```

#### router.getStateByIndex(deprecated)

getStateByIndex(index: number): RouterState | undefined

通过索引值获取对应页面的状态信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/NFYXwG09RzmFK-4YuYjfJg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=0F0C73461FC02C0406BAAA50E57F1A85236C9FC1A8B7BB0270C9C7CA64B8886B)

-   从API version 12开始支持，从API version 18开始废弃，建议使用[getStateByIndex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router#getstatebyindex12)替代。getStateByIndex需先通过[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)获取[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)实例，然后通过该实例进行调用。
    
-   从API version 12开始，可以通过使用[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)方法获取当前UI上下文关联的[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)对象。
    

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| index | number | 是 | 表示要获取的页面索引。从栈底到栈顶，index从1开始递增。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [RouterState](#routerstate) | undefined | 返回页面状态信息。索引不存在时返回undefined。 |

**示例：**

```ts
let options: router.RouterState | undefined = router.getStateByIndex(1);
if (options != undefined) {
  console.info('index = ' + options.index);
  console.info('name = ' + options.name);
  console.info('path = ' + options.path);
  console.info(`params = ${JSON.stringify(options.params)}`);
}
```

#### router.getStateByUrl(deprecated)

getStateByUrl(url: string): Array<RouterState>

通过url获取对应页面的状态信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/JJzlORLKRpCAaSgCFWe3eA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=8EE58DED151AC3701FE8CAA7BB5F3D8BB85537251D1F74546202828A9FFFB7B3)

-   从API version 12开始支持，从API version 18开始废弃，建议使用[getStateByUrl](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router#getstatebyurl12)替代。getStateByUrl需先通过[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)获取[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)实例，然后通过该实例进行调用。
    
-   从API version 12开始，可以通过使用[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)方法获取当前UI上下文关联的[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)对象。
    

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| url | string | 是 | 表示要获取对应页面信息的url。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Array<[RouterState](#routerstate)\> | 页面状态信息。 |

**示例：**

```ts
let options: Array<router.RouterState> = router.getStateByUrl('pages/index');
for (let i: number = 0; i < options.length; i++) {
  console.info('index = ' + options[i].index);
  console.info('name = ' + options[i].name);
  console.info('path = ' + options[i].path);
  console.info('params = ' + options[i].params);
}
```

#### RouterState

页面状态信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| index | number | 否 | 否 | 
表示当前页面在页面栈中的索引。从栈底到栈顶，index从1开始递增。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| name | string | 否 | 否 | 

表示当前页面的名称，即对应文件名。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| path | string | 否 | 否 | 

表示当前页面的路径。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| params12+ | Object | 否 | 否 | 

表示当前页面携带的参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |

#### router.showAlertBeforeBackPage(deprecated)

showAlertBeforeBackPage(options: EnableAlertOptions): void

开启页面返回询问对话框。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/iFGWoJRHRqqpCz0hX94cTw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=BCD358FD4F5676CDE42E4BD72140C8EFE474B80CC1ED0E6D7782250BCA7E5369)

-   从API version 9开始支持，从API version 18开始废弃，建议使用[showAlertBeforeBackPage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router#showalertbeforebackpage)替代。showAlertBeforeBackPage需先通过[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)获取[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)实例，然后通过该实例进行调用。
    
-   从API version 10开始，可以通过使用[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)方法获取当前UI上下文关联的[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)对象。
    

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [EnableAlertOptions](#enablealertoptions) | 是 | 文本弹窗信息描述。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[接口调用异常错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-internal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  this.getUIContext().getRouter().showAlertBeforeBackPage({
    message: 'Message Info'
  });
} catch (err) {
  console.error(`showAlertBeforeBackPage failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}`);
}
```

#### EnableAlertOptions

页面返回询问对话框选项。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.ArkUI.ArkUI.Full。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| message | string | 否 | 否 | 询问对话框内容。 |

#### router.hideAlertBeforeBackPage(deprecated)

hideAlertBeforeBackPage(): void

禁用页面返回询问对话框。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/fk9X0gROTfWhTSQSjbQOPQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=4BBEF0B7399F2D98494A7B680B6BAA4E52D395BEA0421001A86B9652CB921776)

-   从API version 9开始支持，从API version 18开始废弃，建议使用[hideAlertBeforeBackPage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router#hidealertbeforebackpage)替代。hideAlertBeforeBackPage需先通过[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)获取[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)实例，然后通过该实例进行调用。
    
-   从API version 10开始，可以通过使用[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)方法获取当前UI上下文关联的[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)对象。
    

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ts
this.getUIContext().getRouter().hideAlertBeforeBackPage();
```

#### router.getParams(deprecated)

getParams(): Object

获取发起跳转的页面往当前页传入的参数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/jI6aKkpKSre0DIt5scftGQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=72DEAA43D5E4B5C6B950B3FF49650812825D38B4ACF243F0FBDA94827EC0162A)

-   从API version 8开始支持，从API version 18开始废弃，建议使用[getParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router#getparams)替代。getParams需先通过[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)获取[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)实例，然后通过该实例进行调用。
    
-   从API version 10开始，可以通过使用[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)方法获取当前UI上下文关联的[Router](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router)对象。
    

getParams只获取当前页面的参数，并不会清除页面关联的参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Object | 发起跳转的页面往当前页传入的参数。 |

**示例：**

```ts
this.getUIContext().getRouter().getParams();
```

#### RouterOptions

路由跳转选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| url | string | 否 | 否 | 
表示目标页面的url，可以用以下两种格式：

\- 页面绝对路径，由配置文件中pages列表提供，例如：

\- pages/index/index

\- pages/detail/detail

\- 特殊值，如果url的值是"/"，则跳转到首页，首页默认为页面跳转配置项src数组的第一个数据项。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| params | Object | 否 | 是 | 

表示路由跳转时要同时传递到目标页面的数据，切换到其他页面时，当前接收的数据失效。跳转到目标页面后，使用router.getParams()获取传递的参数，此外，在类web范式中，参数也可以在页面中直接使用，如this.keyValue(keyValue为跳转时params参数中的key值)，如果目标页面中已有该字段，则其值会被传入的字段值覆盖。

**说明：**

params参数只能传递可序列化的参数，不能传递方法和系统接口返回的对象（例如，媒体接口定义和返回的PixelMap对象）。建议开发者提取系统接口返回的对象中需要被传递的基础类型属性，自行构造object类型对象进行传递。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| recoverable14+ | boolean | 否 | 是 | 

表示对应的页面是否可恢复，默认为true。当为true时，表示可恢复，当为false时，表示不可恢复。

**说明：**

当应用退到后台，并且在未来的某个时间点，由于系统资源限制等原因被系统杀死，如果某个页面被设置成可恢复，那么该应用再次被拉到前台后系统可以恢复出页面，详细说明请参考[UIAbility备份恢复](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ability-recover-guideline)。

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/Lb38jqiVTJyH5l8nSKYM5Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=938535620CD25E9EB36A5503B3A54F0A550042F666046F3BFCA36A80F9AF2532)

页面路由栈支持的最大Page数量为32。

#### RouterMode9+

路由跳转模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full。

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| Standard | 0 | 
多实例模式，也是默认情况下的跳转模式。

目标页面会被添加到页面栈顶，无论栈中是否存在相同url的页面。

**说明：**

不使用路由跳转模式时，则按照默认的多实例模式进行跳转。

 |
| Single | 1 | 

单实例模式。

如果目标页面的url已经存在于页面栈中，则该url页面移动到栈顶。

如果目标页面的url在页面栈中不存在同url页面，则按照默认的多实例模式进行跳转。

 |

#### NamedRouterOptions10+

命名路由跳转选项。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| name | string | 否 | 否 | 
表示目标命名路由页面的name。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

 |
| params | Object | 否 | 是 | 

表示路由跳转时要同时传递到目标页面的数据。跳转到目标页面后，使用router.getParams()获取传递的参数，此外，在类web范式中，参数也可以在页面中直接使用，如this.keyValue(keyValue为跳转时params参数中的key值)，如果目标页面中已有该字段，则其值会被传入的字段值覆盖。

**说明：**

params参数不能传递方法和系统接口返回的对象（例如，媒体接口定义和返回的PixelMap对象）。建议开发者提取系统接口返回的对象中需要被传递的基础类型属性，自行构造object类型对象进行传递。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

 |
| recoverable14+ | boolean | 否 | 是 | 

表示对应的页面是否可恢复，默认为true。当为true时，表示可恢复，当为false时，表示不可恢复。

**说明：**

当应用退到后台，并且在未来的某个时间点，由于系统资源限制等原因被系统杀死，如果某个页面被设置成可恢复，那么该应用再次被拉到前台后系统可以恢复出页面，详细说明请参考[UIAbility备份恢复](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ability-recover-guideline)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

 |

#### 完整示例

#### \[h2\]基于JS扩展的类Web开发范式

以下代码仅适用于javascript文件，不适用于ArkTS文件

```js
// 在当前页面中
export default {
  pushPage() {
    router.pushUrl({
      url: 'pages/detail/detail',
      params: {
        data1: 'message'
      }
    });
  }
}
```

```js
// 在detail页面中
export default {
  onInit() {
    console.info('showData1:' + this.getUIContext().getRouter().getParams()['data1']);
  }
}
```

#### \[h2\]基于TS扩展的声明式开发范式

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/Pg7qibPMSzuseTTFPlFTbQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=ED54A4855AD9E40A77945CD2EADBB6AEB884316BDF539E23304666FB440ED69A)

直接使用router可能导致[UI上下文不明确](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface#ui上下文不明确)的问题，建议使用getUIContext获取[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)实例，并使用[getRouter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getrouter)获取绑定实例的router。

```ts
// 通过router.pushUrl跳转至目标页携带params参数
import { router } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

// 定义传递参数的类
class innerParams {
  array: number[];

  constructor(tuple: number[]) {
    this.array = tuple;
  }
}

class RouterParams {
  text: string;
  data: innerParams;

  constructor(str: string, tuple: number[]) {
    this.text = str;
    this.data = new innerParams(tuple);
  }
}

@Entry
@Component
struct Index {
  async routePage() {
    let options: router.RouterOptions = {
      url: 'pages/second',
      params: new RouterParams('这是第一页的值', [12, 45, 78])
    }
    // 建议使用this.getUIContext().getRouter().pushUrl()
    this.getUIContext().getRouter().pushUrl(options)
      .then(() => {
        console.error(`pushUrl finish`);
      })
      .catch((err: ESObject) => {
        console.error(`pushUrl failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}`);
      })
    }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Text('这是第一页')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
      Button() {
        Text('next page')
          .fontSize(25)
          .fontWeight(FontWeight.Bold)
      }.type(ButtonType.Capsule)
      .margin({ top: 20 })
      .backgroundColor('#ccc')
      .onClick(() => {
        this.routePage()
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

```ts
// 在second页面中接收传递过来的参数
import { router } from '@kit.ArkUI';

class innerParams {
  array: number[];

  constructor(tuple: number[]) {
    this.array = tuple;
  }
}

class RouterParams {
  text: string;
  data: innerParams;

  constructor(str: string, tuple: number[]) {
    this.text = str;
    this.data = new innerParams(tuple);
  }
}

@Entry
@Component
struct Second {
  private content: string = "这是第二页";
  // 建议使用this.getUIContext().getRouter().getParams()
  @State text: string = (this.getUIContext().getRouter().getParams() as RouterParams).text;
  @State data: object = (this.getUIContext().getRouter().getParams() as RouterParams).data;
  @State secondData: string = '';

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Text(`${this.content}`)
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
      Text(this.text)
        .fontSize(30)
        .onClick(() => {
          this.secondData = (this.data['array'][1]).toString();
        })
        .margin({ top: 20 })
      Text(`第一页传来的数值:${this.secondData}`)
        .fontSize(20)
        .margin({ top: 20 })
        .backgroundColor('red')
    }
    .width('100%')
    .height('100%')
  }
}
```

#### router.push(deprecated)

push(options: RouterOptions): void

跳转到应用内的指定页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/AdEBfq2xRGSfXkmWTXAZbg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=8F520A1E1E000DB84168BC0E9FCCA4A2730F9B730A3AEA0F23952554932E77C9)

从API version 8开始支持，从API version 9开始废弃，建议使用[pushUrl](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router#pushurl)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [RouterOptions](#routeroptions) | 是 | 跳转页面描述信息。 |

**示例：**

```ts
class innerParams {
  data3: number[];

  constructor(tuple: number[]) {
    this.data3 = tuple;
  }
}

class RouterParams {
  data1: string;
  data2: innerParams;

  constructor(str: string, tuple: number[]) {
    this.data1 = str;
    this.data2 = new innerParams(tuple);
  }
}

router.push({
  url: 'pages/routerpage2',
  params: new RouterParams('message', [123, 456, 789])
});
```

#### router.replace(deprecated)

replace(options: RouterOptions): void

用应用内的某个页面替换当前页面，并销毁被替换的页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/1MVoytkRRUiBWdTcdlF8tw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=B00F4719BF03C2092B46295A5E7C6F89350333C9BCE6E498B2B6DCFF3C002F34)

从API version 8开始支持，从API version 9开始废弃，建议使用[replaceUrl](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router#replaceurl)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [RouterOptions](#routeroptions) | 是 | 替换页面描述信息。 |

**示例：**

```ts
class RouterParams {
  data1: string;

  constructor(str: string) {
    this.data1 = str;
  }
}

router.replace({
  url: 'pages/detail',
  params: new RouterParams('message')
});
```

#### router.enableAlertBeforeBackPage(deprecated)

enableAlertBeforeBackPage(options: EnableAlertOptions): void

开启页面返回询问对话框。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/5p0n5kcfQoywNE-VI0V79g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=07CF192C7654ABD123F880F56E79D7C31B8D8801EBBB40D98ED9E5ABEDEF4E24)

从API version 8开始支持，从API version 9开始废弃，建议使用[showAlertBeforeBackPage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router#showalertbeforebackpage)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [EnableAlertOptions](#enablealertoptions) | 是 | 文本弹窗信息描述。 |

**示例：**

```ts
router.enableAlertBeforeBackPage({
  message: 'Message Info'
});
```

#### router.disableAlertBeforeBackPage(deprecated)

disableAlertBeforeBackPage(): void

禁用页面返回询问对话框。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/zShFBEWpQ0OKC7WQXS87lQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=7A4B7FD205BEBD4FCBFD311681A3E10299CDA60A36FFF707002574EC2CFC4683)

从API version 8开始支持，从API version 9开始废弃，建议使用[hideAlertBeforeBackPage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router#hidealertbeforebackpage)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ts
router.disableAlertBeforeBackPage();
```

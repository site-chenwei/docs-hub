---
title: "@ohos.application.formProvider (formProvider)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-formprovider"
menu_path:
  - "参考"
  - "应用框架"
  - "Form Kit（卡片开发服务）"
  - "已停止维护的接口"
  - "@ohos.application.formProvider (formProvider)"
captured_at: "2026-04-17T01:48:15.079Z"
---

# @ohos.application.formProvider (formProvider)

FormProvider模块提供了卡片提供方相关接口的能力，开发者在开发卡片时，可通过该模块提供接口实现更新卡片，设置卡片更新时间，获取卡片信息，请求发布卡片等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/RRj8s0_ORla2UDbrpSnO4g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=DD2B7D58448E39E32794A3E70C339D021AC655493BC5ABE381509E1EFC26646D)

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API version 9 开始废弃，建议使用[formProvider](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-form-formprovider)替代。

#### 导入模块

```ts
import { formProvider } from '@kit.FormKit';
```

#### formProvider.setFormNextRefreshTime

setFormNextRefreshTime(formId: string, minute: number, callback: AsyncCallback<void>): void

设置指定卡片的下一次更新时间，使用callback异步回调。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| formId | string | 是 | 卡片标识。 |
| minute | number | 是 | 指定多久之后更新。单位分钟，大于等于5。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { formProvider } from '@kit.FormKit';
// 使用时需要用已经存在formId
let formId: string = '12400633174999288';
formProvider.setFormNextRefreshTime(formId, 5, (error: BusinessError) => {
  if (error.code) {
    console.error(`formProvider setFormNextRefreshTime, errorCode: ${error.code}, errorMessage: ${error.message}`);
  }
});
```

#### formProvider.setFormNextRefreshTime

setFormNextRefreshTime(formId: string, minute: number): Promise<void>

设置指定卡片的下一次更新时间，使用Promise异步回调。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| formId | string | 是 | 卡片标识。 |
| minute | number | 是 | 指定多久之后更新。单位分钟，大于等于5。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { formProvider } from '@kit.FormKit';
// 使用时需要用已经存在formId
let formId: string = '12400633174999288';
formProvider.setFormNextRefreshTime(formId, 5).then(() => {
  console.info('formProvider setFormNextRefreshTime success');
}).catch((error: BusinessError) => {
  console.error(`formProvider setFormNextRefreshTime, errorCode: ${error.code}, errorMessage: ${error.message}`);
});
```

#### formProvider.updateForm

updateForm(formId: string, formBindingData: formBindingData.FormBindingData, callback: AsyncCallback<void>): void

更新指定的卡片，使用callback异步回调。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| formId | string | 是 | 请求更新的卡片标识。 |
| formBindingData | [formBindingData.FormBindingData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-formbindingdata#formbindingdata) | 是 | 用于更新的数据。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { formProvider, formBindingData } from '@kit.FormKit';

// 使用时需要用已经存在formId
let formId: string = '12400633174999288';
let param: Record<string, string> = {
  'temperature': '22c',
  'time': '22:00'
}
let obj: formBindingData.FormBindingData = formBindingData.createFormBindingData(param);
formProvider.updateForm(formId, obj, (error: BusinessError) => {
  if (error.code) {
    console.error(`formProvider updateForm, errorCode: ${error.code}, errorMessage: ${error.message}`);
  }
});
```

#### formProvider.updateForm

updateForm(formId: string, formBindingData: formBindingData.FormBindingData): Promise<void>

更新指定的卡片，使用Promise异步回调。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| formId | string | 是 | 请求更新的卡片标识。 |
| formBindingData | [formBindingData.FormBindingData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-formbindingdata#formbindingdata) | 是 | 用于更新的数据。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { formProvider, formBindingData } from '@kit.FormKit';

// 使用时需要用已经存在formId
let formId: string = '12400633174999288';
let param: Record<string, string> = {
  'temperature': '22c',
  'time': '22:00'
}
let obj: formBindingData.FormBindingData = formBindingData.createFormBindingData(param);
formProvider.updateForm(formId, obj).then(() => {
  console.info('formProvider updateForm success');
}).catch((error: BusinessError) => {
  console.error(`formProvider updateForm, errorCode: ${error.code}, errorMessage: ${error.message}`);
});
```

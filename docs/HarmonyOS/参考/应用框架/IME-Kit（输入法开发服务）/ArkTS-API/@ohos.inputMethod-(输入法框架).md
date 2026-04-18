---
title: "@ohos.inputMethod (输入法框架)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod"
menu_path:
  - "参考"
  - "应用框架"
  - "IME Kit（输入法开发服务）"
  - "ArkTS API"
  - "@ohos.inputMethod (输入法框架)"
captured_at: "2026-04-17T01:48:15.331Z"
---

# @ohos.inputMethod (输入法框架)

本模块主要面向普通前台应用（备忘录、信息、设置等系统应用与三方应用），提供对输入法（输入法应用）的控制、管理能力，包括显示/隐藏输入法软键盘、切换输入法、获取所有输入法列表等等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/b1boK4oDSASeaCx_nxzc1g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=5DE12DDCF2828A6331F5C3695D1BC397AFFAEA840F2FE68E0240264E1DB643F5)

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import { inputMethod } from '@kit.IMEKit';
```

#### 常量

常量值。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 参数名 | 类型 | 常量值 | 说明 |
| :-- | :-- | :-- | :-- |
| MAX\_TYPE\_NUM8+ | number | 128 | 可支持的最大输入法个数。 |

#### InputMethodProperty8+

输入法应用属性。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| name9+ | string | 是 | 否 | 必填。输入法包名。 |
| id9+ | string | 是 | 否 | 必填。输入法扩展在应用内唯一标识，与name一起组成输入法扩展的全局唯一标识。 |
| label9+ | string | 是 | 是 | 
非必填。

\- 当InputMethodProperty用于切换、查询等接口的入参时，开发者可不填写此字段，通过name和id即可唯一指定一个输入法扩展。

\- 当InputMethodProperty作为查询接口的返回值时（如[getCurrentInputMethod](#inputmethodgetcurrentinputmethod9)），此字段表示输入法扩展对外显示的名称，优先使用InputMethodExtensionAbility中配置的label，若未配置，自动使用应用入口ability的label；当应用入口ability未配置label时，自动使用应用AppScope中配置的label。

 |
| labelId10+ | number | 是 | 是 | 

非必填。

\- 当InputMethodProperty用于切换、查询等接口的入参时，开发者可不填写此字段，通过name和id即可唯一指定一个输入法扩展。

\- 当InputMethodProperty作为查询接口的返回值时（如[getCurrentInputMethod](#inputmethodgetcurrentinputmethod9)），此字段表示label字段的资源号。

 |
| icon9+ | string | 是 | 是 | 

非必填。

\- 当InputMethodProperty用于切换、查询等接口的入参时，开发者可不填写此字段，通过name和id即可唯一指定一个输入法扩展。

\- 当InputMethodProperty作为查询接口的返回值时（如[getCurrentInputMethod](#inputmethodgetcurrentinputmethod9)），此字段表示输入法图标数据，可以通过iconId查询获取。

 |
| iconId9+ | number | 是 | 是 | 

非必填。

\- 当InputMethodProperty用于切换、查询等接口的入参时，开发者可不填写此字段，通过name和id即可唯一指定一个输入法扩展。

\- 当InputMethodProperty作为查询接口的返回值时（如[getCurrentInputMethod](#inputmethodgetcurrentinputmethod9)），此字段表示icon字段的资源号。

 |
| enabledState20+ | [EnabledState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod#enabledstate15) | 是 | 是 | 

非必填。

\- 当InputMethodProperty用于切换、查询等接口的入参时，开发者可不填写此字段，通过name和id即可唯一指定一个输入法扩展

\- 当InputMethodProperty作为查询接口的返回值时（如[getCurrentInputMethod](#inputmethodgetcurrentinputmethod9)），此字段表示该输入法启用状态。

 |
| extra9+ | object | 否 | 是 | 

输入法扩展信息。预留字段，当前无具体含义，暂不支持使用。

\- API version 10起：非必填；

\- API version 9：必填。

 |
| packageName(deprecated) | string | 是 | 否 | 

输入法包名。必填。

说明：从API version 8开始支持，从API version 9开始废弃，建议使用name替代。

 |
| methodId(deprecated) | string | 是 | 否 | 

输入法唯一标识。必填。

说明：从API version 8开始支持，从API version 9开始废弃，建议使用id替代。

 |

#### CapitalizeMode20+

枚举，定义了文本首字母大写的不同模式。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| NONE | 0 | 不进行任何首字母大写处理。 |
| SENTENCES | 1 | 每个句子的首字母大写。 |
| WORDS | 2 | 每个单词首字母大写。 |
| CHARACTERS | 3 | 每个字母都大写。 |

#### inputMethod.getController9+

getController(): InputMethodController

获取客户端实例[InputMethodController](#inputmethodcontroller)。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [InputMethodController](#inputmethodcontroller) | 返回当前客户端实例。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**示例：**

```ts
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
```

#### inputMethod.getDefaultInputMethod11+

getDefaultInputMethod(): InputMethodProperty

获取默认输入法。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [InputMethodProperty](#inputmethodproperty8) | 返回默认输入法属性对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```ts
let defaultIme: inputMethod.InputMethodProperty = inputMethod.getDefaultInputMethod();
```

#### inputMethod.getSystemInputMethodConfigAbility11+

getSystemInputMethodConfigAbility(): ElementName

获取系统输入法设置界面Ability信息。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [ElementName](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-elementname) | 系统输入法设置界面Ability的ElementName。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```ts
import { bundleManager } from '@kit.AbilityKit';

let inputMethodConfig: bundleManager.ElementName = inputMethod.getSystemInputMethodConfigAbility();
```

#### inputMethod.getSetting9+

getSetting(): InputMethodSetting

获取客户端设置实例[InputMethodSetting](#inputmethodsetting8)。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [InputMethodSetting](#inputmethodsetting8) | 返回当前客户端设置实例。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12800007 | input method setter error. Possible cause: create InputMethodSetting object failed. |

**示例：**

```ts
let inputMethodSetting: inputMethod.InputMethodSetting = inputMethod.getSetting();
```

#### inputMethod.switchInputMethod9+

switchInputMethod(target: InputMethodProperty, callback: AsyncCallback<boolean>): void

切换输入法，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/y9hjj_PORfebNYK0wSDQvg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=B1ECDB29AB1E9584AF9007FEED1AE2E7CBEDF5319E68A1D59CD7F28B2CF87019)

-   在API version 9-10版本，仅支持系统应用调用且需要权限ohos.permission.CONNECT\_IME\_ABILITY。
-   在API version 11版本起，仅支持当前输入法应用调用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| target | [InputMethodProperty](#inputmethodproperty8) | 是 | 目标输入法。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当输入法切换成功，err为undefined，data为true；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800005 | configuration persistence error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let currentIme: inputMethod.InputMethodProperty = inputMethod.getCurrentInputMethod();
inputMethod.switchInputMethod(currentIme, (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to switchInputMethod, code: ${err.code}, message: ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in switching input method.');
  } else {
    console.error('Failed to switch input method.');
  }
});
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/AEM4QV9MTAmVe1B-n88LCQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=A4CAC1739F95CA773061ECA02478E192CB5544BF5C330061EE7D0F29A075308F)

在 API11 中 201 permissions check fails. 这个错误码被移除。

#### inputMethod.switchInputMethod9+

switchInputMethod(target: InputMethodProperty): Promise<boolean>

切换输入法，使用promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/tCOpwJ1TQry-Rfd44HBqxw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=622A1991F196603E2681026860F8FA3F363DD97838D5B128C7D928DE9C41E204)

-   在API version 9-10版本，仅支持系统应用调用且需要权限ohos.permission.CONNECT\_IME\_ABILITY。
-   在API version 11版本起，仅支持当前输入法应用调用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| target | [InputMethodProperty](#inputmethodproperty8) | 是 | 目标输入法。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象。返回true表示切换输入法成功，返回false表示切换输入法失败。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800005 | configuration persistence error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let currentIme: inputMethod.InputMethodProperty = inputMethod.getCurrentInputMethod();
inputMethod.switchInputMethod(currentIme).then((result: boolean) => {
  if (result) {
    console.info('Succeeded in switching input method.');
  } else {
    console.error('Failed to switch input method.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to switchInputMethod, code: ${err.code}, message: ${err.message}`);
});
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/baG6JNJzSPOqtcDFYS9HpA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=72C5C2618440B50DC7E0D44BCFCC88567880A633F3005F5EC7E8E1BBCDB747E3)

在 API11 中 201 permissions check fails. 这个错误码被移除。

#### inputMethod.getCurrentInputMethod9+

getCurrentInputMethod(): InputMethodProperty

使用同步方法获取当前输入法。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [InputMethodProperty](#inputmethodproperty8) | 返回当前输入法属性对象。 |

**示例：**

```ts
let currentIme: inputMethod.InputMethodProperty = inputMethod.getCurrentInputMethod();
```

#### inputMethod.switchCurrentInputMethodSubtype9+

switchCurrentInputMethodSubtype(target: InputMethodSubtype, callback: AsyncCallback<boolean>): void

切换当前输入法的子类型。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/SP1iTI8zTga69OZK29yUGw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=2FC737BA89E81A4CB307B0141C12FFB78CBBD81885E9BF42E4628C3DE6312F83)

-   在API version 9版本，仅支持系统应用调用且需要权限ohos.permission.CONNECT\_IME\_ABILITY。
-   在API version 10版本，支持系统应用和当前输入法应用调用；需要权限ohos.permission.CONNECT\_IME\_ABILITY。
-   在API version 11版本起，仅支持当前输入法调用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| target | [InputMethodSubtype](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod-subtype#inputmethodsubtype) | 是 | 目标输入法子类型。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当输入法子类型切换成功，err为undefined，data为true；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800005 | configuration persistence error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let extra: Record<string, string> = {}
// 参考InputMethodSubtype参数说明
inputMethod.switchCurrentInputMethodSubtype({
  id: "ServiceExtAbility",
  label: "",
  name: "com.example.keyboard",
  mode: "upper",
  locale: "",
  language: "",
  icon: "",
  iconId: 0,
  extra: extra
}, (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to switchCurrentInputMethodSubtype, code: ${err.code}, message: ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in switching currentInputMethodSubtype.');
  } else {
    console.error('Failed to switchCurrentInputMethodSubtype');
  }
});
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/epw4mSeKQqORiYr-BrDYVA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=D2DC1876ED382B544190682DC8835DC1B263F0B4AA8AC93FE4911F212337CEAE)

在 API11 中 201 permissions check fails. 这个错误码被移除。

#### inputMethod.switchCurrentInputMethodSubtype9+

switchCurrentInputMethodSubtype(target: InputMethodSubtype): Promise<boolean>

切换当前输入法的子类型。使用promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/Izks3xgsSUCOUQa_VPkDJA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=2AF5244345160769A61BB72D910F80E9D9DA8DEA0C4C32A480BA4CBF8F0BA366)

-   在API version 9版本，仅支持系统应用调用且需要权限ohos.permission.CONNECT\_IME\_ABILITY。
-   在API version 10版本，支持系统应用和当前输入法应用调用；需要权限ohos.permission.CONNECT\_IME\_ABILITY。
-   在API version 11版本起，仅支持当前输入法调用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| target | [InputMethodSubtype](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod-subtype#inputmethodsubtype) | 是 | 目标输入法子类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象。返回true表示当前输入法切换子类型成功，返回false表示当前输入法切换子类型成功失败。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800005 | configuration persistence error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let extra: Record<string, string> = {}
// 参考InputMethodSubtype参数说明
inputMethod.switchCurrentInputMethodSubtype({
  id: "ServiceExtAbility",
  label: "",
  name: "com.example.keyboard",
  mode: "upper",
  locale: "",
  language: "",
  icon: "",
  iconId: 0,
  extra: extra
}).then((result: boolean) => {
  if (result) {
    console.info('Succeeded in switching currentInputMethodSubtype.');
  } else {
    console.error('Failed to switchCurrentInputMethodSubtype.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to switchCurrentInputMethodSubtype, code: ${err.code}, message: ${err.message}`);
});
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/qJonMnx_TWGjV10eLelghA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=63B3E7CE45A0A72CF09EC762FA8D1A0C2CC06212977A0D98466FD7784B38C286)

在 API11 中 201 permissions check fails. 这个错误码被移除。

#### inputMethod.getCurrentInputMethodSubtype9+

getCurrentInputMethodSubtype(): InputMethodSubtype

获取当前输入法的子类型。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [InputMethodSubtype](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod-subtype#inputmethodsubtype) | 返回当前输入法子类型对象。 |

**示例：**

```ts
import { InputMethodSubtype } from '@kit.IMEKit';

let currentImeSubType: InputMethodSubtype = inputMethod.getCurrentInputMethodSubtype();
```

#### inputMethod.switchCurrentInputMethodAndSubtype9+

switchCurrentInputMethodAndSubtype(inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype, callback: AsyncCallback<boolean>): void

切换至指定输入法的指定子类型，适用于跨输入法切换子类型。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/AVyECtXgS82b7M9ZVbHGlA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=ED14A81A8A71C7D36B7123F9B1776221FB51DA2500EDBDD821D75AA304DFB690)

-   在API version 9-10版本，仅支持系统应用调用且需要权限ohos.permission.CONNECT\_IME\_ABILITY。
-   在API version 11版本起，仅支持当前输入法调用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| inputMethodProperty | [InputMethodProperty](#inputmethodproperty8) | 是 | 目标输入法。 |
| inputMethodSubtype | [InputMethodSubtype](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod-subtype#inputmethodsubtype) | 是 | 目标输入法子类型。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当输入法和子类型切换成功，err为undefined，data为获取到的切换子类型结果true；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800005 | configuration persistence error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```ts
import { InputMethodSubtype } from '@kit.IMEKit';
import { BusinessError } from '@kit.BasicServicesKit';

let currentIme: inputMethod.InputMethodProperty = inputMethod.getCurrentInputMethod();
let imSubType: InputMethodSubtype = inputMethod.getCurrentInputMethodSubtype();
inputMethod.switchCurrentInputMethodAndSubtype(currentIme, imSubType, (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to switchCurrentInputMethodAndSubtype, code: ${err.code}, message: ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in switching currentInputMethodAndSubtype.');
  } else {
    console.error('Failed to switchCurrentInputMethodAndSubtype.');
  }
});
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/nRXq3_asQOmF0j96e9-8XA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=FCD31D69AA321ED9F4D34746C2ABEB3E283E0799095A63A90E8BCDC006DD3997)

在 API11 中 201 permissions check fails. 这个错误码被移除。

#### inputMethod.switchCurrentInputMethodAndSubtype9+

switchCurrentInputMethodAndSubtype(inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype): Promise<boolean>

切换至指定输入法的指定子类型，适用于跨输入法切换子类型。使用promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/haL_l2G2RdOnYjBVqjGLKA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=687F04CCED6B183953841916AA6B2F92E4DE291592101E8187FA3892FDD71015)

-   在API version 9-10版本，仅支持系统应用调用且需要权限ohos.permission.CONNECT\_IME\_ABILITY。
-   在API version 11版本起，仅支持当前输入法调用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| inputMethodProperty | [InputMethodProperty](#inputmethodproperty8) | 是 | 目标输入法。 |
| inputMethodSubtype | [InputMethodSubtype](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod-subtype#inputmethodsubtype) | 是 | 目标输入法子类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象。返回true表示切换至指定输入法的指定子类型成功，返回false表示切换至指定输入法的指定子类型失败。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800005 | configuration persistence error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```ts
import { InputMethodSubtype } from '@kit.IMEKit';
import { BusinessError } from '@kit.BasicServicesKit';

let currentIme: inputMethod.InputMethodProperty = inputMethod.getCurrentInputMethod();
let imSubType: InputMethodSubtype = inputMethod.getCurrentInputMethodSubtype();
inputMethod.switchCurrentInputMethodAndSubtype(currentIme, imSubType).then((result: boolean) => {
  if (result) {
    console.info('Succeeded in switching currentInputMethodAndSubtype.');
  } else {
    console.error('Failed to switchCurrentInputMethodAndSubtype.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to switchCurrentInputMethodAndSubtype, code: ${err.code}, message: ${err.message}`);
});
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/WN0ZRm9BQzOJ32DzelCpLw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=CDFB7A3159AF1442E6FCCAD531E0384B3AF606BF290E0635A8B460283615E02B)

在 API11 中 201 permissions check fails. 这个错误码被移除。

#### inputMethod.getInputMethodController(deprecated)

getInputMethodController(): InputMethodController

获取客户端实例[InputMethodController](#inputmethodcontroller)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/NIa2aOO7RBikpLiNONRPIA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=E034C88C748EEABD4657FA18819299F8C17F7CDD322DFA916F4597A10BBB6A2F)

从API version 6开始支持，从API version 9开始废弃，建议使用[getController](#inputmethodgetcontroller9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [InputMethodController](#inputmethodcontroller) | 回调返回当前客户端实例。 |

**示例：**

```ts
let inputMethodController: inputMethod.InputMethodController = inputMethod.getInputMethodController();
```

#### inputMethod.getInputMethodSetting(deprecated)

getInputMethodSetting(): InputMethodSetting

获取客户端设置实例[InputMethodSetting](#inputmethodsetting8)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/I8GUDpOJTkmhWWPgCxlkvw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=521DF03BD2B6FEF5BB67208BFB70A228AFD4EC27E4415F78BCC28B11623A86C0)

从API version 8开始支持，从API version 9开始废弃，建议使用[getSetting](#inputmethodgetsetting9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [InputMethodSetting](#inputmethodsetting8) | 返回当前客户端设置实例。 |

**示例：**

```ts
let inputMethodSetting: inputMethod.InputMethodSetting = inputMethod.getInputMethodSetting();
```

#### inputMethod.setSimpleKeyboardEnabled20+

setSimpleKeyboardEnabled(enable: boolean): void

编辑框应用设置简单键盘标志。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| enable | boolean | 是 | 
简单键盘是否使能标志，true标识简单键盘使能，false标识简单键盘去使能。

原生编辑框组件在下一次点击获焦时生效；自绘控件在下一次调用[attach](#attach10)绑定输入法时生效。

 |

**示例：**

```ts
  let enable: boolean = false;
  inputMethod.setSimpleKeyboardEnabled(enable);
```

#### inputMethod.onAttachmentDidFail22+

onAttachmentDidFail(callback: Callback<AttachFailureReason>): void

订阅绑定失败事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | Callback<[AttachFailureReason](#attachfailurereason22)\> | 是 | 回调函数，返回绑定失败的原因，仅当注册者进程触发的绑定失败时，调用该回调函数。 |

**示例：**

```ts
import { Callback } from '@kit.BasicServicesKit';

let attachmentDidFailCallback: Callback<inputMethod.AttachFailureReason> =
  (reason: inputMethod.AttachFailureReason): void => {
    console.info(`Attachment failed with reason: ${reason}.`);
  if (reason === inputMethod.AttachFailureReason.CALLER_NOT_FOCUSED) {
    console.info(`Failure reason is CALLER_NOT_FOCUSED.`);
  }
  };
inputMethod.onAttachmentDidFail(attachmentDidFailCallback);
```

#### inputMethod.offAttachmentDidFail22+

offAttachmentDidFail(callback?: Callback<AttachFailureReason>): void

取消订阅绑定失败事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | Callback<[AttachFailureReason](#attachfailurereason22)\> | 否 | 取消订阅的回调函数，需要与订阅接口传入的保持一致。参数不填写时，取消订阅该事件的所有回调函数。 |

**示例：**

```ts
import { Callback } from '@kit.BasicServicesKit';

let attachmentDidFailCallback: Callback<inputMethod.AttachFailureReason> =
  (reason: inputMethod.AttachFailureReason): void => {
    console.info(`Attachment failed with reason: ${reason}.`);
  if (reason === inputMethod.AttachFailureReason.CALLER_NOT_FOCUSED) {
    console.info(`Failure reason is CALLER_NOT_FOCUSED.`);
  }
  };
inputMethod.onAttachmentDidFail(attachmentDidFailCallback);
inputMethod.offAttachmentDidFail(attachmentDidFailCallback);
```

#### TextInputType10+

文本输入类型。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| NONE | \-1 | NONE。 |
| TEXT | 0 | 文本类型。 |
| MULTILINE | 1 | 多行类型。 |
| NUMBER | 2 | 数字类型。 |
| PHONE | 3 | 电话号码类型。 |
| DATETIME | 4 | 日期类型。 |
| EMAIL\_ADDRESS | 5 | 邮箱地址类型。 |
| URL | 6 | 链接类型。 |
| VISIBLE\_PASSWORD | 7 | 密码类型。 |
| NUMBER\_PASSWORD11+ | 8 | 数字密码类型。 |
| SCREEN\_LOCK\_PASSWORD20+ | 9 | 锁屏密码类型。 |
| USER\_NAME20+ | 10 | 用户名类型。 |
| NEW\_PASSWORD20+ | 11 | 新密码类型。 |
| NUMBER\_DECIMAL20+ | 12 | 带小数点的数字类型。 |
| ONE\_TIME\_CODE20+ | 13 | 验证码类型。 |

#### EnterKeyType10+

Enter键的功能类型。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| UNSPECIFIED | 0 | 未指定。 |
| NONE | 1 | NONE。 |
| GO | 2 | 前往。 |
| SEARCH | 3 | 查找。 |
| SEND | 4 | 发送。 |
| NEXT | 5 | 下一步。 |
| DONE | 6 | 完成。 |
| PREVIOUS | 7 | 上一步。 |
| NEWLINE12+ | 8 | 换行。 |

#### KeyboardStatus10+

输入法软键盘状态。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| NONE | 0 | NONE。 |
| HIDE | 1 | 隐藏状态。 |
| SHOW | 2 | 显示状态。 |

#### Direction10+

光标移动方向。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| CURSOR\_UP | 1 | 向上。 |
| CURSOR\_DOWN | 2 | 向下。 |
| CURSOR\_LEFT | 3 | 向左。 |
| CURSOR\_RIGHT | 4 | 向右。 |

#### ExtendAction10+

编辑框中文本的扩展编辑操作类型，如剪切、复制等。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| SELECT\_ALL | 0 | 全选。 |
| CUT | 3 | 剪切。 |
| COPY | 4 | 复制。 |
| PASTE | 5 | 粘贴。 |

#### FunctionKey10+

输入法功能键类型。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| enterKeyType | [EnterKeyType](#enterkeytype10) | 否 | 否 | 输入法enter键类型。 |

#### InputAttribute10+

编辑框属性，包含文本输入类型和Enter键功能类型。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| textInputType | [TextInputType](#textinputtype10) | 否 | 否 | 文本输入类型。 |
| enterKeyType | [EnterKeyType](#enterkeytype10) | 否 | 否 | Enter键功能类型。 |
| placeholder20+ | string | 否 | 是 | 
编辑框设置的占位符信息。

\- 编辑框设置占位符信息时，长度不超过255个字符（如果超出将会自动截断为255个字符），用于提示或引导用户输入临时性文本或符号。（例如：提示输入项为"必填"或"非必填"的输入结果反馈。）

\- 编辑框没有设置占位符信息时，默认为空字符串。

\- 该字段在调用[attach](#attach10)时提供给输入法应用。

 |
| abilityName20+ | string | 否 | 是 | 

编辑框设置的ability名称。

\- 编辑框设置ability名称时，长度不超过127个字符（如果超出将会自动截断为127个字符）。

\- 编辑框未设置ability名称时，默认为空字符串。

\- 该字段在调用绑定[attach](#attach10)时提供给输入法应用。

 |

#### TextConfig10+

编辑框的配置信息。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| inputAttribute | [InputAttribute](#inputattribute10) | 否 | 否 | 编辑框属性。 |
| cursorInfo | [CursorInfo](#cursorinfo10) | 否 | 是 | 光标信息。 |
| selection | [Range](#range10) | 否 | 是 | 文本选中的范围。 |
| windowId | number | 否 | 是 | 
编辑框所在的窗口Id，该参数应为整数。

推荐使用[getWindowProperties](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#getwindowproperties9)方法获取窗口id属性。

 |
| newEditBox20+ | boolean | 否 | 是 | 表示是否为新编辑框。true表示新编辑框，false表示非新编辑框。 |
| capitalizeMode20+ | [CapitalizeMode](#capitalizemode20) | 否 | 是 | 编辑框设置大小写模式。如果没有设置或设置非法值，默认不进行任何首字母大写处理。 |

#### CursorInfo10+

光标信息。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| left | number | 否 | 否 | 光标的横坐标，单位为px。该参数应为整数，最小值为0，最大值为当前屏幕的宽度。 |
| top | number | 否 | 否 | 光标的纵坐标，单位为px。该参数应为整数，最小值为0，最大值为当前屏幕的高度。 |
| width | number | 否 | 否 | 光标的宽度，单位为px。该参数应为整数，最小值为0，最大值为当前屏幕的宽度。 |
| height | number | 否 | 否 | 光标的高度，单位为px。该参数应为整数，最小值为0，最大值为当前屏幕的高度 |

#### Range10+

文本的选中范围。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| start | number | 否 | 否 | 选中文本的首字符在编辑框的索引值。该参数应为大于或等于0的整数，不超过文本实际长度。 |
| end | number | 否 | 否 | 选中文本的末字符在编辑框的索引值。该参数应为大于或等于0的整数，不超过文本实际长度，end值要大于start值。 |

#### Movement10+

选中文本时，光标移动的方向。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| direction | [Direction](#direction10) | 否 | 否 | 选中文本时，光标的移动方向。 |

#### InputWindowInfo10+

输入法软键盘的窗口信息。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| name | string | 否 | 否 | 输入法窗口的名称。 |
| left | number | 否 | 否 | 输入法窗口左上顶点的横坐标，单位为px。该参数应为整数，最小值为0，最大值为当前屏幕的宽度。 |
| top | number | 否 | 否 | 输入法窗口左上顶点的纵坐标，单位为px。该参数应为整数，最小值为0，最大值为当前屏幕的高度。 |
| width | number | 否 | 否 | 输入法窗口的宽度，单位为px。该参数应为整数，最小值为0，最大值为当前屏幕的宽度。 |
| height | number | 否 | 否 | 输入法窗口的高度，单位为px。该参数应为整数，最小值为0，最大值为当前屏幕的高度。 |
| displayId23+ | number | 否 | 是 | 
输入法软键盘窗口所在的屏幕ID。

**模型约束：** 该参数仅可在Stage模型下使用。

 |

#### EnabledState15+

输入法启用状态。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| DISABLED | 0 | 未启用。 |
| BASIC\_MODE | 1 | 基础模式。 |
| FULL\_EXPERIENCE\_MODE | 2 | 完整体验模式。 |

#### RequestKeyboardReason15+

请求键盘输入的原因。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| NONE | 0 | 表示没有特定的原因触发键盘请求。 |
| MOUSE | 1 | 表示键盘请求是由鼠标操作触发的。 |
| TOUCH | 2 | 表示键盘请求是由触摸操作触发的。 |
| OTHER | 20 | 表示键盘请求是由其他原因触发的。 |

#### MessageHandler15+

自定义通信对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/AqyeFwjzSKqsd4JYb-MUNQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=4996C65D55E4A3B1793C13B59C604E7F62BCD877E051D9EBA067AF5D661F5FD0)

开发者可通过注册此对象来接收输入法应用发送的自定义通信数据，接收到自定义通信数据时会触发此对象中[onMessage](#onmessage15)回调函数。

此对象全局唯一，多次注册仅保留最后一次注册的对象及有效性，并触发上一个已注册对象的[onTerminated](#onterminated15)回调函数。

若取消注册全局已注册的对象时，会触发被取消对象中[onTerminated](#onterminated15)回调函数。

#### \[h2\]onMessage15+

onMessage(msgId: string, msgParam?: ArrayBuffer): void

接收输入法应用发送的自定义数据回调函数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/sml2lqoZSRGpxLifcW3Kog/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=21F80E2E919297F85F58F3FC7EA476CE2F7BC84BFA17973A8A790816DE91730F)

当已注册的MessageHandler接收到来自输入法应用发送的自定义通信数据时，会触发该回调函数。

msgId为必选参数，msgParam为可选参数。存在收到仅有msgId自定义数据的可能，需与数据发送方确认自定义数据。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| msgId | string | 是 | 接收到的自定义通信数据的标识符。 |
| msgParam | ArrayBuffer | 否 | 接收到的自定义通信数据的消息体。 |

**示例：**

```ts
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();

let messageHandler: inputMethod.MessageHandler = {
  onTerminated(): void {
    console.info('OnTerminated.');
  },
  onMessage(msgId: string, msgParam?: ArrayBuffer): void {
    console.info(`recv message, msg: ${msgId}, msgParam: ${JSON.stringify(msgParam)}`);
  }
};
inputMethodController.recvMessage(messageHandler);
```

#### \[h2\]onTerminated15+

onTerminated(): void

监听对象终止回调函数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/o5GxGK4rRfyMKQY_U-nQvQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=4BEAC82C9D5F121ADC3C0EAA7A358741882729F3CBB6B24B1328551B2595958D)

当应用注册新的MessageHandler对象时，会触发上一个已注册MessageHandler对象的OnTerminated回调函数。

当应用取消注册时，会触发当前已注册MessageHandler对象的OnTerminated回调函数。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**示例：**

```ts
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();

let messageHandler: inputMethod.MessageHandler = {
  onTerminated(): void {
    console.info('OnTerminated.');
  },
  onMessage(msgId: string, msgParam?: ArrayBuffer): void {
    console.info(`recv message, msg: ${msgId}, msgParam: ${JSON.stringify(msgParam)}`);
  }
};
inputMethodController.recvMessage(messageHandler);
```

#### SetPreviewTextCallback17+

type SetPreviewTextCallback = (text: string, range: Range) => void

当输入法框架需要显示预览文本时触发的回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| text | string | 是 | 预览文本内容。 |
| range | [Range](#range10) | 是 | 文本的选中范围。 |

#### AttachFailureReason22+

枚举，绑定失败的原因。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| CALLER\_NOT\_FOCUSED | 0 | 表示调用者非焦点窗口所属应用导致的失败。 |
| IME\_ABNORMAL | 1 | 表示输入法应用异常导致的失败。 |
| SERVICE\_ABNORMAL | 2 | 表示输入法框架服务异常导致的失败。 |

#### AttachOptions23+

绑定输入法的附加选项。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| requestKeyboardReason | [RequestKeyboardReason](#requestkeyboardreason15) | 否 | 是 | 请求键盘输入的原因。 |
| showKeyboard | boolean | 否 | 是 | 
绑定输入法成功后，是否拉起输入法键盘。

\- true表示拉起。

\- false表示不拉起。

 |

#### InputMethodController

下列API示例中都需使用[getController](#inputmethodgetcontroller9)获取到InputMethodController实例，再通过实例调用对应方法。

#### \[h2\]attach10+

attach(showKeyboard: boolean, textConfig: TextConfig, callback: AsyncCallback<void>): void

自绘控件绑定输入法。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/XjJJ_lPSQgySa0SlXpKcTA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=CE675C8F2E714457FA65AC96EE9F6C26A29879B343FDC1C27B451AA102D7ECF8)

需要先调用此接口，完成自绘控件与输入法的绑定，才能使用以下功能：显示/隐藏键盘、更新光标信息、更改编辑框选中范围、保存配置信息、监听处理由输入法应用发送的信息或命令等。

当自绘控件所在窗口通过[setWindowFocusable](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#setwindowfocusable9)设置为不可获焦窗口时，系统将无法保证自绘输入控件与输入法正常交互。若开发者希望在不可获焦窗口中绘制输入框，建议参考[不可获焦窗口中输入框与输入法交互指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-inputmethod-in-not-focusable-window)。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| showKeyboard | boolean | 是 | 
绑定输入法成功后，是否拉起输入法键盘。

\- true表示拉起。

\- false表示不拉起。

 |
| textConfig | [TextConfig](#textconfig10) | 是 | 编辑框的配置信息。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当绑定输入法成功后，err为undefined；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let inputAttribute: inputMethod.InputAttribute = {
  textInputType: inputMethod.TextInputType.TEXT,
  enterKeyType: inputMethod.EnterKeyType.GO
}
let textConfig: inputMethod.TextConfig = { inputAttribute: inputAttribute };
inputMethod.getController().attach(true, textConfig, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to attach, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in attaching the inputMethod.');
});
```

#### \[h2\]attach10+

attach(showKeyboard: boolean, textConfig: TextConfig): Promise<void>

自绘控件绑定输入法。使用promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/rpA-ucc2RNO-g8rsrblrLg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=97FDD27AC9C6B9D3D2F3749FF209FDA6E4123089ACD381CD5D1E70F50E3FBF8A)

需要先调用此接口，完成自绘控件与输入法的绑定，才能使用以下功能：显示/隐藏键盘、更新光标信息、更改编辑框选中范围、保存配置信息、监听处理由输入法应用发送的信息或命令等。

当自绘控件所在窗口通过[setWindowFocusable](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#setwindowfocusable9)设置为不可获焦窗口时，系统将无法保证自绘输入控件与输入法正常交互。若开发者希望在不可获焦窗口中绘制输入框，建议参考[不可获焦窗口中输入框与输入法交互指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-inputmethod-in-not-focusable-window)。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| showKeyboard | boolean | 是 | 
绑定输入法成功后，是否拉起输入法键盘。

\- true表示拉起。

\- false表示不拉起。

 |
| textConfig | [TextConfig](#textconfig10) | 是 | 编辑框的配置信息。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let inputAttribute: inputMethod.InputAttribute = {
  textInputType: inputMethod.TextInputType.TEXT,
  enterKeyType: inputMethod.EnterKeyType.GO
}
let textConfig: inputMethod.TextConfig = { inputAttribute: inputAttribute };
inputMethod.getController().attach(true, textConfig).then(() => {
  console.info('Succeeded in attaching inputMethod.');
}).catch((err: BusinessError) => {
  console.error(`Failed to attach, code: ${err.code}, message: ${err.message}`);
});
```

#### \[h2\]attach15+

attach(showKeyboard: boolean, textConfig: TextConfig, requestKeyboardReason: RequestKeyboardReason): Promise<void>

自绘控件绑定输入法。使用promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/dQTdLIASTlmPk7MeXZUOhA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=9C7B42DD6CABE635A1D78CDC441BDC36F0B4CB1621640FD27F8C3447BE1080D2)

需要先调用此接口，完成自绘控件与输入法的绑定，才能使用以下功能：显示/隐藏键盘、更新光标信息、更改编辑框选中范围、保存配置信息、监听处理由输入法应用发送的信息或命令等。

当自绘控件所在窗口通过[setWindowFocusable](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#setwindowfocusable9)设置为不可获焦窗口时，系统将无法保证自绘输入控件与输入法正常交互。若开发者希望在不可获焦窗口中绘制输入框，建议参考[不可获焦窗口中输入框与输入法交互指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-inputmethod-in-not-focusable-window)。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| showKeyboard | boolean | 是 | 
绑定输入法成功后，是否拉起输入法键盘。

\- true表示拉起。

\- false表示不拉起。

 |
| textConfig | [TextConfig](#textconfig10) | 是 | 编辑框的配置信息。 |
| requestKeyboardReason | [RequestKeyboardReason](#requestkeyboardreason15) | 是 | 请求键盘输入的原因。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)和[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let inputAttribute: inputMethod.InputAttribute = {
  textInputType: inputMethod.TextInputType.TEXT,
  enterKeyType: inputMethod.EnterKeyType.GO
}
let textConfig: inputMethod.TextConfig = { inputAttribute: inputAttribute };
let requestKeyboardReason: inputMethod.RequestKeyboardReason = inputMethod.RequestKeyboardReason.MOUSE;

inputMethod.getController().attach(true, textConfig, requestKeyboardReason).then(() => {
  console.info('Succeeded in attaching inputMethod.');
}).catch((err: BusinessError) => {
  console.error(`Failed to attach, code: ${err.code}, message: ${err.message}`);
});
```

#### \[h2\]attachWithUIContext23+

attachWithUIContext(uiContext: UIContext, textConfig: TextConfig, attachOptions?: AttachOptions): Promise<void>

自绘控件绑定输入法。使用promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/xcSoNDwITH24h1uwIsMf0g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=E88E7605AE5C2B447B36E88231901490A07FCA5EB400CD001BCBBFB10EE9002D)

需要先调用此接口，完成自绘控件与输入法的绑定，才能使用以下功能：显示/隐藏键盘、更新光标信息、更改编辑框选中范围、保存配置信息、监听处理由输入法应用发送的信息或命令等。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| uiContext | [UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext) | 是 | UIContext实例对象。 |
| textConfig | [TextConfig](#textconfig10) | 是 | 编辑框的配置信息。 |
| attachOptions | [AttachOptions](#attachoptions23) | 否 | 绑定附加选项。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12800003 | input method client error. Possible causes:1.the edit box is not focused. 2.no edit box is bound to current input method application.3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { UIContext } from '@kit.ArkUI';

let uiContext: UIContext | undefined = UIContext.getCallingScopeUIContext();
let inputAttribute: inputMethod.InputAttribute = {
  textInputType: inputMethod.TextInputType.TEXT,
  enterKeyType: inputMethod.EnterKeyType.GO
}
let textConfig: inputMethod.TextConfig = { inputAttribute: inputAttribute };
let attachOptions: inputMethod.AttachOptions = { showKeyboard: true };
inputMethod.getController().attachWithUIContext(uiContext, textConfig, attachOptions).then(() => {
  console.info('Succeeded in attaching inputMethod.');
}).catch((err: BusinessError) => {
  console.error(`Failed to attach, code: ${err.code}, message: ${err.message}`);
});
```

#### \[h2\]discardTypingText20+

discardTypingText(): Promise<void>

编辑框应用发送“清空正在输入的文字”命令到输入法。使用promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/hpWo_plUQU6A2XxA8cMpZg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=A735E079539EA822D0CC4277E9E844840CA9A24FDC9A50193EFB420FF2A0CFAD)

当编辑框应用与输入法绑定成功后，才可调用该接口实现此功能。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800009 | input method client detached. |
| 12800015 | the other side does not accept the request. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().discardTypingText().then(() => {
  console.info('Succeeded discardTypingText.');
}).catch((err: BusinessError) => {
  console.error(`Failed to discardTypingText, code: ${err.code}, message: ${err.message}`);
});
```

#### \[h2\]showTextInput10+

showTextInput(callback: AsyncCallback<void>): void

进入文本编辑状态。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/04O2kr5_QVGLny5RB5G0Rw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=C3F4DE63D4A4E37FB67A5FFAB6ED8CD506788D39D329099B799910433D95FFF5)

编辑框与输入法绑定成功后，可调用该接口拉起软键盘，进入文本编辑状态。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | 是 | 回调函数。若成功进入编辑状态，err为undefined；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800009 | input method client detached. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().showTextInput((err: BusinessError) => {
  if (err) {
    console.error(`Failed to showTextInput, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in showing the inputMethod.');
});
```

#### \[h2\]showTextInput10+

showTextInput(): Promise<void>

进入文本编辑状态。使用promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/aF_8iIuySSSt19i8k-eZ_Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=40D1B4F173032C5BE050917B7FA70ECC7A4C83639C283CE3AB0B3D2197E737C5)

编辑框与输入法绑定成功后，可调用该接口拉起软键盘，进入文本编辑状态。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800009 | input method client detached. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().showTextInput().then(() => {
  console.info('Succeeded in showing text input.');
}).catch((err: BusinessError) => {
  console.error(`Failed to showTextInput, code: ${err.code}, message: ${err.message}`);
});
```

#### \[h2\]showTextInput15+

showTextInput(requestKeyboardReason: RequestKeyboardReason): Promise<void>

进入文本编辑状态。使用promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/1ajWcMJMTFiAlr1tM4dAhg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=1AD496A6852E9F9D885740C7F4EB6D6B14D169558422B8E1EC58B78B2F9043CD)

编辑框与输入法绑定成功后，可调用该接口拉起软键盘，进入文本编辑状态。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| requestKeyboardReason | [RequestKeyboardReason](#requestkeyboardreason15) | 是 | 请求键盘输入的原因。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800009 | input method client detached. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let requestKeyboardReason: inputMethod.RequestKeyboardReason = inputMethod.RequestKeyboardReason.MOUSE;

inputMethod.getController().showTextInput(requestKeyboardReason).then(() => {
  console.info('Succeeded in showing text input.');
}).catch((err: BusinessError) => {
  console.error(`Failed to showTextInput, code: ${err.code}, message: ${err.message}`);
});
```

#### \[h2\]hideTextInput10+

hideTextInput(callback: AsyncCallback<void>): void

退出文本编辑状态。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/Xm_4dI0YSdGK91jAe5Adzw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=D8F8B82D6B16739C01B42D2D0C1B2BBC352561ED4ECB7C5FA16F5C8D04E76D74)

调用接口时，若软键盘处于显示状态，调用接口后软键盘会被隐藏。

调用该接口不会解除与输入法的绑定，再次调用[showTextInput](#showtextinput10)时，可重新进入文本编辑状态。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | 是 | 回调函数。当成功退出编辑状态时，err为undefined；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800009 | input method client detached. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().hideTextInput((err: BusinessError) => {
  if (err) {
    console.error(`Failed to hideTextInput, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in hiding text input.');
});
```

#### \[h2\]hideTextInput10+

hideTextInput(): Promise<void>

退出文本编辑状态。使用promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/S0Y_gVe9QOypenTu1sgf6w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=30A8D89CF6461A5CF3837E2AF1D744257E84336B08C102B9B35731E4BB5A3C72)

调用接口时，若软键盘处于显示状态，调用接口后软键盘会被隐藏。

调用该接口不会解除与输入法的绑定，再次调用[showTextInput](#showtextinput10)时，可重新进入文本编辑状态。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800009 | input method client detached. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().hideTextInput().then(() => {
  console.info('Succeeded in hiding inputMethod.');
}).catch((err: BusinessError) => {
  console.error(`Failed to hideTextInput, code: ${err.code}, message: ${err.message}`);
})
```

#### \[h2\]detach10+

detach(callback: AsyncCallback<void>): void

自绘控件解除与输入法的绑定。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | 是 | 回调函数。当解绑定输入法成功时，err为undefined；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().detach((err: BusinessError) => {
  if (err) {
    console.error(`Failed to detach, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in detaching inputMethod.');
});
```

#### \[h2\]detach10+

detach(): Promise<void>

自绘控件解除与输入法的绑定。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().detach().then(() => {
  console.info('Succeeded in detaching inputMethod.');
}).catch((err: BusinessError) => {
  console.error(`Failed to detach, code: ${err.code}, message: ${err.message}`);
});
```

#### \[h2\]setCallingWindow10+

setCallingWindow(windowId: number, callback: AsyncCallback<void>): void

设置要避让软键盘的窗口。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/UjJyngemSeCyafTTgKsg1g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=7B6B8FEA8F458FBE86E2A7E7E14F3B7A34937617D2F7D30F0817B08827C6E0AD)

将绑定到输入法的应用程序所在的窗口Id传入，此窗口可以避让输入法窗口。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| windowId | number | 是 | 绑定输入法应用的应用程序所在的窗口Id。该参数应为整数。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置成功时，err为undefined；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800009 | input method client detached. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let windowId: number = 2000;
inputMethod.getController().setCallingWindow(windowId, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to setCallingWindow, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in setting callingWindow.');
});
```

#### \[h2\]setCallingWindow10+

setCallingWindow(windowId: number): Promise<void>

设置要避让软键盘的窗口。使用promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/Li1GYDd2TM-425s-tPCjPg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=82DCCDA5D1C5D9DDB5136974BF122824750F08FE7DF26C10E48683A2D8E2F678)

将绑定到输入法的应用程序所在的窗口Id传入，此窗口可以避让输入法窗口。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| windowId | number | 是 | 绑定输入法应用的应用程序所在的窗口Id。该参数应为整数。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800009 | input method client detached. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let windowId: number = 2000;
inputMethod.getController().setCallingWindow(windowId).then(() => {
  console.info('Succeeded in setting callingWindow.');
}).catch((err: BusinessError) => {
  console.error(`Failed to setCallingWindow, code: ${err.code}, message: ${err.message}`);
})
```

#### \[h2\]updateCursor10+

updateCursor(cursorInfo: CursorInfo, callback: AsyncCallback<void>): void

当编辑框内的光标信息发生变化时，调用该接口使输入法感知到光标变化。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| cursorInfo | [CursorInfo](#cursorinfo10) | 是 | 光标信息。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当光标信息更新成功时，err为undefined；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800009 | input method client detached. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let cursorInfo: inputMethod.CursorInfo = {
  left: 0,
  top: 0,
  width: 600,
  height: 800
};
inputMethod.getController().updateCursor(cursorInfo, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to updateCursor, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in updating cursorInfo.');
});
```

#### \[h2\]updateCursor10+

updateCursor(cursorInfo: CursorInfo): Promise<void>

当编辑框内的光标信息发生变化时，调用该接口使输入法感知到光标变化。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| cursorInfo | [CursorInfo](#cursorinfo10) | 是 | 光标信息。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800009 | input method client detached. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let cursorInfo: inputMethod.CursorInfo = {
  left: 0,
  top: 0,
  width: 600,
  height: 800
};
inputMethod.getController().updateCursor(cursorInfo).then(() => {
  console.info('Succeeded in updating cursorInfo.');
}).catch((err: BusinessError) => {
  console.error(`Failed to updateCursor, code: ${err.code}, message: ${err.message}`);
});
```

#### \[h2\]changeSelection10+

changeSelection(text: string, start: number, end: number, callback: AsyncCallback<void>): void

当编辑框内被选中的文本信息内容或文本范围发生变化时，可调用该接口更新文本信息，使输入法应用感知到变化。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| text | string | 是 | 整个输入文本。 |
| start | number | 是 | 所选文本的起始位置。该参数应为大于或等于0的整数。 |
| end | number | 是 | 所选文本的结束位置。该参数应为大于或等于0的整数。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当文本信息更新成功时，err为undefined；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800009 | input method client detached. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().changeSelection('text', 0, 5, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to changeSelection, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in changing selection.');
});
```

#### \[h2\]changeSelection10+

changeSelection(text: string, start: number, end: number): Promise<void>

当编辑框内被选中的文本信息内容或文本范围发生变化时，可调用该接口更新文本信息，使输入法应用感知到变化。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| text | string | 是 | 整个输入文本。 |
| start | number | 是 | 所选文本的起始位置。该参数应为大于或等于0的整数。 |
| end | number | 是 | 所选文本的结束位置。该参数应为大于或等于0的整数。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800009 | input method client detached. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().changeSelection('test', 0, 5).then(() => {
  console.info('Succeeded in changing selection.');
}).catch((err: BusinessError) => {
  console.error(`Failed to changeSelection, code: ${err.code}, message: ${err.message}`);
});
```

#### \[h2\]updateAttribute10+

updateAttribute(attribute: InputAttribute, callback: AsyncCallback<void>): void

更新编辑框属性信息。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| attribute | [InputAttribute](#inputattribute10) | 是 | 编辑框属性对象。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当编辑框属性信息更新成功时，err为undefined；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800009 | input method client detached. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let inputAttribute: inputMethod.InputAttribute = { textInputType: 0, enterKeyType: 1 };
inputMethod.getController().updateAttribute(inputAttribute, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to updateAttribute, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in updating attribute.');
});
```

#### \[h2\]updateAttribute10+

updateAttribute(attribute: InputAttribute): Promise<void>

更新编辑框属性信息。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| attribute | [InputAttribute](#inputattribute10) | 是 | 编辑框属性对象。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800009 | input method client detached. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let inputAttribute: inputMethod.InputAttribute = { textInputType: 0, enterKeyType: 1 };
inputMethod.getController().updateAttribute(inputAttribute).then(() => {
  console.info('Succeeded in updating attribute.');
}).catch((err: BusinessError) => {
  console.error(`Failed to updateAttribute, code: ${err.code}, message: ${err.message}`);
});
```

#### \[h2\]stopInputSession9+

stopInputSession(callback: AsyncCallback<boolean>): void

结束输入会话。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/-UZh7x29S56h6WAslR6dpg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=92DD2F7E4AC42E6C4989CB5B46C43DD912D78B273737C6460A56B2A978CB6BDF)

该接口需要编辑框与输入法绑定时才能调用，即点击编辑控件后，才可调用该接口结束输入会话。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当结束输入会话成功时，err为undefined，data为true；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().stopInputSession((err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to stopInputSession, code: ${err.code}, message: ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in stopping inputSession.');
  } else {
    console.error('Failed to stopInputSession.');
  }
});
```

#### \[h2\]stopInputSession9+

stopInputSession(): Promise<boolean>

结束输入会话。使用promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/ct2kKnIdRZ-EQviCFiB6jw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=167E2DBEE6CC1CB1E88807488237689BE4424A023DD23401E5C7E532DE8F0C33)

该接口需要编辑框与输入法绑定时才能调用，即点击编辑控件后，才可调用该接口结束输入会话。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象。返回true表示结束输入会话成功，返回false表示结束输入会话失败。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().stopInputSession().then((result: boolean) => {
  if (result) {
    console.info('Succeeded in stopping inputSession.');
  } else {
    console.error('Failed to stopInputSession.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to stopInputSession, code: ${err.code}, message: ${err.message}`);
});
```

#### \[h2\]showSoftKeyboard9+

showSoftKeyboard(callback: AsyncCallback<void>): void

显示输入法软键盘。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/CJw0Td8USWuWBoHD7VsPrA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=C4DDAD3B240343B56032552590BC83D156F341950B27C1A555D74D6E6BC684DD)

该接口需要编辑框与输入法绑定时才能调用，即点击编辑控件后，才可调用显示当前输入法的软键盘。

**需要权限：** ohos.permission.CONNECT\_IME\_ABILITY，仅系统应用可用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | 是 | 回调函数。当软键盘显示成功。err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | permissions check fails. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().showSoftKeyboard((err: BusinessError) => {
  if (!err) {
    console.info('Succeeded in showing softKeyboard.');
  } else {
    console.error(`Failed to show softKeyboard, ${err.code}, message: ${err.message}`);
  }
});
```

#### \[h2\]showSoftKeyboard9+

showSoftKeyboard(): Promise<void>

显示输入法软键盘。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/73V2CwqPSCOrfJrH0uOvyQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=E96E4E3C9E43BD6590CE5F9A302CB6FC5821ACF1B3B4B1806F50870BDDAB8033)

该接口需要编辑框与输入法绑定时才能调用，即点击编辑控件后，才可调用显示当前输入法的软键盘。

**需要权限：** ohos.permission.CONNECT\_IME\_ABILITY，仅系统应用可用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | permissions check fails. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().showSoftKeyboard().then(() => {
  console.info('Succeeded in showing softKeyboard.');
}).catch((err: BusinessError) => {
  console.error(`Failed to show softKeyboard, code: ${err.code}, message: ${err.message}`);
});
```

#### \[h2\]hideSoftKeyboard9+

hideSoftKeyboard(callback: AsyncCallback<void>): void

隐藏输入法软键盘。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/dBmQLbq1TrG8KRmwT_Z-hg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=FC97A1E416EDA2CB4D5CED5CFA31FFD6483F15580F51A1DEDE49413EAB6781BE)

该接口需要编辑框与输入法绑定时才能调用，即点击编辑控件后，才可调用隐藏当前输入法的软键盘。

**需要权限：** ohos.permission.CONNECT\_IME\_ABILITY，仅系统应用可用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | 是 | 回调函数。当软键盘隐藏成功。err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | permissions check fails. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().hideSoftKeyboard((err: BusinessError) => {
  if (!err) {
    console.info('Succeeded in hiding softKeyboard.');
  } else {
    console.error(`Failed to hide softKeyboard, code: ${err.code}, message: ${err.message}`);
  }
})
```

#### \[h2\]hideSoftKeyboard9+

hideSoftKeyboard(): Promise<void>

隐藏输入法软键盘。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/_NuBp_tHQFauSyE_kjZz0Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=922DB76B47294A7DCB92491FC79E4B4BCEFDEF630C01FED854364177347A8F60)

该接口需要编辑框与输入法绑定时才能调用，即点击编辑控件后，才可调用隐藏当前输入法的软键盘。

**需要权限：** ohos.permission.CONNECT\_IME\_ABILITY，仅系统应用可用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | permissions check fails. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().hideSoftKeyboard().then(() => {
  console.info('Succeeded in hiding softKeyboard.');
}).catch((err: BusinessError) => {
  console.error(`Failed to hide softKeyboard, code: ${err.code}, message: ${err.message}`);
});
```

#### \[h2\]sendMessage15+

sendMessage(msgId: string, msgParam?: ArrayBuffer): Promise<void>

发送自定义通信至输入法应用。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/NqvV84WbT1m6MwasVE3FGA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=4053AE1E27EC373B9B072AD50F5DCF31ED47AD802427D2747560F292D7866BDA)

该接口需要编辑框与输入法绑定并进入编辑状态，且输入法应用处于完整体验模式时才能调用。

msgId最大限制256B，msgParam最大限制128KB。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| msgId | string | 是 | 需要发送至输入法应用的自定义数据的标识符。 |
| msgParam | ArrayBuffer | 否 | 需要发送至输入法应用的自定义数据的消息体。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Incorrect parameter types. 2. Incorrect parameter length. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800009 | input method client detached. |
| 12800014 | the input method is in basic mode. |
| 12800015 | the other side does not accept the request. |
| 12800016 | input method client is not editable. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let msgId: string = "testMsgId";
let msgParam: ArrayBuffer = new ArrayBuffer(128);
inputMethod.getController().sendMessage(msgId, msgParam).then(() => {
  console.info('Succeeded send message.');
}).catch((err: BusinessError) => {
  console.error(`Failed to send message, code: ${err.code}, message: ${err.message}`);
});
```

#### \[h2\]recvMessage15+

recvMessage(msgHandler?: MessageHandler): void

注册或取消注册MessageHandler。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/geVrMwvuQl6eS842ol1LyA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=A87F118010AC21C6EF49CCAC05C9FFC1911836FF2C6E7BED9C4AA8FD6CD11271)

[MessageHandler](#messagehandler15)对象全局唯一，多次注册仅保留最后一次注册的对象及有效性，并触发上一个已注册对象的[onTerminated](#onterminated15)回调函数。

未填写参数，则取消全局已注册的[MessageHandler](#messagehandler15)，并触发被取消注册对象中[onTerminated](#onterminated15)回调函数。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| msgHandler | [MessageHandler](#messagehandler15) | 否 | 
该对象通过[onMessage](#onmessage15)接收来自输入法应用所发送的自定义通信数据，并通过[onTerminated](#onterminated15)接收终止此对象订阅的消息。

若不填写此参数，则取消全局已注册的[MessageHandler](#messagehandler15)对象，同时触发其[onTerminated](#onterminated15)回调函数。

 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Incorrect parameter types. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let messageHandler: inputMethod.MessageHandler = {
  onTerminated(): void {
    console.info('OnTerminated.');
  },
  onMessage(msgId: string, msgParam?: ArrayBuffer): void {
    console.info('recv message.');
  }
};
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.recvMessage(messageHandler);
// 取消已注册的MessageHandler
inputMethodController.recvMessage();
```

#### \[h2\]stopInput(deprecated)

stopInput(callback: AsyncCallback<boolean>): void

结束输入会话。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/7udlAixUTM6A21gvv8gGdQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=1E36C7A518AAEEBF84FD89A2EC182214365A35865ED5CD76D2D964E198455F1F)

该接口需要编辑框与输入法绑定时才能调用，即点击编辑控件后，才可调用该接口结束输入会话。

从API version 6开始支持，从API version 9开始废弃，建议使用[stopInputSession](#stopinputsession9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当会话结束成功，err为undefined，data为true；否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().stopInput((err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to stopInput, code: ${err.code}, message: ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in stopping input.');
  } else {
    console.error('Failed to stopInput.');
  }
});
```

#### \[h2\]stopInput(deprecated)

stopInput(): Promise<boolean>

结束输入会话。使用promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/ppkcLR2ZSpOQ1zMox-UQvA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=E28B050B8953B1C27E0837F971F170353F3464A0FD368E471F9354108503567C)

该接口需要编辑框与输入法绑定时才能调用，即点击编辑控件后，才可调用该接口结束输入会话。

从API version 6开始支持，从API version 9开始废弃，建议使用[stopInputSession](#stopinputsession9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象。返回true表示会话结束成功；返回false表示会话结束失败。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().stopInput().then((result: boolean) => {
  if (result) {
    console.info('Succeeded in stopping input.');
  } else {
    console.error('Failed to stopInput.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to stopInput, code: ${err.code}, message: ${err.message}`);
})
```

#### \[h2\]on('insertText')10+

on(type: 'insertText', callback: (text: string) => void): void

订阅输入法应用插入文本事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'insertText'。 |
| callback | (text: string) => void | 是 | 
回调函数，返回需要插入的文本内容。

根据传入的文本，在回调函数中操作编辑框中的内容。

 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800009 | input method client detached. |

**示例：**

```ts
function callback1(text: string): void {
  console.info(`Succeeded in getting callback1, data: ${text}`);
}

function callback2(text: string): void {
  console.info(`Succeeded in getting callback2, data: ${text}`);
}

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
// 注册回调
inputMethodController.on('insertText', callback1);
inputMethodController.on('insertText', callback2);
// 仅取消insertText的callback1的回调
inputMethodController.off('insertText', callback1);
// 取消insertText的所有回调
inputMethodController.off('insertText');
```

#### \[h2\]off('insertText')10+

off(type: 'insertText', callback?: (text: string) => void): void

取消订阅输入法应用插入文本事件。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'insertText'。 |
| callback | (text: string) => void | 否 | 
取消订阅的回调函数，需要与on接口传入的保持一致。

参数不填写时，取消订阅type对应的所有回调事件。

 |

**示例：**

```ts
import { Callback } from '@kit.BasicServicesKit';

let onInsertTextCallback: Callback<string> = (text: string): void => {
  console.info(`Succeeded in subscribing insertText: ${text}`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('insertText', onInsertTextCallback);
inputMethodController.off('insertText');
```

#### \[h2\]on('deleteLeft')10+

on(type: 'deleteLeft', callback: (length: number) => void): void

订阅输入法应用向左删除文本事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'deleteLeft'。 |
| callback | (length: number) => void | 是 | 
回调函数，返回需要向左删除的文本长度。

根据传入的删除长度，在回调函数中操作编辑框中的文本。

 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800009 | input method client detached. |

**示例：**

```ts
inputMethod.getController().on('deleteLeft', (length: number) => {
  console.info(`Succeeded in subscribing deleteLeft, length: ${length}`);
});
```

#### \[h2\]off('deleteLeft')10+

off(type: 'deleteLeft', callback?: (length: number) => void): void

取消订阅输入法应用向左删除文本事件。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听，固定取值为'deleteLeft'。 |
| callback | (length: number) => void | 否 | 
取消订阅的回调函数，需要与on接口传入的保持一致。

参数不填写时，取消订阅type对应的所有回调事件。

 |

**示例：**

```ts
import { Callback } from '@kit.BasicServicesKit';

let onDeleteLeftCallback: Callback<number> = (length: number): void => {
  console.info(`Succeeded in subscribing deleteLeft, length: ${length}`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('deleteLeft', onDeleteLeftCallback);
inputMethodController.off('deleteLeft');
```

#### \[h2\]on('deleteRight')10+

on(type: 'deleteRight', callback: (length: number) => void): void

订阅输入法应用向右删除文本事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'deleteRight'。 |
| callback | (length: number) => void | 是 | 
回调函数，返回需要向右删除的文本长度。

根据传入的删除长度，在回调函数中操作编辑框中的文本。

 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800009 | input method client detached. |

**示例：**

```ts
inputMethod.getController().on('deleteRight', (length: number) => {
  console.info(`Succeeded in subscribing deleteRight, length: ${length}`);
});
```

#### \[h2\]off('deleteRight')10+

off(type: 'deleteRight', callback?: (length: number) => void): void

取消订阅输入法应用向右删除文本事件。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为deleteRight。 |
| callback | (length: number) => void | 否 | 
取消订阅的回调函数，需要与on接口传入的保持一致。

参数不填写时，取消订阅type对应的所有回调事件。

 |

**示例：**

```ts
import { Callback } from '@kit.BasicServicesKit';

let onDeleteRightCallback: Callback<number> = (length: number): void => {
  console.info(`Succeeded in subscribing deleteRight, length: ${length}`);
};
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('deleteRight', onDeleteRightCallback);
inputMethodController.off('deleteRight');
```

#### \[h2\]on('sendKeyboardStatus')10+

on(type: 'sendKeyboardStatus', callback: (keyboardStatus: KeyboardStatus) => void): void

订阅输入法应用发送输入法软键盘状态事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'sendKeyboardStatus'。 |
| callback | (keyboardStatus: [KeyboardStatus](#keyboardstatus10)) => void | 是 | 
回调函数，返回软键盘状态。

根据传入的软键盘状态，在回调函数中做相应操作。

 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800009 | input method client detached. |

**示例：**

```ts
inputMethod.getController().on('sendKeyboardStatus', (keyboardStatus: inputMethod.KeyboardStatus) => {
  console.info(`Succeeded in subscribing sendKeyboardStatus, keyboardStatus: ${keyboardStatus}`);
});
```

#### \[h2\]off('sendKeyboardStatus')10+

off(type: 'sendKeyboardStatus', callback?: (keyboardStatus: KeyboardStatus) => void): void

取消订阅输入法应用发送输入法软键盘状态事件。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'sendKeyboardStatus'。 |
| callback | (keyboardStatus: [KeyboardStatus](#keyboardstatus10)) => void | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```ts
import { Callback } from '@kit.BasicServicesKit';

let onSendKeyboardStatus: Callback<inputMethod.KeyboardStatus> = (keyboardStatus: inputMethod.KeyboardStatus): void => {
  console.info(`Succeeded in subscribing sendKeyboardStatus, keyboardStatus: ${keyboardStatus}`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('sendKeyboardStatus', onSendKeyboardStatus);
inputMethodController.off('sendKeyboardStatus');
```

#### \[h2\]on('sendFunctionKey')10+

on(type: 'sendFunctionKey', callback: (functionKey: FunctionKey) => void): void

订阅输入法应用发送功能键事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'sendFunctionKey'。 |
| callback | (functionKey: [FunctionKey](#functionkey10)) => void | 是 | 
回调函数，返回输入法应用发送的功能键信息。

根据返回的功能键信息，做相应操作。

 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800009 | input method client detached. |

**示例：**

```ts
inputMethod.getController().on('sendFunctionKey', (functionKey: inputMethod.FunctionKey) => {
  console.info(`Succeeded in subscribing sendFunctionKey, functionKey.enterKeyType: ${functionKey.enterKeyType}`);
});
```

#### \[h2\]off('sendFunctionKey')10+

off(type: 'sendFunctionKey', callback?: (functionKey: FunctionKey) => void): void

取消订阅输入法应用发送功能键事件。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'sendFunctionKey'。 |
| callback | (functionKey: [FunctionKey](#functionkey10)) => void | 否 | 
取消订阅的回调函数，需要与on接口传入的保持一致。

参数不填写时，取消订阅type对应的所有回调事件。

 |

**示例：**

```ts
import { Callback } from '@kit.BasicServicesKit';

let onSendFunctionKey: Callback<inputMethod.FunctionKey> = (functionKey: inputMethod.FunctionKey): void => {
  console.info(`Succeeded in subscribing sendFunctionKey, functionKey: ${functionKey.enterKeyType}`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('sendFunctionKey', onSendFunctionKey);
inputMethodController.off('sendFunctionKey');
```

#### \[h2\]on('moveCursor')10+

on(type: 'moveCursor', callback: (direction: Direction) => void): void

订阅输入法应用移动光标事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'moveCursor'。 |
| callback | (direction: [Direction](#direction10)) => void | 是 | 
回调函数，返回光标信息。

根据返回的光标移动方向，改变光标位置，如光标向上或向下。

 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800009 | input method client detached. |

**示例：**

```ts
inputMethod.getController().on('moveCursor', (direction: inputMethod.Direction) => {
  console.info(`Succeeded in subscribing moveCursor, direction: ${direction}`);
});
```

#### \[h2\]off('moveCursor')10+

off(type: 'moveCursor', callback?: (direction: Direction) => void): void

取消订阅输入法应用移动光标事件。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'moveCursor'。 |
| callback | (direction: [Direction](#direction10)) => void | 否 | 
取消订阅的回调函数，需要与on接口传入的保持一致。

参数不填写时，取消订阅type对应的所有回调事件。

 |

**示例：**

```ts
import { Callback } from '@kit.BasicServicesKit';

let onMoveCursorCallback: Callback<inputMethod.Direction> = (direction: inputMethod.Direction): void => {
  console.info(`Succeeded in subscribing moveCursor, direction: ${direction}`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('moveCursor', onMoveCursorCallback);
inputMethodController.off('moveCursor');
```

#### \[h2\]on('handleExtendAction')10+

on(type: 'handleExtendAction', callback: (action: ExtendAction) => void): void

订阅输入法应用发送扩展编辑操作事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'handleExtendAction'。 |
| callback | (action: [ExtendAction](#extendaction10)) => void | 是 | 
回调函数，返回扩展编辑操作类型。

根据传入的扩展编辑操作类型，做相应的操作，如剪切、复制等。

 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800009 | input method client detached. |

**示例：**

```ts
inputMethod.getController().on('handleExtendAction', (action: inputMethod.ExtendAction) => {
  console.info(`Succeeded in subscribing handleExtendAction, action: ${action}`);
});
```

#### \[h2\]off('handleExtendAction')10+

off(type: 'handleExtendAction', callback?: (action: ExtendAction) => void): void

取消订阅输入法应用发送扩展编辑操作事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'handleExtendAction'。 |
| callback | (action: [ExtendAction](#extendaction10)) => void | 否 | 
取消订阅的回调函数，需要与on接口传入的保持一致。

参数不填写时，取消订阅type对应的所有回调事件。

 |

**示例：**

```ts
import { Callback } from '@kit.BasicServicesKit';

let onHandleExtendActionCallback: Callback<inputMethod.ExtendAction> = (action: inputMethod.ExtendAction): void => {
  console.info(`Succeeded in subscribing handleExtendAction, action: ${action}`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('handleExtendAction', onHandleExtendActionCallback);
inputMethodController.off('handleExtendAction');
```

#### \[h2\]on('selectByRange')10+

on(type: 'selectByRange', callback: Callback<Range>): void

订阅输入法应用按范围选中文本事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'selectByRange'。 |
| callback | Callback<[Range](#range10)\> | 是 | 
回调函数，返回需要选中的文本范围。

根据传入的文本范围，开发者在回调函数中编辑框中相应文本。

 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
inputMethod.getController().on('selectByRange', (range: inputMethod.Range) => {
  console.info(`Succeeded in subscribing selectByRange: start: ${range.start} , end: ${range.end}`);
});
```

#### \[h2\]off('selectByRange')10+

off(type: 'selectByRange', callback?: Callback<Range>): void

取消订阅输入法应用按范围选中文本事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'selectByRange'。 |
| callback | Callback<[Range](#range10)\> | 否 | 
取消订阅的回调函数，需要与on接口传入的保持一致。

参数不填写时，取消订阅type对应的所有回调事件。

 |

**示例：**

```ts
import { Callback } from '@kit.BasicServicesKit';

let onSelectByRangeCallback: Callback<inputMethod.Range> = (range: inputMethod.Range): void => {
  console.info(`Succeeded in subscribing selectByRange, start: ${range.start} , end: ${range.end}`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('selectByRange', onSelectByRangeCallback);
inputMethodController.off('selectByRange');
```

#### \[h2\]on('selectByMovement')10+

on(type: 'selectByMovement', callback: Callback<Movement>): void

订阅输入法应用按光标移动方向，选中文本事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'selectByMovement'。 |
| callback | Callback<[Movement](#movement10)\> | 是 | 
回调函数，返回光标移动的方向。

根据传入的光标移动方向，选中编辑框中相应文本。

 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
inputMethod.getController().on('selectByMovement', (movement: inputMethod.Movement) => {
  console.info('Succeeded in subscribing selectByMovement: direction: ' + movement.direction);
});
```

#### \[h2\]off('selectByMovement')10+

off(type: 'selectByMovement', callback?: Callback<Movement>): void

取消订阅输入法应用按光标移动方向，选中文本事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'selectByMovement'。 |
| callback | Callback<[Movement](#movement10)\> | 否 | 
取消订阅的回调函数，需要与on接口传入的保持一致。

参数不填写时，取消订阅type对应的所有回调事件。

 |

**示例：**

```ts
import { Callback } from '@kit.BasicServicesKit';

let onSelectByMovementCallback: Callback<inputMethod.Movement> = (movement: inputMethod.Movement): void => {
  console.info(`Succeeded in subscribing selectByMovement, movement.direction: ${movement.direction}`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('selectByMovement', onSelectByMovementCallback);
inputMethodController.off('selectByMovement');
```

#### \[h2\]on('getLeftTextOfCursor')10+

on(type: 'getLeftTextOfCursor', callback: (length: number) => string): void

订阅输入法应用获取光标左侧指定长度文本事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'getLeftTextOfCursor'。 |
| callback | (length: number) => string | 是 | 回调函数，获取编辑框最新状态下光标左侧指定长度的文本内容并返回。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800009 | input method client detached. |

**示例：**

```ts
inputMethod.getController().on('getLeftTextOfCursor', (length: number) => {
  console.info(`Succeeded in subscribing getLeftTextOfCursor, length: ${length}`);
  let text: string = "";
  return text;
});
```

#### \[h2\]off('getLeftTextOfCursor')10+

off(type: 'getLeftTextOfCursor', callback?: (length: number) => string): void

取消订阅输入法应用获取光标左侧指定长度文本事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'getLeftTextOfCursor'。 |
| callback | (length: number) => string | 否 | 
取消订阅的回调函数，需要与on接口传入的保持一致。

参数不填写时，取消订阅type对应的所有回调事件。

 |

**示例：**

```ts
let getLeftTextOfCursorCallback: (length: number) => string = (length: number): string => {
  console.info(`Succeeded in unsubscribing getLeftTextOfCursor, length: ${length}`);
  let text: string = "";
  return text;
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('getLeftTextOfCursor', getLeftTextOfCursorCallback);
inputMethodController.off('getLeftTextOfCursor');
```

#### \[h2\]on('getRightTextOfCursor')10+

on(type: 'getRightTextOfCursor', callback: (length: number) => string): void

订阅输入法应用获取光标右侧指定长度文本事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'getRightTextOfCursor'。 |
| callback | (length: number) => string | 是 | 回调函数，获取编辑框最新状态下光标右侧指定长度的文本内容并返回。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800009 | input method client detached. |

**示例：**

```ts
inputMethod.getController().on('getRightTextOfCursor', (length: number) => {
  console.info(`Succeeded in subscribing getRightTextOfCursor, length: ${length}`);
  let text: string = "";
  return text;
});
```

#### \[h2\]off('getRightTextOfCursor')10+

off(type: 'getRightTextOfCursor', callback?: (length: number) => string): void

取消订阅输入法应用获取光标右侧指定长度文本事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'getRightTextOfCursor'。 |
| callback | (length: number) => string | 否 | 
取消订阅的回调函数，需要与on接口传入的保持一致。

参数不填写时，取消订阅type对应的所有回调事件。

 |

**示例：**

```ts
let getRightTextOfCursorCallback: (length: number) => string = (length: number): string => {
  console.info(`Succeeded in unsubscribing getRightTextOfCursor, length: ${length}`);
  let text: string = "";
  return text;
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('getRightTextOfCursor', getRightTextOfCursorCallback);
inputMethodController.off('getRightTextOfCursor');
```

#### \[h2\]on('getTextIndexAtCursor')10+

on(type: 'getTextIndexAtCursor', callback: () => number): void

订阅输入法应用获取光标处文本索引事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'getTextIndexAtCursor'。 |
| callback | () => number | 是 | 回调函数，获取编辑框最新状态下光标处文本索引并返回。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800009 | input method client detached. |

**示例：**

```ts
inputMethod.getController().on('getTextIndexAtCursor', () => {
  console.info(`Succeeded in subscribing getTextIndexAtCursor.`);
  let index: number = 0;
  return index;
});
```

#### \[h2\]off('getTextIndexAtCursor')10+

off(type: 'getTextIndexAtCursor', callback?: () => number): void

取消订阅输入法应用获取光标处文本索引事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'getTextIndexAtCursor'。 |
| callback | () => number | 否 | 
取消订阅的回调函数，需要与on接口传入的保持一致。

参数不填写时，取消订阅type对应的所有回调事件。

 |

**示例：**

```ts
let getTextIndexAtCursorCallback: () => number = (): number => {
  console.info(`Succeeded in unsubscribing getTextIndexAtCursor.`);
  let index: number = 0;
  return index;
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('getTextIndexAtCursor', getTextIndexAtCursorCallback);
inputMethodController.off('getTextIndexAtCursor');
```

#### \[h2\]on('setPreviewText')17+

on(type: 'setPreviewText', callback: SetPreviewTextCallback): void

订阅输入法应用操作文本预览内容的事件。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/JzvThxb4QXuXwjKxLFGbuQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=C92FAC88E0340C6D1506B9D8FFA49EF08BB8822D5F13BD81A38A761B10C39088)

使用预览文本功能，需在调用[attach](#attach10)前订阅此事件，并和[on('finishTextPreview')](#onfinishtextpreview17)一起订阅。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'setPreviewText'。 |
| callback | [SetPreviewTextCallback](#setpreviewtextcallback17) | 是 | 回调函数。用于接收文本预览的内容并返回。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
let setPreviewTextCallback1: inputMethod.SetPreviewTextCallback = (text: string, range: inputMethod.Range): void => {
  console.info(`SetPreviewTextCallback1: Received text - ${text}, Received range - start: ${range.start}, end: ${range.end}`);
};

let setPreviewTextCallback2: inputMethod.SetPreviewTextCallback = (text: string, range: inputMethod.Range): void => {
  console.info(`setPreviewTextCallback2: Received text - ${text}, Received range - start: ${range.start}, end: ${range.end}`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.on('setPreviewText', setPreviewTextCallback1);
console.info(`SetPreviewTextCallback1 subscribed to setPreviewText`);
inputMethodController.on('setPreviewText', setPreviewTextCallback2);
console.info(`SetPreviewTextCallback2 subscribed to setPreviewText`);
// 仅取消setPreviewText的callback1的回调。
inputMethodController.off('setPreviewText', setPreviewTextCallback1);
console.info(`SetPreviewTextCallback1 unsubscribed from setPreviewText`);
// 取消setPreviewText的所有回调。
inputMethodController.off('setPreviewText');
console.info(`All callbacks unsubscribed from setPreviewText`);
```

#### \[h2\]off('setPreviewText')17+

off(type: 'setPreviewText', callback?: SetPreviewTextCallback): void

取消订阅输入法应用操作文本预览内容的事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'setPreviewText'。 |
| callback | [SetPreviewTextCallback](#setpreviewtextcallback17) | 否 | 
取消订阅的回调函数，需要与on接口传入的保持一致。

参数不填写时，取消订阅type对应的所有回调事件。

 |

**示例：**

```ts
let setPreviewTextCallback1: inputMethod.SetPreviewTextCallback = (text: string, range: inputMethod.Range): void => {
  console.info(`SetPreviewTextCallback1: Received text - ${text}, Received range - start: ${range.start}, end: ${range.end}`);
};

let setPreviewTextCallback2: inputMethod.SetPreviewTextCallback = (text: string, range: inputMethod.Range): void => {
  console.info(`setPreviewTextCallback2: Received text - ${text}, Received range - start: ${range.start}, end: ${range.end}`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.on('setPreviewText', setPreviewTextCallback1);
console.info(`SetPreviewTextCallback1 subscribed to setPreviewText`);
inputMethodController.on('setPreviewText', setPreviewTextCallback2);
console.info(`SetPreviewTextCallback2 subscribed to setPreviewText`);
// 仅取消setPreviewText的callback1的回调。
inputMethodController.off('setPreviewText', setPreviewTextCallback1);
console.info(`SetPreviewTextCallback1 unsubscribed from setPreviewText`);
// 取消setPreviewText的所有回调。
inputMethodController.off('setPreviewText');
console.info(`All callbacks unsubscribed from setPreviewText`);
```

#### \[h2\]on('finishTextPreview')17+

on(type: 'finishTextPreview', callback: Callback<void>): void

订阅结束文本预览事件。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/FNKl3NgPR9en3ah5lbku9g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=FF5546F478FF094E8AF7C73C31A5563C2DD8FA6CB0BF9EA2E5D352A96FB0F738)

使用预览文本功能，需在调用[attach](#attach10)前订阅此事件，并和[on('setPreviewText')](#onsetpreviewtext17)一起订阅。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'finishTextPreview'。 |
| callback | Callback<void> | 是 | 回调函数。用于处理预览文本结束的逻辑，类型为void。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { Callback } from '@kit.BasicServicesKit';

let finishTextPreviewCallback1: Callback<void> = (): void => {
  console.info(`FinishTextPreviewCallback1: finishTextPreview event triggered`);
};
let finishTextPreviewCallback2: Callback<void> = (): void => {
  console.info(`FinishTextPreviewCallback2: finishTextPreview event triggered`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.on('finishTextPreview', finishTextPreviewCallback1);
console.info(`FinishTextPreviewCallback1 subscribed to finishTextPreview`);
inputMethodController.on('finishTextPreview', finishTextPreviewCallback2);
console.info(`FinishTextPreviewCallback2 subscribed to finishTextPreview`);
// 仅取消finishTextPreview的callback1的回调。
inputMethodController.off('finishTextPreview', finishTextPreviewCallback1);
console.info(`FinishTextPreviewCallback1 unsubscribed from finishTextPreview`);
// 取消finishTextPreview的所有回调。
inputMethodController.off('finishTextPreview');
console.info(`All callbacks unsubscribed from finishTextPreview`);
```

#### \[h2\]off('finishTextPreview')17+

off(type: 'finishTextPreview', callback?: Callback<void>): void

取消订阅结束文本预览事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'finishTextPreview'。 |
| callback | Callback<void> | 否 | 
取消订阅的回调函数，需要与on接口传入的保持一致。

参数不填写时，取消订阅type对应的所有回调事件。

 |

**示例：**

```ts
import { Callback } from '@kit.BasicServicesKit';

let finishTextPreviewCallback1: Callback<void> = (): void => {
  console.info(`FinishTextPreviewCallback1: finishTextPreview event triggered`);
};
let finishTextPreviewCallback2: Callback<void> = (): void => {
  console.info(`FinishTextPreviewCallback2: finishTextPreview event triggered`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.on('finishTextPreview', finishTextPreviewCallback1);
console.info(`FinishTextPreviewCallback1 subscribed to finishTextPreview`);
inputMethodController.on('finishTextPreview', finishTextPreviewCallback2);
console.info(`FinishTextPreviewCallback2 subscribed to finishTextPreview`);
// 仅取消finishTextPreview的callback1的回调。
inputMethodController.off('finishTextPreview', finishTextPreviewCallback1);
console.info(`FinishTextPreviewCallback1 unsubscribed from finishTextPreview`);
// 取消finishTextPreview的所有回调。
inputMethodController.off('finishTextPreview');
console.info(`All callbacks unsubscribed from finishTextPreview`);
```

#### InputMethodSetting8+

下列API均需使用[getSetting](#inputmethodgetsetting9)获取到InputMethodSetting实例后，通过实例调用。

#### \[h2\]on('imeChange')9+

on(type: 'imeChange', callback: (inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype) => void): void

订阅输入法及子类型变化监听事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'imeChange'。 |
| callback | (inputMethodProperty: [InputMethodProperty](#inputmethodproperty8), inputMethodSubtype: [InputMethodSubtype](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod-subtype#inputmethodsubtype)) => void | 是 | 回调函数，返回输入法属性对象及子类型对象。 |

**示例：**

```ts
import { InputMethodSubtype } from '@kit.IMEKit';

inputMethod.getSetting()
  .on('imeChange', (inputMethodProperty: inputMethod.InputMethodProperty, inputMethodSubtype: InputMethodSubtype) => {
    console.info(`Succeeded in subscribing imeChange: inputMethodProperty.name: ${inputMethodProperty.name} ` +
      `, inputMethodSubtype.id: ${inputMethodSubtype.id}`);
  });
```

#### \[h2\]off('imeChange')9+

off(type: 'imeChange', callback?: (inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype) => void): void

取消订阅输入法及子类型变化监听事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'imeChange'。 |
| callback | (inputMethodProperty: [InputMethodProperty](#inputmethodproperty8), inputMethodSubtype: [InputMethodSubtype](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod-subtype#inputmethodsubtype)) => void | 否 | 回调函数，返回取消订阅的输入法属性对象及子类型对象。 |

**示例：**

```ts
inputMethod.getSetting().off('imeChange');
```

#### \[h2\]listInputMethodSubtype9+

listInputMethodSubtype(inputMethodProperty: InputMethodProperty, callback: AsyncCallback<Array<InputMethodSubtype>>): void

获取指定输入法应用的所有子类型。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| inputMethodProperty | [InputMethodProperty](#inputmethodproperty8) | 是 | 输入法应用。 |
| callback | AsyncCallback<Array<[InputMethodSubtype](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod-subtype#inputmethodsubtype)\>> | 是 | 回调函数，返回指定输入法应用的所有子类型。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800001 | bundle manager error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```ts
import { InputMethodSubtype } from '@kit.IMEKit';
import { BusinessError } from '@kit.BasicServicesKit';

let inputMethodProperty: inputMethod.InputMethodProperty = {
  name: 'com.example.keyboard',
  id: 'propertyId',
  packageName: 'com.example.keyboard',
  methodId: 'propertyId',
}
let inputMethodSetting: inputMethod.InputMethodSetting = inputMethod.getSetting();

inputMethodSetting.listInputMethodSubtype(inputMethodProperty,
  (err: BusinessError, data: Array<InputMethodSubtype>) => {
    if (err) {
      console.error(`Failed to listInputMethodSubtype, code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in listing inputMethodSubtype.');
  });
```

#### \[h2\]listInputMethodSubtype9+

listInputMethodSubtype(inputMethodProperty: InputMethodProperty): Promise<Array<InputMethodSubtype>>

获取指定输入法应用的所有子类型。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| inputMethodProperty | [InputMethodProperty](#inputmethodproperty8) | 是 | 输入法应用。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<[InputMethodSubtype](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod-subtype#inputmethodsubtype)\>> | Promise对象，返回指定输入法应用的所有子类型。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800001 | bundle manager error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```ts
import { InputMethodSubtype } from '@kit.IMEKit';
import { BusinessError } from '@kit.BasicServicesKit';

let inputMethodProperty: inputMethod.InputMethodProperty = {
  name: 'com.example.keyboard',
  id: 'propertyId',
  packageName: 'com.example.keyboard',
  methodId: 'propertyId',
}
let inputMethodSetting: inputMethod.InputMethodSetting = inputMethod.getSetting();

inputMethodSetting.listInputMethodSubtype(inputMethodProperty).then((data: Array<InputMethodSubtype>) => {
  console.info('Succeeded in listing inputMethodSubtype.');
}).catch((err: BusinessError) => {
  console.error(`Failed to listInputMethodSubtype, code: ${err.code}, message: ${err.message}`);
})
```

#### \[h2\]listCurrentInputMethodSubtype9+

listCurrentInputMethodSubtype(callback: AsyncCallback<Array<InputMethodSubtype>>): void

查询当前输入法应用的所有子类型。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[InputMethodSubtype](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod-subtype#inputmethodsubtype)\>> | 是 | 回调函数，返回当前输入法应用的所有子类型。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12800001 | bundle manager error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```ts
import { InputMethodSubtype } from '@kit.IMEKit';
import { BusinessError } from '@kit.BasicServicesKit';

let inputMethodSetting: inputMethod.InputMethodSetting = inputMethod.getSetting();
inputMethodSetting.listCurrentInputMethodSubtype((err: BusinessError, data: Array<InputMethodSubtype>) => {
  if (err) {
    console.error(`Failed to listCurrentInputMethodSubtype, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in listing currentInputMethodSubtype.');
});
```

#### \[h2\]listCurrentInputMethodSubtype9+

listCurrentInputMethodSubtype(): Promise<Array<InputMethodSubtype>>

查询当前输入法应用的所有子类型。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<[InputMethodSubtype](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod-subtype#inputmethodsubtype)\>> | Promise对象，返回当前输入法应用的所有子类型。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12800001 | bundle manager error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```ts
import { InputMethodSubtype } from '@kit.IMEKit';
import { BusinessError } from '@kit.BasicServicesKit';

let inputMethodSetting: inputMethod.InputMethodSetting = inputMethod.getSetting();

inputMethodSetting.listCurrentInputMethodSubtype().then((data: Array<InputMethodSubtype>) => {
  console.info('Succeeded in listing currentInputMethodSubtype.');
}).catch((err: BusinessError) => {
  console.error(`Failed to listCurrentInputMethodSubtype, code: ${err.code}, message: ${err.message}`);
})
```

#### \[h2\]getInputMethods9+

getInputMethods(enable: boolean, callback: AsyncCallback<Array<InputMethodProperty>>): void

获取已激活/未激活的输入法应用列表。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/_K4sxGXYT0OWXf8C91y4MQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=D4ED9A897E8D02D1B75B0FC0F2B9D181800955768BF4BD4530E70049F0F69B5C)

已激活输入法为使能的输入法应用。默认输入法默认使能，其他输入法可被设置为使能或非使能。

已激活输入法列表包括默认输入法和已被设置为使能的输入法应用，未激活输入法列表包括除使能输入法以外的其他已安装的输入法。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| enable | boolean | 是 | true表示返回已激活输入法列表，false表示返回未激活输入法列表。 |
| callback | AsyncCallback<Array<[InputMethodProperty](#inputmethodproperty8)\>> | 是 | 回调函数，返回已激活/未激活输入法列表。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800001 | bundle manager error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getSetting().getInputMethods(true, (err: BusinessError, data: Array<inputMethod.InputMethodProperty>) => {
  if (err) {
    console.error(`Failed to getInputMethods, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in getting inputMethods.');
});
```

#### \[h2\]getInputMethods9+

getInputMethods(enable: boolean): Promise<Array<InputMethodProperty>>

获取已激活/未激活的输入法应用列表。使用promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/EKhfbFZMR3K7r049L6V3tQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=7C64B1DEC1105725B3F16D18E2609CEFBA736D851E85B1EFAADE1923AA1AEB6B)

已激活输入法为使能的输入法应用。默认输入法默认使能，其他输入法可被设置为使能或非使能。

已激活输入法列表包括默认输入法和已被设置为使能的输入法应用，未激活输入法列表包括除使能输入法以外的其他已安装的输入法。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| enable | boolean | 是 | \- true表示返回已激活输入法列表，false表示返回未激活输入法列表。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<[InputMethodProperty](#inputmethodproperty8)\>> | Promise对象，返回已激活/未激活输入法列表。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800001 | bundle manager error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getSetting().getInputMethods(true).then((data: Array<inputMethod.InputMethodProperty>) => {
  console.info('Succeeded in getting inputMethods.');
}).catch((err: BusinessError) => {
  console.error(`Failed to getInputMethods, code: ${err.code}, message: ${err.message}`);
})
```

#### \[h2\]getInputMethodsSync11+

getInputMethodsSync(enable: boolean): Array<InputMethodProperty>

获取已激活/未激活的输入法应用列表。同步接口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/fqylC0PUS4uisVjJW5qOHA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=BEB296E98645FA425F3522C339570419043E2637697E656874B41E546756B198)

已激活输入法为使能的输入法应用。默认输入法默认使能，其他输入法可被设置为使能或非使能。

已激活输入法列表包括默认输入法和已被设置为使能的输入法应用，未激活输入法列表包括除使能输入法以外的其他已安装的输入法。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| enable | boolean | 是 | \- true表示返回已激活输入法列表，false表示返回未激活输入法列表。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Array<[InputMethodProperty](#inputmethodproperty8)\> | 返回已激活/未激活输入法列表。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800001 | bundle manager error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```ts
let imeProperty: Array<inputMethod.InputMethodProperty> = inputMethod.getSetting().getInputMethodsSync(true);
```

#### \[h2\]getAllInputMethods11+

getAllInputMethods(callback: AsyncCallback<Array<InputMethodProperty>>): void

获取所有输入法应用列表。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[InputMethodProperty](#inputmethodproperty8)\>> | 是 | 回调函数，返回所有输入法列表。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12800001 | bundle manager error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getSetting().getAllInputMethods((err: BusinessError, data: Array<inputMethod.InputMethodProperty>) => {
  if (err) {
    console.error(`Failed to getAllInputMethods, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in getting all inputMethods.');
});
```

#### \[h2\]getAllInputMethods11+

getAllInputMethods(): Promise<Array<InputMethodProperty>>

获取所有输入法应用列表。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<[InputMethodProperty](#inputmethodproperty8)\>> | Promise对象，返回所有输入法列表。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12800001 | bundle manager error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getSetting().getAllInputMethods().then((data: Array<inputMethod.InputMethodProperty>) => {
  console.info('Succeeded in getting all inputMethods.');
}).catch((err: BusinessError) => {
  console.error(`Failed to getAllInputMethods, code: ${err.code}, message: ${err.message}`);
})
```

#### \[h2\]getAllInputMethodsSync11+

getAllInputMethodsSync(): Array<InputMethodProperty>

获取所有输入法应用列表。同步接口。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Array<[InputMethodProperty](#inputmethodproperty8)\> | 返回所有输入法列表 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12800001 | bundle manager error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```ts
let imeProperty: Array<inputMethod.InputMethodProperty> = inputMethod.getSetting().getAllInputMethodsSync();
```

#### \[h2\]showOptionalInputMethods(deprecated)

showOptionalInputMethods(callback: AsyncCallback<boolean>): void

显示输入法选择对话框。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/S4ajWwJOQem7ivnHmRoDrw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=488F3E73E3BD29E356D50A92D2CEAAEB5552BA44A0CE85FA60D61B465A4A0332)

从API version 9开始支持，从API version 18开始废弃，建议使用[InputMethodListDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethodlist#inputmethodlistdialog)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当输入法选择对话框显示成功，err为undefined，data为true；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getSetting().showOptionalInputMethods((err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to showOptionalInputMethods, code: ${err.code}, message: ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in showing optionalInputMethods.');
  } else {
    console.error(`Failed to showOptionalInputMethods.`);
  }
});
```

#### \[h2\]showOptionalInputMethods(deprecated)

showOptionalInputMethods(): Promise<boolean>

显示输入法选择对话框。使用promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/LbCrQxjLSeehEwbSEifc8Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=E2E8AB58D7F1E0A823E113B48661609D1E48DB4B30A8FAB6AD8F674B338B2461)

从API version 9开始支持，从API version 18开始废弃，建议使用[InputMethodListDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethodlist#inputmethodlistdialog)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象。当输入法选择对话框显示成功，err为undefined，data为true；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getSetting().showOptionalInputMethods().then((result: boolean) => {
  if (result) {
    console.info('Succeeded in showing optionalInputMethods.');
  } else {
    console.error(`Failed to showOptionalInputMethods.`);
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to showOptionalInputMethods, code: ${err.code}, message: ${err.message}`);
})
```

#### \[h2\]listInputMethod(deprecated)

listInputMethod(callback: AsyncCallback<Array<InputMethodProperty>>): void

查询已安装的输入法列表。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/N7y7XjDTTvmFdUCzVSDYCA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=7D7CCE4A66BC2B5244B669E525419EB720D540DF080387F61996D8F68D9F8897)

从API version 8开始支持，从API version 9开始废弃，建议使用[getInputMethods](#getinputmethods9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[InputMethodProperty](#inputmethodproperty8)\>> | 是 | 回调函数，返回已安装的输入法列表。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getSetting().listInputMethod((err: BusinessError, data: Array<inputMethod.InputMethodProperty>) => {
  if (err) {
    console.error(`Failed to listInputMethod, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in listing inputMethod.');
});
```

#### \[h2\]listInputMethod(deprecated)

listInputMethod(): Promise<Array<InputMethodProperty>>

查询已安装的输入法列表。使用promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/4sDisYniSFKjfqLFysfvHA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=A8BDD9D4EDEE72E0CAED53CF85A795D9EDE0D45F7ED43957F821189F7518688D)

从API version 8开始支持，从API version 9开始废弃，建议使用[getInputMethods](#getinputmethods9-1)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<[InputMethodProperty](#inputmethodproperty8)\>> | Promise对象，返回已安装输入法列表。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getSetting().listInputMethod().then((data: Array<inputMethod.InputMethodProperty>) => {
  console.info('Succeeded in listing inputMethod.');
}).catch((err: BusinessError) => {
  console.error(`Failed to listInputMethod, code: ${err.code}, message: ${err.message}`);
})
```

#### \[h2\]displayOptionalInputMethod(deprecated)

displayOptionalInputMethod(callback: AsyncCallback<void>): void

显示输入法选择对话框。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/WntmMG8aSSuuIlB2BLgeQQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=BCE98973E3A29D7E6AD1475E1970D81C78A4F029E97F4642FE319F30DB8C3C1A)

从API version 8开始支持，从API version 9开始废弃，建议使用[InputMethodListDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethodlist#inputmethodlistdialog)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | 是 | 回调函数。当输入法选择对话框显示成功。err为undefined，否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getSetting().displayOptionalInputMethod((err: BusinessError) => {
  if (err) {
    console.error(`Failed to displayOptionalInputMethod, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in displaying optionalInputMethod.');
});
```

#### \[h2\]displayOptionalInputMethod(deprecated)

displayOptionalInputMethod(): Promise<void>

显示输入法选择对话框。使用promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/qacNgL3WSd2wnXRjaCWTeA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=05365CA89C0AC2E0F64E562FB4804DB25997492E06CAE5A3AA49B034EA40BDA4)

从API version 8开始支持，从API version 9开始废弃，建议使用[InputMethodListDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethodlist#inputmethodlistdialog)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getSetting().displayOptionalInputMethod().then(() => {
  console.info('Succeeded in displaying optionalInputMethod.');
}).catch((err: BusinessError) => {
  console.error(`Failed to displayOptionalInputMethod, code: ${err.code}, message: ${err.message}`);
})
```

#### \[h2\]getInputMethodState15+

getInputMethodState(): Promise<EnabledState>

查询输入法的启用状态。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[EnabledState](#enabledstate15)\> | Promise对象，返回EnabledState.DISABLED表示未启用; 返回EnabledState.BASIC\_MODE表示基础模式; 返回EnabledState.FULL\_EXPERIENCE\_MODE表示完整体验模式。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12800004 | not an input method application. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getSetting().getInputMethodState().then((status: inputMethod.EnabledState) => {
  console.info(`Succeeded in getInputMethodState, status: ${status}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to getInputMethodState, code: ${err.code}, message: ${err.message}`);
})
```

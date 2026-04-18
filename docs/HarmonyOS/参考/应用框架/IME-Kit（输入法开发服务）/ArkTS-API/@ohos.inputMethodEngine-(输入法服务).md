---
title: "@ohos.inputMethodEngine (输入法服务)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethodengine"
menu_path:
  - "参考"
  - "应用框架"
  - "IME Kit（输入法开发服务）"
  - "ArkTS API"
  - "@ohos.inputMethodEngine (输入法服务)"
captured_at: "2026-04-17T01:48:15.480Z"
---

# @ohos.inputMethodEngine (输入法服务)

本模块面向输入法应用（包括系统输入法应用、三方输入法应用），为输入法应用提供能力，包括：创建软键盘窗口、插入/删除字符、选中文本、监听物理键盘按键事件等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/tE63Ym97SNeeWzR_FLFsIA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=0D3AADB4B597B2A3AB37EA9974FB115F2D0F67BCF650F440F7DD1C0FD27E76CC)

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import { inputMethodEngine } from '@kit.IMEKit';
```

#### 常量

功能键常量值、编辑框常量值及光标常量值。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 值 | 说明 |
| :-- | :-- | :-- | :-- |
| ENTER\_KEY\_TYPE\_UNSPECIFIED | number | 0 | 无功能键。 |
| ENTER\_KEY\_TYPE\_GO | number | 2 | “前往”功能键。 |
| ENTER\_KEY\_TYPE\_SEARCH | number | 3 | “搜索”功能键。 |
| ENTER\_KEY\_TYPE\_SEND | number | 4 | “发送”功能键。 |
| ENTER\_KEY\_TYPE\_NEXT | number | 5 | “下一个”功能键。 |
| ENTER\_KEY\_TYPE\_DONE | number | 6 | “回车”功能键。 |
| ENTER\_KEY\_TYPE\_PREVIOUS | number | 7 | “前一个”功能键。 |
| ENTER\_KEY\_TYPE\_NEWLINE12+ | number | 8 | “换行”功能键。 |
| PATTERN\_NULL | number | \-1 | 无特殊性编辑框。 |
| PATTERN\_TEXT | number | 0 | 文本编辑框。 |
| PATTERN\_NUMBER | number | 2 | 数字编辑框。 |
| PATTERN\_PHONE | number | 3 | 电话号码编辑框。 |
| PATTERN\_DATETIME | number | 4 | 日期编辑框。 |
| PATTERN\_EMAIL | number | 5 | 邮件编辑框。 |
| PATTERN\_URI | number | 6 | 超链接编辑框。 |
| PATTERN\_PASSWORD | number | 7 | 密码编辑框。 |
| PATTERN\_PASSWORD\_NUMBER11+ | number | 8 | 数字密码编辑框。 |
| PATTERN\_PASSWORD\_SCREEN\_LOCK11+ | number | 9 | 锁屏密码编辑框。 |
| PATTERN\_USER\_NAME20+ | number | 10 | 用户名编辑框。 |
| PATTERN\_NEW\_PASSWORD20+ | number | 11 | 新密码编辑框。 |
| PATTERN\_NUMBER\_DECIMAL20+ | number | 12 | 带小数点的数字编辑框。 |
| PATTERN\_ONE\_TIME\_CODE20+ | number | 13 | 验证码编辑框。 |
| OPTION\_ASCII | number | 20 | 允许输入ASCII值。 |
| OPTION\_NONE | number | 0 | 不指定编辑框输入属性。 |
| OPTION\_AUTO\_CAP\_CHARACTERS | number | 2 | 允许输入字符。 |
| OPTION\_AUTO\_CAP\_SENTENCES | number | 8 | 允许输入句子。 |
| OPTION\_AUTO\_WORDS | number | 4 | 允许输入单词。 |
| OPTION\_MULTI\_LINE | number | 1 | 允许输入多行。 |
| OPTION\_NO\_FULLSCREEN | number | 10 | 半屏样式。 |
| FLAG\_SELECTING | number | 2 | 编辑框处于选择状态。 |
| FLAG\_SINGLE\_LINE | number | 1 | 编辑框为单行。 |
| DISPLAY\_MODE\_PART | number | 0 | 编辑框显示为半屏。 |
| DISPLAY\_MODE\_FULL | number | 1 | 编辑框显示为全屏。 |
| CURSOR\_UP9+ | number | 1 | 光标上移。 |
| CURSOR\_DOWN9+ | number | 2 | 光标下移。 |
| CURSOR\_LEFT9+ | number | 3 | 光标左移。 |
| CURSOR\_RIGHT9+ | number | 4 | 光标右移。 |
| WINDOW\_TYPE\_INPUT\_METHOD\_FLOAT9+ | number | 2105 | 输入法应用窗口风格标识。 |

#### inputMethodEngine.getInputMethodAbility9+

getInputMethodAbility(): InputMethodAbility

获取输入法应用客户端实例[InputMethodAbility](#inputmethodability)，仅支持输入法应用调用。

输入法应用获取该实例后，可订阅软键盘显示/隐藏请求事件、创建/销毁输入法面板等。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [InputMethodAbility](#inputmethodability) | 输入法应用客户端。 |

**示例：**

```ts
let InputMethodAbility: inputMethodEngine.InputMethodAbility = inputMethodEngine.getInputMethodAbility();
```

#### inputMethodEngine.getKeyboardDelegate9+

getKeyboardDelegate(): KeyboardDelegate

获取客户端编辑事件监听代理实例[KeyboardDelegate](#keyboarddelegate)。

输入法应用获取该实例后，可订阅物理键盘按键事件、选中文本变化事件等。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [KeyboardDelegate](#keyboarddelegate) | 客户端编辑事件监听代理。 |

**示例：**

```ts
let KeyboardDelegate: inputMethodEngine.KeyboardDelegate = inputMethodEngine.getKeyboardDelegate();
```

#### inputMethodEngine.getInputMethodEngine(deprecated)

getInputMethodEngine(): InputMethodEngine

获取输入法应用客户端实例[InputMethodEngine](#inputmethodenginedeprecated)。

输入法应用获取该实例后，可订阅软键盘显示/隐藏请求事件等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/2sxMtNuZR4G2BeXV6vBhww/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=4C226CBE4E047B72AF77EE53B7920DEE694A42DCAA0327FCD4F84933CE4B8003)

从API version 8开始支持，API version 9开始废弃，建议使用[getInputMethodAbility](#inputmethodenginegetinputmethodability9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [InputMethodEngine](#inputmethodenginedeprecated) | 输入法应用客户端。 |

**示例：**

```ts
let InputMethodEngine: inputMethodEngine.InputMethodEngine = inputMethodEngine.getInputMethodEngine();
```

#### inputMethodEngine.createKeyboardDelegate(deprecated)

createKeyboardDelegate(): KeyboardDelegate

获取客户端编辑事件监听代理实例[KeyboardDelegate](#keyboarddelegate)。输入法应用获取该实例后，可订阅物理键盘按键事件、选中文本变化事件等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/HZTaUiiRRKqNSBtaaow5ug/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=42B92C48D5A59B27394C36BF1EDE17CFD9C00323325DF226C046ED04BBFAB2FE)

从API version 8开始支持，API version 9开始废弃，建议使用[getKeyboardDelegate](#inputmethodenginegetkeyboarddelegate9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [KeyboardDelegate](#keyboarddelegate) | 客户端编辑事件监听代理。 |

**示例：**

```ts
let keyboardDelegate: inputMethodEngine.KeyboardDelegate = inputMethodEngine.createKeyboardDelegate();
```

#### CommandDataType12+

type CommandDataType = number | string | boolean;

表示私有数据类型，接口参数具体类型根据其功能而定。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 类型 | 说明 |
| :-- | :-- |
| string | 表示值类型为字符串。 |
| number | 表示值类型为数字。 |
| boolean | 表示值类型为布尔值。 |

#### SizeChangeCallback15+

type SizeChangeCallback = (size: window.Size, keyboardArea?: KeyboardArea) => void

当输入法面板大小变化时触发的回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| size | [window.Size](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-i#size7) | 是 | 当前面板大小。 |
| keyboardArea | [KeyboardArea](#keyboardarea15) | 否 | 当前面板中可作为键盘区域的大小。 |

#### InputMethodEngine(deprecated)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/QOuk-ZHPRWuJKaykmtlbtA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=BB1CBFBEDC1C89B0A5A7D84CA0366A6B49FCB9D99D7A187EC7AEC0EBF4DA52B5)

从API version 8开始支持，API version 23开始废弃，建议使用[InputMethodAbility](#inputmethodability)替代。

下列API均需使用[getInputMethodEngine](#inputmethodenginegetinputmethodenginedeprecated)获取到InputMethodEngine实例后，通过实例调用。

#### \[h2\]on('inputStart')(deprecated)

on(type: 'inputStart', callback: (kbController: KeyboardController, textInputClient: TextInputClient) => void): void

订阅输入法绑定成功事件。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/py1mr45STIu2ai9ACzPo4g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=901729C8842500967E80507D498BF7C74E3956E1903F9B25482554565EAEFD88)

从API version 8开始支持，API version 23开始废弃，建议使用[InputMethodAbility#on](#oninputstart9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'inputStart'。 |
| callback | (kbController: [KeyboardController](#keyboardcontroller), textInputClient: [TextInputClient](#textinputclientdeprecated)) => void | 是 | 回调函数，返回订阅输入法的KeyboardController和TextInputClient实例。 |

**示例：**

```ts
inputMethodEngine.getInputMethodEngine()
  .on('inputStart',
    (kbController: inputMethodEngine.KeyboardController, textClient: inputMethodEngine.TextInputClient) => {
      let keyboardController: inputMethodEngine.KeyboardController = kbController;
      let textInputClient: inputMethodEngine.TextInputClient = textClient;
    });
```

#### \[h2\]off('inputStart')(deprecated)

off(type: 'inputStart', callback?: (kbController: KeyboardController, textInputClient: TextInputClient) => void): void

取消订阅输入法绑定成功事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/f1hVqLkWTBOxKTveDx-Ipw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=16BCB0D918ABAEC9E20EF46098141FFFE7EC534D5A6F9C2D78782FFDD4D6B6FC)

从API version 8开始支持，API version 23开始废弃，建议使用[InputMethodAbility#off](#offinputstart9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'inputStart'。 |
| callback | (kbController: [KeyboardController](#keyboardcontroller), textInputClient: [TextInputClient](#textinputclientdeprecated)) => void | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```ts
inputMethodEngine.getInputMethodEngine()
  .off('inputStart',
    (kbController: inputMethodEngine.KeyboardController, textClient: inputMethodEngine.TextInputClient) => {
      console.info('delete inputStart notification.');
    });
```

#### \[h2\]on('keyboardShow'|'keyboardHide')(deprecated)

on(type: 'keyboardShow'|'keyboardHide', callback: () => void): void

订阅输入法软键盘显示或隐藏事件。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/4ahRhNA6Qfyst5l-IbFLFg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=611C6B256291BE617424562131BBD13DA2E2FF75878F3340E9933E8A1C9CA835)

从API version 8开始支持，API version 23开始废弃，建议使用[InputMethodAbility#on](#onkeyboardshowkeyboardhide9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 
设置监听类型。

\-'keyboardShow'表示显示输入法软键盘。

\-'keyboardHide'表示隐藏输入法软键盘。

 |
| callback | () => void | 是 | 回调函数。 |

**示例：**

```ts
inputMethodEngine.getInputMethodEngine().on('keyboardShow', () => {
  console.info('inputMethodEngine keyboardShow.');
});
inputMethodEngine.getInputMethodEngine().on('keyboardHide', () => {
  console.info('inputMethodEngine keyboardHide.');
});
```

#### \[h2\]off('keyboardShow'|'keyboardHide')(deprecated)

off(type: 'keyboardShow'|'keyboardHide', callback?: () => void): void

取消订阅输入法软键盘显示或隐藏事件。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/fGMNyP5gR7e-QaySjSiQvw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=C4621E73A468250399FAC16AAEF40548559A77B61BD3C21FAD1C8DFD86663A5C)

从API version 8开始支持，API version 23开始废弃，建议使用[InputMethodAbility#off](#offkeyboardshowkeyboardhide9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 
要取消监听的输入法软键盘事件类型。

\-'keyboardShow'表示显示输入法软键盘。

\-'keyboardHide'表示隐藏输入法软键盘。

 |
| callback | () => void | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```ts
inputMethodEngine.getInputMethodEngine().off('keyboardShow');
inputMethodEngine.getInputMethodEngine().off('keyboardHide');
```

#### InputMethodAbility

下列API均需使用[getInputMethodAbility](#inputmethodenginegetinputmethodability9)获取到InputMethodAbility实例后，通过实例调用。

#### \[h2\]on('inputStart')9+

on(type: 'inputStart', callback: (kbController: KeyboardController, inputClient: InputClient) => void): void

订阅输入法绑定成功事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'inputStart'。 |
| callback | (kbController: [KeyboardController](#keyboardcontroller), inputClient: [InputClient](#inputclient9)) => void | 是 | 回调函数，返回输入法操作相关实例。 |

**示例：**

```ts
inputMethodEngine.getInputMethodAbility()
  .on('inputStart',
    (kbController: inputMethodEngine.KeyboardController, client: inputMethodEngine.InputClient) => {
      let keyboardController: inputMethodEngine.KeyboardController = kbController;
      let inputClient: inputMethodEngine.InputClient = client;
    });
```

#### \[h2\]off('inputStart')9+

off(type: 'inputStart', callback?: (kbController: KeyboardController, inputClient: InputClient) => void): void

取消订阅输入法绑定成功事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'inputStart'。 |
| callback | (kbController: [KeyboardController](#keyboardcontroller), inputClient: [InputClient](#inputclient9)) => void | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```ts
inputMethodEngine.getInputMethodAbility().off('inputStart');
```

#### \[h2\]on('inputStop')9+

on(type: 'inputStop', callback: () => void): void

订阅停止输入法应用事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'inputStop'。 |
| callback | () => void | 是 | 回调函数。 |

**示例：**

```ts
inputMethodEngine.getInputMethodAbility().on('inputStop', () => {
  console.info('inputMethodAbility inputStop');
});
```

#### \[h2\]off('inputStop')9+

off(type: 'inputStop', callback: () => void): void

取消订阅停止输入法应用事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'inputStop'。 |
| callback | () => void | 是 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```ts
inputMethodEngine.getInputMethodAbility().off('inputStop', () => {
  console.info('inputMethodAbility delete inputStop notification.');
});
```

#### \[h2\]on('setCallingWindow')9+

on(type: 'setCallingWindow', callback: (wid: number) => void): void

订阅设置调用窗口事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'setCallingWindow'。 |
| callback | (wid: number) => void | 是 | 回调函数，返回调用方窗口的Id。 |

**示例：**

```ts
inputMethodEngine.getInputMethodAbility().on('setCallingWindow', (wid: number) => {
  console.info('inputMethodAbility setCallingWindow');
});
```

#### \[h2\]off('setCallingWindow')9+

off(type: 'setCallingWindow', callback: (wid:number) => void): void

取消订阅设置调用窗口事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'setCallingWindow'。 |
| callback | (wid:number) => void | 是 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```ts
inputMethodEngine.getInputMethodAbility().off('setCallingWindow', (wid: number) => {
  console.info('inputMethodAbility delete setCallingWindow notification.');
});
```

#### \[h2\]on('keyboardShow'|'keyboardHide')9+

on(type: 'keyboardShow'|'keyboardHide', callback: () => void): void

订阅输入法软键盘显示或隐藏事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 
设置监听类型。

\- 'keyboardShow'表示显示输入法软键盘。

\- 'keyboardHide'表示隐藏输入法软键盘。

 |
| callback | () => void | 是 | 回调函数。 |

**示例：**

```ts
inputMethodEngine.getInputMethodAbility().on('keyboardShow', () => {
  console.info('InputMethodAbility keyboardShow.');
});
inputMethodEngine.getInputMethodAbility().on('keyboardHide', () => {
  console.info('InputMethodAbility keyboardHide.');
});
```

#### \[h2\]off('keyboardShow'|'keyboardHide')9+

off(type: 'keyboardShow'|'keyboardHide', callback?: () => void): void

取消订阅输入法软键盘显示或隐藏事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 
设置监听类型。

\- 'keyboardShow'表示显示键盘。

\- 'keyboardHide'表示隐藏键盘。

 |
| callback | () => void | 否 | 回调函数。 |

**示例：**

```ts
inputMethodEngine.getInputMethodAbility().off('keyboardShow', () => {
  console.info('InputMethodAbility delete keyboardShow notification.');
});
inputMethodEngine.getInputMethodAbility().off('keyboardHide', () => {
  console.info('InputMethodAbility delete keyboardHide notification.');
});
```

#### \[h2\]on('setSubtype')9+

on(type: 'setSubtype', callback: (inputMethodSubtype: InputMethodSubtype) => void): void

订阅设置输入法子类型事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'setSubtype'。 |
| callback | (inputMethodSubtype: [InputMethodSubtype](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod-subtype)) => void | 是 | 回调函数，返回设置的输入法子类型。 |

**示例：**

```ts
import { InputMethodSubtype } from '@kit.IMEKit';

inputMethodEngine.getInputMethodAbility().on('setSubtype', (inputMethodSubtype: InputMethodSubtype) => {
  console.info('InputMethodAbility setSubtype.');
});
```

#### \[h2\]off('setSubtype')9+

off(type: 'setSubtype', callback?: (inputMethodSubtype: InputMethodSubtype) => void): void

取消订阅设置输入法子类型事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'setSubtype'。 |
| callback | (inputMethodSubtype: [InputMethodSubtype](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod-subtype)) => void | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```ts
inputMethodEngine.getInputMethodAbility().off('setSubtype', () => {
  console.info('InputMethodAbility delete setSubtype notification.');
});
```

#### \[h2\]on('securityModeChange')11+

on(type: 'securityModeChange', callback: Callback< SecurityMode>): void

订阅输入法安全模式改变类型事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'securityModeChange'。 |
| callback | Callback<[SecurityMode](#securitymode11)\> | 是 | 回调函数，返回当前输入法应用的安全模式。 |

**示例：**

```ts
inputMethodEngine.getInputMethodAbility()
  .on('securityModeChange', (securityMode: inputMethodEngine.SecurityMode) => {
    console.info(`InputMethodAbility securityModeChange, security is ${securityMode}`);
  });
```

#### \[h2\]off('securityModeChange')11+

off(type: 'securityModeChange', callback?: Callback< SecurityMode>): void

取消订阅输入法安全模式改变类型事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'securityModeChange'。 |
| callback | Callback<[SecurityMode](#securitymode11)\> | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```ts
let securityChangeCallback: (securityMode: inputMethodEngine.SecurityMode) => void =
  (securityMode: inputMethodEngine.SecurityMode) => {
    console.info(`InputMethodAbility securityModeChange, security is ${securityMode}`);
  };
let inputMethodAbility: inputMethodEngine.InputMethodAbility = inputMethodEngine.getInputMethodAbility();
inputMethodAbility.on('securityModeChange', securityChangeCallback);
inputMethodAbility.off('securityModeChange', securityChangeCallback);
```

#### \[h2\]on('privateCommand')12+

on(type: 'privateCommand', callback: Callback<Record<string, CommandDataType>>): void;

订阅输入法私有数据事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'privateCommand'。 |
| callback | Callback<Record<string, [CommandDataType](#commanddatatype12)\>> | 是 | 回调函数，返回向输入法应用发送的私有数据。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12800010 | not the preconfigured default input method. |

**示例：**

```ts
let privateCommandCallback: (record: Record<string, inputMethodEngine.CommandDataType>) => void =
  (record: Record<string, inputMethodEngine.CommandDataType>) => {
    for (let i :number = 0; i < record.length; i++) {
      console.info(`private command key: ${i}, value: ${record[i]}`);
    }
  }
inputMethodEngine.getInputMethodAbility().on('privateCommand', privateCommandCallback);
```

#### \[h2\]off('privateCommand')12+

off(type: 'privateCommand', callback?: Callback<Record<string, CommandDataType>>): void

取消订阅输入法私有数据事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'privateCommand'。 |
| callback | Callback<Record<string, [CommandDataType](#commanddatatype12)\>> | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12800010 | not the preconfigured default input method. |

**示例：**

```ts
let privateCommandCallback: (record: Record<string, inputMethodEngine.CommandDataType>) => void =
  (record: Record<string, inputMethodEngine.CommandDataType>) => {
    for (let i: number = 0; i < record.length; i++) {
      console.info(`private command key: ${i}, value: ${record[i]}`);
    }
  }

inputMethodEngine.getInputMethodAbility().off('privateCommand', privateCommandCallback);
```

#### \[h2\]on('callingDisplayDidChange')18+

on(type: 'callingDisplayDidChange', callback: Callback<number>): void

订阅编辑框对应窗口所在屏幕ID变化事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'callingDisplayDidChange'。 |
| callback | Callback<number> | 是 | 回调函数，返回编辑框设置对应窗口屏幕ID。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 801 | capability not supported. |

**示例：**

```ts
let callingDisplayDidChangeCallback: (num: number) => void = (num: number) => {
  console.info(`display id: ${num}`);
}
inputMethodEngine.getInputMethodAbility().on('callingDisplayDidChange', callingDisplayDidChangeCallback);
```

#### \[h2\]off('callingDisplayDidChange')18+

off(type: 'callingDisplayDidChange', callback?: Callback<number>): void

取消订阅编辑框对应窗口所在屏幕ID变化事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'callingDisplayDidChange'。 |
| callback | Callback<number> | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```ts
inputMethodEngine.getInputMethodAbility().off('callingDisplayDidChange', (num: number) => {
  console.info('InputMethodAbility delete calling display  notification.');
});
```

#### \[h2\]on('discardTypingText')20+

on(type: 'discardTypingText', callback: Callback<void>): void

订阅编辑框应用发送“清空候选词”事件到输入法。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 
设置监听类型，固定取值为'discardTypingText'。

\- 'discardTypingText'：表示订阅编辑框应用发送“清空候选词”事件到输入法。

 |
| callback | Callback<void> | 是 | 回调函数。当命令发送成功，err为undefined，否则为错误对象。 |

**示例：**

```ts
inputMethodEngine.getInputMethodAbility().on('discardTypingText', () => {
  console.info('InputMethodAbility discard the typing text.');
});
```

#### \[h2\]off('discardTypingText')20+

off(type: 'discardTypingText', callback?: Callback<void>): void

取消订阅编辑框应用发送“清空候选词”事件到输入法。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 
设置监听类型，固定取值为'discardTypingText'。

\- 'discardTypingText'：表示取消订阅编辑框应用发送“清空候选词”事件到输入法。

 |
| callback | Callback<void> | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```ts
inputMethodEngine.getInputMethodAbility().off('discardTypingText', () => {
  console.info('InputMethodAbility discard the typing text.');
});
```

#### \[h2\]getSecurityMode11+

getSecurityMode(): SecurityMode

获取输入法应用的当前安全模式。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [SecurityMode](#securitymode11) | 安全模式。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12800004 | not an input method application. |

**示例：**

```ts
let security: inputMethodEngine.SecurityMode = inputMethodEngine.getInputMethodAbility().getSecurityMode();
console.error(`getSecurityMode, securityMode is : ${security}`);
```

#### \[h2\]createPanel10+

createPanel(ctx: BaseContext, info: PanelInfo, callback: AsyncCallback<Panel>): void

创建输入法面板，仅支持输入法应用在[InputMethodExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod-extension-ability#inputmethodextensionability)类中调用。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/ymfue0XfQWu-0MmHr22O7Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=B4CB3368A6F318C73ADB247A58360DF84942DB42E050030A6B31D97FF4FF142C)

单个输入法应用仅允许创建一个[软键盘类型](#paneltype10)和一个[状态栏类型](#paneltype10)的面板。

输入法面板不支持创建子窗口。例如：不支持使用[window.createWindow](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-window-fa#设置应用子窗口)、[bindContextMenu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-menu#bindcontextmenu8)、[CustomDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-custom-dialog-box)等接口创建子窗口弹窗。建议开发者采用非子窗的替代方案，如[弹出框](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-dialog)、[bindMenu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-menu#bindmenu)或设置showInSubwindow为false。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| ctx | [BaseContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-basecontext) | 是 | 当前输入法应用上下文信息。 |
| info | [PanelInfo](#panelinfo10) | 是 | 输入法面板信息。 |
| callback | AsyncCallback<[Panel](#panel10)\> | 是 | 回调函数。当输入法面板创建成功，返回当前创建的输入法面板对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 12800004 | not an input method application. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { inputMethodEngine, InputMethodExtensionAbility } from '@kit.IMEKit';
import { Want } from '@kit.AbilityKit';

let panelInfo: inputMethodEngine.PanelInfo = {
  type: inputMethodEngine.PanelType.SOFT_KEYBOARD,
  flag: inputMethodEngine.PanelFlag.FLG_FIXED
}

class InputMethodExt extends InputMethodExtensionAbility {
    onCreate(want: Want): void {
        console.info(`onCreate, want: ${want.abilityName}`);
        if (!this.context) {
            inputMethodEngine.getInputMethodAbility()
            .createPanel(this.context, panelInfo, (err: BusinessError, panel: inputMethodEngine.Panel) => {
                if (err) {
                console.error(`Failed to createPanel. Code is ${err.code}, message is ${err.message}`);
                return;
              }
                console.info('Succeed in creating panel.');
            })
        }
    }
}
```

#### \[h2\]createPanel10+

createPanel(ctx: BaseContext, info: PanelInfo): Promise<Panel>

创建输入法面板，仅支持输入法应用在[InputMethodExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod-extension-ability#inputmethodextensionability)类中调用。使用promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/tbxsym7GS0uIxheCi8-61w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=5ACA61DA210D375E4D51B3D1047A1D17B1C84F8011B2BC9D3935DC98A74A49DE)

单个输入法应用仅允许创建一个[软键盘类型](#paneltype10)和一个[状态栏类型](#paneltype10)的面板。

输入法面板不支持创建子窗口。例如：不支持使用[window.createWindow](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-window-fa#设置应用子窗口)、[bindContextMenu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-menu#bindcontextmenu8)、[CustomDialog](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-custom-dialog-box)等接口创建子窗口弹窗。建议开发者采用非子窗的替代方案，如[弹出框](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-dialog)、[bindMenu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-menu#bindmenu)或设置showInSubwindow为false。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| ctx | [BaseContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-basecontext) | 是 | 当前输入法应用上下文信息。 |
| info | [PanelInfo](#panelinfo10) | 是 | 输入法面板信息。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[Panel](#panel10)\> | 回调函数。当输入法面板创建成功，返回当前创建的输入法面板对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 12800004 | not an input method application. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { inputMethodEngine, InputMethodExtensionAbility } from '@kit.IMEKit';
import { Want } from '@kit.AbilityKit';

let panelInfo: inputMethodEngine.PanelInfo = {
  type: inputMethodEngine.PanelType.SOFT_KEYBOARD,
  flag: inputMethodEngine.PanelFlag.FLG_FIXED
}

class InputMethodExt extends InputMethodExtensionAbility {
    onCreate(want: Want): void {
        console.info(`onCreate, want: ${want.abilityName}`);
        if (this.context) {
            inputMethodEngine.getInputMethodAbility().createPanel(this.context, panelInfo)
                .then((panel: inputMethodEngine.Panel) => {
                console.info('Succeed in creating panel.');
            }).catch((err: BusinessError) => {
                console.error(`Failed to create panel. Code is ${err.code}, message is ${err.message}`);
            })
        }
    }
}
```

#### \[h2\]destroyPanel10+

destroyPanel(panel: Panel, callback: AsyncCallback<void>): void

销毁输入法面板。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| panel | [Panel](#panel10) | 是 | 要销毁的面板对象。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当输入法面板销毁成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let panelInfo: inputMethodEngine.PanelInfo = {
  type: inputMethodEngine.PanelType.SOFT_KEYBOARD,
  flag: inputMethodEngine.PanelFlag.FLG_FIXED
}

let inputPanel: inputMethodEngine.Panel | undefined = undefined;
if (this.context) {
  inputMethodEngine.getInputMethodAbility()
    .createPanel(this.context, panelInfo, (err: BusinessError, panel: inputMethodEngine.Panel) => {
      if (err) {
        console.error(`Failed to create panel. Code is ${err.code}, message is ${err.message}`);
        return;
      }
      inputPanel = panel;
      console.info('Succeed in creating panel.');
    })
}

if (inputPanel) {
  inputMethodEngine.getInputMethodAbility().destroyPanel(inputPanel, (err: BusinessError) => {
    if (err !== undefined) {
      console.error(`Failed to destroy panel. Code is ${err.code}, message is ${err.message}`);
      return;
    }
    console.info('Succeed in destroying panel.');
  })
}
```

#### \[h2\]destroyPanel10+

destroyPanel(panel: Panel): Promise<void>

销毁输入法面板。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| panel | [Panel](#panel10) | 是 | 要销毁的面板对象。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let panelInfo: inputMethodEngine.PanelInfo = {
  type: inputMethodEngine.PanelType.SOFT_KEYBOARD,
  flag: inputMethodEngine.PanelFlag.FLG_FIXED
}

let inputPanel: inputMethodEngine.Panel | undefined = undefined;
if (this.context) {
  inputMethodEngine.getInputMethodAbility()
    .createPanel(this.context, panelInfo, (err: BusinessError, panel: inputMethodEngine.Panel) => {
      if (err) {
        console.error(`Failed to create panel. Code is ${err.code}, message is ${err.message}`);
        return;
      }
      inputPanel = panel;
      console.info('Succeed in creating panel.');
    })
}

if (inputPanel) {
  inputMethodEngine.getInputMethodAbility().destroyPanel(inputPanel).then(() => {
    console.info('Succeed in destroying panel.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to destroy panel. Code is ${err.code}, message is ${err.message}`);
  });
}
```

#### KeyboardDelegate

下列API均需使用[getKeyboardDelegate](#inputmethodenginegetkeyboarddelegate9)获取到KeyboardDelegate实例后，通过实例调用。

#### \[h2\]on('keyDown'|'keyUp')

on(type: 'keyDown'|'keyUp', callback: (event: KeyEvent) => boolean): void

订阅硬键盘（即物理键盘）上物理按键的按下或抬起事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 
设置监听类型。

\- 'keyDown'表示键盘按下。

\- 'keyUp'表示键盘抬起。

 |
| callback | (event: [KeyEvent](#keyevent)) => boolean | 是 | 回调函数，返回按键信息。 若按键事件被事件订阅者消费，则callback应返回true，否则返回false。 |

**示例：**

```ts
inputMethodEngine.getKeyboardDelegate().on('keyUp', (keyEvent: inputMethodEngine.KeyEvent) => {
  console.info(`inputMethodEngine keyCode.(keyUp): ${keyEvent.keyCode}`);
  console.info(`inputMethodEngine keyAction.(keyUp): ${keyEvent.keyAction}`);
  return true;
});
inputMethodEngine.getKeyboardDelegate().on('keyDown', (keyEvent: inputMethodEngine.KeyEvent) => {
  console.info(`inputMethodEngine keyCode.(keyDown): ${keyEvent.keyCode}`);
  console.info(`inputMethodEngine keyAction.(keyDown): ${keyEvent.keyAction}`);
  return true;
});
```

#### \[h2\]off('keyDown'|'keyUp')

off(type: 'keyDown'|'keyUp', callback?: (event: KeyEvent) => boolean): void

取消订阅硬键盘（即物理键盘）上物理按键的按下或抬起事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 
设置监听类型。

\- 'keyDown'表示键盘按下。

\- 'keyUp'表示键盘抬起。

 |
| callback | (event: [KeyEvent](#keyevent)) => boolean | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```ts
inputMethodEngine.getKeyboardDelegate().off('keyUp', (keyEvent: inputMethodEngine.KeyEvent) => {
  console.info('delete keyUp notification.');
  return true;
});
inputMethodEngine.getKeyboardDelegate().off('keyDown', (keyEvent: inputMethodEngine.KeyEvent) => {
  console.info('delete keyDown notification.');
  return true;
});
```

#### \[h2\]on('keyEvent')10+

on(type: 'keyEvent', callback: (event: InputKeyEvent) => boolean): void

订阅硬键盘（即物理键盘）事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'keyEvent'。 |
| callback | (event: [InputKeyEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-keyevent#keyevent)) => boolean | 是 | 
回调函数，入参为按键事件信息，返回值类型为布尔类型。

\- 入参按键事件信息的数据类型为[InputKeyEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-keyevent#keyevent)。

\- 若按键事件被事件订阅者消费，则callback应返回true，否则返回false。

 |

**示例：**

```ts
import type { KeyEvent } from '@kit.InputKit';

inputMethodEngine.getKeyboardDelegate().on('keyEvent', (keyEvent: KeyEvent) => {
  console.info(`inputMethodEngine keyEvent.action:${ keyEvent.action}`);
  console.info(`inputMethodEngine keyEvent.key.code: ${keyEvent.key.code}`);
  console.info(`inputMethodEngine keyEvent.ctrlKey: ${keyEvent.ctrlKey}`);
  console.info(`inputMethodEngine keyEvent.unicodeChar: ${keyEvent.unicodeChar}`);
  return true;
});
```

#### \[h2\]off('keyEvent')10+

off(type: 'keyEvent', callback?: (event: InputKeyEvent) => boolean): void

取消订阅硬键盘（即物理键盘）事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 设置监听类型，固定取值为'keyEvent'。 |
| callback | (event: [InputKeyEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-keyevent#keyevent)) => boolean | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```ts
import type { KeyEvent } from '@kit.InputKit';

inputMethodEngine.getKeyboardDelegate().off('keyEvent', (keyEvent: KeyEvent) => {
  console.info('This is a callback function which will be deregistered.');
  return true;
});
inputMethodEngine.getKeyboardDelegate().off('keyEvent');
```

#### \[h2\]on('cursorContextChange')

on(type: 'cursorContextChange', callback: (x: number, y:number, height:number) => void): void

订阅光标变化事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 光标变化事件，固定取值为'cursorContextChange'。 |
| callback | (x: number, y: number, height: number) => void | 是 | 
回调函数，返回光标信息。

\- x为光标上端的x坐标值，y为光标上端的y坐标值，height为光标的高度值。

 |

**示例：**

```ts
inputMethodEngine.getKeyboardDelegate().on('cursorContextChange', (x: number, y: number, height: number) => {
  console.info('inputMethodEngine cursorContextChange x:' + x);
  console.info('inputMethodEngine cursorContextChange y:' + y);
  console.info('inputMethodEngine cursorContextChange height:' + height);
});
```

#### \[h2\]off('cursorContextChange')

off(type: 'cursorContextChange', callback?: (x: number, y: number, height: number) => void): void

取消订阅光标变化事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 光标变化事件，固定取值为'cursorContextChange'。 |
| callback | (x: number, y:number, height:number) => void | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```ts
inputMethodEngine.getKeyboardDelegate().off('cursorContextChange', (x: number, y: number, height: number) => {
  console.info('delete cursorContextChange notification.');
});
```

#### \[h2\]on('selectionChange')

on(type: 'selectionChange', callback: (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void): void

订阅文本选择范围变化事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 文本选择变化事件，固定取值为'selectionChange'。 |
| callback | (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void | 是 | 
回调函数，返回文本选择信息。

\- oldBegin为变化前被选中文本的起始下标，oldEnd为变化前被选中文本的终止下标。

\- newBegin为变化后被选中文本的起始下标，newEnd为变化后被选中文本的终止下标。

 |

**示例：**

```ts
inputMethodEngine.getKeyboardDelegate()
  .on('selectionChange', (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => {
    console.info('selectionChange oldBegin:' + oldBegin);
    console.info('selectionChange oldEnd:' + oldEnd);
    console.info('selectionChange newBegin:' + newBegin);
    console.info('selectionChange newEnd:' + newEnd);
  });
```

#### \[h2\]off('selectionChange')

off(type: 'selectionChange', callback?: (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void): void

取消订阅文本选择范围变化事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 文本选择变化事件，固定取值为'selectionChange'。 |
| callback | (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```ts
inputMethodEngine.getKeyboardDelegate()
  .off('selectionChange', (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => {
    console.info('delete selectionChange notification.');
  });
```

#### \[h2\]on('textChange')

on(type: 'textChange', callback: (text: string) => void): void

订阅文本内容变化事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 文本变化事件，固定取值为'textChange'。 |
| callback | (text: string) => void | 是 | 回调函数，返回订阅的文本内容。 |

**示例：**

```ts
inputMethodEngine.getKeyboardDelegate().on('textChange', (text: string) => {
  console.info('inputMethodEngine textChange. text:' + text);
});
```

#### \[h2\]off('textChange')

off(type: 'textChange', callback?: (text: string) => void): void

取消订阅文本内容变化事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 文本变化事件，固定取值为'textChange'。 |
| callback | (text: string) => void | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```ts
inputMethodEngine.getKeyboardDelegate().off('textChange', (text: string) => {
  console.info('delete textChange notification. text:' + text);
});
```

#### \[h2\]on('editorAttributeChanged')10+

on(type: 'editorAttributeChanged', callback: (attr: EditorAttribute) => void): void

订阅编辑框属性变化事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 文本变化事件，固定取值为'editorAttributeChanged'。 |
| callback | (attr: [EditorAttribute](#editorattribute)) => void | 是 | 回调函数，返回变化的编辑框属性。 |

**示例：**

```ts
inputMethodEngine.getKeyboardDelegate()
  .on('editorAttributeChanged', (attr: inputMethodEngine.EditorAttribute) => {
    console.info(`Succeeded in receiving attribute of editor, inputPattern = ${attr.inputPattern}, enterKeyType = ${attr.enterKeyType}`);
  });
```

#### \[h2\]off('editorAttributeChanged')10+

off(type: 'editorAttributeChanged', callback?: (attr: EditorAttribute) => void): void

取消订阅编辑框属性变化事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 文本变化事件，固定取值为'editorAttributeChanged'。 |
| callback | (attr: [EditorAttribute](#editorattribute)) => void | 否 | 所要取消订阅的回调处理函数。参数不填写时，默认取消订阅type对应的所有回调事件。 |

**示例：**

```ts
inputMethodEngine.getKeyboardDelegate().off('editorAttributeChanged');
```

#### Panel10+

下列API均需使用[createPanel](#createpanel10)获取到Panel实例后，通过实例调用。

#### \[h2\]setUiContent10+

setUiContent(path: string, callback: AsyncCallback<void>): void

为当前的输入法面板加载具体页面内容，使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 具体页面的路径。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当面板页面内容加载成功，err为undefined，否则err为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

panel.setUiContent('pages/page2/page2', (err: BusinessError) => {
  if (err) {
    console.error(`Failed to setUiContent. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in setting the content.');
});
```

#### \[h2\]setUiContent10+

setUiContent(path: string): Promise<void>

为当前的输入法面板加载具体页面内容，使用Promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 具体页面的路径。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

panel.setUiContent('pages/page2/page2').then(() => {
  console.info('Succeeded in setting the content.');
}).catch((err: BusinessError) => {
  console.error(`Failed to setUiContent. Code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]setUiContent10+

setUiContent(path: string, storage: LocalStorage, callback: AsyncCallback<void>): void

为当前的输入法面板加载与LocalStorage相关联的具体页面内容，使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | LocalStorage相关联的具体页面的路径。 |
| storage | [LocalStorage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-state-management#localstorage9) | 是 | 存储单元，为应用程序范围内的可变和不可变状态属性提供存储。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当面板页面内容加载成功，err为undefined，否则err为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let storage: LocalStorage = new LocalStorage();
storage.setOrCreate('storageSimpleProp', 121);
panel.setUiContent('pages/page2/page2', storage, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to setUiContent. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in setting the content.');
});
```

#### \[h2\]setUiContent10+

setUiContent(path: string, storage: LocalStorage): Promise<void>

为当前面板加载与LocalStorage相关联的具体页面内容，使用Promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| path | string | 是 | 设置加载页面的路径。 |
| storage | [LocalStorage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-state-management#localstorage9) | 是 | 存储单元，为应用程序范围内的可变状态属性和非可变状态属性提供存储。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let storage: LocalStorage = new LocalStorage();
storage.setOrCreate('storageSimpleProp', 121);
panel.setUiContent('pages/page2/page2', storage).then(() => {
  console.info('Succeeded in setting the content.');
}).catch((err: BusinessError) => {
  console.error(`Failed to setUiContent. Code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]resize10+

resize(width: number, height: number, callback: AsyncCallback<void>): void

改变当前输入法面板的大小，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/KHEZi7lFQWmIhToGcPvv_A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=C2A69F18391062B5943CBA9005943206FF56CCDC709BE92A3912A907E6DB83D4)

面板宽度不超出屏幕宽度，面板高度不高于屏幕高度的0.7倍。

手机的PanelFlag是FLG\_FLOATING且面板宽度在0~288vp之间时，面板底部功能键将随面板宽度动态调整大小，为了保证最佳用户体验，建议面板宽度不小于90vp。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| width | number | 是 | 目标面板的宽度，单位为px。该参数应为大于或等于0的整数，不超出屏幕宽度。 |
| height | number | 是 | 目标面板的高度，单位为px。该参数应为大于或等于0的整数，不高于屏幕高度的0.7倍。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当面板大小改变成功，err为undefined，否则err为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

panel.resize(500, 1000, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to resize panel. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in changing the panel size.');
});
```

#### \[h2\]resize10+

resize(width: number, height: number): Promise<void>

改变当前输入法面板的大小，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/9RDvtXYIRqKyNuLYaxrUUA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=5A29A45456D594868FCCFD08963EB7B912324FA9D7B02B5BF5137F15F33C362F)

面板宽度不超出屏幕宽度，面板高度不高于屏幕高度的0.7倍。

手机的PanelFlag是FLG\_FLOATING且面板宽度在0~288vp之间时，面板底部功能键将随面板宽度动态调整大小，为了保证最佳用户体验，建议面板宽度不小于90vp。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| width | number | 是 | 目标面板的宽度，单位为px。该参数应为大于或等于0的整数，不超出屏幕宽度。 |
| height | number | 是 | 目标面板的高度，单位为px。该参数应为大于或等于0的整数，不高于屏幕高度的0.7倍。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

panel.resize(500, 1000).then(() => {
  console.info('Succeeded in changing the panel size.');
}).catch((err: BusinessError) => {
  console.error(`Failed to resize panel. Code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]moveTo10+

moveTo(x: number, y: number, callback: AsyncCallback<void>): void

移动面板位置，使用callback异步回调。[面板状态](#panelflag10)为固定态时，不产生实际移动效果。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| x | number | 是 | 横轴方向移动的值，值大于0表示右移，单位为px。该参数应为整数。 |
| y | number | 是 | 纵轴方向移动的值，值大于0表示下移，单位为px。该参数应为整数。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当面板位置移动成功，err为undefined，否则err为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

panel.moveTo(300, 300, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to move panel. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in moving the panel.');
});
```

#### \[h2\]moveTo10+

moveTo(x: number, y: number): Promise<void>

移动面板位置，使用promise异步回调。[面板状态](#panelflag10)为固定态时，不产生实际移动效果。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| x | number | 是 | 横轴方向移动的值，值大于0表示右移，单位为px。该参数应为整数。 |
| y | number | 是 | 纵轴方向移动的值，值大于0表示下移，单位为px。该参数应为整数。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

panel.moveTo(300, 300).then(() => {
  console.info('Succeeded in moving the panel.');
}).catch((err: BusinessError) => {
  console.error(`Failed to move panel. Code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]startMoving15+

startMoving(): void

发送移动命令给窗口，不产生实际移动效果（仅在鼠标点击作用才可以移动）。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 801 | capability not supported. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800013 | window manager service error. |
| 12800017 | invalid panel type or panel flag. |

**示例：**

```ts
panel.startMoving();
```

#### \[h2\]getDisplayId15+

getDisplayId(): Promise<number>

获取当前窗口的所在id，使用Promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | Promise对象。返回窗口的displayId。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800013 | window manager service error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

panel.getDisplayId().then((result: number) => {
  console.info('get displayId:' + result);
}).catch((err: BusinessError) => {
  console.error(`Failed to get displayId. Code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]show10+

show(callback: AsyncCallback<void>): void

显示当前输入法面板，使用callback异步回调。输入法应用与编辑框绑定成功后可正常调用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | 是 | 回调函数。当面板显示成功，err为undefined，否则err为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

panel.show((err: BusinessError) => {
  if (err) {
    console.error(`Failed to show panel. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in showing the panel.');
});
```

#### \[h2\]show10+

show(): Promise<void>

显示当前输入法面板，使用promise异步回调。输入法应用与编辑框绑定成功后可正常调用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

panel.show().then(() => {
  console.info('Succeeded in showing the panel.');
}).catch((err: BusinessError) => {
  console.error(`Failed to show panel. Code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]hide10+

hide(callback: AsyncCallback<void>): void

隐藏当前输入法面板，使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | 是 | 回调函数。当面板隐藏成功，err为undefined，否则err为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

panel.hide((err: BusinessError) => {
  if (err) {
    console.error(`Failed to hide panel. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in hiding the panel.');
});
```

#### \[h2\]hide10+

hide(): Promise<void>

隐藏当前输入法面板，使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

panel.hide().then(() => {
  console.info('Succeeded in hiding the panel.');
}).catch((err: BusinessError) => {
  console.error(`Failed to hide panel. Code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]adjustPanelRect12+

adjustPanelRect(flag: PanelFlag, rect: PanelRect): void

预设置输入法应用横竖屏大小。接口调用完毕表示adjust请求已提交到输入法框架，不表示执行完毕。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/3G1StGDOTxO9shuOfXsYkw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=BEC0BCED2543B82FA817F648F84977038B617DA4D532A5BD4D6389B5F7D985AB)

仅用于SOFT\_KEYBOARD类型，状态为FLG\_FIXED或FLG\_FLOATING的面板。

此接口为同步接口，接口返回仅代表系统侧收到设置的请求，不代表已完成设置。

手机的PanelFlag是FLG\_FLOATING且面板宽度在0~288vp之间时，面板底部功能键将随面板宽度动态调整大小，为了保证最佳用户体验，建议面板宽度不小于90vp。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| flag | [PanelFlag](#panelflag10) | 是 | 目标面板状态类型。类型为FLG\_FIXED或FLG\_FLOATING。 |
| rect | [PanelRect](#panelrect12) | 是 | 目标面板横屏状态及竖屏状态的横坐标，纵坐标，宽度以及高度。固定态：高度不能超过屏幕高度的70%，宽度不能超过屏幕宽度；悬浮态：高度不能超过屏幕高度，宽度不能超过屏幕宽度。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800013 | window manager service error. |

**示例：**

```ts
import { window } from '@kit.ArkUI';

let landscapeRect: window.Rect = {
  left: 100,
  top: 100,
  width: 400,
  height: 400
};

let portraitRect: window.Rect = {
  left: 200,
  top: 200,
  width: 300,
  height: 300
};

// 目标面板状态类型
let panelFlag: inputMethodEngine.PanelFlag = inputMethodEngine.PanelFlag.FLG_FIXED;
// 目标面板横屏状态及竖屏状态的横坐标，纵坐标，宽度以及高度
let panelRect: inputMethodEngine.PanelRect = {
  landscapeRect: landscapeRect,
  portraitRect: portraitRect
};
panel.adjustPanelRect(panelFlag, panelRect);
```

#### \[h2\]adjustPanelRect15+

adjustPanelRect(flag: PanelFlag, rect: EnhancedPanelRect): void

预设置输入法应用横竖屏大小、位置、自定义避让区域以及热区。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/IRL2qWStRrKxF_AImjisCg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=F5B6EF3CE2CFBDE5321E1ADE788A448C21E359988889B3A23A80FD63D3968498)

仅用于SOFT\_KEYBOARD类型，状态为FLG\_FIXED或FLG\_FLOATING的面板。此接口兼容[adjustPanelRect](#adjustpanelrect12)的调用方法，若入参rect仅填写属性landscapeRect和portraitRect，则默认调用[adjustPanelRect](#adjustpanelrect12)。

此接口为同步接口，接口返回仅代表系统侧收到设置的请求，不代表已完成设置。

手机的PanelFlag是FLG\_FLOATING且面板宽度在0~288vp之间时，面板底部功能键将随面板宽度动态调整大小，为了保证最佳用户体验，建议面板宽度不小于90vp。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| flag | [PanelFlag](#panelflag10) | 是 | 目标面板状态类型。类型为FLG\_FIXED或FLG\_FLOATING。 |
| rect | [EnhancedPanelRect](#enhancedpanelrect15) | 是 | 目标面板横屏状态及竖屏状态的位置、大小、避让区域以及热区。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800013 | window manager service error. |
| 12800017 | invalid panel type or panel flag. |

**示例：**

```ts
import { window } from '@kit.ArkUI';

let landscapeRect1: window.Rect = {
  left: 300,
  top: 650,
  width: 2000,
  height: 500
};
let landscapeInputRegion: Array<window.Rect> = [landscapeRect1];

let portraitRect1: window.Rect = {
  left: 0,
  top: 1800,
  width: 1200,
  height: 800
}
let portraitInputRegion: Array<window.Rect> = [portraitRect1];
// 目标面板状态类型。
let panelFlag: inputMethodEngine.PanelFlag = inputMethodEngine.PanelFlag.FLG_FIXED;
// 目标面板横屏状态及竖屏状态的位置、大小、避让区域以及热区。
let panelRect: inputMethodEngine.EnhancedPanelRect = {
  landscapeAvoidY: 650,
  landscapeInputRegion: landscapeInputRegion,
  portraitAvoidY: 1800,
  portraitInputRegion: portraitInputRegion,
  fullScreenMode: true
};
panel.adjustPanelRect(panelFlag, panelRect);
```

#### \[h2\]updateRegion15+

updateRegion(inputRegion: Array<window.Rect>): void

更新当前状态下输入法面板内的热区。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/PVPLX5CFQOua6XfvnuDOXw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=39A01FDC48F2FFBBCD5F6D9CF59927BD661EDD60620D6B8083900F33C5218581)

仅用于SOFT\_KEYBOARD类型，状态为FLG\_FIXED或FLG\_FLOATING的面板。

此接口为同步接口，接口返回仅代表系统侧收到更新热区的请求，不代表已完成热区更新。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| inputRegion | Array<[window.Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-i#rect7)\> | 是 | 
面板内接收输入事件的区域。

\- 数组大小限制为\[1, 4\]。

\- 传入的热区位置是相对于输入法面板窗口左顶点的位置。

 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800013 | window manager service error. |
| 12800017 | invalid panel type or panel flag. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

let inputRegion: Array<window.Rect> = [{
  left: 300,
  top: 650,
  width: 2000,
  height: 500
}];
panel.updateRegion(inputRegion);
```

#### \[h2\]on('show')10+

on(type: 'show', callback: () => void): void

监听当前面板显示状态，使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 监听当前面板的状态类型，固定取值为'show'。 |
| callback | () => void | 是 | 回调函数。 |

**示例：**

```ts
panel.on('show', () => {
  console.info('Panel is showing.');
});
```

#### \[h2\]on('hide')10+

on(type: 'hide', callback: () => void): void

监听当前面板隐藏状态，使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 监听当前面板的状态类型，固定取值为'hide'。 |
| callback | () => void | 是 | 回调函数。 |

**示例：**

```ts
panel.on('hide', () => {
  console.info('Panel is hiding.');
});
```

#### \[h2\]on('sizeChange')12+

on(type: 'sizeChange', callback: SizeChangeCallback): void

监听当前面板大小变化，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/PLQ5N3GdTO6wO__yvVOuFA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=B814C3C23E3E66E6010EE17893261F791A8D18E6E8ED8A005752533245C8512D)

仅用于SOFT\_KEYBOARD类型，状态为FLG\_FIXED或FLG\_FLOATING的面板。输入法通过adjustPanelRect等接口对面板大小进行调节时，系统会根据一定规则校验计算出最终的数值（例如超出屏幕等场景），输入法应用可通过该回调获取的真实面板大小，完成最终的面板布局刷新。

-   从API version 12-14开始支持，此接口回调函数中仅包含[window.Size](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-i#size7)类型的必选参数。
-   从API version 15起，调用[adjustPanelRect](#adjustpanelrect15)接口后，此接口回调函数增加[KeyboardArea](#keyboardarea15)类型的可选参数。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 监听当前面板的大小是否产生变化，固定值为'sizeChange'。 |
| callback | [SizeChangeCallback](#sizechangecallback15) | 是 | 回调函数。返回当前软键盘面板的大小，包含宽度和高度值。 |

**示例：**

```ts
import { window } from '@kit.ArkUI';

panel.on('sizeChange', (windowSize: window.Size) => {
  console.info(`panel size changed, width: ${windowSize.width}, height: ${windowSize.height}`);
});

panel.on('sizeChange', (windowSize: window.Size, keyboardArea: inputMethodEngine.KeyboardArea) => {
  console.info(`panel size changed, windowSize: ${windowSize.width}, ${windowSize.height}, ` +
    `keyboardArea: ${keyboardArea.top}, ${keyboardArea.bottom}, ${keyboardArea.left}, ${keyboardArea.right}`);
});
```

#### \[h2\]off('show')10+

off(type: 'show', callback?: () => void): void

取消监听当前面板的显示状态，使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 取消监听当前面板的状态类型，固定取值为'show'。 |
| callback | () => void | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
panel.off('show');
```

#### \[h2\]off('hide')10+

off(type: 'hide', callback?: () => void): void

取消监听当前面板的隐藏状态，使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 要取消监听的当前面板状态类型，固定取值为'hide'。 |
| callback | () => void | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
panel.off('hide');
```

#### \[h2\]off('sizeChange')12+

off(type: 'sizeChange', callback?: SizeChangeCallback): void

取消监听当前面板大小变化，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/hVcvREvgSPiViU2m5I9_RQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=9BF2531BC3ADFDE42321EA05A40683EB751ED12965F92B652D777B02C8C0DD0A)

仅用于SOFT\_KEYBOARD类型，状态为FLG\_FIXED或FLG\_FLOATING的面板。输入法通过adjustPanelRect等接口对面板大小进行调节时，系统会根据一定规则校验计算出最终的数值（例如超出屏幕等场景），输入法应用可通过该回调获取的真实面板大小，完成最终的面板布局刷新。

-   从API version 12-14开始支持，此接口回调函数中仅包含[window.Size](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-i#size7)类型的必选参数。
-   从API version 15起，调用[adjustPanelRect](#adjustpanelrect15)接口后，此接口回调函数增加[KeyboardArea](#keyboardarea15)类型的可选参数。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 监听当前面板的大小是否产生变化，固定取值为'sizeChange'。 |
| callback | [SizeChangeCallback](#sizechangecallback15) | 否 | 回调函数。返回当前软键盘面板的大小，包含宽度和高度值。 |

**示例：**

```ts
import { window } from '@kit.ArkUI';

panel.off('sizeChange', (windowSize: window.Size) => {
  console.info(`panel size changed, width: ${windowSize.width}, height: ${windowSize.height}`);
});
```

#### \[h2\]changeFlag10+

changeFlag(flag: PanelFlag): void

将输入法应用的面板状态改变为其他[PanelFlag](#panelflag10)形态，仅对[SOFT\_KEYBOARD](#paneltype10)生效。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| flag | [PanelFlag](#panelflag10) | 是 | 目标面板状态类型。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
let panelFlag: inputMethodEngine.PanelFlag = inputMethodEngine.PanelFlag.FLG_FIXED;
panel.changeFlag(panelFlag);
```

#### \[h2\]setPrivacyMode11+

setPrivacyMode(isPrivacyMode: boolean): void

将输入法应用的面板设置为隐私模式，隐私模式不可被录屏、截屏。

**需要权限：** ohos.permission.PRIVACY\_WINDOW

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| isPrivacyMode | boolean | 是 | 
是否设置隐私模式。

\- 值为true，表示将设置为隐私模式。

\- 值为false，表示将设置为非隐私模式。

 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | permissions check fails. |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```ts
let isPrivacyMode: boolean = true;
panel.setPrivacyMode(isPrivacyMode);
```

#### \[h2\]setImmersiveMode15+

setImmersiveMode(mode: ImmersiveMode): void

设置输入法应用的沉浸模式。只能设置不使用沉浸模式(NONE\_IMMERSIVE)、浅色沉浸模式(LIGHT\_IMMERSIVE)或深色沉浸模式(DARK\_IMMERSIVE)。不能设置为沉浸模式(IMMERSIVE)。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| mode | [ImmersiveMode](#immersivemode15) | 是 | 沉浸模式。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800013 | window manager service error. |

**示例：**

```ts
panel.setImmersiveMode(inputMethodEngine.ImmersiveMode.LIGHT_IMMERSIVE);
```

#### \[h2\]getImmersiveMode15+

getImmersiveMode(): ImmersiveMode

获取输入法应用的沉浸模式。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [ImmersiveMode](#immersivemode15) | 沉浸模式。 |

**示例：**

```ts
let mode: inputMethodEngine.ImmersiveMode = panel.getImmersiveMode();
```

#### \[h2\]setImmersiveEffect20+

setImmersiveEffect(effect: ImmersiveEffect): void

设置输入法应用的沉浸效果。

-   只有在[启用沉浸式模式](#setimmersivemode15)时，才能使用渐变模式和流光模式。
-   只有在启用渐变模式时，才能使用流光模式。
-   未启用渐变模式时，渐变高度必须为0px。
-   只有系统应用才能设置流光模式。
-   必须先调用以下任一接口，才能调用当前接口：
    -   [adjustPanelRect](#adjustpanelrect12)(支持API version 12)
    -   [adjustPanelRect](#adjustpanelrect15)(支持API version 15)
    -   [resize](#resize10)(支持API version 10)

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| effect | [ImmersiveEffect](#immersiveeffect20) | 是 | 沉浸效果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 801 | capability not supported. |
| 12800002 | input method engine error. Possible causes:1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800013 | window manager service error. |
| 12800020 | invalid immersive effect. 1.The gradient mode and the fluid light mode can only be used when the immersive mode is enabled. 2.The fluid light mode can only be used when the gradient mode is enabled. 3.When the gradient mode is not enabled, the gradient height can only be 0. |
| 12800021 | this operation is allowed only after adjustPanelRect or resize is called. |

**示例：**

```ts
let effect: inputMethodEngine.ImmersiveEffect = {
  gradientHeight: 100,
  gradientMode: inputMethodEngine.GradientMode.LINEAR_GRADIENT
}
panel.setImmersiveEffect(effect);
```

#### \[h2\]setKeepScreenOn20+

setKeepScreenOn(isKeepScreenOn: boolean): Promise<void>

设置屏幕常亮。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/yY8PucRYT-q4ZIniiu1-YA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=416B74B1B9E7EA04CFE79E700A63FF7E83BEC7BF143CF36940D74EBE597EB1BC)

-   当键盘拉起时设置常亮生效，键盘关闭则自动失效。
-   规范使用该接口：必要场景（例如：语音输入）下，设置该属性为true；退出必要场景后，重置该属性为false；其他场景下，不使用该接口。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| isKeepScreenOn | boolean | 是 | 是否设置屏幕常亮。true表示打开屏幕常亮，false表示关闭屏幕常亮。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12800013 | window manager service error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

panel.setKeepScreenOn(true).then(() => {
  console.info(`setKeepScreenOn success.`);
}).catch((error: BusinessError) => {
  console.error(`setKeepScreenOn failed, code: ${error.code}, message: ${error.message}`);
})
```

#### \[h2\]getSystemPanelCurrentInsets21+

getSystemPanelCurrentInsets(displayId: number): Promise<SystemPanelInsets>

获取指定屏幕当前状态（例如：折叠或展开）下，当前输入法键盘状态（例如：悬浮或固定）下输入法软键盘相对系统面板的偏移区域。使用Promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| displayId | number | 是 | 输入法键盘所在屏幕的displayId，可通过[getDisplayId](#getdisplayid15)获取 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[SystemPanelInsets](#systempanelinsets21)\> | Promise对象。输入法键盘与系统面板的偏移区域。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12800013 | window manager service error. |
| 12800017 | invalid panel type or panel flag. Possible causes: 1. Current panel's type is not SOFT\_KEYBOARD. 2. Panel's flag is not FLG\_FIXED or FLG\_FLOATING. |
| 12800022 | invalid displayId. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { inputMethodEngine } from '@kit.IMEKit';

let inputMethodAbility: inputMethodEngine.InputMethodAbility = inputMethodEngine.getInputMethodAbility();
let panelConfig: inputMethodEngine.PanelInfo = {
  type: inputMethodEngine.PanelType.SOFT_KEYBOARD,
  flag: inputMethodEngine.PanelFlag.FLG_FIXED
}
// 以下逻辑需要在输入法InputMethodExtensionAbility中执行，this.context是InputMethodExtensionAbility的上下文
inputMethodAbility.createPanel(this.context, panelConfig).then( (panel: inputMethodEngine.Panel) =>{
  panel.getDisplayId().then((displayId: number) => {
    panel.getSystemPanelCurrentInsets(displayId).then((insets: inputMethodEngine.SystemPanelInsets) => {
      console.info(`getSystemPanelCurrentInsets success, insets is { left: ${insets.left}, right: ${insets.right}, bottom: ${insets.bottom} }`);
    }).catch((error: BusinessError) => {
      console.error(`getSystemPanelCurrentInsets failed, code: ${error.code}, message: ${error.message}`);
    })
  });
})
```

#### \[h2\]setSystemPanelButtonColor22+

setSystemPanelButtonColor(fillColor: string | undefined, backgroundColor: string | undefined): Promise<void>

设置当前面板功能键颜色和功能键的背景颜色。使用Promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fillColor | string|undefined | 是 | 功能键的颜色，取值范围为\[#01000000, #FFFFFFFF\] 或 \[#000000, #FFFFFF\]，不支持具有完全透明Alpha通道（#00xxxxxx）的值。 |
| backgroundColor | string|undefined | 是 | 功能键的背景颜色，取值范围为\[#01000000, #FFFFFFFF\] 或 \[#000000, #FFFFFF\]，不支持具有完全透明Alpha通道（#00xxxxxx）的值。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let fillColor = "#FFFF00";
  let backgroundColor = "#0000FF";
  this.panel.setSystemPanelButtonColor(fillColor, backgroundColor).then(() => {
    console.info(`setSystemPanelButtonColor success.`);
  }).catch((error: BusinessError) => {
    console.error(`setSystemPanelButtonColor failed, code: ${error.code}, message: ${error.message}`);
  })
} catch (err) {
  let error = err as BusinessError;
  console.error(`setSystemPanelButtonColor failed, code: ${error.code}, message: ${error.message}`);
}
```

#### KeyboardController

下列API均需使用[on('inputStart')](#oninputstart9)获取到KeyboardController实例后，通过实例调用。

#### \[h2\]hide9+

hide(callback: AsyncCallback<void>): void

隐藏输入法。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | 是 | 回调函数。当输入法隐藏成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

keyboardController.hide((err: BusinessError) => {
  if (err) {
    console.error(`Failed to hide. Code:${err.code}, message:${err.message}`);
    return;
  }
  console.info('Succeeded in hiding keyboard.');
});
```

#### \[h2\]hide9+

hide(): Promise<void>

隐藏输入法。使用promise异步回调。

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

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

keyboardController.hide().then(() => {
  console.info('Succeeded in hiding keyboard.');
}).catch((err: BusinessError) => {
  console.error(`Failed to hide. Code:${err.code}, message:${err.message}`);
});
```

#### \[h2\]hideKeyboard(deprecated)

hideKeyboard(callback: AsyncCallback<void>): void

隐藏输入法。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/7jlTTWdNQY-710bc7a7W9Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=9B9F62DBB7C643A70B238826C989438D31E319E1984E0D2F67013C69DB9137EC)

从API version 8开始支持，API version 9开始废弃，建议使用[hide](#hide9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | 是 | 回调函数。当输入法隐藏成功，err为undefined，否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

keyboardController.hideKeyboard((err: BusinessError) => {
  if (err) {
    console.error(`Failed to hideKeyboard. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in hiding keyboard.');
});
```

#### \[h2\]hideKeyboard(deprecated)

hideKeyboard(): Promise<void>

隐藏输入法。使用promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/J2DWqBXiQL2FdkwMIRuFmg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=10854FC56CFB4ED2143F50B7AAB8CAD98036CDD3EF5C4A4BB78FEBE170D82736)

从API version 8开始支持，API version 9开始废弃，建议使用[hide](#hide9-1)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

keyboardController.hideKeyboard().then(() => {
  console.info('Succeeded in hiding keyboard.');
}).catch((err: BusinessError) => {
  console.info(`Failed to hideKeyboard. Code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]exitCurrentInputType11+

exitCurrentInputType(callback: AsyncCallback<void>): void

退出当前输入类型，仅支持系统配置的默认输入法应用调用。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | 是 | 回调函数。当退出当前输入类型成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800010 | not the preconfigured default input method. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

keyboardController.exitCurrentInputType((err: BusinessError) => {
  if (err) {
    console.error(`Failed to exit current input type. Code:${err.code}, message:${err.message}`);
    return;
  }
  console.info('Succeeded in exiting current input type.');
});
```

#### \[h2\]exitCurrentInputType11+

exitCurrentInputType(): Promise<void>

退出当前输入类型，仅支持系统配置的默认输入法应用调用。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800010 | not the preconfigured default input method. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

keyboardController.exitCurrentInputType().then(() => {
  console.info('Succeeded in exiting current input type.');
}).catch((err: BusinessError) => {
  console.error(`Failed to exit current input type. Code:${err.code}, message:${err.message}`);
});
```

#### SecurityMode11+

输入法的安全模式，如BASIC或FULL。

**系统能力**: SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| BASIC | 0 | 基础访问模式，基础打字模式，会限制网络访问。 |
| FULL | 1 | 完全访问模式，不做限制，可以访问网络。 |

#### ExtendAction10+

编辑框中文本的扩展编辑操作类型，如剪切、复制等。

**系统能力**: SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| SELECT\_ALL | 0 | 全选。 |
| CUT | 3 | 剪切。 |
| COPY | 4 | 复制。 |
| PASTE | 5 | 粘贴。 |

#### Direction10+

光标的移动方向。

**系统能力**: SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| CURSOR\_UP | 1 | 向上。 |
| CURSOR\_DOWN | 2 | 向下。 |
| CURSOR\_LEFT | 3 | 向左。 |
| CURSOR\_RIGHT | 4 | 向右。 |

#### Range10+

选中的文本范围。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| start | number | 否 | 否 | 选中文本的首字符在编辑框的索引值。 |
| end | number | 否 | 否 | 选中文本的末字符在编辑框的索引值。 |

#### Movement10+

选中文本时，光标移动的方向

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| direction | [Direction](#direction10) | 否 | 否 | 选中文本时，光标的移动方向。 |

#### MessageHandler15+

自定义通信对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/wRyiqQzjSj2X_LSWxsQ4hw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=B1FA5CDA9D6C21EF4D2C1B7AC415B92919B2369AFB7356DC22E26F66B4FBA67B)

开发者可通过注册此对象来接收已绑定当前输入法应用的编辑框应用所发送的自定义通信数据，接收到自定义通信数据时会触发此对象中[onMessage](#onmessage15)回调函数。

此对象全局唯一，多次注册仅保留最后一次注册的对象及有效性，并触发上一个已注册对象的[onTerminated](#onterminated15)回调函数。

若取消注册全局已注册的对象时，会触发被取消对象中[onTerminated](#onterminated15)回调函数。

#### \[h2\]onMessage15+

onMessage(msgId: string, msgParam?: ArrayBuffer): void

接收已绑定当前输入法应用的编辑框应用发送的自定义数据回调函数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/w1KpwGrxTTauXEQL8AbIEw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=3589F4B785244DC86995C9CF0820916CCC9ABF194833C3DFF8A3FBC7A6341E05)

当已注册的[MessageHandler](#messagehandler15)接收到来自已绑定当前输入法应用的编辑框应用所发送的自定义通信数据时，会触发该回调函数。

msgId为必选参数，msgParam为可选参数。存在收到仅有msgId自定义数据的可能，需与数据发送方确认自定义数据。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| msgId | string | 是 | 接收到的自定义通信数据的标识符。 |
| msgParam | ArrayBuffer | 否 | 接收到的自定义通信数据的消息体。 |

**示例：**

```ts
inputMethodEngine.getInputMethodAbility()
  .on('inputStart',
    (kbController: inputMethodEngine.KeyboardController, client: inputMethodEngine.InputClient) => {
      let keyboardController: inputMethodEngine.KeyboardController = kbController;
      let inputClient: inputMethodEngine.InputClient = client;
      let messageHandler: inputMethodEngine.MessageHandler = {
        onTerminated(): void {
          console.info('OnTerminated.');
        },
        onMessage(msgId: string, msgParam?: ArrayBuffer): void {
          console.info(`recv message, msgId is ${msgId}, msgParam is ${JSON.stringify(msgParam)}`);
        }
      }
      inputClient.recvMessage(messageHandler);
    });
```

#### \[h2\]onTerminated15+

onTerminated(): void

监听对象终止回调函数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/J1KS9frHTMawE-DXFe9xHA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=5D02AB95E14C2468584EC932D1C93D2597E01850140114D9D976B977D3F040CC)

当应用注册新的[MessageHandler](#messagehandler15)对象时，会触发上一个已注册[MessageHandler](#messagehandler15)对象的[onTerminated](#onterminated15)回调函数。

当应用取消注册时，会触发当前已注册[MessageHandler](#messagehandler15)对象的[onTerminated](#onterminated15)回调函数。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**示例：**

```ts
inputMethodEngine.getInputMethodAbility()
  .on('inputStart',
    (kbController: inputMethodEngine.KeyboardController, client: inputMethodEngine.InputClient) => {
      let keyboardController: inputMethodEngine.KeyboardController = kbController;
      let inputClient: inputMethodEngine.InputClient = client;
      let messageHandler: inputMethodEngine.MessageHandler = {
        onTerminated(): void {
          console.info('OnTerminated.');
        },
        onMessage(msgId: string, msgParam?: ArrayBuffer): void {
          console.info(`recv message, msgId is ${msgId}, msgParam is ${JSON.stringify(msgParam)}`);
        }
      }
      inputClient.recvMessage(messageHandler);
    });
```

#### InputClient9+

下列API均需使用[on('inputStart')](#oninputstart9)获取到InputClient实例后，通过实例调用。

#### \[h2\]sendKeyFunction9+

sendKeyFunction(action:number, callback: AsyncCallback<boolean>): void

发送功能键。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| action | number | 是 | 
功能键键值。

\- 当值为0时，表示无效按键。

\- 当值为1时，表示确认键（即回车键）。

 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当功能键发送成功，err为undefined，data为true；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let action: number = 1;

inputClient.sendKeyFunction(action, (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to sendKeyFunction. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in sending key function.');
  } else {
    console.error('Failed to sendKeyFunction.');
  }
});
```

#### \[h2\]sendKeyFunction9+

sendKeyFunction(action: number): Promise<boolean>

发送功能键。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| action | number | 是 | 
功能键键值。

当值为0时，表示无效按键；

当值为1时，表示确认键（即回车键）。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象。返回true表示功能键发送成功；返回false表示功能键发送失败。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let action: number = 1;
inputClient.sendKeyFunction(action).then((result: boolean) => {
  if (result) {
    console.info('Succeeded in sending key function.');
  } else {
    console.error('Failed to sendKeyFunction.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to sendKeyFunction. Code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]getForward9+

getForward(length:number, callback: AsyncCallback<string>): void

获取光标前固定长度的文本。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| length | number | 是 | 文本长度。不能小于0。 |
| callback | AsyncCallback<string> | 是 | 回调函数。当光标前固定长度的文本获取成功，err为undefined，data为获取到的文本；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.getForward(length, (err: BusinessError, text: string) => {
  if (err) {
    console.error(`Failed to getForward. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in getting forward, text: ' + text);
});
```

#### \[h2\]getForward9+

getForward(length:number): Promise<string>

获取光标前固定长度的文本。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| length | number | 是 | 文本长度。不能小于0 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | Promise对象，返回光标前固定长度的文本。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.getForward(length).then((text: string) => {
  console.info('Succeeded in getting forward, text: ' + text);
}).catch((err: BusinessError) => {
  console.error(`Failed to getForward. Code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]getForwardSync10+

getForwardSync(length:number): string

获取光标前固定长度的文本。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| length | number | 是 | 文本长度。不能小于0。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 返回光标前固定长度的文本。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**示例：**

```ts
let length: number = 1;
let text: string = inputClient.getForwardSync(length);
console.info(`Succeeded in getting forward, text: ${text}`);
```

#### \[h2\]getBackward9+

getBackward(length:number, callback: AsyncCallback<string>): void

获取光标后固定长度的文本。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| length | number | 是 | 文本长度。不能小于0。 |
| callback | AsyncCallback<string> | 是 | 回调函数。当光标后固定长度的文本获取成功，err为undefined，data为获取到的文本；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.getBackward(length, (err: BusinessError, text: string) => {
  if (err) {
    console.error(`Failed to getBackward. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in getting backward, text: ' + text);
});
```

#### \[h2\]getBackward9+

getBackward(length:number): Promise<string>

获取光标后固定长度的文本。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| length | number | 是 | 文本长度。不能小于0。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | Promise对象，返回光标后固定长度的文本。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.getBackward(length).then((text: string) => {
  console.info('Succeeded in getting backward, text: ' + text);
}).catch((err: BusinessError) => {
  console.error(`Failed to getBackward. Code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]getBackwardSync10+

getBackwardSync(length:number): string

获取光标后固定长度的文本。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| length | number | 是 | 文本长度。不能小于0。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 返回光标后固定长度的文本。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**示例：**

```ts
let length: number = 1;
let text: string = inputClient.getBackwardSync(length);
console.info(`Succeeded in getting backward, text: ${text}`);
```

#### \[h2\]deleteForward9+

deleteForward(length:number, callback: AsyncCallback<boolean>): void

删除光标前固定长度的文本。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| length | number | 是 | 文本长度。不能小于0。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当光标前固定长度的文本删除成功，err为undefined，data为true；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.deleteForward(length, (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to deleteForward. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in deleting forward.');
  } else {
    console.error(`Failed to deleteForward.`);
  }
});
```

#### \[h2\]deleteForward9+

deleteForward(length:number): Promise<boolean>

删除光标前固定长度的文本。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| length | number | 是 | 文本长度。不能小于0。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象。返回true表示删除光标前固定长度的文本成功；返回false表示删除光标前固定长度的文本失败。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.deleteForward(length).then((result: boolean) => {
  if (result) {
    console.info('Succeeded in deleting forward.');
  } else {
    console.error('Failed to delete Forward.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to deleteForward. Code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]deleteForwardSync10+

deleteForwardSync(length:number): void

删除光标前固定长度的文本。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| length | number | 是 | 文本长度。不能小于0。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ts
let length: number = 1;
inputClient.deleteForwardSync(length);
```

#### \[h2\]deleteBackward9+

deleteBackward(length:number, callback: AsyncCallback<boolean>): void

删除光标后固定长度的文本。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| length | number | 是 | 文本长度。不能小于0。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当光标后固定长度的文本删除成功，err为undefined，data为true；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.deleteBackward(length, (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to deleteBackward. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in deleting backward.');
  } else {
    console.error(`Failed to deleteBackward.`);
  }
});
```

#### \[h2\]deleteBackward9+

deleteBackward(length:number): Promise<boolean>

删除光标后固定长度的文本。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| length | number | 是 | 文本长度。不能小于0。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象。返回true表示删除光标后固定长度的文本成功；返回false表示删除光标后固定长度的文本失败。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.deleteBackward(length).then((result: boolean) => {
  if (result) {
    console.info('Succeeded in deleting backward.');
  } else {
    console.error('Failed to deleteBackward.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to deleteBackward. Code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]deleteBackwardSync10+

deleteBackwardSync(length:number): void

删除光标后固定长度的文本。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| length | number | 是 | 文本长度。不能小于0。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ts
let length: number = 1;
inputClient.deleteBackwardSync(length);
```

#### \[h2\]insertText9+

insertText(text:string, callback: AsyncCallback<boolean>): void

插入文本。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| text | string | 是 | 文本内容。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当文本插入成功，err为undefined，data为true；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.insertText('test', (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to insertText. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in inserting text.');
  } else {
    console.error('Failed to insertText.');
  }
});
```

#### \[h2\]insertText9+

insertText(text:string): Promise<boolean>

插入文本。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| text | string | 是 | 文本。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象。返回true表示插入文本成功；返回false表示插入文本失败。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.insertText('test').then((result: boolean) => {
  if (result) {
    console.info('Succeeded in inserting text.');
  } else {
    console.error('Failed to insertText.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to insertText. Code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]insertTextSync10+

insertTextSync(text: string): void

插入文本。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| text | string | 是 | 文本内容。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ts
inputClient.insertTextSync('test');
```

#### \[h2\]getEditorAttribute9+

getEditorAttribute(callback: AsyncCallback<EditorAttribute>): void

获取编辑框属性值。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[EditorAttribute](#editorattribute)\> | 是 | 回调函数。当编辑框属性值获取成功，err为undefined，data为编辑框属性值；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.getEditorAttribute((err: BusinessError, editorAttribute: inputMethodEngine.EditorAttribute) => {
  if (err) {
    console.error(`Failed to getEditorAttribute. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`editorAttribute.inputPattern:  ${editorAttribute.inputPattern}`);
  console.info(`editorAttribute.enterKeyType:  ${editorAttribute.enterKeyType}`);
});
```

#### \[h2\]getEditorAttribute9+

getEditorAttribute(): Promise<EditorAttribute>

获取编辑框属性值。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[EditorAttribute](#editorattribute)\> | Promise对象，返回编辑框属性值。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.getEditorAttribute().then((editorAttribute: inputMethodEngine.EditorAttribute) => {
  console.info(`editorAttribute.inputPattern:  ${editorAttribute.inputPattern}`);
  console.info(`editorAttribute.enterKeyType:  ${editorAttribute.enterKeyType}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to getEditorAttribute. Code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]getEditorAttributeSync10+

getEditorAttributeSync(): EditorAttribute

获取编辑框属性值。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [EditorAttribute](#editorattribute) | 编辑框属性对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ts
let editorAttribute: inputMethodEngine.EditorAttribute = inputClient.getEditorAttributeSync();
console.info(`editorAttribute.inputPattern:  ${editorAttribute.inputPattern}`);
console.info(`editorAttribute.enterKeyType:  ${editorAttribute.enterKeyType}`);
```

#### \[h2\]moveCursor9+

moveCursor(direction: number, callback: AsyncCallback<void>): void

移动光标。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| direction | number | 是 | 
光标移动方向。

\- 当值为1时，表示向上。

\- 当值为2时，表示向下。

\- 当值为3时，表示向左。

\- 当值为4时，表示向右。不能小于0。

 |
| callback | AsyncCallback<void> | 是 | 回调函数。当光标移动成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.moveCursor(inputMethodEngine.Direction.CURSOR_UP, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to moveCursor. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in moving cursor.');
});
```

#### \[h2\]moveCursor9+

moveCursor(direction: number): Promise<void>

移动光标。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| direction | number | 是 | 
光标移动方向。

\- 当值为1时，表示向上。

\- 当值为2时，表示向下。

\- 当值为3时，表示向左。

\- 当值为4时，表示向右。不能小于0。

 |

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

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.moveCursor(inputMethodEngine.Direction.CURSOR_UP).then(() => {
  console.info('Succeeded in moving cursor.');
}).catch((err: BusinessError) => {
  console.error(`Failed to moveCursor. Code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]moveCursorSync10+

moveCursorSync(direction: number): void

移动光标。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| direction | number | 是 | 
光标移动方向。

\- 当值为1时，表示向上。

\- 当值为2时，表示向下。

\- 当值为3时，表示向左。

\- 当值为4时，表示向右。不能小于0。

 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ts
inputClient.moveCursorSync(inputMethodEngine.Direction.CURSOR_UP);
```

#### \[h2\]selectByRange10+

selectByRange(range: Range, callback: AsyncCallback<void>): void

根据索引范围选中文本。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| range | [Range](#range10) | 是 | 选中文本的范围。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当成功发送选中事件后，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let range: inputMethodEngine.Range = { start: 0, end: 1 };
inputClient.selectByRange(range, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to selectByRange. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in selecting by range.');
});
```

#### \[h2\]selectByRange10+

selectByRange(range: Range): Promise<void>

根据索引范围选中文本。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| range | [Range](#range10) | 是 | 选中文本的范围。 |

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

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let range: inputMethodEngine.Range = { start: 0, end: 1 };
inputClient.selectByRange(range).then(() => {
  console.info('Succeeded in selecting by range.');
}).catch((err: BusinessError) => {
  console.error(`Failed to selectByRange. Code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]selectByRangeSync10+

selectByRangeSync(range: Range): void

根据索引范围选中文本。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| range | [Range](#range10) | 是 | 选中文本的范围。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ts
let range: inputMethodEngine.Range = { start: 0, end: 1 };
inputClient.selectByRangeSync(range);
```

#### \[h2\]selectByMovement10+

selectByMovement(movement: Movement, callback: AsyncCallback<void>): void

根据光标移动方向选中文本。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| movement | [Movement](#movement10) | 是 | 选中时光标移动的方向。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当成功发送选中事件后，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let movement: inputMethodEngine.Movement = { direction: 1 };
inputClient.selectByMovement(movement, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to selectByMovement. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in selecting by movement.');
});
```

#### \[h2\]selectByMovement10+

selectByMovement(movement: Movement): Promise<void>

根据光标移动方向选中文本。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| movement | [Movement](#movement10) | 是 | 选中时光标移动的方向。 |

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

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let movement: inputMethodEngine.Movement = { direction: 1 };
inputClient.selectByMovement(movement).then(() => {
  console.info('Succeeded in selecting by movement.');
}).catch((err: BusinessError) => {
  console.error(`Failed to selectByMovement. Code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]selectByMovementSync10+

selectByMovementSync(movement: Movement): void

根据光标移动方向选中文本。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| movement | [Movement](#movement10) | 是 | 选中时光标移动的方向。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**示例：**

```ts
let movement: inputMethodEngine.Movement = { direction: 1 };
inputClient.selectByMovementSync(movement);
```

#### \[h2\]getTextIndexAtCursor10+

getTextIndexAtCursor(callback: AsyncCallback<number>): void

获取光标所在处的文本索引。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | 是 | 回调函数。当文本索引获取成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.getTextIndexAtCursor((err: BusinessError, index: number) => {
  if (err) {
    console.error(`Failed to getTextIndexAtCursor. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in getTextIndexAtCursor: ' + index);
});
```

#### \[h2\]getTextIndexAtCursor10+

getTextIndexAtCursor(): Promise<number>

获取光标所在处的文本索引。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | Promise对象，返回光标所在处的文本索引。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.getTextIndexAtCursor().then((index: number) => {
  console.info('Succeeded in getTextIndexAtCursor: ' + index);
}).catch((err: BusinessError) => {
  console.error(`Failed to getTextIndexAtCursor. Code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]getTextIndexAtCursorSync10+

getTextIndexAtCursorSync(): number

获取光标所在处的文本索引。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回光标所在处的文本索引。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**示例：**

```ts
let index: number = inputClient.getTextIndexAtCursorSync();
console.info(`Succeeded in getTextIndexAtCursorSync, index: ${index}`);
```

#### \[h2\]sendExtendAction10+

sendExtendAction(action: ExtendAction, callback: AsyncCallback<void>): void

发送扩展编辑操作。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/V5tWuW9ISv-LAZb3bCWRIQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=FE84A4488260041C626E13D935E5ED73365779860ADBA8E3F012FCB61076485A)

输入法应用调用该接口向编辑框发送扩展编辑操作，编辑框监听相应事件[on('handleExtendAction')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod#onhandleextendaction10)，从而进一步做出处理。

编辑框响应[ExtendAction](#extendaction10)的PASTE命令时，需要编辑框应用申请[ohos.permission.READ\_PASTEBOARD](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/restricted-permissions#ohospermissionread_pasteboard)权限。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| action | [ExtendAction](#extendaction10) | 是 | 要发送的扩展操作。 |
| callback | AsyncCallback<void> | 是 | 回调函数。发送成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.sendExtendAction(inputMethodEngine.ExtendAction.COPY, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to sendExtendAction. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in sending extend action.');
});
```

#### \[h2\]sendExtendAction10+

sendExtendAction(action: ExtendAction): Promise<void>

发送扩展编辑操作。使用promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/KmDlykOjR4mLavbXL5yq_Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=5044D8A82EAB0484DB80774C9C5147913BABE04D7FB059B5C8248A79CAD1F483)

输入法应用调用该接口向编辑框发送扩展编辑操作，编辑框监听相应事件[on('handleExtendAction')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod#onhandleextendaction10)，从而进一步做出处理。

编辑框响应[ExtendAction](#extendaction10)的PASTE命令时，需要编辑框应用申请[ohos.permission.READ\_PASTEBOARD](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/restricted-permissions#ohospermissionread_pasteboard)权限。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| action | [ExtendAction](#extendaction10) | 是 | 要发送的扩展操作。 |

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
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.sendExtendAction(inputMethodEngine.ExtendAction.COPY).then(() => {
  console.info('Succeeded in sending extend action.');
}).catch((err: BusinessError) => {
  console.error(`Failed to sendExtendAction. Code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]sendPrivateCommand12+

sendPrivateCommand(commandData: Record<string, CommandDataType>): Promise<void>

发送私有数据至需要与输入法应用通信的系统其他部分。使用promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/pkYrOY8gRTWwn73_O3YORA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=028C9C94AAEC7E5BB79B30F1392DDAC478EC7F82A6D761D1F769C909BB5350C3)

-   私有数据通道是系统预置输入法应用与系统特定组件（如文本框、桌面应用等）的通信机制，常用于设备级厂商在特定设备上实现自定义的输入法功能。
-   私有数据规格限制：总大小32KB，数量限制5条。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| commandData | Record<string, [CommandDataType](#commanddatatype12)\> | 是 | 私有数据。 |

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
| 12800010 | not the preconfigured default input method. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

inputMethodEngine.getInputMethodAbility().on('inputStart', (kbController, textInputClient) => {
  let record: Record<string, inputMethodEngine.CommandDataType> = {
    "valueString1": "abcdefg",
    "valueString2": true,
    "valueString3": 500,
  }
  textInputClient.sendPrivateCommand(record).then(() => {
  }).catch((err: BusinessError) => {
    if (err !== undefined) {
      console.error(`sendPrivateCommand catch error: ${err.code} ${err.message}`);
    }
  });
})
```

#### \[h2\]getCallingWindowInfo12+

getCallingWindowInfo(): Promise<WindowInfo>

获取当前拉起输入法的输入框所在应用窗口信息。使用promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/ioUbr9ePR72e3PwMEkSnkA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=5567B982902ED052A946A313669BE7EAE7797C87CB618E7BC237ABDE53F0A0FF)

本接口仅适用于适配使用[Panel](#panel10)作为软键盘窗口的输入法应用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[WindowInfo](#windowinfo12)\> | Promise对象，返回拉起输入法的输入框所在应用窗口信息。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800012 | the input method panel does not exist. |
| 12800013 | window manager service error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.getCallingWindowInfo().then((windowInfo: inputMethodEngine.WindowInfo) => {
  console.info(`windowInfo.rect: ${windowInfo.rect.left}, ${windowInfo.rect.top}, ${windowInfo.rect.width}, ${windowInfo.rect.height}`);
  console.info(`windowInfo.status: ${windowInfo.status}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to getCallingWindowInfo. Code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]setPreviewText12+

setPreviewText(text: string, range: Range): Promise<void>

设置预上屏文本。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| text | string | 是 | 将被预上屏的文本。 |
| range | [Range](#range10) | 是 | 
目标替换的文本范围。

\- 当值为{ start: -1, end: -1 }时，默认将参数text替换当前预上屏区域全部文本。

\- 当start等于end，默认将参数text插入start对应的光标位置。

\- 当start不等于end，将参数text替换range对应区域的文本。

\- 当start与end为其他含有负数值的组合，按照参数错误返回。

\- 当输入框已有预上屏文本，参数range不得超过预上屏文本范围，否则按照参数错误返回。

\- 当输入框无预上屏文本，参数range不得超过输入框文本范围，否则按照参数错误返回。

 |

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
| 12800011 | text preview not supported. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let range: inputMethodEngine.Range = { start: 0, end: 1 };
inputClient.setPreviewText('test', range).then(() => {
  console.info('Succeeded in setting preview text.');
}).catch((err: BusinessError) => {
  console.error(`Failed to setPreviewText. Code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]setPreviewTextSync12+

setPreviewTextSync(text: string, range: Range): void

设置预上屏文本。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| text | string | 是 | 将被预上屏的文本。 |
| range | [Range](#range10) | 是 | 
目标替换的文本范围。

\- 当值为{ start: -1, end: -1 }时，默认将参数text替换当前预上屏区域全部文本。

\- 当start等于end，默认将参数text插入start对应的光标位置。

\- 当start不等于end，将参数text替换range对应区域的文本。

\- 当start与end为其他含有负数值的组合，按照参数错误返回。

\- 当输入框已有预上屏文本，参数range不得超过预上屏文本范围，否则按照参数错误返回。

\- 当输入框无预上屏文本，参数range不得超过输入框文本范围，否则按照参数错误返回。

 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)，[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800011 | text preview not supported. |

**示例：**

```ts
let range: inputMethodEngine.Range = { start: 0, end: 1 };
inputClient.setPreviewTextSync('test', range);
```

#### \[h2\]finishTextPreview12+

finishTextPreview(): Promise<void>

结束预上屏。使用promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/p1G213n3SjCj4QcgkhOdOw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=300F64EBDD3B1870415BA803393829F98F575FAE37171AAD2066E08C6E0E1EE3)

若当前输入框已有预上屏状态文本，调用此接口后，预上屏内容将被系统正式上屏。

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
| 12800011 | text preview not supported. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.finishTextPreview().then(() => {
  console.info('Succeeded in finishing text preview.');
}).catch((err: BusinessError) => {
  console.error(`Failed to finishTextPreview. Code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]finishTextPreviewSync12+

finishTextPreviewSync(): void

结束预上屏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/Gt5JO0VWTtS0CZmCJw15bw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=B40BAF83CECE531E0E306F9A0F4B6E6DA0041700C6BED03EF24BBE14AE0ACA71)

若当前输入框已有预上屏状态文本，调用此接口后，预上屏内容将被系统正式上屏。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputmethod-framework)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800011 | text preview not supported. |

**示例：**

```ts
inputClient.finishTextPreviewSync();
```

#### \[h2\]sendMessage15+

sendMessage(msgId: string, msgParam?: ArrayBuffer): Promise<void>

发送自定义通信至已绑定当前输入法应用的编辑框应用。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/a_9b3YZsSX-p-tfa9aTR5Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=A0309812BA7AACBBF3313F5BD256695ABB9C22EEABC169FEB955B26AB15AA34E)

该接口需要编辑框与输入法绑定并进入编辑状态，且输入法应用处于完整体验模式时才能调用。

msgId最大限制256B，msgParam最大限制128KB。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| msgId | string | 是 | 需要发送至已绑定当前输入法应用的编辑框应用的自定义数据的标识符。 |
| msgParam | ArrayBuffer | 否 | 需要发送至已绑定当前输入法应用的编辑框应用的自定义数据的消息体。 |

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
inputClient.sendMessage(msgId, msgParam).then(() => {
  console.info('Succeeded send message.');
}).catch((err: BusinessError) => {
  console.error(`Failed to send message. Code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]recvMessage15+

recvMessage(msgHandler?: MessageHandler): void;

注册或取消注册Messagehandler。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/e-pznNXASuKxWFMbneJ1-A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=48E64DA14179BE786AA3B9B3D9E89C9F4A0576B3CBC62CAB424B829825184D11)

[MessageHandler](#messagehandler15)对象全局唯一，多次注册仅保留最后一次注册的对象及有效性，并触发上一个已注册对象的[onTerminated](#onterminated15)回调函数。

未填写参数，则取消全局已注册的[MessageHandler](#messagehandler15)，并会触发被取消注册对象中[onTerminated](#onterminated15)回调函数。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| msgHandler | [MessageHandler](#messagehandler15) | 否 | 
该对象将通过[onMessage](#onmessage15)接收来自已绑定当前输入法应用的编辑框应用所发送的自定义通信数据，并通过[onTerminated](#onterminated15)接收终止此对象订阅的消息。

若不填写此参数，则取消全局已注册的[MessageHandler](#messagehandler15)对象，同时触发其[onTerminated](#onterminated15)回调函数。

 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Incorrect parameter types. |

**示例：**

```ts
inputMethodEngine.getInputMethodAbility()
  .on('inputStart',
    (kbController: inputMethodEngine.KeyboardController, client: inputMethodEngine.InputClient) => {
      let keyboardController: inputMethodEngine.KeyboardController = kbController;
      let inputClient: inputMethodEngine.InputClient = client;
      let messageHandler: inputMethodEngine.MessageHandler = {
        onTerminated(): void {
          console.info('OnTerminated.');
        },
        onMessage(msgId: string, msgParam?: ArrayBuffer): void {
          console.info('recv message.');
        }
      }
      inputClient.recvMessage(messageHandler);
    });
```

#### \[h2\]getAttachOptions19+

getAttachOptions(): AttachOptions

获取绑定输入法时的附加选项。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [AttachOptions](#attachoptions19) | 返回绑定输入法时的附加选项内容。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/P4yIi-gUTH26ae-QMKMq7w/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=96BFC8A83C0F82E049787D524CB200EC52BB0CC40878D303F60355F15D445EAF)

从API version 20 开始，错误码801 Capability not supported.被移除。

**示例：**

```ts
let attachOptions: inputMethodEngine.AttachOptions = inputClient.getAttachOptions();
console.info(`Succeeded in getting AttachOptions, AttachOptions is ${attachOptions}`);
```

#### \[h2\]on('attachOptionsDidChange')19+

on(type: 'attachOptionsDidChange', callback: Callback<AttachOptions>): void

订阅绑定输入法时的附加选项变更事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 绑定输入法时的附加选项变更事件，固定取值为'attachOptionsDidChange'。 |
| callback | Callback<[AttachOptions](#attachoptions19)\> | 是 | 回调函数，返回绑定输入法时的附加选项。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/vj89NbPNQqK2N9yk2MqhfA/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=D9B4C88DDC1DFB5C1BAB3FBF707D20AE84E41EB1877DBC6A6AA0E6EE93B2CA4D)

从API version 20 开始，错误码801 Capability not supported.被移除。

**示例：**

```ts
let attachOptionsDidChangeCallback: (attachOptions: inputMethodEngine.AttachOptions) => void =
  (attachOptions: inputMethodEngine.AttachOptions) => {
    console.info(`AttachOptionsDidChangeCallback1: attachOptionsDidChange event triggered`);
  };

inputClient.on('attachOptionsDidChange', attachOptionsDidChangeCallback);
console.info(`attachOptionsDidChangeCallback subscribed to attachOptionsDidChange`);
inputClient.off('attachOptionsDidChange', attachOptionsDidChangeCallback);
console.info(`attachOptionsDidChange unsubscribed from attachOptionsDidChange`);
```

#### \[h2\]off('attachOptionsDidChange')19+

off(type: 'attachOptionsDidChange', callback?: Callback<AttachOptions>): void

取消订阅绑定输入法时的附加选项变更事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 绑定输入法时的附加选项变更事件，固定取值为'attachOptionsDidChange'。 |
| callback | Callback<[AttachOptions](#attachoptions19)\> | 否 | 取消订阅的回调函数。参数不填写时，默认取消订阅type对应的所有回调事件。 |

**示例：**

```ts
let attachOptionsDidChangeCallback: (attachOptions: inputMethodEngine.AttachOptions) => void =
  (attachOptions: inputMethodEngine.AttachOptions) => {
    console.info(`AttachOptionsDidChangeCallback1: attachOptionsDidChange event triggered`);
  };

inputClient.on('attachOptionsDidChange', attachOptionsDidChangeCallback);
console.info(`attachOptionsDidChangeCallback subscribed to attachOptionsDidChange`);
inputClient.off('attachOptionsDidChange', attachOptionsDidChangeCallback);
console.info(`attachOptionsDidChange unsubscribed from attachOptionsDidChange`);
```

#### \[h2\]CapitalizeMode20+

枚举，定义了文本首字母大写的不同模式。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| NONE | 0 | 不进行任何首字母大写处理。 |
| SENTENCES | 1 | 每个句子的首字母大写。 |
| WORDS | 2 | 每个单词的首字母大写。 |
| CHARACTERS | 3 | 每个字母都大写。 |

#### \[h2\]EditorAttribute

编辑框属性值。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| enterKeyType | number | 是 | 否 | 编辑框的功能属性，详见[常量中的功能键定义](#常量)。 |
| inputPattern | number | 是 | 否 | 编辑框的文本属性，详见[常量中的编辑框定义](#常量)。 |
| isTextPreviewSupported12+ | boolean | 否 | 否 | 
编辑框是否支持预上屏。

\- 值为true，表示支持。

\- 值为false，表示不支持。

 |
| bundleName14+ | string | 是 | 是 | 编辑框所属应用包名；该值可能为""，使用该属性时需要考虑为""的场景。 |
| immersiveMode15+ | [ImmersiveMode](#immersivemode15) | 是 | 是 | 输入法沉浸模式。 |
| windowId18+ | number | 是 | 是 | 编辑框设置所属窗口ID。 |
| displayId18+ | number | 是 | 是 | 编辑框设置窗口对应的屏幕ID。如果没有设置windowId，取当前焦点窗口屏幕ID。 |
| placeholder20+ | string | 是 | 是 | 编辑框设置的占位符信息。 |
| abilityName20+ | string | 是 | 是 | 编辑框设置的ability名称。 |
| capitalizeMode20+ | [CapitalizeMode](#capitalizemode20) | 是 | 是 | 编辑框设置大小写模式。如果没有设置或设置非法值，默认不进行任何首字母大写处理。 |
| gradientMode20+ | [GradientMode](#gradientmode20) | 是 | 是 | 渐变模式。如果没有设置或设置非法值，默认不使用渐变模式。 |
| extraConfig22+ | [InputMethodExtraConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod-extraconfig#inputmethodextraconfig) | 是 | 是 | 输入法扩展信息。 |

#### KeyEvent

按键属性值。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| keyCode | number | 是 | 否 | 按键的键值。键码值说明参考[KeyCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-keycode#keycode)。 |
| keyAction | number | 是 | 否 | 
按键事件类型。

\- 当值为2时，表示按下事件；

\- 当值为3时，表示抬起事件。

 |

#### PanelFlag10+

输入法面板状态类型枚举。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| FLG\_FIXED | 0 | 固定态面板类型。 |
| FLG\_FLOATING | 1 | 悬浮态面板类型。 |
| FLAG\_CANDIDATE15+ | 2 | 候选词态面板类型。 |

#### PanelType10+

输入法面板类型枚举。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| SOFT\_KEYBOARD | 0 | 软键盘类型。 |
| STATUS\_BAR | 1 | 状态栏类型。 |

#### PanelInfo10+

输入法面板属性。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| type | [PanelType](#paneltype10) | 否 | 否 | 面板的类型。 |
| flag | [PanelFlag](#panelflag10) | 否 | 是 | 面板的状态类型。 |

#### PanelRect12+

输入法面板位置大小信息。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| landscapeRect | [window.Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-i#rect7) | 否 | 否 | 横屏状态时输入法面板窗口的位置大小。 |
| portraitRect | [window.Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-i#rect7) | 否 | 否 | 竖屏状态时输入法面板窗口的位置大小。 |

#### EnhancedPanelRect15+

增强的输入法面板位置、大小信息，包含自定义避让区域、自定义热区。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| landscapeRect | [window.Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-i#rect7) | 否 | 是 | 
横屏状态时输入法面板窗口的位置大小。

\- 当fullScreenMode不填写或值为false时，此属性为必选。

 |
| portraitRect | [window.Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-i#rect7) | 否 | 是 | 

竖屏状态时，输入法面板窗口的位置大小。

\- 当fullScreenMode不填写或值为false时，此属性为必选。

 |
| landscapeAvoidY | number | 否 | 是 | 

横屏状态时，面板中的避让线距离面板顶部的距离，单位px。默认值为0。

\- 应用内其他系统组件会对避让线以下的输入法面板区域进行避让。

\- 面板为固定态时，避让线到屏幕底部的高度不能超过屏幕高度的70%。

 |
| landscapeInputRegion | Array<[window.Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-i#rect7)\> | 否 | 是 | 

横屏状态时，面板接收输入事件的区域。

\- 数组大小限制为\[1, 4\]。默认值为横屏时的面板大小。

\- 传入的热区位置是相对于输入法面板窗口左顶点的位置。

 |
| portraitAvoidY | number | 否 | 是 | 

竖屏状态时，面板中的避让线距离面板顶部的距离，单位px。默认值为0。

\- 应用内其他系统组件会对避让线以下的输入法面板区域进行避让。

\- 面板为固定态时，避让线到屏幕底部的高度不能超过屏幕高度的70%。

 |
| portraitInputRegion | Array<[window.Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-i#rect7)\> | 否 | 是 | 

竖屏状态时，面板接收输入事件的区域。

\- 数组大小限制为\[1, 4\]。默认值为竖屏时的面板大小。

\- 传入的热区位置是相对于输入法面板窗口左顶点的位置。

 |
| fullScreenMode | boolean | 否 | 是 | 

是否开启全屏模式。默认值为false。

\- 值为true，landscapeRect和portraitRect可不填写。

\- 值为false，landscapeRect和portraitRect为必选属性。

 |

#### KeyboardArea15+

面板中的键盘区域。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| top | number | 否 | 否 | 键盘区域的上边界到面板区域上边界的距离，单位为px，该参数为整数。 |
| bottom | number | 否 | 否 | 键盘区域的下边界到面板区域下边界的距离，单位为px，该参数为整数。 |
| left | number | 否 | 否 | 键盘区域的左边界到面板区域左边界的距离，单位为px，该参数为整数。 |
| right | number | 否 | 否 | 键盘区域的右边界到面板区域右边界的距离，单位为px，该参数为整数。 |

#### AttachOptions19+

绑定输入法时的附加选项。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| requestKeyboardReason | [RequestKeyboardReason](#requestkeyboardreason19) | 否 | 是 | 该属性由编辑框应用设置，如果没有设置或设置非法值，则默认没有特定的原因触发键盘请求。 |
| isSimpleKeyboardEnabled20+ | boolean | 否 | 是 | 
是否使能简单键盘，该属性由编辑框应用设置，true表示使能简单键盘，false表示不使能简单键盘。

如果没有设置或设置非法值，则默认不使能简单键盘。

 |

#### WindowInfo12+

窗口信息。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| rect | [window.Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-i#rect7) | 否 | 否 | 窗口矩形区域。 |
| status | [window.WindowStatusType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-e#windowstatustype11) | 否 | 否 | 窗口模式类型。 |

#### ImmersiveMode15+

枚举，输入法沉浸模式。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| NONE\_IMMERSIVE | 0 | 不使用沉浸模式。 |
| IMMERSIVE | 1 | 沉浸模式，由输入法应用确定沉浸模式类型。 |
| LIGHT\_IMMERSIVE | 2 | 浅色沉浸模式。 |
| DARK\_IMMERSIVE | 3 | 深色沉浸模式。 |

#### RequestKeyboardReason19+

枚举，请求键盘输入的原因。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| NONE | 0 | 表示没有特定的原因触发键盘请求。 |
| MOUSE | 1 | 表示键盘请求是由鼠标操作触发的。 |
| TOUCH | 2 | 表示键盘请求是由触摸操作触发的。 |
| OTHER | 20 | 表示键盘请求是由其他原因触发的。 |

#### GradientMode20+

枚举，输入法渐变模式。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| NONE | 0 | 不使用渐变模式。 |
| LINEAR\_GRADIENT | 1 | 线性渐变。 |

#### ImmersiveEffect20+

沉浸效果。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| gradientHeight | number | 否 | 否 | 渐变高度，不能超过屏幕高度的15%。 |
| gradientMode | [GradientMode](#gradientmode20) | 否 | 否 | 渐变模式。 |

#### SystemPanelInsets21+

输入法软键盘相对系统面板的偏移区域。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| bottom | number | 是 | 否 | 键盘区域的下边界到系统面板区域下边界的距离，单位为px，该参数为整数。 |
| left | number | 是 | 否 | 键盘区域的左边界到系统面板区域左边界的距离，单位为px，该参数为整数。 |
| right | number | 是 | 否 | 键盘区域的右边界到系统面板区域右边界的距离，单位为px，该参数为整数。 |

#### TextInputClient(deprecated)

下列API示例中都需使用[on('inputStart')](#oninputstartdeprecated)回调获取到TextInputClient实例，再通过此实例调用对应方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/TaLV30-4RWK0f_aWLM-qaQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=8163933590CCD3CC059B173981233C51A810BE0874B0A2D38D9DDA37914A0AF7)

从API version 8开始支持，API version 9开始废弃，建议使用[InputClient](#inputclient9)替代。

#### \[h2\]getForward(deprecated)

getForward(length:number, callback: AsyncCallback<string>): void

获取光标前固定长度的文本。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/zKNQ-ZveTz-uu3OMLPCkfw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=BD930E5EEEF33EBEFFC41B8DA267FCACEF5BEF401929AA81003CB72CB92B9403)

从API version 8开始支持，API version 9开始废弃，建议使用[getForward](#getforward9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| length | number | 是 | 文本长度。不能小于0。 |
| callback | AsyncCallback<string> | 是 | 回调函数。当光标前固定长度的文本获取成功，err为undefined，data为获取到的文本；否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
textInputClient.getForward(length, (err: BusinessError, text: string) => {
  if (err) {
    console.error(`Failed to getForward. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in getting forward, text: ' + text);
});
```

#### \[h2\]getForward(deprecated)

getForward(length:number): Promise<string>

获取光标前固定长度的文本。使用promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/yJs7rJX8R5OijevZqyN5ow/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=3129857C544E65C9367D360927E2DE73C2AF9E204BA29BA8728D1E6FE5231E83)

从API version 8开始支持，API version 9开始废弃，建议使用[getForward](#getforward9-1)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| length | number | 是 | 文本长度。不能小于0。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | Promise对象，返回光标前固定长度的文本。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
textInputClient.getForward(length).then((text: string) => {
  console.info('Succeeded in getting forward, text: ' + text);
}).catch((err: BusinessError) => {
  console.error(`Failed to getForward. Code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]getBackward(deprecated)

getBackward(length:number, callback: AsyncCallback<string>): void

获取光标后固定长度的文本。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/CitAd-PsSZW6QJEqN285Qw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=A2C9A683628FFB94E93873EF12299D2C6230579DE2D72F9DF2EA96BEB965EA91)

从API version 8开始支持，API version 9开始废弃，建议使用[getBackward](#getbackward9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| length | number | 是 | 文本长度。不能小于0。 |
| callback | AsyncCallback<string> | 是 | 回调函数。当光标后固定长度的文本获取成功，err为undefined，data为获取到的文本；否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
textInputClient.getBackward(length, (err: BusinessError, text: string) => {
  if (err) {
    console.error(`Failed to getBackward. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in getting backward, text: ' + text);
});
```

#### \[h2\]getBackward(deprecated)

getBackward(length:number): Promise<string>

获取光标后固定长度的文本。使用promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/bZqM2f7iQjCixC-uDl8ogQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=9BEB2C68AFD68D15078C5BF0FD853A105C08030DA8FFF14E61E11C02B46D238D)

从API version 8开始支持，API version 9开始废弃，建议使用[getBackward](#getbackward9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| length | number | 是 | 文本长度。不能小于0。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | Promise对象，返回光标后固定长度的文本。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
textInputClient.getBackward(length).then((text: string) => {
  console.info(`'Succeeded in getting backward: ${text}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to getBackward. Code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]deleteForward(deprecated)

deleteForward(length:number, callback: AsyncCallback<boolean>): void

删除光标前固定长度的文本。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/L8v0mWuTS8Ko5R5M0IB32A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=C77B460069B75B74426A8EAD151C4F5F51B49DE785E73D5689DE4D7468CAF85F)

从API version 8开始支持，API version 9开始废弃，建议使用[deleteForward](#deleteforward9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| length | number | 是 | 文本长度。不能小于0。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当光标前固定长度的文本删除成功，err为undefined，data为true；否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
textInputClient.deleteForward(length, (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to deleteForward. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in deleting forward.');
  } else {
    console.error('Failed to deleteForward.');
  }
});
```

#### \[h2\]deleteForward(deprecated)

deleteForward(length:number): Promise<boolean>

删除光标前固定长度的文本。使用promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/eZYXocKtRDaDfP72_WvolA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=8D1F8414696B11FC1014D2010F638714349112C090BF5BE3FCBD5FE15DF1A5CC)

从API version 8开始支持，API version 9开始废弃，建议使用[deleteForward](#deleteforward9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| length | number | 是 | 文本长度。不能小于0。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象。返回true表示删除光标前固定长度的文本成功；返回false表示删除光标前固定长度的文本失败。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
textInputClient.deleteForward(length).then((result: boolean) => {
  if (result) {
    console.info('Succeeded in deleting forward.');
  } else {
    console.error('Failed to delete forward.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to deleteForward. Code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]deleteBackward(deprecated)

deleteBackward(length:number, callback: AsyncCallback<boolean>): void

删除光标后固定长度的文本。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/U-nN_NPMQN6A69XPO68etQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=680953FCF5739B05DC87BCD1703FFDF8880B7A3DD0E0CFF0D7B2A51661350F38)

从API version 8开始支持，API version 9开始废弃，建议使用[deleteBackward](#deletebackward9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| length | number | 是 | 文本长度。不能小于0。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当光标后固定长度的文本删除成功，err为undefined，data为true；否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
textInputClient.deleteBackward(length, (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to deleteBackward. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in deleting backward.');
  } else {
    console.error('Failed to deleteBackward.');
  }
});
```

#### \[h2\]deleteBackward(deprecated)

deleteBackward(length:number): Promise<boolean>

删除光标后固定长度的文本。使用promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/hWPrMdoeT96egjOXxHbxYA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=CEC3A0E5E6B7D6FE4AC8E8D267CA677DFE0E28EF77AB6B40AEC9F6B462EC07BF)

从API version 8开始支持，API version 9开始废弃，建议使用[deleteBackward](#deletebackward9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| length | number | 是 | 文本长度。不能小于0。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象。返回true表示删除光标后固定长度的文本成功；返回false表示删除光标后固定长度的文本失败。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
textInputClient.deleteBackward(length).then((result: boolean) => {
  if (result) {
    console.info('Succeeded in deleting backward.');
  } else {
    console.error('Failed to deleteBackward.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to deleteBackward. Code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]sendKeyFunction(deprecated)

sendKeyFunction(action: number, callback: AsyncCallback<boolean>): void

发送功能键。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/FVESh7_2QQW1KNAkJRmF2g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=5D1D3525E24496A3C63E70474D6A062FBBB12D44B00D0BC8CBD230695B5343BE)

从API version 8开始支持，API version 9开始废弃，建议使用[sendKeyFunction](#sendkeyfunction9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| action | number | 是 | 
功能键键值。

\- 当值为0时，表示无效按键；

\- 当值为1时，表示确认键（即回车键）。

 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当功能键发送成功，err为undefined，data为true；否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let action: number = 1;
textInputClient.sendKeyFunction(action, (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to sendKeyFunction. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in sending key function.');
  } else {
    console.error('Failed to sendKeyFunction.');
  }
});
```

#### \[h2\]sendKeyFunction(deprecated)

sendKeyFunction(action: number): Promise<boolean>

发送功能键。使用promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/4VOBU3o9TYmzLDZ-gHaKKg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=FCAE4451D4F37781C8E2479566B5101C5721C97CBBFDCA871CE348C4978E7289)

从API version 8开始支持，API version 9开始废弃，建议使用[sendKeyFunction](#sendkeyfunction9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| action | number | 是 | 
功能键键值。

当值为0时，表示无效按键；

当值为1时，表示确认键（即回车键）。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象。返回true表示发送功能键成功；返回false表示发送功能键失败。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let action: number = 1;
textInputClient.sendKeyFunction(action).then((result: boolean) => {
  if (result) {
    console.info('Succeeded in sending key function.');
  } else {
    console.error('Failed to sendKeyFunction.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to sendKeyFunction:. Code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]insertText(deprecated)

insertText(text:string, callback: AsyncCallback<boolean>): void

插入文本。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/NQuzz1MVTruYGw3qFUhM9Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=0631D04E23B3549DFDFFE453EBB57D63FABB035959D63AB72BD550E3A20B3EBB)

从API version 8开始支持，API version 9开始废弃，建议使用[insertText](#inserttext9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| text | string | 是 | 文本。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当文本插入成功，err为undefined，data为true；否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

textInputClient.insertText('test', (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to insertText. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in inserting text.');
  } else {
    console.error('Failed to insertText.');
  }
});
```

#### \[h2\]insertText(deprecated)

insertText(text:string): Promise<boolean>

插入文本。使用promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/zrr5LPjgRNSQftx5i5U-cg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=38CB7C88789F9426410DECF132C75B6B257A1426DD59DB26D4D8551F4B89C8A4)

从API version 8开始支持，API version 9开始废弃，建议使用[insertText](#inserttext9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| text | string | 是 | 文本。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象。返回true表示插入文本成功；返回false表示插入文本失败。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

textInputClient.insertText('test').then((result: boolean) => {
  if (result) {
    console.info('Succeeded in inserting text.');
  } else {
    console.error('Failed to insertText.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to insertText. Code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]getEditorAttribute(deprecated)

getEditorAttribute(callback: AsyncCallback<EditorAttribute>): void

获取编辑框属性值。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/qIOKdGNfQTK245KdpdC15A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=FD37F36FEABF6F5DB20BD5F9A79DDBB3FCA52EB663C74294FB69CEC2FD9A008D)

从API version 8开始支持，API version 9开始废弃，建议使用[getEditorAttribute](#geteditorattribute9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[EditorAttribute](#editorattribute)\> | 是 | 回调函数。当编辑框的属性值获取成功，err为undefined，data为编辑框属性值；否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

textInputClient.getEditorAttribute((err: BusinessError,
  editorAttribute: inputMethodEngine.EditorAttribute) => {
  if (err) {
    console.error(`Failed to getEditorAttribute. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`editorAttribute.inputPattern: ${editorAttribute.inputPattern}`);
  console.info(`editorAttribute.enterKeyType: ${editorAttribute.enterKeyType}`);
});
```

#### \[h2\]getEditorAttribute(deprecated)

getEditorAttribute(): Promise<EditorAttribute>

获取编辑框属性值。使用promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/QZtvqpCgSpil7JpyL8CL1g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=6A63C8C1859A16E749BDDFD569B016BF56B5397BFFD518F0F74A89F83AE7C5CF)

从API version 8开始支持，API version 9开始废弃，建议使用[getEditorAttribute](#geteditorattribute9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[EditorAttribute](#editorattribute)\> | Promise对象，返回编辑框属性值。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

textInputClient.getEditorAttribute().then((editorAttribute: inputMethodEngine.EditorAttribute) => {
  console.info(`editorAttribute.inputPattern: ${editorAttribute.inputPattern}`);
  console.info(`editorAttribute.enterKeyType: ${editorAttribute.enterKeyType}}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to getEditorAttribute. Code is ${err.code}, message is ${err.message}`);
});
```

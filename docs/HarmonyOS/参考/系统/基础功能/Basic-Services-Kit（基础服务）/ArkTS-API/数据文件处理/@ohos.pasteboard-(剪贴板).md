---
title: "@ohos.pasteboard (剪贴板)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-pasteboard"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "Basic Services Kit（基础服务）"
  - "ArkTS API"
  - "数据文件处理"
  - "@ohos.pasteboard (剪贴板)"
captured_at: "2026-04-17T01:48:27.983Z"
---

# @ohos.pasteboard (剪贴板)

本模块提供管理系统剪贴板的能力，支持系统复制、粘贴功能。系统剪贴板支持对文本、HTML、URI、Want、PixelMap等内容的操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/teKUSy6RRduTyDFp5ACmBg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=157FE9E4900B48D1EADB284E46E5665470A7FBF0E9A3496C3CBE41725DAEDD20)

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import { pasteboard } from '@kit.BasicServicesKit';
```

#### 常量

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

| 名称 | 类型 | 值 | 说明 |
| :-- | :-- | :-- | :-- |
| MAX\_RECORD\_NUM7+ | number | \- | 
API version 10之前，此常量值为512，表示单个PasteData中所能包含的最大条目数为512。当剪贴板内容中添加的条目达到数量上限512后，后续的添加操作无效。

从API version 10开始，不再限制单个PasteData中所能包含的最大条目数。

 |
| MIMETYPE\_TEXT\_HTML7+ | string | 'text/html' | HTML内容的MIME类型定义。 |
| MIMETYPE\_TEXT\_WANT7+ | string | 'text/want' | Want内容的MIME类型定义。 |
| MIMETYPE\_TEXT\_PLAIN7+ | string | 'text/plain' | 纯文本内容的MIME类型定义。 |
| MIMETYPE\_TEXT\_URI7+ | string | 'text/uri' | URI内容的MIME类型定义。 |
| MIMETYPE\_PIXELMAP9+ | string | 'pixelMap' | PixelMap内容的MIME类型定义。 |

#### ValueType9+

type ValueType = string | image.PixelMap | Want | ArrayBuffer

用于表示允许的数据字段类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

| 类型 | 说明 |
| :-- | :-- |
| string | 表示string的类型。 |
| image.PixelMap | 表示[image.PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)的类型。 |
| Want | 表示[Want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-want)的类型。 |
| ArrayBuffer | 表示ArrayBuffer的类型。 |

#### pasteboard.createData9+

createData(mimeType: string, value: ValueType): PasteData

构建一个指定类型的剪贴板内容对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| mimeType | string | 是 | 剪贴板数据对应的MIME类型，可以是[常量](#常量)中已定义的类型，包括HTML类型，WANT类型，纯文本类型，URI类型，PIXELMAP类型；也可以是自定义的MIME类型，开发者可自定义此参数值, mimeType长度不能超过1024字节。 |
| value | [ValueType](#valuetype9) | 是 | 自定义数据内容。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [PasteData](#pastedata) | 剪贴板内容对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例1：**

```ts
let dataXml = new ArrayBuffer(256);
let pasteData: pasteboard.PasteData = pasteboard.createData('app/xml', dataXml);
```

**示例2：**

```ts
let dataText = 'hello';
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, dataText);
```

#### pasteboard.createData14+

createData(data: Record<string, ValueType>): PasteData

构建一个包含多个类型数据的剪贴板内容对象。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| data | [Record](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/introduction-to-arkts#对象字面量)<string, [ValueType](#valuetype9)\> | 是 | 
Record的key为剪贴板数据对应的MIME类型。可以是[常量](#常量)中已定义的类型，包括HTML类型，WANT类型，纯文本类型，URI类型，PIXELMAP类型。也可以是自定义的MIME类型，可自定义此参数值，mimeType长度不能超过1024字节。

Record的value为key中指定MIME类型对应的数据。

Record中的首个key-value指定的MIME类型，会作为剪贴板内容对象中首个PasteDataRecord的默认MIME类型，非默认类型的数据在粘贴时只能使用[getData](#getdata14)接口读取。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [PasteData](#pastedata) | 剪贴板内容对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例1：**

```ts
let pasteData: pasteboard.PasteData = pasteboard.createData({
    'text/plain': 'hello',
    'app/xml': new ArrayBuffer(256),
});
```

**示例2：**

```ts
let record: Record<string, pasteboard.ValueType> = {};
record[pasteboard.MIMETYPE_TEXT_PLAIN] = 'hello';
record[pasteboard.MIMETYPE_TEXT_URI] = 'dataability:///com.example.myapplication1/user.txt';
let pasteData: pasteboard.PasteData = pasteboard.createData(record);
```

#### pasteboard.createRecord9+

createRecord(mimeType: string, value: ValueType): PasteDataRecord

创建一条指定类型的数据内容条目。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| mimeType | string | 是 | 剪贴板数据对应的MIME类型，可以是[常量](#常量)中已定义的类型，包括HTML类型，WANT类型，纯文本类型，URI类型，PIXELMAP类型；也可以是自定义的MIME类型，开发者可自定义此参数值，mimeType长度不能超过1024字节。 |
| value | [ValueType](#valuetype9) | 是 | 指定类型对应的数据内容。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [PasteDataRecord](#pastedatarecord7) | 一条新建的指定类型的数据内容条目。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例1：**

```ts
let dataXml = new ArrayBuffer(256);
let pasteDataRecord: pasteboard.PasteDataRecord = pasteboard.createRecord('app/xml', dataXml);
```

**示例2：**

```ts
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
let record: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE_TEXT_URI, 'file://com.example.myapplication1/data/storage/el2/base/files/file.txt');
pasteData.replaceRecord(0, record);
```

#### pasteboard.getSystemPasteboard

getSystemPasteboard(): SystemPasteboard

获取系统剪贴板对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [SystemPasteboard](#systempasteboard) | 系统剪贴板对象。 |

**示例：**

```ts
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
```

#### ShareOption9+

可粘贴数据的范围类型枚举。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| INAPP | 0 | 表示仅允许同应用内粘贴。 |
| LOCALDEVICE | 1 | 表示允许在任何应用内粘贴。用户在“设置-多设备协同-跨设备剪贴板开关”选项中控制允许跨设备粘贴，表示允许跨设备在任何应用内粘贴。 |
| CROSSDEVICE(deprecated) | 2 | 
表示允许跨设备在任何应用内粘贴。

从API version 12开始废弃，无替代接口和替代方法，后续由用户在“设置-多设备协同-跨设备剪贴板开关”选项中控制是否允许跨设备粘贴。

 |

#### pasteboard.createHtmlData(deprecated)

createHtmlData(htmlText: string): PasteData

构建一个HTML剪贴板内容对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/mRcMV-FIQcmNNZn5gTuuLg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=0A686FF05A2CF8F7AC6DC936210D1D92C72F37EBA3EBF1BFA10A7642B007F78D)

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[pasteboard.createData](#pasteboardcreatedata9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| htmlText | string | 是 | HTML内容。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [PasteData](#pastedata) | 剪贴板内容对象。 |

**示例：**

```ts
let html = "<!DOCTYPE html>\n" + "<html>\n" + "<head>\n" + "<meta charset=\"utf-8\">\n" + "<title>HTML-PASTEBOARD_HTML</title>\n" + "</head>\n" + "<body>\n" + "    <h1>HEAD</h1>\n" + "    <p></p>\n" + "</body>\n" + "</html>";
let pasteData: pasteboard.PasteData = pasteboard.createHtmlData(html);
```

#### pasteboard.createWantData(deprecated)

createWantData(want: Want): PasteData

构建一个Want剪贴板内容对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/3GZSEhRiQgG0x0j-x44T1w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=F3F55DAB240AF225A7C85CB4B5786A48D001A21384322E2981856412F8D48B18)

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[pasteboard.createData](#pasteboardcreatedata9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| want | [Want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-want) | 是 | Want内容。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [PasteData](#pastedata) | 剪贴板内容对象。 |

**示例：**

```ts
import { Want } from '@kit.AbilityKit';

let object: Want = {
    bundleName: "com.example.aafwk.test",
    abilityName: "com.example.aafwk.test.TwoAbility"
};
let pasteData: pasteboard.PasteData = pasteboard.createWantData(object);
```

#### pasteboard.createPlainTextData(deprecated)

createPlainTextData(text: string): PasteData

构建一个纯文本剪贴板内容对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/D6rebzU_SOSoSPDyRe1TcA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=1CE509AB8971E9AC7C26DBC0351D5CBE0182F2EDF0FDD1526314471037D94408)

从 API version 6 开始支持，从 API version 9 开始废弃，建议使用[pasteboard.createData](#pasteboardcreatedata9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| text | string | 是 | 纯文本内容。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [PasteData](#pastedata) | 剪贴板内容对象。 |

**示例：**

```ts
let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('content');
```

#### pasteboard.createUriData(deprecated)

createUriData(uri: string): PasteData

构建一个URI剪贴板内容对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/p1Y1wVZPTH-G3PHIZEGxPw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=8DDD4704287D7E1947C4764A0674690B016D3FE1747DB2DE59B90AA75BC35617)

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[pasteboard.createData](#pasteboardcreatedata9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| uri | string | 是 | URI内容。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [PasteData](#pastedata) | 剪贴板内容对象。 |

**示例：**

```ts
let pasteData: pasteboard.PasteData = pasteboard.createUriData('dataability:///com.example.myapplication1/user.txt');
```

#### pasteboard.createHtmlTextRecord(deprecated)

createHtmlTextRecord(htmlText: string): PasteDataRecord

创建一条HTML内容的条目。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/u_yFbDcoS4STOtS2z2ZgSQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=9160AB311C4B1A3EA3667C3A1AE77848BCC6F1232B5AC9F83E671A42ADB29FEE)

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[pasteboard.createRecord](#pasteboardcreaterecord9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| htmlText | string | 是 | HTML内容。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [PasteDataRecord](#pastedatarecord7) | 一条新建的HTML内容条目。 |

**示例：**

```ts
let html = "<!DOCTYPE html>\n" + "<html>\n" + "<head>\n" + "<meta charset=\"utf-8\">\n" + "<title>HTML-PASTEBOARD_HTML</title>\n" + "</head>\n" + "<body>\n" + "    <h1>HEAD</h1>\n" + "    <p></p>\n" + "</body>\n" + "</html>";
let record: pasteboard.PasteDataRecord = pasteboard.createHtmlTextRecord(html);
```

#### pasteboard.createWantRecord(deprecated)

createWantRecord(want: Want): PasteDataRecord

创建一条Want内容条目。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/01QkcSlbQ06FIac14dRa_Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=4DC0AB410CE192E54929F0CE659338D00736C7CFFBBF3819918329FF633D39CC)

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[pasteboard.createRecord](#pasteboardcreaterecord9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| want | [Want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-want) | 是 | Want内容。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [PasteDataRecord](#pastedatarecord7) | 一条新建的Want内容条目。 |

**示例：**

```ts
import { Want } from '@kit.AbilityKit';

let object: Want = {
    bundleName: "com.example.aafwk.test",
    abilityName: "com.example.aafwk.test.TwoAbility"
};
let record: pasteboard.PasteDataRecord = pasteboard.createWantRecord(object);
```

#### pasteboard.createPlainTextRecord(deprecated)

createPlainTextRecord(text: string): PasteDataRecord

创建一条纯文本内容条目。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/ulFQdpzxQtKtD8BtqDKHFg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=218AAE05B15A974ECF7A34B2ABFA19DF0AD4E7818B474ACF13AABC7200681FDE)

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[pasteboard.createRecord](#pasteboardcreaterecord9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| text | string | 是 | 纯文本内容。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [PasteDataRecord](#pastedatarecord7) | 一条新建的纯文本内容条目。 |

**示例：**

```ts
let record: pasteboard.PasteDataRecord = pasteboard.createPlainTextRecord('hello');
```

#### pasteboard.createUriRecord(deprecated)

createUriRecord(uri: string): PasteDataRecord

创建一条URI内容的条目。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/BoOD-qKBT2GPwGwMh_xlVQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=100E92C429A042206A068164FF4831D323818CF934CC3A60D0F6B722D50BE563)

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[pasteboard.createRecord](#pasteboardcreaterecord9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| uri | string | 是 | URI内容。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [PasteDataRecord](#pastedatarecord7) | 一条新建的URI内容条目。 |

**示例：**

```ts
let record: pasteboard.PasteDataRecord = pasteboard.createUriRecord('dataability:///com.example.myapplication1/user.txt');
```

#### PasteDataProperty7+

定义剪贴板中所有内容条目的属性，包含时间戳、数据类型、粘贴范围以及一些附加数据等，该属性必须通过[setProperty](#setproperty9)方法，才能设置到剪贴板中。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| additions | Record<string, object> | 否 | 否 | 设置其他附加属性数据。不支持动态追加属性，只能通过重新赋值的方式修改附加值，具体见相关示例setProperty， 默认为空。 |
| mimeTypes | Array<string> | 是 | 否 | 剪贴板内容条目的数据类型，非重复的类型列表。 |
| tag | string | 否 | 否 | 用户自定义标签，默认为空。 |
| timestamp | number | 是 | 否 | 剪贴板数据的写入时间戳（单位：已开机时间的ns数）。 |
| localOnly | boolean | 否 | 否 | 配置剪贴板内容是否为“仅在本地”，默认值为false。其值会被shareOption属性覆盖，推荐使用[ShareOption](#shareoption9)属性。 |
| shareOption9+ | [ShareOption](#shareoption9) | 否 | 否 | 指示剪贴板数据可以粘贴到的范围，默认值为CROSSDEVICE。 |

#### FileConflictOptions15+

定义文件拷贝冲突时的选项。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| OVERWRITE | 0 | 目标路径存在同文件名时覆盖。 |
| SKIP | 1 | 目标路径存在同文件名时跳过，若设置SKIP，应用获取到的粘贴数据不包含跳过文件。 |

#### ProgressIndicator15+

定义进度条指示选项，可选择是否采用系统默认进度显示。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| NONE | 0 | 不采用系统默认进度显示。 |
| DEFAULT | 1 | 采用系统默认进度显示。 |

#### ProgressInfo15+

定义进度上报的数据结构，且仅当进度指示选项[ProgressIndicator](#progressindicator15)设置为NONE时才会上报此信息。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| progress | number | 否 | 否 | 不使用系统提供的进度条时，系统上报拷贝粘贴任务进度百分比。 |

#### ProgressListener15+

type ProgressListener = (progress: ProgressInfo) => void

定义进度数据变化的订阅函数，当选择不使用系统默认进度显示时，可设置该项获取粘贴过程的进度。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| progress | [ProgressInfo](#progressinfo15) | 是 | 定义进度上报的数据结构，且仅当进度指示选项[ProgressIndicator](#progressindicator15)设置为NONE时才会上报此信息。 |

#### ProgressSignal15+

定义进度取消的函数，在粘贴过程中可选择取消任务，且仅当进度指示选项[ProgressIndicator](#progressindicator15)设置为NONE时此参数才有意义。

**系统能力：** SystemCapability.MiscServices.Pasteboard

#### \[h2\]cancel15+

cancel(): void

取消正在进行的拷贝粘贴任务。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**示例：**

```ts
import { BusinessError, pasteboard } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';
@Entry
@Component
struct PasteboardTest {
 build() {
   RelativeContainer() {
     Column() {
       Column() {
         Button("Copy txt")
           .onClick(async ()=>{
              let text = "test";
              let pasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, text);
              let systemPasteboard = pasteboard.getSystemPasteboard();
              await systemPasteboard.setData(pasteData);
              let signal = new pasteboard.ProgressSignal;
              let progressListenerInfo = (progress: pasteboard.ProgressInfo) => {
                console.info('progressListener success, progress:' + progress.progress);
                signal.cancel();
              };
              let destPath: string = '/data/storage/el2/base/files/';
              let destUri : string = fileUri.getUriFromPath(destPath);
              let params: pasteboard.GetDataParams = {
                destUri: destUri,
                fileConflictOptions: pasteboard.FileConflictOptions.OVERWRITE,
                progressIndicator: pasteboard.ProgressIndicator.DEFAULT,
                progressListener: progressListenerInfo,
              };
              systemPasteboard.getDataWithProgress(params).then((pasteData: pasteboard.PasteData) => {
                console.info('getDataWithProgress success');
              }).catch((err: BusinessError) => {
                console.error('Failed to get PasteData. Cause: ' + err.message);
              })
          })
        }
      }
    }
  }
}
```

#### GetDataParams15+

应用在使用剪贴板提供的文件拷贝能力的情况下需要的参数，包含目标路径、文件冲突选项、进度条类型等。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| destUri | string | 否 | 是 | 拷贝文件时目标路径。若不支持文件处理，则不需要设置此参数；若应用涉及复杂文件处理策略或需要区分文件多路径存储，建议不设置此参数，由应用自行完成文件copy处理，默认为空。 |
| fileConflictOptions | [FileConflictOptions](#fileconflictoptions15) | 否 | 是 | 定义文件拷贝冲突时的选项，默认为OVERWRITE。 |
| progressIndicator | [ProgressIndicator](#progressindicator15) | 否 | 否 | 定义进度条指示选项，可选择是否采用系统默认进度显示。 |
| progressListener | [ProgressListener](#progresslistener15) | 否 | 是 | 定义进度数据变化的订阅函数，当选择不使用系统默认进度显示时，可设置该项获取粘贴过程的进度，默认为空。 |
| progressSignal | [ProgressSignal](#progresssignal15) | 否 | 是 | 定义进度取消的函数，在粘贴过程中可选择取消任务，且仅当进度指示选项[ProgressIndicator](#progressindicator15)设置为NONE时此参数才有意义，默认为空。 |

#### PasteDataRecord7+

对于剪贴板中内容记录的抽象定义，称之为条目。剪贴板内容部分由一个或者多个条目构成，例如一条文本内容、一份HTML、一个URI或者一个Want。

#### \[h2\]属性

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| htmlText | string | 是 | 否 | HTML内容。 |
| want | [Want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-want) | 是 | 否 | Want内容。 |
| mimeType | string | 是 | 否 | 默认数据类型。 |
| plainText | string | 是 | 否 | 纯文本内容。 |
| uri | string | 是 | 否 | URI内容。 |
| pixelMap9+ | [image.PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap) | 是 | 否 | PixelMap内容。 |
| data9+ | Record<string, ArrayBuffer> | 是 | 否 | 自定义数据内容。 |

#### \[h2\]toPlainText9+

toPlainText(): string

将一个PasteDataRecord中的html、plain、uri内容强制转换为文本内容。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 纯文本内容。 |

**示例：**

```ts
let record: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE_TEXT_HTML, '<html>hello</html>');
let text: string = record.toPlainText();
console.info(`Succeeded in converting to text. Text: ${text}`);
```

#### \[h2\]addEntry14+

addEntry(type: string, value: ValueType): void

往一个PasteDataRecord中额外添加一种样式的自定义数据。此方式添加的MIME类型都不是Record的默认类型，粘贴时只能使用[getData](#getdata14)接口读取对应数据。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 剪贴板数据对应的MIME类型，可以是[常量](#常量)中已定义的类型，包括HTML类型，WANT类型，纯文本类型，URI类型，PIXELMAP类型；也可以是自定义的MIME类型，开发者可自定义此参数值，mimeType长度不能超过1024字节。 |
| value | [ValueType](#valuetype9) | 是 | 自定义数据内容。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和见[剪贴板错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-pasteboard)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```ts
let html = "<!DOCTYPE html>\n" + "<html>\n" + "<head>\n" + "<meta charset=\"utf-8\">\n" + "<title>HTML-PASTEBOARD_HTML</title>\n" + "</head>\n" + "<body>\n" + "    <h1>HEAD</h1>\n" + "    <p></p>\n" + "</body>\n" + "</html>";
let record: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE_TEXT_URI, 'dataability:///com.example.myapplication1/user.txt');
record.addEntry(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
record.addEntry(pasteboard.MIMETYPE_TEXT_HTML, html);
```

#### \[h2\]getValidTypes14+

getValidTypes(types: Array<string>): Array<string>

根据传入的MIME类型，返回传入的MIME类型和剪贴板中数据的MIME类型的交集。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| types | Array<string> | 是 | MIME类型列表。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Array<string> | 传入的MIME类型和剪贴板中数据的MIME类型的交集。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和见[剪贴板错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-pasteboard)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```ts
let html = "<!DOCTYPE html>\n" + "<html>\n" + "<head>\n" + "<meta charset=\"utf-8\">\n" + "<title>HTML-PASTEBOARD_HTML</title>\n" + "</head>\n" + "<body>\n" + "    <h1>HEAD</h1>\n" + "    <p></p>\n" + "</body>\n" + "</html>";
let record: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE_TEXT_URI, 'dataability:///com.example.myapplication1/user.txt');
record.addEntry(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
record.addEntry(pasteboard.MIMETYPE_TEXT_HTML, html);
let types: string[] = record.getValidTypes([
    pasteboard.MIMETYPE_TEXT_PLAIN,
    pasteboard.MIMETYPE_TEXT_HTML,
    pasteboard.MIMETYPE_TEXT_URI,
    pasteboard.MIMETYPE_TEXT_WANT,
    pasteboard.MIMETYPE_PIXELMAP
]);
```

#### \[h2\]getData14+

getData(type: string): Promise<ValueType>

从PasteDataRecord中获取指定MIME类型的自定义数据。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | MIME类型，其长度不能超过1024字节。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[ValueType](#valuetype9)\> | 
Promise对象，返回PasteDataRecord中指定MIME类型的自定义数据。

PasteDataRecord中包含多个MIME类型数据时，非PasteDataRecord的默认MIME类型的数据只能通过本接口获取。

 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和见[剪贴板错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-pasteboard)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let html = "<!DOCTYPE html>\n" + "<html>\n" + "<head>\n" + "<meta charset=\"utf-8\">\n" + "<title>HTML-PASTEBOARD_HTML</title>\n" + "</head>\n" + "<body>\n" + "    <h1>HEAD</h1>\n" + "    <p></p>\n" + "</body>\n" + "</html>";
let record: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE_TEXT_URI, 'dataability:///com.example.myapplication1/user.txt');
record.addEntry(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
record.addEntry(pasteboard.MIMETYPE_TEXT_HTML, html);
record.getData(pasteboard.MIMETYPE_TEXT_PLAIN).then((value: pasteboard.ValueType) => {
    let textPlainContent = value as string;
    console.info('Success to get text/plain value. value is: ' + textPlainContent);
}).catch((err: BusinessError) => {
    console.error('Failed to get text/plain value. Cause: ' + err.message);
});
record.getData(pasteboard.MIMETYPE_TEXT_URI).then((value: pasteboard.ValueType) => {
    let uri = value as string;
    console.info('Success to get text/uri value. value is: ' + uri);
}).catch((err: BusinessError) => {
    console.error('Failed to get text/uri value. Cause: ' + err.message);
});
```

#### \[h2\]convertToText(deprecated)

convertToText(callback: AsyncCallback<string>): void

将一个PasteData中的内容强制转换为文本内容，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/C3R210vNRAqx0c-mtVkPiQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=AACF30D7FEC7660FD9C460A4111C872CD426AEE007EE35DAC820C8650A8065DF)

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[toPlainText](#toplaintext9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<string> | 是 | 回调函数，当转换成功，err为undefined，data为强制转换的文本内容；否则返回错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Possible causes: Incorrect parameters types. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let record: pasteboard.PasteDataRecord = pasteboard.createUriRecord('dataability:///com.example.myapplication1/user.txt');
record.convertToText((err: BusinessError, data: string) => {
    if (err) {
        console.error(`Failed to convert to text. Cause: ${err.message}`);
        return;
    }
    console.info(`Succeeded in converting to text. Data: ${data}`);
});
```

#### \[h2\]convertToText(deprecated)

convertToText(): Promise<string>

将一个PasteData中的内容强制转换为文本内容，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/GKrFyq6LTr21DDzoXlW8iQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=FABE86DB546D876CDAA6430143446240DB198C9CD789DD791C4ACFA6022E80C7)

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[toPlainText](#toplaintext9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | Promise对象，返回强制转换的文本内容。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let record: pasteboard.PasteDataRecord = pasteboard.createUriRecord('dataability:///com.example.myapplication1/user.txt');
record.convertToText().then((data: string) => {
    console.info(`Succeeded in converting to text. Data: ${data}`);
}).catch((err: BusinessError) => {
    console.error(`Failed to convert to text. Cause: ${err.message}`);
});
```

#### PasteData

剪贴板内容对象。剪贴板内容包含一个或者多个内容条目（[PasteDataRecord](#pastedatarecord7)）以及属性描述对象（[PasteDataProperty](#pastedataproperty7)）。

在调用PasteData的接口前，需要先通过[createData()](#pasteboardcreatedata9)或[getData()](#getdata9)获取一个PasteData对象。

**系统能力：** SystemCapability.MiscServices.Pasteboard

#### \[h2\]getPrimaryText

getPrimaryText(): string

获取第一条纯文本内容。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 纯文本内容。剪贴板内容对象中没有纯文本内容时，默认返回为undefined。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
    let text: string = pasteData.getPrimaryText();
}).catch((err: BusinessError) => {
    console.error('Failed to get PasteData. Cause: ' + err.message);
});
```

#### \[h2\]getPrimaryHtml7+

getPrimaryHtml(): string

获取第一条的HTML内容。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | HTML内容。剪贴板内容对象中没有HTML内容时，默认返回为undefined。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
    let htmlText: string = pasteData.getPrimaryHtml();
}).catch((err: BusinessError) => {
    console.error('Failed to get PasteData. Cause: ' + err.message);
});
```

#### \[h2\]getPrimaryWant7+

getPrimaryWant(): Want

获取第一条的Want对象内容。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [Want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-want) | Want对象内容。剪贴板内容对象中没有Want内容时，默认返回为undefined。 |

**示例：**

```ts
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
    let want: Want = pasteData.getPrimaryWant();
}).catch((err: BusinessError) => {
    console.error('Failed to get PasteData. Cause: ' + err.message);
});
```

#### \[h2\]getPrimaryUri7+

getPrimaryUri(): string

获取第一条的URI内容。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | URI内容。剪贴板内容对象中没有URI内容时，默认返回为undefined。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
    let uri: string = pasteData.getPrimaryUri();
}).catch((err: BusinessError) => {
    console.error('Failed to get PasteData. Cause: ' + err.message);
});
```

#### \[h2\]getPrimaryPixelMap9+

getPrimaryPixelMap(): image.PixelMap

获取第一条的PixelMap内容。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [image.PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap) | PixelMap内容。剪贴板内容对象中没有PixelMap内容时，默认返回为undefined。 |

**示例：**

```ts
import { image } from '@kit.ImageKit';

let buffer = new ArrayBuffer(128);
let realSize: image.Size = { height: 3, width: 5 };
let opt: image.InitializationOptions = {
    size: realSize,
    pixelFormat: 3,
    editable: true,
    alphaType: 1,
    scaleMode: 1
};
image.createPixelMap(buffer, opt).then((pixelMap: image.PixelMap) => {
    let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_PIXELMAP, pixelMap);
    let PixelMap: image.PixelMap = pasteData.getPrimaryPixelMap();
});
```

#### \[h2\]addRecord7+

addRecord(record: PasteDataRecord): void

向当前剪贴板内容中添加一条条目，同时也会将条目类型添加到[PasteDataProperty](#pastedataproperty7)的mimeTypes中。入参均不能为空，否则添加失败。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| record | [PasteDataRecord](#pastedatarecord7) | 是 | 待添加的条目。 |

**示例：**

```ts
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_URI, 'dataability:///com.example.myapplication1/user.txt');
let textRecord: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
let html: string = "<!DOCTYPE html>\n" + "<html>\n" + "<head>\n" + "<meta charset=\"utf-8\">\n" + "<title>HTML-PASTEBOARD_HTML</title>\n" + "</head>\n" + "<body>\n" + "    <h1>HEAD</h1>\n" + "    <p></p>\n" + "</body>\n" + "</html>";
let htmlRecord: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE_TEXT_HTML, html);
pasteData.addRecord(textRecord);
pasteData.addRecord(htmlRecord);
```

#### \[h2\]addRecord9+

addRecord(mimeType: string, value: ValueType): void

向当前剪贴板内容中添加一条数据内容条目，同时也会将数据类型添加到[PasteDataProperty](#pastedataproperty7)的mimeTypes中。入参均不能为空，否则添加失败。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| mimeType | string | 是 | 数据的MIME类型， 其长度不能超过1024字节。 |
| value | [ValueType](#valuetype9) | 是 | 数据内容。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[剪贴板错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-pasteboard)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```ts
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_URI, 'dataability:///com.example.myapplication1/user.txt');
let dataXml = new ArrayBuffer(256);
pasteData.addRecord('app/xml', dataXml);
```

#### \[h2\]getMimeTypes7+

getMimeTypes(): Array<string>

获取剪贴板中[PasteDataProperty](#pastedataproperty7)的mimeTypes列表，接口调用异常时返回undefined。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Array<string> | 剪贴板内容条目的数据类型，非重复的类型列表。 |

**示例：**

```ts
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
let types: string[] = pasteData.getMimeTypes();
```

#### \[h2\]getPrimaryMimeType7+

getPrimaryMimeType(): string

获取剪贴板内容中首个条目的数据类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 首个条目的数据类型。 |

**示例：**

```ts
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
let type: string = pasteData.getPrimaryMimeType();
```

#### \[h2\]getProperty7+

getProperty(): PasteDataProperty

获取剪贴板内容的属性描述对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [PasteDataProperty](#pastedataproperty7) | 属性描述对象。 |

**示例：**

```ts
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
let property: pasteboard.PasteDataProperty = pasteData.getProperty();
```

#### \[h2\]setProperty9+

setProperty(property: PasteDataProperty): void

设置剪贴板内容的属性描述对象[PasteDataProperty](#pastedataproperty7)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| property | [PasteDataProperty](#pastedataproperty7) | 是 | 属性描述对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ts
type AdditionType = Record<string, Record<string, Object>>;

let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_HTML, 'application/xml');
let prop: pasteboard.PasteDataProperty = pasteData.getProperty();
prop.shareOption = pasteboard.ShareOption.INAPP;
// 需要注意，不支持对addition进行追加属性的操作，只能通过重新赋值的方式达到追加属性的目的。
prop.additions = { 'TestOne': { 'Test': 123 }, 'TestTwo': { 'Test': 'additions' } } as AdditionType;
prop.tag = 'TestTag';
pasteData.setProperty(prop);
```

[PasteDataProperty](#pastedataproperty7)的localOnly与shareOption属性互斥，最终结果以shareOption为准，shareOption会影响localOnly的值。

```ts
(async () => {
    let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
    let prop: pasteboard.PasteDataProperty = pasteData.getProperty();
    prop.shareOption = pasteboard.ShareOption.INAPP;
    prop.localOnly = false;
    pasteData.setProperty(prop);
    const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();

    await systemPasteboard.setData(pasteData).then(async () => {
        console.info('Succeeded in setting PasteData.');
        await systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
            let prop: pasteboard.PasteDataProperty = pasteData.getProperty();
            prop.localOnly; // true
        });
    });

    prop.shareOption = pasteboard.ShareOption.LOCALDEVICE;
    prop.localOnly = false;
    pasteData.setProperty(prop);

    await systemPasteboard.setData(pasteData).then(async () => {
        console.info('Succeeded in setting PasteData.');
        await systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
            let prop: pasteboard.PasteDataProperty = pasteData.getProperty();
            prop.localOnly; // true
        });
    });
})
```

#### \[h2\]getRecord9+

getRecord(index: number): PasteDataRecord

获取剪贴板内容中指定下标的条目。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| index | number | 是 | 指定条目的下标。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [PasteDataRecord](#pastedatarecord7) | 指定下标的条目。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[剪贴板错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-pasteboard)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12900001 | The index is out of the record. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
let record: pasteboard.PasteDataRecord = pasteData.getRecord(0);
```

#### \[h2\]getRecordCount7+

getRecordCount(): number

获取剪贴板内容中条目的个数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 条目的个数。 |

**示例：**

```ts
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
let count: number = pasteData.getRecordCount();
```

#### \[h2\]getTag7+

getTag(): string

获取剪贴板内容中用户自定义的标签内容，如果没有设置用户自定义的标签内容将返回空。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 返回用户自定义的标签内容，如果没有设置用户自定义的标签内容，将返回空。 |

**示例：**

```ts
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
let tag: string = pasteData.getTag();
```

#### \[h2\]hasType9+

hasType(mimeType: string): boolean

检查剪贴板内容中是否有指定的MIME数据类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| mimeType | string | 是 | 待查询的数据类型。可以是[常量](#常量)中已定义的类型，包括HTML类型，WANT类型，纯文本类型，URI类型，PIXELMAP类型；也可以是自定义的MIME类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 有指定的数据类型返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ts
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
let hasType: boolean = pasteData.hasType(pasteboard.MIMETYPE_TEXT_PLAIN);
```

#### \[h2\]removeRecord9+

removeRecord(index: number): void

移除剪贴板内容中指定下标的条目。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| index | number | 是 | 指定的下标。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[剪贴板错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-pasteboard)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12900001 | The index is out of the record. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |

**示例：**

```ts
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
pasteData.removeRecord(0);
```

#### \[h2\]replaceRecord9+

replaceRecord(index: number, record: PasteDataRecord): void

替换剪贴板内容中指定下标的条目。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| index | number | 是 | 指定的下标。 |
| record | [PasteDataRecord](#pastedatarecord7) | 是 | 被替换后的条目数据内容。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[剪贴板错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-pasteboard)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12900001 | The index is out of the record. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |

**示例：**

```ts
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
let record: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE_TEXT_URI, 'file://com.example.myapplication1/data/storage/el2/base/files/file.txt');
pasteData.replaceRecord(0, record);
```

#### \[h2\]pasteStart12+

pasteStart(): void

读取剪贴板数据前，通知剪贴板服务保留跨设备通道。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getData((err: BusinessError, pasteData: pasteboard.PasteData) => {
    if (err) {
        console.error('Failed to get PasteData. Cause: ' + err.message);
        return;
    }
    pasteData.pasteStart();
    console.info(`using data: ${pasteData.getPrimaryText()}`);
    pasteData.pasteComplete();
});
```

#### \[h2\]pasteComplete12+

pasteComplete(): void

通知剪贴板服务数据使用已完成。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getData((err: BusinessError, pasteData: pasteboard.PasteData) => {
    if (err) {
        console.error('Failed to get PasteData. Cause: ' + err.message);
        return;
    }
    pasteData.pasteStart();
    console.info(`using data: ${pasteData.getPrimaryText()}`);
    pasteData.pasteComplete();
});
```

#### \[h2\]addHtmlRecord(deprecated)

addHtmlRecord(htmlText: string): void

向当前剪贴板内容中添加一条HTML内容条目，并将MIMETYPE\_TEXT\_HTML添加到[PasteDataProperty](#pastedataproperty7)的mimeTypes中。入参均不能为空，否则添加失败。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/-bXSYdnVQAqXAaGAErXV_w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=1363826AF869E39940AD9E5E2C88CE7F14F0C920F6A05842E9AF5ACDFA792791)

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[addRecord](#addrecord9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| htmlText | string | 是 | HTML内容。 |

**示例：**

```ts
let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
let html: string = "<!DOCTYPE html>\n" + "<html>\n" + "<head>\n" + "<meta charset=\"utf-8\">\n" + "<title>HTML-PASTEBOARD_HTML</title>\n" + "</head>\n" + "<body>\n" + "    <h1>HEAD</h1>\n" + "    <p></p>\n" + "</body>\n" + "</html>";
pasteData.addHtmlRecord(html);
```

#### \[h2\]addWantRecord(deprecated)

addWantRecord(want: Want): void

向当前剪贴板内容中添加一条Want条目，并将MIMETYPE\_TEXT\_WANT添加到[PasteDataProperty](#pastedataproperty7)的mimeTypes中。入参均不能为空，否则添加失败。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/1tWtZrDfT7CQMAHdYS9Jfg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=B5B20702E60B16E2E0272192400F4AC68490475863E2A6A77570DD06852DABA7)

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[addRecord](#addrecord9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| want | [Want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-want) | 是 | Want对象内容。 |

**示例：**

```ts
import { Want } from '@kit.AbilityKit';

let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
let object: Want = {
    bundleName: "com.example.aafwk.test",
    abilityName: "com.example.aafwk.test.TwoAbility"
};
pasteData.addWantRecord(object);
```

#### \[h2\]addTextRecord(deprecated)

addTextRecord(text: string): void

向当前剪贴板内容中添加一条纯文本条目，并将MIMETYPE\_TEXT\_PLAIN添加到[PasteDataProperty](#pastedataproperty7)的mimeTypes中。入参均不能为空，否则添加失败。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/PJdck_ifTsWfXLaSfnEV2g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=C7F36FD8F3DA83AE4A96C424895D71743DA582F720636E3D466B86EF75B7E0B4)

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[addRecord](#addrecord9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| text | string | 是 | 纯文本内容。 |

**示例：**

```ts
let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
pasteData.addTextRecord('good');
```

#### \[h2\]addUriRecord(deprecated)

addUriRecord(uri: string): void

向当前剪贴板内容中添加一条URI条目，并将MIMETYPE\_TEXT\_URI添加到[PasteDataProperty](#pastedataproperty7)的mimeTypes中。入参均不能为空，否则添加失败。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/EFDKi7D-StCN9_gqHBMsdQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=FC482FC6809137D0294312492CFFB18FB3B01AAE1F8C55E914AB12F5D9991B5D)

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[addRecord](#addrecord9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| uri | string | 是 | URI内容。 |

**示例：**

```ts
let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
pasteData.addUriRecord('dataability:///com.example.myapplication1/user.txt');
```

#### \[h2\]getRecordAt(deprecated)

getRecordAt(index: number): PasteDataRecord

获取剪贴板内容中指定下标的条目。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/TuIuxkelTwmFc4cr-ja76w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=822A3258AC6FD12DEA8877E729396175F2D7E82C795B915373FE3283BC52615B)

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[getRecord](#getrecord9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| index | number | 是 | 指定条目的下标。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [PasteDataRecord](#pastedatarecord7) | 指定下标的条目。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ts
let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
let record: pasteboard.PasteDataRecord = pasteData.getRecordAt(0);
```

#### \[h2\]hasMimeType(deprecated)

hasMimeType(mimeType: string): boolean

检查剪贴板内容中是否有指定的数据类型。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/rvOjg-W-RPGzmUwI5ucNAg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=EA0828D344C29A68150AF4BD2FB2ED63DEA8FCA6681C20F610BE3F0B17216F52)

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[hasType](#hastype9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| mimeType | string | 是 | 待查询的数据类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 有指定的数据类型返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ts
let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
let hasType: boolean = pasteData.hasMimeType(pasteboard.MIMETYPE_TEXT_PLAIN);
```

#### \[h2\]removeRecordAt(deprecated)

removeRecordAt(index: number): boolean

移除剪贴板内容中指定下标的条目。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/TX-ctpgzQqisIHJfW0oBvg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=7EDA5E5850954D1FBE7F88C6493D298AC98A2B16C7EC200713108BD564373155)

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[removeRecord](#removerecord9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| index | number | 是 | 指定的下标。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 成功移除返回true，失败返回false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ts
let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
let isRemove: boolean = pasteData.removeRecordAt(0);
```

#### \[h2\]replaceRecordAt(deprecated)

replaceRecordAt(index: number, record: PasteDataRecord): boolean

替换剪贴板内容中指定下标的条目。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/88pi2LCdRzapHbY6Euo67w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=515607E60DFED56A546A7ED949AE17505637480B1A5D6245558A4AB56E198018)

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[replaceRecord](#replacerecord9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| index | number | 是 | 指定的下标。 |
| record | [PasteDataRecord](#pastedatarecord7) | 是 | 替换后的条目。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 成功替换返回true，失败返回false。 |

**示例：**

```ts
let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
let record: pasteboard.PasteDataRecord = pasteboard.createUriRecord('dataability:///com.example.myapplication1/user.txt');
let isReplace: boolean = pasteData.replaceRecordAt(0, record);
```

#### SystemPasteboard

系统剪贴板对象。

在调用SystemPasteboard的接口前，需要先通过[getSystemPasteboard](#pasteboardgetsystempasteboard)获取系统剪贴板。

```ts
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
```

#### \[h2\]on('update')7+

on(type: 'update', callback: () =>void): void

订阅系统剪贴板内容变化事件，当系统剪贴板中内容变化时触发用户程序的回调。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 取值为'update'，表示系统剪贴板内容变化事件。 |
| callback | function | 是 | 剪贴板中内容变化时触发的用户程序的回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ts
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
let listener = () => {
    console.info('The system pasteboard has changed.');
};
systemPasteboard.on('update', listener);
```

#### \[h2\]off('update')7+

off(type: 'update', callback?: () =>void): void

取消订阅系统剪贴板内容变化事件。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 取值为'update'，表示系统剪贴板内容变化事件。 |
| callback | function | 否 | 剪贴板中内容变化时触发的用户程序的回调。如果此参数未填，表明清除本应用的所有监听回调，否则表示清除指定监听回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ts
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
let listener = () => {
    console.info('The system pasteboard has changed.');
};
systemPasteboard.off('update', listener);
```

#### \[h2\]clearData9+

clearData(callback: AsyncCallback<void>): void

清空系统剪贴板内容，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | 是 | 回调函数。当成功清空时，err为undefined；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ts
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.clearData((err, data) => {
    if (err) {
        console.error(`Failed to clear the pasteboard. Cause: ${err.message}`);
        return;
    }
    console.info('Succeeded in clearing the pasteboard.');
});
```

#### \[h2\]clearData9+

clearData(): Promise<void>

清空系统剪贴板内容，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.clearData().then((data: void) => {
    console.info('Succeeded in clearing the pasteboard.');
}).catch((err: BusinessError) => {
    console.error(`Failed to clear the pasteboard. Cause: ${err.message}`);
});
```

#### \[h2\]setData9+

setData(data: PasteData, callback: AsyncCallback<void>): void

将数据写入系统剪贴板，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| data | [PasteData](#pastedata) | 是 | PasteData对象。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当写入成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[剪贴板错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-pasteboard)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 27787277 | Another copy or paste operation is in progress. |
| 27787278 | Replication is prohibited. |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ts
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'content');
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.setData(pasteData, (err, data) => {
    if (err) {
        console.error('Failed to set PasteData. Cause: ' + err.message);
        return;
    }
    console.info('Succeeded in setting PasteData.');
});
```

#### \[h2\]setData9+

setData(data: PasteData): Promise<void>

将数据写入系统剪贴板，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| data | [PasteData](#pastedata) | 是 | PasteData对象。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[剪贴板错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-pasteboard)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 27787277 | Another copy or paste operation is in progress. |
| 27787278 | Replication is prohibited. |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'content');
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.setData(pasteData).then((data: void) => {
    console.info('Succeeded in setting PasteData.');
}).catch((err: BusinessError) => {
    console.error('Failed to set PasteData. Cause: ' + err.message);
});
```

#### \[h2\]getData9+

getData(callback: AsyncCallback<PasteData>): void

读取系统剪贴板内容，使用callback异步回调。

**需要权限**：ohos.permission.READ\_PASTEBOARD，应用访问剪贴板内容需[申请访问剪贴板权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/get-pastedata-permission-guidelines)。[使用粘贴控件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pastebutton)访问剪贴板内容的应用，可以无需申请权限。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[PasteData](#pastedata)\> | 是 | 回调函数。当读取成功，err为undefined，data为返回的系统剪贴板数据；否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[剪贴板错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-pasteboard)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 27787277 | Another copy or paste operation is in progress. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getData((err: BusinessError, pasteData: pasteboard.PasteData) => {
    if (err) {
        console.error('Failed to get PasteData. Cause: ' + err.message);
        return;
    }
    let text: string = pasteData.getPrimaryText();
});
```

#### \[h2\]getData9+

getData(): Promise<PasteData>

读取系统剪贴板内容，使用Promise异步回调。

**需要权限**：ohos.permission.READ\_PASTEBOARD，应用访问剪贴板内容需[申请访问剪贴板权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/get-pastedata-permission-guidelines)。[使用粘贴控件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pastebutton)访问剪贴板内容的应用，可以无需申请权限。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[PasteData](#pastedata)\> | Promise对象，返回系统剪贴板数据。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[剪贴板错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-pasteboard)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 27787277 | Another copy or paste operation is in progress. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
    let text: string = pasteData.getPrimaryText();
}).catch((err: BusinessError) => {
    console.error('Failed to get PasteData. Cause: ' + err.message);
});
```

#### \[h2\]hasData9+

hasData(callback: AsyncCallback<boolean>): void

判断系统剪贴板中是否有内容，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | 是 | 返回true表示系统剪贴板中有内容，返回false表示系统剪贴板中没有内容。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.hasData((err: BusinessError, data: boolean) => {
    if (err) {
        console.error(`Failed to check the PasteData. Cause: ${err.message}`);
        return;
    }
    console.info(`Succeeded in checking the PasteData. Data: ${data}`);
});
```

#### \[h2\]hasData9+

hasData(): Promise<boolean>

判断系统剪贴板中是否有内容，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | 返回true表示系统剪贴板中有内容，返回false表示系统剪贴板中没有内容。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.hasData().then((data: boolean) => {
    console.info(`Succeeded in checking the PasteData. Data: ${data}`);
}).catch((err: BusinessError) => {
    console.error(`Failed to check the PasteData. Cause: ${err.message}`);
});
```

#### \[h2\]clear(deprecated)

clear(callback: AsyncCallback<void>): void

清空系统剪贴板内容，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/vvs6UM5mTvCZK81mNYVASw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=472D2DFE00F14FB61E089D383E19397BA07DEFAA1BB7405F02BFF5FC0CB9E603)

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[pasteboard.clearData](#cleardata9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | 是 | 回调函数。当成功清空时，err为undefined；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ts
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.clear((err, data) => {
    if (err) {
        console.error(`Failed to clear the PasteData. Cause: ${err.message}`);
        return;
    }
    console.info('Succeeded in clearing the PasteData.');
});
```

#### \[h2\]clear(deprecated)

clear(): Promise<void>

清空系统剪贴板内容，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/ikkd4t3UTRCdBTeY8QntiA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=DCEA5F6A3E8FD51D275B7B846E9B6D6CFCF4ADBCB0EB31DEC45580E061CBF2CA)

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[pasteboard.clearData](#cleardata9-1)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.clear().then((data) => {
    console.info('Succeeded in clearing the PasteData.');
}).catch((err: BusinessError) => {
    console.error(`Failed to clear the PasteData. Cause: ${err.message}`);
});
```

#### \[h2\]getPasteData(deprecated)

getPasteData(callback: AsyncCallback<PasteData>): void

读取系统剪贴板内容，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/IHFE1XqkTHeD-QVGmxs6ag/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=EBCAF3587F948C4ACD587FCDC5BDB9F570780A256882AD68CCB45E151AC45A65)

从 API version 6 开始支持，从 API version 9 开始废弃，建议使用[getData](#getdata9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[PasteData](#pastedata)\> | 是 | 回调函数。当读取成功，err为undefined，data为返回的系统剪贴板数据；否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getPasteData((err: BusinessError, pasteData: pasteboard.PasteData) => {
    if (err) {
        console.error('Failed to get PasteData. Cause: ' + err.message);
        return;
    }
    let text: string = pasteData.getPrimaryText();
});
```

#### \[h2\]getPasteData(deprecated)

getPasteData(): Promise<PasteData>

读取系统剪贴板内容，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/MOZ_gMbbROinaz2cbh-UPw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=CC2E6CA10F6AE333EBBA375519B7266E1F13F1B5B202EA4513044539D726D6F0)

从 API version 6 开始支持，从 API version 9 开始废弃，建议使用[getData](#getdata9-1)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[PasteData](#pastedata)\> | Promise对象，返回系统剪贴板数据。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getPasteData().then((pasteData: pasteboard.PasteData) => {
    let text: string = pasteData.getPrimaryText();
}).catch((err: BusinessError) => {
    console.error('Failed to get PasteData. Cause: ' + err.message);
});
```

#### \[h2\]hasPasteData(deprecated)

hasPasteData(callback: AsyncCallback<boolean>): void

判断系统剪贴板中是否有内容，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/K5n6C9RWS1WIbzKBuydfGQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=09D4168859EC0ED709055CCFEA2F103D952AFB186F198C72DFFDC07EE6E8BC66)

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[hasData](#hasdata9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | 是 | 返回true表示系统剪贴板中有内容，返回false表示系统剪贴板中没有内容。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.hasPasteData((err: BusinessError, data: boolean) => {
    if (err) {
        console.error(`Failed to check the PasteData. Cause: ${err.message}`);
        return;
    }
    console.info(`Succeeded in checking the PasteData. Data: ${data}`);
});
```

#### \[h2\]hasPasteData(deprecated)

hasPasteData(): Promise<boolean>

判断系统剪贴板中是否有内容，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/8kO9e7PFTfGDEUVV9Edvqg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=983BD6D322813A1C428934E2CF4EACD9D1C41917F742F08667866590E568707A)

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[hasData](#hasdata9-1)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | 返回true表示系统剪贴板中有内容，返回false表示系统剪贴板中没有内容。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.hasPasteData().then((data: boolean) => {
    console.info(`Succeeded in checking the PasteData. Data: ${data}`);
}).catch((err: BusinessError) => {
    console.error(`Failed to check the PasteData. Cause: ${err.message}`);
});
```

#### \[h2\]setPasteData(deprecated)

setPasteData(data: PasteData, callback: AsyncCallback<void>): void

将数据写入系统剪贴板，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/kSoXrZYvQWmRb7DsZLhsjQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=8B86E2EECCE8F4032FB120C44EB3E50AC567E4BDC04770CD283D33B2F57DE8EE)

从 API version 6 开始支持，从 API version 9 开始废弃，建议使用[setData](#setdata9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| data | [PasteData](#pastedata) | 是 | PasteData对象。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当写入成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ts
let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('content');
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.setPasteData(pasteData, (err, data) => {
    if (err) {
        console.error('Failed to set PasteData. Cause: ' + err.message);
        return;
    }
    console.info('Succeeded in setting PasteData.');
});
```

#### \[h2\]setPasteData(deprecated)

setPasteData(data: PasteData): Promise<void>

将数据写入系统剪贴板，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/IKqcyVYZQ0-GZebzYsx3_w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=A65521390F078397A2DC1860139DBB150CE17102D35F7CB1C413F9722C50757B)

从 API version 6 开始支持，从 API version 9 开始废弃，建议使用[setData](#setdata9-1)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| data | [PasteData](#pastedata) | 是 | PasteData对象。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('content');
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.setPasteData(pasteData).then((data: void) => {
    console.info('Succeeded in setting PasteData.');
}).catch((err: BusinessError) => {
    console.error('Failed to set PasteData. Cause: ' + err.message);
});
```

#### \[h2\]isRemoteData11+

isRemoteData(): boolean

判断剪贴板中的数据是否来自其他设备。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 是来自其他设备返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[剪贴板错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-pasteboard)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12900005 | Excessive processing time for internal data. |

**示例：**

```ts
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    let result: boolean = systemPasteboard.isRemoteData();
    console.info(`Succeeded in checking the RemoteData. Result: ${result}`);
} catch (err) {
    console.error('Failed to check the RemoteData. Cause:' + err.message);
};
```

#### \[h2\]getDataSource11+

getDataSource(): string

获取数据来源的应用名称。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 数据来源的应用名称。 |

**错误码：**

以下错误码的详细介绍请参见[剪贴板错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-pasteboard)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12900005 | Excessive processing time for internal data. |

**示例：**

```ts
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    let result: string = systemPasteboard.getDataSource();
    console.info(`Succeeded in getting DataSource. Result: ${result}`);
} catch (err) {
    console.error('Failed to get DataSource. Cause:' + err.message);
};
```

#### \[h2\]hasDataType11+

hasDataType(mimeType: string): boolean

检查剪贴板内容中是否有指定类型的数据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| mimeType | string | 是 | 数据类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 有指定类型的数据返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[剪贴板错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-pasteboard)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 12900005 | Excessive processing time for internal data. |

**示例：**

```ts
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    let result: boolean = systemPasteboard.hasDataType(pasteboard.MIMETYPE_TEXT_PLAIN);
    console.info(`Succeeded in checking the DataType. Result: ${result}`);
} catch (err) {
    console.error('Failed to check the DataType. Cause:' + err.message);
};
```

#### \[h2\]clearDataSync11+

clearDataSync(): void

清空系统剪贴板内容, 此接口为同步接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**错误码：**

以下错误码的详细介绍请参见[剪贴板错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-pasteboard)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12900005 | Excessive processing time for internal data. |

**示例：**

```ts
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    systemPasteboard.clearDataSync();
    console.info('Succeeded in clearing the pasteboard.');
} catch (err) {
    console.error('Failed to clear the pasteboard. Cause:' + err.message);
};
```

#### \[h2\]getDataSync11+

getDataSync(): PasteData

读取系统剪贴板内容, 此接口为同步接口。

**需要权限**：ohos.permission.READ\_PASTEBOARD，应用访问剪贴板内容需[申请访问剪贴板权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/get-pastedata-permission-guidelines)。[使用粘贴控件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pastebutton)访问剪贴板内容的应用，可以无需申请权限。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [PasteData](#pastedata) | 返回系统剪贴板数据。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[剪贴板错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-pasteboard)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12900005 | Excessive processing time for internal data. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ts
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    let result: pasteboard.PasteData = systemPasteboard.getDataSync();
    console.info('Succeeded in getting PasteData.');
} catch (err) {
    console.error('Failed to get PasteData. Cause:' + err.message);
};
```

#### \[h2\]setDataSync11+

setDataSync(data: PasteData): void

将数据写入系统剪贴板, 此接口为同步接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| data | [PasteData](#pastedata) | 是 | 需要写入剪贴板中的数据。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[剪贴板错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-pasteboard)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 12900005 | Excessive processing time for internal data. |

**示例：**

```ts
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    systemPasteboard.setDataSync(pasteData);
    console.info('Succeeded in setting PasteData.');
} catch (err) {
    console.error('Failed to set PasteData. Cause:' + err.message);
};
```

#### \[h2\]hasDataSync11+

hasDataSync(): boolean

判断系统剪贴板中是否有内容, 此接口为同步接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 返回true表示系统剪贴板中有内容，返回false表示系统剪贴板中没有内容。 |

**错误码：**

以下错误码的详细介绍请参见[剪贴板错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-pasteboard)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 12900005 | Excessive processing time for internal data. |

**示例：**

```ts
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    let result: boolean = systemPasteboard.hasDataSync();
    console.info(`Succeeded in checking the PasteData. Result: ${result}`);
} catch (err) {
    console.error('Failed to check the PasteData. Cause:' + err.message);
};
```

#### \[h2\]getUnifiedData12+

getUnifiedData(): Promise<unifiedDataChannel.UnifiedData>

读取系统剪贴板内容，使用Promise异步回调。

**需要权限**：ohos.permission.READ\_PASTEBOARD，应用访问剪贴板内容需[申请访问剪贴板权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/get-pastedata-permission-guidelines)。[使用粘贴控件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pastebutton)访问剪贴板内容的应用，可以无需申请权限。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[unifiedDataChannel.UnifiedData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-unifieddatachannel#unifieddata)\> | Promise对象，返回系统剪贴板数据。 |

**错误码：**

以下错误码的详细介绍请参见[剪贴板错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-pasteboard)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 27787277 | Another copy or paste operation is in progress. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { unifiedDataChannel, uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getUnifiedData().then((data) => {
    let records: Array<unifiedDataChannel.UnifiedRecord> = data.getRecords();
    for (let j = 0; j < records.length; j++) {
        if (records[j].getType() === uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) {
            let text = records[j].getValue() as uniformDataStruct.PlainText;
            console.info(`${j + 1}.${text.textContent}`);
        }
    }
}).catch((err: BusinessError) => {
    console.error('Failed to get UnifiedData. Cause: ' + err.message);
});
```

#### \[h2\]getUnifiedDataSync12+

getUnifiedDataSync(): unifiedDataChannel.UnifiedData

读取系统剪贴板内容, 此接口为同步接口。

**需要权限**：ohos.permission.READ\_PASTEBOARD，应用访问剪贴板内容需[申请访问剪贴板权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/get-pastedata-permission-guidelines)。[使用粘贴控件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pastebutton)访问剪贴板内容的应用，可以无需申请权限。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [unifiedDataChannel.UnifiedData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-unifieddatachannel#unifieddata) | 返回系统剪贴板数据。 |

**错误码：**

以下错误码的详细介绍请参见[剪贴板错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-pasteboard)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 12900005 | Excessive processing time for internal data. |

**示例：**

```ts
import { unifiedDataChannel } from '@kit.ArkData';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    let result: unifiedDataChannel.UnifiedData = systemPasteboard.getUnifiedDataSync();
    console.info('Succeeded in getting UnifiedData.');
} catch (err) {
    console.error('Failed to get UnifiedData. Cause:' + err.message);
};
```

#### \[h2\]setUnifiedData12+

setUnifiedData(data: unifiedDataChannel.UnifiedData): Promise<void>

将数据写入系统剪贴板，使用Promise异步回调。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| data | [unifiedDataChannel.UnifiedData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-unifieddatachannel#unifieddata) | 是 | 需要写入剪贴板中的数据。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[剪贴板错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-pasteboard)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 27787277 | Another copy or paste operation is in progress. |
| 27787278 | Replication is prohibited. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { unifiedDataChannel, uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';

let plainText : uniformDataStruct.PlainText = {
    uniformDataType: uniformTypeDescriptor.UniformDataType.PLAIN_TEXT,
    textContent : 'PLAINTEXT_CONTENT',
    abstract : 'PLAINTEXT_ABSTRACT',
}
let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);
let data = new unifiedDataChannel.UnifiedData();
data.addRecord(record);

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.setUnifiedData(data).then((data: void) => {
    console.info('Succeeded in setting UnifiedData.');
}).catch((err: BusinessError) => {
    console.error('Failed to setUnifiedData. Cause: ' + err.message);
});
```

#### \[h2\]setUnifiedDataSync12+

setUnifiedDataSync(data: unifiedDataChannel.UnifiedData): void

将数据写入系统剪贴板, 此接口为同步接口。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| data | [unifiedDataChannel.UnifiedData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-unifieddatachannel#unifieddata) | 是 | 需要写入剪贴板中的数据。 |

**错误码：**

以下错误码的详细介绍请参见[剪贴板错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-pasteboard)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 12900005 | Excessive processing time for internal data. |

**示例：**

```ts
import { unifiedDataChannel } from '@kit.ArkData';

let plainTextData = new unifiedDataChannel.UnifiedData();
let plainText = new unifiedDataChannel.PlainText();
plainText.details = {
    Key: 'delayPlaintext',
    Value: 'delayPlaintext',
};
plainText.textContent = 'delayTextContent';
plainText.abstract = 'delayTextContent';
plainTextData.addRecord(plainText);

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    systemPasteboard.setUnifiedDataSync(plainTextData);
    console.info('Succeeded in setting UnifiedData.');
} catch (err) {
    console.error('Failed to set UnifiedData. Cause:' + err.message);
};
```

#### \[h2\]setAppShareOptions14+

setAppShareOptions(shareOptions: ShareOption): void

应用设置本应用剪贴板数据的可粘贴范围。

**需要权限**：ohos.permission.MANAGE\_PASTEBOARD\_APP\_SHARE\_OPTION

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| shareOptions | [ShareOption](#shareoption9) | 是 | 可粘贴的范围，参数只允许pasteboard.ShareOption.INAPP。 |

**错误码：**

以下错误码的详细介绍请参见[剪贴板错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-pasteboard)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12900006 | Settings already exist. |

**示例：**

```ts
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
  systemPasteboard.setAppShareOptions(pasteboard.ShareOption.INAPP);
  console.info('Set app share options success.');
} catch (error) {
  console.error(`Set app share options failed, errorCode: ${error.code}, errorMessage: ${error.message}.`);
}
```

#### \[h2\]removeAppShareOptions14+

removeAppShareOptions(): void

删除应用全局的可粘贴的范围。

**需要权限**：ohos.permission.MANAGE\_PASTEBOARD\_APP\_SHARE\_OPTION

**系统能力：** SystemCapability.MiscServices.Pasteboard

**错误码：**

以下错误码的详细介绍请参见[剪贴板错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-pasteboard)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ts
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
  systemPasteboard.removeAppShareOptions();
  console.info('Remove app share options success.');
} catch (error) {
  console.error(`Remove app share options failed, errorCode: ${error.code}, errorMessage: ${error.message}.`);
}
```

#### \[h2\]Pattern13+

剪贴板支持检测的模式类型。

**系统能力：** SystemCapability.MiscServices.Pasteboard

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| URL | 0 | URL类型。 |
| NUMBER | 1 | 数字类型。 |
| EMAIL\_ADDRESS | 2 | 邮箱地址类型。 |

#### \[h2\]detectPatterns13+

detectPatterns(patterns: Array<Pattern>): Promise<Array<Pattern>>

检测**本地**剪贴板中存在的[Pattern](#pattern13)模式，使用Promise异步回调。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| patterns | [Array<Pattern>](#pattern13) | 是 | 需要在剪贴板中检测的模式。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<Pattern>> | Promise对象，返回检测到的模式。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. 3. Parameter verification failed. |

**示例：**

```ts
import { pasteboard } from '@kit.BasicServicesKit'

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
let patterns: Array<pasteboard.Pattern> = [pasteboard.Pattern.URL, pasteboard.Pattern.EMAIL_ADDRESS];

systemPasteboard.detectPatterns(patterns).then((data: Array<pasteboard.Pattern>) => {
    if (patterns.sort().join('')==data.sort().join('')) {
      console.info('All needed patterns detected, next get data');
      try {
        let result: pasteboard.PasteData = systemPasteboard.getDataSync();
        console.info('Succeeded in getting PasteData.');
      } catch (err) {
        console.error('Failed to get PasteData. Cause:' + err.message);
      };
    } else {
      console.info("Not all needed patterns detected, no need to get data.");
    }
});
```

#### \[h2\]getMimeTypes14+

getMimeTypes(): Promise<Array<string>>

读取剪贴板中存在的MIME类型，使用Promise异步回调。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<string>> | Promise对象，返回读取到的MIME类型。 |

**示例：**

```ts
import { pasteboard, BusinessError } from '@kit.BasicServicesKit'

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getMimeTypes().then((data: Array<string>) => {
    console.info('Succeeded in getting mimeTypes. mimeTypes: ' + data.sort().join(','));
}).catch((err: BusinessError) => {
    console.error('Failed to get mimeTypes. Cause:' + err.message);
});
```

#### \[h2\]getDataWithProgress15+

getDataWithProgress(params: GetDataParams): Promise<PasteData>

获取剪贴板的内容和进度，使用Promise异步回调，不支持对文件夹的拷贝。

**需要权限**：ohos.permission.READ\_PASTEBOARD，应用访问剪贴板内容需[申请访问剪贴板权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/get-pastedata-permission-guidelines)。[使用粘贴控件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pastebutton)访问剪贴板内容的应用，可以无需申请权限。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| params | [GetDataParams](#getdataparams15) | 是 | 应用在使用剪贴板提供的文件拷贝能力的情况下需要的参数，包含目标路径、文件冲突选项、进度条类型等。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[PasteData](#pastedata)\> | Promise对象，返回系统剪贴板数据。 |

**错误码：**

以下错误码的详细介绍请参见[剪贴板错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-pasteboard)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. |
| 12900003 | Another copy or paste operation is in progress. |
| 12900007 | Invalid destUri or file system error. |
| 12900008 | Failed to start progress. |
| 12900009 | Progress exits abnormally. |
| 12900010 | System error occurred during paste execution. |

**示例：**

```ts
import { BusinessError, pasteboard } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';
@Entry
@Component
struct PasteboardTest {
 build() {
   RelativeContainer() {
     Column() {
       Column() {
         Button("Copy txt")
           .onClick(async ()=>{
              let text = "test";
              let pasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, text);
              let systemPasteboard = pasteboard.getSystemPasteboard();
              await systemPasteboard.setData(pasteData);
              let progressListenerInfo = (progress: pasteboard.ProgressInfo) => {
                console.info('progressListener success, progress:' + progress.progress);
              };
              let destPath: string = '/data/storage/el2/base/files/';
              let destUri : string = fileUri.getUriFromPath(destPath);
              let params: pasteboard.GetDataParams = {
                destUri: destUri,
                fileConflictOptions: pasteboard.FileConflictOptions.OVERWRITE,
                progressIndicator: pasteboard.ProgressIndicator.DEFAULT,
                progressListener: progressListenerInfo,
              };
              systemPasteboard.getDataWithProgress(params).then((pasteData: pasteboard.PasteData) => {
                console.info('getDataWithProgress success');
              }).catch((err: BusinessError) => {
                console.error('Failed to get PasteData. Cause: ' + err.message);
              })
          })
        }
      }
    }
  }
}
```

#### \[h2\]getChangeCount18+

getChangeCount(): number

获取剪贴板内容的变化次数。

执行成功时返回剪贴板内容的变化次数，否则返回0。

当剪贴板内容过期或调用[clearDataSync](#cleardatasync11)等接口导致剪贴板内容为空时，内容变化次数不会因此改变。

系统重启或剪贴板服务异常重启时，剪贴板内容变化次数重新从0开始计数。对同一内容连续多次复制会被视作多次更改，每次复制均会导致内容变化次数增加。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回读取到的剪贴板内容变化次数。 |

**示例：**

```ts
import { BusinessError, pasteboard } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    let result : number = systemPasteboard.getChangeCount();
    console.info(`Succeeded in getting the ChangeCount. Result: ${result}`);
} catch (err) {
    console.error(`Failed to get the ChangeCount. Cause: ${err.message}`);
};
```

#### \[h2\]UpdateCallback 22+

type UpdateCallback = () => void

表示剪贴板内容变更的回调

**系统能力：** SystemCapability.MiscServices.Pasteboard

#### \[h2\]onRemoteUpdate(callback: UpdateCallback)22+

onRemoteUpdate(callback: UpdateCallback): void

订阅跨设备剪贴板内容变化事件，当远端设备系统剪贴板中内容变化时触发用户程序的回调。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | [UpdateCallback](#updatecallback-22) | 是 | 剪贴板中内容变化时触发的用户程序的回调。 |

**示例：**

```ts
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
let listener = () => {
    console.info('The remote pasteboard has changed.');
};
systemPasteboard.onRemoteUpdate(listener);
```

#### \[h2\]offRemoteUpdate22+

offRemoteUpdate(callback?: UpdateCallback): void

取消订阅跨设备剪贴板内容变化事件。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | [UpdateCallback](#updatecallback-22) | 否 | 远端设备剪贴板中内容变化时触发的用户程序的回调。如果此参数未填，表明清除本应用的所有远端监听回调，否则表示清除指定远端监听回调。 |

**示例：**

```ts
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
let listener = () => {
    console.info('The remote pasteboard has changed.');
};
systemPasteboard.offRemoteUpdate(listener);
```

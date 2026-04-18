---
title: "@ohos.connectedTag (有源标签)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-connectedtag"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Connectivity Kit（短距通信服务）"
  - "ArkTS API"
  - "@ohos.connectedTag (有源标签)"
captured_at: "2026-04-17T01:48:21.472Z"
---

# @ohos.connectedTag (有源标签)

本模块提供有源标签的使用，包括初始化有源标签芯片、读取有源标签内容、写入内容到有源标签等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/CycX46p7Q3ak0TBJxee5YA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=DAEEBDC6CFDAE396512263334C81A0F8769DB4B5DCC5B1953A1F1DB88A025C37)

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```js
import { connectedTag } from '@kit.ConnectivityKit';
```

#### connectedTag.init(deprecated)

init(): boolean

初始化有源标签芯片。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/KVdqwXkORQKbszQHaWB9LA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=444547630BC995D4D4AAF6A0F6136C7E0073E11CE86C402B789B7C813396B6B1)

从API version 8开始支持，从API version 9开始废弃，建议使用[initialize](#connectedtaginitialize9)替代。

**需要权限**：ohos.permission.NFC\_TAG

**系统能力**：SystemCapability.Communication.ConnectedTag

**返回值：**

| **类型** | **说明** |
| :-- | :-- |
| boolean | 
true：初始化成功。

false：初始化失败。

 |

#### connectedTag.initialize9+

initialize(): void

初始化有源标签芯片。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.ConnectedTag

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[NFC错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-nfc)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 3200101 | Connected NFC tag running state is abnormal in service. |

#### connectedTag.uninit(deprecated)

uninit(): boolean

卸载有源标签芯片资源。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/0piow4DHT3uClrT75PA0eA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=843E8496E9450899ACA198D241C9B03481F32DD5401AF4E6A67D93704FA0D2AE)

从API version 8开始支持，从API version 9开始废弃，建议使用[uninitialize](#connectedtaguninitialize9)替代。

**需要权限**：ohos.permission.NFC\_TAG

**系统能力**：SystemCapability.Communication.ConnectedTag

**返回值：**

| **类型** | **说明** |
| :-- | :-- |
| boolean | 
true：卸载操作成功。

false：卸载操作失败。

 |

#### connectedTag.uninitialize9+

uninitialize(): void

卸载有源标签芯片资源。

**需要权限:** ohos.permission.NFC\_TAG

**系统能力:** SystemCapability.Communication.ConnectedTag

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[NFC错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-nfc)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 3200101 | Connected NFC tag running state is abnormal in service. |

#### connectedTag.readNdefTag(deprecated)

readNdefTag(): Promise<string>

读取有源标签内容，使用promise方式作为异步方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/wFZD_WrXRYCjNxOyTMVQRA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=B23FF83CD06A85C0DCD9B2380D69E628639798AABF216BF2D24D2EC0FE7A7E54)

从 API version 8 开始支持，从 API version 9 开始废弃，建议使用[connectedTag.read](#connectedtagread9)替代。

**需要权限**：ohos.permission.NFC\_TAG

**系统能力**：SystemCapability.Communication.ConnectedTag

**返回值：**

| **类型** | **说明** |
| :-- | :-- |
| Promise<string> | 返回读取有源标签内容。 |

**示例：**

```js
import { connectedTag } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

connectedTag.readNdefTag().then((data) => {
    console.info("connectedTag readNdefTag Promise data = " + data);
}).catch((err: BusinessError)=> {
    console.error("connectedTag readNdefTag Promise err: " + err);
});
```

#### connectedTag.read9+

read(): Promise<number\[\]>

读取有源标签内容，使用promise方式作为异步方法。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.ConnectedTag

**返回值：**

| **类型** | **说明** |
| :-- | :-- |
| Promise<number\[\]> | 返回读取有源标签内容。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[NFC错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-nfc)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 3200101 | Connected NFC tag running state is abnormal in service. |

**示例：**

```js
import { connectedTag } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

connectedTag.read().then((data) => {
    console.info("connectedTag read Promise data = " + data);
}).catch((err: BusinessError)=> {
    console.error("connectedTag read Promise err: " + err);
});
```

#### connectedTag.readNdefTag(deprecated)

readNdefTag(callback: AsyncCallback<string>): void

读取有源标签内容，使用AsyncCallback方式作为异步方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/cFBUZ2YhQTmDh6EaTAvQgA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=104B48531DE447B35BC8FB15F1189A718B43B2DCCE65AC3B03FA93D569EDF94A)

从 API version 8 开始支持，从 API version 9 开始废弃，建议使用[connectedTag.read](#connectedtagread9)替代。

**需要权限**：ohos.permission.NFC\_TAG

**系统能力**：SystemCapability.Communication.ConnectedTag

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<string> | 是 | 读取有源标签内容回调函数。 |

**示例：**

```js
import { connectedTag } from '@kit.ConnectivityKit';

connectedTag.readNdefTag((err, data)=> {
    if (err) {
        console.error("connectedTag readNdefTag AsyncCallback err: " + err);
    } else {
        console.info("connectedTag readNdefTag AsyncCallback data: " + data);
    }
});
```

#### connectedTag.read9+

read(callback: AsyncCallback<number\[\]>): void

读取有源标签内容，使用AsyncCallback方式作为异步方法。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.ConnectedTag

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number\[\]> | 是 | 读取有源标签内容回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[NFC错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-nfc)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 3200101 | Connected NFC tag running state is abnormal in service. |

**示例：**

```js
import { connectedTag } from '@kit.ConnectivityKit';

connectedTag.read((err, data)=> {
    if (err) {
        console.error("connectedTag read AsyncCallback err: " + err);
    } else {
        console.info("connectedTag read AsyncCallback data: " + data);
    }
});
```

#### connectedTag.writeNdefTag(deprecated)

writeNdefTag(data: string): Promise<void>

写入内容到有源标签，使用promise方式作为异步方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/yY3r_H8yRMCfEWUqbc4z_g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=6EC34FC3F1044DCC54778A2C61E72E763092C851BF3C59291367D4E774461B90)

从 API version 8 开始支持，从 API version 9 开始废弃，建议使用[connectedTag.write](#connectedtagwrite9)替代。

**需要权限**：ohos.permission.NFC\_TAG

**系统能力**：SystemCapability.Communication.ConnectedTag

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| :-- | :-- | :-- | :-- |
| data | string | 是 | 有源标签内容, 最大长度为1024个字节。 |

**返回值：**

| **类型** | **说明** |
| :-- | :-- |
| Promise<void> | 无返回值。 |

**示例：**

```js
import { connectedTag } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let rawData = "010203"; // change it to be correct.
connectedTag.writeNdefTag(rawData).then(() => {
    console.info("connectedTag.writeNdefTag Promise success.");
}).catch((err: BusinessError)=> {
    console.error("connectedTag.writeNdefTag Promise err: " + err);
});
```

#### connectedTag.write9+

write(data: number\[\]): Promise<void>

写入内容到有源标签，使用promise方式作为异步方法。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.ConnectedTag

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| :-- | :-- | :-- | :-- |
| data | number\[\] | 是 | 有源标签内容, 由十六进制数字组成。范围：0x00至0xFF。 |

**返回值：**

| **类型** | **说明** |
| :-- | :-- |
| Promise<void> | 无返回值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[NFC错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-nfc)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameters types.

3\. Parameter verification failed.

 |
| 801 | Capability not supported. |
| 3200101 | Connected NFC tag running state is abnormal in service. |

**示例：**

```js
import { connectedTag } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let rawData = [0x01, 0x02, 0x03]; // change it to be correct.
connectedTag.write(rawData).then(() => {
    console.info("connectedTag.writeNdefTag Promise success.");
}).catch((err: BusinessError)=> {
    console.error("connectedTag.writeNdefTag Promise err: " + err);
});
```

#### connectedTag.writeNdefTag(deprecated)

writeNdefTag(data: string, callback: AsyncCallback<void>): void

写入内容到有源标签，使用AsyncCallback方式作为异步方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/cfS6heToT6mCRK_M7iDOnw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014822Z&HW-CC-Expire=86400&HW-CC-Sign=361695B26336E08F07A45A27D6D333A84B99A4677913D602A01738B6146F5BCD)

从 API version 8 开始支持，从 API version 9 开始废弃，建议使用[connectedTag.write](#connectedtagwrite9)替代。

**需要权限**：ohos.permission.NFC\_TAG

**系统能力**：SystemCapability.Communication.ConnectedTag

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| :-- | :-- | :-- | :-- |
| data | string | 是 | 有源标签内容, 最大长度为1024个字节。 |
| callback | AsyncCallback<void> | 是 | 读取有源标签内容回调函数。 |

**示例：**

```js
import { connectedTag } from '@kit.ConnectivityKit';

let rawData = "010203"; // change it to be correct.
connectedTag.writeNdefTag(rawData, (err)=> {
    if (err) {
        console.error("connectedTag.writeNdefTag AsyncCallback err: " + err);
    } else {
        console.info("connectedTag.writeNdefTag AsyncCallback success.");
    }
});
```

#### connectedTag.write9+

write(data: number\[\], callback: AsyncCallback<void>): void

写入内容到有源标签，使用AsyncCallback方式作为异步方法。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.ConnectedTag

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| :-- | :-- | :-- | :-- |
| data | number\[\] | 是 | 有源标签内容, 由十六进制数字组成。范围：0x00至0xFF。 |
| callback | AsyncCallback<void> | 是 | 读取有源标签内容回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[NFC错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-nfc)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameters types.

3\. Parameter verification failed.

 |
| 801 | Capability not supported. |
| 3200101 | Connected NFC tag running state is abnormal in service. |

**示例：**

```js
import { connectedTag } from '@kit.ConnectivityKit';

let rawData = [0x01, 0x02, 0x03]; // change it to be correct.
connectedTag.write(rawData, (err)=> {
    if (err) {
        console.error("connectedTag.writeNdefTag AsyncCallback err: " + err);
    } else {
        console.info("connectedTag.writeNdefTag AsyncCallback success.");
    }
});
```

#### connectedTag.on('notify')

on(type: "notify", callback: Callback<number>): void

注册NFC场强状态事件。

**需要权限**：ohos.permission.NFC\_TAG

**系统能力**：SystemCapability.Communication.ConnectedTag

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 固定填"notify"字符串。 |
| callback | Callback<number> | 是 | 状态改变回调函数，返回值参见[NfcRfType](#nfcrftype)。 |

#### connectedTag.off('notify')

off(type: "notify", callback?: Callback<number>): void

取消NFC场强状态事件的注册。

**需要权限**：ohos.permission.NFC\_TAG

**系统能力**：SystemCapability.Communication.ConnectedTag

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 固定填"notify"字符串。 |
| callback | Callback<number> | 否 | 状态改变回调函数。如果callback不填，将“去注册”该事件关联的所有回调函数。 |

**示例：**

```js
import { connectedTag } from '@kit.ConnectivityKit';

function nfcStatusCb(rfState: connectedTag.NfcRfType) {
    console.info("connectedTag on Callback rfState: ", rfState);
}

// 有源nfc标签的使用流程
async function nfcTagTestOn(): Promise<void> {
    try {
        console.info("connectedTag initialize");
        connectedTag.initialize();
    } catch (error) {
        console.error("initialize error:" + error);
    }
    // 注册回调以接收nfc进离场状态更改通知
    connectedTag.on("notify", nfcStatusCb);
    try {
        let tag = [3, 1, 0];
        console.info("connectedTag write: tag=" + tag);
        await connectedTag.write(tag);
        let data = await connectedTag.read();
        console.info("connectedTag read: data=" + data);
    } catch (error) {
        console.error("connectedTag error: " + error);
    }
}

// 业务退出时，取消注册回调、取消初始化
async function nfcTagTestOff(): Promise<void> {
    // 取消注册回调
    connectedTag.off("notify", nfcStatusCb);
    try {
        console.info("connectedTag uninitialize");
        connectedTag.uninitialize();
    } catch (error) {
        console.error("connectedTag error: " + error);
    }
}

export { nfcTagTestOn, nfcTagTestOff }
```

#### NfcRfType

表示NFC场强状态的枚举。

**系统能力**：SystemCapability.Communication.ConnectedTag

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| NFC\_RF\_LEAVE | 0 | NFC离场事件。 |
| NFC\_RF\_ENTER | 1 | NFC进场事件。 |

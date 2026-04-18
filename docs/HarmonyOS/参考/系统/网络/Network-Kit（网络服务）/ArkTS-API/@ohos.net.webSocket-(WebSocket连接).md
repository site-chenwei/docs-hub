---
title: "@ohos.net.webSocket (WebSocket连接)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-websocket"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Network Kit（网络服务）"
  - "ArkTS API"
  - "@ohos.net.webSocket (WebSocket连接)"
captured_at: "2026-04-17T01:48:22.849Z"
---

# @ohos.net.webSocket (WebSocket连接)

给第三方应用提供webSocket客户端和服务端服务器，实现客户端与服务端的双向连接。

客户端：使用WebSocket建立服务器与客户端的双向连接，需要先通过[createWebSocket](#websocketcreatewebsocket)方法创建[WebSocket](#websocket)对象，然后通过[connect](#connect)方法连接到服务器。当连接成功后，客户端会收到[open](#onopen)事件的回调，之后客户端就可以通过[send](#send)方法与服务器进行通信。当服务器发信息给客户端时，客户端会收到[message](#onmessage)事件的回调。当客户端想要取消此连接时，通过调用[close](#close)方法主动断开连接后，客户端会收到[close](#onclose)事件的回调。若在上述任一过程中发生错误，客户端会收到[error](#onerror)事件的回调。

服务端：（从API version 23开始支持全设备使用，之前仅支持TV设备使用）使用WebSocket建立服务器与客户端的双向连接，需要先通过[createWebSocketServer](#websocketcreatewebsocketserver19)方法创建[WebSocketServer](#websocketserver19)对象，然后通过[start](#start19)方法启动服务器，监听客户端的申请建链的消息。当连接成功后，服务端会收到[connect](#onconnect19)事件的回调，之后服务端可以通过[send](#send19)方法与客户端进行通信，或者通过[listAllConnections](#listallconnections19)方法列举出当前与服务端建链的所有客户端信息。当客户端给服务端发消息时，服务端会收到[messageReceive](#onmessagereceive19)事件回调。当服务端想断开与某个客户端的连接时，可以通过调用[close](#close19)方法主动断开与某个客户端的连接，之后服务端会收到[close](#onclose19)事件的回调。当服务端想停止service时，可以调用[stop](#stop19)方法。若在上述任一过程中发生错误，服务端会收到[error](#onerror19)事件的回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/Xi5iVPGVRWiqeJmgLbp2bQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=0E29AD456A2A3CC37E16E15F59BEF1499C417718B75C1E0267AF77E4C0BD4432)

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import { webSocket } from '@kit.NetworkKit';
```

#### webSocket.createWebSocket

createWebSocket(): WebSocket

创建一个WebSocket对象，里面包括建立连接、关闭连接、发送数据和订阅/取消订阅WebSocket连接的打开事件、接收到服务器消息事件、关闭事件和错误事件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [WebSocket](#websocket) | 返回一个WebSocket对象，里面包括connect、send、close、on和off方法。 |

**示例：**

```ts
let ws: webSocket.WebSocket = webSocket.createWebSocket();
```

#### WebSocket

在调用WebSocket的方法前，需要先通过[webSocket.createWebSocket](#websocketcreatewebsocket)创建一个WebSocket。

#### \[h2\]connect

connect(url: string, callback: AsyncCallback<boolean>): void

根据URL地址，建立一个WebSocket连接，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/BuIHqwjhSZ6YZDDexYgN3g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=9317CFAF2F2B195DA64716429ED19274BF2468C79D00C56BC19943710B2F28CA)

callback中返回的boolean值仅表示连接请求创建是否成功。如需感知WebSocket是否连接成功，需要在调用该接口前调用[on('open')](#onopen)订阅open事件。

**需要权限**：ohos.permission.INTERNET

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/XMmSyLp9R8Wg_s0YsqUqRA/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=F04331241C4E5D68D17B01FB96A5CA419BB0697B2E0BFAC15C4ADE4778AA7ADE)

URL地址长度不能超过1024个字符，否则会连接失败。从API version 15开始，URL地址长度限制由1024修改为2048。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| url | string | 是 | 建立WebSocket连接的URL地址。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。true:连接请求创建成功；false:连接请求创建失败。 |

**错误码：**

以下错误码的详细介绍参见[webSocket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-websocket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2302001 | Websocket url error. |
| 2302002 | Websocket certificate file does not exist. |
| 2302003 | Websocket connection already exists. |
| 2302998 | It is not allowed to access this domain. |
| 2302999 | Internal error. |

**示例：**

```ts
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();
let url = "ws://";
ws.connect(url, (err: BusinessError, value: boolean) => {
  if (!err) {
    console.info("connect success")
  } else {
    console.error(`connect fail. Code: ${err.code}, message: ${err.message}`)
  }
});
```

#### \[h2\]connect

connect(url: string, options: WebSocketRequestOptions, callback: AsyncCallback<boolean>): void

根据URL地址，建立一个WebSocket连接，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/1doSqxlrTqK7_SIk0PCq8g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=F3BDA466E967EC60E2044815767D600F993A55CF2727913451EA67C88DDB2A71)

callback中返回的boolean值仅表示连接请求创建是否成功。如需感知WebSocket是否连接成功，需要在调用该接口前调用[on('open')](#onopen)订阅open事件。

**需要权限**：ohos.permission.INTERNET

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/aJc8rj2MRqq1LluFnC9e4A/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=F5CA294482748A129C9B823EA8D6DA25CCDAA5F5FDCF4BF6F7C081F512EE910A)

URL地址长度不能超过1024个字符，否则会连接失败。从API version 15开始，URL地址长度限制由1024修改为2048。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| url | string | 是 | 建立WebSocket连接的URL地址。 |
| options | WebSocketRequestOptions | 是 | 参考[WebSocketRequestOptions](#websocketrequestoptions)。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。true:连接请求创建成功；false:连接请求创建失败。 |

**错误码：**

以下错误码的详细介绍参见[webSocket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-websocket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2302001 | Websocket url error. |
| 2302002 | Websocket certificate file does not exist. |
| 2302003 | Websocket connection already exists. |
| 2302998 | It is not allowed to access this domain. |
| 2302999 | Internal error. |

**示例：**

```ts
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();
let options: webSocket.WebSocketRequestOptions | undefined;
if (options !=undefined) {
  options.header = {
     name1: "value1",
     name2: "value2",
     name3: "value3"
  };
  options.caPath = "";
}
let url = "ws://"
ws.connect(url, options, (err: BusinessError, value: Object) => {
  if (!err) {
    console.info("connect success")
  } else {
    console.error(`connect fail. Code: ${err.code}, message: ${err.message}`)
  }
});
```

#### \[h2\]connect

connect(url: string, options?: WebSocketRequestOptions): Promise<boolean>

根据URL地址和header，建立一个WebSocket连接。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/EW04giSjRZ20tR4pmNO4xQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=E604AEA2CA731C424347D2611E3DA5194B3DEC5A440588C642BAEB7D31629CE5)

callback中返回的boolean值仅表示连接请求创建是否成功。如需感知WebSocket是否连接成功，需要在调用该接口前调用[on('open')](#onopen)订阅open事件。

**需要权限**：ohos.permission.INTERNET

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/dCTTCo12S3eaKsiqg-JsHw/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=F488C9114A676106BDD555ADB1734303837CE15790970081BDBA8B4188960864)

URL地址长度不能超过1024个字符，否则会连接失败。从API version 15开始，URL地址长度限制由1024修改为2048。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| url | string | 是 | 建立WebSocket连接的URL地址。 |
| options | WebSocketRequestOptions | 否 | 参考[WebSocketRequestOptions](#websocketrequestoptions)。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | 回调函数。true:连接请求创建成功；false:连接请求创建失败。 |

**错误码：**

以下错误码的详细介绍参见[webSocket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-websocket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2302001 | Websocket url error. |
| 2302002 | Websocket certificate file does not exist. |
| 2302003 | Websocket connection already exists. |
| 2302998 | It is not allowed to access this domain. |
| 2302999 | Internal error. |

**示例：**

```ts
import { webSocket } from '@kit.NetworkKit';

let ws = webSocket.createWebSocket();
let url = "ws://"
let promise = ws.connect(url);
promise.then((value: boolean) => {
  console.info("connect success")
}).catch((err:string) => {
  console.error("connect fail, error:" + JSON.stringify(err))
});
```

#### \[h2\]send

send(data: string | ArrayBuffer, callback: AsyncCallback<boolean>): void

通过WebSocket连接发送数据，使用callback异步回调。

**需要权限**：ohos.permission.INTERNET

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| data | string | ArrayBuffer | 是 | 
发送的数据。

API 6及更早版本仅支持string类型。API 8起同时支持string和ArrayBuffer类型。最大支持发送5242864字节数据(即5 \* 1024 \* 1024 - 16)，超过该大小会返回401错误码。

 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。true:发送请求创建成功；false:发送请求创建失败。 |

**错误码：**

以下错误码的详细介绍参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**示例：**

```ts
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();
let url = "ws://"
class OutValue {
  status: number = 0
  message: string = ""
}
ws.connect(url, (err: BusinessError, value: boolean) => {
    if (!err) {
      console.info("connect success")
    } else {
      console.error(`connect fail. Code: ${err.code}, message: ${err.message}`)
    }
});
ws.on('open', (err: BusinessError, value: Object) => {
  console.info("on open, status:" + (value as OutValue).status + ", message:" + (value as OutValue).message)
    ws.send("Hello, server!", (err: BusinessError, value: boolean) => {
    if (!err) {
      console.info("send success")
    } else {
      console.error(`send fail. Code: ${err.code}, message: ${err.message}`)
    }
  });
});
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/OyPU9znoT-KOoiY_bNHheA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=A1C7DE404336C5B44F6D3D42228F81614D52EEF8E3E99DAE87665D52FACFC92C)

send接口必须在监听到open事件后才可以调用。

#### \[h2\]send

send(data: string | ArrayBuffer): Promise<boolean>

通过WebSocket连接发送数据。使用Promise异步回调。

**需要权限**：ohos.permission.INTERNET

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| data | string | ArrayBuffer | 是 | 
发送的数据。

API 6及更早版本仅支持string类型。API 8起同时支持string和ArrayBuffer类型。最大支持发送5242864字节数据(即5 \* 1024 \* 1024 - 16)，超过该大小会返回401错误码。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | 以Promise形式返回发送数据的结果。true:发送请求创建成功；false:发送请求创建失败。 |

**错误码：**

以下错误码的详细介绍参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**示例：**

```ts
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();
let url = "ws://"
class OutValue {
  status: number = 0
  message: string = ""
}
ws.connect(url, (err: BusinessError, value: boolean) => {
    if (!err) {
      console.info("connect success")
    } else {
      console.error("connect fail. Code: ${err.code}, message: ${err.message}")
    }
});

ws.on('open', (err: BusinessError, value: Object) => {
  console.info("on open, status:" + (value as OutValue).status + ", message:" + (value as OutValue).message)
  let promise = ws.send("Hello, server!");
  promise.then((value: boolean) => {
    console.info("send success")
  }).catch((err:string) => {
    console.error("send fail, error:" + JSON.stringify(err))
  });
});
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/yTQ0dEI7QrWK0uN4o2oTgw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=859A53FB2DD725FDF0DE1E7F2EF43B440A4C0C369361A7EB21DA7403B2B5FF4E)

send接口必须在监听到open事件后才可以调用。

#### \[h2\]close

close(callback: AsyncCallback<boolean>): void

关闭WebSocket连接，使用callback异步回调。

**需要权限**：ohos.permission.INTERNET

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。true:关闭请求创建成功；false:关闭请求创建失败。 |

**错误码：**

以下错误码的详细介绍参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**示例：**

```ts
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();
ws.close((err: BusinessError) => {
  if (!err) {
    console.info("close success")
  } else {
    console.error(`close fail. Code: ${err.code}, message: ${err.message}`)
  }
});
```

#### \[h2\]close

close(options: WebSocketCloseOptions, callback: AsyncCallback<boolean>): void

根据参数options，关闭WebSocket连接，使用callback异步回调。

**需要权限**：ohos.permission.INTERNET

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | WebSocketCloseOptions | 是 | 参考[WebSocketCloseOptions](#websocketcloseoptions)。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。true:关闭请求创建成功；false:关闭请求创建失败。 |

**错误码：**

以下错误码的详细介绍参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**示例：**

```ts
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();

let options: webSocket.WebSocketCloseOptions | undefined;
if (options != undefined) {
    options.code = 1000
    options.reason = "your reason"
}
ws.close(options, (err: BusinessError) => {
    if (!err) {
        console.info("close success")
    } else {
        console.error(`close fail. Code: ${err.code}, message: ${err.message}`)
    }
});
```

#### \[h2\]close

close(options?: WebSocketCloseOptions): Promise<boolean>

根据可选参数code和reason，关闭WebSocket连接。使用Promise异步回调。

**需要权限**：ohos.permission.INTERNET

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | WebSocketCloseOptions | 否 | 参考[WebSocketCloseOptions](#websocketcloseoptions)。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | 以Promise形式返回关闭连接的结果。true:关闭请求创建成功；false:关闭请求创建失败。 |

**错误码：**

以下错误码的详细介绍参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**示例：**

```ts
import { webSocket } from '@kit.NetworkKit';

let ws = webSocket.createWebSocket();
let options: webSocket.WebSocketCloseOptions | undefined;
if (options != undefined) {
    options.code = 1000
    options.reason = "your reason"
}
let promise = ws.close();
promise.then((value: boolean) => {
    console.info("close success")
}).catch((err:string) => {
    console.error("close fail, error:" + JSON.stringify(err))
});
```

#### \[h2\]on('open')

on(type: 'open', callback: AsyncCallback<Object>): void

订阅WebSocket的打开事件，使用callback异步回调。该事件用于指示WebSocket是否连接成功。该接口需要在调用[connect](#connect)发起连接请求前调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅的事件类型。'open'：WebSocket的打开事件。 |
| callback | AsyncCallback<Object> | 是 | 回调函数。 |

**示例：**

```ts
import { webSocket } from '@kit.NetworkKit';
import { BusinessError, Callback } from '@kit.BasicServicesKit';

let ws= webSocket.createWebSocket();
class OutValue {
  status: number = 0
  message: string = ""
}
ws.on('open', (err: BusinessError, value: Object) => {
  console.info("on open, status:" + (value as OutValue).status + ", message:" + (value as OutValue).message)
});
```

#### \[h2\]off('open')

off(type: 'open', callback?: AsyncCallback<Object>): void

取消订阅WebSocket的打开事件，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/520DCj4PTkGrq0krfJfGbA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=225E592DA5D85CA9FD925909E845F93F7404E757F73532E648B719D953D9A214)

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 取消订阅的事件类型。'open'：WebSocket的打开事件。 |
| callback | AsyncCallback<Object> | 否 | 回调函数。 |

**示例：**

```ts
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();
class OutValue {
  status: number = 0
  message: string = ""
}
let callback1 = (err: BusinessError, value: Object) => {
 console.info("on open, status:" + ((value as OutValue).status + ", message:" + (value as OutValue).message))
}
ws.on('open', callback1);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
ws.off('open', callback1);
```

#### \[h2\]on('message')

on(type: 'message', callback: AsyncCallback<string | ArrayBuffer>): void

订阅WebSocket的接收服务器消息事件，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/QC62n_bKSlKdFXvgJLPLFg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=AA17125D87DF7B0BC1F2AADD5D6C500BC8FB5C0C45A773067E0B146D4B66D881)

AsyncCallback中的数据可以是字符串（API version 6开始支持）或ArrayBuffer（API version 8开始支持）。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅的事件类型。'message'：WebSocket的接收服务器消息事件。 |
| callback | AsyncCallback<string | ArrayBuffer 8+\> | 是 | 回调函数。 |

**示例：**

```ts
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();
ws.on('message', (err: BusinessError<void>, value: string | ArrayBuffer) => {
  console.info("on message, message:" + value)
});
```

#### \[h2\]off('message')

off(type: 'message', callback?: AsyncCallback<string | ArrayBuffer>): void

取消订阅WebSocket的接收服务器消息事件，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/hPIpZhGFRNaGSMhVy8ar7A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=3B84BEA810B8CEB7EA9E2B7FA36EE3028316D6B06D611A564289CF6B23A6DFF9)

AsyncCallback中的数据可以是字符串(API 6)或ArrayBuffer(API 8)。

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 取消订阅的事件类型。'message'：WebSocket的接收到服务器消息事件。 |
| callback | AsyncCallback<string |ArrayBuffer 8+\> | 否 | 回调函数。 |

**示例：**

```ts
import { webSocket } from '@kit.NetworkKit';

let ws = webSocket.createWebSocket();
ws.off('message');
```

#### \[h2\]on('close')

on(type: 'close', callback: AsyncCallback<CloseResult>): void

订阅WebSocket的关闭事件，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅的事件类型。'close'：WebSocket的关闭事件。 |
| callback | AsyncCallback<CloseResult> | 是 | 
回调函数。

close：close错误码，reason：错误码说明

 |

**示例：**

```ts
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();
ws.on('close', (err: BusinessError, value: webSocket.CloseResult) => {
  console.info("on close, code is " + value.code + ", reason is " + value.reason)
});
```

#### \[h2\]off('close')

off(type: 'close', callback?: AsyncCallback<CloseResult>): void

取消订阅WebSocket的关闭事件，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/BO8_ge2AQbG5Q4NVWVbrAQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=3A677BFFDE15E9EE45D6A704191FEA3FA986836D3A23C70E63EE85795BEBD292)

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 取消订阅的事件类型。'close'：WebSocket的关闭事件。 |
| callback | AsyncCallback<CloseResult> | 否 | 
回调函数。

close：close错误码，reason：错误码说明

 |

**示例：**

```ts
import { webSocket } from '@kit.NetworkKit';

let ws = webSocket.createWebSocket();
ws.off('close');
```

#### \[h2\]on('error')

on(type: 'error', callback: ErrorCallback): void

订阅WebSocket的Error事件，使用callback异步回调。

关于[error](#onerror)事件回调的错误码说明：WebSocket的本质是HTTP协议升级，若服务器同意升级，服务器会返回101。状态码表示协议从HTTP切换为WebSocket协议（触发open回调），而如果服务器拒绝了升级或出现其他异常，则返回200，表示服务器只是将请求当作普通的HTTP请求来处理。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅的事件类型。'error'：WebSocket的Error事件。 |
| callback | ErrorCallback | 是 | 回调函数。 |

**示例：**

```ts
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ws = webSocket.createWebSocket();
ws.on('error', (err: BusinessError) => {
  console.error(`on error. Code: ${err.code}, message: ${err.message}`)
});
```

#### \[h2\]off('error')

off(type: 'error', callback?: ErrorCallback): void

取消订阅WebSocket的Error事件，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/9QMNhgcVSauH5hPLuczgLQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=C9D787AF429BC19F2B55F92566F706D75B7B0CA1A6AFC2C347A9D54A650FAF7A)

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 取消订阅的事件类型。'error'：WebSocket的Error事件。 |
| callback | ErrorCallback | 否 | 回调函数。 |

**示例：**

```ts
import { webSocket } from '@kit.NetworkKit';

let ws = webSocket.createWebSocket();
ws.off('error');
```

#### \[h2\]on('dataEnd')11+

on(type: 'dataEnd', callback: Callback<void>): void

订阅WebSocket的数据接收结束事件，使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅的事件类型。'dataEnd'：WebSocket的数据接收结束事件。 |
| callback | Callback<void> | 是 | 回调函数。 |

**示例：**

```ts
import { webSocket } from '@kit.NetworkKit';

let ws = webSocket.createWebSocket();
ws.on('dataEnd', () => {
  console.info("on dataEnd")
});
```

#### \[h2\]off('dataEnd')11+

off(type: 'dataEnd', callback?: Callback<void>): void

取消订阅WebSocket的数据接收结束事件，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/Jp-h-I8SSJaSKhcqLXB6Ag/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=D999578666EE2C928C553941184039E7F87C21C2188663F20636D2232350DD68)

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 取消订阅的事件类型。'dataEnd'：WebSocket的数据接收结束事件。 |
| callback | Callback<void> | 否 | 回调函数。 |

**示例：**

```ts
import { webSocket } from '@kit.NetworkKit';

let ws = webSocket.createWebSocket();
ws.off('dataEnd');
```

#### \[h2\]on('headerReceive')12+

on(type: 'headerReceive', callback: Callback<ResponseHeaders>): void

订阅HTTP Response Header事件，使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅的事件类型。'headerReceive'：WebSocket的headerReceive事件。 |
| callback | Callback<ResponseHeaders> | 是 | 回调函数，返回订阅事件。 |

**示例：**

```ts
import { webSocket } from '@kit.NetworkKit';

let ws = webSocket.createWebSocket();
ws.on('headerReceive', (data) => {
  console.info("on headerReceive " + JSON.stringify(data))
});
```

#### \[h2\]off('headerReceive')12+

off(type: 'headerReceive', callback?: Callback<ResponseHeaders>): void

取消订阅HTTP Response Header事件，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/D5PcVK9LTJy5gDhaQTt1zA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=DBA6CB277B9197C65D33ECB1D1FCAD086ED5DE63A74FD74FBFDF976FE26CCBB5)

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 取消订阅的事件类型。'headerReceive'：WebSocket的headerReceive事件。 |
| callback | Callback<ResponseHeaders> | 否 | 回调函数，返回订阅事件。 |

**示例：**

```ts
import { webSocket } from '@kit.NetworkKit';

let ws = webSocket.createWebSocket();
ws.off('headerReceive');
```

#### webSocket.createWebSocketServer19+

createWebSocketServer(): WebSocketServer

创建一个WebSocketServer对象，包括启动服务、发送数据、关闭连接、列出客户端信息、停止服务，订阅/取消订阅webSocket连接的连接事件、接收到客户端消息事件、关闭事件和错误事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/dmCf91HhRO2GUTauJS-kyQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=590337B88A695E7B2D6384D731A2170B5B0F7AE54A96943745A387E15A9AD625)

从API version 23开始支持全设备使用，之前仅支持TV设备使用。

**系统能力**: SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [WebSocketServer](#websocketserver19) | 返回一个WebSocketServer对象，里面包括start、listAllConnections、send、close、stop、on和off方法。 |

**示例：**

```ts
let ws: webSocket.WebSocketServer = webSocket.createWebSocketServer();
```

#### WebSocketServer19+

在调用WebSocketServer方法前，需要先通过[webSocket.createWebSocketServer](#websocketcreatewebsocketserver19)创建一个WebSocketServer。

#### \[h2\]start19+

start(config: WebSocketServerConfig): Promise<boolean>

配置config参数，启动服务端service。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/O1mIwOjATw6RdZ4XdrgZaA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=A791C6B5B363FFF2BD6B09DA78E079F0CB932ED2F2533BBD5CD91CEEBB58BFF9)

在多次调用该接口时，应避免监听同一端口。

**需要权限**: ohos.permission.INTERNET

**系统能力**: SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| config | [WebSocketServerConfig](#websocketserverconfig19) | 是 | 启动websocketServer服务器。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | promise对象。返回true表示服务器启动成功；返回false表示服务启动失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[webSocket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-websocket)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 2302002 | Websocket certificate file does not exist. |
| 2302004 | Can't listen on the given NIC. |
| 2302005 | Can't listen on the given Port. |
| 2302999 | Websocket other unknown error. |

**示例：**

```ts
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let localServer: webSocket.WebSocketServer;
let config: webSocket.WebSocketServerConfig = {
  serverPort: 8080, // 监听端口
  maxConcurrentClientsNumber: 10,
  maxConnectionsForOneClient: 10,
}

localServer = webSocket.createWebSocketServer();
localServer.start(config).then((success: boolean) => {
  if (success) {
    console.info('webSocket server start success');
  } else {
    console.error('websocket server start failed');
  }
}).catch((error: BusinessError) => {
  console.error(`Failed to start. Code: ${error.code}, message: ${error.message}`);
});
```

#### \[h2\]send19+

send(data: string | ArrayBuffer, connection: WebSocketConnection): Promise<boolean>

通过WebSocket连接发送数据。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/fhRidnUpQLa8ilCNzKzWwg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=271695A8C8013303C3ED5C71E493D1567C25B507D092C4492B559933BDA5CB23)

send接口必须在监听到connect事件后才可以调用。

**需要权限**: ohos.permission.INTERNET

**系统能力**: SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| data | string | ArrayBuffer | 是 | 服务端发送消息的数据，同时支持string（字符串）和ArrayBuffer（二进制）类型。最大支持发送5242864字节数据(即5 \* 1024 \* 1024 - 16)，超过该大小会返回401错误码。 |
| connection | [WebSocketConnection](#websocketconnection19) | 是 | 发送的客户端信息。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | promise对象。返回true表示发送请求创建成功；返回false表示发送请求创建失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[webSocket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-websocket)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 2302006 | websocket connection does not exist. |

**示例：**

```ts
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let localServer: webSocket.WebSocketServer;
let config: webSocket.WebSocketServerConfig = {
  serverPort: 8080, // 监听端口
  maxConcurrentClientsNumber: 10,
  maxConnectionsForOneClient: 10,
}

localServer = webSocket.createWebSocketServer();
localServer.start(config).then((success: boolean) => {
  if (success) {
    console.info('webSocket server start success');
  } else {
    console.error('websocket server start failed');
  }
}).catch((error: BusinessError) => {
  console.error(`Failed to start. Code: ${error.code}, message: ${error.message}`);
});

localServer.on('connect', async (connection: webSocket.WebSocketConnection) => {
  console.info(`New client connected! Client ip: ${connection.clientIP}, Client port: ${connection.clientPort}`);
  // 当收到on('connect')事件时，可以通过send()方法与客户端进行通信
  localServer.send("Hello, I'm server!", connection).then((success: boolean) => {
    if (success) {
      console.info('message send successfully');
    } else {
      console.error('message send failed');
    }
  }).catch((error: BusinessError) => {
    console.error(`message send failed, Code: ${error.code}, message: ${error.message}`);
  });
});
```

#### \[h2\]listAllConnections19+

listAllConnections(): WebSocketConnection\[\]

获取与服务端连接的所有客户端信息。

**需要权限**: ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/LPxOAuwrR9C8re9-Mp0-LQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=3771A5D9167DEF3F36E65E97122496A4B68843169C46B8CEA3D66F44FE8F408B)

该接口为异步调用，返回结果需通过await关键字等待异步操作完成，以确保正确获取到所有客户端连接信息。

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [WebSocketConnection\[\]](#websocketconnection19) | 以字符串数组形式返回所有客户端的信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |

**示例：**

```ts
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let connections: webSocket.WebSocketConnection[] = [];
let localServer: webSocket.WebSocketServer;
let config: webSocket.WebSocketServerConfig = {
  serverPort: 8080, // 监听端口
  maxConcurrentClientsNumber: 10,
  maxConnectionsForOneClient: 10,
}

localServer = webSocket.createWebSocketServer();
localServer.start(config).then((success: boolean) => {
  if (success) {
    console.info('webSocket server start success');
  } else {
    console.error('websocket server start failed');
  }
}).catch((error: BusinessError) => {
  console.error(`Failed to start. Code: ${error.code}, message: ${error.message}`);
});

localServer.on('connect', async (connection: webSocket.WebSocketConnection) => {
  console.info(`New client connected! Client ip: ${connection.clientIP}, Client port: ${connection.clientPort}`);
  try {
    connections = await localServer.listAllConnections();
    if (connections.length === 0) {
      console.info('client list is empty');
    } else {
      console.info(`client list cnt: ${connections.length}, client connections list is: ${connections}`);
    }
  } catch (error) {
    console.error(`Failed to listAllConnections. Code: ${error.code}, message: ${error.message}`);
  }
});
```

#### \[h2\]close19+

close(connection: WebSocketConnection, options?: webSocket.WebSocketCloseOptions): Promise<boolean>

关闭指定websocket连接。使用Promise异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| connection | [WebSocketConnection](#websocketconnection19) | 是 | 客户端信息，包括客户端的ip地址和端口号port。 |
| options | [webSocket.WebSocketCloseOptions](#websocketcloseoptions) | 否 | 
关闭WebSocket连接时，可选参数的类型和说明。

\- 错误码默认：200。原因值默认：Websocket connect failed。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | promise对象。返回true表示关闭请求创建成功；返回false表示关闭请求创建失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[webSocket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-websocket)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 2302006 | websocket connection does not exist. |

**示例：**

```ts
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let localServer: webSocket.WebSocketServer;
let config: webSocket.WebSocketServerConfig = {
  serverPort: 8080, // 监听端口
  maxConcurrentClientsNumber: 10,
  maxConnectionsForOneClient: 10,
}

localServer = webSocket.createWebSocketServer();
localServer.start(config).then((success: boolean) => {
  if (success) {
    console.info('webSocket server start success');
  } else {
    console.error('websocket server start failed');
  }
}).catch((error: BusinessError) => {
  console.error(`Failed to start. Code: ${error.code}, message: ${error.message}`);
});

localServer.on('connect', (connection: webSocket.WebSocketConnection) => {
  console.info(`New client connected! Client ip: ${connection.clientIP}, Client port: ${connection.clientPort}`);
  localServer.close(connection).then((success: boolean) => {
    if (success) {
      console.info('close client successfully');
    } else {
      console.error('close client failed');
    }
  });
});
```

#### \[h2\]stop19+

stop(): Promise<boolean>

停止服务端服务。使用Promise异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | promise对象。返回true表示停止服务端service请求创建成功；返回false表示停止服务端service请求创建失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |

**示例：**

```ts
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let localServer: webSocket.WebSocketServer;
let config: webSocket.WebSocketServerConfig = {
  serverPort: 8080, // 监听端口
  maxConcurrentClientsNumber: 10,
  maxConnectionsForOneClient: 10,
}

localServer = webSocket.createWebSocketServer();
localServer.start(config).then((success: boolean) => {
  if (success) {
    console.info('webSocket server start success');
  } else {
    console.error('websocket server start failed');
  }
}).catch((error: BusinessError) => {
  console.error(`Failed to start. Code: ${error.code}, message: ${error.message}`);
});

localServer.stop().then((success: boolean) => {
  if (success) {
    console.info('server stop service successfully');
  } else {
    console.error('server stop service failed');
  }
});
```

#### \[h2\]on('connect')19+

on(type: 'connect', callback: Callback<WebSocketConnection>): void

订阅WebSocketServer的连接事件（客户端与服务端建链成功），使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 事件回调类型，支持的事件为'connect'，当onconnect()调用完成，客户端与服务端建链成功。 |
| callback | Callback<[WebSocketConnection](#websocketconnection19)\> | 是 | 回调函数。连接的客户端信息。 |

**示例：**

```ts
import { webSocket } from '@kit.NetworkKit';
import { BusinessError, Callback } from '@kit.BasicServicesKit';

let localServer = webSocket.createWebSocketServer();
localServer.on('connect', (connection: webSocket.WebSocketConnection) => {
  console.info(`New client connected! Client ip: ${connection.clientIP}, Client port: ${connection.clientPort}`);
});
```

#### \[h2\]off('connect')19+

off(type: 'connect', callback?: Callback<WebSocketConnection>): void

取消订阅WebSocketServer的连接事件（客户端与服务端建链成功），使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/VOlQ8mHCSTqGdEYQkpzJjg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=9F3D4E1678F7465EE9C9B179C9BC4B3B86457C198A7E3E7A3DFB845B3D322351)

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 事件回调类型，支持的事件为'connect'，当offconnect()调用完成，取消监听连接事件成功。 |
| callback | Callback<[WebSocketConnection](#websocketconnection19)\> | 否 | 回调函数。连接的客户端信息。 |

**示例：**

```ts
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let localServer = webSocket.createWebSocketServer();
localServer.off('connect');
```

#### \[h2\]on('messageReceive')19+

on(type: 'messageReceive', callback: Callback<WebSocketMessage>): void

订阅WebSocketServer的接收客户端消息的事件，使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 事件回调类型，支持的事件为'messageReceive'，当onmessageReceive()调用完成，接收到客户端消息成功。 |
| callback | Callback<[WebSocketMessage](#websocketmessage19)\> | 是 | 
回调函数。

clientconnection:客户端信息，data:客户端发送的数据消息。

 |

**示例：**

```ts
import { webSocket } from '@kit.NetworkKit';
import { BusinessError, Callback } from '@kit.BasicServicesKit';

let localServer = webSocket.createWebSocketServer();
localServer.on('messageReceive', (message: webSocket.WebSocketMessage) => {
  console.info(`on message received, client: ${message.clientConnection}, data: ${message.data}`);
});
```

#### \[h2\]off('messageReceive')19+

off(type: 'messageReceive', callback?: Callback<WebSocketMessage>): void

取消订阅WebSocketServer的接收到客户端消息事件，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/ao5b8V8IQ2S8_zYaM4HJhQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=813E3873FE17B9961A990AB6C33999687686EE1BFA9A58F4F7BCD36DCC96DF05)

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 事件回调类型，支持的事件为'messageReceive'，当offmessageReceive()调用完成，取消订阅接收客户端消息成功。 |
| callback | Callback<[WebSocketMessage](#websocketmessage19)\> | 否 | 
从指定客户端接收到的消息，包括客户端的信息和数据。

\- clientconnection：客户端信息。

\- data：客户端发送的消息。

 |

**示例：**

```ts
import { webSocket } from '@kit.NetworkKit';
import { BusinessError, Callback } from '@kit.BasicServicesKit';

let localServer = webSocket.createWebSocketServer();
localServer.off('messageReceive');
```

#### \[h2\]on('close')19+

on(type: 'close', callback: ClientConnectionCloseCallback): void

订阅WebSocketServer的关闭事件，使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 事件回调类型，支持的事件为'close'，当onclose()调用完成，连接关闭成功。 |
| callback | [ClientConnectionCloseCallback](#clientconnectionclosecallback19) | 是 | 
回调函数。

close：close错误码；reason：错误码说明。

 |

**示例：**

```ts
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let localServer = webSocket.createWebSocketServer();
localServer.on('close', (clientConnection: webSocket.WebSocketConnection, closeReason: webSocket.CloseResult) => {
  console.info(`client close, client: ${clientConnection}, closeReason: Code: ${closeReason.code}, reason: ${closeReason.reason}`);
});
```

#### \[h2\]off('close')19+

off(type: 'close', callback?: ClientConnectionCloseCallback): void

取消订阅WebSocketServer的关闭事件，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/rdm2oCnyTYCBiKkEFbdWLA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=70B8C4C65CBDE13E26FCCFEA290B61D691A5534F8965582CCE5A7B8CBB1D408C)

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 事件回调类型，支持的事件为'close'，当offclose()调用完成，取消订阅连接关闭事件成功。 |
| callback | [ClientConnectionCloseCallback](#clientconnectionclosecallback19) | 否 | 
回调函数。

close：close错误码；reason：错误码说明。

 |

**示例：**

```ts
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let localServer = webSocket.createWebSocketServer();
localServer.off('close');
```

#### \[h2\]on('error')19+

on(type: 'error', callback: ErrorCallback): void

订阅WebSocketServer的Error事件，使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 事件回调类型，支持的事件为'error'，当onerror()调用完成，error事件发生。 |
| callback | [ErrorCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-base#errorcallback) | 是 | 回调函数。 |

**示例：**

```ts
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wsServer: webSocket.WebSocketServer = webSocket.createWebSocketServer();
wsServer.on('error', (err: BusinessError) => {
  console.error(`error. Code: ${err.code}, message: ${err.message}`);
});
```

#### \[h2\]off('error')19+

off(type: 'error', callback?: ErrorCallback): void

取消订阅WebSocketServer的Error事件，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/w3XqyZO-RmWBJJ-XooDMoQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=BED5FDDAEC888F6A451EAFDAE87E9BA6F712820F33D9C2503F201CD49868666C)

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 事件回调类型，支持的事件为'error'，当offerror()调用完成，取消订阅error事件成功。 |
| callback | [ErrorCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-base#errorcallback) | 否 | 回调函数。默认值：200。 |

**示例：**

```ts
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let localServer = webSocket.createWebSocketServer();
localServer.off('error');
```

#### WebSocketRequestOptions

建立WebSocket连接时，可选参数的类型和说明。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| header | Object | 否 | 是 | 
建立WebSocket连接可选参数，代表建立连接时携带的HTTP头信息。参数内容自定义，也可以不指定。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| caPath11+ | string | 否 | 是 | 如果设置了此参数，系统将使用用户指定路径的CA证书，(开发者需保证该路径下CA证书的可访问性)，否则将使用系统预设CA证书，系统预设CA证书位置：/etc/ssl/certs/cacert.pem。证书路径为沙箱映射路径（开发者可通过UIAbilityContext提供的能力获取应用沙箱路径）。目前仅支持格式为pem的文本证书。 |
| clientCert11+ | [ClientCert](#clientcert11) | 否 | 是 | 支持传输客户端证书。 |
| proxy12+ | [ProxyConfiguration](#proxyconfiguration12) | 否 | 是 | 通信过程中的代理信息，默认使用系统网络代理。 |
| protocol12+ | string | 否 | 是 | 自定义Sec-WebSocket-Protocol字段，默认为""。 |
| skipServerCertVerification20+ | boolean | 否 | 是 | 是否跳过服务器证书验证。true表示跳过服务器证书验证，false表示不跳过服务器证书验证。默认为false。 |
| pingInterval21+ | number | 否 | 是 | 自定义[心跳检测](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/websocket-connection#场景介绍)时间，默认为30s。每pingInterval周期会发起心跳检测，设置为0则表示关闭心跳检测。最大值：30000s，最小值：0s。 |
| pongTimeout21+ | number | 否 | 是 | 自定义发起心跳检测后，超时断开时间，默认为30s。发起心跳检测后若pongTimeout时间未响应则断开连接。最大值：30000s，最小值：0s。pongTimeout须小于等于pingInterval。 |

#### ClientCert11+

客户端证书类型。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| certPath | string | 否 | 否 | 证书路径。 |
| keyPath | string | 否 | 否 | 证书密钥的路径。 |
| keyPassword | string | 否 | 是 | 证书密钥的密码。缺省为空字符串。 |

#### ProxyConfiguration12+

type ProxyConfiguration = 'system' | 'no-proxy' | HttpProxy

网络代理配置信息

**系统能力**：SystemCapability.Communication.NetStack

| 类型 | 说明 |
| :-- | :-- |
| 'system' | 使用系统默认网络代理。 |
| 'no-proxy' | 不使用网络代理。 |
| [HttpProxy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection#httpproxy10) | 使用指定的网络代理。 |

#### WebSocketCloseOptions

关闭WebSocket连接时，可选参数的类型和说明。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| code | number | 否 | 是 | 错误码，关闭WebSocket连接时的可选参数，可根据实际情况来填。传入值必须为正整数，取值范围为\[1000,1015\]。如果未指定错误码或传入值不在上述范围内，code将会被设置为默认值1000。 |
| reason | string | 否 | 是 | 原因值，关闭WebSocket连接时的可选参数，可根据实际情况来填。如果未指定原因值，则原因值将会被设置为默认值"CLOSE\_NORMAL"。 |

#### CloseResult10+

关闭WebSocket连接时，订阅close事件得到的关闭结果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| code | number | 否 | 否 | 错误码，订阅close事件得到的关闭连接的错误码。 |
| reason | string | 否 | 否 | 原因值，订阅close事件得到的关闭连接的错误原因。 |

#### ResponseHeaders12+

type ResponseHeaders = { \[k: string\]: string | string\[\] | undefined; }

服务器发送的响应头。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| \[k:string\] | string | string\[\] | undefined | 否 | 键值对形式存储。其键的类型为字符，可取任意值，其值的类型为字符、字符数组或undefined。 |

#### close错误码说明

发送给服务端的错误码必须为正整数，取值范围为\[1000,1015\],可以自行定义，如果未指定错误码或传入值不在上述范围内，错误码将会被设置为默认值1000。下面的列表仅供参考。

**系统能力**：SystemCapability.Communication.NetStack

| 值 | 说明 |
| :-- | :-- |
| 1000 | 正常关闭。 |
| 1001 | 服务器主动关闭。 |
| 1002 | 协议错误。 |
| 1003 | 无法处理的数据类型。 |
| 1004~1015 | 保留值。 |

#### HttpProxy12+

type HttpProxy = connection.HttpProxy

网络全局代理配置信息。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 类型 | 说明 |
| :-- | :-- |
| connection.HttpProxy | 使用指定的网络代理。 |

#### WebSocketServerConfig19+

启动服务端的service时，需要输入的配置信息和说明。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| serverIP | string | 否 | 是 | 服务端监听特定ip地址，默认是"0.0.0.0"。 |
| serverPort | number | 否 | 否 | 服务端监听的端口号。 |
| serverCert | [ServerCert](#servercert19) | 否 | 是 | 指定服务端证书的信息，包括服务端证书文件路径和服务端证书的私钥文件路径。 |
| protocol | string | 否 | 是 | 自定义协议。 |
| maxConcurrentClientsNumber | number | 否 | 否 | 最大并发客户端数量，当达到最大数时，服务端拒绝新连接。默认最大数量为10。 |
| maxConnectionsForOneClient | number | 否 | 否 | 单个客户端的最大连接数。默认最大数量为10。 |

#### ServerCert19+

指定服务端证书的信息，包括服务端证书文件路径和服务端证书的私钥文件路径。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| certPath | string | 否 | 否 | 服务端证书文件路径。 |
| keyPath | string | 否 | 否 | 服务端证书的私钥文件路径。 |

#### WebSocketMessage19+

从指定客户端接收到的消息，包括客户端的信息和数据。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| data | string |ArrayBuffer | 否 | 否 | 接收到的客户端发的消息数据。 |
| clientConnection | [WebSocketConnection](#websocketconnection19) | 否 | 否 | 客户端信息，包括客户端的ip地址和端口号port。 |

#### WebSocketConnection19+

客户端信息，包括客户端的ip地址和端口号port。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| clientIP | string | 否 | 否 | 客户端的ip地址。 |
| clientPort | number | 否 | 否 | 客户端的端口号port。 |

#### ClientConnectionCloseCallback19+

type ClientConnectionCloseCallback = (clientConnection: WebSocketConnection, closeReason: CloseResult) => void

关闭WebSocketServer连接时，订阅close事件得到的指定客户端的关闭结果。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| clientConnection | [WebSocketConnection](#websocketconnection19) | 是 | 客户端信息，包括客户端的ip地址和端口号port。 |
| closeReason | [CloseResult](#closeresult10) | 是 | 关闭WebSocket连接时，订阅close事件得到的关闭结果。 |

---
title: "@ohos.net.socket (Socket连接)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-socket"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Network Kit（网络服务）"
  - "ArkTS API"
  - "@ohos.net.socket (Socket连接)"
captured_at: "2026-04-17T01:48:23.001Z"
---

# @ohos.net.socket (Socket连接)

本模块提供利用Socket进行数据传输的能力，支持TCPSocket、UDPSocket、WebSocket和TLSSocket。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/hbcZKbbDS0yzb7M7TJzPUA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=616D7D6B635C1D47A48159263816B986B16ABED75A0B140C8908C998C9D5E508)

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块API使用时建议放在worker线程或者taskpool中做网络操作，否则可能会导致UI线程卡顿。

#### 导入模块

```ts
import { socket } from '@kit.NetworkKit';
```

#### socket.constructUDPSocketInstance

constructUDPSocketInstance(): UDPSocket

创建一个UDPSocket对象。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [UDPSocket](#udpsocket) | 返回一个UDPSocket对象。 |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
```

#### UDPSocket

UDPSocket连接。在调用UDPSocket的方法前，需要先通过[socket.constructUDPSocketInstance](#socketconstructudpsocketinstance)创建UDPSocket对象。

#### \[h2\]bind

bind(address: NetAddress, callback: AsyncCallback<void>): void

绑定IP地址和端口，端口可以由用户指定或由系统随机分配。使用callback异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| address | [NetAddress](#netaddress) | 是 | 本端地址信息，参考[NetAddress](#netaddress)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。成功返回空，失败返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',  // 本端地址
  port: 1234
}
udp.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
```

#### \[h2\]bind

bind(address: NetAddress): Promise<void>

绑定IP地址和端口，端口可以由用户指定或由系统随机分配。使用Promise异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| address | [NetAddress](#netaddress) | 是 | 本端地址信息，参考[NetAddress](#netaddress)。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',  // 本端地址
  port: 8080
}
udp.bind(bindAddr).then(() => {
  console.info('bind success');
}).catch((err: BusinessError) => {
  console.error('bind fail');
});
```

#### \[h2\]send

send(options: UDPSendOptions, callback: AsyncCallback<void>): void

通过UDPSocket连接发送数据。使用callback异步回调。

发送数据前，需要先调用[UDPSocket.bind()](#bind)绑定IP地址和端口。该接口为耗时操作，请在Worker线程或taskpool线程调用该接口。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [UDPSendOptions](#udpsendoptions) | 是 | UDPSocket发送参数，参考[UDPSendOptions](#udpsendoptions)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。成功返回空，失败返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2301206 | Socks5 failed to connect to the proxy server. |
| 2301207 | Socks5 username or password is invalid. |
| 2301208 | Socks5 failed to connect to the remote server. |
| 2301209 | Socks5 failed to negotiate the authentication method. |
| 2301210 | Socks5 failed to send the message. |
| 2301211 | Socks5 failed to receive the message. |
| 2301212 | Socks5 serialization error. |
| 2301213 | Socks5 deserialization error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',  // 本端地址
  port: 1234
}
udp.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',  // 对端地址
  port: 8080
}
let sendOptions: socket.UDPSendOptions = {
  data: 'Hello, server!',
  address: netAddress
}
udp.send(sendOptions, (err: BusinessError) => {
  if (err) {
    console.error('send fail');
    return;
  }
  console.info('send success');
});
```

**示例（设置socket代理）：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',  // 本端地址
  port: 1234
}
udp.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',  // 对端地址
  port: 8080
}
let socks5Server: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let proxyOptions: socket.ProxyOptions = {
  type : 1,
  address: socks5Server,
  username: "xxx",
  password: "xxx"
}
let sendOptions: socket.UDPSendOptions = {
  data: 'Hello, server!',
  address: netAddress,
  proxy: proxyOptions,
}
udp.send(sendOptions, (err: BusinessError) => {
  if (err) {
    console.error('send fail');
    return;
  }
  console.info('send success');
});
```

#### \[h2\]send

send(options: UDPSendOptions): Promise<void>

通过UDPSocket连接发送数据。使用Promise异步回调。

发送数据前，需要先调用[UDPSocket.bind()](#bind)绑定IP地址和端口。该接口为耗时操作，请在Worker线程或taskpool线程调用该接口。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [UDPSendOptions](#udpsendoptions) | 是 | UDPSocket发送参数，参考[UDPSendOptions](#udpsendoptions)。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2301206 | Socks5 failed to connect to the proxy server. |
| 2301207 | Socks5 username or password is invalid. |
| 2301208 | Socks5 failed to connect to the remote server. |
| 2301209 | Socks5 failed to negotiate the authentication method. |
| 2301210 | Socks5 failed to send the message. |
| 2301211 | Socks5 failed to receive the message. |
| 2301212 | Socks5 serialization error. |
| 2301213 | Socks5 deserialization error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx', // 本端地址
  port: 8080
}
udp.bind(bindAddr).then(() => {
  console.info('bind success');
}).catch((err: BusinessError) => {
  console.error('bind fail');
  return;
});
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx', // 对端地址
  port: 8080
}
let sendOptions: socket.UDPSendOptions = {
  data: 'Hello, server!',
  address: netAddress
}
udp.send(sendOptions).then(() => {
  console.info('send success');
}).catch((err: BusinessError) => {
  console.error('send fail');
});
```

**示例（设置socket代理）：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx', // 本端地址
  port: 8080
}
udp.bind(bindAddr).then(() => {
  console.info('bind success');
}).catch((err: BusinessError) => {
  console.error('bind fail');
  return;
});
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx', // 对端地址
  port: 8080
}
let socks5Server: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let proxyOptions: socket.ProxyOptions = {
  type : 1,
  address: socks5Server,
  username: "xxx",
  password: "xxx"
}
let sendOptions: socket.UDPSendOptions = {
  data: 'Hello, server!',
  address: netAddress,
  proxy: proxyOptions,
}
udp.send(sendOptions).then(() => {
  console.info('send success');
}).catch((err: BusinessError) => {
  console.error('send fail');
});
```

#### \[h2\]close

close(callback: AsyncCallback<void>): void

关闭UDPSocket连接。使用callback异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | 是 | 回调函数。关闭UDPSocket连接后触发回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
udp.close((err: BusinessError) => {
  if (err) {
    console.error('close fail');
    return;
  }
  console.info('close success');
})
```

#### \[h2\]close

close(): Promise<void>

关闭UDPSocket连接。使用Promise异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
udp.close().then(() => {
  console.info('close success');
}).catch((err: BusinessError) => {
  console.error('close fail');
});
```

#### \[h2\]getState

getState(callback: AsyncCallback<SocketStateBase>): void

获取UDPSocket状态。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/-UmibiYoSriYcKqCk53BTw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=FDA6628390C91F07AF79605530E7B8F71A9F9C4AA01E2A6B1582594262E4335C)

bind方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[SocketStateBase](#socketstatebase)\> | 是 | 回调函数。成功返回UDPSocket状态信息，失败返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
udp.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.error('bind success');
  udp.getState((err: BusinessError, data: socket.SocketStateBase) => {
    if (err) {
      console.error('getState fail');
      return;
    }
    console.info('getState success:' + JSON.stringify(data));
  })
})
```

#### \[h2\]getState

getState(): Promise<SocketStateBase>

获取UDPSocket状态。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/CISUuTmcRgGeVuS1bgGicA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=07BE242F0D33B143D9158280178852989703059611497892DFC588FA14ED82C0)

bind方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[SocketStateBase](#socketstatebase)\> | 以Promise形式返回获取UDPSocket状态的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
udp.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
  udp.getState().then((data: socket.SocketStateBase) => {
    console.info('getState success:' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error('getState fail' + JSON.stringify(err));
  });
});
```

#### \[h2\]getSocketFd23+

getSocketFd(): Promise<number>

获取UDPSocket的文件描述符。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/DuvyQYzLRqKiaX9GEow6nA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=DD90F9B2B601FDFD3D57316F7BAE73204BD29D685B24E2BD2125D32CCF4B599E)

-   [bind](#bind)方法调用成功后，才可调用此方法。
-   bind异常、Socket已关闭（如调用close后）等异常情况下调用本接口会返回-1。
-   文件描述符的生命周期由系统管理，应用可以通过[close](#close)方法关闭Socket连接，避免直接操作文件描述符进行关闭。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | Promise对象，返回Socket的文件描述符。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
let bindAddr: socket.NetAddress = {
    address: '192.168.xx.xxx',
    port: 8080
}
udp.bind(bindAddr)
  .then(() => {
    udp.getSocketFd()
      .then((fd: number) => {
        console.info(`Socket FD：${fd}`);
      }).catch((err: BusinessError) => {
      console.error(`getSocketFd fail: ${err.message}, errorCode: ${err.code}`);
    });
  }).catch((err: BusinessError) => {
  console.error('bind fail');
});
```

#### \[h2\]setExtraOptions

setExtraOptions(options: UDPExtraOptions, callback: AsyncCallback<void>): void

设置UDPSocket连接的其他属性。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/yjUODGSERECTVm6-xvS0qQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=3E6A1A9BE2EC66812F8E18A7715A1D90AF7C126751C1FBDDC0EDA3B30F8938AF)

bind方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [UDPExtraOptions](#udpextraoptions) | 是 | UDPSocket连接的其他属性，参考[UDPExtraOptions](#udpextraoptions)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。成功返回空，失败返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();

let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
udp.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
  let udpextraoptions: socket.UDPExtraOptions = {
    receiveBufferSize: 8192,
    sendBufferSize: 8192,
    reuseAddress: false,
    socketTimeout: 6000,
    broadcast: true
  }
  udp.setExtraOptions(udpextraoptions, (err: BusinessError) => {
    if (err) {
      console.error('setExtraOptions fail');
      return;
    }
    console.info('setExtraOptions success');
  })
})
```

#### \[h2\]setExtraOptions

setExtraOptions(options: UDPExtraOptions): Promise<void>

设置UDPSocket连接的其他属性。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/VfKRFTktSIG6CRpX5wG5iw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=6C65C8B054DD5FB1F132D0CEFA6343945FD7A49C6F4F59AFEC5CA1B2C5657F85)

bind方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [UDPExtraOptions](#udpextraoptions) | 是 | UDPSocket连接的其他属性，参考[UDPExtraOptions](#udpextraoptions)。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();

let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
udp.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
  let udpextraoptions: socket.UDPExtraOptions = {
    receiveBufferSize: 8192,
    sendBufferSize: 8192,
    reuseAddress: false,
    socketTimeout: 6000,
    broadcast: true
  }
  udp.setExtraOptions(udpextraoptions).then(() => {
    console.info('setExtraOptions success');
  }).catch((err: BusinessError) => {
    console.error('setExtraOptions fail');
  });
})
```

#### \[h2\]getLocalAddress12+

getLocalAddress(): Promise<NetAddress>

获取UDP连接的本地Socket地址。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/pOjroUMlSTKZfczqO8VEtQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=9D104A67FB395AD3E170347AD153780175775A87ADDA1072010898E05A04A9CF)

bind方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[NetAddress](#netaddress)\> | 以Promise形式返回获取本地socket地址的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 2300002 | System internal error. |
| 2301009 | Bad file descriptor. |
| 2303188 | Socket operation on non-socket. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();

let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
udp.bind(bindAddr).then(() => {
  console.info('bind success');
  udp.getLocalAddress().then((localAddress: socket.NetAddress) => {
        console.info("UDP_Socket get SUCCESS! Address：" + JSON.stringify(localAddress));
      }).catch((err: BusinessError) => {
        console.error("UDP_Socket get FAILED! Error: " + JSON.stringify(err));
      })
}).catch((err: BusinessError) => {
  console.error('bind fail');
});
```

#### \[h2\]on('message')

on(type: 'message', callback: Callback<SocketMessageInfo>): void

订阅UDPSocket连接的接收消息事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅的事件类型。'message'：接收消息事件。 |
| callback | Callback<[SocketMessageInfo](#socketmessageinfo11)\> | 是 | 回调函数。返回订阅某类事件后UDPSocket连接成功的状态信息。 |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();

udp.on('message', (value: socket.SocketMessageInfo) => {
  let messageView = '';
  let uint8Array = new Uint8Array(value.message);
  for (let i: number = 0; i < value.message.byteLength; i++) {
    let messages = uint8Array[i];
    let message = String.fromCharCode(messages);
    messageView += message;
  }
  console.info('on message message: ' + JSON.stringify(messageView));
  console.info('remoteInfo: ' + JSON.stringify(value.remoteInfo));
});
```

#### \[h2\]off('message')

off(type: 'message', callback?: Callback<SocketMessageInfo>): void

取消订阅UDPSocket连接的接收消息事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 取消订阅的事件类型。'message'：接收消息事件。 |
| callback | Callback<[SocketMessageInfo](#socketmessageinfo11)\> | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
let messageView = '';
let callback = (value: socket.SocketMessageInfo) => {
  for (let i: number = 0; i < value.message.byteLength; i++) {
    let uint8Array = new Uint8Array(value.message)
    let messages = uint8Array[i]
    let message = String.fromCharCode(messages);
    messageView += message;
  }
  console.info('on message message: ' + JSON.stringify(messageView));
  console.info('remoteInfo: ' + JSON.stringify(value.remoteInfo));
}
udp.on('message', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
udp.off('message', callback);
udp.off('message');
```

#### \[h2\]on('listening' | 'close')

on(type: 'listening' | 'close', callback: Callback<void>): void

订阅UDPSocket连接的数据包消息事件或关闭事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 
订阅的事件类型。

\- 'listening'：数据包消息事件。

\- 'close'：关闭事件。

 |
| callback | Callback<void> | 是 | 回调函数。UDPSocket连接的某类数据包消息事件或关闭事件发生变化后触发回调函数。 |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
udp.on('listening', () => {
  console.info("on listening success");
});
udp.on('close', () => {
  console.info("on close success");
});
```

#### \[h2\]off('listening' | 'close')

off(type: 'listening' | 'close', callback?: Callback<void>): void

取消订阅UDPSocket连接的数据包消息事件或关闭事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 
取消订阅事件类型。

\- 'listening'：数据包消息事件。

\- 'close'：关闭事件。

 |
| callback | Callback<void> | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
let callback1 = () => {
  console.info("on listening, success");
}
udp.on('listening', callback1);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
udp.off('listening', callback1);
udp.off('listening');
let callback2 = () => {
  console.info("on close, success");
}
udp.on('close', callback2);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
udp.off('close', callback2);
udp.off('close');
```

#### \[h2\]on('error')

on(type: 'error', callback: ErrorCallback): void

订阅UDPSocket连接的error事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅的事件类型。'error'：error事件。 |
| callback | ErrorCallback | 是 | 回调函数。UDPSocket连接发生error事件后触发回调函数。 |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
udp.on('error', (err: BusinessError) => {
  console.error("on error, err:" + JSON.stringify(err))
});
```

#### \[h2\]off('error')

off(type: 'error', callback?: ErrorCallback): void

取消订阅UDPSocket连接的error事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 取消订阅的事件类型。'error'：error事件。 |
| callback | ErrorCallback | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
let callback = (err: BusinessError) => {
  console.error("on error, err:" + JSON.stringify(err));
}
udp.on('error', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
udp.off('error', callback);
udp.off('error');
```

#### NetAddress

目标地址信息。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| address11+ | string | 否 | 否 | 本地绑定的ip地址。 |
| port | number | 否 | 否 | 端口号 ，范围0~65535。如果不指定系统随机分配端口。 |
| family | number | 否 | 否 | 
网络协议类型，可选类型：

\- 1：IPv4。默认为1。

\- 2：IPv6。地址为IPV6类型，该字段必须被显式指定为2。

\- 3：Domain18+。地址为Domain类型，该字段必须被显式指定为3。当前仅支持[TCPSocket.connect](#connect)和[TLSSocket.connect](#connect9)。

 |

#### ProxyOptions18+

Socket代理信息。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| type | [ProxyTypes](#proxytypes18) | 否 | 否 | 代理类型。 |
| address | [NetAddress](#netaddress) | 否 | 否 | 代理地址信息。 |
| username | string | 否 | 是 | 指定用户名，如果使用用户密码验证方式。 |
| password | string | 否 | 是 | 指定密码，如果使用用户密码验证方式。 |

#### ProxyTypes18+

Socket代理类型。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| NONE | 0 | 不使用代理。 |
| SOCKS5 | 1 | 使用Socks5代理。 |

#### UDPSendOptions

UDPSocket发送参数。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| data | string | ArrayBuffer | 否 | 否 | 发送的数据。 |
| address | [NetAddress](#netaddress) | 否 | 否 | 目标地址信息。 |
| proxy18+ | [ProxyOptions](#proxyoptions18) | 否 | 是 | 使用的代理信息，默认不使用代理。 |

#### UDPExtraOptions

UDPSocket连接的其他属性。继承自[ExtraOptionsBase](#extraoptionsbase)。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| broadcast | boolean | 否 | 是 | 是否可以发送广播。true表示可发送广播，false表示不可发送广播。默认为false。 |

#### SocketMessageInfo11+

socket连接信息

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| message | ArrayBuffer | 否 | 否 | 接收的事件消息。 |
| remoteInfo | [SocketRemoteInfo](#socketremoteinfo) | 否 | 否 | socket连接信息。 |

#### SocketStateBase

Socket的状态信息。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| isBound | boolean | 否 | 否 | 是否绑定。true：绑定；false：不绑定。 |
| isClose | boolean | 否 | 否 | 是否关闭。true：关闭；false：打开。 |
| isConnected | boolean | 否 | 否 | 是否连接。true：连接；false：断开。 |

#### SocketRemoteInfo

Socket的连接信息。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| address | string | 否 | 否 | 本地绑定的ip地址。 |
| family | 'IPv4' | 'IPv6' | 否 | 否 | 
网络协议类型，可选类型：

\- IPv4

\- IPv6

默认为IPv4。

 |
| port | number | 否 | 否 | 端口号，范围0~65535。 |
| size | number | 否 | 否 | 服务器响应信息的字节长度。 |

#### UDP 错误码说明

UDP 其余错误码映射形式为：2301000 + Linux内核错误码。

错误码的详细介绍参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)。

#### socket.constructMulticastSocketInstance11+

constructMulticastSocketInstance(): MulticastSocket

创建一个MulticastSocket对象。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [MulticastSocket](#multicastsocket11) | 返回一个MulticastSocket对象。 |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
```

#### MulticastSocket11+

MulticastSocket连接。在调用MulticastSocket的方法前，需要先通过[socket.constructMulticastSocketInstance](#socketconstructmulticastsocketinstance11)创建MulticastSocket对象。

#### \[h2\]addMembership11+

addMembership(multicastAddress: NetAddress, callback: AsyncCallback<void>): void

加入多播组。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/HmquAHJVQaWcHNb9Xg-PEg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=40B3BDD1312B63A13C6B9788C80CDAC83C2CE03E619C102E7597E2E90B697295)

多播使用的IP地址属于特定的范围（例如224.0.0.0到239.255.255.255）。

加入多播组后，既可以是发送端，也可以是接收端，相互之间以广播的形式传递数据，不区分客户端或服务端。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| multicastAddress | [NetAddress](#netaddress) | 是 | 目标地址信息，参考[NetAddress](#netaddress)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。失败返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2301022 | Invalid argument. |
| 2301088 | Not a socket. |
| 2301098 | Address in use. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';

let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
let addr: socket.NetAddress = {
  address: '239.255.0.1',
  port: 8080
}
multicast.addMembership(addr, (err: Object) => {
  if (err) {
    console.error('add membership fail, err: ' + JSON.stringify(err));
    return;
  }
  console.info('add membership success');
})
```

#### \[h2\]addMembership11+

addMembership(multicastAddress: NetAddress): Promise<void>

加入多播组。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/oYpkKNEAS7SgWxzPLZu7ug/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=F90C44AB82D4E50E4765384E204A15E1DBC29CE9EAE5973B9AC51A9A17A6F471)

多播使用的IP地址属于特定的范围（例如224.0.0.0到239.255.255.255）。

加入多播组后，既可以是发送端，也可以是接收端，相互之间以广播的形式传递数据，不区分客户端或服务端。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| multicastAddress | [NetAddress](#netaddress) | 是 | 目标地址信息，参考[NetAddress](#netaddress)。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 以Promise形式返回MulticastSocket加入多播组的行为结果。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2301088 | Not a socket. |
| 2301098 | Address in use. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';

let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
let addr: socket.NetAddress = {
  address: '239.255.0.1',
  port: 8080
}
multicast.addMembership(addr).then(() => {
  console.info('addMembership success');
}).catch((err: Object) => {
  console.error('addMembership fail');
});
```

#### \[h2\]dropMembership11+

dropMembership(multicastAddress: NetAddress, callback: AsyncCallback<void>): void

退出多播组。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/MB7Z2omXS66rhYs3azlYDA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=D05C1283EBDFA82264C027CAC65E0845C769B907C80806626BFB42252310405C)

多播使用的IP地址属于特定的范围（例如224.0.0.0到239.255.255.255）。

从已加入的多播组中退出，必须在加入多播组 [addMembership](#addmembership11) 之后退出才有效。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| multicastAddress | [NetAddress](#netaddress) | 是 | 目标地址信息，参考[NetAddress](#netaddress)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。失败返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2301088 | Not a socket. |
| 2301098 | Address in use. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';

let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
let addr: socket.NetAddress = {
  address: '239.255.0.1',
  port: 8080
}
multicast.dropMembership(addr, (err: Object) => {
  if (err) {
    console.error('drop membership fail, err: ' + JSON.stringify(err));
    return;
  }
  console.info('drop membership success');
})
```

#### \[h2\]dropMembership11+

dropMembership(multicastAddress: NetAddress): Promise<void>

退出多播组。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/KzPaxOBqTEODUprR7ZiGmg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=4F51A74BF27965FDAF563F196D71451EBE2C3F01A0D3D43B543D1113121D9A1D)

多播使用的IP地址属于特定的范围（例如224.0.0.0到239.255.255.255）。

从已加入的多播组中退出，必须在加入多播组 [addMembership](#addmembership11) 之后退出才有效。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| multicastAddress | [NetAddress](#netaddress) | 是 | 目标地址信息，参考[NetAddress](#netaddress)。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 以Promise形式返回MulticastSocket加入多播组的执行结果。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2301088 | Not a socket. |
| 2301098 | Address in use. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';

let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
let addr: socket.NetAddress = {
  address: '239.255.0.1',
  port: 8080
}
multicast.dropMembership(addr).then(() => {
  console.info('drop membership success');
}).catch((err: Object) => {
  console.error('drop membership fail');
});
```

#### \[h2\]setMulticastTTL11+

setMulticastTTL(ttl: number, callback: AsyncCallback<void>): void

设置多播通信时数据包在网络传输过程中路由器最大跳数。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/kqkfDalrTWm6jsj-2a0wqg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=1A3429A86EC84C4DF822D53DEE59C7B6B5094B23756B972E04305864FE8DA61F)

用于限制数据包在网络中传输时能够经过的最大路由器跳数的字段，TTL (Time to live)。

范围为 0～255，默认值为 1 。

如果一个多播数据包的 TTL 值为 1，那么它只能被直接连接到发送者的主机接收。如果 TTL 被设置为一个较大的值，那么数据包就能够被传送到更远的网络范围内。

在调用 [addMembership](#addmembership11) 之后，调用此接口才有效。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| ttl | number | 是 | ttl设置数值，类型为数字number。 |
| callback | AsyncCallback<void> | 是 | 回调函数。失败返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2301022 | Invalid argument. |
| 2301088 | Not a socket. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';

let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
let ttl = 8
multicast.setMulticastTTL(ttl, (err: Object) => {
  if (err) {
    console.error('set ttl fail, err: ' + JSON.stringify(err));
    return;
  }
  console.info('set ttl success');
})
```

#### \[h2\]setMulticastTTL11+

setMulticastTTL(ttl: number): Promise<void>

设置多播通信时数据包在网络传输过程中路由器最大跳数。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/9bId-9oSSVO9kpCiq8ISTQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=663EF6D15A5F9406127D476487F39710F45611A45FC75745650545548D149055)

用于限制数据包在网络中传输时能够经过的最大路由器跳数的字段，TTL (Time to live)。

范围为 0～255，默认值为 1 。

如果一个多播数据包的 TTL 值为 1，那么它只能被直接连接到发送者的主机接收。如果 TTL 被设置为一个较大的值，那么数据包就能够被传送到更远的网络范围内。

在调用 [addMembership](#addmembership11) 之后，调用此接口才有效。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| ttl | number | 是 | ttl设置数值，类型为数字Number。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 以Promise形式返回MulticastSocket设置TTL数值的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2301022 | Invalid argument. |
| 2301088 | Not a socket. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';

let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
multicast.setMulticastTTL(8).then(() => {
  console.info('set ttl success');
}).catch((err: Object) => {
  console.error('set ttl failed');
});
```

#### \[h2\]getMulticastTTL11+

getMulticastTTL(callback: AsyncCallback<number>): void

获取数据包在网络传输过程中路由器最大跳数(TTL)的值。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/d8Q_9-S7ToKjnd1MyNCkbA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=1B27AA50EC80C4DE1F0BF946DB25D26BE9CE362E152B3F92471AC852A0EE64BF)

用于限制数据包在网络中传输时能够经过的最大路由器跳数的字段，TTL (Time to live)。

范围为 0～255，默认值为 1 。

如果一个多播数据包的 TTL 值为 1，那么它只能被直接连接到发送者的主机接收。如果 TTL 被设置为一个较大的值，那么数据包就能够被传送到更远的网络范围内。

在调用 [addMembership](#addmembership11) 之后，调用此接口才有效。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | 是 | 回调函数。失败返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2301088 | Not a socket. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';

let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
multicast.getMulticastTTL((err: Object, value: Number) => {
  if (err) {
    console.error('set ttl fail, err: ' + JSON.stringify(err));
    return;
  }
  console.info('set ttl success, value: ' + JSON.stringify(value));
})
```

#### \[h2\]getMulticastTTL11+

getMulticastTTL(): Promise<number>

获取数据包在网络传输过程中路由器最大跳数(TTL)的值。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/jP6Dcq0NQb-WrIDRUZTjhQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=E9FAD50E41CE18B8164CA8E40CF512A4AD649A85657A58C288F43BD481A7C6DB)

用于限制数据包在网络中传输时能够经过的最大路由器跳数的字段，TTL (Time to live)。

范围为 0～255，默认值为 1 。

如果一个多播数据包的 TTL 值为 1，那么它只能被直接连接到发送者的主机接收。如果 TTL 被设置为一个较大的值，那么数据包就能够被传送到更远的网络范围内。

在调用 [addMembership](#addmembership11) 之后，调用此接口才有效。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | 以Promise形式返回当前TTL数值。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2301088 | Not a socket. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';

let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
multicast.getMulticastTTL().then((value: Number) => {
  console.info('ttl: ', JSON.stringify(value));
}).catch((err: Object) => {
  console.error('set ttl failed');
});
```

#### \[h2\]setLoopbackMode11+

setLoopbackMode(flag: boolean, callback: AsyncCallback<void>): void

设置多播通信中的环回模式标志位。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/9PoQooAVTn2_jQvSLYQsIA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=7043C08D4D06AC0A102A9C474EF09513933C80FC0C614059F5B398DA6C4E19A2)

用于设置环回模式，开启或关闭两种状态，默认为开启状态。

如果一个多播通信中环回模式设置值为 true，那么它允许主机在本地循环接收自己发送的多播数据包。如果为 false，则主机不会接收到自己发送的多播数据包。

在调用 [addMembership](#addmembership11) 之后，调用此接口才有效。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| flag | boolean | 是 | 是否开启环回模式。true表示环回模式开启，false表示环回模式关闭。 |
| callback | AsyncCallback<void> | 是 | 回调函数。失败返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2301088 | Not a socket. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';

let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
multicast.setLoopbackMode(false, (err: Object) => {
  if (err) {
    console.error('set loopback mode fail, err: ' + JSON.stringify(err));
    return;
  }
  console.info('set loopback mode success');
})
```

#### \[h2\]setLoopbackMode11+

setLoopbackMode(flag: boolean): Promise<void>

设置多播通信中的环回模式标志位。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/sHQgHp9RQq2nkiaeeJ_pHw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=BA47F46F9EE39A9BBD7999FF5D74D951C3A6D210980EBD77E6F7ED43D4F7A40B)

用于设置环回模式，开启或关闭两种状态，默认为开启状态。

如果一个多播通信中环回模式设置值为 true，那么它允许主机在本地循环接收自己发送的多播数据包。如果为 false，则主机不会接收到自己发送的多播数据包。

在调用 [addMembership](#addmembership11) 之后，调用此接口才有效。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| flag | boolean | 是 | 是否开启环回模式。true表示环回模式开启，false表示环回模式关闭。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 以Promise形式返回MulticastSocket设置环回模式的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2301088 | Not a socket. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';

let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
multicast.setLoopbackMode(false).then(() => {
  console.info('set loopback mode success');
}).catch((err: Object) => {
  console.error('set loopback mode failed');
});
```

#### \[h2\]getLoopbackMode11+

getLoopbackMode(callback: AsyncCallback<boolean>): void

获取多播通信中的环回模式状态。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/thpSuI8pRQmCk1ZhRojdEw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=53B909A265ADE8D683886A69B5B0293E4D395EB44CDF1AD589A45ADE9BA9E917)

用于获取当前环回模式开启或关闭的状态。

如果获取的属性值为 true，表示环回模式是开启的状态，允许主机在本地循环接收自己发送的多播数据包。如果为 false，则表示环回模式是关闭的状态，主机不会接收到自己发送的多播数据包。

在调用 [addMembership](#addmembership11) 之后，调用此接口才有效。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回值为环回模式状态，true表示环回模式开启，false表示环回模式关闭。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2301088 | Not a socket. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';

let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
multicast.getLoopbackMode((err: Object, value: Boolean) => {
  if (err) {
    console.error('get loopback mode fail, err: ' + JSON.stringify(err));
    return;
  }
  console.info('get loopback mode success, value: ' + JSON.stringify(value));
})
```

#### \[h2\]getLoopbackMode11+

getLoopbackMode(): Promise<boolean>

获取多播通信中的环回模式状态。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/bGJU53Z3SeeWd73fH14Rbw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=4BD64BEECD1EE1F8E639059C828E18DA19300E94898C4D1919D01D1B829C8C94)

用于获取当前环回模式开启或关闭的状态。

如果获取的属性值为 true，表示环回模式是开启的状态，允许主机在本地循环接收自己发送的多播数据包。如果为 false，则表示环回模式是关闭的状态，主机不会接收到自己发送的多播数据包。

在调用 [addMembership](#addmembership11) 之后，调用此接口才有效。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象。返回true表示环回模式开启，返回false表示环回模式关闭。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2301088 | Not a socket. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';

let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
multicast.getLoopbackMode().then((value: Boolean) => {
  console.info('loopback mode: ', JSON.stringify(value));
}).catch((err: Object) => {
  console.error('get loopback mode failed');
});
```

#### \[h2\]getSocketFd23+

getSocketFd(): Promise<number>

获取MulticastSocket的文件描述符。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/2Ms70-G0Sg-aKw7C7b-2SA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=CA2254C9817EFE938F93770BA7C08349287BAB95DD0715AAA1CDBDDD41863266)

-   [bind](#bind)方法调用成功后，才可调用此方法。
-   bind异常、Socket已关闭（如调用close后）等异常情况下调用本接口会返回-1。
-   文件描述符的生命周期由系统管理，应用可以通过[close](#close)方法关闭Socket连接，避免直接操作文件描述符进行关闭。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**模型约束：** 此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | Promise对象，返回Socket的文件描述符。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
let bindAddr: socket.NetAddress = {
    address: '192.168.xx.xxx',
    port: 8080
}
multicast.bind(bindAddr)
  .then(() => {
    console.info('bind success');
    multicast.getSocketFd().then((fd: number) => {
      console.info(`Socket FD：${fd}`);
    }).catch((err: BusinessError) => {
      console.error(`getSocketFd fail: ${err.message}, errorCode: ${err.code}`);
    });
  }).catch((err: BusinessError) => {
  console.error('bind fail');
});
```

#### socket.constructTCPSocketInstance

constructTCPSocketInstance(): TCPSocket

创建一个TCPSocket对象。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [TCPSocket](#tcpsocket) | 返回一个TCPSocket对象。 |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
```

#### TCPSocket

TCPSocket连接。在调用TCPSocket的方法前，需要先通过[socket.constructTCPSocketInstance](#socketconstructtcpsocketinstance)创建TCPSocket对象。

#### \[h2\]bind

bind(address: NetAddress, callback: AsyncCallback<void>): void

绑定IP地址和端口，端口可以指定为0由系统随机分配或由用户指定为其它非0端口。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/-56uIDibQYWH5telKQobwA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=F081B1E9ADAC5F4D0AE15513F7562666D203D6F00E2DB20998AF63DCDDD7014A)

bind方法如果因为端口冲突而执行失败，则会由系统随机分配端口号。

TCP客户端可先调用该接口(tcp.bind)显式绑定IP地址和端口号，再调用tcp.connect完成与服务端的连接；也可直接调用tcp.connect由系统自动绑定IP地址和端口号，完成与服务端的连接。

bind的IP为'localhost'或'127.0.0.1'时，只允许本地回环接口的连接，即服务端和客户端运行在同一台机器上。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| address | [NetAddress](#netaddress) | 是 | 本端地址信息，参考[NetAddress](#netaddress)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。失败返回错误、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
tcp.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
})
```

#### \[h2\]bind

bind(address: NetAddress): Promise<void>

绑定IP地址和端口，端口可以指定为0由系统随机分配或由用户指定为其它非0端口。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/jvni8CGZRb2xBH43DJ0kbA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=9C500DB8D761317563B468D7F4CD34288630681BC644C62F809A883430EF5851)

bind方法如果因为端口冲突而执行失败，则会由系统随机分配端口号。

TCP客户端可先调用该接口(tcp.bind)显式绑定IP地址和端口号，再调用tcp.connect完成与服务端的连接；也可直接调用tcp.connect由系统自动绑定IP地址和端口号，完成与服务端的连接。

bind的IP为'localhost'或'127.0.0.1'时，只允许本地回环接口的连接，即服务端和客户端运行在同一台机器上。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| address | [NetAddress](#netaddress) | 是 | 本端地址信息，参考[NetAddress](#netaddress)。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 以Promise形式返回TCPSocket绑定本机的IP地址和端口的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
tcp.bind(bindAddr).then(() => {
  console.info('bind success');
}).catch((err: BusinessError) => {
  console.error('bind fail');
});
```

#### \[h2\]connect

connect(options: TCPConnectOptions, callback: AsyncCallback<void>): void

连接到指定的IP地址和端口。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/EFsFfuEhT-awsLtUH15kug/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=820F99FEA38D645523DAEE614CBB6DC2BAF9396509032CFCD6E111E270933B79)

在没有执行tcp.bind的情况下，也可以直接调用该接口完成与TCP服务端的连接

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [TCPConnectOptions](#tcpconnectoptions) | 是 | TCPSocket连接的参数，参考[TCPConnectOptions](#tcpconnectoptions)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。失败返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2301206 | Socks5 failed to connect to the proxy server. |
| 2301207 | Socks5 username or password is invalid. |
| 2301208 | Socks5 failed to connect to the remote server. |
| 2301209 | Socks5 failed to negotiate the authentication method. |
| 2301210 | Socks5 failed to send the message. |
| 2301211 | Socks5 failed to receive the message. |
| 2301212 | Socks5 serialization error. |
| 2301213 | Socks5 deserialization error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000
}
tcp.connect(tcpconnectoptions, (err: BusinessError) => {
  if (err) {
    console.error('connect fail');
    return;
  }
  console.info('connect success');
})
```

**示例（设置socket代理）：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let socks5Server: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let proxyOptions: socket.ProxyOptions = {
  type : 1,
  address: socks5Server,
  username: "xxx",
  password: "xxx"
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000,
  proxy: proxyOptions,
}
tcp.connect(tcpconnectoptions, (err: BusinessError) => {
  if (err) {
    console.error('connect fail');
    return;
  }
  console.info('connect success');
})
```

#### \[h2\]connect

connect(options: TCPConnectOptions): Promise<void>

连接到指定的IP地址和端口。使用promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/zKGetUEAS9WyqXIbv7I8Ew/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=CA98252FB93841A7455ED2E29280E85C1744F031E7F3447AB16DEBEBE2C5D58D)

在没有执行tcp.bind的情况下，也可以直接调用该接口完成与TCP服务端的连接。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [TCPConnectOptions](#tcpconnectoptions) | 是 | TCPSocket连接的参数，参考[TCPConnectOptions](#tcpconnectoptions)。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 以Promise形式返回TCPSocket连接到指定的IP地址和端口的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2301206 | Socks5 failed to connect to the proxy server. |
| 2301207 | Socks5 username or password is invalid. |
| 2301208 | Socks5 failed to connect to the remote server. |
| 2301209 | Socks5 failed to negotiate the authentication method. |
| 2301210 | Socks5 failed to send the message. |
| 2301211 | Socks5 failed to receive the message. |
| 2301212 | Socks5 serialization error. |
| 2301213 | Socks5 deserialization error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000
}
tcp.connect(tcpconnectoptions).then(() => {
  console.info('connect success')
}).catch((err: BusinessError) => {
  console.error('connect fail');
});
```

**示例（设置socket代理）：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let socks5Server: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let proxyOptions: socket.ProxyOptions = {
  type : 1,
  address: socks5Server,
  username: "xxx",
  password: "xxx"
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000,
  proxy: proxyOptions,
}
tcp.connect(tcpconnectoptions).then(() => {
  console.info('connect success')
}).catch((err: BusinessError) => {
  console.error('connect fail');
});
```

#### \[h2\]send

send(options: TCPSendOptions, callback: AsyncCallback<void>): void

通过TCPSocket连接发送数据。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/l77cjVinRKy9DLbUpmz_iQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=2819F04173C83984D5E110176F852F965428A2B2A7A2D60723B2C8E0C4A31441)

connect方法调用成功后，才可调用此方法。该接口为耗时操作，请在Worker线程或taskpool线程调用该接口。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [TCPSendOptions](#tcpsendoptions) | 是 | TCPSocket发送请求的参数，参考[TCPSendOptions](#tcpsendoptions)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。失败返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000
}
tcp.connect(tcpconnectoptions, () => {
  console.info('connect success');
  let tcpSendOptions: socket.TCPSendOptions = {
    data: 'Hello, server!'
  }
  tcp.send(tcpSendOptions, (err: BusinessError) => {
    if (err) {
      console.error('send fail');
      return;
    }
    console.info('send success');
  })
})
```

#### \[h2\]send

send(options: TCPSendOptions): Promise<void>

通过TCPSocket连接发送数据。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/92dNUPfkRaeSUqE9XGdRFw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=42E3D005F673BEF5D8ECE4479C46CF6C4C6619BAD33D995DDB783F787DFF4D35)

connect方法调用成功后，才可调用此方法。该接口为耗时操作，请在Worker线程或taskpool线程调用该接口。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [TCPSendOptions](#tcpsendoptions) | 是 | TCPSocket发送请求的参数，参考[TCPSendOptions](#tcpsendoptions)。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000
}
tcp.connect(tcpconnectoptions, () => {
  console.info('connect success');
  let tcpSendOptions: socket.TCPSendOptions = {
    data: 'Hello, server!'
  }
  tcp.send(tcpSendOptions).then(() => {
    console.info('send success');
  }).catch((err: BusinessError) => {
    console.error('send fail');
  });
})
```

#### \[h2\]close

close(callback: AsyncCallback<void>): void

关闭TCPSocket连接。使用callback异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | 是 | 回调函数。失败返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();

tcp.close((err: BusinessError) => {
  if (err) {
    console.error('close fail');
    return;
  }
  console.info('close success');
})
```

#### \[h2\]close

close(): Promise<void>

关闭TCPSocket连接。使用Promise异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();

tcp.close().then(() => {
  console.info('close success');
}).catch((err: BusinessError) => {
  console.error('close fail');
});
```

#### \[h2\]getRemoteAddress

getRemoteAddress(callback: AsyncCallback<NetAddress>): void

获取对端Socket地址。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/4jekWEoMRqGo-Ogf5pFBkA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=B18558E67E9F227A1638A11E8165CE4ECDE97BB89E388CE11D1BDC772DCED745)

connect方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[NetAddress](#netaddress)\> | 是 | 回调函数。成功时返回对端Socket地址，失败时返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000
}
tcp.connect(tcpconnectoptions, () => {
  console.info('connect success');
  tcp.getRemoteAddress((err: BusinessError, data: socket.NetAddress) => {
    if (err) {
      console.error('getRemoteAddressfail');
      return;
    }
    console.info('getRemoteAddresssuccess:' + JSON.stringify(data));
  })
});
```

#### \[h2\]getRemoteAddress

getRemoteAddress(): Promise<NetAddress>

获取对端Socket地址。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/770JDykbSga05HwZCzo69w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=5B2087DF6E8025B37F16D4A0B731E502D628A1642E3484404E29954587AB506E)

connect方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[NetAddress](#netaddress)\> | 以Promise形式返回获取对端socket地址的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000
}
tcp.connect(tcpconnectoptions).then(() => {
  console.info('connect success');
  tcp.getRemoteAddress().then(() => {
    console.info('getRemoteAddress success');
  }).catch((err: BusinessError) => {
    console.error('getRemoteAddressfail');
  });
}).catch((err: BusinessError) => {
  console.error('connect fail');
});
```

#### \[h2\]getState

getState(callback: AsyncCallback<SocketStateBase>): void

获取TCPSocket状态。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/Brkl_WgWTymGeDqg6HP8yw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=B83D5D5046A09503DDC3EEDD4FB7422FCA98C0A6D514C1F134E0766E0B63EEFD)

bind或connect方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[SocketStateBase](#socketstatebase)\> | 是 | 回调函数。成功时获取TCPSocket状态，失败时返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000
}
tcp.connect(tcpconnectoptions, () => {
  console.info('connect success');
  tcp.getState((err: BusinessError, data: socket.SocketStateBase) => {
    if (err) {
      console.error('getState fail');
      return;
    }
    console.info('getState success:' + JSON.stringify(data));
  });
});
```

#### \[h2\]getState

getState(): Promise<SocketStateBase>

获取TCPSocket状态。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/LJlWZtP4SpqCZFrS2TTx1g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=AC9F8F87CA4A70910332C2FCEC584AFD50AF890C996D18A023CCA06B12529BA4)

bind或connect方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[SocketStateBase](#socketstatebase)\> | 以Promise形式返回获取TCPSocket状态的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000
}
tcp.connect(tcpconnectoptions).then(() => {
  console.info('connect success');
  tcp.getState().then(() => {
    console.info('getState success');
  }).catch((err: BusinessError) => {
    console.error('getState fail');
  });
}).catch((err: BusinessError) => {
  console.error('connect fail');
});
```

#### \[h2\]getSocketFd10+

getSocketFd(callback: AsyncCallback<number>): void

获取TCPSocket的文件描述符。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/g14LmZXhQy6arCCgqcAfQQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=EAAF48337FCA17762D33F85CC629301FF16DDD77A269E132E4550AE45E449D53)

-   bind或connect方法调用成功后，才可调用此方法。
-   文件描述符的生命周期由系统管理，应用可以通过[close](#close-2)方法关闭Socket连接，避免直接操作文件描述符进行关闭。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | 是 | 回调函数，当成功时，返回socket的文件描述符，失败时，返回undefined。 |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  // 绑定指定网络接口
}
tcp.bind(bindAddr)
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000
}
tcp.connect(tcpconnectoptions)
tcp.getSocketFd((err: BusinessError, data: number) => {
  console.error("getSocketFd failed: " + err);
  console.info("socketFd: " + data);
})
```

#### \[h2\]getSocketFd10+

getSocketFd(): Promise<number>

获取TCPSocket的文件描述符。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/At3CnitAQSWVEEFeFjuRaA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=6319BAB36B658F103A5D8047E35CC3E6AD7BFDEEB33ED9CB0A6A4B7ED1F5E4D6)

-   bind或connect方法调用成功后，才可调用此方法。
-   文件描述符的生命周期由系统管理，应用可以通过[close](#close-2)方法关闭Socket连接，避免直接操作文件描述符进行关闭。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | 以Promise形式返回socket的文件描述符。 |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let bindAddr: socket.NetAddress = {
    address: '192.168.xx.xxx',
  // 绑定指定网络接口
}
tcp.bind(bindAddr)
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000
}
tcp.connect(tcpconnectoptions)
tcp.getSocketFd().then((data: number) => {
  console.info("socketFd: " + data);
})
```

#### \[h2\]setExtraOptions

setExtraOptions(options: TCPExtraOptions, callback: AsyncCallback<void>): void

设置TCPSocket连接的其他属性。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/xEtqa0mCT3GtHwpGnQwzwA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=9D2A7B14C3C063B49689E0E5B19C260783288BAAA97729E4EBA229A527CBDB75)

bind或connect方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [TCPExtraOptions](#tcpextraoptions) | 是 | TCPSocket连接的其他属性，参考[TCPExtraOptions](#tcpextraoptions)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。失败时返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000
}

interface SocketLinger {
  on: boolean;
  linger: number;
}

tcp.connect(tcpconnectoptions, () => {
  console.info('connect success');
  let tcpExtraOptions: socket.TCPExtraOptions = {
    keepAlive: true,
    OOBInline: true,
    TCPNoDelay: true,
    socketLinger: { on: true, linger: 10 } as SocketLinger,
    receiveBufferSize: 8192,
    sendBufferSize: 8192,
    reuseAddress: true,
    socketTimeout: 3000
  }
  tcp.setExtraOptions(tcpExtraOptions, (err: BusinessError) => {
    if (err) {
      console.error('setExtraOptions fail');
      return;
    }
    console.info('setExtraOptions success');
  });
});
```

#### \[h2\]setExtraOptions

setExtraOptions(options: TCPExtraOptions): Promise<void>

设置TCPSocket连接的其他属性。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/KksEKhrbQhWZD8EU0UqHkw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=EA90D03BA3F0EFA2041F204C84DB2BAD0CBEDA85F5AD3145A15124279C5F6876)

bind或connect方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [TCPExtraOptions](#tcpextraoptions) | 是 | TCPSocket连接的其他属性，参考[TCPExtraOptions](#tcpextraoptions)。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000
}

interface SocketLinger {
  on: boolean;
  linger: number;
}

tcp.connect(tcpconnectoptions, () => {
  console.info('connect success');
  let tcpExtraOptions: socket.TCPExtraOptions = {
    keepAlive: true,
    OOBInline: true,
    TCPNoDelay: true,
    socketLinger: { on: true, linger: 10 } as SocketLinger,
    receiveBufferSize: 8192,
    sendBufferSize: 8192,
    reuseAddress: true,
    socketTimeout: 3000
  }
  tcp.setExtraOptions(tcpExtraOptions).then(() => {
    console.info('setExtraOptions success');
  }).catch((err: BusinessError) => {
    console.error('setExtraOptions fail');
  });
});
```

#### \[h2\]getLocalAddress12+

getLocalAddress(): Promise<NetAddress>

获取TCPSocket的本地Socket地址。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/PSTzq1eMQ26e2OaHj2GWoQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=A5FA920566B749870E7FD92B70348385F4E8473E98C660E4947F1F32C45B781B)

bind方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[NetAddress](#netaddress)\> | 以Promise形式返回获取本地socket地址的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 2300002 | System internal error. |
| 2301009 | Bad file descriptor. |
| 2303188 | Socket operation on non-socket. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  family: 1,
  port: 8080
}
tcp.bind(bindAddr).then(() => {
  tcp.getLocalAddress().then((localAddress: socket.NetAddress) => {
    console.info("SUCCESS! Address:" + JSON.stringify(localAddress));
  }).catch((err: BusinessError) => {
    console.error("FAILED! Error:" + JSON.stringify(err));
  })
}).catch((err: BusinessError) => {
  console.error('bind fail');
});
```

#### \[h2\]on('message')

on(type: 'message', callback: Callback<SocketMessageInfo>): void

订阅TCPSocket连接的接收消息事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅的事件类型。'message'：接收消息事件。 |
| callback | Callback<[SocketMessageInfo](#socketmessageinfo11)\> | 是 | 回调函数。返回TCPSocket连接信息。 |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
tcp.on('message', (value: socket.SocketMessageInfo) => {
  let messageView = '';
  let uint8Array = new Uint8Array(value.message);
  for (let i: number = 0; i < value.message.byteLength; i++) {
    let messages = uint8Array[i];
    let message = String.fromCharCode(messages);
    messageView += message;
  }
  console.info('on message message: ' + JSON.stringify(messageView));
  console.info('remoteInfo: ' + JSON.stringify(value.remoteInfo));
});
```

#### \[h2\]off('message')

off(type: 'message', callback?: Callback<SocketMessageInfo>): void

取消订阅TCPSocket连接的接收消息事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 取消订阅的事件类型。'message'：接收消息事件。 |
| callback | Callback<[SocketMessageInfo](#socketmessageinfo11)\> | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let messageView = '';
let callback = (value: socket.SocketMessageInfo) => {
  for (let i: number = 0; i < value.message.byteLength; i++) {
    let uint8Array = new Uint8Array(value.message)
    let messages = uint8Array[i]
    let message = String.fromCharCode(messages);
    messageView += message;
  }
  console.info('on message message: ' + JSON.stringify(messageView));
  console.info('remoteInfo: ' + JSON.stringify(value.remoteInfo));
}
tcp.on('message', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
tcp.off('message', callback);
tcp.off('message');
```

#### \[h2\]on('connect' | 'close')

on(type: 'connect' | 'close', callback: Callback<void>): void

订阅TCPSocket的连接事件或关闭事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 
订阅的事件类型。

\- 'connect'：连接事件。

\- 'close'：关闭事件。

 |
| callback | Callback<void> | 是 | 回调函数。TCPSocket的连接事件或关闭事件触发时调用回调函数。 |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
tcp.on('connect', () => {
  console.info("on connect success")
});
tcp.on('close', () => {
  console.info("on close success")
});
```

#### \[h2\]off('connect' | 'close')

off(type: 'connect' | 'close', callback?: Callback<void>): void

取消订阅TCPSocket的连接事件或关闭事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 
取消订阅的事件类型。

\- 'connect'：连接事件。

\- 'close'：关闭事件。

 |
| callback | Callback<void> | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let callback1 = () => {
  console.info("on connect success");
}
tcp.on('connect', callback1);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
tcp.off('connect', callback1);
tcp.off('connect');
let callback2 = () => {
  console.info("on close success");
}
tcp.on('close', callback2);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
tcp.off('close', callback2);
tcp.off('close');
```

#### \[h2\]on('error')

on(type: 'error', callback: ErrorCallback): void

订阅TCPSocket连接的error事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅的事件类型。'error'：error事件。 |
| callback | ErrorCallback | 是 | 回调函数。TCPSocket连接订阅的某类error事件触发时调用回调函数。 |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
tcp.on('error', (err: BusinessError) => {
  console.error("on error, err:" + JSON.stringify(err))
});
```

#### \[h2\]off('error')

off(type: 'error', callback?: ErrorCallback): void

取消订阅TCPSocket连接的error事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 取消订阅的事件类型。'error'：error事件。 |
| callback | ErrorCallback | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let callback = (err: BusinessError) => {
  console.error("on error, err:" + JSON.stringify(err));
}
tcp.on('error', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
tcp.off('error', callback);
tcp.off('error');
```

#### TCPConnectOptions

TCPSocket连接的参数。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| address | [NetAddress](#netaddress) | 否 | 否 | 绑定的地址以及端口。 |
| timeout | number | 否 | 是 | 超时时间，单位毫秒（ms）。默认值为5000。 |
| proxy18+ | [ProxyOptions](#proxyoptions18) | 否 | 是 | 使用的代理信息，默认不使用代理。 |

#### TCPSendOptions

TCPSocket发送请求的参数。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| data | string| ArrayBuffer | 否 | 否 | 发送的数据。 |
| encoding | string | 否 | 是 | 字符编码(UTF-8，UTF-16BE，UTF-16LE，UTF-16，US-AECII，ISO-8859-1)，默认为UTF-8。 |

#### TCPExtraOptions

TCPSocket连接的其他属性。继承自[ExtraOptionsBase](#extraoptionsbase)。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| keepAlive | boolean | 否 | 是 | 是否保持连接。默认为false。true：保持连接；false：断开连接。 |
| OOBInline | boolean | 否 | 是 | 是否为OOB内联。默认为false。true：是OOB内联；false：不是OOB内联。 |
| TCPNoDelay | boolean | 否 | 是 | TCPSocket连接是否无时延。默认为false。true：无时延；false：有时延。 |
| socketLinger | {on:boolean, linger:number} | 否 | 是 | 
socket是否继续逗留。

\- on：是否逗留（true：逗留；false：不逗留）。

\- linger：逗留时长，单位毫秒（ms），取值范围为0~65535。

当入参on设置为true时，才需要设置。

 |

#### socket.constructTCPSocketServerInstance10+

constructTCPSocketServerInstance(): TCPSocketServer

创建一个TCPSocketServer对象。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [TCPSocketServer](#tcpsocketserver10) | 返回一个TCPSocketServer对象。 |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
```

#### TCPSocketServer10+

TCPSocketServer连接。在调用TCPSocketServer的方法前，需要先通过[socket.constructTCPSocketServerInstance](#socketconstructtcpsocketserverinstance10)创建TCPSocketServer对象。

#### \[h2\]listen10+

listen(address: NetAddress, callback: AsyncCallback<void>): void

绑定IP地址和端口，端口可以指定或由系统随机分配。监听并接受与此套接字建立的TCPSocket连接。该接口使用多线程并发处理客户端的数据。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/oqNG23fKR9q-BmdxyraNeg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=13EC6AAB0D4FC1E40A41189A4FD13AC23E7452634FB1743DEE49A5F10C95DFE9)

服务端使用该方法完成bind，listen，accept操作，bind方法失败会由系统随机分配端口号。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| address | [NetAddress](#netaddress) | 是 | 目标地址信息。 |
| callback | AsyncCallback<void> | 是 | 回调函数。失败时返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300002 | System internal error. |
| 2303109 | Bad file number. |
| 2303111 | Resource temporarily unavailable. Try again. |
| 2303198 | Address already in use. |
| 2303199 | Cannot assign requested address. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
let listenAddr: socket.NetAddress = {
  address:  '192.168.xx.xxx',
  port: 8080,
  family: 1
}
tcpServer.listen(listenAddr, (err: BusinessError) => {
  if (err) {
    console.error("listen fail");
    return;
  }
  console.info("listen success");
})
```

#### \[h2\]listen10+

listen(address: NetAddress): Promise<void>

绑定IP地址和端口，端口可以指定或由系统随机分配。监听并接受与此套接字建立的TCPSocket连接。该接口使用多线程并发处理客户端的数据。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/lG5tzwQqTtOztVO-6Dn-ZQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=1A0180BF140D13958556B164259DD1061E336A08FA443B7F03FBAE1BD4944EAD)

服务端使用该方法完成bind，listen，accept操作，bind方法失败会由系统随机分配端口号。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| address | [NetAddress](#netaddress) | 是 | 目标地址信息。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300002 | System internal error. |
| 2303109 | Bad file number. |
| 2303111 | Resource temporarily unavailable. Try again. |
| 2303198 | Address already in use. |
| 2303199 | Cannot assign requested address. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
let listenAddr: socket.NetAddress = {
  address:  '192.168.xx.xxx',
  port: 8080,
  family: 1
}
tcpServer.listen(listenAddr).then(() => {
  console.info('listen success');
}).catch((err: BusinessError) => {
  console.error('listen fail');
});
```

#### \[h2\]getState10+

getState(callback: AsyncCallback<SocketStateBase>): void

获取TCPSocketServer状态。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/IzlF3HOJRZWlcncU4wpNHA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=B16544B8634CAC336582805490864C6E73234B9D2D519980D84E7EFCD4651F55)

listen方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[SocketStateBase](#socketstatebase)\> | 是 | 回调函数。失败时返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300002 | System internal error. |
| 2303188 | Socket operation on non-socket. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
let listenAddr: socket.NetAddress = {
  address:  '192.168.xx.xxx',
  port: 8080,
  family: 1
}
tcpServer.listen(listenAddr, (err: BusinessError) => {
  if (err) {
    console.error("listen fail");
    return;
  }
  console.info("listen success");
})
tcpServer.getState((err: BusinessError, data: socket.SocketStateBase) => {
  if (err) {
    console.error('getState fail');
    return;
  }
  console.info('getState success:' + JSON.stringify(data));
})
```

#### \[h2\]getState10+

getState(): Promise<SocketStateBase>

获取TCPSocketServer状态。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/sy9AfoRPTM64ey7SYmr1XA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=2C2DE5994358E8C2C8605409C7F15D570FFE3FDA70B702DEA0D1778277097792)

listen方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[SocketStateBase](#socketstatebase)\> | 以Promise形式返回获取TCPSocket状态的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 2300002 | System internal error. |
| 2303188 | Socket operation on non-socket. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
let listenAddr: socket.NetAddress = {
  address:  '192.168.xx.xxx',
  port: 8080,
  family: 1
}
tcpServer.listen(listenAddr, (err: BusinessError) => {
  if (err) {
    console.error("listen fail");
    return;
  }
  console.info("listen success");
})
tcpServer.getState().then((data: socket.SocketStateBase) => {
  console.info('getState success' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error('getState fail');
});
```

#### \[h2\]getSocketFd23+

getSocketFd(): Promise<number>

获取TCPSocketServer监听端口绑定的文件描述符。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/3ljjs0XHSoiatdA0-mjR2Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=40216E579029F1A7BF9AAA30F2C678B911BD169365560172C8DC865F8BEB3B5B)

-   [listen](#listen10)方法调用成功后，才可调用此方法。多次调用listen时，会获取最新监听端口绑定的文件描述符。
-   监听异常、Socket已关闭（如调用close后）等异常情况下调用本接口会返回-1。
-   文件描述符的生命周期由系统管理，应用可以通过[close](#close20)方法关闭Socket连接，避免直接操作文件描述符进行关闭。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | Promise对象，返回Socket的文件描述符。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
let listenAddr: socket.NetAddress = {
  address:  '192.168.xx.xxx',
  port: 8080,
  family: 1
}
tcpServer.listen(listenAddr).then(() => {
  console.info('listen success');
  tcpServer.getSocketFd().then((fd: number) => {
    console.info(`Socket FD：${fd}`);
  }).catch((err: BusinessError) => {
    console.error(`getSocketFd fail: ${err.message}, errorCode: ${err.code}`);
  });
}).catch((err: BusinessError) => {
  console.error('listen fail');
});
```

#### \[h2\]setExtraOptions10+

setExtraOptions(options: TCPExtraOptions, callback: AsyncCallback<void>): void

设置TCPSocketServer连接的其他属性。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/i6-l-PiZTDqk9q7C_wIFlQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=1B9D9D871D273497E3C78CA5BA841C28307387F6FB583C68393639F1E7B639EB)

listen方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [TCPExtraOptions](#tcpextraoptions) | 是 | TCPSocketServer连接的其他属性。 |
| callback | AsyncCallback<void> | 是 | 回调函数。失败时返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300002 | System internal error. |
| 2303188 | Socket operation on non-socket. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
let listenAddr: socket.NetAddress = {
  address:  '192.168.xx.xxx',
  port: 8080,
  family: 1
}
tcpServer.listen(listenAddr, (err: BusinessError) => {
  if (err) {
    console.error("listen fail");
    return;
  }
  console.info("listen success");
})

interface SocketLinger {
  on: boolean;
  linger: number;
}

let tcpExtraOptions: socket.TCPExtraOptions = {
  keepAlive: true,
  OOBInline: true,
  TCPNoDelay: true,
  socketLinger: { on: true, linger: 10 } as SocketLinger,
  receiveBufferSize: 8192,
  sendBufferSize: 8192,
  reuseAddress: true,
  socketTimeout: 3000
}
tcpServer.setExtraOptions(tcpExtraOptions, (err: BusinessError) => {
  if (err) {
    console.error('setExtraOptions fail');
    return;
  }
  console.info('setExtraOptions success');
});
```

#### \[h2\]setExtraOptions10+

setExtraOptions(options: TCPExtraOptions): Promise<void>

设置TCPSocketServer连接的其他属性。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/cr9xPGS4SHKDhjI3lHJpjw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=B2301757F0230FB8E5C644CD4297FBA8ECB3FD08EFC6C8B785E7788CB51F6160)

listen方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [TCPExtraOptions](#tcpextraoptions) | 是 | TCPSocketServer连接的其他属性。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300002 | System internal error. |
| 2303188 | Socket operation on non-socket. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
let listenAddr: socket.NetAddress = {
  address:  '192.168.xx.xxx',
  port: 8080,
  family: 1
}

interface SocketLinger {
  on: boolean;
  linger: number;
}

tcpServer.listen(listenAddr, (err: BusinessError) => {
  if (err) {
    console.error("listen fail");
    return;
  }
  console.info("listen success");
})

let tcpExtraOptions: socket.TCPExtraOptions = {
  keepAlive: true,
  OOBInline: true,
  TCPNoDelay: true,
  socketLinger: { on: true, linger: 10 } as SocketLinger,
  receiveBufferSize: 8192,
  sendBufferSize: 8192,
  reuseAddress: true,
  socketTimeout: 3000
}
tcpServer.setExtraOptions(tcpExtraOptions).then(() => {
  console.info('setExtraOptions success');
}).catch((err: BusinessError) => {
  console.error('setExtraOptions fail');
});
```

#### \[h2\]getLocalAddress12+

getLocalAddress(): Promise<NetAddress>

获取TCPSocketServer的本地Socket地址。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/ps_6vkzDScWTuqSqmmKpYQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=0CE839310E1A00F835EE8D08C9412C00F6B13E906F9F0C960925317ECF7A350B)

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[NetAddress](#netaddress)\> | 以Promise形式返回获取本地socket地址的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 2300002 | System internal error. |
| 2301009 | Bad file descriptor. |
| 2303188 | Socket operation on non-socket. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
let listenAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080,
  family: 1
}
tcpServer.listen(listenAddr).then(() => {
  tcpServer.getLocalAddress().then((localAddress: socket.NetAddress) => {
    console.info("SUCCESS! Address:" + JSON.stringify(localAddress));
  }).catch((err: BusinessError) => {
    console.error("FerrorAILED! Error:" + JSON.stringify(err));
  })
}).catch((err: BusinessError) => {
  console.error('listen fail');
});
```

#### \[h2\]on('connect')10+

on(type: 'connect', callback: Callback<TCPSocketConnection>): void

订阅TCPSocketServer的连接事件。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/ivlJqLLAQ8q7AqxNIqn2IQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=ECE8869CC75CB8EED30E470683ACD6FEC80470CCB1340D36B2C6284A54509E17)

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅的事件类型。'connect'：连接事件。 |
| callback | Callback<[TCPSocketConnection](#tcpsocketconnection10)\> | 是 | 回调函数。失败时返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();

let listenAddr: socket.NetAddress = {
  address:  '192.168.xx.xxx',
  port: 8080,
  family: 1
}
tcpServer.listen(listenAddr, (err: BusinessError) => {
  if (err) {
    console.error("listen fail");
    return;
  }
  console.info("listen success");
  tcpServer.on('connect', (data: socket.TCPSocketConnection) => {
    console.info(JSON.stringify(data))
  });
})
```

#### \[h2\]off('connect')10+

off(type: 'connect', callback?: Callback<TCPSocketConnection>): void

取消订阅TCPSocketServer的连接事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 取消订阅的事件类型。'connect'：连接事件。 |
| callback | Callback<[TCPSocketConnection](#tcpsocketconnection10)\> | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();

let listenAddr: socket.NetAddress = {
  address:  '192.168.xx.xxx',
  port: 8080,
  family: 1
}
tcpServer.listen(listenAddr, (err: BusinessError) => {
  if (err) {
    console.error("listen fail");
    return;
  }
  console.info("listen success");
  let callback = (data: socket.TCPSocketConnection) => {
    console.info('on connect message: ' + JSON.stringify(data));
  }
  tcpServer.on('connect', callback);
  // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
  tcpServer.off('connect', callback);
  tcpServer.off('connect');
})
```

#### \[h2\]on('error')10+

on(type: 'error', callback: ErrorCallback): void

订阅TCPSocketServer连接的error事件。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/Qg8n1RtdRVWJv1R4l8ReYw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=0928E742FFC37A925ACBDD13108332D0016F52D62F0EC71E98845505DB5C884F)

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅的事件类型。'error'：error事件。 |
| callback | ErrorCallback | 是 | 回调函数。失败时返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();

let listenAddr: socket.NetAddress = {
  address:  '192.168.xx.xxx',
  port: 8080,
  family: 1
}
tcpServer.listen(listenAddr, (err: BusinessError) => {
  if (err) {
    console.error("listen fail");
    return;
  }
  console.info("listen success");
  tcpServer.on('error', (err: BusinessError) => {
    console.error("on error, err:" + JSON.stringify(err))
  });
})
```

#### \[h2\]off('error')10+

off(type: 'error', callback?: ErrorCallback): void

取消订阅TCPSocketServer连接的error事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 取消订阅的事件类型。'error'：error事件。 |
| callback | ErrorCallback | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();

let listenAddr: socket.NetAddress = {
  address:  '192.168.xx.xxx',
  port: 8080,
  family: 1
}
tcpServer.listen(listenAddr, (err: BusinessError) => {
  if (err) {
    console.error("listen fail");
    return;
  }
  console.info("listen success");
  let callback = (err: BusinessError) => {
    console.error("on error, err:" + JSON.stringify(err));
  }
  tcpServer.on('error', callback);
  // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
  tcpServer.off('error', callback);
  tcpServer.off('error');
})
```

#### \[h2\]close20+

close(): Promise<void>

TCPSocketServer停止监听并释放通过[listen](#listen10)方法绑定的端口。若多次调用[listen](#listen10)方法，再调用此方法时会释放TCPSocketServer的所有监听端口。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/0lHwQN__Q3eTt9TCRP7byA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=32F9DA799DD85E3A149AC26E345AFC317DEA0D20BB9AEFA36C821A1A0A635859)

该方法不会关闭已有连接。如需关闭，请调用[TCPSocketConnection](#tcpsocketconnection10)的[close](#close10)方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
let listenAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080,
  family: 1
}
tcpServer.on('connect', (connection: socket.TCPSocketConnection) => {
  console.info("connection clientId: " + connection.clientId);
  // 逻辑处理
  tcpServer.close(); // 停止监听
  connection.close(); // 关闭当前连接
});
tcpServer.listen(listenAddr).then(() => {
  console.info('listen success');
}).catch((err: BusinessError) => {
  console.error('listen fail: ' + err.code);
});
```

#### TCPSocketConnection10+

TCPSocketConnection连接，即TCPSocket客户端与服务端的连接。在调用TCPSocketConnection的方法前，需要先获取TCPSocketConnection对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/V9Aw60TaRiiQmZjCkEh1sw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=DC1A375E36BC808CF5E36CE4404C3E747D905E3E2F2454EDE00F504EE9E7D1A1)

客户端与服务端成功建立连接后，才能通过返回的TCPSocketConnection对象调用相应的接口。

**系统能力**：SystemCapability.Communication.NetStack

#### \[h2\]属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| clientId | number | 否 | 否 | 客户端与TCPSocketServer建立连接的id。 |

#### \[h2\]send10+

send(options: TCPSendOptions, callback: AsyncCallback<void>): void

通过TCPSocketConnection连接发送数据。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/WBM_aE4OQQSAo_ffWNcy4g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=1F2E3D9A9A2FA8D88925F8B05838888B688C29CBE96BA854E371B0C2D9C7350C)

与客户端建立连接后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [TCPSendOptions](#tcpsendoptions) | 是 | TCPSocketConnection发送请求的参数。 |
| callback | AsyncCallback<void> | 是 | 回调函数。失败时返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();

tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
  let tcpSendOption: socket.TCPSendOptions = {
    data: 'Hello, client!'
  }
  client.send(tcpSendOption, () => {
    console.info('send success');
  });
});
```

#### \[h2\]send10+

send(options: TCPSendOptions): Promise<void>

通过TCPSocketConnection连接发送数据。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/nzI-N2UMR0aEr2quvmpwiQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=2B1D4F43AE8E766ABEF26EA68C56E4F91F0E6DBC908BB1EE00BCCF791CB7517E)

与客户端建立连接后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [TCPSendOptions](#tcpsendoptions) | 是 | TCPSocketConnection发送请求的参数。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();

tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
  let tcpSendOption: socket.TCPSendOptions = {
    data: 'Hello, client!'
  }
  client.send(tcpSendOption).then(() => {
    console.info('send success');
  }).catch((err: BusinessError) => {
    console.error('send fail');
  });
});
```

#### \[h2\]close10+

close(callback: AsyncCallback<void>): void

关闭一个与TCPSocket建立的连接。使用callback异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | 是 | 回调函数。失败时返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();

tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
  client.close((err: BusinessError) => {
    if (err) {
      console.error('close fail');
      return;
    }
    console.info('close success');
  });
});
```

#### \[h2\]close10+

close(): Promise<void>

关闭一个与TCPSocket建立的连接。使用Promise异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
  client.close().then(() => {
    console.info('close success');
  }).catch((err: BusinessError) => {
    console.error('close fail');
  });
});
```

#### \[h2\]getRemoteAddress10+

getRemoteAddress(callback: AsyncCallback<NetAddress>): void

获取对端Socket地址。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/BQ_S4IKgRf2a5hLbQOn6nQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=A9BC4A6D2B665C0D3EADF42947E742DFC739111EF578A6ACA73FEEDA6300E433)

与客户端建立连接后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[NetAddress](#netaddress)\> | 是 | 回调函数。失败时返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300002 | System internal error. |
| 2303188 | Socket operation on non-socket. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
  client.getRemoteAddress((err: BusinessError, data: socket.NetAddress) => {
    if (err) {
      console.error('getRemoteAddress fail');
      return;
    }
    console.info('getRemoteAddress success:' + JSON.stringify(data));
  });
});
```

#### \[h2\]getRemoteAddress10+

getRemoteAddress(): Promise<NetAddress>

获取对端Socket地址。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/oOpaqGPWSKWag-J7i3d6Jg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=42B5F2BCD33CB365545309FA360592821F8D671DE3F94D415DF4004B6D9053B9)

与客户端建立连接后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[NetAddress](#netaddress)\> | 以Promise形式返回获取对端socket地址的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 2300002 | System internal error. |
| 2303188 | Socket operation on non-socket. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
  client.getRemoteAddress().then(() => {
    console.info('getRemoteAddress success');
  }).catch((err: BusinessError) => {
    console.error('getRemoteAddress fail');
  });
});
```

#### \[h2\]getLocalAddress12+

getLocalAddress(): Promise<NetAddress>

获取TCPSocketConnection连接的本地Socket地址。使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[NetAddress](#netaddress)\> | 以Promise形式返回获取本地socket地址的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 2300002 | System internal error. |
| 2301009 | Bad file descriptor. |
| 2303188 | Socket operation on non-socket. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
let listenAddr: socket.NetAddress = {
  address: "192.168.xx.xx",
  port: 8080,
  family: 1
}
tcpServer.listen(listenAddr, (err: BusinessError) => {
  let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
  let netAddress: socket.NetAddress = {
    address: "192.168.xx.xx",
    port: 8080
  }
  let options: socket.TCPConnectOptions = {
    address: netAddress,
    timeout: 6000
  }
  tcp.connect(options, (err: BusinessError) => {
    if (err) {
      console.error('connect fail');
      return;
    }
    console.info('connect success!');
  })
  tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
    client.getLocalAddress().then((localAddress: socket.NetAddress) => {
      console.info("Family IP Port: " + JSON.stringify(localAddress));
    }).catch((err: BusinessError) => {
      console.error('Error:' + JSON.stringify(err));
    });
  })
})
```

#### \[h2\]getSocketFd23+

getSocketFd(): Promise<number>

获取TCPSocketConnection连接的文件描述符。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/RPihJ7NNRFO_sVPEZcC_QA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=210EBAB6F4D222DA0192E93A87C594023B773FBCA6EA71E71F1B8E59793B4847)

-   与客户端建立连接后，才可调用此方法。
-   连接断开、Socket已关闭（如调用close后）等异常情况下调用本接口会返回-1。
-   文件描述符的生命周期由系统管理，应用可以通过[close](#close10)方法关闭Socket连接，避免直接操作文件描述符进行关闭。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | Promise对象，返回Socket的文件描述符。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
let listenAddr: socket.NetAddress = {
  address: "192.168.xx.xx",
  port: 8080,
  family: 1
}
tcpServer.listen(listenAddr, (err: BusinessError) => {
  tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
    client.getSocketFd().then((fd: number) => {
      console.info(`Socket FD：${fd}`);
    }).catch((err: BusinessError) => {
      console.error(`getSocketFd fail: ${err.message}, errorCode: ${err.code}`);
    });
  })
}).catch((err: BusinessError) => {
  console.error('listen fail');
});
```

#### \[h2\]on('message')10+

on(type: 'message', callback: Callback<SocketMessageInfo>): void

订阅TCPSocketConnection连接的接收消息事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅的事件类型。'message'：接收消息事件。 |
| callback | Callback<[SocketMessageInfo](#socketmessageinfo11)\> | 是 | 回调函数。失败时返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();

tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
  client.on('message', (value: socket.SocketMessageInfo) => {
    let messageView = '';
    let uint8Array = new Uint8Array(value.message);
    for (let i: number = 0; i < value.message.byteLength; i++) {
      let messages = uint8Array[i];
      let message = String.fromCharCode(messages);
      messageView += message;
    }
    console.info('on message message: ' + JSON.stringify(messageView));
    console.info('remoteInfo: ' + JSON.stringify(value.remoteInfo));
  });
});
```

#### \[h2\]off('message')10+

off(type: 'message', callback?: Callback<SocketMessageInfo>): void

取消订阅TCPSocketConnection连接的接收消息事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 取消订阅的事件类型。'message'：接收消息事件。 |
| callback | Callback<[SocketMessageInfo](#socketmessageinfo11)\> | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
let callback = (value: socket.SocketMessageInfo) => {
  let messageView = '';
  for (let i: number = 0; i < value.message.byteLength; i++) {
    let uint8Array = new Uint8Array(value.message)
    let messages = uint8Array[i]
    let message = String.fromCharCode(messages);
    messageView += message;
  }
  console.info('on message message: ' + JSON.stringify(messageView));
  console.info('remoteInfo: ' + JSON.stringify(value.remoteInfo));
}
tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
  client.on('message', callback);
  // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
  client.off('message', callback);
  client.off('message');
});
```

#### \[h2\]on('close')10+

on(type: 'close', callback: Callback<void>): void

订阅TCPSocketConnection的关闭事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅的事件类型。'close'：关闭事件。 |
| callback | Callback<void> | 是 | 回调函数。失败时返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
  client.on('close', () => {
    console.info("on close success")
  });
});
```

#### \[h2\]off('close')10+

off(type: 'close', callback?: Callback<void>): void

取消订阅TCPSocketConnection的关闭事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 取消订阅的事件类型。'close'：关闭事件。 |
| callback | Callback<void> | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
let callback = () => {
  console.info("on close success");
}
tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
  client.on('close', callback);
  // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
  client.off('close', callback);
  client.off('close');
});
```

#### \[h2\]on('error')10+

on(type: 'error', callback: ErrorCallback): void

订阅TCPSocketConnection连接的error事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅的事件类型。'error'：error事件。 |
| callback | ErrorCallback | 是 | 回调函数。失败时返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
  client.on('error', (err: BusinessError) => {
    console.error("on error, err:" + JSON.stringify(err))
  });
});
```

#### \[h2\]off('error')10+

off(type: 'error', callback?: ErrorCallback): void

取消订阅TCPSocketConnection连接的error事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 取消订阅的事件类型。'error'：error事件。 |
| callback | ErrorCallback | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let callback = (err: BusinessError) => {
  console.error("on error, err:" + JSON.stringify(err));
}
let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
  client.on('error', callback);
  // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
  client.off('error', callback);
  client.off('error');
});
```

#### TCP 错误码说明

TCP 其余错误码映射形式为：2301000 + Linux内核错误码。

错误码的详细介绍参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)。

#### socket.constructLocalSocketInstance11+

constructLocalSocketInstance(): LocalSocket

创建一个LocalSocket对象。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [LocalSocket](#localsocket11) | 返回一个LocalSocket对象。 |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
let client: socket.LocalSocket = socket.constructLocalSocketInstance();
```

#### LocalSocket11+

LocalSocket连接。在调用LocalSocket的方法前，需要先通过[socket.constructLocalSocketInstance](#socketconstructlocalsocketinstance11)创建LocalSocket对象。

#### \[h2\]bind11+

bind(address: LocalAddress): Promise<void>;

绑定本地套接字文件的路径。使用promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/bJXYliX2SWqGthL8nFEV9Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=19BFC7AC41619DCB85B70B3E4312A22AAFDE5116FD025FCCC312520C00917FB4)

bind方法可以使客户端确保有个明确的本地套接字路径，显式的绑定一个本地套接字文件。

bind方法在本地套接字通信中非必须。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| address | [LocalAddress](#localaddress11) | 是 | 本端地址信息，参考[LocalAddress](#localaddress11)。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2301013 | Insufficient permissions. |
| 2301022 | Invalid argument. |
| 2301098 | Address already in use. |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/S-F8Wz8cTaar2eNr5uWeOw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=448B32E2EC87843A3B2EE7AD1EF1CE2FA02F7F16A2535ED3096B72C69EF7BC69)

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance()
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let address : socket.LocalAddress = {
  address: sandboxPath
}
client.bind(address).then(() => {
  console.info('bind success')
}).catch((err: Object) => {
  console.error('failed to bind: ' + JSON.stringify(err))
})
```

#### \[h2\]connect11+

connect(options: LocalConnectOptions): Promise<void>

连接到指定的套接字文件。使用promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/zEOXI5anTKqOiqxcOkDcyw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=55BEE9E64ABA1D1CEDBC7DB4002283455CD9F6E72F0436B44973012F38DE5374)

在没有执行localsocket.bind的情况下，也可以直接调用该接口完成与LocalSocket服务端的连接。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [LocalConnectOptions](#localconnectoptions11) | 是 | LocalSocket连接的参数，参考[LocalConnectOptions](#localconnectoptions11)。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 以Promise形式返回LocalSocket连接服务端的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2301013 | Insufficient permissions. |
| 2301022 | Invalid argument. |
| 2301111 | Connection refused. |
| 2301099 | Cannot assign requested address. |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/M6tADdMYTOG4yr2b8WZpuw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=23489AE858F7AB280EB5213538206BBF8DBB8B03FD115885E896B032758BFC0E)

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let localAddress : socket.LocalAddress = {
  address: sandboxPath
}
let connectOpt: socket.LocalConnectOptions = {
  address: localAddress,
  timeout: 6000
}
client.connect(connectOpt).then(() => {
  console.info('connect success')
}).catch((err: Object) => {
  console.error('connect fail: ' + JSON.stringify(err));
});
```

#### \[h2\]send11+

send(options: LocalSendOptions): Promise<void>

通过LocalSocket连接发送数据。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/hU86SX2cR4G391TWTWGqyg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=29C5B69894DA006E8D47CA74682C3CA73C3C0EE871A2900DDD7585B51E9891E8)

connect方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [LocalSendOptions](#localsendoptions11) | 是 | LocalSocket发送请求的参数，参考[LocalSendOptions](#localsendoptions11)。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2301011 | Operation would block. |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/ZRBPATUwTvus7VZ8ZHFnvw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=88AECBA7D7EAC0EC00396CE2EDC98D2114C63827234339A19C30EBECE37A4FCA)

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance()
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let localAddress : socket.LocalAddress = {
  address: sandboxPath
}
let connectOpt: socket.LocalConnectOptions = {
  address: localAddress,
  timeout: 6000
}
client.connect(connectOpt).then(() => {
  console.info('connect success')
}).catch((err: Object) => {
  console.error('connect failed: ' + JSON.stringify(err))
})
let sendOpt: socket.LocalSendOptions = {
  data: 'Hello world!'
}
client.send(sendOpt).then(() => {
  console.info('send success')
}).catch((err: Object) => {
  console.error('send fail: ' + JSON.stringify(err))
})
```

#### \[h2\]close11+

close(): Promise<void>

关闭LocalSocket连接。使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 2301009 | Bad file descriptor. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();

client.close().then(() => {
  console.info('close success');
}).catch((err: Object) => {
  console.error('close fail: ' + JSON.stringify(err));
});
```

#### \[h2\]getState11+

getState(): Promise<SocketStateBase>

获取LocalSocket状态。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/qkT-x0TdT-m_oX7-y4aqfg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=455D2FCED2AFD9A37A205C6A849797B8BD289A47306B0787B04AD977D96DD258)

bind或connect方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[SocketStateBase](#socketstatebase)\> | 以Promise形式返回获取LocalSocket状态的结果。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/0Tk3u04zQPmrFx3aZe3sLQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=0530F853D210CBC6E3F30874DFF5ADF1E70034B91B2603FF816986C4572F6BE1)

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let localAddress : socket.LocalAddress = {
  address: sandboxPath
}
let connectOpt: socket.LocalConnectOptions = {
  address: localAddress,
  timeout: 6000
}
client.connect(connectOpt).then(() => {
  console.info('connect success');
  client.getState().then(() => {
    console.info('getState success');
  }).catch((err: Object) => {
    console.error('getState fail: ' + JSON.stringify(err))
  });
}).catch((err: Object) => {
  console.error('connect fail: ' + JSON.stringify(err));
});
```

#### \[h2\]getSocketFd11+

getSocketFd(): Promise<number>

获取LocalSocket的文件描述符。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/WCBohoY8SEm3PhKkSEhkXw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=718F58C49EEFC4F77C4D17A4ED2785811C51588646DA72EE3FAF2814BB9655D2)

-   bind或connect方法调用成功后，才可调用此方法。
-   获取由系统内核分配的唯一文件描述符，用于标识当前使用的套接字。
-   文件描述符的生命周期由系统管理，应用可以通过[close](#close11)方法关闭Socket连接，避免直接操作文件描述符进行关闭。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | 以Promise形式返回socket的文件描述符。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/DOJOuT0sSGOIqKEE0STuTw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=DE0C21056E45801357911171DF4C95AEEC586F32D048E74FEF4F90DFF234E18E)

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let localAddress : socket.LocalAddress = {
  address: sandboxPath
}
let connectOpt: socket.LocalConnectOptions = {
  address: localAddress,
  timeout: 6000
}
client.connect(connectOpt).then(() => {
  console.info('connect ok')
}).catch((err: Object) => {
  console.error('connect fail: ' + JSON.stringify(err))
})
client.getSocketFd().then((data: number) => {
  console.info("fd: " + data);
}).catch((err: Object) => {
  console.error("getSocketFd failed: " + JSON.stringify(err));
})
```

#### \[h2\]setExtraOptions11+

setExtraOptions(options: ExtraOptionsBase): Promise<void>

设置LocalSocket的套接字属性。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/9_hGmzKfQku9bo651lq7Ng/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=3FD8B90B510A91291296F8FEFA11B0403FB4E26B735C04F60596A344F16E0E67)

bind或connect方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [ExtraOptionsBase](#extraoptionsbase) | 是 | LocalSocket连接的其他属性，参考[ExtraOptionsBase](#extraoptionsbase)。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 以Promise形式返回设置LocalSocket套接字属性的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2301009 | Bad file descriptor. |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/Bbu7CQKySk2Peshf_1cKYg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=8DDBEBB115E2B9C1C40B21D84FA9956EC0DF4F0788412EAB09A3069BC3A1C617)

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let localAddress : socket.LocalAddress = {
  address: sandboxPath
}
let connectOpt: socket.LocalConnectOptions = {
  address: localAddress,
  timeout: 6000
}
client.connect(connectOpt).then(() => {
  console.info('connect success');
  let options: socket.ExtraOptionsBase = {
    receiveBufferSize: 8192,
    sendBufferSize: 8192,
    socketTimeout: 3000
  }
  client.setExtraOptions(options).then(() => {
    console.info('setExtraOptions success');
  }).catch((err: Object) => {
    console.error('setExtraOptions fail: ' + JSON.stringify(err));
  });
}).catch((err: Object) => {
  console.error('connect fail: ' + JSON.stringify(err));
});
```

#### \[h2\]getExtraOptions11+

getExtraOptions(): Promise<ExtraOptionsBase>;

获取LocalSocket的套接字属性。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/X8mWexvQSqCVf8RKJOASTQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=47159100EF94D157CCA3B41AC6EF267C8B3800A03ADE1EF3A7AD0D9EB966A8FA)

bind或connect方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[ExtraOptionsBase](#extraoptionsbase)\> | 以Promise形式返回设置LocalSocket套接字的属性。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 2301009 | Bad file descriptor. |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/yK8sF7F6RhKjUqqM0FH1Ag/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=42A419CA7ECB77626FC23BD3745C3FB372E983BA57307D66E39BCEF6BAE16DEF)

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let localAddress : socket.LocalAddress = {
  address: sandboxPath
}
let connectOpt: socket.LocalConnectOptions = {
  address: localAddress,
  timeout: 6000
}
client.connect(connectOpt).then(() => {
  console.info('connect success');
  client.getExtraOptions().then((options : socket.ExtraOptionsBase) => {
    console.info('options: ' + JSON.stringify(options));
  }).catch((err: Object) => {
    console.error('setExtraOptions fail: ' + JSON.stringify(err));
  });
}).catch((err: Object) => {
  console.error('connect fail: ' + JSON.stringify(err));
});
```

#### \[h2\]getLocalAddress12+

getLocalAddress(): Promise<string>

获取LocalSocket的本地Socket地址。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/azQ2ZJtJSNW9kNz0euzGDw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=C81A234330557071D08F385E8A9954792DC91F6CE2E3979D1C98C2F6D1065034)

bind方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | 以Promise形式返回获取本地socket地址的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 2300002 | System internal error. |
| 2301009 | Bad file descriptor. |
| 2303188 | Socket operation on non-socket. |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/pQjCXQzrS6GdpPPgCwa59Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=C35CBCD84EA0F44827223375400AB3213471ED9826D08016AAEAD98B196621CE)

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
import { common } from '@kit.AbilityKit';
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let address : socket.LocalAddress = {
  address: sandboxPath
}
client.bind(address).then(() => {
  console.error('bind success');
  client.getLocalAddress().then((localPath: string) => {
    console.info("SUCCESS " + JSON.stringify(localPath));
  }).catch((err: BusinessError) => {
    console.error("FAIL " + JSON.stringify(err));
  })
}).catch((err: Object) => {
  console.error('failed to bind: ' + JSON.stringify(err));
})
```

#### \[h2\]on('message')11+

on(type: 'message', callback: Callback<LocalSocketMessageInfo>): void

订阅LocalSocket连接的接收消息事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅的事件类型。'message'：接收消息事件。 |
| callback | Callback<[LocalSocketMessageInfo](#localsocketmessageinfo11)\> | 是 | 以callback的形式异步返回接收的消息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
client.on('message', (value: socket.LocalSocketMessageInfo) => {
  const uintArray = new Uint8Array(value.message)
  let messageView = '';
  for (let i = 0; i < uintArray.length; i++) {
    messageView += String.fromCharCode(uintArray[i]);
  }
  console.info('total: ' + JSON.stringify(value));
  console.info('message information: ' + messageView);
});
```

#### \[h2\]off('message')11+

off(type: 'message', callback?: Callback<LocalSocketMessageInfo>): void

取消订阅LocalSocket连接的接收消息事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 取消订阅的事件类型。'message'：接收消息事件。 |
| callback | Callback<[LocalSocketMessageInfo](#localsocketmessageinfo11)\> | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
let messageView = '';
let callback = (value: socket.LocalSocketMessageInfo) => {
  const uintArray = new Uint8Array(value.message)
  let messageView = '';
  for (let i = 0; i < uintArray.length; i++) {
    messageView += String.fromCharCode(uintArray[i]);
  }
  console.info('total: ' + JSON.stringify(value));
  console.info('message information: ' + messageView);
}
client.on('message', callback);
client.off('message');
```

#### \[h2\]on('connect')11+

on(type: 'connect', callback: Callback<void>): void

订阅LocalSocket的连接事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅的事件类型。 |
| callback | Callback<void> | 是 | 以callback的形式异步返回与服务端连接的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
client.on('connect', () => {
  console.info("on connect success")
});
```

#### \[h2\]off('connect')11+

off(type: 'connect', callback?: Callback<void>): void

取消订阅LocalSocket的连接事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 取消订阅的事件类型。'connect'：LocalSocket的connect事件。 |
| callback | Callback<void> | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
let callback = () => {
  console.info("on connect success");
}
client.on('connect', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
client.off('connect', callback);
client.off('connect');
```

#### \[h2\]on('close')11+

on(type: 'close', callback: Callback<void>): void

订阅LocalSocket的关闭事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅LocalSocket的关闭事件。 |
| callback | Callback<void> | 是 | 以callback的形式异步返回关闭localsocket的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
let callback = () => {
  console.info("on close success");
}
client.on('close', callback);
```

#### \[h2\]off('close')11+

off(type: 'close', callback?: Callback<void>): void

取消订阅LocalSocket的关闭事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 取消订阅的事件类型。'close'：LocalSocket的关闭事件。 |
| callback | Callback<void> | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
let callback = () => {
  console.info("on close success");
}
client.on('close', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
client.off('close', callback);
client.off('close');
```

#### \[h2\]on('error')11+

on(type: 'error', callback: ErrorCallback): void

订阅LocalSocket连接的error事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅LocalSocket的error事件。 |
| callback | ErrorCallback | 是 | 以callback的形式异步返回出现错误的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
client.on('error', (err: Object) => {
  console.error("on error, err:" + JSON.stringify(err))
});
```

#### \[h2\]off('error')11+

off(type: 'error', callback?: ErrorCallback): void

取消订阅LocalSocket连接的error事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 取消订阅的事件类型。'error'：LocalSocket的error事件。 |
| callback | ErrorCallback | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';

let client: socket.LocalSocket = socket.constructLocalSocketInstance();
let callback = (err: Object) => {
  console.error("on error, err:" + JSON.stringify(err));
}
client.on('error', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
client.off('error', callback);
client.off('error');
```

#### LocalSocketMessageInfo11+

LocalSocket客户端与服务端通信时接收的数据。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| message | ArrayBuffer | 否 | 否 | 收到的消息数据。 |
| address | string | 否 | 否 | 使用的本地套接字路径。 |
| size | number | 否 | 否 | 数据长度。 |

#### LocalAddress11+

LocalSocket本地套接字文件路径信息，在传入套接字路径进行绑定时，会在此路径下创建套接字文件。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| address | string | 否 | 否 | 本地套接字路径。 |

#### LocalConnectOptions11+

LocalSocket客户端在连接服务端时传入的参数信息。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| address | [LocalAddress](#localaddress11) | 否 | 否 | 指定的本地套接字路径。 |
| timeout | number | 否 | 是 | 连接服务端的超时时间，单位为毫秒。默认值为0。需要应用手动设置一下，建议设置为5000。 |

#### LocalSendOptions11+

LocalSocket发送请求的参数。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| data | string | ArrayBuffer | 否 | 否 | 需要发送的数据。 |
| encoding | string | 否 | 是 | 字符编码。 |

#### ExtraOptionsBase

Socket套接字的基础属性。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| receiveBufferSize | number | 否 | 是 | 接收缓冲区大小（单位：Byte），取值范围0~262144，不设置或设置的值超过取值范围则会默认为8192。 |
| sendBufferSize | number | 否 | 是 | 发送缓冲区大小（单位：Byte），取值范围0~262144，不设置或设置的值超过取值范围则会默认为8192。 |
| reuseAddress | boolean | 否 | 是 | 是否重用地址。true：重用地址；false：不重用地址。 |
| socketTimeout | number | 否 | 是 | 套接字超时时间，单位毫秒（ms）。 |

#### socket.constructLocalSocketServerInstance11+

constructLocalSocketServerInstance(): LocalSocketServer

创建一个LocalSocketServer对象。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [LocalSocketServer](#localsocketserver11) | 返回一个LocalSocketServer对象。 |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
```

#### LocalSocketServer11+

LocalSocketServer类。在调用LocalSocketServer的方法前，需要先通过[socket.constructLocalSocketServerInstance](#socketconstructlocalsocketserverinstance11)创建LocalSocketServer对象。

#### \[h2\]listen11+

listen(address: LocalAddress): Promise<void>

绑定本地套接字文件，监听并接受与此套接字建立的LocalSocket连接。该接口使用多线程并发处理客户端的数据。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/_Zni3dPlRt-VVJCgXKD6Fw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=F2CD2832823D5CC8594A6F618CE695E3BB2785FDBB8FBC52B242963C9A741564)

服务端使用该方法完成bind，listen，accept操作，传入套接字文件路径，调用此接口后会自动生成本地套接字文件。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| address | [LocalAddress](#localaddress11) | 是 | 目标地址信息。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 以Promise形式返回执行结果， 成功返回空，失败返回错误码错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2303109 | Bad file number. |
| 2301013 | Insufficient permissions. |
| 2301022 | Invalid argument. |
| 2301098 | Address already in use. |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/rZlkr1zJSiO8L98dHH9qpg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=1C2FE15085CF0B973137AD63C6131637B58B8FF8C9236F1468A00178A921E69F)

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let addr: socket.LocalAddress = {
  address: sandboxPath
}
server.listen(addr).then(() => {
  console.info('listen success');
}).catch((err: Object) => {
  console.error('listen fail: ' + JSON.stringify(err));
});
```

#### \[h2\]getState11+

getState(): Promise<SocketStateBase>

获取LocalSocketServer状态。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/dEd4z9NXSAKOFoGIcBKejA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=3CE0CE94911A5C68D0A9BD9B8FDE88B667B21A23F35C1BF23F149C68EF38577A)

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[SocketStateBase](#socketstatebase)\> | 以Promise形式返回获取LocalSocketServer状态的结果。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/ndooC5x6Tve2aL7K_Sdo2w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=4DECC53924DA5AF39A639D9FF1F91D16F9C5C028F9C7994DB6FDA0D3C05BF8D1)

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let listenAddr: socket.LocalAddress = {
  address: sandboxPath
}
server.listen(listenAddr).then(() => {
  console.info("listen success");
}).catch((err: Object) => {
  console.error("listen fail: " + JSON.stringify(err));
})
server.getState().then((data: socket.SocketStateBase) => {
  console.info('getState success: ' + JSON.stringify(data));
}).catch((err: Object) => {
  console.error('getState fail: ' + JSON.stringify(err));
});
```

#### \[h2\]setExtraOptions11+

setExtraOptions(options: ExtraOptionsBase): Promise<void>

设置LocalSocketServer连接的套接字属性。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/vvXW4p7DTF28Yh5YaQXqBw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=4C84C6F222CE0ED9F408BEB0C5B72B5F22F2D78C9F1D04151F73CF9BAF351B1D)

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [ExtraOptionsBase](#extraoptionsbase) | 是 | LocalSocketServer连接的其他属性。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2301009 | Bad file descriptor. |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/f1pBDpFjSrGxLcjP32JZQg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=471BFD77C0E4CCF5D8D7D69FB14B681C64F40B05F3FD17C7F7A0A814F7FD3A0B)

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let listenAddr: socket.NetAddress = {
  address: sandboxPath
}
server.listen(listenAddr).then(() => {
  console.info("listen success");
}).catch((err: Object) => {
  console.error("listen fail: " + JSON.stringify(err));
})

let options: socket.ExtraOptionsBase = {
  receiveBufferSize: 8192,
  sendBufferSize: 8192,
  socketTimeout: 3000
}
server.setExtraOptions(options).then(() => {
  console.info('setExtraOptions success');
}).catch((err: Object) => {
  console.error('setExtraOptions fail: ' + JSON.stringify(err));
});
```

#### \[h2\]getExtraOptions11+

getExtraOptions(): Promise<ExtraOptionsBase>;

获取LocalSocketServer中连接的套接字的属性。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/UUhmTpnUSuKikyAW-t2P0A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=192EF3E51EBD8C3528B5DD6E99E0F4F286EBB2527A0E457512B4E5A03A2F7467)

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[ExtraOptionsBase](#extraoptionsbase)\> | 以Promise形式返回套接字的属性。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/u35H4JxtRzewpIu52Qt8Mg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=235C98FFCF25589EAC5CD23190C52D230768E28E5CBAD0BA30C26929DBD229FB)

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let listenAddr: socket.LocalAddress = {
  address: sandboxPath
}
server.listen(listenAddr).then(() => {
  console.info("listen success");
}).catch((err: Object) => {
  console.error("listen fail: " + JSON.stringify(err));
})
server.getExtraOptions().then((options: socket.ExtraOptionsBase) => {
  console.info('options: ' + JSON.stringify(options));
}).catch((err: Object) => {
  console.error('getExtraOptions fail: ' + JSON.stringify(err));
});
```

#### \[h2\]getLocalAddress12+

getLocalAddress(): Promise<string>

获取LocalSocketServer中本地Socket地址。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/8SKPbwOsS9-xIzF7YVKyRw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=E8BA33F080AF2E980F1A2D7E3342727BD9DE0F6B858B990472998AD76BDCA6C0)

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | 以Promise形式返回获取本地socket地址的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 2300002 | System internal error. |
| 2301009 | Bad file descriptor. |
| 2303188 | Socket operation on non-socket. |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/LVt3DRg3RKug-qRtRFow-A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=B35E981E8F0E9468ACF8CE7B91F65FE855D58AC8C22D41B267CC874CAD97FED5)

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
import { common } from '@kit.AbilityKit';
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let listenAddr: socket.LocalAddress = {
  address: sandboxPath
}
server.listen(listenAddr).then(() => {
  console.info("listen success");
  server.getLocalAddress().then((localPath: string) => {
    console.info("SUCCESS " + JSON.stringify(localPath));
  }).catch((err: BusinessError) => {
    console.error("FAIL " + JSON.stringify(err));
  })
}).catch((err: Object) => {
  console.error("listen fail: " + JSON.stringify(err));
})
```

#### \[h2\]getSocketFd23+

getSocketFd(): Promise<number>

获取LocalSocketServer监听端口绑定的文件描述符。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/xHwYGsjmQ02h8j2U7fCz1A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=97B38E91F585F0372C434CF72B4AD955A7E5D24BC25D417EEC6631B7F83235E1)

-   [listen](#listen11)方法调用成功后，才可调用此方法。
-   监听异常、Socket已关闭（如调用close后）等异常情况下调用本接口会返回-1。
-   文件描述符的生命周期由系统管理，应用可以通过[close](#close20-1)方法关闭Socket连接，避免直接操作文件描述符进行关闭。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | Promise对象，返回Socket的文件描述符。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/nTcuqPj7TgqMOlf-pZQQoQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=BD8196A0DB03117BDEE9326EE6146FAC9ABB2EB01B23D06197819376B6F15CD1)

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let listenAddr : socket.LocalAddress = {
  address: sandboxPath
}

server.listen(listenAddr).then(() => {
  console.info("listen success");
  server.getSocketFd().then((fd: number) => {
    console.info(`Socket FD：${fd}`);
  }).catch((err: Object) => {
    console.error(`getSocketFd fail: ${JSON.stringify(err)}`);
  });
}).catch((err: Object) => {
  console.error("listen fail: " + JSON.stringify(err));
})
```

#### \[h2\]on('connect')11+

on(type: 'connect', callback: Callback<LocalSocketConnection>): void

订阅LocalSocketServer的连接事件。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/1IfKdtw2QCmpuOLeS63eMA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=589025A6ABC6F443B0149ED76C042DC0D004FAC20E2A9E20AE553E472BEC6B0F)

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅的事件类型。'connect'：连接事件。 |
| callback | Callback<[LocalSocketConnection](#localsocketconnection11)\> | 是 | 以callback的形式异步返回接收到客户端连接的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
server.on('connect', (connection: socket.LocalSocketConnection) => {
  if (connection) {
    console.info('accept a client')
  }
});
```

#### \[h2\]off('connect')11+

off(type: 'connect', callback?: Callback<LocalSocketConnection>): void

取消订阅LocalSocketServer的连接事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 取消订阅的事件类型。'connect'：LocalSocketServer的连接事件。 |
| callback | Callback<[LocalSocketConnection](#localsocketconnection11)\> | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
let callback = (connection: socket.LocalSocketConnection) => {
  if (connection) {
    console.info('accept a client')
  }
}
server.on('connect', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
server.off('connect', callback);
server.off('connect');
```

#### \[h2\]on('error')11+

on(type: 'error', callback: ErrorCallback): void

订阅LocalSocketServer连接的error事件。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/zTCoXZqASdiYK8uDx0McmQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=4586DED05ACF03026858B9B5C430363154F39A44EF34FF65B9BE64A6DE83B10E)

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅的事件类型。'error'：error事件。 |
| callback | ErrorCallback | 是 | 以callback的形式异步返回出现错误的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
server.on('error', (err: Object) => {
  console.error("on error, err:" + JSON.stringify(err))
});
```

#### \[h2\]off('error')11+

off(type: 'error', callback?: ErrorCallback): void

取消订阅LocalSocketServer连接的error事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 取消订阅的事件类型。'error'：error事件。 |
| callback | ErrorCallback | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
let callback = (err: Object) => {
  console.error("on error, err:" + JSON.stringify(err));
}
server.on('error', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
server.off('error', callback);
server.off('error');
```

#### \[h2\]close20+

close(): Promise<void>

LocalSocketServer停止监听并释放通过[listen](#listen11)方法绑定的监听端口。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/5dfBMXoQQ4SCrh_TNMZ41g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=F12CC7B3871DBC16177C60123467F69F89BA98ADBEAE009BEFEBB3F8C86DAC78)

该方法不会关闭已有连接。如需关闭，请调用[LocalSocketConnection](#localsocketconnection11)的[close](#close11-1)方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 2300002 | System internal error. |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/W_yKvSOBQIm1EPRHNFiEiQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=40B160DA1B8006D64F76B7EAF1173003A8E356CB81BABC71D6E29369198C561E)

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let localserver: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let addr: socket.LocalAddress = {
  address: sandboxPath
}
localserver.on('connect', (connection: socket.LocalSocketConnection) => {
  console.info("connection clientId: " + connection.clientId);
  // 逻辑处理
  localserver.close(); // 停止监听
  connection.close(); // 关闭当前连接
});
localserver.listen(addr).then(() => {
  console.info('listen success');
}).catch((err: BusinessError) => {
  console.error('listen fail: ' + err.code);
});
```

#### LocalSocketConnection11+

LocalSocketConnection连接，即LocalSocket客户端与服务端的会话连接。在调用LocalSocketConnection的方法前，需要先获取LocalSocketConnection对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/3RV9I5xqQeShOWuq6VVioA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=77803F8D19E18F8EFEF9D6F31DA4E6B69F51456BC41B20E02AFB0A6710B3033C)

客户端与服务端成功建立连接后，才能通过返回的LocalSocketConnection对象调用相应的接口。

**系统能力**：SystemCapability.Communication.NetStack

#### \[h2\]属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| clientId | number | 否 | 否 | 客户端与服务端建立的会话连接的id。 |

#### \[h2\]send11+

send(options: LocalSendOptions): Promise<void>

通过LocalSocketConnection连接对象发送数据。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/TeHhuUluSrusv2lQgqC37g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=5E1F0A733452F6CC8D8D757B7E38B67F5E4AAD396860684E04C3B8EDF006ECB5)

服务端与客户端建立连接后，服务端通过connect事件回调得到LocalSocketConnection连接对象后，才可使用连接对象调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [LocalSendOptions](#localsendoptions11) | 是 | LocalSocketConnection发送请求的参数。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2301011 | Operation would block. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();

server.on('connect', (connection: socket.LocalSocketConnection) => {
  let sendOptions: socket.LocalSendOptions = {
    data: 'Hello, client!'
  }
  connection.send(sendOptions).then(() => {
    console.info('send success');
  }).catch((err: Object) => {
    console.error('send fail: ' + JSON.stringify(err));
  });
});
```

#### \[h2\]close11+

close(): Promise<void>

关闭一个LocalSocket客户端与服务端建立的连接。使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 2301009 | Bad file descriptor. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
server.on('connect', (connection: socket.LocalSocketConnection) => {
  connection.close().then(() => {
    console.info('close success');
  }).catch((err: Object) => {
    console.error('close fail: ' + JSON.stringify(err));
  });
});
```

#### \[h2\]getLocalAddress12+

getLocalAddress(): Promise<string>

获取LocalSocketConnection连接中的本地Socket地址。使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | 以Promise形式返回获取本地socket地址的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 2300002 | System internal error. |
| 2301009 | Bad file descriptor. |
| 2303188 | Socket operation on non-socket. |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/TH5JXdn2SG-k3PTWGDYckA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=90DFA36AA42DE36A36A95EFEF18E5E259E32C476A5D96159B46504B8695DAAB2)

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
import { common } from '@kit.AbilityKit';
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let localAddr: socket.LocalAddress = {
  address: sandboxPath
}
server.listen(localAddr).then(() => {
  console.info('listen success');
  let client: socket.LocalSocket = socket.constructLocalSocketInstance();
  let connectOpt: socket.LocalConnectOptions = {
    address: localAddr,
    timeout: 6000
  }
  client.connect(connectOpt).then(() => {
    server.getLocalAddress().then((localPath: string) => {
      console.info("success, localPath is" + JSON.stringify(localPath));
    }).catch((err: BusinessError) => {
      console.error("FAIL " + JSON.stringify(err));
    })
  }).catch((err: Object) => {
    console.error('connect fail: ' + JSON.stringify(err));
  });
});
```

#### \[h2\]getSocketFd23+

getSocketFd(): Promise<number>

获取LocalSocketConnection连接的文件描述符。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/YMNQJIU0Rfi5_gH0Y4OkPw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=5756A6EAE4A6E48146FDF19D4CCCABF6BB1301033830216F532E7C0765639D1D)

-   成功建立连接后，才可调用此方法。
-   连接断开、Socket已关闭（如调用close后）等异常情况下调用本接口会返回-1。
-   文件描述符的生命周期由系统管理，应用可以通过[close](#close11-1)方法关闭Socket连接，避免直接操作文件描述符进行关闭。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | Promise对象，返回Socket的文件描述符。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/0oFLrBDKSo67AUoh6LHSOQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=7B76BF26DC654CF3DCD3563BE34E015994EE6F9A826465E9CCB008571F0080B9)

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let listenAddr : socket.LocalAddress = {
  address: sandboxPath
}
server.on('connect', (connection: socket.LocalSocketConnection) => {
  connection.getSocketFd().then((fd: number) => {
    console.info(`Socket FD：${fd}`);
  }).catch((err: Object) => {
    console.error(`getSocketFd fail: ${JSON.stringify(err)}`);
  });
});
server.listen(listenAddr).then(() => {
  console.info("listen success");
}).catch((err: Object) => {
  console.error(`listen fail: ${JSON.stringify(err)}`);
})
```

#### \[h2\]on('message')11+

on(type: 'message', callback: Callback<LocalSocketMessageInfo>): void

订阅LocalSocketConnection连接的接收消息事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅的事件类型。'message'：接收消息事件。 |
| callback | Callback<[LocalSocketMessageInfo](#localsocketmessageinfo11)\> | 是 | 以callback的形式异步返回接收到的来自客户端的消息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/STJA3mIDT1mXy2I6CrojZw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=BCD1850D9C62546F582BC239956C7C4E7878E9956ADC2ABF3950D0B0B547D689)

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let sandboxPath: string = context.filesDir + '/testSocket';
let listenAddr: socket.LocalAddress = {
  address: sandboxPath
}
server.listen(listenAddr).then(() => {
  console.info("listen success");
}).catch((err: Object) => {
  console.error("listen fail: " + JSON.stringify(err));
});
server.on('connect', (connection: socket.LocalSocketConnection) => {
  connection.on('message', (value: socket.LocalSocketMessageInfo) => {
    const uintArray = new Uint8Array(value.message);
    let messageView = '';
    for (let i = 0; i < uintArray.length; i++) {
      messageView += String.fromCharCode(uintArray[i]);
    }
    console.info('total: ' + JSON.stringify(value));
    console.info('message information: ' + messageView);
  });
});
```

#### \[h2\]off('message')11+

off(type: 'message', callback?: Callback<LocalSocketMessageInfo>): void

取消订阅LocalSocketConnection连接的接收消息事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 取消订阅的事件类型。'message'：接收消息事件。 |
| callback | Callback<[LocalSocketMessageInfo](#localsocketmessageinfo11)\> | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
let callback = (value: socket.LocalSocketMessageInfo) => {
  const uintArray = new Uint8Array(value.message)
  let messageView = '';
  for (let i = 0; i < uintArray.length; i++) {
    messageView += String.fromCharCode(uintArray[i]);
  }
  console.info('total: ' + JSON.stringify(value));
  console.info('message information: ' + messageView);
}
server.on('connect', (connection: socket.LocalSocketConnection) => {
  connection.on('message', callback);
  // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
  connection.off('message', callback);
  connection.off('message');
});
```

#### \[h2\]on('close')11+

on(type: 'close', callback: Callback<void>): void

订阅LocalSocketConnection的关闭事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅的事件类型。'close'：关闭事件。 |
| callback | Callback<void> | 是 | 以callback的形式异步返回会话关闭的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
server.on('connect', (connection: socket.LocalSocketConnection) => {
  connection.on('close', () => {
    console.info("on close success")
  });
});
```

#### \[h2\]off('close')11+

off(type: 'close', callback?: Callback<void>): void

取消订阅LocalSocketConnection的关闭事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 取消订阅的事件类型。'close'：关闭事件。 |
| callback | Callback<void> | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
let callback = () => {
  console.info("on close success");
}
server.on('connect', (connection: socket.LocalSocketConnection) => {
  connection.on('close', callback);
  // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
  connection.off('close', callback);
  connection.off('close');
});
```

#### \[h2\]on('error')11+

on(type: 'error', callback: ErrorCallback): void

订阅LocalSocketConnection连接的error事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅的事件类型。'error'：error事件。 |
| callback | ErrorCallback | 是 | 以callback的形式异步返回出现错误的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';

let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
server.on('connect', (connection: socket.LocalSocketConnection) => {
  connection.on('error', (err: Object) => {
    console.error("on error, err:" + JSON.stringify(err))
  });
});
```

#### \[h2\]off('error')11+

off(type: 'error', callback?: ErrorCallback): void

取消订阅LocalSocketConnection连接的error事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 取消订阅的事件类型。'error'：error事件。 |
| callback | ErrorCallback | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';

let callback = (err: Object) => {
  console.error("on error, err: " + JSON.stringify(err));
}
let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
server.on('connect', (connection: socket.LocalSocketConnection) => {
  connection.on('error', callback);
  // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
  connection.off('error', callback);
  connection.off('error');
});
```

#### LocalSocket 错误码说明

LocalSocket 错误码映射形式为：2301000 + Linux内核错误码。

错误码的详细介绍参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)。

#### socket.constructTLSSocketInstance9+

constructTLSSocketInstance(): TLSSocket

创建并返回一个TLSSocket对象。

**系统能力**：SystemCapability.Communication.NetStack

**返回值:**

| 类型 | 说明 |
| :-- | :-- |
| [TLSSocket](#tlssocket9) | 返回一个TLSSocket对象。 |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
```

#### socket.constructTLSSocketInstance12+

constructTLSSocketInstance(tcpSocket: TCPSocket): TLSSocket

将TCPSocket升级为TLSSocket，创建并返回一个TLSSocket对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/paOhTcnnTbOk6yDic1QH3g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=653D682FC79A191BF8998C25A1A8043A5EB11316205D397AD1D37FDE750FEAA1)

需要确保TCPSocket已连接，并且当前已经没有传输数据，再调用constructTLSSocketInstance升级TLSSocket。当升级成功后，无需对TCPSocket对象调用close方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| tcpSocket | [TCPSocket](#tcpsocket) | 是 | 需要进行升级的TCPSocket对象。 |

**返回值:**

| 类型 | 说明 |
| :-- | :-- |
| [TLSSocket](#tlssocket9) | 返回一个TLSSocket对象。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2300002 | System internal error. |
| 2303601 | Invalid socket FD. |
| 2303602 | Socket is not connected. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tcpconnectoptions: socket.TCPConnectOptions = {
  address: netAddress,
  timeout: 6000
}

tcp.connect(tcpconnectoptions, (err: BusinessError) => {
  if (err) {
    console.error('connect fail');
    return;
  }
  console.info('connect success');

  // 确保TCPSocket已连接后，再升级TLSSocket
  let tls: socket.TLSSocket = socket.constructTLSSocketInstance(tcp);
})
```

#### TLSSocket9+

TLSSocket连接。在调用TLSSocket的方法前，需要先通过[socket.constructTLSSocketInstance](#socketconstructtlssocketinstance9)创建TLSSocket对象。

#### \[h2\]bind9+

bind(address: NetAddress, callback: AsyncCallback<void>): void

绑定IP地址和端口。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/vmup0eZwTe6auujwi12ahA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=9735978446D82B0F26ABD1923F00683E496831FB846F5544F3A03C8D6AB9CF03)

如果TLSSocket对象是通过TCPSocket对象升级创建的，可以不用执行bind方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| address | [NetAddress](#netaddress) | 是 | 本端地址信息，参考[NetAddress](#netaddress)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。成功返回TLSSocket绑定本机的IP地址和端口的结果。失败返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2303198 | Address already in use. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
tls.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
```

#### \[h2\]bind9+

bind(address: NetAddress): Promise<void>

绑定IP地址和端口。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/jEB9uEzNRP-Dd__QQ79h_Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=24E1650A56CDC05788143A9917BFC02B5B32BB6A53BED02245A6C9282D6C0114)

如果TLSSocket对象是通过TCPSocket对象升级创建的，可以不用执行bind方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| address | [NetAddress](#netaddress) | 是 | 本端地址信息，参考[NetAddress](#netaddress)。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 以Promise形式返回TLSSocket绑定本机的IP地址和端口的结果。失败返回错误码，错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2303198 | Address already in use. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
tls.bind(bindAddr).then(() => {
  console.info('bind success');
}).catch((err: BusinessError) => {
  console.error('bind fail');
});
```

#### \[h2\]getState9+

getState(callback: AsyncCallback<SocketStateBase>): void

在TLSSocket的bind成功之后，获取TLSSocket状态。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[SocketStateBase](#socketstatebase)\> | 是 | 回调函数。成功返回TLSSocket状态，失败返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 2303188 | Socket operation on non-socket. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
tls.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
tls.getState((err: BusinessError, data: socket.SocketStateBase) => {
  if (err) {
    console.error('getState fail');
    return;
  }
  console.info('getState success:' + JSON.stringify(data));
});
```

#### \[h2\]getState9+

getState(): Promise<SocketStateBase>

在TLSSocket的bind成功之后，获取TLSSocket状态。使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[SocketStateBase](#socketstatebase)\> | 以Promise形式返回获取TLSSocket状态的结果。失败返回错误码，错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 2303188 | Socket operation on non-socket. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
tls.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
tls.getState().then(() => {
  console.info('getState success');
}).catch((err: BusinessError) => {
  console.error('getState fail');
});
```

#### \[h2\]setExtraOptions9+

setExtraOptions(options: TCPExtraOptions, callback: AsyncCallback<void>): void

在TLSSocket的bind成功之后，设置TCPSocket连接的其他属性。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [TCPExtraOptions](#tcpextraoptions) | 是 | TCPSocket连接的其他属性，参考[TCPExtraOptions](#tcpextraoptions)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。成功返回设置TCPSocket连接的其他属性的结果，失败返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2303188 | Socket operation on non-socket. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
tls.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});

interface SocketLinger {
  on: boolean;
  linger: number;
}

let tcpExtraOptions: socket.TCPExtraOptions = {
  keepAlive: true,
  OOBInline: true,
  TCPNoDelay: true,
  socketLinger: { on: true, linger: 10 } as SocketLinger,
  receiveBufferSize: 8192,
  sendBufferSize: 8192,
  reuseAddress: true,
  socketTimeout: 3000
}
tls.setExtraOptions(tcpExtraOptions, (err: BusinessError) => {
  if (err) {
    console.error('setExtraOptions fail');
    return;
  }
  console.info('setExtraOptions success');
});
```

#### \[h2\]setExtraOptions9+

setExtraOptions(options: TCPExtraOptions): Promise<void>

在TLSSocket的bind成功之后，设置TCPSocket连接的其他属性。使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [TCPExtraOptions](#tcpextraoptions) | 是 | TCPSocket连接的其他属性，参考[TCPExtraOptions](#tcpextraoptions)。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2303188 | Socket operation on non-socket. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
tls.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});

interface SocketLinger {
  on: boolean;
  linger: number;
}

let tcpExtraOptions: socket.TCPExtraOptions = {
  keepAlive: true,
  OOBInline: true,
  TCPNoDelay: true,
  socketLinger: { on: true, linger: 10 } as SocketLinger,
  receiveBufferSize: 8192,
  sendBufferSize: 8192,
  reuseAddress: true,
  socketTimeout: 3000
}
tls.setExtraOptions(tcpExtraOptions).then(() => {
  console.info('setExtraOptions success');
}).catch((err: BusinessError) => {
  console.error('setExtraOptions fail');
});
```

#### \[h2\]on('message')9+

on(type: 'message', callback: Callback<SocketMessageInfo>): void

订阅TLSSocket连接的接收消息事件。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/6con55x8QCWgavaO-Qa_9g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=0EF09A44C19D008BBBB89CEBC5D8E20AE9217EE6875915A749AAC1CF675A3CB6)

bind方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅的事件类型。'message'：接收消息事件。 |
| callback | Callback<[SocketMessageInfo](#socketmessageinfo11)\> | 是 | 回调函数。TLSSocket连接订阅某类接受消息事件触发的调用函数，返回TLSSocket连接信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
tls.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
  tls.on('message', (value: socket.SocketMessageInfo) => {
    let messageView = '';
    let uint8Array = new Uint8Array(value.message);
    for (let i: number = 0; i < value.message.byteLength; i++) {
      let messages = uint8Array[i];
      let message = String.fromCharCode(messages);
      messageView += message;
    }
    console.info('on message message: ' + JSON.stringify(messageView));
    console.info('remoteInfo: ' + JSON.stringify(value.remoteInfo));
  });
});
```

#### \[h2\]off('message')9+

off(type: 'message', callback?: Callback<SocketMessageInfo>): void

取消订阅TLSSocket连接的接收消息事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅的事件类型。'message'：接收消息事件。 |
| callback | Callback<[SocketMessageInfo](#socketmessageinfo11)\> | 否 | 回调函数。TLSSocket连接取消订阅某类接受消息事件触发的调用函数，返回TLSSocket连接信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
let messageView = '';
let callback = (value: socket.SocketMessageInfo) => {
  for (let i: number = 0; i < value.message.byteLength; i++) {
    let uint8Array = new Uint8Array(value.message)
    let messages = uint8Array[i]
    let message = String.fromCharCode(messages);
    messageView += message;
  }
  console.info('on message message: ' + JSON.stringify(messageView));
  console.info('remoteInfo: ' + JSON.stringify(value.remoteInfo));
}
tls.on('message', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
tls.off('message', callback);
```

#### \[h2\]on('connect' | 'close')9+

on(type: 'connect' | 'close', callback: Callback<void>): void

订阅TLSSocket的连接事件或关闭事件。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/WDE6oNNcQ-WF5eGSEbbTpg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=D3595E39DE682D1608F176FD511156D152C30338B16DA8451046F1CD6D6ACA1B)

bind方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 
订阅的事件类型。

\- 'connect'：连接事件。

\- 'close'：关闭事件。

 |
| callback | Callback<void> | 是 | 回调函数。TLSSocket连接订阅某类事件触发的调用函数。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
tls.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
  tls.on('connect', () => {
    console.info("on connect success")
  });
  tls.on('close', () => {
    console.info("on close success")
  });
});
```

#### \[h2\]off('connect' | 'close')9+

off(type: 'connect' | 'close', callback?: Callback<void>): void

取消订阅TLSSocket的连接事件或关闭事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 
订阅的事件类型。

\- 'connect'：连接事件。

\- 'close'：关闭事件。

 |
| callback | Callback<void> | 否 | 回调函数。TLSSocket连接订阅某类事件触发的调用函数。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
let callback1 = () => {
  console.info("on connect success");
}
tls.on('connect', callback1);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
tls.off('connect', callback1);
tls.off('connect');
let callback2 = () => {
  console.info("on close success");
}
tls.on('close', callback2);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
tls.off('close', callback2);
```

#### \[h2\]on('error')9+

on(type: 'error', callback: ErrorCallback): void

订阅TLSSocket连接的error事件。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/BwFIgCXfQGeJMjdXcwPGdQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=8DA18450A1A5BB89ACCDA70F33DCF2A0F18D42BFAC69E97895477F5C228CE3C9)

bind方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅的事件类型。'error'：error事件。 |
| callback | ErrorCallback | 是 | 回调函数。TLSSocket连接订阅某类error事件触发的调用函数。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
tls.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
  tls.on('error', (err: BusinessError) => {
    console.error("on error, err:" + JSON.stringify(err))
  });
});
```

#### \[h2\]off('error')9+

off(type: 'error', callback?: ErrorCallback): void

取消订阅TLSSocket连接的error事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅的事件类型。'error'：error事件。 |
| callback | ErrorCallback | 否 | 回调函数。TLSSocket连接取消订阅某类error事件触发的调用函数。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
let callback = (err: BusinessError) => {
  console.error("on error, err:" + JSON.stringify(err));
}
tls.on('error', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
tls.off('error', callback);
```

#### \[h2\]connect9+

connect(options: TLSConnectOptions, callback: AsyncCallback<void>): void

在TLSSocket上bind成功之后，进行通信连接，并创建和初始化TLS会话，实现建立连接过程，启动与服务器的TLS/SSL握手，实现数据传输功能，使用callback异步回调。需要注意options入参下secureOptions内的ca在API11及之前的版本为必填项，需填入服务端的ca证书(用于认证校验服务端的数字证书)，证书内容以"-----BEGIN CERTIFICATE-----"开头，以"-----END CERTIFICATE-----"结尾，自API12开始，为非必填项。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [TLSConnectOptions](#tlsconnectoptions9) | 是 | TLSSocket连接所需要的参数。 |
| callback | AsyncCallback<void> | 是 | 回调函数，成功无返回，失败返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2303104 | Interrupted system call. |
| 2303109 | Bad file number. |
| 2303111 | Resource temporarily unavailable. Try again. |
| 2303188 | Socket operation on non-socket. |
| 2303191 | Incorrect socket protocol type. |
| 2303198 | Address already in use. |
| 2303199 | Cannot assign requested address. |
| 2303210 | Connection timed out. |
| 2303501 | SSL is null. |
| 2303502 | An error occurred when reading data on the TLS socket. |
| 2303503 | An error occurred when writing data on the TLS socket. |
| 2303505 | An error occurred in the TLS system call. |
| 2303506 | Failed to close the TLS connection. |
| 2300002 | System internal error. |
| 2301206 | Socks5 failed to connect to the proxy server. |
| 2301207 | Socks5 username or password is invalid. |
| 2301208 | Socks5 failed to connect to the remote server. |
| 2301209 | Socks5 failed to negotiate the authentication method. |
| 2301210 | Socks5 failed to send the message. |
| 2301211 | Socks5 failed to receive the message. |
| 2301212 | Socks5 serialization error. |
| 2301213 | Socks5 deserialization error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsTwoWay: socket.TLSSocket = socket.constructTLSSocketInstance();  // Two way authentication
let bindAddr: socket.NetAddress = {
    address: '192.168.xx.xxx',
  // 绑定指定网络接口
}
tlsTwoWay.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
let twoWayNetAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let twoWaySecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: twoWayNetAddr,
  secureOptions: twoWaySecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}

tlsTwoWay.connect(tlsConnectOptions, (err: BusinessError) => {
  console.error("connect callback error" + err);
});

let tlsOneWay: socket.TLSSocket = socket.constructTLSSocketInstance(); // One way authentication
tlsOneWay.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
let oneWayNetAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let oneWaySecureOptions: socket.TLSSecureOptions = {
  ca: ["xxxx", "xxxx"],
  cipherSuite: "AES256-SHA256"
}
let tlsOneWayConnectOptions: socket.TLSConnectOptions = {
  address: oneWayNetAddr,
  secureOptions: oneWaySecureOptions
}
tlsOneWay.connect(tlsOneWayConnectOptions, (err: BusinessError) => {
  console.error("connect callback error" + err);
});
```

**示例（设置socket代理）：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsTwoWay: socket.TLSSocket = socket.constructTLSSocketInstance();  // 双向认证
let bindAddr: socket.NetAddress = {
   address: '192.168.xx.xxx',
  // 绑定指定网络接口
}
tlsTwoWay.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
let twoWayNetAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let socks5Server: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let twoWaySecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let proxyOptions: socket.ProxyOptions = {
  type : 1,
  address: socks5Server,
  username: "xxx",
  password: "xxx"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: twoWayNetAddr,
  secureOptions: twoWaySecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"],
  proxy: proxyOptions,
}

tlsTwoWay.connect(tlsConnectOptions, (err: BusinessError) => {
  console.error("connect callback error" + err);
});

let tlsOneWay: socket.TLSSocket = socket.constructTLSSocketInstance(); // 单向认证
tlsOneWay.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
let oneWayNetAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let oneWaySecureOptions: socket.TLSSecureOptions = {
  ca: ["xxxx", "xxxx"],
  cipherSuite: "AES256-SHA256"
}
let oneWayProxyOptions: socket.ProxyOptions = {
  type : 1,
  address: socks5Server,
  username: "xxx",
  password: "xxx"
}
let tlsOneWayConnectOptions: socket.TLSConnectOptions = {
  address: oneWayNetAddr,
  secureOptions: oneWaySecureOptions,
  proxy: oneWayProxyOptions,
}
tlsOneWay.connect(tlsOneWayConnectOptions, (err: BusinessError) => {
  console.error("connect callback error" + err);
});
```

#### \[h2\]connect9+

connect(options: TLSConnectOptions): Promise<void>

在TLSSocket上bind成功之后，进行通信连接，并创建和初始化TLS会话，实现建立连接过程，启动与服务器的TLS/SSL握手，实现数据传输功能，该连接包括两种认证方式，单向认证与双向认证，使用Promise异步回调。需要注意options入参下secureOptions内的ca在API11及之前的版本为必填项，需填入服务端的ca证书(用于认证校验服务端的数字证书)，证书内容以"-----BEGIN CERTIFICATE-----"开头，以"-----END CERTIFICATE-----"结尾，自API12开始，为非必填项。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [TLSConnectOptions](#tlsconnectoptions9) | 是 | 连接所需要的参数。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 以Promise形式返回，成功无返回，失败返回错误码，错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2303104 | Interrupted system call. |
| 2303109 | Bad file number. |
| 2303111 | Resource temporarily unavailable. Try again. |
| 2303188 | Socket operation on non-socket. |
| 2303191 | Incorrect socket protocol type. |
| 2303198 | Address already in use. |
| 2303199 | Cannot assign requested address. |
| 2303210 | Connection timed out. |
| 2303501 | SSL is null. |
| 2303502 | An error occurred when reading data on the TLS socket. |
| 2303503 | An error occurred when writing data on the TLS socket. |
| 2303505 | An error occurred in the TLS system call. |
| 2303506 | Failed to close the TLS connection. |
| 2300002 | System internal error. |
| 2301206 | Socks5 failed to connect to the proxy server. |
| 2301207 | Socks5 username or password is invalid. |
| 2301208 | Socks5 failed to connect to the remote server. |
| 2301209 | Socks5 failed to negotiate the authentication method. |
| 2301210 | Socks5 failed to send the message. |
| 2301211 | Socks5 failed to receive the message. |
| 2301212 | Socks5 serialization error. |
| 2301213 | Socks5 deserialization error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsTwoWay: socket.TLSSocket = socket.constructTLSSocketInstance();  // Two way authentication
let bindAddr: socket.NetAddress = {
   address: '192.168.xx.xxx',
  // 绑定指定网络接口
}
tlsTwoWay.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
let twoWayNetAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let twoWaySecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: twoWayNetAddr,
  secureOptions: twoWaySecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}

tlsTwoWay.connect(tlsConnectOptions).then(() => {
  console.info("connect successfully");
}).catch((err: BusinessError) => {
  console.error("connect failed " + JSON.stringify(err));
});

let tlsOneWay: socket.TLSSocket = socket.constructTLSSocketInstance(); // One way authentication
tlsOneWay.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
let oneWayNetAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let oneWaySecureOptions: socket.TLSSecureOptions = {
  ca: ["xxxx", "xxxx"],
  cipherSuite: "AES256-SHA256"
}
let tlsOneWayConnectOptions: socket.TLSConnectOptions = {
  address: oneWayNetAddr,
  secureOptions: oneWaySecureOptions
}
tlsOneWay.connect(tlsOneWayConnectOptions).then(() => {
  console.info("connect successfully");
}).catch((err: BusinessError) => {
  console.error("connect failed " + JSON.stringify(err));
});
```

**示例（设置socket代理）：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsTwoWay: socket.TLSSocket = socket.constructTLSSocketInstance();  // 双向认证
let bindAddr: socket.NetAddress = {
   address: '192.168.xx.xxx',
  // 绑定指定网络接口
}
tlsTwoWay.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
let twoWayNetAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let socks5Server: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let twoWaySecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let proxyOptions: socket.ProxyOptions = {
  type : 1,
  address: socks5Server,
  username: "xxx",
  password: "xxx"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: twoWayNetAddr,
  secureOptions: twoWaySecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"],
  proxy: proxyOptions,
}

tlsTwoWay.connect(tlsConnectOptions).then(() => {
  console.info("connect successfully");
}).catch((err: BusinessError) => {
  console.error("connect failed " + JSON.stringify(err));
});

let tlsOneWay: socket.TLSSocket = socket.constructTLSSocketInstance(); // 单向认证
tlsOneWay.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
let oneWayNetAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let oneWaySecureOptions: socket.TLSSecureOptions = {
  ca: ["xxxx", "xxxx"],
  cipherSuite: "AES256-SHA256"
}
let oneWayProxyOptions: socket.ProxyOptions = {
  type : 1,
  address: socks5Server,
  username: "xxx",
  password: "xxx"
}
let tlsOneWayConnectOptions: socket.TLSConnectOptions = {
  address: oneWayNetAddr,
  secureOptions: oneWaySecureOptions,
  proxy: oneWayProxyOptions,
}
tlsOneWay.connect(tlsOneWayConnectOptions).then(() => {
  console.info("connect successfully");
}).catch((err: BusinessError) => {
  console.error("connect failed " + JSON.stringify(err));
});
```

#### \[h2\]getRemoteAddress9+

getRemoteAddress(callback: AsyncCallback<NetAddress>): void

在TLSSocket通信连接成功之后，获取对端Socket地址。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[NetAddress](#netaddress)\> | 是 | 回调函数。成功返回对端的socket地址，失败返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 2303188 | Socket operation on non-socket. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.getRemoteAddress((err: BusinessError, data: socket.NetAddress) => {
  if (err) {
    console.error('getRemoteAddress fail');
    return;
  }
  console.info('getRemoteAddress success:' + JSON.stringify(data));
});
```

#### \[h2\]getRemoteAddress9+

getRemoteAddress(): Promise<NetAddress>

在TLSSocket通信连接成功之后，获取对端Socket地址。使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[NetAddress](#netaddress)\> | 以Promise形式返回获取对端socket地址的结果。失败返回错误码，错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 2303188 | Socket operation on non-socket. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.getRemoteAddress().then(() => {
  console.info('getRemoteAddress success');
}).catch((err: BusinessError) => {
  console.error('getRemoteAddress fail');
});
```

#### \[h2\]getCertificate9+

getCertificate(callback: AsyncCallback<[X509CertRawData](#x509certrawdata9)\>): void

在TLSSocket通信连接成功之后，获取本地的数字证书，该接口只适用于双向认证时，使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[X509CertRawData](#x509certrawdata9)\> | 是 | 回调函数，成功返回本地的证书，失败返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 2303501 | SSL is null. |
| 2303504 | An error occurred when verifying the X.509 certificate. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.getCertificate((err: BusinessError, data: socket.X509CertRawData) => {
  if (err) {
    console.error("getCertificate callback error = " + err);
  } else {
    console.info("getCertificate callback = " + data);
  }
});
```

#### \[h2\]getCertificate9+

getCertificate():Promise<[X509CertRawData](#x509certrawdata9)\>

在TLSSocket通信连接之后，获取本地的数字证书，该接口只适用于双向认证时，使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[X509CertRawData](#x509certrawdata9)\> | 以Promise形式返回本地的数字证书的结果。失败返回错误码，错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 2303501 | SSL is null. |
| 2303504 | An error occurred when verifying the X.509 certificate. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.getCertificate().then((data: socket.X509CertRawData) => {
  const decoder = util.TextDecoder.create();
  const str = decoder.decodeToString(data.data);
  console.info("getCertificate: " + str);
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
```

#### \[h2\]getRemoteCertificate9+

getRemoteCertificate(callback: AsyncCallback<[X509CertRawData](#x509certrawdata9)\>): void

在TLSSocket通信连接成功之后，获取服务端的数字证书，使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[X509CertRawData](#x509certrawdata9)\> | 是 | 回调函数，返回服务端的证书。失败返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 2303501 | SSL is null. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.getRemoteCertificate((err: BusinessError, data: socket.X509CertRawData) => {
  if (err) {
    console.error("getRemoteCertificate callback error = " + err);
  } else {
    const decoder = util.TextDecoder.create();
    const str = decoder.decodeToString(data.data);
    console.info("getRemoteCertificate callback = " + str);
  }
});
```

#### \[h2\]getRemoteCertificate9+

getRemoteCertificate():Promise<[X509CertRawData](#x509certrawdata9)\>

在TLSSocket通信连接成功之后，获取服务端的数字证书，使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[X509CertRawData](#x509certrawdata9)\> | 以Promise形式返回服务端的数字证书的结果。失败返回错误码，错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 2303501 | SSL is null. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.getRemoteCertificate().then((data: socket.X509CertRawData) => {
  const decoder = util.TextDecoder.create();
  const str = decoder.decodeToString(data.data);
  console.info("getRemoteCertificate:" + str);
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
```

#### \[h2\]getProtocol9+

getProtocol(callback: AsyncCallback<string>): void

在TLSSocket通信连接成功之后，获取通信的协议版本，使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<string> | 是 | 回调函数，返回通信的协议。失败返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 2303501 | SSL is null. |
| 2303505 | An error occurred in the TLS system call. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.getProtocol((err: BusinessError, data: string) => {
  if (err) {
    console.error("getProtocol callback error = " + err);
  } else {
    console.info("getProtocol callback = " + data);
  }
});
```

#### \[h2\]getProtocol9+

getProtocol():Promise<string>

在TLSSocket通信连接成功之后，获取通信的协议版本，使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | 以Promise形式返回通信的协议。失败返回错误码，错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 2303501 | SSL is null. |
| 2303505 | An error occurred in the TLS system call. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.getProtocol().then((data: string) => {
  console.info(data);
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
```

#### \[h2\]getCipherSuite9+

getCipherSuite(callback: AsyncCallback<Array<string>>): void

在TLSSocket通信连接成功之后，获取通信双方协商后的加密套件，使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<string>> | 是 | 回调函数，返回通信双方支持的加密套件。失败返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 2303501 | SSL is null. |
| 2303502 | An error occurred when reading data on the TLS socket. |
| 2303505 | An error occurred in the TLS system call. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.getCipherSuite((err: BusinessError, data: Array<string>) => {
  if (err) {
    console.error("getCipherSuite callback error = " + err);
  } else {
    console.info("getCipherSuite callback = " + data);
  }
});
```

#### \[h2\]getCipherSuite9+

getCipherSuite(): Promise<Array<string>>

在TLSSocket通信连接成功之后，获取通信双方协商后的加密套件，使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<string>> | 以Promise形式返回通信双方支持的加密套件。失败返回错误码，错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 2303501 | SSL is null. |
| 2303502 | An error occurred when reading data on the TLS socket. |
| 2303505 | An error occurred in the TLS system call. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.getCipherSuite().then((data: Array<string>) => {
  console.info('getCipherSuite success:' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
```

#### \[h2\]getSignatureAlgorithms9+

getSignatureAlgorithms(callback: AsyncCallback<Array<string>>): void

在TLSSocket通信连接成功之后，获取通信双方协商后签名算法，该接口只适配双向认证模式下，使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<string>> | 是 | 回调函数，返回双方支持的签名算法。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 2303501 | SSL is null. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.getSignatureAlgorithms((err: BusinessError, data: Array<string>) => {
  if (err) {
    console.error("getSignatureAlgorithms callback error = " + err);
  } else {
    console.info("getSignatureAlgorithms callback = " + data);
  }
});
```

#### \[h2\]getSignatureAlgorithms9+

getSignatureAlgorithms(): Promise<Array<string>>

在TLSSocket通信连接成功之后，获取通信双方协商后的签名算法，该接口只适配双向认证模式下，使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<string>> | 以Promise形式返回获取到的双方支持的签名算法。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 2303501 | SSL is null. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.getSignatureAlgorithms().then((data: Array<string>) => {
  console.info("getSignatureAlgorithms success" + data);
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
```

#### \[h2\]getLocalAddress12+

getLocalAddress(): Promise<NetAddress>

获取TLSSocket的本地Socket地址。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/W6oLvo2kRtan08vfxQDJtg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=C8AAF01CFD8D941AE60ECDB316FD41F26350C10D037BE422C2A5277ECBAEA704)

在TLSSocketServer通信连接成功之后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[NetAddress](#netaddress)\> | 以Promise形式返回获取本地socket地址的结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 2300002 | System internal error. |
| 2301009 | Bad file descriptor. |
| 2303188 | Socket operation on non-socket. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.getLocalAddress().then((localAddress: socket.NetAddress) => {
  console.info("Get success: " + JSON.stringify(localAddress));
}).catch((err: BusinessError) => {
  console.error("Get failed, error: " + JSON.stringify(err));
})
```

#### \[h2\]getSocketFd16+

getSocketFd(): Promise<number>

获取TLSSocket的文件描述符。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/yP-XhmDQRi2MhEst_uwDIw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=A54563BFEFB6C8695F5DE68CCADDD04B628350E2A60C86C4B516645791FFB91E)

-   bind方法调用成功后，才可调用此方法。
-   文件描述符的生命周期由系统管理，应用可以通过[close](#close9)方法关闭Socket连接，避免直接操作文件描述符进行关闭。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | 以Promise形式返回socket的文件描述符。 |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
let bindAddr: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
tls.bind(bindAddr, (err: BusinessError) => {
  if (err) {
    console.error('bind fail');
    return;
  }
  console.info('bind success');
});
tls.getSocketFd().then((data: number) => {
  console.info("tls socket fd: " + data);
})
```

#### \[h2\]send9+

send(data: string | ArrayBuffer, callback: AsyncCallback<void>): void

在TLSSocket通信连接成功之后，向服务端发送消息，使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| data | string | ArrayBuffer | 是 | 发送的数据内容。 |
| callback | AsyncCallback<void> | 是 | 回调函数,返回TLSSocket发送数据的结果。失败返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2303501 | SSL is null. |
| 2303503 | An error occurred when writing data on the TLS socket. |
| 2303505 | An error occurred in the TLS system call. |
| 2303506 | Failed to close the TLS connection. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.send("xxxx", (err: BusinessError) => {
  if (err) {
    console.error("send callback error = " + err);
  } else {
    console.info("send success");
  }
});
```

#### \[h2\]send9+

send(data: string | ArrayBuffer): Promise<void>

在TLSSocket通信连接成功之后，向服务端发送消息，使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| data | string | ArrayBuffer | 是 | 发送的数据内容。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 以Promise形式返回,返回TLSSocket发送数据的结果。失败返回错误码，错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2303501 | SSL is null. |
| 2303503 | An error occurred when writing data on the TLS socket. |
| 2303505 | An error occurred in the TLS system call. |
| 2303506 | Failed to close the TLS connection. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.send("xxxx").then(() => {
  console.info("send success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
```

#### \[h2\]close9+

close(callback: AsyncCallback<void>): void

在TLSSocket通信连接成功之后，断开连接，使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | 是 | 回调函数,成功返回TLSSocket关闭连接的结果。失败返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2303501 | SSL is null. |
| 2303505 | An error occurred in the TLS system call. |
| 2303506 | Failed to close the TLS connection. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.close((err: BusinessError) => {
  if (err) {
    console.error("close callback error = " + err);
  } else {
    console.info("close success");
  }
});
```

#### \[h2\]close9+

close(): Promise<void>

在TLSSocket通信连接成功之后，断开连接，使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 以Promise形式返回,返回TLSSocket关闭连接的结果。失败返回错误码，错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2303501 | SSL is null. |
| 2303505 | An error occurred in the TLS system call. |
| 2303506 | Failed to close the TLS connection. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
tls.close().then(() => {
  console.info("close success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
```

#### TLSConnectOptions9+

TLS连接的操作。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| address | [NetAddress](#netaddress) | 否 | 否 | 网关地址。 |
| secureOptions | [TLSSecureOptions](#tlssecureoptions9) | 否 | 否 | TLS安全相关操作。 |
| ALPNProtocols | Array<string> | 否 | 是 | ALPN协议，支持\["spdy/1", "http/1.1"\]，默认为\[\]。 |
| skipRemoteValidation12+ | boolean | 否 | 是 | 是否跳过对服务端进行证书认证，默认为false。true：跳过对服务端进行证书认证；false：不跳过对服务端进行证书认证。 |
| proxy18+ | [ProxyOptions](#proxyoptions18) | 否 | 是 | 使用的代理信息，默认不使用代理。 |
| timeout22+ | number | 否 | 是 | 连接超时时间，单位：ms，默认为0。传入值需为0-4294967295范围内的整数。TLSSocket连接在超时后会失败。 |

#### TLSSecureOptions9+

TLS安全相关操作。当本地证书cert和私钥key不为空时，开启双向验证模式。cert和key其中一项为空时，开启单向验证模式。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| ca | string | Array<string> | 否 | 是 | 服务端的ca证书，用于认证校验服务端的数字证书。默认为系统预置CA证书12+。最多支持设置1000本证书。 |
| cert | string | 否 | 是 | 本地客户端的数字证书。 |
| key | string | 否 | 是 | 本地数字证书的私钥。 |
| password | string | 否 | 是 | 读取私钥的密码。 |
| protocols | [Protocol](#protocol9) |Array<[Protocol](#protocol9)\> | 否 | 是 | TLS的协议版本，默认为"TLSv1.2"。 |
| useRemoteCipherPrefer | boolean | 否 | 是 | 优先使用对等方的密码套件。true：优先使用对等方的密码套件；false：不优先使用对等方的密码套件。 |
| signatureAlgorithms | string | 否 | 是 | 通信过程中的签名算法，默认为"" 。 |
| cipherSuite | string | 否 | 是 | 通信过程中的加密套件，默认为"" 。 |
| isBidirectionalAuthentication12+ | boolean | 否 | 是 | 用于设置双向认证，默认为false。true：设置双向认证；false：不设置双向认证。 |

#### Protocol9+

TLS通信的协议版本。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| TLSv12 | "TLSv1.2" | 使用TLSv1.2协议通信。 |
| TLSv13 | "TLSv1.3" | 使用TLSv1.3协议通信。 |

#### X509CertRawData9+

type X509CertRawData = cert.EncodingBlob

存储证书的数据。

**系统能力**：SystemCapability.Communication.NetStack

| 类型 | 说明 |
| :-- | :-- |
| cert.EncodingBlob | 提供证书编码blob类型。 |

#### socket.constructTLSSocketServerInstance10+

constructTLSSocketServerInstance(): TLSSocketServer

创建并返回一个TLSSocketServer对象。

**系统能力**：SystemCapability.Communication.NetStack

**返回值:**

| 类型 | 说明 |
| :-- | :-- |
| [TLSSocketServer](#tlssocketserver10) | 返回一个TLSSocketServer对象。 |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
```

#### TLSSocketServer10+

TLSSocketServer连接。在调用TLSSocketServer的方法前，需要先通过[socket.constructTLSSocketServerInstance](#socketconstructtlssocketserverinstance10)创建TLSSocketServer对象。

#### \[h2\]listen10+

listen(options: TLSConnectOptions, callback: AsyncCallback<void>): void

绑定IP地址和端口，在TLSSocketServer上bind成功之后，监听客户端的连接，创建和初始化TLS会话，实现建立连接过程，加载证书秘钥并验证，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/JUWddm5nTtWl786aGUaFrQ/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=B6C6DB21CB96A84BD6E1CB6123370D78F3829E65E6A21BD258D35DEE1B0727DF)

IP地址设置为0.0.0.0时，可以监听本机所有地址。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [TLSConnectOptions](#tlsconnectoptions9) | 是 | TLSSocketServer连接所需要的参数。 |
| callback | AsyncCallback<void> | 是 | 回调函数，成功返回空，失败返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300002 | System internal error. |
| 2303109 | Bad file number. |
| 2303111 | Resource temporarily unavailable. Try again. |
| 2303198 | Address already in use. |
| 2303199 | Cannot assign requested address. |
| 2303501 | SSL is null. |
| 2303502 | An error occurred when reading data on the TLS socket. |
| 2303503 | An error occurred when writing data on the TLS socket. |
| 2303505 | An error occurred in the TLS system call. |
| 2303506 | Failed to close the TLS connection. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"],
  skipRemoteValidation: false
}
tlsServer.listen(tlsConnectOptions, (err: BusinessError) => {
  console.error("listen callback error" + err);
});
```

#### \[h2\]listen10+

listen(options: TLSConnectOptions): Promise<void>

绑定IP地址和端口，在TLSSocketServer上bind成功之后，监听客户端的连接，并创建和初始化TLS会话，实现建立连接过程，加载证书秘钥并验证，使用Promise异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [TLSConnectOptions](#tlsconnectoptions9) | 是 | 连接所需要的参数。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 以Promise形式返回，成功返回空，失败返回错误码，错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300002 | System internal error. |
| 2303109 | Bad file number. |
| 2303111 | Resource temporarily unavailable. Try again. |
| 2303198 | Address already in use. |
| 2303199 | Cannot assign requested address. |
| 2303501 | SSL is null. |
| 2303502 | An error occurred when reading data on the TLS socket. |
| 2303503 | An error occurred when writing data on the TLS socket. |
| 2303505 | An error occurred in the TLS system call. |
| 2303506 | Failed to close the TLS connection. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"],
  skipRemoteValidation: false
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed: " + JSON.stringify(err));
});
```

#### \[h2\]getState10+

getState(callback: AsyncCallback<SocketStateBase>): void

在TLSSocketServer的listen成功之后，获取TLSSocketServer状态。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/gQPTX_0LR-yw-iJDWo2mxQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=D7B0F9C24A8543245517220D2230C56E980D8FE83C508E2D258DD26E0A577A71)

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[SocketStateBase](#socketstatebase)\> | 是 | 回调函数。成功返回TLSSocketServer状态，失败返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2303188 | Socket operation on non-socket. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed: " + JSON.stringify(err));
});
tlsServer.getState((err: BusinessError, data: socket.SocketStateBase) => {
  if (err) {
    console.error('getState fail');
    return;
  }
  console.info('getState success:' + JSON.stringify(data));
});
```

#### \[h2\]getState10+

getState(): Promise<SocketStateBase>

在TLSSocketServer的listen成功之后，获取TLSSocketServer状态。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/pCBAkRVzRKCQB6ZXCh_lfA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=6C06FB5482020BD6496772B59A2CD4DCE1CAA8010A628BABFA7CC6A158E80399)

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[SocketStateBase](#socketstatebase)\> | 以Promise形式返回获取TLSSocketServer状态的结果。失败返回错误码，错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 2303188 | Socket operation on non-socket. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed: " + JSON.stringify(err));
});
tlsServer.getState().then(() => {
  console.info('getState success');
}).catch((err: BusinessError) => {
  console.error('getState fail');
});
```

#### \[h2\]getSocketFd23+

getSocketFd(): Promise<number>

获取TLSSocketServer监听端口绑定的文件描述符。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/W_BbPMC1SNaJQbTlRiq9vg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=71C55646E1875C3CDDFE9CDDEF76CA8964C59036A70C7D4112A1653BD94515F4)

-   [listen](#listen10-3)方法调用成功后，才可调用此方法。多次调用listen时，会获取最新监听端口绑定的文件描述符。
-   监听异常、Socket已关闭（如调用close后）等异常情况下调用本接口会返回-1。
-   文件描述符的生命周期由系统管理，应用可以通过[close](#close20-2)方法关闭Socket连接，避免直接操作文件描述符进行关闭。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | Promise对象，返回Socket的文件描述符。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen success");
  tlsServer.getSocketFd().then((fd: number) => {
    console.info(`Socket FD：${fd}`);
  }).catch((err: BusinessError) => {
    console.error(`getSocketFd fail: ${err.message}, errorCode: ${err.code}`);
  });
}).catch((err: BusinessError) => {
  console.error(`listen failed: ${JSON.stringify(err)}`);
});
```

#### \[h2\]setExtraOptions10+

setExtraOptions(options: TCPExtraOptions, callback: AsyncCallback<void>): void

在TLSSocketServer的listen成功之后，设置TLSSocketServer连接的其他属性。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/JbTmCx7JQ5SIeA6Ekzd2yw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=01AC0E1572F828C478337717953F6EAF59103AF8F93F5F7779EA18174DE1D6C1)

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [TCPExtraOptions](#tcpextraoptions) | 是 | TLSSocketServer连接的其他属性。 |
| callback | AsyncCallback<void> | 是 | 回调函数。成功返回空，失败返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2303188 | Socket operation on non-socket. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed: " + JSON.stringify(err));
});

interface SocketLinger {
  on: boolean;
  linger: number;
}

let tcpExtraOptions: socket.TCPExtraOptions = {
  keepAlive: true,
  OOBInline: true,
  TCPNoDelay: true,
  socketLinger: { on: true, linger: 10 } as SocketLinger,
  receiveBufferSize: 8192,
  sendBufferSize: 8192,
  reuseAddress: true,
  socketTimeout: 3000
}
tlsServer.setExtraOptions(tcpExtraOptions, (err: BusinessError) => {
  if (err) {
    console.error('setExtraOptions fail');
    return;
  }
  console.info('setExtraOptions success');
});
```

#### \[h2\]setExtraOptions10+

setExtraOptions(options: TCPExtraOptions): Promise<void>

在TLSSocketServer的listen成功之后，设置TLSSocketServer连接的其他属性，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/dRSGVpdRT5OVAAjQN_cfww/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=E1D9AE8B66093D20EB8A503D4A61070BA1EA34DF9EB46A82A25F525FB47EE468)

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [TCPExtraOptions](#tcpextraoptions) | 是 | TLSSocketServer连接的其他属性。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 以Promise形式返回，成功返回空，失败返回错误码，错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2303188 | Socket operation on non-socket. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed: " + JSON.stringify(err));
});

interface SocketLinger {
  on: boolean;
  linger: number;
}

let tcpExtraOptions: socket.TCPExtraOptions = {
  keepAlive: true,
  OOBInline: true,
  TCPNoDelay: true,
  socketLinger: { on: true, linger: 10 } as SocketLinger,
  receiveBufferSize: 8192,
  sendBufferSize: 8192,
  reuseAddress: true,
  socketTimeout: 3000
}
tlsServer.setExtraOptions(tcpExtraOptions).then(() => {
  console.info('setExtraOptions success');
}).catch((err: BusinessError) => {
  console.error('setExtraOptions fail');
});
```

#### \[h2\]getCertificate10+

getCertificate(callback: AsyncCallback<[X509CertRawData](#x509certrawdata9)\>): void

在TLSSocketServer通信连接成功之后，获取本地的数字证书，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/AEXwjHXOR22EWMuIcfSuQw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=C418B1060BD8F4DE6439D11B15E47CBB9D1679A5D672F6CDEC83A67D536A89E2)

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[X509CertRawData](#x509certrawdata9)\> | 是 | 回调函数，成功返回本地的证书，失败返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2303501 | SSL is null. |
| 2303504 | An error occurred when verifying the X.509 certificate. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed: " + JSON.stringify(err));
});
tlsServer.getCertificate((err: BusinessError, data: socket.X509CertRawData) => {
  if (err) {
    console.error("getCertificate callback error = " + err);
  } else {
    const decoder = util.TextDecoder.create();
    const str = decoder.decodeToString(data.data);
    console.info("getCertificate callback: " + str);
  }
});
```

#### \[h2\]getCertificate10+

getCertificate():Promise<[X509CertRawData](#x509certrawdata9)\>

在TLSSocketServer通信连接之后，获取本地的数字证书，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/LcdgN06CTcG3pdq-yRIhzg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=23085EAB166F3231A54F8B02772FDA71FB7367D19D98192C9153DF134C1022C4)

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[X509CertRawData](#x509certrawdata9)\> | 以Promise形式返回本地的数字证书的结果。失败返回错误码，错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 2303501 | SSL is null. |
| 2303504 | An error occurred when verifying the X.509 certificate. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed: " + JSON.stringify(err));
});
tlsServer.getCertificate().then((data: socket.X509CertRawData) => {
  const decoder = util.TextDecoder.create();
  const str = decoder.decodeToString(data.data);
  console.info("getCertificate: " + str);
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
```

#### \[h2\]getProtocol10+

getProtocol(callback: AsyncCallback<string>): void

在TLSSocketServer通信连接成功之后，获取通信的协议版本，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/XIalEBKxQTevjArfqYQq-Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=DDE79E07D5F4F9C34DA0B499C42DBCB558AAF7E384A2A5383487BED9710463C0)

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<string> | 是 | 回调函数，返回通信的协议。失败返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2303501 | SSL is null. |
| 2303505 | An error occurred in the TLS system call. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed: " + JSON.stringify(err));
});
tlsServer.getProtocol((err: BusinessError, data: string) => {
  if (err) {
    console.error("getProtocol callback error = " + err);
  } else {
    console.info("getProtocol callback = " + data);
  }
});
```

#### \[h2\]getProtocol10+

getProtocol():Promise<string>

在TLSSocketServer通信连接成功之后，获取通信的协议版本，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/w1ufahJ8Q7Sb7KuyO5sPuQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=80ECAAB83C5E92CCCE45F43100F310ED0FECA46F3128983E4DC32B74B0E006A2)

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | 以Promise形式返回通信的协议。失败返回错误码，错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 2303501 | SSL is null. |
| 2303505 | An error occurred in the TLS system call. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed: " + JSON.stringify(err));
});
tlsServer.getProtocol().then((data: string) => {
  console.info(data);
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
```

#### \[h2\]getLocalAddress12+

getLocalAddress(): Promise<NetAddress>

获取TLSSocketServer的本地Socket地址。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/9_ivJXvHTCaoimKvKP7r1A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=7C8CD73B999706A93097A9DC0CFD7A2A219385BA413FF0F44D76E40530D66D0A)

在TLSSocketServer通信连接成功之后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[NetAddress](#netaddress)\> | 以Promise形式返回获取本地socket地址的结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 2300002 | System internal error. |
| 2301009 | Bad file descriptor. |
| 2303188 | Socket operation on non-socket. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
tlsServer.getLocalAddress().then((localAddress: socket.NetAddress) => {
  console.info("Get success: " + JSON.stringify(localAddress));
}).catch((err: BusinessError) => {
  console.error("Get failed, error: " + JSON.stringify(err));
})
```

#### \[h2\]on('connect')10+

on(type: 'connect', callback: Callback<TLSSocketConnection>): void

订阅TLSSocketServer的连接事件。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/4uzjtGOnSNOPgCqYG1rscA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=C0FEE4E8F7412A95CA7C7562A04ABE610BDBE68974345F58F491E703E98A764D)

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅的事件类型。'connect'：连接事件。 |
| callback | Callback<[TLSSocketConnection](#tlssocketconnection10)\> | 是 | 回调函数。失败时返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
  tlsServer.on('connect', (data: socket.TLSSocketConnection) => {
    console.info(JSON.stringify(data));
  });
}).catch((err: BusinessError) => {
  console.error("failed: " + JSON.stringify(err));
});
```

#### \[h2\]off('connect')10+

off(type: 'connect', callback?: Callback<TLSSocketConnection>): void

取消订阅TLSSocketServer的连接事件。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/8vUmsA5ZS52KqSE_A7n66w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=EB41E05BD5495E2DAC50FABA4018889EF77363D5170A2A90E2D61B358BB5C789)

listen方法调用成功后，才可调用此方法。

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅的事件类型。'connect'：连接事件。 |
| callback | Callback<[TLSSocketConnection](#tlssocketconnection10)\> | 否 | 回调函数。失败时返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed: " + JSON.stringify(err));
});

let callback = (data: socket.TLSSocketConnection) => {
  console.info('on connect message: ' + JSON.stringify(data));
}
tlsServer.on('connect', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
tlsServer.off('connect', callback);
tlsServer.off('connect');
```

#### \[h2\]on('error')10+

on(type: 'error', callback: ErrorCallback): void

订阅TLSSocketServer连接的error事件。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/H9ERr8txRGyvlneAtmLg-g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=55D28A097D24CF8786B4E8676D4FD81EAA77CA22C18B262631A37D9088E246CE)

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅的事件类型。'error'：error事件。 |
| callback | ErrorCallback | 是 | 回调函数。失败时返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed: " + JSON.stringify(err));
});
tlsServer.on('error', (err: BusinessError) => {
  console.error("on error, err:" + JSON.stringify(err))
});
```

#### \[h2\]off('error')10+

off(type: 'error', callback?: ErrorCallback): void

取消订阅TLSSocketServer连接的error事件。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/FWlY4V2ORriMxblWxcz76g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=206B0C413705E9C6E723840A8424DE8DB9F1EDA79119B37F5BB50CDD5AB9C126)

listen方法调用成功后，才可调用此方法。

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅的事件类型。'error'：error事件。 |
| callback | ErrorCallback | 否 | 回调函数。失败时返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed: " + JSON.stringify(err));
});

let callback = (err: BusinessError) => {
  console.error("on error, err:" + JSON.stringify(err));
}
tlsServer.on('error', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
tlsServer.off('error', callback);
tlsServer.off('error');
```

#### \[h2\]close20+

close(): Promise<void>

TLSSocketServer停止监听并释放通过[listen](#listen10-2)方法绑定的端口。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/MGKAZo-0TsC6gt9LprANYQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=A83C0BD600C8ACE2FCF4C5EA0EE33C8947C74526A5037E68B3279C024079219B)

该方法不会关闭已有连接。如需关闭，请调用[TLSSocketConnection](#tlssocketconnection10)的[close](#close10-2)方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.on('connect', (connection: socket.TLSSocketConnection) => {
  console.info("connection clientId: " + connection.clientId);
  // 逻辑处理
  tlsServer.close(); // 停止监听
  connection.close(); // 关闭当前连接
});
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("listen failed: " + err.code);
});
```

#### TLSSocketConnection10+

TLSSocketConnection连接，即TLSSocket客户端与服务端的连接。在调用TLSSocketConnection的方法前，需要先获取TLSSocketConnection对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/dclFKDQoQNSFxivinK4ZEg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=9789F46B026B8263AADAB1D98B31C27FB6212E5783AABC3256AE52FDE67017D5)

客户端与服务端成功建立连接后，才能通过返回的TLSSocketConnection对象调用相应的接口。

**系统能力**：SystemCapability.Communication.NetStack

#### \[h2\]属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| clientId | number | 否 | 否 | 客户端与TLSSocketServer建立连接的id。 |

#### \[h2\]send10+

send(data: string | ArrayBuffer, callback: AsyncCallback<void>): void

在TLSSocketServer通信连接成功之后，向客户端发送消息，使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| data | string | ArrayBuffer | 是 | TLSSocketServer发送数据所需要的参数。 |
| callback | AsyncCallback<void> | 是 | 回调函数，成功返回空，失败返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2303501 | SSL is null. |
| 2303503 | An error occurred when writing data on the TLS socket. |
| 2303505 | An error occurred in the TLS system call. |
| 2303506 | Failed to close the TLS connection. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});

tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.send('Hello, client!', (err: BusinessError) => {
    if (err) {
      console.error('send fail');
      return;
    }
    console.info('send success');
  });
});
```

#### \[h2\]send10+

send(data: string | ArrayBuffer): Promise<void>

在TLSSocketServer通信连接成功之后，向服务端发送消息，使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| data | string | ArrayBuffer | 是 | TLSSocketServer发送数据所需要的参数。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 以Promise形式返回，成功返回空，失败返回错误码，错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2303501 | SSL is null. |
| 2303503 | An error occurred when writing data on the TLS socket. |
| 2303505 | An error occurred in the TLS system call. |
| 2303506 | Failed to close the TLS connection. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});

tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.send('Hello, client!').then(() => {
    console.info('send success');
  }).catch((err: BusinessError) => {
    console.error('send fail');
  });
});
```

#### \[h2\]close10+

close(callback: AsyncCallback<void>): void

在与TLSSocketServer通信连接成功之后，断开连接，使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | 是 | 回调函数，成功返回空，失败返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2303501 | SSL is null. |
| 2303505 | An error occurred in the TLS system call. |
| 2303506 | Failed to close the TLS connection. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});

tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.close((err: BusinessError) => {
    if (err) {
      console.error('close fail');
      return;
    }
    console.info('close success');
  });
});
```

#### \[h2\]close10+

close(): Promise<void>

在与TLSSocketServer通信连接成功之后，断开连接，使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 以Promise形式返回，成功返回空。失败返回错误码，错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 2303501 | SSL is null. |
| 2303505 | An error occurred in the TLS system call. |
| 2303506 | Failed to close the TLS connection. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.close().then(() => {
    console.info('close success');
  }).catch((err: BusinessError) => {
    console.error('close fail');
  });
});
```

#### \[h2\]getRemoteAddress10+

getRemoteAddress(callback: AsyncCallback<NetAddress>): void

在TLSSocketServer通信连接成功之后，获取对端Socket地址。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[NetAddress](#netaddress)\> | 是 | 回调函数。成功返回对端的socket地址，失败返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2303188 | Socket operation on non-socket. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.getRemoteAddress((err: BusinessError, data: socket.NetAddress) => {
    if (err) {
      console.error('getRemoteAddress fail');
      return;
    }
    console.info('getRemoteAddress success:' + JSON.stringify(data));
  });
});
```

#### \[h2\]getRemoteAddress10+

getRemoteAddress(): Promise<NetAddress>

在TLSSocketServer通信连接成功之后，获取对端Socket地址。使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[NetAddress](#netaddress)\> | 以Promise形式返回获取对端socket地址的结果。失败返回错误码，错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 2303188 | Socket operation on non-socket. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.getRemoteAddress().then((data: socket.NetAddress) => {
    console.info('getRemoteAddress success:' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error("failed" + err);
  });
});
```

#### \[h2\]getRemoteCertificate10+

getRemoteCertificate(callback: AsyncCallback<[X509CertRawData](#x509certrawdata9)\>): void

在TLSSocketServer通信连接成功之后，获取对端的数字证书，该接口只适用于客户端向服务端发送证书时，使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[X509CertRawData](#x509certrawdata9)\> | 是 | 回调函数，返回对端的证书。失败返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2303501 | SSL is null. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.getRemoteCertificate((err: BusinessError, data: socket.X509CertRawData) => {
    if (err) {
      console.error("getRemoteCertificate callback error: " + err);
    } else {
      const decoder = util.TextDecoder.create();
      const str = decoder.decodeToString(data.data);
      console.info("getRemoteCertificate callback: " + str);
    }
  });
});
```

#### \[h2\]getRemoteCertificate10+

getRemoteCertificate():Promise<[X509CertRawData](#x509certrawdata9)\>

在TLSSocketServer通信连接成功之后，获取对端的数字证书，该接口只适用于客户端向服务端发送证书时，使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[X509CertRawData](#x509certrawdata9)\> | 以Promise形式返回对端的数字证书的结果。失败返回错误码，错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 2303501 | SSL is null. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.getRemoteCertificate().then((data: socket.X509CertRawData) => {
    const decoder = util.TextDecoder.create();
    const str = decoder.decodeToString(data.data);
    console.info("getRemoteCertificate success: " + str);
  }).catch((err: BusinessError) => {
    console.error("failed" + err);
  });
});
```

#### \[h2\]getCipherSuite10+

getCipherSuite(callback: AsyncCallback<Array<string>>): void

在TLSSocketServer通信连接成功之后，获取通信双方协商后的加密套件，使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<string>> | 是 | 回调函数，返回通信双方支持的加密套件。失败返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2303501 | SSL is null. |
| 2303502 | An error occurred when reading data on the TLS socket. |
| 2303505 | An error occurred in the TLS system call. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.getCipherSuite((err: BusinessError, data: Array<string>) => {
    if (err) {
      console.error("getCipherSuite callback error = " + err);
    } else {
      console.info("getCipherSuite callback = " + data);
    }
  });
});
```

#### \[h2\]getCipherSuite10+

getCipherSuite(): Promise<Array<string>>

在TLSSocketServer通信连接成功之后，获取通信双方协商后的加密套件，使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<string>> | 以Promise形式返回通信双方支持的加密套件。失败返回错误码，错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 2303501 | SSL is null. |
| 2303502 | An error occurred when reading data on the TLS socket. |
| 2303505 | An error occurred in the TLS system call. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.getCipherSuite().then((data: Array<string>) => {
    console.info('getCipherSuite success:' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error("failed" + err);
  });
});
```

#### \[h2\]getSignatureAlgorithms10+

getSignatureAlgorithms(callback: AsyncCallback<Array<string>>): void

在TLSSocketServer通信连接成功之后，获取通信双方协商后签名算法，使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<string>> | 是 | 回调函数，返回双方支持的签名算法。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |
| 2303501 | SSL is null. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.getSignatureAlgorithms((err: BusinessError, data: Array<string>) => {
    if (err) {
      console.error("getSignatureAlgorithms callback error = " + err);
    } else {
      console.info("getSignatureAlgorithms callback = " + data);
    }
  });
});
```

#### \[h2\]getSignatureAlgorithms10+

getSignatureAlgorithms(): Promise<Array<string>>

在TLSSocketServer通信连接成功之后，获取通信双方协商后的签名算法，使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<string>> | 以Promise形式返回获取到的双方支持的签名算法。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 2303501 | SSL is null. |
| 2300002 | System internal error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.getSignatureAlgorithms().then((data: Array<string>) => {
    console.info("getSignatureAlgorithms success" + data);
  }).catch((err: BusinessError) => {
    console.error("failed" + err);
  });
});
```

#### \[h2\]getLocalAddress12+

getLocalAddress(): Promise<NetAddress>

获取TLSSocketConnection连接的本地Socket地址。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/zxgprUs1TzuUoXABA6YsKw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=56369DAB1FC24CB00907AB77FF30E9499E99704DBF845BE1D693760467D5DA6C)

在TLSSocketServer通信连接成功之后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[NetAddress](#netaddress)\> | 以Promise形式返回获取本地socket地址的结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 2300002 | System internal error. |
| 2301009 | Bad file descriptor. |
| 2303188 | Socket operation on non-socket. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});

tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.getLocalAddress().then((localAddress: socket.NetAddress) => {
    console.info("Family IP Port: " + JSON.stringify(localAddress));
  }).catch((err: BusinessError) => {
    console.error("TLS Client Get Family IP Port failed, error: " + JSON.stringify(err));
  })
});
```

#### \[h2\]getSocketFd23+

getSocketFd(): Promise<number>

获取TLSSocketConnection连接的文件描述符。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/oOTpEBvRQu-xs0Ga6u6bJQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014823Z&HW-CC-Expire=86400&HW-CC-Sign=513BB399C9D90B74748A985833288AAA4604AC6BF585169FA330242F34FBB3F9)

-   在TLSSocketServer通信连接成功之后，才可调用此方法。
-   连接断开、Socket已关闭（如调用close后）等异常情况下调用本接口会返回-1。
-   文件描述符的生命周期由系统管理，应用可以通过[close](#close10-2)方法关闭Socket连接，避免直接操作文件描述符进行关闭。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | Promise对象，返回Socket的文件描述符。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | Permission denied. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen success");
  tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
    client.getSocketFd().then((fd: number) => {
      console.info(`Socket FD：${fd}`);
    }).catch((err: BusinessError) => {
      console.error(`getSocketFd fail: ${err.message}, errorCode: ${err.code}`);
    })
  });
}).catch((err: BusinessError) => {
  console.error(`listen failed: ${JSON.stringify(err)}`);
});
```

#### \[h2\]on('message')10+

on(type: 'message', callback: Callback<SocketMessageInfo>): void

订阅TLSSocketConnection连接的接收消息事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅的事件类型。'message'：接收消息事件。 |
| callback | Callback<[SocketMessageInfo](#socketmessageinfo11)\> | 是 | 回调函数。成功时返回TLSSocketConnection连接信息，失败时返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});

tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.on('message', (value: socket.SocketMessageInfo) => {
    let messageView = '';
    let uint8Array = new Uint8Array(value.message);
    for (let i: number = 0; i < value.message.byteLength; i++) {
      let messages = uint8Array[i];
      let message = String.fromCharCode(messages);
      messageView += message;
    }
    console.info('on message message: ' + JSON.stringify(messageView));
    console.info('remoteInfo: ' + JSON.stringify(value.remoteInfo));
  });
});
```

#### \[h2\]off('message')10+

off(type: 'message', callback?: Callback<SocketMessageInfo>): void

取消订阅TLSSocketConnection连接的接收消息事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅的事件类型。'message'：接收消息事件。 |
| callback | Callback<[SocketMessageInfo](#socketmessageinfo11)\> | 否 | 回调函数。成功时返回TLSSocketConnection连接信息，失败时返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});

let callback = (value: socket.SocketMessageInfo) => {
  let messageView = '';
  for (let i: number = 0; i < value.message.byteLength; i++) {
    let uint8Array = new Uint8Array(value.message)
    let messages = uint8Array[i]
    let message = String.fromCharCode(messages);
    messageView += message;
  }
  console.info('on message message: ' + JSON.stringify(messageView));
  console.info('remoteInfo: ' + JSON.stringify(value.remoteInfo));
}
tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.on('message', callback);
  // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
  client.off('message', callback);
  client.off('message');
});
```

#### \[h2\]on('close')10+

on(type: 'close', callback: Callback<void>): void

订阅TLSSocketConnection的关闭事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅的事件类型。'close'：关闭事件。 |
| callback | Callback<void> | 是 | 回调函数。成功时返回空，失败时返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});
tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.on('close', () => {
    console.info("on close success")
  });
});
```

#### \[h2\]off('close')10+

off(type: 'close', callback?: Callback<void>): void

取消订阅TLSSocketConnection的关闭事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅的事件类型。'close'：关闭事件。 |
| callback | Callback<void> | 否 | 回调函数。成功时返回空，失败时返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});

let callback = () => {
  console.info("on close success");
}
tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.on('close', callback);
  // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
  client.off('close', callback);
  client.off('close');
});
```

#### \[h2\]on('error')10+

on(type: 'error', callback: ErrorCallback): void

订阅TLSSocketConnection连接的error事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅的事件类型。'error'：error事件。 |
| callback | ErrorCallback | 是 | 回调函数。成功时返回空，失败时返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});

tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.on('error', (err: BusinessError) => {
    console.error("on error, err:" + JSON.stringify(err))
  });
});
```

#### \[h2\]off('error')10+

off(type: 'error', callback?: ErrorCallback): void

取消订阅TLSSocketConnection连接的error事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅的事件类型。'error'：error事件。 |
| callback | ErrorCallback | 否 | 回调函数。成功时返回空，失败时返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. |

**示例：**

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
let netAddress: socket.NetAddress = {
  address: '192.168.xx.xxx',
  port: 8080
}
let tlsSecureOptions: socket.TLSSecureOptions = {
  key: "xxxx",
  cert: "xxxx",
  ca: ["xxxx"],
  password: "xxxx",
  protocols: socket.Protocol.TLSv12,
  useRemoteCipherPrefer: true,
  signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
  cipherSuite: "AES256-SHA256"
}
let tlsConnectOptions: socket.TLSConnectOptions = {
  address: netAddress,
  secureOptions: tlsSecureOptions,
  ALPNProtocols: ["spdy/1", "http/1.1"]
}
tlsServer.listen(tlsConnectOptions).then(() => {
  console.info("listen callback success");
}).catch((err: BusinessError) => {
  console.error("failed" + err);
});

let callback = (err: BusinessError) => {
  console.error("on error, err:" + JSON.stringify(err));
}
tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
  client.on('error', callback);
  // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
  client.off('error', callback);
  client.off('error');
});
```

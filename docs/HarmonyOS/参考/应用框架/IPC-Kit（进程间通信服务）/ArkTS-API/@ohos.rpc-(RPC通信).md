---
title: "@ohos.rpc (RPC通信)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-rpc"
menu_path:
  - "参考"
  - "应用框架"
  - "IPC Kit（进程间通信服务）"
  - "ArkTS API"
  - "@ohos.rpc (RPC通信)"
captured_at: "2026-04-17T01:48:16.094Z"
---

# @ohos.rpc (RPC通信)

本模块提供进程间通信能力，包括设备内的进程间通信（IPC）和设备间的进程间通信（RPC），前者基于Binder驱动，后者基于软总线驱动。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/RXlVrILoQPGgemvouTX9uw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=00DDEB34C524B821F13A2C8EDDB88E7D09F36ABDD35A5A5FD78183C72415F46A)

-   本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
    
-   本模块从API version 9开始支持异常返回功能。
    

#### 导入模块

```ts
import { rpc } from '@kit.IPCKit';
```

#### ErrorCode9+

从API version 9起，IPC支持异常返回功能。错误码对应数值及含义如下。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| CHECK\_PARAM\_ERROR | 401 | 检查参数失败。 |
| OS\_MMAP\_ERROR | 1900001 | 执行系统调用mmap失败。 |
| OS\_IOCTL\_ERROR | 1900002 | 在共享内存文件描述符上执行系统调用ioctl失败。 |
| WRITE\_TO\_ASHMEM\_ERROR | 1900003 | 向共享内存写数据失败。 |
| READ\_FROM\_ASHMEM\_ERROR | 1900004 | 从共享内存读数据失败。 |
| ONLY\_PROXY\_OBJECT\_PERMITTED\_ERROR | 1900005 | 只有proxy对象允许该操作。 |
| ONLY\_REMOTE\_OBJECT\_PERMITTED\_ERROR | 1900006 | 只有remote对象允许该操作。 |
| COMMUNICATION\_ERROR | 1900007 | 和远端对象进行进程间通信失败。 |
| PROXY\_OR\_REMOTE\_OBJECT\_INVALID\_ERROR | 1900008 | 非法的代理对象或者远端对象。 |
| WRITE\_DATA\_TO\_MESSAGE\_SEQUENCE\_ERROR | 1900009 | 向MessageSequence写数据失败。 |
| READ\_DATA\_FROM\_MESSAGE\_SEQUENCE\_ERROR | 1900010 | 读取MessageSequence数据失败。 |
| PARCEL\_MEMORY\_ALLOC\_ERROR | 1900011 | 序列化过程中内存分配失败。 |
| CALL\_JS\_METHOD\_ERROR | 1900012 | 执行JS回调方法失败。 |
| OS\_DUP\_ERROR | 1900013 | 执行系统调用dup失败。 |

#### TypeCode12+

从API version 12起，IPC新增[writeArrayBuffer](#writearraybuffer12)和[readArrayBuffer](#readarraybuffer12)方法传递ArrayBuffer数据，传递数据时通过具体类型值来分辨业务是以哪一种TypedArray去进行数据的读写。类型码对应数值及含义如下。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| INT8\_ARRAY | 0 | TypedArray类型为INT8\_ARRAY。 |
| UINT8\_ARRAY | 1 | TypedArray类型为UINT8\_ARRAY。 |
| INT16\_ARRAY | 2 | TypedArray类型为INT16\_ARRAY。 |
| UINT16\_ARRAY | 3 | TypedArray类型为UINT16\_ARRAY。 |
| INT32\_ARRAY | 4 | TypedArray类型为INT32\_ARRAY。 |
| UINT32\_ARRAY | 5 | TypedArray类型为UINT32\_ARRAY。 |
| FLOAT32\_ARRAY | 6 | TypedArray类型为FLOAT32\_ARRAY。 |
| FLOAT64\_ARRAY | 7 | TypedArray类型为FLOAT64\_ARRAY。 |
| BIGINT64\_ARRAY | 8 | TypedArray类型为BIGINT64\_ARRAY。 |
| BIGUINT64\_ARRAY | 9 | TypedArray类型为BIGUINT64\_ARRAY。 |

#### MessageSequence9+

在RPC或IPC过程中，发送方可以使用MessageSequence提供的写方法，将待发送的数据以特定格式写入该对象。接收方可以使用MessageSequence提供的读方法从该对象中读取特定格式的数据。数据格式包括：基础类型及数组、IPC对象、接口描述符和自定义序列化对象。

#### \[h2\]create9+

static create(): MessageSequence

静态方法，创建MessageSequence对象。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [MessageSequence](#messagesequence9) | 返回创建的MessageSequence对象。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  hilog.info(0x0000, 'testTag', 'data is ' + data);

  // 当MessageSequence对象不再使用，由业务主动调用reclaim方法去释放资源。
  data.reclaim();
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]reclaim9+

reclaim(): void

释放不再使用的MessageSequence对象。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let reply = rpc.MessageSequence.create();
  reply.reclaim();
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]writeRemoteObject9+

writeRemoteObject(obj: IRemoteObject): void

序列化远程对象并将其写入[MessageSequence](#messagesequence9)对象。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| obj | [IRemoteObject](#iremoteobject) | 是 | 要序列化并写入MessageSequence的远程对象。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900008 | The proxy or remote object is invalid. |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    // 根据业务实际逻辑，进行相应处理
    return true;
  }
}

try {
  let data = rpc.MessageSequence.create();
  let testRemoteObject = new TestRemoteObject("testObject");
  data.writeRemoteObject(testRemoteObject);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]readRemoteObject9+

readRemoteObject(): IRemoteObject

从MessageSequence读取远程对象。此方法用于反序列化MessageSequence对象以生成IRemoteObject。远程对象按写入MessageSequence的顺序读取。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [IRemoteObject](#iremoteobject) | 读取到的远程对象。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 1900008 | The proxy or remote object is invalid. |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    // 根据业务实际逻辑，进行相应处理
    return true;
  }
}

try {
  let data = rpc.MessageSequence.create();
  let testRemoteObject = new TestRemoteObject("testObject");
  data.writeRemoteObject(testRemoteObject);
  let proxy = data.readRemoteObject();
  hilog.info(0x0000, 'testTag', 'readRemoteObject is ' + proxy);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]writeInterfaceToken9+

writeInterfaceToken(token: string): void

将接口描述符写入MessageSequence对象，远端对象可使用该信息校验本次通信。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| token | string | 是 | 字符串类型描述符，其长度应小于40960字节。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.The string length is greater than or equal to 40960 bytes;

4.The number of bytes copied to the buffer is different from the length of the obtained string.

 |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeInterfaceToken("aaa");
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]readInterfaceToken9+

readInterfaceToken(): string

从MessageSequence对象中读取接口描述符，接口描述符按写入MessageSequence的顺序读取，本地对象可使用该信息检验本次通信。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 返回读取到的接口描述符。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeInterfaceToken("aaa");
  let interfaceToken = data.readInterfaceToken();
  hilog.info(0x0000, 'testTag', 'RpcServer: interfaceToken is ' + interfaceToken);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]getSize9+

getSize(): number

获取当前创建的MessageSequence对象的数据大小。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 获取的MessageSequence实例的数据大小。以字节为单位。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  let size = data.getSize();
  hilog.info(0x0000, 'testTag', 'size is ' + size);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]getCapacity9+

getCapacity(): number

获取当前MessageSequence对象的容量大小。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 获取的MessageSequence实例的容量大小。以字节为单位。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  let result = data.getCapacity();
  hilog.info(0x0000, 'testTag', 'capacity is ' + result);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]setSize9+

setSize(size: number): void

设置MessageSequence对象中包含的数据大小。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| size | number | 是 | MessageSequence实例的数据大小。以字节为单位。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeString('Hello World');
  data.setSize(16);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]setCapacity9+

setCapacity(size: number): void

设置MessageSequence对象的存储容量。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| size | number | 是 | MessageSequence实例的存储容量。以字节为单位。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900009 | Failed to write data to the message sequence. |
| 1900011 | Memory allocation failed. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.setCapacity(100);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]getWritableBytes9+

getWritableBytes(): number

获取MessageSequence的可写字节空间大小。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 获取到的MessageSequence实例的可写字节空间。以字节为单位。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.setCapacity(100);
  let getWritableBytes = data.getWritableBytes();
  hilog.info(0x0000, 'testTag', 'RpcServer: getWritableBytes is ' + getWritableBytes);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]getReadableBytes9+

getReadableBytes(): number

获取MessageSequence的可读字节空间。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 获取到的MessageSequence实例的可读字节空间。以字节为单位。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeString("hello world");
  let result = data.getReadableBytes();
  hilog.info(0x0000, 'testTag', 'RpcServer: getReadableBytes is ' + result);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]getReadPosition9+

getReadPosition(): number

获取MessageSequence的读位置。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回MessageSequence实例中的当前读取位置。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeString("hello world");
  let readPos = data.getReadPosition();
  hilog.info(0x0000, 'testTag', 'readPos is ' + readPos);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]getWritePosition9+

getWritePosition(): number

获取MessageSequence的写位置。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回MessageSequence实例中的当前写入位置。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeInt(10);
  let bwPos = data.getWritePosition();
  hilog.info(0x0000, 'testTag', 'bwPos is ' + bwPos);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]rewindRead9+

rewindRead(pos: number): void

重新偏移读取位置到指定的位置。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| pos | number | 是 | 开始读取数据的目标位置。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeInt(12);
  data.writeString("sequence");
  let number = data.readInt();
  hilog.info(0x0000, 'testTag', 'number is ' + number);
  data.rewindRead(0);
  let number2 = data.readInt();
  hilog.info(0x0000, 'testTag', 'rewindRead is ' + number2);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]rewindWrite9+

rewindWrite(pos: number): void

重新偏移写位置到指定的位置。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| pos | number | 是 | 开始写入数据的目标位置。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeInt(4);
  data.rewindWrite(0);
  data.writeInt(5);
  let number = data.readInt();
  hilog.info(0x0000, 'testTag', 'rewindWrite is: ' + number);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]writeByte9+

writeByte(val: number): void

将字节值写入MessageSequence实例。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| val | number | 是 | 要写入的字节值。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeByte(2);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]readByte9+

readByte(): number

从MessageSequence实例中读取字节值。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回字节值。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeByte(2);
  let ret = data.readByte();
  hilog.info(0x0000, 'testTag', 'readByte is: ' +  ret);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]writeShort9+

writeShort(val: number): void

将短整数值写入MessageSequence实例。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| val | number | 是 | 要写入的短整数值。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeShort(8);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]readShort9+

readShort(): number

从MessageSequence实例中读取短整数值。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回短整数值。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeShort(8);
  let ret = data.readShort();
  hilog.info(0x0000, 'testTag', 'readShort is ' + ret);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]writeInt9+

writeInt(val: number): void

将整数值写入MessageSequence实例。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| val | number | 是 | 要写入的整数值。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeInt(10);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]readInt9+

readInt(): number

从MessageSequence实例中读取整数值。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回整数值。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeInt(10);
  let ret = data.readInt();
  hilog.info(0x0000, 'testTag', 'readInt is ' + ret);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]writeLong9+

writeLong(val: number): void

将长整数值写入MessageSequence实例。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| val | number | 是 | 要写入的长整数值。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeLong(10000);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]readLong9+

readLong(): number

从MessageSequence实例中读取长整数值。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回长整数值。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeLong(10000);
  let ret = data.readLong();
  hilog.info(0x0000, 'testTag', 'readLong is ' + ret);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]writeFloat9+

writeFloat(val: number): void

将双精度浮点值写入MessageSequence实例。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| val | number | 是 | 要写入的双精度浮点值。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeFloat(1.2);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]readFloat9+

readFloat(): number

从MessageSequence实例中读取双精度浮点值。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回双精度浮点值。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeFloat(1.2);
  let ret = data.readFloat();
  hilog.info(0x0000, 'testTag', 'readFloat is ' + ret);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]writeDouble9+

writeDouble(val: number): void

将双精度浮点值写入MessageSequence实例。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| val | number | 是 | 要写入的双精度浮点值。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeDouble(10.2);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]readDouble9+

readDouble(): number

从MessageSequence实例中读取双精度浮点值。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回双精度浮点值。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeDouble(10.2);
  let ret = data.readDouble();
  hilog.info(0x0000, 'testTag', 'readDouble is ' +  ret);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]writeBoolean9+

writeBoolean(val: boolean): void

将布尔值写入MessageSequence实例。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| val | boolean | 是 | 要写入的布尔值。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeBoolean(false);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]readBoolean9+

readBoolean(): boolean

从MessageSequence实例中读取布尔值。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 返回读取到的布尔值。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeBoolean(false);
  let ret = data.readBoolean();
  hilog.info(0x0000, 'testTag', 'readBoolean is ' + ret);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]writeChar9+

writeChar(val: number): void

将单个字符值写入MessageSequence实例。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| val | number | 是 | 要写入的单个字符值。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeChar(97);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]readChar9+

readChar(): number

从MessageSequence实例中读取单个字符值。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回单个字符值。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeChar(97);
  let ret = data.readChar();
  hilog.info(0x0000, 'testTag', 'readChar is ' + ret);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]writeString9+

writeString(val: string): void

将字符串值写入MessageSequence实例。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| val | string | 是 | 要写入的字符串值，其长度应小于40960字节。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.The string length is greater than or equal to 40960 bytes;

4.The number of bytes copied to the buffer is different from the length of the obtained string.

 |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeString('abc');
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]readString9+

readString(): string

从MessageSequence实例中读取字符串值。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 返回字符串值。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeString('abc');
  let ret = data.readString();
  hilog.info(0x0000, 'testTag', 'readString is ' + ret);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]writeParcelable9+

writeParcelable(val: Parcelable): void

将自定义序列化对象写入MessageSequence实例。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| val | [Parcelable](#parcelable9) | 是 | 要写入的可序列对象。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

class MyParcelable implements rpc.Parcelable {
  num: number = 0;
  str: string = '';
  constructor( num: number, str: string) {
    this.num = num;
    this.str = str;
  }
  marshalling(messageSequence: rpc.MessageSequence): boolean {
    messageSequence.writeInt(this.num);
    messageSequence.writeString(this.str);
    return true;
  }
  unmarshalling(messageSequence: rpc.MessageSequence): boolean {
    this.num = messageSequence.readInt();
    this.str = messageSequence.readString();
    return true;
  }
}

try {
  let parcelable = new MyParcelable(1, "aaa");
  let data = rpc.MessageSequence.create();
  data.writeParcelable(parcelable);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]readParcelable9+

readParcelable(dataIn: Parcelable): void

从MessageSequence实例中读取成员变量到指定的对象（dataIn）。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| dataIn | [Parcelable](#parcelable9) | 是 | 需要从MessageSequence读取成员变量的对象。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect.

 |
| 1900010 | Failed to read data from the message sequence. |
| 1900012 | Failed to call the JS callback function. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

class MyParcelable implements rpc.Parcelable {
  num: number = 0;
  str: string = '';
  constructor( num: number, str: string) {
    this.num = num;
    this.str = str;
  }
  marshalling(messageSequence: rpc.MessageSequence): boolean {
    messageSequence.writeInt(this.num);
    messageSequence.writeString(this.str);
    return true;
  }
  unmarshalling(messageSequence: rpc.MessageSequence): boolean {
    this.num = messageSequence.readInt();
    this.str = messageSequence.readString();
    return true;
  }
}

try {
  let parcelable = new MyParcelable(1, "aaa");
  let data = rpc.MessageSequence.create();
  data.writeParcelable(parcelable);
  let ret = new MyParcelable(0, "");
  data.readParcelable(ret);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]writeByteArray9+

writeByteArray(byteArray: number\[\]): void

将字节数组写入MessageSequence实例。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| byteArray | number\[\] | 是 | 要写入的字节数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match;

4.The element does not exist in the array.

5.The type of the element in the array is incorrect.

 |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  let ByteArrayVar = [1, 2, 3, 4, 5];
  data.writeByteArray(ByteArrayVar);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]readByteArray9+

readByteArray(dataIn: number\[\]): void

从MessageSequence实例中读取字节数组，并将其写入到创建的空数组中。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| dataIn | number\[\] | 是 | 要读取的字节数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match.

 |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  let ByteArrayVar = [1, 2, 3, 4, 5];
  data.writeByteArray(ByteArrayVar);
  let array: Array<number> = new Array(5);
  data.readByteArray(array);
  hilog.info(0x0000, 'testTag', 'readByteArray is  ' + array);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]readByteArray9+

readByteArray(): number\[\]

从MessageSequence实例中读取字节数组。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number\[\] | 返回字节数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  let ByteArrayVar = [1, 2, 3, 4, 5];
  data.writeByteArray(ByteArrayVar);
  let array = data.readByteArray();
  hilog.info(0x0000, 'testTag', 'readByteArray is  ' + array);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]writeShortArray9+

writeShortArray(shortArray: number\[\]): void

将短整数数组写入MessageSequence实例。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| shortArray | number\[\] | 是 | 要写入的短整数数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match;

4.The element does not exist in the array;

5.The type of the element in the array is incorrect.

 |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeShortArray([11, 12, 13]);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]readShortArray9+

readShortArray(dataIn: number\[\]): void

从MessageSequence实例中读取短整数数组，并将其写入到创建的空数组中。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| dataIn | number\[\] | 是 | 要读取的短整数数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match.

 |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeShortArray([11, 12, 13]);
  let array: Array<number> = new Array(3);
  data.readShortArray(array);
  hilog.info(0x0000, 'testTag', 'readShortArray is  ' + array);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]readShortArray9+

readShortArray(): number\[\]

从MessageSequence实例中读取短整数数组。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number\[\] | 返回短整数数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeShortArray([11, 12, 13]);
  let array = data.readShortArray();
  hilog.info(0x0000, 'testTag', 'readShortArray is ' + array);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]writeIntArray9+

writeIntArray(intArray: number\[\]): void

将整数数组写入MessageSequence实例。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| intArray | number\[\] | 是 | 要写入的整数数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match;

4.The element does not exist in the array;

5.The type of the element in the array is incorrect.

 |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeIntArray([100, 111, 112]);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]readIntArray9+

readIntArray(dataIn: number\[\]): void

从MessageSequence实例中读取整数数组，并将其写入到创建的空数组中。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| dataIn | number\[\] | 是 | 要读取的整数数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match.

 |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeIntArray([100, 111, 112]);
  let array: Array<number> = new Array(3);
  data.readIntArray(array);
  hilog.info(0x0000, 'testTag', 'readIntArray is  ' + array);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]readIntArray9+

readIntArray(): number\[\]

从MessageSequence实例中读取整数数组。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number\[\] | 返回整数数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeIntArray([100, 111, 112]);
  let array = data.readIntArray();
  hilog.info(0x0000, 'testTag', 'readIntArray is ' + array);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]writeLongArray9+

writeLongArray(longArray: number\[\]): void

将长整数数组写入MessageSequence实例。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| longArray | number\[\] | 是 | 要写入的长整数数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match;

4.The element does not exist in the array;

5.The type of the element in the array is incorrect.

 |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeLongArray([1111, 1112, 1113]);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]readLongArray9+

readLongArray(dataIn: number\[\]): void

从MessageSequence实例中读取的长整数数组，并将其写入到创建的空数组中。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| dataIn | number\[\] | 是 | 要读取的长整数数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match.

 |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeLongArray([1111, 1112, 1113]);
  let array: Array<number> = new Array(3);
  data.readLongArray(array);
  hilog.info(0x0000, 'testTag', 'readLongArray is ' + array);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]readLongArray9+

readLongArray(): number\[\]

从MessageSequence实例中读取所有的长整数数组。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number\[\] | 返回长整数数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeLongArray([1111, 1112, 1113]);
  let array = data.readLongArray();
  hilog.info(0x0000, 'testTag', 'readLongArray is ' + array);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]writeFloatArray9+

writeFloatArray(floatArray: number\[\]): void

将双精度浮点数组写入MessageSequence实例。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| floatArray | number\[\] | 是 | 要写入的双精度浮点数组。由于系统内部对float类型的数据是按照double处理的，使用时对于数组所占的总字节数应按照double类型来计算。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match;

4.The element does not exist in the array;

5.The type of the element in the array is incorrect.

 |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeFloatArray([1.2, 1.3, 1.4]);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]readFloatArray9+

readFloatArray(dataIn: number\[\]): void

从MessageSequence实例中读取双精度浮点数组，并将其写入到创建的空数组中。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| dataIn | number\[\] | 是 | 要读取的双精度浮点数组。由于系统内部对float类型的数据是按照double处理的，使用时对于数组所占的总字节数应按照double类型来计算。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match.

 |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeFloatArray([1.2, 1.3, 1.4]);
  let array: Array<number> = new Array(3);
  data.readFloatArray(array);
  hilog.info(0x0000, 'testTag', 'readFloatArray is ' + array);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]readFloatArray9+

readFloatArray(): number\[\]

从MessageSequence实例中读取双精度浮点数组。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number\[\] | 返回双精度浮点数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeFloatArray([1.2, 1.3, 1.4]);
  let array = data.readFloatArray();
  hilog.info(0x0000, 'testTag', 'readFloatArray is ' + array);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]writeDoubleArray9+

writeDoubleArray(doubleArray: number\[\]): void

将双精度浮点数组写入MessageSequence实例。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| doubleArray | number\[\] | 是 | 要写入的双精度浮点数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match;

4.The element does not exist in the array;

5.The type of the element in the array is incorrect.

 |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeDoubleArray([11.1, 12.2, 13.3]);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]readDoubleArray9+

readDoubleArray(dataIn: number\[\]): void

从MessageSequence实例中读取双精度浮点数组，并将其写入到创建的空数组中。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| dataIn | number\[\] | 是 | 要读取的双精度浮点数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match.

 |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeDoubleArray([11.1, 12.2, 13.3]);
  let array: Array<number> = new Array(3);
  data.readDoubleArray(array);
  hilog.info(0x0000, 'testTag', 'readDoubleArray is ' + array);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]readDoubleArray9+

readDoubleArray(): number\[\]

从MessageSequence实例中读取所有双精度浮点数组。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number\[\] | 返回双精度浮点数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeDoubleArray([11.1, 12.2, 13.3]);
  let array = data.readDoubleArray();
  hilog.info(0x0000, 'testTag', 'readDoubleArray is ' + array);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]writeBooleanArray9+

writeBooleanArray(booleanArray: boolean\[\]): void

将布尔数组写入MessageSequence实例。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| booleanArray | boolean\[\] | 是 | 要写入的布尔数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match;

4.The element does not exist in the array.

 |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeBooleanArray([false, true, false]);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]readBooleanArray9+

readBooleanArray(dataIn: boolean\[\]): void

从MessageSequence实例中读取布尔数组，并将其写入到创建的空数组中。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| dataIn | boolean\[\] | 是 | 要读取的布尔数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match.

 |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeBooleanArray([false, true, false]);
  let array: Array<boolean> = new Array(3);
  data.readBooleanArray(array);
  hilog.info(0x0000, 'testTag', 'readBooleanArray is ' + array);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]readBooleanArray9+

readBooleanArray(): boolean\[\]

从MessageSequence实例中读取所有布尔数组。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean\[\] | 返回布尔数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeBooleanArray([false, true, false]);
  let array = data.readBooleanArray();
  hilog.info(0x0000, 'testTag', 'readBooleanArray is ' + array);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]writeCharArray9+

writeCharArray(charArray: number\[\]): void

将单个字符数组写入MessageSequence实例。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| charArray | number\[\] | 是 | 要写入的单个字符数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match;

4.The element does not exist in the array.

 |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeCharArray([97, 98, 88]);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]readCharArray9+

readCharArray(dataIn: number\[\]): void

从MessageSequence实例中读取单个字符数组，并将其写入到创建的空数组中。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| dataIn | number\[\] | 是 | 要读取的单个字符数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match.

 |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeCharArray([97, 98, 88]);
  let array: Array<number> = new Array(3);
  data.readCharArray(array);
  hilog.info(0x0000, 'testTag', 'readCharArray is ' + array);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]readCharArray9+

readCharArray(): number\[\]

从MessageSequence实例中读取单个字符数组。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number\[\] | 返回单个字符数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeCharArray([97, 98, 88]);
  let array = data.readCharArray();
  hilog.info(0x0000, 'testTag', 'readCharArray is ' + array);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]writeStringArray9+

writeStringArray(stringArray: string\[\]): void

将字符串数组写入MessageSequence实例。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| stringArray | string\[\] | 是 | 要写入的字符串数组，数组单个元素的长度应小于40960字节。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match;

4.The string length is greater than or equal to 40960 bytes;

5.The number of bytes copied to the buffer is different from the length of the obtained string.

 |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeStringArray(["abc", "def"]);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]readStringArray9+

readStringArray(dataIn: string\[\]): void

从MessageSequence实例中读取字符串数组，并将其写入到创建的空数组中。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| dataIn | string\[\] | 是 | 要读取的字符串数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match.

 |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeStringArray(["abc", "def"]);
  let array: Array<string> = new Array(2);
  data.readStringArray(array);
  hilog.info(0x0000, 'testTag', 'readStringArray is ' + array);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]readStringArray9+

readStringArray(): string\[\]

从MessageSequence实例中读取字符串数组。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string\[\] | 返回字符串数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeStringArray(["abc", "def"]);
  let array = data.readStringArray();
  hilog.info(0x0000, 'testTag', 'readStringArray is ' + array);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]writeNoException9+

writeNoException(): void

向MessageSequence写入“指示未发生异常”的信息。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    if (code === 1) {
      hilog.info(0x0000, 'testTag', 'RpcServer: onRemoteMessageRequest called');
      try {
        reply.writeNoException();
      } catch (error) {
        let e: BusinessError = error as BusinessError;
        hilog.error(0x0000, 'testTag', 'rpc write no exception fail, errorCode ' + e.code);
        hilog.error(0x0000, 'testTag', 'rpc write no exception fail, errorMessage ' + e.message);
      }
      return true;
    } else {
      hilog.error(0x0000, 'testTag', 'RpcServer: unknown code: ' + code);
      return false;
    }
  }
}
```

#### \[h2\]readException9+

readException(): void

从MessageSequence中读取异常。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/ujDanKK3QL-k8RKoLzrBqQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=909D0849BC465D5DBFC52DCA4DF8BFDD703F4ABA30498ADCAD9F2AF620E16A11)

在本文档的示例中，通过this.getUIContext().getHostContext()来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
// FA模型需要从@kit.AbilityKit导入featureAbility
// import { featureAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { Want, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let proxy: rpc.IRemoteObject | undefined;
let connect: common.ConnectOptions = {
  onConnect: (elementName, remoteProxy) => {
    hilog.info(0x0000, 'testTag', 'js onConnect called');
    proxy = remoteProxy;
  },
  onDisconnect: (elementName) => {
    hilog.info(0x0000, 'testTag', 'onDisconnect');
  },
  onFailed: () => {
    hilog.info(0x0000, 'testTag', 'onFailed');
  }
};
let want: Want = {
  // 获取服务端包名和ability名称
  bundleName: "com.ohos.server",
  abilityName: "com.ohos.server.EntryAbility",
};

// FA模型使用此方法连接服务
// FA.connectAbility(want,connect);

// 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
// 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
let connectionId = context.connectServiceExtensionAbility(want, connect);
```

上述onConnect回调函数中的proxy对象需要等ability异步连接成功后才会被赋值，然后才可调用proxy对象的sendMessageRequest接口方法发送消息

```ts
import { rpc } from '@kit.IPCKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
  
try {
  let option = new rpc.MessageOption();
  let data = rpc.MessageSequence.create();
  let reply = rpc.MessageSequence.create();
  data.writeNoException();
  data.writeInt(6);
  if (proxy != undefined) {
    proxy.sendMessageRequest(1, data, reply, option)
      .then((result: rpc.RequestResult) => {
        if (result.errCode === 0) {
          hilog.info(0x0000, 'testTag', 'sendMessageRequest got result');
          result.reply.readException();
          let num = result.reply.readInt();
          hilog.info(0x0000, 'testTag', 'reply num: ' + num);
        } else {
          hilog.error(0x0000, 'testTag', 'sendMessageRequest failed, errCode: ' + result.errCode);
        }
      }).catch((e: Error) => {
        hilog.error(0x0000, 'testTag', 'sendMessageRequest got exception: ' + JSON.stringify(e));
      }).finally (() => {
        hilog.info(0x0000, 'testTag', 'sendMessageRequest ends, reclaim parcel');
        data.reclaim();
        reply.reclaim();
      });
  }
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]writeParcelableArray9+

writeParcelableArray(parcelableArray: Parcelable\[\]): void

将可序列化对象数组写入MessageSequence实例。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| parcelableArray | [Parcelable](#parcelable9)\[\] | 是 | 要写入的可序列化对象数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match;

4.The element does not exist in the array.

 |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

class MyParcelable implements rpc.Parcelable {
  num: number = 0;
  str: string = '';
  constructor(num: number, str: string) {
    this.num = num;
    this.str = str;
  }
  marshalling(messageSequence: rpc.MessageSequence): boolean {
    messageSequence.writeInt(this.num);
    messageSequence.writeString(this.str);
    return true;
  }
  unmarshalling(messageSequence: rpc.MessageSequence): boolean {
    this.num = messageSequence.readInt();
    this.str = messageSequence.readString();
    return true;
  }
}

try {
  let parcelable = new MyParcelable(1, "aaa");
  let parcelable2 = new MyParcelable(2, "bbb");
  let parcelable3 = new MyParcelable(3, "ccc");
  let a = [parcelable, parcelable2, parcelable3];
  let data = rpc.MessageSequence.create();
  data.writeParcelableArray(a);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'rpc write parcelable array fail, errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'rpc write parcelable array fail, errorMessage ' + e.message);
}
```

#### \[h2\]readParcelableArray9+

readParcelableArray(parcelableArray: Parcelable\[\]): void

从MessageSequence实例中读取可序列化对象数组。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| parcelableArray | [Parcelable](#parcelable9)\[\] | 是 | 要读取的可序列化对象数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match;

4.The length of the array passed when reading is not equal to the length passed when writing to the array;

5.The element does not exist in the array.

 |
| 1900010 | Failed to read data from the message sequence. |
| 1900012 | Failed to call the JS callback function. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

class MyParcelable implements rpc.Parcelable {
  num: number = 0;
  str: string = '';
  constructor(num: number, str: string) {
    this.num = num;
    this.str = str;
  }
  marshalling(messageSequence: rpc.MessageSequence): boolean {
    messageSequence.writeInt(this.num);
    messageSequence.writeString(this.str);
    return true;
  }
  unmarshalling(messageSequence: rpc.MessageSequence): boolean {
    this.num = messageSequence.readInt();
    this.str = messageSequence.readString();
    return true;
  }
}

try {
  let parcelable = new MyParcelable(1, "aaa");
  let parcelable2 = new MyParcelable(2, "bbb");
  let parcelable3 = new MyParcelable(3, "ccc");
  let a = [parcelable, parcelable2, parcelable3];
  let data = rpc.MessageSequence.create();
  data.writeParcelableArray(a);
  let b = [new MyParcelable(0, ""), new MyParcelable(0, ""), new MyParcelable(0, "")];
  data.readParcelableArray(b);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'rpc write parcelable array fail, errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'rpc write parcelable array fail, errorMessage ' + e.message);
}
```

#### \[h2\]writeRemoteObjectArray9+

writeRemoteObjectArray(objectArray: IRemoteObject\[\]): void

将IRemoteObject对象数组写入MessageSequence。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| objectArray | [IRemoteObject](#iremoteobject)\[\] | 是 | 要写入MessageSequence的IRemoteObject对象数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match;

4.The element does not exist in the array;

5.The obtained remoteObject is null.

 |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    // 根据业务实际逻辑，进行相应处理
    return true;
  }
}

try {
  let a = [new TestRemoteObject("testObject1"), new TestRemoteObject("testObject2"), new TestRemoteObject("testObject3")];
  let data = rpc.MessageSequence.create();
  data.writeRemoteObjectArray(a);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]readRemoteObjectArray9+

readRemoteObjectArray(objects: IRemoteObject\[\]): void

从MessageSequence读取IRemoteObject对象数组，并将其写入到创建的空数组中。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| objects | [IRemoteObject](#iremoteobject)\[\] | 是 | 从MessageSequence读取的IRemoteObject对象数组。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match;

4.The length of the array passed when reading is not equal to the length passed when writing to the array.

 |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    // 根据业务实际逻辑，进行相应处理
    return true;
  }
}

try {
  let a = [new TestRemoteObject("testObject1"), new TestRemoteObject("testObject2"), new TestRemoteObject("testObject3")];
  let data = rpc.MessageSequence.create();
  data.writeRemoteObjectArray(a);
  let b: Array<rpc.IRemoteObject> = new Array(3);
  data.readRemoteObjectArray(b);
  hilog.info(0x0000, 'testTag', 'readRemoteObjectArray is ' + b);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]readRemoteObjectArray9+

readRemoteObjectArray(): IRemoteObject\[\]

从MessageSequence读取IRemoteObject对象数组。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [IRemoteObject](#iremoteobject)\[\] | 返回IRemoteObject对象数组；当写入的是空数组时，返回的是null。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    // 根据业务实际逻辑，进行相应处理
    return true;
  }
}

try {
  let a = [new TestRemoteObject("testObject1"), new TestRemoteObject("testObject2"), new TestRemoteObject("testObject3")];
  let data = rpc.MessageSequence.create();
  let b = data.readRemoteObjectArray();
  hilog.info(0x0000, 'testTag', 'readRemoteObjectArray is ' + b);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]closeFileDescriptor9+

static closeFileDescriptor(fd: number): void

静态方法，关闭给定的文件描述符。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 要关闭的文件描述符。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { fileIo } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let filePath = "path/to/file";
  let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
  rpc.MessageSequence.closeFileDescriptor(file.fd);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]dupFileDescriptor9+

static dupFileDescriptor(fd: number): number

静态方法，复制给定的文件描述符。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 表示已存在的文件描述符。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回新的文件描述符。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900013 | Failed to call dup. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { fileIo } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let filePath = "path/to/file";
  let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
  rpc.MessageSequence.dupFileDescriptor(file.fd);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]containFileDescriptors9+

containFileDescriptors(): boolean

检查此MessageSequence对象是否包含文件描述符。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：包含文件描述符，false：不包含文件描述符。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { fileIo } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let sequence = rpc.MessageSequence.create();
  let filePath = "path/to/file";
  let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
  let containFD = sequence.containFileDescriptors();
  hilog.info(0x0000, 'testTag', 'sequence after write fd containFd result is ' + containFD);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]writeFileDescriptor9+

writeFileDescriptor(fd: number): void

写入文件描述符到MessageSequence。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 文件描述符。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { fileIo } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let sequence = rpc.MessageSequence.create();
  let filePath = "path/to/file";
  let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
  sequence.writeFileDescriptor(file.fd);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]readFileDescriptor9+

readFileDescriptor(): number

从MessageSequence中读取文件描述符。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回文件描述符。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { fileIo } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let sequence = rpc.MessageSequence.create();
  let filePath = "path/to/file";
  let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
  sequence.writeFileDescriptor(file.fd);
  let readFD = sequence.readFileDescriptor();
  hilog.info(0x0000, 'testTag', 'readFileDescriptor is ' + readFD);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]writeAshmem9+

writeAshmem(ashmem: Ashmem): void

将指定的匿名共享对象写入此MessageSequence。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| ashmem | [Ashmem](#ashmem8) | 是 | 要写入MessageSequence的匿名共享对象。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter is not an instance of the Ashmem object.

 |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let sequence = rpc.MessageSequence.create();
  let ashmem = rpc.Ashmem.create("ashmem", 1024);
  // ashmem里写入数据
  let buffer = new ArrayBuffer(1024);
  let int32View = new Int32Array(buffer);
  for (let i = 0; i < int32View.length; i++) {
    int32View[i] = i * 2 + 1;
  }
  let size = buffer.byteLength;
  ashmem.mapReadWriteAshmem();
  ashmem.writeDataToAshmem(buffer, size, 0);
  // 将ashmem对象写入messageSequence对象中
  sequence.writeAshmem(ashmem);
  // 将传递的数据大小写入messageSequence对象中
  sequence.writeInt(size);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]readAshmem9+

readAshmem(): Ashmem

从MessageSequence读取匿名共享对象。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [Ashmem](#ashmem8) | 返回匿名共享对象。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let sequence = rpc.MessageSequence.create();
  let ashmem = rpc.Ashmem.create("ashmem", 1024);
  // ashmem里写入数据
  let buffer = new ArrayBuffer(1024);
  let int32View = new Int32Array(buffer);
  for (let i = 0; i < int32View.length; i++) {
    int32View[i] = i * 2 + 1;
  }
  let size = buffer.byteLength;
  ashmem.mapReadWriteAshmem();
  ashmem.writeDataToAshmem(buffer, size, 0);
  // 将传递的数据大小写入messageSequence对象中
  sequence.writeInt(size);
  // 将ashmem对象写入messageSequence对象中
  sequence.writeAshmem(ashmem);

  // 读取传递的数据大小
  let dataSize = sequence.readInt();
  // 从messageSequence对象中读取ashmem对象
  let ashmem1 = sequence.readAshmem();
  // 从ashmem对象中读取数据
  ashmem1.mapReadWriteAshmem();
  let readResult = ashmem1.readDataFromAshmem(dataSize, 0);
  let readInt32View = new Int32Array(readResult);
  hilog.info(0x0000, 'testTag', 'read from Ashmem result is ' + readInt32View);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]getRawDataCapacity9+

getRawDataCapacity(): number

获取MessageSequence可以容纳的最大原始数据量。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回MessageSequence可以容纳的最大原始数据量，即128MB。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let sequence = rpc.MessageSequence.create();
  let result = sequence.getRawDataCapacity();
  hilog.info(0x0000, 'testTag', 'sequence get RawDataCapacity result is ' + result);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]writeRawData(deprecated)

writeRawData(rawData: number\[\], size: number): void

将原始数据写入MessageSequence对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/gRlhAjoaR5KrxzFtYtphTg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=EC0DDFE1BF11A70878DCDC20098CBB6CA083C334C12BF44DC254915F836EC9E5)

从API version 9 开始支持，API version 11 开始废弃，建议使用[writeRawDataBuffer](#writerawdatabuffer11)替代。

该接口是一次性接口，不允许在一次parcel通信中多次调用该接口。

该接口在传输数据时，当数据量较大时（超过32KB），会使用共享内存传输数据，此时需注意selinux配置。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| rawData | number\[\] | 是 | 要写入的原始数据，大小不能超过128MB。 |
| size | number | 是 | 发送的原始数据大小，以字节为单位。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match;

4.The transferred size cannot be obtained;

5.The transferred size is less than or equal to 0;

6.The element does not exist in the array;

7.Failed to obtain typedArray information;

8.The array is not of type int32;

9.The length of typedarray is smaller than the size of the original data sent.

 |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let sequence = rpc.MessageSequence.create();
  let arr = [1, 2, 3, 4, 5];
  sequence.writeRawData(arr, arr.length);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]writeRawDataBuffer11+

writeRawDataBuffer(rawData: ArrayBuffer, size: number): void

将原始数据写入MessageSequence对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/dN4jHRFAQieFcGBgDzTcaw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=CD641E6938CBE65DAC78CF341F03F926DD7AE88BB8823481C518ACE878A9CC6C)

该接口是一次性接口，不允许在一次parcel通信中多次调用该接口。

该接口在传输数据时，当数据量较大时（超过32KB），会使用共享内存传输数据，此时需注意selinux配置。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| rawData | ArrayBuffer | 是 | 要写入的原始数据，大小不能超过128MB。 |
| size | number | 是 | 发送的原始数据大小，以字节为单位。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.Failed to obtain arrayBuffer information;

4.The transferred size cannot be obtained;

5.The transferred size is less than or equal to 0;

6.The transferred size is greater than the byte length of ArrayBuffer.

 |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let buffer = new ArrayBuffer(64 * 1024);
  let int32View = new Int32Array(buffer);
  for (let i = 0; i < int32View.length; i++) {
    int32View[i] = i * 2 + 1;
  }
  let size = buffer.byteLength;
  let sequence = rpc.MessageSequence.create();
  sequence.writeRawDataBuffer(buffer, size);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]readRawData(deprecated)

readRawData(size: number): number\[\]

从MessageSequence读取原始数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/6jWzHWv1RYigjWoJRgyTEQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=4C58CCAC80C12911A76F083A46AF209E11C982F6F5187CA5E65ED97599136186)

从API version 9 开始支持，API version 11 开始废弃，建议使用[readRawDataBuffer](#readrawdatabuffer11)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| size | number | 是 | 要读取的原始数据的大小。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number\[\] | 返回原始数据（以字节为单位）。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let sequence = rpc.MessageSequence.create();
  let arr = [1, 2, 3, 4, 5];
  sequence.writeRawData(arr, arr.length);
  let size = arr.length;
  let result = sequence.readRawData(size);
  hilog.info(0x0000, 'testTag', 'sequence read raw data result is ' + result);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]readRawDataBuffer11+

readRawDataBuffer(size: number): ArrayBuffer

从MessageSequence读取原始数据。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| size | number | 是 | 要读取的原始数据的大小。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| ArrayBuffer | 返回原始数据（以字节为单位）。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let buffer = new ArrayBuffer(64 * 1024);
  let int32View = new Int32Array(buffer);
  for (let i = 0; i < int32View.length; i++) {
    int32View[i] = i * 2 + 1;
  }
  let size = buffer.byteLength;
  let sequence = rpc.MessageSequence.create();
  sequence.writeRawDataBuffer(buffer, size);
  let result = sequence.readRawDataBuffer(size);
  let readInt32View = new Int32Array(result);
  hilog.info(0x0000, 'testTag', 'sequence read raw data result is ' + readInt32View);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]writeArrayBuffer12+

writeArrayBuffer(buf: ArrayBuffer, typeCode: TypeCode): void

将ArrayBuffer类型数据写入MessageSequence对象。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| buf | ArrayBuffer | 是 | 要写入的ArrayBuffer数据。 |
| typeCode | [TypeCode](#typecode12) | 是 | ArrayBuffer数据具体是以哪一种TypedArray来访问和操作(会根据业务传递的类型枚举值去决定底层的写入方式，需要业务正确传递枚举值。) |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match;

4.The obtained value of typeCode is incorrect;

5.Failed to obtain arrayBuffer information.

 |
| 1900009 | Failed to write data to the message sequence. |

**示例：**

```ts
// TypeCode 类型枚举较多，示例代码以Int16Array为例
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  let buffer = new ArrayBuffer(10);
  let int16View = new Int16Array(buffer);
  for (let i = 0; i < int16View.length; i++) {
    int16View[i] = i * 2 + 1;
  }
  data.writeArrayBuffer(buffer, rpc.TypeCode.INT16_ARRAY);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]readArrayBuffer12+

readArrayBuffer(typeCode: TypeCode): ArrayBuffer

从MessageSequence读取ArrayBuffer类型数据。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| typeCode | [TypeCode](#typecode12) | 是 | ArrayBuffer数据具体是以哪一种TypedArray来访问和操作(会根据业务传递的类型枚举值去决定底层的读取方式，需要业务正确传递枚举值，读写枚举值不匹配会导致数据异常。) |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| ArrayBuffer | 返回ArrayBuffer类型数据（以字节为单位）。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.The obtained value of typeCode is incorrect;

 |
| 1900010 | Failed to read data from the message sequence. |

**示例：**

```ts
// TypeCode 类型枚举较多，示例代码以Int16Array为例
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  let buffer = new ArrayBuffer(10);
  let int16View = new Int16Array(buffer);
  for (let i = 0; i < int16View.length; i++) {
    int16View[i] = i * 2 + 1;
  }
  data.writeArrayBuffer(buffer, rpc.TypeCode.INT16_ARRAY);
  let result = data.readArrayBuffer(rpc.TypeCode.INT16_ARRAY);
  let readInt16View = new Int16Array(result);
  hilog.info(0x0000, 'testTag', 'read ArrayBuffer result is ' + readInt16View);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### MessageParcel(deprecated)

在RPC过程中，发送方可以使用MessageParcel提供的写方法，将待发送的数据以特定格式写入该对象。接收方可以使用MessageParcel提供的读方法从该对象中读取特定格式的数据。数据格式包括：基础类型及数组、IPC对象、接口描述符和自定义序列化对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/5g1ug4URTJis9JBoHtdkwQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=72E99C659B8F8AB92A227B44C37A8E7047D222CE2C924151F568BA8F2E142B3F)

从API version 7 开始支持，API version 9 开始废弃，建议使用[MessageSequence](#messagesequence9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

#### \[h2\]create(deprecated)

static create(): MessageParcel

静态方法，创建MessageParcel对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/L2yRzMd4Rh6DDGW8R3Rw3Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=AF1366BB7703A3722FC992772672C99D062F24527C8273A7F8244D9A47AF05CF)

从API version 7 开始支持，API version 9 开始废弃，建议使用[create](#create9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [MessageParcel](#messageparceldeprecated) | 返回创建的MessageParcel对象。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  hilog.info(0x0000, 'testTag', 'data is ' + data);

  // 当MessageParcel对象不再使用，由业务主动调用reclaim方法去释放资源。
  data.reclaim();
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]reclaim(deprecated)

reclaim(): void

释放不再使用的MessageParcel对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/ME3PIwUjS3eJx35vwZrcbQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=A7E1A2B9B1C58B6FF20E64D784449B88D7C63A1A353313B785552EFF774E12F1)

从API version 7 开始支持，API version 9 开始废弃，建议使用[reclaim](#reclaim9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let reply = rpc.MessageParcel.create();
  reply.reclaim();
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]writeRemoteObject(deprecated)

writeRemoteObject(object: IRemoteObject): boolean

序列化远程对象并将其写入MessageParcel对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/gD4w8VkMSFWPvvGl3RSHpg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=4A0BC3AD181EFA209ED5F42F7C0BB3371224ACDA677B97475164B5F3A73DA292)

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeRemoteObject](#writeremoteobject9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| object | [IRemoteObject](#iremoteobject) | 是 | 要序列化并写入MessageParcel的远程对象。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：操作成功，false：操作失败。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel, option: rpc.MessageOption): boolean {
    // 根据业务实际逻辑，进行相应处理
    return true;
  }
}

try {
  let data = rpc.MessageParcel.create();
  let testRemoteObject = new TestRemoteObject("testObject");
  data.writeRemoteObject(testRemoteObject);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]readRemoteObject(deprecated)

readRemoteObject(): IRemoteObject

从MessageParcel读取远程对象。此方法用于反序列化MessageParcel对象以生成IRemoteObject。远程对象按写入MessageParcel的顺序读取。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/GQkGSwcORkCIXBkMzzmC-Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=4CE8FBFF5DDCA97F641B569007D375AA0EEBA36BB12573CA24AC1A38B0C1FCDC)

从API version 7 开始支持，API version 9 开始废弃，建议使用[readRemoteObject](#readremoteobject9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [IRemoteObject](#iremoteobject) | 读取到的远程对象。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel,
    option: rpc.MessageOption): boolean {
    // 根据业务实际逻辑，进行相应处理
    return true;
  }
}

try {
  let data = rpc.MessageParcel.create();
  let testRemoteObject = new TestRemoteObject("testObject");
  data.writeRemoteObject(testRemoteObject);
  let proxy = data.readRemoteObject();
  hilog.info(0x0000, 'testTag', 'readRemoteObject is ' + proxy);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]writeInterfaceToken(deprecated)

writeInterfaceToken(token: string): boolean

将接口描述符写入MessageParcel对象，远端对象可使用该信息校验本次通信。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/CqP5tL8iQtKhDu13IEb7YQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=48F227A83936F7AAFF93CE4B8DB7E5730F9306C80C64D7F915FA57368EB98D61)

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeInterfaceToken](#writeinterfacetoken9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| token | string | 是 | 字符串类型描述符，其长度应小于40960字节。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：操作成功，false：操作失败。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeInterfaceToken("aaa");
  hilog.info(0x0000, 'testTag', 'RpcServer: writeInterfaceToken is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]readInterfaceToken(deprecated)

readInterfaceToken(): string

从MessageParcel中读取接口描述符，接口描述符按写入MessageParcel的顺序读取，本地对象可使用该信息检验本次通信。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/O4Uy6emqTKOXbnaLpKJV9w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=1EAE2C5568FD00162ED26023D78C3FE28C627D34850FD2F620C0230932297433)

从API version 7 开始支持，API version 9 开始废弃，建议使用[readInterfaceToken](#readinterfacetoken9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 返回读取到的接口描述符。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeInterfaceToken("aaa");
  let interfaceToken = data.readInterfaceToken();
  hilog.info(0x0000, 'testTag', 'RpcServer: interfaceToken is ' + interfaceToken);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]getSize(deprecated)

getSize(): number

获取当前MessageParcel的数据大小。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/1W0_nFU3RqmlTVs_nCtqtg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=F5F7999946F4BEF556D49D3850A8999B710B896589296387EEAA9D9E0C222E97)

从API version 7 开始支持，API version 9 开始废弃，建议使用[getSize](#getsize9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 获取的MessageParcel的数据大小。以字节为单位。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  data.writeInt(1);
  let size = data.getSize();
  hilog.info(0x0000, 'testTag', 'size is ' + size);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]getCapacity(deprecated)

getCapacity(): number

获取当前MessageParcel的容量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/2ZmjIZY5Tzyfdikb2qq2ZQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=8BD28E78A7AAE39C60BA5539655211A615DBA1F1CACA1FB0AB081698BB535A3E)

从API version 7 开始支持，API version 9 开始废弃，建议使用[getCapacity](#getcapacity9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 获取的MessageParcel的容量大小。以字节为单位。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.getCapacity();
  hilog.info(0x0000, 'testTag', 'capacity is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]setSize(deprecated)

setSize(size: number): boolean

设置MessageParcel实例中包含的数据大小。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/dVw0YIqJTjuIC5DAfhDB_g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=C507329D8A833D43C62689893289C50E22832EF9BB27C3B7809797AA7D2485E8)

从API version 7 开始支持，API version 9 开始废弃，建议使用[setSize](#setsize9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| size | number | 是 | MessageParcel实例的数据大小。以字节为单位。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：设置成功，false：设置失败。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let setSize = data.setSize(16);
  hilog.info(0x0000, 'testTag', 'setSize is ' + setSize);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]setCapacity(deprecated)

setCapacity(size: number): boolean

设置MessageParcel实例的存储容量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/6dlzYmxQQXODQ9fkvgFDqw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=23280CBF92B68217A4DE37D59C6F9FF64570A67847DDE6B6644BD3C8CF6A2210)

从API version 7 开始支持，API version 9 开始废弃，建议使用[setCapacity](#setcapacity9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| size | number | 是 | MessageParcel实例的存储容量。以字节为单位。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：设置成功，false：设置失败。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.setCapacity(100);
  hilog.info(0x0000, 'testTag', 'setCapacity is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]getWritableBytes(deprecated)

getWritableBytes(): number

获取MessageParcel的可写字节空间。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/VrBEwda_SPWndf9l31A7rA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=78AB20599D9BB02DE77F7071192C0D0C24FD6056B6BDD5AEFE402CB8C24FA4B1)

从API version 7 开始支持，API version 9 开始废弃，建议使用[getWritableBytes](#getwritablebytes9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 获取到的MessageParcel的可写字节空间。以字节为单位。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  data.writeInt(1);
  let getWritableBytes = data.getWritableBytes();
  hilog.info(0x0000, 'testTag', 'RpcServer: getWritableBytes is ' + getWritableBytes);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]getReadableBytes(deprecated)

getReadableBytes(): number

获取MessageParcel的可读字节空间。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/Ddnky6bdQi-DGZQufEGVTQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=7B5B63E6397382C6639FDED49C103353379DB3EB9EC0B7AC07FB2B6682C9499C)

从API version 7 开始支持，API version 9 开始废弃，建议使用[getReadableBytes](#getreadablebytes9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 获取到的MessageParcel的可读字节空间。以字节为单位。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  data.writeInt(1);
  let result = data.getReadableBytes();
  hilog.info(0x0000, 'testTag', 'RpcServer: getReadableBytes is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]getReadPosition(deprecated)

getReadPosition(): number

获取MessageParcel的读位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/ssopQp4ITcO4JGo6aLz4rw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=A3DEC8E3E83DBAAFCCD263AF9D6E7A49A94C63898E1F7404168A8048183C2533)

从API version 7 开始支持，API version 9 开始废弃，建议使用[getReadPosition](#getreadposition9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回MessageParcel实例中的当前读取位置。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let readPos = data.getReadPosition();
  hilog.info(0x0000, 'testTag', 'readPos is ' + readPos);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]getWritePosition(deprecated)

getWritePosition(): number

获取MessageParcel的写位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/k3eA7GmdRM-ekbMmMtlDcw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=0A3C30D03DA8DC53661BE313E53B1B363FDE1FCFBCC4EDF334E49DE3B5CECFBB)

从API version 7 开始支持，API version 9 开始废弃，建议使用[getWritePosition](#getwriteposition9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回MessageParcel实例中的当前写入位置。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  data.writeInt(10);
  let bwPos = data.getWritePosition();
  hilog.info(0x0000, 'testTag', 'bwPos is ' + bwPos);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]rewindRead(deprecated)

rewindRead(pos: number): boolean

重新偏移读取位置到指定的位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/WWX0Vm6DQBGQ7JINzWXibg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=1F2B225869E3DDB037D5970FC34AE9DF1A1800A28ED6BACE5FDA6D8ED7BAB3D1)

从API version 7 开始支持，API version 9 开始废弃，建议使用[rewindRead](#rewindread9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| pos | number | 是 | 开始读取数据的目标位置。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：读取位置发生更改，false：读取位置未发生更改。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  data.writeInt(12);
  data.writeString("parcel");
  let number = data.readInt();
  hilog.info(0x0000, 'testTag', 'number is ' + number);
  data.rewindRead(0);
  let number2 = data.readInt();
  hilog.info(0x0000, 'testTag', 'rewindRead is ' + number2);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]rewindWrite(deprecated)

rewindWrite(pos: number): boolean

重新偏移写位置到指定的位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/R4W-O7BzR-iUWyfQw4Up_w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=B6101D6C59094EA8274504CA0ACB5F40FE69960B546A2569D11ED57D034B5782)

从API version 7 开始支持，API version 9 开始废弃，建议使用[rewindWrite](#rewindwrite9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| pos | number | 是 | 开始写入数据的目标位置。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：写入位置发生更改，false：写入位置未发生更改。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  data.writeInt(4);
  data.rewindWrite(0);
  data.writeInt(5);
  let number = data.readInt();
  hilog.info(0x0000, 'testTag', 'rewindWrite is ' + number);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]writeByte(deprecated)

writeByte(val: number): boolean

将字节值写入MessageParcel实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/zL2p6SQbQdWSWfRYYOwxoA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=0478F513773A56A60F1E4084D7C1BF0535D91A194B91484272BAB7CEF47CDD61)

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeByte](#writebyte9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| val | number | 是 | 要写入的字节值。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeByte(2);
  hilog.info(0x0000, 'testTag', 'writeByte is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]readByte(deprecated)

readByte(): number

从MessageParcel实例中读取字节值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/IrKppsBTSn6g29eHp1NUuQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=F18AC962EC2F5B5615C78265C9797B928DE35960AC0C765DBFEF13398297F9E1)

从API version 7 开始支持，API version 9 开始废弃，建议使用[readByte](#readbyte9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回字节值。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeByte(2);
  hilog.info(0x0000, 'testTag', 'writeByte is ' + result);
  let ret = data.readByte();
  hilog.info(0x0000, 'testTag', 'readByte is ' + ret);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]writeShort(deprecated)

writeShort(val: number): boolean

将短整数值写入MessageParcel实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/qo7XNcVqRyaUExU733GdRw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=C2F9A5B4E7E3CEBE5885FE17AF887318EA251691E682C8B2D2736572A29413F9)

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeShort](#writeshort9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| val | number | 是 | 要写入的短整数值。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeShort(8);
  hilog.info(0x0000, 'testTag', 'writeShort is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]readShort(deprecated)

readShort(): number

从MessageParcel实例中读取短整数值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/BvKtiRZzRLK1X0L1bQKKYQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=C4FDE4EF9060EC9F1B91B6C4FBC3C22DE830412BC01458B0CB107B717DF887EE)

从API version 7 开始支持，API version 9 开始废弃，建议使用[readShort](#readshort9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回短整数值。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeShort(8);
  hilog.info(0x0000, 'testTag', 'writeShort is ' + result);
  let ret = data.readShort();
  hilog.info(0x0000, 'testTag', 'readShort is ' + ret);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]writeInt(deprecated)

writeInt(val: number): boolean

将整数值写入MessageParcel实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/k61vid6JRQCtOmZKjhAIRQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=E30C6BD76F631454112CA6ED1D8963BEA6D3754CE26F3D00687B5707578174D6)

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeInt](#writeint9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| val | number | 是 | 要写入的整数值。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeInt(10);
  hilog.info(0x0000, 'testTag', 'writeInt is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]readInt(deprecated)

readInt(): number

从MessageParcel实例中读取整数值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/L4I9NvUjRtysXOyMinpK-g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=6501644F5B6B7CB898410C5F52855D03943E9BBC0FA3E37A03A3AFC20A0D9B6C)

从API version 7 开始支持，API version 9 开始废弃，建议使用[readInt](#readint9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回整数值。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeInt(10);
  hilog.info(0x0000, 'testTag', 'writeInt is ' + result);
  let ret = data.readInt();
  hilog.info(0x0000, 'testTag', 'readInt is ' + ret);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]writeLong(deprecated)

writeLong(val: number): boolean

将长整数值写入MessageParcel实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/XpKq0zT2SEG2_95xwZTKuQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=153164443F6F7D3D67BCF903AF175D544ED6830E7E0D2ACFDCD12A10B6DED03B)

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeLong](#writelong9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| val | number | 是 | 要写入的长整数值 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeLong(10000);
  hilog.info(0x0000, 'testTag', 'writeLong is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]readLong(deprecated)

readLong(): number

从MessageParcel实例中读取长整数值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/QveQWCMMS6uh_2B60y0YQg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=FC0F17E081CCCA0B0305B5F7D91594D8433DB06FF71FF712C13DFCE6B65B4736)

从API version 7 开始支持，API version 9 开始废弃，建议使用[readLong](#readlong9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回长整数值。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeLong(10000);
  hilog.info(0x0000, 'testTag', 'writeLong is ' + result);
  let ret = data.readLong();
  hilog.info(0x0000, 'testTag', 'readLong is ' + ret);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]writeFloat(deprecated)

writeFloat(val: number): boolean

将双精度浮点值写入MessageParcel实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/Ddw0glcfR9aZ9YM3pWwnfw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=204688AD25D55CAEFAABDA63BEC0795A3D5CA12AF03B48F5F43C9EDEF9610532)

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeFloat](#writefloat9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| val | number | 是 | 要写入的双精度浮点值。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeFloat(1.2);
  hilog.info(0x0000, 'testTag', 'writeFloat is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]readFloat(deprecated)

readFloat(): number

从MessageParcel实例中读取双精度浮点值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/ey3ufAUvTDuwUdBIfmwxxw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=96109BB38006760B0CA471B079D3B74985E5A30B08DB180A4795325AF5C5B749)

从API version 7 开始支持，API version 9 开始废弃，建议使用[readFloat](#readfloat9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回双精度浮点值。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeFloat(1.2);
  hilog.info(0x0000, 'testTag', 'writeFloat is ' + result);
  let ret = data.readFloat();
  hilog.info(0x0000, 'testTag', 'readFloat is ' + ret);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]writeDouble(deprecated)

writeDouble(val: number): boolean

将双精度浮点值写入MessageParcel实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/N96dVh7BSDyQVzSZ5AQGlA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=DB773E91E7D4C755CF0CB92F6EC408DF8F22029B8811519FE060CC8F6C26FFBB)

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeDouble](#writedouble9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| val | number | 是 | 要写入的双精度浮点值。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeDouble(10.2);
  hilog.info(0x0000, 'testTag', 'writeDouble is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]readDouble(deprecated)

readDouble(): number

从MessageParcel实例中读取双精度浮点值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/DD6QW6RURjK2WOtbKnRvYQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=33B4F12ACE94AA3A09659BA96A0A1984AB73BEE54350B2A095D957B01CCE387D)

从API version 7 开始支持，API version 9 开始废弃，建议使用[readDouble](#readdouble9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回双精度浮点值。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeDouble(10.2);
  hilog.info(0x0000, 'testTag', 'writeDouble is ' + result);
  let ret = data.readDouble();
  hilog.info(0x0000, 'testTag', 'readDouble is ' + ret);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]writeBoolean(deprecated)

writeBoolean(val: boolean): boolean

将布尔值写入MessageParcel实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/HoTirDNER0ikUtYRmf-5Uw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=D9AECC22BB6FF867A8A904A49A2BE0C1918A2483E5EEB9A0DF76864D866BC15B)

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeBoolean](#writeboolean9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| val | boolean | 是 | 要写入的布尔值。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeBoolean(false);
  hilog.info(0x0000, 'testTag', 'writeBoolean is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]readBoolean(deprecated)

readBoolean(): boolean

从MessageParcel实例中读取布尔值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/I87_USbOS9-6VOdRFJ6O-A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=01320D135EE37D651851F62DB4059821512F7D98D55B16FEA0E190903A31FA9E)

从API version 7 开始支持，API version 9 开始废弃，建议使用[readBoolean](#readboolean9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 返回读取到的布尔值。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeBoolean(false);
  hilog.info(0x0000, 'testTag', 'writeBoolean is ' + result);
  let ret = data.readBoolean();
  hilog.info(0x0000, 'testTag', 'readBoolean is ' + ret);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]writeChar(deprecated)

writeChar(val: number): boolean

将单个字符值写入MessageParcel实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/Hq3i3KzCTMqzuWsaslRv-w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=784A0ADC371AF9FB53477C72DA74271432867783283703F33C8FB0228DEF3EAC)

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeChar](#writechar9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| val | number | 是 | 要写入的单个字符值。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeChar(97);
  hilog.info(0x0000, 'testTag', 'writeChar is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]readChar(deprecated)

readChar(): number

从MessageParcel实例中读取单个字符值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/XK0ux8hzQBG_WJ_62m34Ow/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=BE4609C8EA0479521922F54864769719F272A3B04CFCD7FDB3759468465D8D33)

从API version 7 开始支持，API version 9 开始废弃，建议使用[readChar](#readchar9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回单个字符值。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeChar(97);
  hilog.info(0x0000, 'testTag', 'writeChar is ' + result);
  let ret = data.readChar();
  hilog.info(0x0000, 'testTag', 'readChar is ' + ret);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]writeString(deprecated)

writeString(val: string): boolean

将字符串值写入MessageParcel实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/IdZ6KnWKRoe1vaP2VfbDuQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=C5E1A15AD3D18B775C6912595B4104C8DADC1C1DF161B8E3D640B125CEA0586B)

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeString](#writestring9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| val | string | 是 | 要写入的字符串值，其长度应小于40960字节。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeString('abc');
  hilog.info(0x0000, 'testTag', 'writeString is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]readString(deprecated)

readString(): string

从MessageParcel实例中读取字符串值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/xmO3wj1TTn2bC-rltm7sog/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=17C44F606EC697ECE00FB633F93DE22D373687E5B1F07DE6590891FF1A823F98)

从API version 7 开始支持，API version 9 开始废弃，建议使用[readString](#readstring9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 返回字符串值。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeString('abc');
  hilog.info(0x0000, 'testTag', 'writeString is ' + result);
  let ret = data.readString();
  hilog.info(0x0000, 'testTag', 'readString is ' + ret);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]writeSequenceable(deprecated)

writeSequenceable(val: Sequenceable): boolean

将自定义序列化对象写入MessageParcel实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/zXRZC2lUTSSQ5Fp37oLOeQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=08C1304FC7531FF6792F95BBCCB2C11CA6C6FE5F5BA580346EFCD4EE9F0DEC60)

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeParcelable](#writeparcelable9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| val | [Sequenceable](#sequenceabledeprecated) | 是 | 要写入的可序列对象。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MySequenceable implements rpc.Sequenceable {
  num: number = 0;
  str: string = '';
  constructor(num: number, str: string) {
    this.num = num;
    this.str = str;
  }
  marshalling(messageParcel: rpc.MessageParcel): boolean {
    messageParcel.writeInt(this.num);
    messageParcel.writeString(this.str);
    return true;
  }
  unmarshalling(messageParcel: rpc.MessageParcel): boolean {
    this.num = messageParcel.readInt();
    this.str = messageParcel.readString();
    return true;
  }
}

try {
  let sequenceable = new MySequenceable(1, "aaa");
  let data = rpc.MessageParcel.create();
  let result = data.writeSequenceable(sequenceable);
  hilog.info(0x0000, 'testTag', 'writeSequenceable is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]readSequenceable(deprecated)

readSequenceable(dataIn: Sequenceable): boolean

从MessageParcel实例中读取成员变量到指定的对象（dataIn）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/DXTXzeGaStW5MwFRU-fT_w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=67445E35F03F062A7BA7613889B83CF29F70F3E1C4039953C493BE169B2657EB)

从API version 7 开始支持，API version 9 开始废弃，建议使用[readParcelable](#readparcelable9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| dataIn | [Sequenceable](#sequenceabledeprecated) | 是 | 需要从MessageParcel读取成员变量的对象。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：反序列化成功，false：反序列化失败。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MySequenceable implements rpc.Sequenceable {
  num: number = 0;
  str: string = '';
  constructor(num: number, str: string) {
    this.num = num;
    this.str = str;
  }
  marshalling(messageParcel: rpc.MessageParcel): boolean {
    messageParcel.writeInt(this.num);
    messageParcel.writeString(this.str);
    return true;
  }
  unmarshalling(messageParcel: rpc.MessageParcel): boolean {
    this.num = messageParcel.readInt();
    this.str = messageParcel.readString();
    return true;
  }
}

try {
  let sequenceable = new MySequenceable(1, "aaa");
  let data = rpc.MessageParcel.create();
  let result = data.writeSequenceable(sequenceable);
  hilog.info(0x0000, 'testTag', 'writeSequenceable is ' + result);
  let ret = new MySequenceable(0, "");
  let result2 = data.readSequenceable(ret);
  hilog.info(0x0000, 'testTag', 'readSequenceable is ' + result2);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]writeByteArray(deprecated)

writeByteArray(byteArray: number\[\]): boolean

将字节数组写入MessageParcel实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/G9LmfNl3Qcm0uWvJ-TKtxw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=DA1C84C3374305975A67D95AE010F7F0DE01FD627C0A9252C91FCC2CBD9637D9)

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeByteArray](#writebytearray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| byteArray | number\[\] | 是 | 要写入的字节数组。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let ByteArrayVar = [1, 2, 3, 4, 5];
  let result = data.writeByteArray(ByteArrayVar);
  hilog.info(0x0000, 'testTag', 'writeByteArray is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]readByteArray(deprecated)

readByteArray(dataIn: number\[\]): void

从MessageParcel实例中读取字节数组，并将其写入到创建的空数组中。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/xjDCFy-FRy6c55cvwCjT3w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=54A4E5463D7A9CCD07328578EF1F7B595FB483A2A97585DFE4AD2562C105A505)

从API version 7 开始支持，API version 9 开始废弃，建议使用[readByteArray](#readbytearray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| dataIn | number\[\] | 是 | 要读取的字节数组。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let ByteArrayVar = [1, 2, 3, 4, 5];
  let result = data.writeByteArray(ByteArrayVar);
  let array: Array<number> = new Array(5);
  data.readByteArray(array);
  hilog.info(0x0000, 'testTag', 'readByteArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]readByteArray(deprecated)

readByteArray(): number\[\]

从MessageParcel实例中读取字节数组。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/YWl18-azQMG4acPycfZ3jw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=7EE1222414BF2EC553EF47127D0C11AB8591DA1F2ED1465AC62C82CAD95C6B59)

从API version 7 开始支持，API version 9 开始废弃，建议使用[readByteArray](#readbytearray9-1)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number\[\] | 返回字节数组。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let ByteArrayVar = [1, 2, 3, 4, 5];
  let result = data.writeByteArray(ByteArrayVar);
  hilog.info(0x0000, 'testTag', 'writeByteArray is ' + result);
  let array = data.readByteArray();
  hilog.info(0x0000, 'testTag', 'readByteArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]writeShortArray(deprecated)

writeShortArray(shortArray: number\[\]): boolean

将短整数数组写入MessageParcel实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/rYOLoRXgQeqD7SoGnqmqWw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=4AE9939919CFE8EBF660BFBCEB3587CBEE8C35CA82162F60AEEC4A2C5C17075F)

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeShortArray](#writeshortarray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| shortArray | number\[\] | 是 | 要写入的短整数数组。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeShortArray([11, 12, 13]);
  hilog.info(0x0000, 'testTag', 'writeShortArray is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]readShortArray(deprecated)

readShortArray(dataIn: number\[\]): void

从MessageParcel实例中读取短整数数组，并将其写入到创建的空数组中。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/qWOi7eUIRLefHH7Y4J8ADQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=C5B7D111283CEB4868284D8F9B3253218FB8DB92D189AB0E6EE08C20E20D26C0)

从API version 7 开始支持，API version 9 开始废弃，建议使用[readShortArray](#readshortarray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| dataIn | number\[\] | 是 | 要读取的短整数数组。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeShortArray([11, 12, 13]);
  hilog.info(0x0000, 'testTag', 'writeShortArray is ' + result);
  let array: Array<number> = new Array(3);
  data.readShortArray(array);
  hilog.info(0x0000, 'testTag', 'readShortArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]readShortArray(deprecated)

readShortArray(): number\[\]

从MessageParcel实例中读取短整数数组。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/hXAoZorMSWO5-QQqT7GBLQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=0E4C3477E23EC5561ECC43770B98E9671C61054167B565B91AB4F03BAD6B09B4)

从API version 7 开始支持，API version 9 开始废弃，建议使用[readShortArray](#readshortarray9-1)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number\[\] | 返回短整数数组。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeShortArray([11, 12, 13]);
  hilog.info(0x0000, 'testTag', 'writeShortArray is ' + result);
  let array = data.readShortArray();
  hilog.info(0x0000, 'testTag', 'readShortArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]writeIntArray(deprecated)

writeIntArray(intArray: number\[\]): boolean

将整数数组写入MessageParcel实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/GatwS1MNQQaXk6hH1YVDRw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=C2BE3E2D93426385A9844051E357A7A0FF208CAA9C9C282DDFF3745D9F5E4CC8)

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeIntArray](#writeintarray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| intArray | number\[\] | 是 | 要写入的整数数组。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeIntArray([100, 111, 112]);
  hilog.info(0x0000, 'testTag', 'writeIntArray is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]readIntArray(deprecated)

readIntArray(dataIn: number\[\]): void

从MessageParcel实例中读取整数数组，并将其写入到创建的空数组中。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/LTgLvJpJQp2eAj9f63Gi4g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=BB9AA0272D34D302625957C3F938DE4F89712CD3498C3E176A67196B06756345)

从API version 7 开始支持，API version 9 开始废弃，建议使用[readIntArray](#readintarray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| dataIn | number\[\] | 是 | 要读取的整数数组。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeIntArray([100, 111, 112]);
  hilog.info(0x0000, 'testTag', 'writeIntArray is ' + result);
  let array: Array<number> = new Array(3);
  data.readIntArray(array);
  hilog.info(0x0000, 'testTag', 'readIntArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]readIntArray(deprecated)

readIntArray(): number\[\]

从MessageParcel实例中读取整数数组。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/QyKyiQcCSF-fi6zaEQcM7Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=28AFAE8CC9B3B42FF6015E3654D243901E2C09DADE6FFAF49118BFFBCA2E6A30)

从API version 7 开始支持，API version 9 开始废弃，建议使用[readIntArray](#readintarray9-1)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number\[\] | 返回整数数组。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeIntArray([100, 111, 112]);
  hilog.info(0x0000, 'testTag', 'writeIntArray is ' + result);
  let array = data.readIntArray();
  hilog.info(0x0000, 'testTag', 'readIntArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]writeLongArray(deprecated)

writeLongArray(longArray: number\[\]): boolean

将长整数数组写入MessageParcel实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/plNxQigiQb6hm8sAcYLobg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=ADCB8A13680FA316A0BF1F062EE8814540FC46A84219A1CFE1E05789629D7B05)

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeLongArray](#writelongarray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| longArray | number\[\] | 是 | 要写入的长整数数组。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeLongArray([1111, 1112, 1113]);
  hilog.info(0x0000, 'testTag', 'writeLongArray is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]readLongArray(deprecated)

readLongArray(dataIn: number\[\]): void

从MessageParcel实例中读取长整数数组，并将其写入到创建的空数组中。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/DpA-hbeWR3GIahWE-0jFDA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=9237277A88505D414860744502ACD951A0999E873353D38953B8B598C0612EB3)

从API version 7 开始支持，API version 9 开始废弃，建议使用[readLongArray](#readlongarray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| dataIn | number\[\] | 是 | 要读取的长整数数组。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeLongArray([1111, 1112, 1113]);
  hilog.info(0x0000, 'testTag', 'writeLongArray is ' + result);
  let array: Array<number> = new Array(3);
  data.readLongArray(array);
  hilog.info(0x0000, 'testTag', 'readLongArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]readLongArray(deprecated)

readLongArray(): number\[\]

从MessageParcel实例中读取长整数数组。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/73gJUkttRiOLQFwJKiOOYA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=B9C1AB1727E8B7F6B313C6E6A1B0D5AA80ADE966E4681F8FCF4A9F47619DA32C)

从API version 7 开始支持，API version 9 开始废弃，建议使用[readLongArray](#readlongarray9-1)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number\[\] | 返回长整数数组。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeLongArray([1111, 1112, 1113]);
  hilog.info(0x0000, 'testTag', 'writeLongArray is ' + result);
  let array = data.readLongArray();
  hilog.info(0x0000, 'testTag', 'readLongArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]writeFloatArray(deprecated)

writeFloatArray(floatArray: number\[\]): boolean

将双精度浮点数组写入MessageParcel实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/fM7YUjHuTXC7sxNBPIxnUQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=5851502165473330434E54D639AF9A5BC045CCAAAF120DD59635E5BEF367A8BD)

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeFloatArray](#writefloatarray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| floatArray | number\[\] | 是 | 要写入的双精度浮点数组。由于系统内部对float类型的数据是按照double处理的，使用时对于数组所占的总字节数应按照double类型来计算。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeFloatArray([1.2, 1.3, 1.4]);
  hilog.info(0x0000, 'testTag', 'writeFloatArray is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]readFloatArray(deprecated)

readFloatArray(dataIn: number\[\]): void

从MessageParcel实例中读取双精度浮点数组，并将其写入到创建的空数组中。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/eag7-LWhTCacHvMD5ViDdA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=EAD041D7247CBE5E743D11BCBA4ECBCD6DC107DBB3AA8FEADFDCD47D5635451A)

从API version 7 开始支持，API version 9 开始废弃，建议使用[readFloatArray](#readfloatarray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| dataIn | number\[\] | 是 | 要读取的双精度浮点数组。由于系统内部对float类型的数据是按照double处理的，使用时对于数组所占的总字节数应按照double类型来计算。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeFloatArray([1.2, 1.3, 1.4]);
  hilog.info(0x0000, 'testTag', 'writeFloatArray is ' + result);
  let array: Array<number> = new Array(3);
  data.readFloatArray(array);
  hilog.info(0x0000, 'testTag', 'readFloatArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]readFloatArray(deprecated)

readFloatArray(): number\[\]

从MessageParcel实例中读取双精度浮点数组。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/sZANbPEAR_e8bGnDCWLSkg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=DA1F91B24E126BF6156C35ADB15F5418EB99C925B27848EE39268EB89A991823)

从API version 7 开始支持，API version 9 开始废弃，建议使用[readFloatArray](#readfloatarray9-1)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number\[\] | 返回双精度浮点数组。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeFloatArray([1.2, 1.3, 1.4]);
  hilog.info(0x0000, 'testTag', 'writeFloatArray is ' + result);
  let array = data.readFloatArray();
  hilog.info(0x0000, 'testTag', 'readFloatArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]writeDoubleArray(deprecated)

writeDoubleArray(doubleArray: number\[\]): boolean

将双精度浮点数组写入MessageParcel实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/T7OmT_JXRvWdh1FV7GAq2g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=46479952C79A18B56AB0904E8643247DEC76B71FF640E6600C400A9A9E0B075E)

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeDoubleArray](#writedoublearray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| doubleArray | number\[\] | 是 | 要写入的双精度浮点数组。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeDoubleArray([11.1, 12.2, 13.3]);
  hilog.info(0x0000, 'testTag', 'writeDoubleArray is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]readDoubleArray(deprecated)

readDoubleArray(dataIn: number\[\]): void

从MessageParcel实例中读取双精度浮点数组，并将其写入到创建的空数组中。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/WDhTLL8YSSOlMJQexoYIew/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=A830DE1A03A1F84D249CC119CC1CA2027379B555E126E299758E0161DB8208AE)

从API version 7 开始支持，API version 9 开始废弃，建议使用[readDoubleArray](#readdoublearray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| dataIn | number\[\] | 是 | 要读取的双精度浮点数组。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeDoubleArray([11.1, 12.2, 13.3]);
  hilog.info(0x0000, 'testTag', 'writeDoubleArray is ' + result);
  let array: Array<number> = new Array(3);
  data.readDoubleArray(array);
  hilog.info(0x0000, 'testTag', 'readDoubleArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]readDoubleArray(deprecated)

readDoubleArray(): number\[\]

从MessageParcel实例中读取双精度浮点数组。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/L6mw0sd3TJSzdjb5CrW4iQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=1AC2AF420D23DF6245231532BCD1F3D58777642C1538F81CFF8FCF33F67EF821)

从API version 7 开始支持，API version 9 开始废弃，建议使用[readDoubleArray](#readdoublearray9-1)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number\[\] | 返回双精度浮点数组。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeDoubleArray([11.1, 12.2, 13.3]);
  hilog.info(0x0000, 'testTag', 'writeDoubleArray is ' + result);
  let array = data.readDoubleArray();
  hilog.info(0x0000, 'testTag', 'readDoubleArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]writeBooleanArray(deprecated)

writeBooleanArray(booleanArray: boolean\[\]): boolean

将布尔数组写入MessageParcel实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/oNeJ4_-LSWqWgAVmwdmHPg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=CF6E905DE56633FCC68C70BA3D1436870FEC0DA8FA107BE7B94E93751A833053)

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeBooleanArray](#writebooleanarray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| booleanArray | boolean\[\] | 是 | 要写入的布尔数组。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeBooleanArray([false, true, false]);
  hilog.info(0x0000, 'testTag', 'writeBooleanArray is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]readBooleanArray(deprecated)

readBooleanArray(dataIn: boolean\[\]): void

从MessageParcel实例中读取布尔数组，并将其写入到创建的空数组中。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/wHa_QTEQSPSAmks4hQFuGw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=161FA380C6E3ED39E662464833D24DC5387C6C09195DD607B4EFFF0A38227567)

从API version 7 开始支持，API version 9 开始废弃，建议使用[readBooleanArray](#readbooleanarray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| dataIn | boolean\[\] | 是 | 要读取的布尔数组。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeBooleanArray([false, true, false]);
  hilog.info(0x0000, 'testTag', 'writeBooleanArray is ' + result);
  let array: Array<boolean> = new Array(3);
  data.readBooleanArray(array);
  hilog.info(0x0000, 'testTag', 'readBooleanArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]readBooleanArray(deprecated)

readBooleanArray(): boolean\[\]

从MessageParcel实例中读取布尔数组。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/8vWyvGdMTM-sAtqOuRKjlA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=4AEE2158E0EF825B207F8DCAFE84221C0856226E459E1303EA82D102A779ECF6)

从API version 7 开始支持，API version 9 开始废弃，建议使用[readBooleanArray](#readbooleanarray9-1)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean\[\] | 返回布尔数组。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeBooleanArray([false, true, false]);
  hilog.info(0x0000, 'testTag', 'writeBooleanArray is ' + result);
  let array = data.readBooleanArray();
  hilog.info(0x0000, 'testTag', 'readBooleanArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]writeCharArray(deprecated)

writeCharArray(charArray: number\[\]): boolean

将单个字符数组写入MessageParcel实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/OfBvbhwYQuKkEMkxV-Ha_A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=30E4D6BD3CC6F2D30C78555DA5872547AC37B3361C791E0007D5920D3965A726)

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeCharArray](#writechararray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| charArray | number\[\] | 是 | 要写入的单个字符数组。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeCharArray([97, 98, 88]);
  hilog.info(0x0000, 'testTag', 'writeCharArray is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]readCharArray(deprecated)

readCharArray(dataIn: number\[\]): void

从MessageParcel实例中读取单个字符数组，并将其写入到创建的空数组中。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/q9JFxjqWRsavUFxqpwn_Ag/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=B3424AF5E874B777CA9E1F238522E7F4D9FEFEA3F38A55BD4BAD383C109A60B9)

从API version 7 开始支持，API version 9 开始废弃，建议使用[readCharArray](#readchararray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| dataIn | number\[\] | 是 | 要读取的单个字符数组。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeCharArray([97, 98, 99]);
  hilog.info(0x0000, 'testTag', 'writeCharArray is ' + result);
  let array: Array<number> = new Array(3);
  data.readCharArray(array);
  hilog.info(0x0000, 'testTag', 'writeCharArray is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]readCharArray(deprecated)

readCharArray(): number\[\]

从MessageParcel实例中读取单个字符数组。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/XnGn-LSsStGOyLpl1K46Mg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=10717529D6C31FA91CC51B151224B7206C3B9759748F5BCF1C9AE7B7AEF2613D)

从API version 7 开始支持，API version 9 开始废弃，建议使用[readCharArray](#readchararray9-1)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number\[\] | 返回单个字符数组。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeCharArray([97, 98, 99]);
  hilog.info(0x0000, 'testTag', 'writeCharArray is ' + result);
  let array = data.readCharArray();
  hilog.info(0x0000, 'testTag', 'readCharArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]writeStringArray(deprecated)

writeStringArray(stringArray: string\[\]): boolean

将字符串数组写入MessageParcel实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/FLujszZURT6j3sMo7LNYHg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=ADACB171D36B627CAF6247A36A3FA2A89379B1017138F7C1E67DDB1FA9C8A5C4)

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeStringArray](#writestringarray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| stringArray | string\[\] | 是 | 要写入的字符串数组，数组单个元素的长度应小于40960字节。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeStringArray(["abc", "def"]);
  hilog.info(0x0000, 'testTag', 'writeStringArray is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]readStringArray(deprecated)

readStringArray(dataIn: string\[\]): void

从MessageParcel实例中读取字符串数组，并将其写入到创建的空数组中。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/-l9BYMPvQMCYpKZWgAFzag/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=0A73B8272D73C25FF5E90905C6F06015ECFA618BFCF2F7BD217A692DAE130D0E)

从API version 7 开始支持，API version 9 开始废弃，建议使用[readStringArray](#readstringarray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| dataIn | string\[\] | 是 | 要读取的字符串数组。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeStringArray(["abc", "def"]);
  hilog.info(0x0000, 'testTag', 'writeStringArray is ' + result);
  let array: Array<string> = new Array(2);
  data.readStringArray(array);
  hilog.info(0x0000, 'testTag', 'readStringArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]readStringArray(deprecated)

readStringArray(): string\[\]

从MessageParcel实例中读取字符串数组。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/Fpnj5TTWQs2ImUL-jVZQ0g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=8EE36D23499946746470C54E258F0929D5E087F1EA50872AF65EAB11FC9FA5E8)

从API version 7 开始支持，API version 9 开始废弃，建议使用[readStringArray](#readstringarray9-1)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string\[\] | 返回字符串数组。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeStringArray(["abc", "def"]);
  hilog.info(0x0000, 'testTag', 'writeStringArray is ' + result);
  let array = data.readStringArray();
  hilog.info(0x0000, 'testTag', 'readStringArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]writeNoException(deprecated)

writeNoException(): void

向MessageParcel写入“指示未发生异常”的信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/OOLyrRM6TpuctI4o8JsIAg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=F1CA101E04DE8BAAB6D41A5414DC9E382627E2AED1F07E8DBD60B089658962B9)

从API version 8 开始支持，API version 9 开始废弃，建议使用[writeNoException](#writenoexception9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MyDeathRecipient implements rpc.DeathRecipient {
  onRemoteDied() {
    hilog.info(0x0000, 'testTag', 'server died');
  }
}
class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }

onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel, option: rpc.MessageOption): boolean {
    if (code === 1) {
      hilog.info(0x0000, 'testTag', 'RpcServer: onRemoteRequest called');
      reply.writeNoException();
      return true;
    } else {
      hilog.error(0x0000, 'testTag', 'RpcServer: unknown code: ' + code);
      return false;
    }
  }
}
```

#### \[h2\]readException(deprecated)

readException(): void

从MessageParcel中读取异常。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/vnQ1xhjLQlapw35MZaMsmQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=ED74DAAB1185AC63C5BD1D26B41C9CC59DD8E7FABA451A3EBFAC90B32CFF3940)

从API version 8 开始支持，API version 9 开始废弃，建议使用[readException](#readexception9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/oFtno1WFSQeaXadd83VB7Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=EE3B062F4B9F3524A259493300BF14C649068237093DA42C76D8D5A66D6B2C3F)

在本文档的示例中，通过this.getUIContext().getHostContext()来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
// FA模型需要从@kit.AbilityKit导入featureAbility
// import { featureAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { Want, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let proxy: rpc.IRemoteObject | undefined;
let connect: common.ConnectOptions = {
  onConnect: (elementName, remoteProxy) => {
    hilog.info(0x0000, 'testTag', 'js onConnect called');
    proxy = remoteProxy;
  },
  onDisconnect: (elementName) => {
    hilog.info(0x0000, 'testTag', 'onDisconnect');
  },
  onFailed: () => {
    hilog.info(0x0000, 'testTag', 'onFailed');
  }
};
let want: Want = {
  // 获取服务端包名和ability名称
  bundleName: "com.ohos.server",
  abilityName: "com.ohos.server.EntryAbility",
};

// FA模型使用此方法连接服务
// FA.connectAbility(want,connect);

// 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
// 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
let connectionId = context.connectServiceExtensionAbility(want, connect);
```

上述onConnect回调函数中的proxy对象需要等ability异步连接成功后才会被赋值，然后才可调用proxy对象的sendRequest接口方法发送消息

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let option = new rpc.MessageOption();
  let data = rpc.MessageParcel.create();
  let reply = rpc.MessageParcel.create();
  data.writeNoException();
  data.writeString('hello');
  if (proxy != undefined) {
    let a = proxy.sendRequest(1, data, reply, option) as Object;
    let b = a as Promise<rpc.SendRequestResult>;
    b.then((result: rpc.SendRequestResult) => {
      if (result.errCode === 0) {
        hilog.info(0x0000, 'testTag', 'sendRequest got result');
        result.reply.readException();
        let msg = result.reply.readString();
        hilog.info(0x0000, 'testTag', 'reply msg: ' + msg);
      } else {
        hilog.error(0x0000, 'testTag', 'sendRequest failed, errCode: ' + result.errCode);
      }
    }).catch((e: Error) => {
      hilog.error(0x0000, 'testTag', 'sendRequest got exception: ' + JSON.stringify(e));
    }).finally (() => {
      hilog.info(0x0000, 'testTag', 'sendRequest ends, reclaim parcel');
      data.reclaim();
      reply.reclaim();
    });
  }
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]writeSequenceableArray(deprecated)

writeSequenceableArray(sequenceableArray: Sequenceable\[\]): boolean

将可序列化对象数组写入MessageParcel实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/PIiY-Vg3TNi07Mk7QuMVjQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=5AB5BBBADCBBAA0E03A8495007B3DF4D549235B01D3C23E32035924B82F8B902)

从API version 7 开始支持，API version 9 开始废弃，建议使用[writeParcelableArray](#writeparcelablearray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| sequenceableArray | [Sequenceable](#sequenceabledeprecated)\[\] | 是 | 要写入的可序列化对象数组。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MySequenceable implements rpc.Sequenceable {
  num: number = 0;
  str: string = '';
  constructor(num: number, str: string) {
    this.num = num;
    this.str = str;
  }
  marshalling(messageParcel: rpc.MessageParcel): boolean {
    messageParcel.writeInt(this.num);
    messageParcel.writeString(this.str);
    return true;
  }
  unmarshalling(messageParcel: rpc.MessageParcel): boolean {
    this.num = messageParcel.readInt();
    this.str = messageParcel.readString();
    return true;
  }
}

try {
  let sequenceable = new MySequenceable(1, "aaa");
  let sequenceable2 = new MySequenceable(2, "bbb");
  let sequenceable3 = new MySequenceable(3, "ccc");
  let a = [sequenceable, sequenceable2, sequenceable3];
  let data = rpc.MessageParcel.create();
  let result = data.writeSequenceableArray(a);
  hilog.info(0x0000, 'testTag', 'writeSequenceableArray is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]readSequenceableArray(deprecated)

readSequenceableArray(sequenceableArray: Sequenceable\[\]): void

从MessageParcel实例中读取可序列化对象数组。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/8OIgJ_C4S9udK-KMoDIQdg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=0711BFE0B5A0ABEAEE4EE9D87A8DE8F7B77EA22B5FB6452BE331D077336E9093)

从API version 8 开始支持，API version 9 开始废弃，建议使用[readParcelableArray](#readparcelablearray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| sequenceableArray | [Sequenceable](#sequenceabledeprecated)\[\] | 是 | 要读取的可序列化对象数组。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MySequenceable implements rpc.Sequenceable {
  num: number = 0;
  str: string = '';
  constructor(num: number, str: string) {
    this.num = num;
    this.str = str;
  }
  marshalling(messageParcel: rpc.MessageParcel): boolean {
    messageParcel.writeInt(this.num);
    messageParcel.writeString(this.str);
    return true;
  }
  unmarshalling(messageParcel: rpc.MessageParcel): boolean {
    this.num = messageParcel.readInt();
    this.str = messageParcel.readString();
    return true;
  }
}

try {
  let sequenceable = new MySequenceable(1, "aaa");
  let sequenceable2 = new MySequenceable(2, "bbb");
  let sequenceable3 = new MySequenceable(3, "ccc");
  let a = [sequenceable, sequenceable2, sequenceable3];
  let data = rpc.MessageParcel.create();
  let result = data.writeSequenceableArray(a);
  hilog.info(0x0000, 'testTag', 'writeSequenceableArray is ' + result);
  let b = [new MySequenceable(0, ""), new MySequenceable(0, ""), new MySequenceable(0, "")];
  data.readSequenceableArray(b);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]writeRemoteObjectArray(deprecated)

writeRemoteObjectArray(objectArray: IRemoteObject\[\]): boolean

将IRemoteObject对象数组写入MessageParcel。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/B3QNEECKROaAd-BmOKap9Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=B5A625B732CE961A553E363D6D8F6C1C02099DCE66DCB1E3E6664063E79CCBCE)

从API version 8 开始支持，API version 9 开始废弃，建议使用[writeRemoteObjectArray](#writeremoteobjectarray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| objectArray | [IRemoteObject](#iremoteobject)\[\] | 是 | 要写入MessageParcel的IRemoteObject对象数组。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel,
    option: rpc.MessageOption): boolean {
    // 具体处理由业务决定
    return true;
  }
}

try {
  let a = [new TestRemoteObject("testObject1"), new TestRemoteObject("testObject2"), new TestRemoteObject("testObject3")];
  let data = rpc.MessageParcel.create();
  let result = data.writeRemoteObjectArray(a);
  hilog.info(0x0000, 'testTag', 'writeRemoteObjectArray is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]readRemoteObjectArray(deprecated)

readRemoteObjectArray(objects: IRemoteObject\[\]): void

从MessageParcel读取IRemoteObject对象数组，并将其写入到创建的空数组中。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/VafYNVogRb6SlQsXjigJVQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=09907096892487CCCE435E50072876CA44584FE4B1429EED21919D6B9A47F644)

从API version 8 开始支持，API version 9 开始废弃，建议使用[readRemoteObjectArray](#readremoteobjectarray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| objects | [IRemoteObject](#iremoteobject)\[\] | 是 | 从MessageParcel读取的IRemoteObject对象数组。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel,
    option: rpc.MessageOption): boolean {
    // 具体处理由业务决定
    return true;
  }
}

try {
  let a = [new TestRemoteObject("testObject1"), new TestRemoteObject("testObject2"),
    new TestRemoteObject("testObject3")];
  let data = rpc.MessageParcel.create();
  data.writeRemoteObjectArray(a);
  let b: Array<rpc.IRemoteObject> = new Array(3);
  data.readRemoteObjectArray(b);
  hilog.info(0x0000, 'testTag', 'readRemoteObjectArray is ' + b);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]readRemoteObjectArray(deprecated)

readRemoteObjectArray(): IRemoteObject\[\]

从MessageParcel读取IRemoteObject对象数组。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/fdPn1YdHRkWcOgfwdyZjew/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=051117CDE947C2B73FAF52CE95A5C33FA6AE37379774E2DBC6961B15E256918C)

从API version 8 开始支持，API version 9 开始废弃，建议使用[readRemoteObjectArray](#readremoteobjectarray9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [IRemoteObject](#iremoteobject)\[\] | 返回IRemoteObject对象数组。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel,
    option: rpc.MessageOption): boolean {
    // 具体处理由业务决定
    return true;
  }
}

try {
  let a = [new TestRemoteObject("testObject1"), new TestRemoteObject("testObject2"),
    new TestRemoteObject("testObject3")];
  let data = rpc.MessageParcel.create();
  let result = data.writeRemoteObjectArray(a);
  hilog.info(0x0000, 'testTag', 'readRemoteObjectArray is ' + result);
  let b = data.readRemoteObjectArray();
  hilog.info(0x0000, 'testTag', 'readRemoteObjectArray is ' + b);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]closeFileDescriptor(deprecated)

static closeFileDescriptor(fd: number): void

静态方法，关闭给定的文件描述符。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/9WwQS-wTRoKPKm4EvWCcJw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=42A769BF64375140FC1789ED079B0A2A715AA5FD947CCF6E941D250DD6DC6956)

从API version 8 开始支持，API version 9 开始废弃，建议使用[closeFileDescriptor](#closefiledescriptor9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 要关闭的文件描述符。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { fileIo } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let filePath = "path/to/file";
  let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
  rpc.MessageParcel.closeFileDescriptor(file.fd);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]dupFileDescriptor(deprecated)

static dupFileDescriptor(fd: number) :number

静态方法，复制给定的文件描述符。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/Hj8TmfIlTm2_n85L54DJJA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=3E7750B1C442A04A196FB1B1ECC280FD03B55ABC9ECF09836BF5FB9999429192)

从API version 8 开始支持，API version 9 开始废弃，建议使用[dupFileDescriptor](#dupfiledescriptor9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 表示已存在的文件描述符。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回新的文件描述符。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { fileIo } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let filePath = "path/to/file";
  let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
  rpc.MessageParcel.dupFileDescriptor(file.fd);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]containFileDescriptors(deprecated)

containFileDescriptors(): boolean

检查此MessageParcel对象是否包含文件描述符。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/M1PfbewqQXadqMqRWcQbyQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=2F91D068E4DE7C958938CF8C6C271B8AC5CF5F522192A1A2A26B37A80C12ADEB)

从API version 8 开始支持，API version 9 开始废弃，建议使用[containFileDescriptors](#containfiledescriptors9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：包含文件描述符，false：未包含文件描述符。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { fileIo } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let parcel = new rpc.MessageParcel();
  let filePath = "path/to/file";
  let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
  let writeResult = parcel.writeFileDescriptor(file.fd);
  hilog.info(0x0000, 'testTag', 'parcel writeFd result is ' + writeResult);
  let containFD = parcel.containFileDescriptors();
  hilog.info(0x0000, 'testTag', 'parcel after write fd containFd result is ' + containFD);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]writeFileDescriptor(deprecated)

writeFileDescriptor(fd: number): boolean

写入文件描述符到MessageParcel。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/t29AX1HgTXO3qii8bUdU3A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=010C19843732DC37908754B912FEB8EF721B1AE102E89CDF6F926CC7D4A49DB5)

从API version 8 开始支持，API version 9 开始废弃，建议使用[writeFileDescriptor](#writefiledescriptor9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fd | number | 是 | 文件描述符。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：操作成功，false：操作失败。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { fileIo } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let parcel = new rpc.MessageParcel();
  let filePath = "path/to/file";
  let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
  let writeResult = parcel.writeFileDescriptor(file.fd);
  hilog.info(0x0000, 'testTag', 'parcel writeFd result is ' + writeResult);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]readFileDescriptor(deprecated)

readFileDescriptor(): number

从MessageParcel中读取文件描述符。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/9d5V__u0ShmFNnkggYdm_A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=AD2AC85780B8F417AD3E5BD9D0FB8EA6679F44D25F3B722A5B45528047D3A380)

从API version 8 开始支持，API version 9 开始废弃，建议使用[readFileDescriptor](#readfiledescriptor9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回文件描述符。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { fileIo } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let parcel = new rpc.MessageParcel();
  let filePath = "path/to/file";
  let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
  parcel.writeFileDescriptor(file.fd);
  let readFD = parcel.readFileDescriptor();
  hilog.info(0x0000, 'testTag', 'parcel read fd is ' + readFD);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]writeAshmem(deprecated)

writeAshmem(ashmem: Ashmem): boolean

将指定的匿名共享对象写入此MessageParcel。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/ZTw7-RQiSUCHRmjt9YXLFA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=8E65ABFD1E1D00C83C9B44349BCFC09312D415FB7573C5B7DE38D2E8D5A89123)

从API version 8 开始支持，API version 9 开始废弃，建议使用[writeAshmem](#writeashmem9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| ashmem | [Ashmem](#ashmem8) | 是 | 要写入MessageParcel的匿名共享对象。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let parcel = new rpc.MessageParcel();
  let ashmem = rpc.Ashmem.createAshmem("ashmem", 1024);
  let isWriteSuccess = parcel.writeAshmem(ashmem);
  hilog.info(0x0000, 'testTag', 'write ashmem to result is ' + isWriteSuccess);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]readAshmem(deprecated)

readAshmem(): Ashmem

从MessageParcel读取匿名共享对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/-5guIptjTNWrFhiFvJEtVQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=5BE0B12488855F55924A81ECB03DE78621AD39271D32C7D124D40150010363BD)

从API version 8 开始支持，API version 9 开始废弃，建议使用[readAshmem](#readashmem9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [Ashmem](#ashmem8) | 返回匿名共享对象。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let parcel = new rpc.MessageParcel();
  let ashmem = rpc.Ashmem.createAshmem("ashmem", 1024);
  let isWriteSuccess = parcel.writeAshmem(ashmem);
  hilog.info(0x0000, 'testTag', 'write ashmem to result is ' + isWriteSuccess);
  let readAshmem = parcel.readAshmem();
  hilog.info(0x0000, 'testTag', 'read ashmem to result is ' + readAshmem);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]getRawDataCapacity(deprecated)

getRawDataCapacity(): number

获取MessageParcel可以容纳的最大原始数据量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/ZEuIT8vxSCatEIs5Q8iPMg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=5C09E3B8CB3ECED8D2D7F618B18B78CE6C9EDBDC629ECE14572D1B2F5088CF1E)

从API version 8 开始支持，API version 9 开始废弃，建议使用[getRawDataCapacity](#getrawdatacapacity9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回MessageParcel可以容纳的最大原始数据量，即128MB。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let parcel = new rpc.MessageParcel();
  let result = parcel.getRawDataCapacity();
  hilog.info(0x0000, 'testTag', 'parcel get RawDataCapacity result is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]writeRawData(deprecated)

writeRawData(rawData: number\[\], size: number): boolean

将原始数据写入MessageParcel对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/NmHc3lh5QJGWyRdtDxDuaQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=6E0C3D4251DB9C265A322806338E30D19FDA70988A6AE9837715AF433C480B7A)

从API version 8 开始支持，API version 9 开始废弃，建议使用[writeRawDataBuffer](#writerawdatabuffer11)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| rawData | number\[\] | 是 | 要写入的原始数据，大小不能超过128MB。 |
| size | number | 是 | 发送的原始数据大小，以字节为单位。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：写入成功，false：写入失败。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let parcel = new rpc.MessageParcel();
  let arr = [1, 2, 3, 4, 5];
  let isWriteSuccess = parcel.writeRawData(arr, arr.length);
  hilog.info(0x0000, 'testTag', 'parcel write raw data result is ' + isWriteSuccess);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]readRawData(deprecated)

readRawData(size: number): number\[\]

从MessageParcel读取原始数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/nsaHu9lvT72YGJg-O0mAQw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=79F71EDDBCA6B951B436DA981105974B65EA4B6178712AD1A8BB71513E453D4D)

从API version 8 开始支持，API version 9 开始废弃，建议使用[readRawDataBuffer](#readrawdatabuffer11)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| size | number | 是 | 要读取的原始数据的大小。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number\[\] | 返回原始数据（以字节为单位）。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let parcel = new rpc.MessageParcel();
  let arr = [1, 2, 3, 4, 5];
  let isWriteSuccess = parcel.writeRawData(arr, arr.length);
  hilog.info(0x0000, 'testTag', 'parcel write raw data result is ' + isWriteSuccess);
  let result = parcel.readRawData(5);
  hilog.info(0x0000, 'testTag', 'parcel read raw data result is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### Parcelable9+

在进程间通信（IPC）期间，将类的对象写入MessageSequence并从MessageSequence中恢复它们。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

#### \[h2\]marshalling9+

marshalling(dataOut: MessageSequence): boolean

将此可序列对象封送到MessageSequence中。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| dataOut | [MessageSequence](#messagesequence9) | 是 | 可序列对象将被封送到的MessageSequence对象。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：封送成功，false：封送失败。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MyParcelable implements rpc.Parcelable {
  num: number = 0;
  str: string = '';
  constructor(num: number, str: string) {
    this.num = num;
    this.str = str;
  }
  marshalling(messageSequence: rpc.MessageSequence): boolean {
    messageSequence.writeInt(this.num);
    messageSequence.writeString(this.str);
    return true;
  }
  unmarshalling(messageSequence: rpc.MessageSequence): boolean {
    this.num = messageSequence.readInt();
    this.str = messageSequence.readString();
    hilog.info(0x0000, 'testTag', 'readInt is ' + this.num + ' readString is ' + this.str);
    return true;
  }
}

try {
  let parcelable = new MyParcelable(1, "aaa");
  let data = rpc.MessageSequence.create();
  data.writeParcelable(parcelable);
  let ret = new MyParcelable(0, "");
  data.readParcelable(ret);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]unmarshalling9+

unmarshalling(dataIn: MessageSequence): boolean

从MessageSequence中解封此可序列对象。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| dataIn | [MessageSequence](#messagesequence9) | 是 | 已将可序列对象封送到其中的MessageSequence对象。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：反序列化成功，false：反序列化失败。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MyParcelable implements rpc.Parcelable {
  num: number = 0;
  str: string = '';
  constructor(num: number, str: string) {
    this.num = num;
    this.str = str;
  }
  marshalling(messageSequence: rpc.MessageSequence): boolean {
    messageSequence.writeInt(this.num);
    messageSequence.writeString(this.str);
    return true;
  }
  unmarshalling(messageSequence: rpc.MessageSequence): boolean {
    this.num = messageSequence.readInt();
    this.str = messageSequence.readString();
    hilog.info(0x0000, 'testTag', 'readInt is ' + this.num + ' readString is ' + this.str);
    return true;
  }
}

try {
  let parcelable = new MyParcelable(1, "aaa");
  let data = rpc.MessageSequence.create();
  data.writeParcelable(parcelable);
  let ret = new MyParcelable(0, "");
  data.readParcelable(ret);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### Sequenceable(deprecated)

在进程间通信（IPC）期间，将类的对象写入MessageParcel并从MessageParcel中恢复它们。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/jezMKSpdQo25ObKYjwk0Eg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=2AF42D51EDBF5299C9284B306823657E4A4E04FF870A17B6117AE313C3297955)

从API version 7 开始支持，API version 9 开始废弃，建议使用[Parcelable](#parcelable9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

#### \[h2\]marshalling(deprecated)

marshalling(dataOut: MessageParcel): boolean

将此可序列对象封送到MessageParcel中。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/qWPdlSfxTLiEOkC6LCYRTQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=449D4C4BBA80D0876B50789BD7790FD3A820CBF4E95FBB12CAF17D72201F1804)

从API version 7 开始支持，API version 9 开始废弃，建议使用[marshalling](#marshalling9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| dataOut | [MessageParcel](#messageparceldeprecated) | 是 | 可序列对象将被封送到的MessageParcel对象。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：封送成功，false：封送失败。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MySequenceable implements rpc.Sequenceable {
  num: number = 0;
  str: string = '';
  constructor(num: number, str: string) {
    this.num = num;
    this.str = str;
  }
  marshalling(messageParcel: rpc.MessageParcel): boolean {
    messageParcel.writeInt(this.num);
    messageParcel.writeString(this.str);
    return true;
  }
  unmarshalling(messageParcel: rpc.MessageParcel): boolean {
    this.num = messageParcel.readInt();
    this.str = messageParcel.readString();
    return true;
  }
}

try {
  let sequenceable = new MySequenceable(1, "aaa");
  let data = rpc.MessageParcel.create();
  let result = data.writeSequenceable(sequenceable);
  hilog.info(0x0000, 'testTag', 'writeSequenceable is ' + result);
  let ret = new MySequenceable(0, "");
  let result2 = data.readSequenceable(ret);
  hilog.info(0x0000, 'testTag', 'readSequenceable is ' + result2);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]unmarshalling(deprecated)

unmarshalling(dataIn: MessageParcel): boolean

从MessageParcel中解封此可序列对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/WFBUsEaNRkyz7lC59WmBLQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=B24904F009EE7757547D07CEDB73FD451C267E13AD6030D3453791BE4295E0D5)

从API version 7 开始支持，API version 9 开始废弃，建议使用[unmarshalling](#unmarshalling9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| dataIn | [MessageParcel](#messageparceldeprecated) | 是 | 已将可序列对象封送到其中的MessageParcel对象。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：反序列化成功，false：反序列化失败。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MySequenceable implements rpc.Sequenceable {
  num: number = 0;
  str: string = '';
  constructor(num: number, str: string) {
    this.num = num;
    this.str = str;
  }
  marshalling(messageParcel: rpc.MessageParcel): boolean {
    messageParcel.writeInt(this.num);
    messageParcel.writeString(this.str);
    return true;
  }
  unmarshalling(messageParcel: rpc.MessageParcel): boolean {
    this.num = messageParcel.readInt();
    this.str = messageParcel.readString();
    return true;
  }
}

try {
  let sequenceable = new MySequenceable(1, "aaa");
  let data = rpc.MessageParcel.create();
  let result = data.writeSequenceable(sequenceable);
  hilog.info(0x0000, 'testTag', 'writeSequenceable is ' + result);
  let ret = new MySequenceable(0, "");
  let result2 = data.readSequenceable(ret);
  hilog.info(0x0000, 'testTag', 'readSequenceable is ' + result2);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### IRemoteBroker

远端对象的代理持有者。用于获取代理对象。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

#### \[h2\]asObject

asObject(): IRemoteObject

需派生类实现，获取代理或远端对象。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [IRemoteObject](#iremoteobject) | 如果调用者是RemoteObject对象，则直接返回本身；如果调用者是[RemoteProxy](#remoteproxy)对象，则返回它的持有者[IRemoteObject](#iremoteobject)。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';

class TestAbility extends rpc.RemoteObject {
  asObject() {
    return this;
  }
}
let remoteObject = new TestAbility("testObject").asObject();
```

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/3EBhejo9SiisZpoB4YtbcA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=0F200C4B76D16F356C27E8A72CB80294F8F048BA8684A71A5CBB25CF6EFB6623)

在本文档的示例中，通过this.getUIContext().getHostContext()来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
// FA模型需要从@kit.AbilityKit导入featureAbility
// import { featureAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { Want, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let proxy: rpc.IRemoteObject | undefined;
let connect: common.ConnectOptions = {
  onConnect: (elementName, remoteProxy) => {
    hilog.info(0x0000, 'testTag', 'js onConnect called');
    proxy = remoteProxy;
  },
  onDisconnect: (elementName) => {
    hilog.info(0x0000, 'testTag', 'onDisconnect');
  },
  onFailed: () => {
    hilog.info(0x0000, 'testTag', 'onFailed');
  }
};
let want: Want  = {
  // 获取服务端包名和ability名称
  bundleName: "com.ohos.server",
  abilityName: "com.ohos.server.EntryAbility",
};

// FA模型使用此方法连接服务
// FA.connectAbility(want,connect);

// 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
// 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
let connectionId = context.connectServiceExtensionAbility(want, connect);
```

上述onConnect回调函数中的proxy对象需要等ability异步连接成功后才会被赋值，然后才可调用proxy对象的asObject接口方法获取代理或远端对象

```ts
import { rpc } from '@kit.IPCKit';

class TestProxy {
  remote: rpc.IRemoteObject;
  constructor(remote: rpc.IRemoteObject) {
    this.remote = remote;
  }
  asObject() {
    return this.remote;
  }
}
if (proxy != undefined) {
  let iRemoteObject = new TestProxy(proxy).asObject();
}
```

#### DeathRecipient

用于订阅远端对象的死亡通知。当被订阅该通知的远端对象死亡时，本端可收到消息，调用[onRemoteDied](#onremotedied)接口。远端对象死亡可以为远端对象所在进程死亡，远端对象所在设备关机或重启，当远端对象与本端对象属于不同设备时，也可为远端对象离开组网时。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

#### \[h2\]onRemoteDied

onRemoteDied(): void

在成功添加死亡通知订阅后，当远端对象死亡时，将自动调用本方法。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MyDeathRecipient implements rpc.DeathRecipient {
  onRemoteDied() {
    hilog.info(0x0000, 'testTag', 'server died');
  }
}
```

#### RequestResult9+

发送请求的响应结果。

\*\*系统能力：\*\*以下各项对应的系统能力均为SystemCapability.Communication.IPC.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| errCode | number | 否 | 否 | 错误码。 |
| code | number | 否 | 否 | 消息代码。 |
| data | [MessageSequence](#messagesequence9) | 否 | 否 | 发送给对端进程的MessageSequence对象。 |
| reply | [MessageSequence](#messagesequence9) | 否 | 否 | 对端进程返回的MessageSequence对象。 |

#### SendRequestResult(deprecated)

发送请求的响应结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/rxjwnAsTQ-6lpJKsohJJsw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=68E7EEB3A69D09C55B989A7BBADE481A2D2C7BE85B405D62A30A17101F3682AA)

从API version 8 开始支持，API version 9 开始废弃，建议使用[RequestResult](#requestresult9)替代。

\*\*系统能力：\*\*以下各项对应的系统能力均为SystemCapability.Communication.IPC.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| errCode | number | 否 | 否 | 错误码。 |
| code | number | 否 | 否 | 消息代码。 |
| data | [MessageParcel](#messageparceldeprecated) | 否 | 否 | 发送给对端进程的MessageParcel对象。 |
| reply | [MessageParcel](#messageparceldeprecated) | 否 | 否 | 对端进程返回的MessageParcel对象。 |

#### CallingInfo23+

IPC上下文信息，包括PID和UID、本端和对端设备ID、检查接口调用是否在同一设备上。

\*\*系统能力：\*\*以下各项对应的系统能力均为SystemCapability.Communication.IPC.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| callerPid | number | 是 | 否 | 调用者的PID。 |
| callerUid | number | 是 | 否 | 调用者的UID。 |
| callerTokenId | number | 是 | 否 | 调用者的TokenId。 |
| remoteDeviceId | string | 是 | 否 | 对端设备的设备ID，仅RPC场景有效。 |
| localDeviceId | string | 是 | 否 | 本端设备的设备ID，仅RPC场景有效。 |
| isLocalCalling | boolean | 是 | 否 | 当前通信对端是否为本设备进程。true：调用在同一台设备，false：调用未在同一台设备。 |

#### IRemoteObject

该接口可用于查询或获取接口描述符、添加或删除死亡通知、转储对象状态到特定文件、发送消息。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

#### \[h2\]getLocalInterface9+

getLocalInterface(descriptor: string): IRemoteBroker

查询接口描述符的字符串。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| descriptor | string | 是 | 接口描述符的字符串。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [IRemoteBroker](#iremotebroker) | 返回绑定到指定接口描述符的IRemoteBroker对象。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.The string length is greater than or equal to 40960 bytes;

4.The number of bytes copied to the buffer is different from the length of the obtained string.

 |

#### \[h2\]queryLocalInterface(deprecated)

queryLocalInterface(descriptor: string): IRemoteBroker

查询接口描述符的字符串。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/vXn9-JyQS8iMb2y9hK-8rQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=92AAA1660ED444FBF32B7E9A5493726F581DE6DF246DAE2E279B31145B7FD00F)

从API version 7 开始支持，API version 9 开始废弃，建议使用[getLocalInterface](#getlocalinterface9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| descriptor | string | 是 | 接口描述符的字符串。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [IRemoteBroker](#iremotebroker) | 返回绑定到指定接口描述符的IRemoteBroker对象。 |

#### \[h2\]sendRequest(deprecated)

sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): boolean

以同步或异步方式向对端进程发送MessageParcel消息。如果为选项设置了异步模式，则期约立即兑现，reply报文里没有内容。如果为选项设置了同步模式，则期约将在sendRequest返回时兑现，回复内容在reply报文里。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/XvqLPBvmSJCpP30jhbjP4g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=AEB389BEAB4F4C4B0A833B030F641E2ABE3089B34299D1BDC71F04A5827EB8E9)

从API version 7 开始支持，API version 9 开始废弃，建议使用[sendMessageRequest](#sendmessagerequest9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| code | number | 是 | 本次请求调用的消息码\[1-16777215\]，由通信双方确定。如果接口由IDL工具生成，则消息代码由IDL自动生成。 |
| data | [MessageParcel](#messageparceldeprecated) | 是 | 保存待发送数据的MessageParcel对象。 |
| reply | [MessageParcel](#messageparceldeprecated) | 是 | 接收应答数据的MessageParcel对象。 |
| options | [MessageOption](#messageoption) | 是 | 本次请求的同异步模式，默认同步调用。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：发送成功，false：发送失败。 |

#### \[h2\]sendMessageRequest9+

sendMessageRequest(code: number, data: MessageSequence, reply: MessageSequence, options: MessageOption): Promise<RequestResult>

以同步或异步方式向对端进程发送MessageSequence消息。如果为选项设置了异步模式，则期约立即兑现，reply报文里没有内容，具体回复需要在业务侧的回调中获取。如果为选项设置了同步模式，则期约将在sendMessageRequest返回时兑现，回复内容在reply报文里。使用Promise异步回调。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| code | number | 是 | 本次请求调用的消息码\[1-16777215\]，由通信双方确定。如果接口由IDL工具生成，则消息代码由IDL自动生成。 |
| data | [MessageSequence](#messagesequence9) | 是 | 保存待发送数据的MessageSequence对象。 |
| reply | [MessageSequence](#messagesequence9) | 是 | 接收应答数据的MessageSequence对象。 |
| options | [MessageOption](#messageoption) | 是 | 本次请求的同异步模式，默认同步调用。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[RequestResult](#requestresult9)\> | Promise对象，返回一个期约，兑现值是requestResult实例。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.Failed to obtain the passed object instance.

 |

#### \[h2\]sendRequest(deprecated)

sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): Promise<SendRequestResult>

以同步或异步方式向对端进程发送MessageParcel消息。如果为选项设置了异步模式，则期约立即兑现，reply报文里没有内容，具体回复需要在业务侧的回调中获取。如果为选项设置了同步模式，则期约将在sendRequest返回时兑现，回复内容在reply报文里。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/MEPdexgWQqSnx5B2WIGUqQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=71A39D24084AB1A58CAFE66D8ACE46BD68F261E66DD0CE25F5E1DCCB9EB463D3)

从API version 8 开始支持，API version 9 开始废弃，建议使用[sendMessageRequest](#sendmessagerequest9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| code | number | 是 | 本次请求调用的消息码\[1-16777215\]，由通信双方确定。如果接口由IDL工具生成，则消息代码由IDL自动生成。 |
| data | [MessageParcel](#messageparceldeprecated) | 是 | 保存待发送数据的MessageParcel对象。 |
| reply | [MessageParcel](#messageparceldeprecated) | 是 | 接收应答数据的MessageParcel对象。 |
| options | [MessageOption](#messageoption) | 是 | 本次请求的同异步模式，默认同步调用。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[SendRequestResult](#sendrequestresultdeprecated)\> | Promise对象，返回一个期约，兑现值是sendRequestResult实例。 |

#### \[h2\]sendMessageRequest9+

sendMessageRequest(code: number, data: MessageSequence, reply: MessageSequence, options: MessageOption, callback: AsyncCallback<RequestResult>): void

以同步或异步方式向对端进程发送MessageSequence消息。如果为选项设置了异步模式，则立即收到回调，reply报文里没有内容，具体回复需要在业务侧的回调中获取。如果为选项设置了同步模式，则将在sendRequest返回时收到回调，回复内容在reply报文里。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| code | number | 是 | 本次请求调用的消息码\[1-16777215\]，由通信双方确定。如果接口由IDL工具生成，则消息代码由IDL自动生成。 |
| data | [MessageSequence](#messagesequence9) | 是 | 保存待发送数据的MessageSequence对象。 |
| reply | [MessageSequence](#messagesequence9) | 是 | 接收应答数据的MessageSequence对象。 |
| options | [MessageOption](#messageoption) | 是 | 本次请求的同异步模式，默认同步调用。 |
| callback | AsyncCallback<[RequestResult](#requestresult9)\> | 是 | 回调函数。当消息发送成功时，可从RequestResult中读取服务端返回的数据。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.Failed to obtain the passed object instance.

 |

#### \[h2\]sendRequest(deprecated)

sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption, callback: AsyncCallback<SendRequestResult>): void

以同步或异步方式向对端进程发送MessageParcel消息。如果为选项设置了异步模式，则立即收到回调，reply报文里没有内容，具体回复需要在业务侧的回调中获取。如果为选项设置了同步模式，则将在sendRequest返回时收到回调，回复内容在reply报文里。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/qivWNiGeTwGBkaSOrbs-5g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=2384CBEF580884B92DF726F5351F6482877A24D80571C0DE29BC915F063F02BC)

从API version 8 开始支持，API version 9 开始废弃，建议使用[sendMessageRequest](#sendmessagerequest9-1)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| code | number | 是 | 本次请求调用的消息码\[1-16777215\]，由通信双方确定。如果接口由IDL工具生成，则消息代码由IDL自动生成。 |
| data | [MessageParcel](#messageparceldeprecated) | 是 | 保存待发送数据的MessageParcel对象。 |
| reply | [MessageParcel](#messageparceldeprecated) | 是 | 接收应答数据的MessageParcel对象。 |
| options | [MessageOption](#messageoption) | 是 | 本次请求的同异步模式，默认同步调用。 |
| callback | AsyncCallback<[SendRequestResult](#sendrequestresultdeprecated)\> | 是 | 接收发送结果的回调。 |

#### \[h2\]registerDeathRecipient9+

registerDeathRecipient(recipient: DeathRecipient, flags: number): void

注册用于接收远程对象死亡通知的回调。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| recipient | [DeathRecipient](#deathrecipient) | 是 | 要注册的回调。 |
| flags | number | 是 | 死亡通知标志。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.The callback used to receive remote object death notifications is empty.

 |
| 1900005 | Operation allowed only for the proxy object. |
| 1900008 | The proxy or remote object is invalid. |

#### \[h2\]addDeathRecipient(deprecated)

addDeathRecipient(recipient: DeathRecipient, flags: number): boolean

注册用于接收远程对象死亡通知的回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/_XTC37ZnQ1qS8XFDlAQDHA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=6B08754DB3AA5BA0543E4BCFC451D51ABC90204C300D05ADF37160C3E082EA23)

从API version 7 开始支持，API version 9 开始废弃，建议使用[registerDeathRecipient](#registerdeathrecipient9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| recipient | [DeathRecipient](#deathrecipient) | 是 | 要注册的回调。 |
| flags | number | 是 | 死亡通知标志。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：回调注册成功，false：回调注册失败。 |

#### \[h2\]unregisterDeathRecipient9+

unregisterDeathRecipient(recipient: DeathRecipient, flags: number): void

注销用于接收远程对象死亡通知的回调。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| recipient | [DeathRecipient](#deathrecipient) | 是 | 要注销的回调。 |
| flags | number | 是 | 死亡通知标志。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.The callback used to receive remote object death notifications is empty.

 |
| 1900005 | Operation allowed only for the proxy object. |
| 1900008 | The proxy or remote object is invalid. |

#### \[h2\]removeDeathRecipient(deprecated)

removeDeathRecipient(recipient: DeathRecipient, flags: number): boolean

注销用于接收远程对象死亡通知的回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/EBdxJv37SAOXmB3ozCKTRg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=70964E02931BCCC28AE95F058CD9689B12DE949A79D91F5D114D4A1DA11A2804)

从API version 7 开始支持，API version 9 开始废弃，建议使用[unregisterDeathRecipient](#unregisterdeathrecipient9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| recipient | [DeathRecipient](#deathrecipient) | 是 | 要注销的回调。 |
| flags | number | 是 | 死亡通知标志。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：回调注销成功，false：回调注销失败。 |

#### \[h2\]getDescriptor9+

getDescriptor(): string

获取对象的接口描述符，接口描述符为字符串。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 返回接口描述符。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 1900008 | The proxy or remote object is invalid. |

#### \[h2\]getInterfaceDescriptor(deprecated)

getInterfaceDescriptor(): string

获取对象的接口描述符，接口描述符为字符串。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/Pzzkqn93RU2tvfW86szKag/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=CBA6BF70DB299012987B1D92B2CD9B4A54A3A6F2B3DA223662CAF78851FDABF9)

从API version 7 开始支持，API version 9 开始废弃，建议使用[getDescriptor](#getdescriptor9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 返回接口描述符。 |

#### \[h2\]isObjectDead

isObjectDead(): boolean

检查当前对象是否死亡。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：对象死亡，false：对象未死亡。 |

#### RemoteProxy

实现IRemoteObject代理对象。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

#### \[h2\]属性

\*\*系统能力：\*\*以下各项对应的系统能力均为SystemCapability.Communication.IPC.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| PING\_TRANSACTION | number | 是 | 否 | 内部指令码，用于测试IPC服务是否正常。 |
| DUMP\_TRANSACTION | number | 是 | 否 | 内部指令码，获取IPC服务相关的状态信息。 |
| INTERFACE\_TRANSACTION | number | 是 | 否 | 内部指令码，获取对端接口描述符。 |
| MIN\_TRANSACTION\_ID | number | 是 | 否 | 最小有效指令码。 |
| MAX\_TRANSACTION\_ID | number | 是 | 否 | 最大有效指令码。 |

#### \[h2\]sendRequest(deprecated)

sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): boolean

以同步或异步方式向对端进程发送MessageParcel消息。如果为选项设置了异步模式，则期约立即兑现，reply报文里没有内容，具体回复需要在业务侧的回调中获取。如果为选项设置了同步模式，则期约将在sendRequest返回时兑现，回复内容在reply报文里。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/cevZ8fGUTvWsvPuPafJQkQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=E274AF293627574E0AF85257361EB0241B4B1D4DA5FF1B6C38BACC3BE44DBB8E)

从API version 7 开始支持，API version 8 开始废弃，建议使用[sendMessageRequest](#sendmessagerequest9-2)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| code | number | 是 | 本次请求调用的消息码\[1-16777215\]，由通信双方确定。如果接口由IDL工具生成，则消息代码由IDL自动生成。 |
| data | [MessageParcel](#messageparceldeprecated) | 是 | 保存待发送数据的MessageParcel对象。 |
| reply | [MessageParcel](#messageparceldeprecated) | 是 | 接收应答数据的MessageParcel对象。 |
| options | [MessageOption](#messageoption) | 是 | 本次请求的同异步模式，默认同步调用。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：发送成功，false：发送失败。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/XSjXk_DFSuOBqK3XjSh15Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=DDB060F1602AA2DF52ECE0D612F35FFFC9E4336502A219769D7E8D60F4771F86)

在本文档的示例中，通过this.getUIContext().getHostContext()来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
// FA模型需要从@kit.AbilityKit导入featureAbility
// import { featureAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { Want, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let proxy: rpc.IRemoteObject | undefined;
let connect: common.ConnectOptions = {
  onConnect: (elementName, remoteProxy) => {
    hilog.info(0x0000, 'testTag', 'js onConnect called');
    proxy = remoteProxy;
  },
  onDisconnect: (elementName) => {
    hilog.info(0x0000, 'testTag', 'onDisconnect');
  },
  onFailed: () => {
    hilog.info(0x0000, 'testTag', 'onFailed');
  }
};
let want: Want = {
  // 获取服务端包名和ability名称
  bundleName: "com.ohos.server",
  abilityName: "com.ohos.server.EntryAbility",
};

// FA模型使用此方法连接服务
// FA.connectAbility(want,connect);

// 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
// 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
let connectionId = context.connectServiceExtensionAbility(want, connect);
```

上述onConnect回调函数中的proxy对象需要等ability异步连接成功后才会被赋值，然后才可调用proxy对象的sendRequest接口方法发送消息

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let option = new rpc.MessageOption();
  let data = rpc.MessageParcel.create();
  let reply = rpc.MessageParcel.create();
  data.writeInt(1);
  data.writeString("hello");
  if (proxy != undefined) {
    let ret: boolean = proxy.sendRequest(1, data, reply, option);
    if (ret) {
      hilog.info(0x0000, 'testTag', 'sendRequest got result');
      let msg = reply.readString();
      hilog.info(0x0000, 'testTag', 'reply msg: ' + msg);
    } else {
      hilog.error(0x0000, 'testTag', 'sendRequest failed');
    }
    hilog.info(0x0000, 'testTag', 'sendRequest ends, reclaim parcel');
    data.reclaim();
    reply.reclaim();
  }
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error: ' + error);
}
```

#### \[h2\]sendMessageRequest9+

sendMessageRequest(code: number, data: MessageSequence, reply: MessageSequence, options: MessageOption): Promise<RequestResult>

以同步或异步方式向对端进程发送MessageSequence消息。如果为选项设置了异步模式，则期约立即兑现，reply报文里没有内容，具体回复需要在业务侧的回调中获取。如果为选项设置了同步模式，则期约将在sendMessageRequest返回时兑现，回复内容在reply报文里。使用Promise异步回调。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| code | number | 是 | 本次请求调用的消息码\[1-16777215\]，由通信双方确定。如果接口由IDL工具生成，则消息代码由IDL自动生成。 |
| data | [MessageSequence](#messagesequence9) | 是 | 保存待发送数据的MessageSequence对象。 |
| reply | [MessageSequence](#messagesequence9) | 是 | 接收应答数据的MessageSequence对象。 |
| options | [MessageOption](#messageoption) | 是 | 本次请求的同异步模式，默认同步调用。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[RequestResult](#requestresult9)\> | Promise对象，返回一个期约，兑现值是requestResult实例。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.Failed to obtain the passed object instance.

 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/yYLyWkWPRT6AXAJ5vhI1oA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=71FABEB894C3B001248BF098DE9F77ADDCB582B68979B87D2DE3B5BA1797BDFC)

在本文档的示例中，通过this.getUIContext().getHostContext()来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
// FA模型需要从@kit.AbilityKit导入featureAbility
// import { featureAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { Want, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let proxy: rpc.IRemoteObject | undefined;
let connect: common.ConnectOptions = {
  onConnect: (elementName, remoteProxy) => {
    hilog.info(0x0000, 'testTag', 'js onConnect called');
    proxy = remoteProxy;
  },
  onDisconnect: (elementName) => {
    hilog.info(0x0000, 'testTag', 'onDisconnect');
  },
  onFailed: () => {
    hilog.info(0x0000, 'testTag', 'onFailed');
  }
};
let want: Want = {
  // 获取服务端包名和ability名称
  bundleName: "com.ohos.server",
  abilityName: "com.ohos.server.EntryAbility",
};

// FA模型使用此方法连接服务
// FA.connectAbility(want,connect);

// 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
// 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
let connectionId = context.connectServiceExtensionAbility(want, connect);
```

上述onConnect回调函数中的proxy对象需要等ability异步连接成功后才会被赋值，然后才可调用proxy对象的sendMessageRequest接口方法发送消息

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let option = new rpc.MessageOption();
  let data = rpc.MessageSequence.create();
  let reply = rpc.MessageSequence.create();
  data.writeInt(1);
  data.writeString("hello");
  if (proxy != undefined) {
    proxy.sendMessageRequest(1, data, reply, option)
    .then((result: rpc.RequestResult) => {
      if (result.errCode === 0) {
        hilog.info(0x0000, 'testTag', 'sendMessageRequest got result');
        let num = result.reply.readInt();
        let msg = result.reply.readString();
        hilog.info(0x0000, 'testTag', 'reply num: ' + num);
        hilog.info(0x0000, 'testTag', 'reply msg: ' + msg);
      } else {
        hilog.error(0x0000, 'testTag', 'sendMessageRequest failed, errCode: ' + result.errCode);
      }
    }).catch((e: Error) => {
      hilog.error(0x0000, 'testTag', 'sendMessageRequest failed, error: ' + JSON.stringify(e));
    }).finally (() => {
      hilog.info(0x0000, 'testTag', 'sendMessageRequest ends, reclaim parcel');
      data.reclaim();
      reply.reclaim();
    });
  }
} catch (error) {
  hilog.error(0x0000, 'testTag', 'sendMessageRequest failed, error: ' + error);
}
```

#### \[h2\]sendRequest(deprecated)

sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): Promise<SendRequestResult>

以同步或异步方式向对端进程发送MessageParcel消息。如果为选项设置了异步模式，则期约立即兑现，reply报文里没有内容，具体回复需要在业务侧的回调中获取。如果为选项设置了同步模式，则期约将在sendRequest返回时兑现，回复内容在reply报文里。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/m2RRF5fkRjO6cHp7PqExNw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=9523448140FEFE73E99C47192803B0865F2D413A01724892BA9A19D25CC83472)

从API version 8 开始支持，API version 9 开始废弃，建议使用[sendMessageRequest](#sendmessagerequest9-2)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| code | number | 是 | 本次请求调用的消息码\[1-16777215\]，由通信双方确定。如果接口由IDL工具生成，则消息代码由IDL自动生成。 |
| data | [MessageParcel](#messageparceldeprecated) | 是 | 保存待发送数据的MessageParcel对象。 |
| reply | [MessageParcel](#messageparceldeprecated) | 是 | 接收应答数据的MessageParcel对象。 |
| options | [MessageOption](#messageoption) | 是 | 本次请求的同异步模式，默认同步调用。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[SendRequestResult](#sendrequestresultdeprecated)\> | Promise对象，返回一个期约，兑现值是sendRequestResult实例。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/v-_WzL8GS6yZSdqF_DeDsQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=7131A3A4F5E367E69671C54F27BF3139CD161D9626DBEE803D98B4B0B7582DF0)

在本文档的示例中，通过this.getUIContext().getHostContext()来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
// FA模型需要从@kit.AbilityKit导入featureAbility
// import { featureAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { Want, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let proxy: rpc.IRemoteObject | undefined;
let connect: common.ConnectOptions = {
  onConnect: (elementName, remoteProxy) => {
    hilog.info(0x0000, 'testTag', 'js onConnect called');
    proxy = remoteProxy;
  },
  onDisconnect: (elementName) => {
    hilog.info(0x0000, 'testTag', 'onDisconnect');
  },
  onFailed: () => {
    hilog.info(0x0000, 'testTag', 'onFailed');
  }
};
let want: Want = {
  // 获取服务端包名和ability名称
  bundleName: "com.ohos.server",
  abilityName: "com.ohos.server.EntryAbility",
};

// FA模型使用此方法连接服务
// FA.connectAbility(want,connect);

// 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
// 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
let connectionId = context.connectServiceExtensionAbility(want, connect);
```

上述onConnect回调函数中的proxy对象需要等ability异步连接成功后才会被赋值，然后才可调用proxy对象的sendRequest接口方法发送消息

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let option = new rpc.MessageOption();
  let data = rpc.MessageParcel.create();
  let reply = rpc.MessageParcel.create();
  data.writeInt(1);
  data.writeString("hello");
  if (proxy != undefined) {
    let a = proxy.sendRequest(1, data, reply, option) as Object;
    let b = a as Promise<rpc.SendRequestResult>;
    b.then((result: rpc.SendRequestResult) => {
      if (result.errCode === 0) {
        hilog.info(0x0000, 'testTag', 'sendRequest got result');
        let num = result.reply.readInt();
        let msg = result.reply.readString();
        hilog.info(0x0000, 'testTag', 'reply num: ' + num);
        hilog.info(0x0000, 'testTag', 'reply msg: ' + msg);
      } else {
        hilog.error(0x0000, 'testTag', 'sendRequest failed, errCode: ' + result.errCode);
      }
    }).catch((e: Error) => {
      hilog.error(0x0000, 'testTag', 'sendRequest failed, error: ' + JSON.stringify(e));
    }).finally (() => {
      hilog.info(0x0000, 'testTag', 'sendRequest ends, reclaim parcel');
      data.reclaim();
      reply.reclaim();
    });
  }
} catch (error) {
  hilog.error(0x0000, 'testTag', 'sendRequest failed, error: ' + error);
}
```

#### \[h2\]sendMessageRequest9+

sendMessageRequest(code: number, data: MessageSequence, reply: MessageSequence, options: MessageOption, callback: AsyncCallback<RequestResult>): void

以同步或异步方式向对端进程发送MessageSequence消息。如果为选项设置了异步模式，则立即收到回调，reply报文里没有内容，具体回复需要在业务侧的回调中获取。如果为选项设置了同步模式，则将在sendMessageRequest返回后的某个时机执行回调，回复内容在RequestResult的reply报文里。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| code | number | 是 | 本次请求调用的消息码\[1-16777215\]，由通信双方确定。如果接口由IDL工具生成，则消息代码由IDL自动生成。 |
| data | [MessageSequence](#messagesequence9) | 是 | 保存待发送数据的MessageSequence对象。 |
| reply | [MessageSequence](#messagesequence9) | 是 | 接收应答数据的MessageSequence对象。 |
| options | [MessageOption](#messageoption) | 是 | 本次请求的同异步模式，默认同步调用。 |
| callback | AsyncCallback<[RequestResult](#requestresult9)\> | 是 | 回调函数。当消息发送成功时，可从RequestResult中读取服务端返回的数据。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.Failed to obtain the passed object instance.

 |

#### \[h2\]sendRequest(deprecated)

sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption, callback: AsyncCallback<SendRequestResult>): void

以同步或异步方式向对端进程发送MessageParcel消息。如果为选项设置了异步模式，则立即收到回调，reply报文里没有内容，具体回复需要在业务侧的回调中获取。如果为选项设置了同步模式，则将在sendRequest返回时收到回调，回复内容在reply报文里。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/1_LGei2kRxO6Eaebm5ip3w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=74929FFF014C7844AAA81333C2F117508F159EB983266E85B2BF4769D1DE9AD7)

从API version 8 开始支持，API version 9 开始废弃，建议使用[sendMessageRequest](#sendmessagerequest9-3)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| code | number | 是 | 本次请求调用的消息码\[1-16777215\]，由通信双方确定。如果接口由IDL工具生成，则消息代码由IDL自动生成。 |
| data | [MessageParcel](#messageparceldeprecated) | 是 | 保存待发送数据的MessageParcel对象。 |
| reply | [MessageParcel](#messageparceldeprecated) | 是 | 接收应答数据的MessageParcel对象。 |
| options | [MessageOption](#messageoption) | 是 | 本次请求的同异步模式，默认同步调用。 |
| callback | AsyncCallback<[SendRequestResult](#sendrequestresultdeprecated)\> | 是 | 接收发送结果的回调。 |

#### \[h2\]getLocalInterface9+

getLocalInterface(interfaceDes: string): IRemoteBroker

查询并获取当前接口描述符对应的本地接口对象。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| interfaceDes | string | 是 | 需要查询的接口描述符。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [IRemoteBroker](#iremotebroker) | 默认返回Null，标识该接口是一个代理侧接口。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | check param failed |
| 1900006 | Operation allowed only for the remote object. |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/xpVOsYxYQNqu8A6iMzgy1A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=522D42687305BB06780601566A4C6F9F20C57FC2586A682ACE6D02F2DB355455)

在本文档的示例中，通过this.getUIContext().getHostContext()来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
// FA模型需要从@kit.AbilityKit导入featureAbility
// import { featureAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { Want, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let proxy: rpc.IRemoteObject | undefined;
let connect: common.ConnectOptions = {
  onConnect: (elementName, remoteProxy) => {
    hilog.info(0x0000, 'testTag', 'js onConnect called');
    proxy = remoteProxy;
  },
  onDisconnect: (elementName) => {
    hilog.info(0x0000, 'testTag', 'onDisconnect');
  },
  onFailed: () => {
    hilog.info(0x0000, 'testTag', 'onFailed');
  }
};
let want: Want = {
  // 获取服务端包名和ability名称
  bundleName: "com.ohos.server",
  abilityName: "com.ohos.server.EntryAbility",
};

// FA模型使用此方法连接服务
// FA.connectAbility(want,connect);

// 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
// 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
let connectionId = context.connectServiceExtensionAbility(want, connect);
```

上述onConnect回调函数中的proxy对象需要等ability异步连接成功后才会被赋值，然后才可调用proxy对象的getLocalInterface接口方法查询接口对象

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

if (proxy != undefined) {
  try {
    let broker: rpc.IRemoteBroker = proxy.getLocalInterface("testObject");
    hilog.info(0x0000, 'testTag', 'getLocalInterface is ' + broker);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    hilog.error(0x0000, 'testTag', 'rpc get local interface fail, errorCode ' + e.code);
    hilog.error(0x0000, 'testTag', 'rpc get local interface fail, errorMessage ' + e.message);
  }
}
```

#### \[h2\]queryLocalInterface(deprecated)

queryLocalInterface(interface: string): IRemoteBroker

查询并获取当前接口描述符对应的本地接口对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/hkuyRp7DTniCgmMMa7Jwfg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=9E63477FA1F272520F15DF519D5E37916D5ED94AFB38250F8D031CA3583C5A8C)

从API version 7 开始支持，API version 9 开始废弃，建议使用[getLocalInterface](#getlocalinterface9-1)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| interface | string | 是 | 需要查询的接口描述符。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [IRemoteBroker](#iremotebroker) | 默认返回Null，标识该接口是一个代理侧接口。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/D1-bhr9WRPS3z5nY72LuFw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=9B399D00627345B59FD89127BC58B191F0DC1E7EACC3F2AACEDA24F70F870A81)

在本文档的示例中，通过this.getUIContext().getHostContext()来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
// FA模型需要从@kit.AbilityKit导入featureAbility
// import { featureAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { Want, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let proxy: rpc.IRemoteObject | undefined;
let connect: common.ConnectOptions = {
  onConnect: (elementName, remoteProxy) => {
    hilog.info(0x0000, 'testTag', 'js onConnect called');
    proxy = remoteProxy;
  },
  onDisconnect: (elementName) => {
    hilog.info(0x0000, 'testTag', 'onDisconnect');
  },
  onFailed: () => {
    hilog.info(0x0000, 'testTag', 'onFailed');
  }
};
let want: Want = {
  // 获取服务端包名和ability名称
  bundleName: "com.ohos.server",
  abilityName: "com.ohos.server.EntryAbility",
};

// FA模型使用此方法连接服务
// FA.connectAbility(want,connect);

// 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
// 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
let connectionId = context.connectServiceExtensionAbility(want, connect);
```

上述onConnect回调函数中的proxy对象需要等ability异步连接成功后才会被赋值，然后才可调用proxy对象的queryLocalInterface接口获取接口对象

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

if (proxy != undefined) {
  let broker: rpc.IRemoteBroker = proxy.queryLocalInterface("testObject");
  hilog.info(0x0000, 'testTag', 'queryLocalInterface is ' + broker);
}
```

#### \[h2\]registerDeathRecipient9+

registerDeathRecipient(recipient: DeathRecipient, flags: number): void

注册用于接收远程对象死亡通知的回调。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| recipient | [DeathRecipient](#deathrecipient) | 是 | 要注册的回调。 |
| flags | number | 是 | 死亡通知标志。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.The callback used to receive remote object death notifications is empty.

 |
| 1900008 | The proxy or remote object is invalid. |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/A9toMdtuTO-t88nU66BfHA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=12BD897693694F652B2D41C435A08F177404D660F4D7436B00683879A12458A5)

在本文档的示例中，通过this.getUIContext().getHostContext()来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
// FA模型需要从@kit.AbilityKit导入featureAbility
// import { featureAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { Want, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let proxy: rpc.IRemoteObject | undefined;
let connect: common.ConnectOptions = {
  onConnect: (elementName, remoteProxy) => {
    hilog.info(0x0000, 'testTag', 'js onConnect called');
    proxy = remoteProxy;
  },
  onDisconnect: (elementName) => {
    hilog.info(0x0000, 'testTag', 'onDisconnect');
  },
  onFailed: () => {
    hilog.info(0x0000, 'testTag', 'onFailed');
  }
};
let want: Want = {
  // 获取服务端包名和ability名称
  bundleName: "com.ohos.server",
  abilityName: "com.ohos.server.EntryAbility",
};

// FA模型使用此方法连接服务
// FA.connectAbility(want,connect);

// 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
// 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
let connectionId = context.connectServiceExtensionAbility(want, connect);
```

上述onConnect回调函数中的proxy对象需要等ability异步连接成功后才会被赋值，然后才可调用proxy对象的registerDeathRecipient接口注册死亡回调

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

class MyDeathRecipient implements rpc.DeathRecipient {
  onRemoteDied() {
    hilog.info(0x0000, 'testTag', 'server died');
  }
}
if (proxy != undefined) {
  try {
    let deathRecipient = new MyDeathRecipient();
    proxy.registerDeathRecipient(deathRecipient, 0);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    hilog.error(0x0000, 'testTag', 'proxy register deathRecipient fail, errorCode ' + e.code);
    hilog.error(0x0000, 'testTag', 'proxy register deathRecipient fail, errorMessage ' + e.message);
  }
}
```

#### \[h2\]addDeathRecipient(deprecated)

addDeathRecipient(recipient: DeathRecipient, flags: number): boolean

注册用于接收远程对象死亡通知的回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/0IIgRqyzSEWO76NC4ppzig/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=02170A89B1C8F629633A32520F9282AEC567BC99911E81585C4D163D766B32B1)

从API version 7 开始支持，API version 9 开始废弃，建议使用[registerDeathRecipient](#registerdeathrecipient9-1)类替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| recipient | [DeathRecipient](#deathrecipient) | 是 | 收件人表示要注册的回调。 |
| flags | number | 是 | 死亡通知标志。保留参数。设置为0。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：回调注册成功，false：回调注册失败。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/LGCzr8uNRY6vmOSxN054Ig/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=ACF0E4FD842AB7BF70EDC2B678F1ED26D0E7A521A87A388266AD336D1E325803)

在本文档的示例中，通过this.getUIContext().getHostContext()来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
// FA模型需要从@kit.AbilityKit导入featureAbility
// import { featureAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { Want, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let proxy: rpc.IRemoteObject | undefined;
let connect: common.ConnectOptions = {
  onConnect: (elementName, remoteProxy) => {
    hilog.info(0x0000, 'testTag', 'js onConnect called');
    proxy = remoteProxy;
  },
  onDisconnect: (elementName) => {
    hilog.info(0x0000, 'testTag', 'onDisconnect');
  },
  onFailed: () => {
    hilog.info(0x0000, 'testTag', 'onFailed');
  }
};
let want: Want = {
  // 获取服务端包名和ability名称
  bundleName: "com.ohos.server",
  abilityName: "com.ohos.server.EntryAbility",
};

// FA模型使用此方法连接服务
// FA.connectAbility(want,connect);

// 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
// 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
let connectionId = context.connectServiceExtensionAbility(want, connect);
```

上述onConnect回调函数中的proxy对象需要等ability异步连接成功后才会被赋值，然后才可调用proxy对象的addDeathRecipient接口方法新增死亡回调

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MyDeathRecipient implements rpc.DeathRecipient {
  onRemoteDied() {
    hilog.info(0x0000, 'testTag', 'server died');
  }
}
if (proxy != undefined) {
  let deathRecipient = new MyDeathRecipient();
  proxy.addDeathRecipient(deathRecipient, 0);
}
```

#### \[h2\]unregisterDeathRecipient9+

unregisterDeathRecipient(recipient: DeathRecipient, flags: number): void

注销用于接收远程对象死亡通知的回调。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| recipient | [DeathRecipient](#deathrecipient) | 是 | 要注销的回调。 |
| flags | number | 是 | 死亡通知标志。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.The callback used to receive remote object death notifications is empty.

 |
| 1900008 | The proxy or remote object is invalid. |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/fjF9QQMtQQyrjWT3FM-C2g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=58EF8EBC466A3A5E049E18A34661890A63E5F4A24B2B74F58F49B4D70DFCD4D2)

在本文档的示例中，通过this.getUIContext().getHostContext()来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
// FA模型需要从@kit.AbilityKit导入featureAbility
// import { featureAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { Want, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let proxy: rpc.IRemoteObject | undefined;
let connect: common.ConnectOptions = {
  onConnect: (elementName, remoteProxy) => {
    hilog.info(0x0000, 'testTag', 'js onConnect called');
    proxy = remoteProxy;
  },
  onDisconnect: (elementName) => {
    hilog.info(0x0000, 'testTag', 'onDisconnect');
  },
  onFailed: () => {
    hilog.info(0x0000, 'testTag', 'onFailed');
  }
};
let want: Want = {
  // 获取服务端包名和ability名称
  bundleName: "com.ohos.server",
  abilityName: "com.ohos.server.EntryAbility",
};

// FA模型使用此方法连接服务
// FA.connectAbility(want,connect);

// 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
// 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
let connectionId = context.connectServiceExtensionAbility(want, connect);
```

上述onConnect回调函数中的proxy对象需要等ability异步连接成功后才会被赋值，然后才可调用proxy对象的unregisterDeathRecipient接口方法注销死亡回调

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

class MyDeathRecipient implements rpc.DeathRecipient {
  onRemoteDied() {
    hilog.info(0x0000, 'testTag', 'server died');
  }
}
if (proxy != undefined) {
  try {
    let deathRecipient = new MyDeathRecipient();
    proxy.registerDeathRecipient(deathRecipient, 0);
    proxy.unregisterDeathRecipient(deathRecipient, 0);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    hilog.error(0x0000, 'testTag', 'proxy unregister deathRecipient fail, errorCode ' + e.code);
    hilog.error(0x0000, 'testTag', 'proxy unregister deathRecipient fail, errorMessage ' + e.message);
  }
}
```

#### \[h2\]removeDeathRecipient(deprecated)

removeDeathRecipient(recipient: DeathRecipient, flags: number): boolean

注销用于接收远程对象死亡通知的回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/g8Wof5DNSamFfg4inDvbpg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=EAE27BC804DE8562D690E2461ECF05255E77048A785B12367CD6CD411C6649A4)

从API version 7 开始支持，API version 9 开始废弃，建议使用[unregisterDeathRecipient](#unregisterdeathrecipient9-1)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| recipient | [DeathRecipient](#deathrecipient) | 是 | 要注销的死亡回调。 |
| flags | number | 是 | 死亡通知标志。保留参数。设置为0。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：回调注销成功，false：回调注销失败。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/gnvvn2jOQcm2q0QJh7v4tQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=23EE83AD5C68136A27DAD36D5F4DCF202A162E8CCCC78FAE5FA99F9161A1A81D)

在本文档的示例中，通过this.getUIContext().getHostContext()来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
// FA模型需要从@kit.AbilityKit导入featureAbility
// import { featureAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { Want, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let proxy: rpc.IRemoteObject | undefined;
let connect: common.ConnectOptions = {
  onConnect: (elementName, remoteProxy) => {
    hilog.info(0x0000, 'testTag', 'js onConnect called');
    proxy = remoteProxy;
  },
  onDisconnect: (elementName) => {
    hilog.info(0x0000, 'testTag', 'onDisconnect');
  },
  onFailed: () => {
    hilog.info(0x0000, 'testTag', 'onFailed');
  }
};
let want: Want = {
  // 获取服务端包名和ability名称
  bundleName: "com.ohos.server",
  abilityName: "com.ohos.server.EntryAbility",
};

// FA模型使用此方法连接服务
// FA.connectAbility(want,connect);

// 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
// 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
let connectionId = context.connectServiceExtensionAbility(want, connect);
```

上述onConnect回调函数中的proxy对象需要等ability异步连接成功后才会被赋值，然后才可调用proxy对象的removeDeathRecipient接口方法去注册死亡回调

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MyDeathRecipient implements rpc.DeathRecipient {
  onRemoteDied() {
    hilog.info(0x0000, 'testTag', 'server died');
  }
}
if (proxy != undefined) {
  let deathRecipient = new MyDeathRecipient();
  proxy.addDeathRecipient(deathRecipient, 0);
  proxy.removeDeathRecipient(deathRecipient, 0);
}
```

#### \[h2\]getDescriptor9+

getDescriptor(): string

获取对象的接口描述符，接口描述符为字符串。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 返回接口描述符。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 1900007 | communication failed. |
| 1900008 | The proxy or remote object is invalid. |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/ADzMQI2KQM-DNA-sm8OW-Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=7F68CF19F081C0B46548BAFF9F73863FFE51D5C72B81F0131A920A2A58177582)

在本文档的示例中，通过this.getUIContext().getHostContext()来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
// FA模型需要从@kit.AbilityKit导入featureAbility
// import { featureAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { Want, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let proxy: rpc.IRemoteObject | undefined;
let connect: common.ConnectOptions = {
  onConnect: (elementName, remoteProxy) => {
    hilog.info(0x0000, 'testTag', 'js onConnect called');
    proxy = remoteProxy;
  },
  onDisconnect: (elementName) => {
    hilog.info(0x0000, 'testTag', 'onDisconnect');
  },
  onFailed: () => {
    hilog.info(0x0000, 'testTag', 'onFailed');
  }
};
let want: Want = {
  // 获取服务端包名和ability名称
  bundleName: "com.ohos.server",
  abilityName: "com.ohos.server.EntryAbility",
};

// FA模型使用此方法连接服务
// FA.connectAbility(want,connect);

// 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
// 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
let connectionId = context.connectServiceExtensionAbility(want, connect);
```

上述onConnect回调函数中的proxy对象需要等ability异步连接成功后才会被赋值，然后才可调用proxy对象的getDescriptor接口方法获取对象的接口描述符

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

if (proxy != undefined) {
  try {
    let descriptor: string = proxy.getDescriptor();
    hilog.info(0x0000, 'testTag', 'descriptor is ' + descriptor);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    hilog.error(0x0000, 'testTag', 'rpc get interface descriptor fail, errorCode ' + e.code);
    hilog.error(0x0000, 'testTag', 'rpc get interface descriptor fail, errorMessage ' + e.message);
  }
}
```

#### \[h2\]getInterfaceDescriptor(deprecated)

getInterfaceDescriptor(): string

查询当前代理对象接口的描述符。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/ODtHbdc8S4-mfcgrRmIBmw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=EB2C971E20B44CDBEE31AE0CC013994AEBC620A02E23B48C51FFBB793FDC2FBC)

从API version 7 开始支持，API version 9 开始废弃，建议使用[getDescriptor](#getdescriptor9-1)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 当前的接口描述符。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/_JpL2Db2TYyVGVLM9T71yQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=F2A0FAD10363A9424B8493B6BFB6011C130ECC360257E95B546EA3B48F8AE790)

在本文档的示例中，通过this.getUIContext().getHostContext()来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
// FA模型需要从@kit.AbilityKit导入featureAbility
// import { featureAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { Want, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let proxy: rpc.IRemoteObject | undefined;
let connect: common.ConnectOptions = {
  onConnect: (elementName, remoteProxy) => {
    hilog.info(0x0000, 'testTag', 'js onConnect called');
    proxy = remoteProxy;
  },
  onDisconnect: (elementName) => {
    hilog.info(0x0000, 'testTag', 'onDisconnect');
  },
  onFailed: () => {
    hilog.info(0x0000, 'testTag', 'onFailed');
  }
};
let want: Want = {
  // 获取服务端包名和ability名称
  bundleName: "com.ohos.server",
  abilityName: "com.ohos.server.EntryAbility",
};

// FA模型使用此方法连接服务
// FA.connectAbility(want,connect);

// 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
// 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
let connectionId = context.connectServiceExtensionAbility(want, connect);
```

上述onConnect回调函数中的proxy对象需要等ability异步连接成功后才会被赋值，然后才可调用proxy对象的getInterfaceDescriptor接口方法查询当前代理对象接口的描述符

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

if (proxy != undefined) {
  let descriptor: string = proxy.getInterfaceDescriptor();
  hilog.info(0x0000, 'testTag', 'descriptor is ' + descriptor);
}
```

#### \[h2\]isObjectDead

isObjectDead(): boolean

指示对应的RemoteObject是否死亡。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：对应的对象已经死亡，false：对应的对象未死亡。 |

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/jRd8B5sxTA-CiHM2Jh_0dQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=48AA3C44DCDC057C81AC44CDA6464815BE78201B6C038D0B60B2ACB3F65211B0)

在本文档的示例中，通过this.getUIContext().getHostContext()来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ts
// FA模型需要从@kit.AbilityKit导入featureAbility
// import { featureAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { Want, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let proxy: rpc.IRemoteObject | undefined;
let connect: common.ConnectOptions = {
  onConnect: (elementName, remoteProxy) => {
    hilog.info(0x0000, 'testTag', 'js onConnect called');
    proxy = remoteProxy;
  },
  onDisconnect: (elementName) => {
    hilog.info(0x0000, 'testTag', 'onDisconnect');
  },
  onFailed: () => {
    hilog.info(0x0000, 'testTag', 'onFailed');
  }
};
let want: Want = {
  // 获取服务端包名和ability名称
  bundleName: "com.ohos.server",
  abilityName: "com.ohos.server.EntryAbility",
};

// FA模型使用此方法连接服务
// FA.connectAbility(want,connect);

// 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
// 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
let connectionId = context.connectServiceExtensionAbility(want, connect);
```

上述onConnect回调函数中的proxy对象需要等ability异步连接成功后才会被赋值，然后才可调用proxy对象的isObjectDead接口方法判断当前对象是否已经死亡

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

if (proxy != undefined) {
  let isDead: boolean = proxy.isObjectDead();
  hilog.info(0x0000, 'testTag', 'isObjectDead is ' + isDead);
}
```

#### MessageOption

公共消息选项，使用指定的标志类型，构造指定的MessageOption对象。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

#### \[h2\]属性

\*\*系统能力：\*\*以下各项对应的系统能力均为SystemCapability.Communication.IPC.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| TF\_SYNC | number | 是 | 否 | 同步调用标识。 |
| TF\_ASYNC | number | 是 | 否 | 异步调用标识。 |
| TF\_ACCEPT\_FDS | number | 是 | 否 | 指示sendMessageRequest9+接口可以传递文件描述符。 |
| TF\_WAIT\_TIME | number | 是 | 否 | RPC等待时间(单位/秒)，IPC场景下无效。默认等待为8秒（不建议修改等待时间）。 |

#### \[h2\]constructor9+

constructor(async?: boolean)

MessageOption构造函数。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| async | boolean | 否 | true：表示异步调用标志，false：表示同步调用标志。默认同步调用。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';

class TestRemoteObject extends rpc.MessageOption {
  constructor(async: boolean) {
    super(async);
  }
}
```

#### \[h2\]constructor

constructor(syncFlags?: number, waitTime?: number)

MessageOption构造函数。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| syncFlags | number | 否 | 同步调用或异步调用标志，同步调用标志：0；异步调用标志：1。默认同步调用。 |
| waitTime | number | 否 | 调用rpc最长等待时间。默认TF\_WAIT\_TIME。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';

class TestRemoteObject extends rpc.MessageOption {
  constructor(syncFlags?: number,waitTime?: number) {
    super(syncFlags,waitTime);
  }
}
```

#### \[h2\]isAsync9+

isAsync(): boolean

获取[sendMessageRequest](#sendmessagerequest9-2)调用中确定同步或是异步的标志。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：异步调用成功，false：同步调用成功。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let option = new rpc.MessageOption();
  let result = option.isAsync();
} catch (error) {
  hilog.info(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]setAsync9+

setAsync(isAsync: boolean): void

设置[sendMessageRequest](#sendmessagerequest9-2)调用中确定同步或是异步的标志。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| isAsync | boolean | 是 | true：表示异步调用标志，false：表示同步调用标志。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let option = new rpc.MessageOption();
  option.setAsync(true);
} catch (error) {
  hilog.info(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]getFlags

getFlags(): number

获取同步调用或异步调用标志。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 调用成功返回同步调用或异步调用标志。同步调用标志：0，异步调用标志：1。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let option = new rpc.MessageOption();
  hilog.info(0x0000, 'testTag', 'create object successfully');
  let flag = option.getFlags();
  hilog.info(0x0000, 'testTag', 'run getFlags success, flag is ' + flag);
  option.setFlags(rpc.MessageOption.TF_ASYNC);
  hilog.info(0x0000, 'testTag', 'run setFlags success');
  let flag2 = option.getFlags();
  hilog.info(0x0000, 'testTag', 'run getFlags success, flag2 is ' + flag2);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]setFlags

setFlags(flags: number): void

设置同步调用或异步调用标志。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| flags | number | 是 | 同步调用或异步调用标志。同步调用标志：0；异步调用标志：1 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let option = new rpc.MessageOption();
  option.setFlags(rpc.MessageOption.TF_ASYNC);
  hilog.info(0x0000, 'testTag', 'run setFlags success');
  let flag = option.getFlags();
  hilog.info(0x0000, 'testTag', 'run getFlags success, flag is ' + flag);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]getWaitTime

getWaitTime(): number

获取rpc调用的最长等待时间。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | rpc最长等待时间。默认TF\_WAIT\_TIME。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let option = new rpc.MessageOption();
  let time = option.getWaitTime();
  hilog.info(0x0000, 'testTag', 'run getWaitTime success, time is ' + time);
  option.setWaitTime(16);
  let time2 = option.getWaitTime();
  hilog.info(0x0000, 'testTag', 'run getWaitTime success, time is ' + time2);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]setWaitTime

setWaitTime(waitTime: number): void

设置rpc调用最长等待时间。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| waitTime | number | 是 | rpc调用最长等待时间，上限为3000秒。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let option = new rpc.MessageOption();
  option.setWaitTime(16);
  let time = option.getWaitTime();
  hilog.info(0x0000, 'testTag', 'run getWaitTime success, time is ' + time);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### IPCSkeleton

用于获取IPC上下文信息，包括获取UID和PID、获取本端和对端设备ID、检查接口调用是否在同一设备上。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

#### \[h2\]getContextObject

static getContextObject(): IRemoteObject

静态方法，获取系统能力的管理者。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [IRemoteObject](#iremoteobject) | 返回系统能力管理者。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let samgr = rpc.IPCSkeleton.getContextObject();
  hilog.info(0x0000, 'testTag', 'RpcServer: getContextObject result: ' + samgr);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]getCallingPid

static getCallingPid(): number

静态方法，获取调用者的PID。此方法由[RemoteObject](#remoteobject)对象在IPC上下文环境（[onRemoteMessageRequest](#onremotemessagerequest9)）中调用，不在则返回本进程的PID。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回调用者的PID。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class Stub extends rpc.RemoteObject {
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    try {
      let callerPid = rpc.IPCSkeleton.getCallingPid();
      hilog.info(0x0000, 'testTag', 'RpcServer: getCallingPid result: ' + callerPid);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'error ' + error);
    }
    return true;
  }
}
```

#### \[h2\]getCallingUid

static getCallingUid(): number

静态方法，获取调用者的UID。此方法由[RemoteObject](#remoteobject)对象在IPC上下文环境（[onRemoteMessageRequest](#onremotemessagerequest9)）中调用，不在则返回本进程的UID。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回调用者的UID。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class Stub extends rpc.RemoteObject {
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    try {
      let callerUid = rpc.IPCSkeleton.getCallingUid();
      hilog.info(0x0000, 'testTag', 'RpcServer: getCallingUid result: ' + callerUid);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'error ' + error);
    }
    return true;
  }
}
```

#### \[h2\]getCallingTokenId8+

static getCallingTokenId(): number

静态方法，获取调用者的TokenId，用于被调用方对调用方的身份校验。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回调用者的TokenId。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class Stub extends rpc.RemoteObject {
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    try {
      let callerTokenId = rpc.IPCSkeleton.getCallingTokenId();
      hilog.info(0x0000, 'testTag', 'RpcServer: getCallingTokenId result: ' + callerTokenId);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'error ' + error);
    }
    return true;
  }
}
```

#### \[h2\]getCallingDeviceID

static getCallingDeviceID(): string

静态方法，获取调用者进程所在的设备ID。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 返回调用者进程所在的设备ID。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class Stub extends rpc.RemoteObject {
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    try {
      let callerDeviceID = rpc.IPCSkeleton.getCallingDeviceID();
      hilog.info(0x0000, 'testTag', 'RpcServer: callerDeviceID is ' + callerDeviceID);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'error ' + error);
    }
    return true;
  }
}
```

#### \[h2\]getLocalDeviceID

static getLocalDeviceID(): string

静态方法，获取本端设备ID。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 返回本地设备的ID。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class Stub extends rpc.RemoteObject {
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    try {
      let localDeviceID = rpc.IPCSkeleton.getLocalDeviceID();
      hilog.info(0x0000, 'testTag', 'RpcServer: localDeviceID is ' + localDeviceID);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'error ' + error);
    }
    return true;
  }
}
```

#### \[h2\]isLocalCalling

static isLocalCalling(): boolean

静态方法，检查当前通信对端是否是本设备的进程。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：调用在同一台设备，false：调用未在同一台设备。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class Stub extends rpc.RemoteObject {
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    try {
      let isLocalCalling = rpc.IPCSkeleton.isLocalCalling();
      hilog.info(0x0000, 'testTag', 'RpcServer: isLocalCalling is ' + isLocalCalling);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'error ' + error);
    }
    return true;
  }
}
```

#### \[h2\]flushCmdBuffer9+

static flushCmdBuffer(object: IRemoteObject): void

静态方法，将所有挂起的命令从指定的RemoteProxy刷新到相应的RemoteObject。建议在任何时间执行敏感操作之前调用此方法。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| object | [IRemoteObject](#iremoteobject) | 是 | 指定的RemoteProxy。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    // 根据业务实际逻辑，进行相应处理
    return true;
  }
}
try {
  let remoteObject = new TestRemoteObject("aaa");
  rpc.IPCSkeleton.flushCmdBuffer(remoteObject);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'proxy flushCmdBuffer fail, errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'proxy flushCmdBuffer fail, errorMessage ' + e.message);
}
```

#### \[h2\]flushCommands(deprecated)

static flushCommands(object: IRemoteObject): number

静态方法，将所有挂起的命令从指定的RemoteProxy刷新到相应的RemoteObject。建议在任何时间执行敏感操作之前调用此方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/2fhGSFjRRs-vR7rKGjG1YQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=C2B5FA7F0BE7A702E092E7C79E798BC0330011FC8C970AE4CD97F7B0535FEB6B)

从API version 7 开始支持，API version 9 开始废弃，建议使用[flushCmdBuffer](#flushcmdbuffer9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| object | [IRemoteObject](#iremoteobject) | 是 | 指定的RemoteProxy。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 如果操作成功，返回0；如果输入对象为空或RemoteObject，或者操作失败，返回错误代码。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    // 根据业务实际逻辑，进行相应处理
    return true;
  }
}
try {
  let remoteObject = new TestRemoteObject("aaa");
  let ret = rpc.IPCSkeleton.flushCommands(remoteObject);
  hilog.info(0x0000, 'testTag', 'RpcServer: flushCommands result: ' + ret);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'proxy flushCmdBuffer fail, errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'proxy flushCmdBuffer fail, errorMessage ' + e.message);
}
```

#### \[h2\]resetCallingIdentity

static resetCallingIdentity(): string

静态方法，将远程用户的UID和PID替换为本地用户的UID和PID。它可以用于身份验证等场景。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 返回包含远程用户的UID和PID的字符串。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class Stub extends rpc.RemoteObject {
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    try {
      let callingIdentity = rpc.IPCSkeleton.resetCallingIdentity();
      hilog.info(0x0000, 'testTag', 'RpcServer: callingIdentity is ' + callingIdentity);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'error ' + error);
    }
    return true;
  }
}
```

#### \[h2\]restoreCallingIdentity9+

static restoreCallingIdentity(identity: string): void

静态方法，将UID和PID恢复为远程用户的UID和PID。它通常在使用resetCallingIdentity后调用，需要resetCallingIdentity返回的远程用户的UID和PID。该接口仅支持在IPC上下文（[onRemoteMessageRequest](#onremotemessagerequest9)）中使用，否则直接返回。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| identity | string | 是 | 标识表示包含远程用户UID和PID的字符串，其长度应小于40960字节。由resetCallingIdentity返回。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.The string length is greater than or equal to 40960 bytes;

4.The number of bytes copied to the buffer is different from the length of the obtained string.

 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class Stub extends rpc.RemoteObject {
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    try {
      let callingIdentity = rpc.IPCSkeleton.resetCallingIdentity();
      hilog.info(0x0000, 'testTag', 'RpcServer: callingIdentity is ' + callingIdentity);
      rpc.IPCSkeleton.restoreCallingIdentity(callingIdentity);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'error ' + error);
    }
    return true;
  }
}
```

#### \[h2\]setCallingIdentity(deprecated)

static setCallingIdentity(identity: string): boolean

静态方法，将UID和PID恢复为远程用户的UID和PID。它通常在使用resetCallingIdentity后调用，需要resetCallingIdentity返回的远程用户的UID和PID。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/_kJrF73sScqHAnQcXcQUUw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=8469C3F246F7DD4F59A3E85B2C821E1D61E78C597027F3B9B82930A88892B799)

从API version 7 开始支持，API version 9 开始废弃，建议使用[restoreCallingIdentity](#restorecallingidentity9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| identity | string | 是 | 标识表示包含远程用户UID和PID的字符串。由resetCallingIdentity返回。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：设置成功，false：设置失败。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class Stub extends rpc.RemoteObject {
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    try {
      let callingIdentity = rpc.IPCSkeleton.resetCallingIdentity();
      hilog.info(0x0000, 'testTag', 'RpcServer: callingIdentity is ' + callingIdentity);
      let ret = rpc.IPCSkeleton.setCallingIdentity(callingIdentity);
      hilog.info(0x0000, 'testTag', 'RpcServer: setCallingIdentity is ' + ret);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'error ' + error);
    }
    return true;
  }
}
```

#### RemoteObject

实现远程对象。服务提供者必须继承此类。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

#### \[h2\]constructor

constructor(descriptor: string)

RemoteObject构造函数。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| descriptor | string | 是 | 接口描述符，其长度应小于40960字节。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
}
```

#### \[h2\]sendRequest(deprecated)

sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): boolean

以同步或异步方式向对端进程发送MessageParcel消息。如果为选项设置了异步模式，则期约立即兑现，reply报文里没有内容，具体回复需要在业务侧的回调中获取。如果为选项设置了同步模式，则期约将在sendRequest返回时兑现，回复内容在reply报文里。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/-LUSxAqiSGmw9MbNCa68Qw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=81C0E42355B05050AC8B2E79393F53BD00746C85BD145940D0A5402C345F9F77)

从API version 7 开始支持，API version 8 开始废弃，建议使用[sendMessageRequest](#sendmessagerequest9-4)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| code | number | 是 | 本次请求调用的消息码\[1-16777215\]，由通信双方确定。如果接口由IDL工具生成，则消息代码由IDL自动生成。 |
| data | [MessageParcel](#messageparceldeprecated) | 是 | 保存待发送数据的MessageParcel对象。 |
| reply | [MessageParcel](#messageparceldeprecated) | 是 | 接收应答数据的MessageParcel对象。 |
| options | [MessageOption](#messageoption) | 是 | 本次请求的同异步模式，默认同步调用。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：发送成功，false：发送失败。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class testRemoteObject extends rpc.RemoteObject {
  onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel,
    option: rpc.MessageOption): boolean {
    // 根据业务实际逻辑，进行相应处理
    return true;
  }
}
try {
  let testRemoteObject = new TestRemoteObject("testObject");
  let option = new rpc.MessageOption();
  let data = rpc.MessageParcel.create();
  let reply = rpc.MessageParcel.create();
  data.writeInt(1);
  data.writeString("hello");
  let ret: boolean = testRemoteObject.sendRequest(1, data, reply, option);
  if (ret) {
    hilog.info(0x0000, 'testTag', 'sendRequest got result');
    let msg = reply.readString();
    hilog.info(0x0000, 'testTag', 'reply msg: ' + msg);
  } else {
    hilog.error(0x0000, 'testTag', 'sendRequest failed');
  }
  hilog.info(0x0000, 'testTag', 'sendRequest ends, reclaim parcel');
  data.reclaim();
  reply.reclaim();
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]sendMessageRequest9+

sendMessageRequest(code: number, data: MessageSequence, reply: MessageSequence, options: MessageOption): Promise<RequestResult>

以同步或异步方式向对端进程发送MessageSequence消息。如果为选项设置了异步模式，则期约立即兑现，reply报文里没有内容，具体回复需要在业务侧的回调中获取。如果为选项设置了同步模式，则期约将在sendMessageRequest返回时兑现，回复内容在reply报文里。使用Promise异步回调。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| code | number | 是 | 本次请求调用的消息码\[1-16777215\]，由通信双方确定。如果接口由IDL工具生成，则消息代码由IDL自动生成。 |
| data | [MessageSequence](#messagesequence9) | 是 | 保存待发送数据的MessageSequence对象。 |
| reply | [MessageSequence](#messagesequence9) | 是 | 接收应答数据的MessageSequence对象。 |
| options | [MessageOption](#messageoption) | 是 | 本次请求的同异步模式，默认同步调用。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[RequestResult](#requestresult9)\> | Promise对象，返回一个期约，兑现值是RequestResult实例。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.Failed to obtain the passed object instance.

 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    // 根据业务实际逻辑，进行相应处理
    return true;
  }
}
try {
  let testRemoteObject = new TestRemoteObject("testObject");
  let option = new rpc.MessageOption();
  let data = rpc.MessageSequence.create();
  let reply = rpc.MessageSequence.create();
  data.writeInt(1);
  data.writeString("hello");
  testRemoteObject.sendMessageRequest(1, data, reply, option)
    .then((result: rpc.RequestResult) => {
      if (result.errCode === 0) {
        hilog.info(0x0000, 'testTag', 'sendMessageRequest got result');
        let num = result.reply.readInt();
        let msg = result.reply.readString();
        hilog.info(0x0000, 'testTag', 'reply num: ' + num);
        hilog.info(0x0000, 'testTag', 'reply msg: ' + msg);
      } else {
        hilog.error(0x0000, 'testTag', 'sendMessageRequest failed, errCode: ' + result.errCode);
      }
    }).catch((e: Error) => {
      hilog.error(0x0000, 'testTag', 'sendMessageRequest failed, error: ' + JSON.stringify(e));
    }).finally (() => {
      hilog.info(0x0000, 'testTag', 'sendMessageRequest ends, reclaim parcel');
      data.reclaim();
      reply.reclaim();
    });
} catch (error) {
  hilog.error(0x0000, 'testTag', 'sendMessageRequest failed, error: ' + error);
}
```

#### \[h2\]sendRequest(deprecated)

sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): Promise<SendRequestResult>

以同步或异步方式向对端进程发送MessageParcel消息。如果为选项设置了异步模式，则期约立即兑现，reply报文里没有内容，具体回复需要在业务侧的回调中获取。如果为选项设置了同步模式，则期约将在sendRequest返回时兑现，回复内容在reply报文里。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/zryt6PSISymkV6C99rha8w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=DAEEE28D652C34775A7C994BD41DBA69A48A7444AECE6E7860A3E3BEC779380D)

从API version 8 开始支持，API version 9 开始废弃，建议使用[sendMessageRequest](#sendmessagerequest9-4)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| code | number | 是 | 本次请求调用的消息码\[1-16777215\]，由通信双方确定。如果接口由IDL工具生成，则消息代码由IDL自动生成。 |
| data | [MessageParcel](#messageparceldeprecated) | 是 | 保存待发送数据的MessageParcel对象。 |
| reply | [MessageParcel](#messageparceldeprecated) | 是 | 接收应答数据的MessageParcel对象。 |
| options | [MessageOption](#messageoption) | 是 | 本次请求的同异步模式，默认同步调用。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[SendRequestResult](#sendrequestresultdeprecated)\> | Promise对象，返回一个期约，兑现值是sendRequestResult实例。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel, option: rpc.MessageOption): boolean {
    // 根据业务实际逻辑，进行相应处理
    return true;
  }
}
try {
  let testRemoteObject = new TestRemoteObject("testObject");
  let option = new rpc.MessageOption();
  let data = rpc.MessageParcel.create();
  let reply = rpc.MessageParcel.create();
  data.writeInt(1);
  data.writeString("hello");
  let a = testRemoteObject.sendRequest(1, data, reply, option) as Object;
  let b = a as Promise<rpc.SendRequestResult>;
  b.then((result: rpc.SendRequestResult) => {
    if (result.errCode === 0) {
      hilog.info(0x0000, 'testTag', 'sendRequest got result');
      let num = result.reply.readInt();
      let msg = result.reply.readString();
      hilog.info(0x0000, 'testTag', 'reply num: ' + num);
      hilog.info(0x0000, 'testTag', 'reply msg: ' + msg);
    } else {
      hilog.error(0x0000, 'testTag', 'sendRequest failed, errCode: ' + result.errCode);
    }
  }).catch((e: Error) => {
    hilog.error(0x0000, 'testTag', 'sendRequest failed, error: ' + JSON.stringify(e));
  }).finally (() => {
    hilog.info(0x0000, 'testTag', 'sendRequest ends, reclaim parcel');
    data.reclaim();
    reply.reclaim();
  });
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error: ' + error);
}
```

#### \[h2\]sendMessageRequest9+

sendMessageRequest(code: number, data: MessageSequence, reply: MessageSequence, options: MessageOption, callback: AsyncCallback<RequestResult>): void

以同步或异步方式向对端进程发送MessageSequence消息。如果为选项设置了异步模式，则立即收到回调，reply报文里没有内容，具体回复需要在业务侧的回调中获取。如果为选项设置了同步模式，则将在sendMessageRequest返回时收到回调，回复内容在reply报文里。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| code | number | 是 | 本次请求调用的消息码\[1-16777215\]，由通信双方确定。如果接口由IDL工具生成，则消息代码由IDL自动生成。 |
| data | [MessageSequence](#messagesequence9) | 是 | 保存待发送数据的MessageSequence对象。 |
| reply | [MessageSequence](#messagesequence9) | 是 | 接收应答数据的MessageSequence对象。 |
| options | [MessageOption](#messageoption) | 是 | 本次请求的同异步模式，默认同步调用。 |
| callback | AsyncCallback<[RequestResult](#requestresult9)\> | 是 | 回调函数。当消息发送成功时，可从RequestResult中读取服务端返回的数据。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.Failed to obtain the passed object instance.

 |

#### \[h2\]sendRequest(deprecated)

sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption, callback: AsyncCallback<SendRequestResult>): void

以同步或异步方式向对端进程发送MessageParcel消息。如果为选项设置了异步模式，则立即收到回调，reply报文里没有内容，具体回复需要在业务侧的回调中获取。如果为选项设置了同步模式，则将在sendRequest返回时收到回调，回复内容在reply报文里。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/jq-a3juJRxOqS6lCO0Zt0g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=3166F48EE0211FF456703CDD1239E587C4EC12A9D53690A2FA72704142D325B3)

从API version 8 开始支持，API version 9 开始废弃，建议使用[sendMessageRequest](#sendmessagerequest9-5)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| code | number | 是 | 本次请求调用的消息码\[1-16777215\]，由通信双方确定。如果接口由IDL工具生成，则消息代码由IDL自动生成。 |
| data | [MessageParcel](#messageparceldeprecated) | 是 | 保存待发送数据的MessageParcel对象。 |
| reply | [MessageParcel](#messageparceldeprecated) | 是 | 接收应答数据的MessageParcel对象。 |
| options | [MessageOption](#messageoption) | 是 | 本次请求的同异步模式，默认同步调用。 |
| callback | AsyncCallback<[SendRequestResult](#sendrequestresultdeprecated)\> | 是 | 接收发送结果的回调。 |

#### \[h2\]onRemoteMessageRequest23+

onRemoteMessageRequest(code: number, data: MessageSequence, reply: MessageSequence, options: MessageOption, callingInfo?: CallingInfo): boolean | Promise<boolean>

sendMessageRequest请求的响应处理函数，服务端在该函数里同步或异步地处理请求，回复结果，该接口可从入参callingInfo中获取IPC上下文信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/mZ4tf9LtTHqFr2WVTcsq4Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=9E4AD2B520F93F6BA881ECA5218B4F00C5B499B4C508DC9E52000F214825577E)

开发者应优先选择重写带有CallingInfo参数的onRemoteMessageRequest方法，其中可以自由实现同步和异步的消息处理。

开发者同时重写onRemoteRequest和onRemoteMessageRequest方法时，仅onRemoteMessageRequest方法生效。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| code | number | 是 | 对端发送的服务请求码。 |
| data | [MessageSequence](#messagesequence9) | 是 | 携带客户端调用参数的MessageSequence对象。 |
| reply | [MessageSequence](#messagesequence9) | 是 | 写入结果的MessageSequence对象。 |
| options | [MessageOption](#messageoption) | 是 | 指示操作是同步还是异步。 |
| callingInfo | [CallingInfo](#callinginfo23) | 否 | 获取IPC上下文信息。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | Promise<boolean> | 
\- 若在onRemoteMessageRequest中同步处理请求，则返回一个布尔值。返回true表示操作成功，返回false表示操作失败。

\- 若在onRemoteMessageRequest中异步处理请求，则返回一个Promise对象。返回true表示操作成功，返回false表示操作失败。

 |

**示例：**

```ts
// 重写onRemoteMessageRequest方法同步处理请求
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }

  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption, callingInfo?: rpc.CallingInfo): boolean | Promise<boolean> {
    if (code === 1) {
      hilog.info(0x0000, 'testTag', 'RpcServer: sync onRemoteMessageRequest is called');
      let pid = callingInfo?.callerPid;
      return true;
    } else {
      hilog.error(0x0000, 'testTag', 'RpcServer: unknown code: ' + code);
      return false;
    }
  }
}
```

**示例：**

```ts
// 重写onRemoteMessageRequest方法异步处理请求
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }

  async onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption, callingInfo?: rpc.CallingInfo): Promise<boolean> {
    if (code === 1) {
      hilog.info(0x0000, 'testTag', 'RpcServer: async onRemoteMessageRequest is called');
      let pid = callingInfo?.callerPid;
    } else {
      hilog.error(0x0000, 'testTag', 'RpcServer: unknown code: ' + code);
      return false;
    }
    await new Promise((resolve: (data: rpc.RequestResult) => void) => {
      setTimeout(resolve, 100);
    })
    return true;
  }
}
```

**示例：**

```ts
// 同时重写onRemoteMessageRequest和onRemoteRequest方法同步处理请求
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }

  onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel, option: rpc.MessageOption): boolean {
     if (code === 1) {
        hilog.info(0x0000, 'testTag', 'RpcServer: sync onRemoteMessageRequest is called');
        return true;
     } else {
        hilog.error(0x0000, 'testTag', 'RpcServer: unknown code: ' + code);
        return false;
     }
  }
    // 同时调用仅会执行onRemoteMessageRequest
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption, callingInfo?: rpc.CallingInfo): boolean | Promise<boolean> {
    if (code === 1) {
      hilog.info(0x0000, 'testTag', 'RpcServer: async onRemoteMessageRequest is called');
      let pid = callingInfo?.callerPid;
    } else {
      hilog.error(0x0000, 'testTag', 'RpcServer: unknown code: ' + code);
      return false;
    }
    return true;
  }
}
```

#### \[h2\]onRemoteMessageRequest9+

onRemoteMessageRequest(code: number, data: MessageSequence, reply: MessageSequence, options: MessageOption): boolean | Promise<boolean>

sendMessageRequest请求的响应处理函数，服务端在该函数里同步或异步地处理请求，回复结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/JShCraPaR3uBPYlNeghleg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=04549C6CE039ECCC9126DD5EAF5014EF1A5DCAC9B7A5AE6A0C1C2E7FC9CD44DC)

开发者应优先选择重写onRemoteMessageRequest方法，其中可以自由实现同步和异步的消息处理。

开发者同时重写onRemoteRequest和onRemoteMessageRequest方法时，仅onRemoteMessageRequest方法生效。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| code | number | 是 | 对端发送的服务请求码。 |
| data | [MessageSequence](#messagesequence9) | 是 | 携带客户端调用参数的MessageSequence对象。 |
| reply | [MessageSequence](#messagesequence9) | 是 | 写入结果的MessageSequence对象。 |
| options | [MessageOption](#messageoption) | 是 | 指示操作是同步还是异步。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | Promise<boolean> | 
\- 若在onRemoteMessageRequest中同步处理请求，则返回一个布尔值。返回true表示操作成功，返回false表示操作失败。

\- 若在onRemoteMessageRequest中异步处理请求，则返回一个Promise对象。返回true表示操作成功，返回false表示操作失败。

 |

**示例：**

```ts
// 重写onRemoteMessageRequest方法同步处理请求
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }

  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean {
    if (code === 1) {
      hilog.info(0x0000, 'testTag', 'RpcServer: sync onRemoteMessageRequest is called');
      return true;
    } else {
      hilog.error(0x0000, 'testTag', 'RpcServer: unknown code: ' + code);
      return false;
    }
  }
}
```

**示例：**

```ts
// 重写onRemoteMessageRequest方法异步处理请求
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }

  async onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): Promise<boolean> {
    if (code === 1) {
      hilog.info(0x0000, 'testTag', 'RpcServer: async onRemoteMessageRequest is called');
    } else {
      hilog.error(0x0000, 'testTag', 'RpcServer: unknown code: ' + code);
      return false;
    }
    await new Promise((resolve: (data: rpc.RequestResult) => void) => {
      setTimeout(resolve, 100);
    })
    return true;
  }
}
```

**示例：**

```ts
// 同时重写onRemoteMessageRequest和onRemoteRequest方法同步处理请求
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }

  onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel, option: rpc.MessageOption): boolean {
     if (code === 1) {
        hilog.info(0x0000, 'testTag', 'RpcServer: sync onRemoteMessageRequest is called');
        return true;
     } else {
        hilog.error(0x0000, 'testTag', 'RpcServer: unknown code: ' + code);
        return false;
     }
  }
    // 同时调用仅会执行onRemoteMessageRequest
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    if (code === 1) {
      hilog.info(0x0000, 'testTag', 'RpcServer: async onRemoteMessageRequest is called');
    } else {
      hilog.error(0x0000, 'testTag', 'RpcServer: unknown code: ' + code);
      return false;
    }
    return true;
  }
}
```

#### \[h2\]onRemoteRequest(deprecated)

onRemoteRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): boolean

sendRequest请求的响应处理函数，服务端在该函数里处理请求，回复结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/ndCjtvOJRbqAfVXX5ekWYA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=8480475C5581A30D4E484E3CC1C621622298F4072780FB713E4A798555021451)

从API version 7 开始支持，API version 9 开始废弃，建议使用[onRemoteMessageRequest](#onremotemessagerequest9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| code | number | 是 | 对端发送的服务请求码。 |
| data | [MessageParcel](#messageparceldeprecated) | 是 | 携带客户端调用参数的MessageParcel对象。 |
| reply | [MessageParcel](#messageparceldeprecated) | 是 | 写入结果的MessageParcel对象。 |
| options | [MessageOption](#messageoption) | 是 | 指示操作是同步还是异步。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：操作成功，false：操作失败。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel, option: rpc.MessageOption): boolean {
    if (code === 1) {
      hilog.info(0x0000, 'testTag', 'RpcServer: onRemoteRequest called');
      return true;
    } else {
      hilog.error(0x0000, 'testTag', 'RpcServer: unknown code: ' + code);
      return false;
    }
  }
}
```

#### \[h2\]getCallingUid

getCallingUid(): number

获取通信对端的进程Uid。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回通信对端的进程Uid。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    // 根据业务实际逻辑，进行相应处理
    return true;
  }
}
try {
  let testRemoteObject = new TestRemoteObject("testObject");
  hilog.info(0x0000, 'testTag', 'RpcServer: getCallingUid: ' + testRemoteObject.getCallingUid());
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error: ' + error);
}
```

#### \[h2\]getCallingPid

getCallingPid(): number

获取通信对端的进程Pid。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回通信对端的进程Pid。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    // 根据业务实际逻辑，进行相应处理
    return true;
  }
}
try {
  let testRemoteObject = new TestRemoteObject("testObject");
  hilog.info(0x0000, 'testTag', 'RpcServer: getCallingPid: ' + testRemoteObject.getCallingPid());
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error: ' + error);
}
```

#### \[h2\]getLocalInterface9+

getLocalInterface(descriptor: string): IRemoteBroker

查询接口描述符的字符串。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| descriptor | string | 是 | 接口描述符的字符串，其长度应小于40960字节。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [IRemoteBroker](#iremotebroker) | 返回绑定到指定接口描述符的IRemoteBroker对象。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.The string length is greater than or equal to 40960 bytes;

4.The number of bytes copied to the buffer is different from the length of the obtained string.

 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    // 根据业务实际逻辑，进行相应处理
    return true;
  }
}
try {
  let testRemoteObject = new TestRemoteObject("testObject");
  testRemoteObject.getLocalInterface("testObject");
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]queryLocalInterface(deprecated)

queryLocalInterface(descriptor: string): IRemoteBroker

查询并获取当前接口描述符对应的远端对象是否已经存在。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/01jQZIW8R_GMAdXMc9c1zg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=C100AC5A86D9B4B689D92B24B5A7A792B31733475BA5026848A140B7D5C1B17E)

从API version 7 开始支持，API version 9 开始废弃，建议使用[getLocalInterface](#getlocalinterface9-2)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| descriptor | string | 是 | 需要查询的接口描述符。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [IRemoteBroker](#iremotebroker) | 如果接口描述符对应的远端对象存在，则返回该远端对象，否则返回Null。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    // 根据业务实际逻辑，进行相应处理
    return true;
  }
}
try {
  let testRemoteObject = new TestRemoteObject("testObject");
  testRemoteObject.queryLocalInterface("testObject");
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error: ' + error);
}
```

#### \[h2\]getDescriptor9+

getDescriptor(): string

获取对象的接口描述符。接口描述符为字符串。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 返回接口描述符。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 1900008 | The proxy or remote object is invalid. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    // 根据业务实际逻辑，进行相应处理
    return true;
  }
}
try {
  let testObject = new TestRemoteObject("ipcTest");
  let descriptor = testObject.getDescriptor();
  hilog.info(0x0000, 'testTag', 'RpcServer: descriptor is ' + descriptor);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]getInterfaceDescriptor(deprecated)

getInterfaceDescriptor(): string

查询接口描述符。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/NUD8_jSkSSaaBivm_CAVFw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=9CC40F0BD5425367F8A47BD5683EC28CFE558DD673B3D809BD98E6C39F04DFC1)

从API version 7 开始支持，API version 9 开始废弃，建议使用[getDescriptor](#getdescriptor9-2)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 返回接口描述符。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    // 根据业务实际逻辑，进行相应处理
    return true;
  }
}

try {
  let testRemoteObject = new TestRemoteObject("testObject");
  let descriptor = testRemoteObject.getInterfaceDescriptor();
  hilog.info(0x0000, 'testTag', 'RpcServer: descriptor is: ' + descriptor);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]modifyLocalInterface9+

modifyLocalInterface(localInterface: IRemoteBroker, descriptor: string): void

此接口用于把接口描述符和IRemoteBroker对象绑定。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| localInterface | [IRemoteBroker](#iremotebroker) | 是 | 将与描述符绑定的IRemoteBroker对象。 |
| descriptor | string | 是 | 用于与IRemoteBroker对象绑定的描述符，其长度应小于40960字节。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.The string length is greater than or equal to 40960 bytes;

4.The number of bytes copied to the buffer is different from the length of the obtained string.

 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

class MyDeathRecipient implements rpc.DeathRecipient {
  onRemoteDied() {
    hilog.info(0x0000, 'testTag', 'server died');
  }
}
class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
    try {
      this.modifyLocalInterface(this, descriptor);
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
      hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
    }
  }
  registerDeathRecipient(recipient: MyDeathRecipient, flags: number) {
    // 方法逻辑需开发者根据业务需要实现
  }
  unregisterDeathRecipient(recipient: MyDeathRecipient, flags: number) {
    // 方法逻辑需开发者根据业务需要实现
  }
}
let testRemoteObject = new TestRemoteObject("testObject");
```

#### \[h2\]attachLocalInterface(deprecated)

attachLocalInterface(localInterface: IRemoteBroker, descriptor: string): void

此接口用于把接口描述符和IRemoteBroker对象绑定。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/lIx6PbDNTBiVZRSH-KJevg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=2610CFB95DC8F88E5C2AA337F4D7CEFEAB53A7E9F75E088D813F7A32D6B8FBB5)

从API version 7 开始支持，API version 9 开始废弃，建议使用[modifyLocalInterface](#modifylocalinterface9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| localInterface | [IRemoteBroker](#iremotebroker) | 是 | 将与描述符绑定的IRemoteBroker对象。 |
| descriptor | string | 是 | 用于与IRemoteBroker对象绑定的描述符。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MyDeathRecipient implements rpc.DeathRecipient {
  onRemoteDied() {
    hilog.info(0x0000, 'testTag', 'server died');
  }
}
class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
    this.attachLocalInterface(this, descriptor);
  }
  addDeathRecipient(recipient: MyDeathRecipient, flags: number): boolean {
    // 方法逻辑需开发者根据业务需要实现
    return true;
  }
  removeDeathRecipient(recipient: MyDeathRecipient, flags: number): boolean {
    // 方法逻辑需开发者根据业务需要实现
    return true;
  }
}
let testRemoteObject = new TestRemoteObject("testObject");
```

#### Ashmem8+

提供与匿名共享内存对象相关的方法，包括创建、关闭、映射和取消映射Ashmem、从Ashmem读取数据和写入数据、获取Ashmem大小、设置Ashmem保护。

共享内存只适用与本设备内跨进程通信。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

#### \[h2\]属性

\*\*系统能力：\*\*以下各项对应的系统能力均为SystemCapability.Communication.IPC.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| PROT\_EXEC | number | 是 | 否 | 映射内存保护类型，代表映射的内存可执行。 |
| PROT\_NONE | number | 是 | 否 | 映射内存保护类型，代表映射的内存不可访问。 |
| PROT\_READ | number | 是 | 否 | 映射内存保护类型，代表映射的内存可读。 |
| PROT\_WRITE | number | 是 | 否 | 映射内存保护类型，代表映射的内存可写。 |

#### \[h2\]create9+

static create(name: string, size: number): Ashmem

静态方法，根据指定的名称和大小创建Ashmem对象。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | Ashmem名称，用于查询Ashmem信息，其长度不能为0。 |
| size | number | 是 | Ashmem的大小，其大小应大于0，以字节为单位。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [Ashmem](#ashmem8) | 返回创建的Ashmem对象；如果创建失败，返回null。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.The Ashmem name passed is empty;

4.The Ashmem size passed is less than or equal to 0.

 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
  hilog.info(0x0000, 'testTag', 'create ashmem: ' + ashmem);
  let size = ashmem.getAshmemSize();
  hilog.info(0x0000, 'testTag',  'size is ' + size);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]createAshmem(deprecated)

static createAshmem(name: string, size: number): Ashmem

静态方法，根据指定的名称和大小创建Ashmem对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/-s2aiHiKRkimV1gnBfiZUA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=BBA9C061B1A479319273D2ACA443AB390D37D64A6A589B0859065F9E9200C10C)

从API version 8 开始支持，API version 9 开始废弃，建议使用[create](#create9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 名称，用于查询Ashmem信息。 |
| size | number | 是 | Ashmem的大小，以字节为单位。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [Ashmem](#ashmem8) | 返回创建的Ashmem对象；如果创建失败，返回null。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let ashmem = rpc.Ashmem.createAshmem("ashmem", 1024*1024);
  hilog.info(0x0000, 'testTag', 'create ashmem: ' + ashmem);
  let size = ashmem.getAshmemSize();
  hilog.info(0x0000, 'testTag',  'size is ' + size);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]create9+

static create(ashmem: Ashmem): Ashmem

静态方法，通过复制现有Ashmem对象的文件描述符(fd)来创建Ashmem对象。两个Ashmem对象指向同一个共享内存区域。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| ashmem | [Ashmem](#ashmem8) | 是 | 已存在的Ashmem对象。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [Ashmem](#ashmem8) | 返回创建的Ashmem对象。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The passed parameter is not an Ashmem object;

3.The ashmem instance for obtaining packaging is empty.

 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
  let ashmem2 = rpc.Ashmem.create(ashmem);
  let size = ashmem2.getAshmemSize();
  hilog.info(0x0000, 'testTag', 'size is ' + size);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]createAshmemFromExisting(deprecated)

static createAshmemFromExisting(ashmem: Ashmem): Ashmem

静态方法，通过复制现有Ashmem对象的文件描述符(fd)来创建Ashmem对象。两个Ashmem对象指向同一个共享内存区域。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/8nG0xbgTRSySbrXyF6xXnw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=E634E8DF79A64C8E9C72CAB3A9E97E0194849726D849B1CC131916CE1A8C3E33)

从API version 8 开始支持，API version 9 开始废弃，建议使用[create](#create9-1)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| ashmem | [Ashmem](#ashmem8) | 是 | 已存在的Ashmem对象。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [Ashmem](#ashmem8) | 返回创建的Ashmem对象。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
  let ashmem2 = rpc.Ashmem.createAshmemFromExisting(ashmem);
  let size = ashmem2.getAshmemSize();
  hilog.info(0x0000, 'testTag', 'size is ' + size);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error is ' + error);
}
```

#### \[h2\]closeAshmem8+

closeAshmem(): void

关闭这个Ashmem。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/k9WL-YxzQwmDHc06Hx7e_A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=4806D8EE61E86FFFE7DEB4D8B1F42E9589C5BB831CABB8289A3C9E8576B1EF1C)

关闭Ashmem对象前需要先解除地址映射。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
  ashmem.closeAshmem();
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error is ' + error);
}
```

#### \[h2\]unmapAshmem8+

unmapAshmem(): void

删除该Ashmem对象的地址映射。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
  ashmem.unmapAshmem();
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error is ' + error);
}
```

#### \[h2\]getAshmemSize8+

getAshmemSize(): number

获取Ashmem对象的内存大小。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回Ashmem对象的内存大小。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
  let size = ashmem.getAshmemSize();
  hilog.info(0x0000, 'testTag', ' size is ' + size);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error is ' + error);
}
```

#### \[h2\]mapTypedAshmem9+

mapTypedAshmem(mapType: number): void

在此进程的虚拟地址空间上创建共享文件映射，映射区域大小由此Ashmem对象指定。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| mapType | number | 是 | 指定映射的内存区域的保护等级。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.The passed mapType exceeds the maximum protection level.

 |
| 1900001 | Failed to call mmap. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
  ashmem.mapTypedAshmem(rpc.Ashmem.PROT_READ | rpc.Ashmem.PROT_WRITE);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]mapAshmem(deprecated)

mapAshmem(mapType: number): boolean

在此进程的虚拟地址空间上创建共享文件映射，映射区域大小由此Ashmem对象指定。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/EA_8v9SVQn2pkvAS8Qyfcg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=46297117D73BC0AFE111E59EE37AB4121D48BEC1125209DEAE7B403A499374E6)

从API version 8 开始支持，API version 9 开始废弃，建议使用[mapTypedAshmem](#maptypedashmem9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| mapType | number | 是 | 指定映射的内存区域的保护等级。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：映射成功，false：映射失败。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
  let mapReadAndWrite = ashmem.mapAshmem(rpc.Ashmem.PROT_READ | rpc.Ashmem.PROT_WRITE);
  hilog.info(0x0000, 'testTag', 'map ashmem result is ' + mapReadAndWrite);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error is ' + error);
}
```

#### \[h2\]mapReadWriteAshmem9+

mapReadWriteAshmem(): void

在此进程虚拟地址空间上创建可读写的共享文件映射。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 1900001 | Failed to call mmap. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
  ashmem.mapReadWriteAshmem();
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]mapReadAndWriteAshmem(deprecated)

mapReadAndWriteAshmem(): boolean

在此进程虚拟地址空间上创建可读写的共享文件映射。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/g9vdgFCsQgO1cU5od6DdJg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=083B7EE63EFA9962CBC8577F25E189DCC7BEA017C6E698B8B55CD4CA771DFD7B)

从API version 8 开始支持，API version 9 开始废弃，建议使用[mapReadWriteAshmem](#mapreadwriteashmem9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：映射成功，false：映射失败。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
  let mapResult = ashmem.mapReadAndWriteAshmem();
  hilog.info(0x0000, 'testTag', 'map ashmem result is ' + mapResult);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error is ' + error);
}
```

#### \[h2\]mapReadonlyAshmem9+

mapReadonlyAshmem(): void

在此进程虚拟地址空间上创建只读的共享文件映射。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 1900001 | Failed to call mmap. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
  ashmem.mapReadonlyAshmem();
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]mapReadOnlyAshmem(deprecated)

mapReadOnlyAshmem(): boolean

在此进程虚拟地址空间上创建只读的共享文件映射。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/_zhWI4oXSE2NxgKybC3-ew/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=58A642712295CC3C8FA3D3198C036E3CAAED0A7723AB7F14BB16B8F84B9F76FA)

从API version 8 开始支持，API version 9 开始废弃，建议使用[mapReadonlyAshmem](#mapreadonlyashmem9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：映射成功，false：映射失败。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
  let mapResult = ashmem.mapReadOnlyAshmem();
  hilog.info(0x0000, 'testTag', 'Ashmem mapReadOnlyAshmem result is ' + mapResult);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error is ' + error);
}
```

#### \[h2\]setProtectionType9+

setProtectionType(protectionType: number): void

设置映射内存区域的保护等级。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| protectionType | number | 是 | 要设置的保护类型。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900002 | Failed to call ioctl. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
  ashmem.setProtectionType(rpc.Ashmem.PROT_READ);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'Rpc set protection type fail, errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'Rpc set protection type fail, errorMessage ' + e.message);
}
```

#### \[h2\]setProtection(deprecated)

setProtection(protectionType: number): boolean

设置映射内存区域的保护等级。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/TH8x0zKKQRWWN0LY0jkJfg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=51D38E1E438A13C712D3920095173A6AA0D7231489A2D50174202B328762D058)

从API version 8 开始支持，API version 9 开始废弃，建议使用[setProtectionType](#setprotectiontype9)替代。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| protectionType | number | 是 | 要设置的保护类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：设置成功，false：设置失败。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
  let result = ashmem.setProtection(rpc.Ashmem.PROT_READ);
  hilog.info(0x0000, 'testTag', 'Ashmem setProtection result is ' + result);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

#### \[h2\]writeDataToAshmem11+

writeDataToAshmem(buf: ArrayBuffer, size: number, offset: number): void

将数据写入此Ashmem对象关联的共享文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/s3ex5hQdQOuFuIpZLOnFDA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=166292AA0C1CBA3EB701449C1C8DE8830BCA982F21A79B761D8629EF8FAA2CEE)

对Ashmem对象进行写操作时，需要先调用[mapReadWriteAshmem](#mapreadwriteashmem9)进行映射。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| buf | ArrayBuffer | 是 | 写入Ashmem对象的数据。 |
| size | number | 是 | 要写入的数据大小。 |
| offset | number | 是 | 要写入的数据在此Ashmem对象关联的内存区间的起始位置。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.Failed to obtain arrayBuffer information.

 |
| 1900003 | Failed to write data to the shared memory. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let buffer = new ArrayBuffer(1024);
  let int32View = new Int32Array(buffer);
  for (let i = 0; i < int32View.length; i++) {
    int32View[i] = i * 2 + 1;
  }
  let size = buffer.byteLength;
  let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
  ashmem.mapReadWriteAshmem();
  ashmem.writeDataToAshmem(buffer, size, 0);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]writeAshmem(deprecated)

writeAshmem(buf: number\[\], size: number, offset: number): void

将数据写入此Ashmem对象关联的共享文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/Tkw75ybkQyCy_pE5DUcISQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=04CE9727D07D146708FF4AA59CC1F3EF0F416B3076CC88D76AD1FF1D475EAA1E)

从API version 9 开始支持，API version 11 开始废弃，建议使用[writeDataToAshmem](#writedatatoashmem11)替代。

对Ashmem对象进行写操作时，需要先调用[mapReadWriteAshmem](#mapreadwriteashmem9)进行映射。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| buf | number\[\] | 是 | 写入Ashmem对象的数据。 |
| size | number | 是 | 要写入的数据大小。 |
| offset | number | 是 | 要写入的数据在此Ashmem对象关联的内存区间的起始位置。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.The element does not exist in the array.

 |
| 1900003 | Failed to write data to the shared memory. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
  ashmem.mapReadWriteAshmem();
  let ByteArrayVar = [1, 2, 3, 4, 5];
  ashmem.writeAshmem(ByteArrayVar, 5, 0);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'Rpc write to ashmem fail, errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'Rpc write to ashmem fail, errorMessage ' + e.message);
}
```

#### \[h2\]writeToAshmem(deprecated)

writeToAshmem(buf: number\[\], size: number, offset: number): boolean

将数据写入此Ashmem对象关联的共享文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/z4XGiL9XQCOLQg2S074D_g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=097FC6635C8170D2CB069CD49C1610B4EB62D4CEC81986C42D0114AC65D684AE)

从API version 8 开始支持，API version 9 开始废弃，建议使用[writeDataToAshmem](#writedatatoashmem11)替代。

对Ashmem对象进行写操作时，需要先调用[mapReadWriteAshmem](#mapreadwriteashmem9)进行映射。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| buf | number\[\] | 是 | 写入Ashmem对象的数据。 |
| size | number | 是 | 要写入的数据大小。 |
| offset | number | 是 | 要写入的数据在此Ashmem对象关联的内存区间的起始位置。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | true：如果数据写入成功，false：在其他情况下，如数据写入越界或未获得写入权限。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
  let mapResult = ashmem.mapReadAndWriteAshmem();
  hilog.info(0x0000, 'testTag', 'RpcTest map ashmem result is ' + mapResult);
  let ByteArrayVar = [1, 2, 3, 4, 5];
  let writeResult = ashmem.writeToAshmem(ByteArrayVar, 5, 0);
  hilog.info(0x0000, 'testTag', 'write to Ashmem result is ' + writeResult);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error is ' + error);
}
```

#### \[h2\]readDataFromAshmem11+

readDataFromAshmem(size: number, offset: number): ArrayBuffer

从此Ashmem对象关联的共享文件中读取数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/HCtDDDM2Q_uTXNVwI2Qq_g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=12415F3B90C17D0D1C5ED8C4931853B9FB1C7D8C405F3FCF68EF469D9D9F5289)

对Ashmem对象进行写操作时，需要先调用[mapReadWriteAshmem](#mapreadwriteashmem9)进行映射。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| size | number | 是 | 要读取的数据的大小。 |
| offset | number | 是 | 要读取的数据在此Ashmem对象关联的内存区间的起始位置。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| ArrayBuffer | 返回读取的数据。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900004 | Failed to read data from the shared memory. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let buffer = new ArrayBuffer(1024);
  let int32View = new Int32Array(buffer);
  for (let i = 0; i < int32View.length; i++) {
    int32View[i] = i * 2 + 1;
  }
  let size = buffer.byteLength;
  let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
  ashmem.mapReadWriteAshmem();
  ashmem.writeDataToAshmem(buffer, size, 0);
  let readResult = ashmem.readDataFromAshmem(size, 0);
  let readInt32View = new Int32Array(readResult);
  hilog.info(0x0000, 'testTag', 'read from Ashmem result is ' + readInt32View);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]readAshmem(deprecated)

readAshmem(size: number, offset: number): number\[\]

从此Ashmem对象关联的共享文件中读取数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/N3ae3GmFRg233G9ZLlycBA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=DF2605DB8AB3C03E9EAA5A2B464A0BE91F29639AA04E704B04CEFCEAF3EF19CA)

从API version 9 开始支持，API version 11 开始废弃，建议使用[readDataFromAshmem](#readdatafromashmem11)替代。

对Ashmem对象进行写操作时，需要先调用[mapReadWriteAshmem](#mapreadwriteashmem9)进行映射。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| size | number | 是 | 要读取的数据的大小。 |
| offset | number | 是 | 要读取的数据在此Ashmem对象关联的内存区间的起始位置。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number\[\] | 返回读取的数据。 |

**错误码：**

以下错误码的详细介绍请参见[ohos.rpc错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-rpc)

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900004 | Failed to read data from the shared memory. |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
  ashmem.mapReadWriteAshmem();
  let ByteArrayVar = [1, 2, 3, 4, 5];
  ashmem.writeAshmem(ByteArrayVar, 5, 0);
  let readResult = ashmem.readAshmem(5, 0);
  hilog.info(0x0000, 'testTag', 'read from Ashmem result is ' + readResult);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}
```

#### \[h2\]readFromAshmem(deprecated)

readFromAshmem(size: number, offset: number): number\[\]

从此Ashmem对象关联的共享文件中读取数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/KHeUZdl-R6mO22sD0x-TSQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=0B4B60E68E66FCF49CBFB0170411D976395614B897676808FCF16C741FED50E0)

从API version 8 开始支持，API version 9 开始废弃，建议使用[readDataFromAshmem](#readdatafromashmem11)替代。

对Ashmem对象进行写操作时，需要先调用[mapReadWriteAshmem](#mapreadwriteashmem9)进行映射。

\*\*系统能力：\*\*SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| size | number | 是 | 要读取的数据的大小。 |
| offset | number | 是 | 要读取的数据在此Ashmem对象关联的内存区间的起始位置。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number\[\] | 返回读取的数据。 |

**示例：**

```ts
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024*1024);
  let mapResult = ashmem.mapReadAndWriteAshmem();
  hilog.info(0x0000, 'testTag', 'RpcTest map ashmem result is ' + mapResult);
  let ByteArrayVar = [1, 2, 3, 4, 5];
  let writeResult = ashmem.writeToAshmem(ByteArrayVar, 5, 0);
  hilog.info(0x0000, 'testTag', 'write to Ashmem result is ' + writeResult);
  let readResult = ashmem.readFromAshmem(5, 0);
  hilog.info(0x0000, 'testTag', 'read to Ashmem result is ' + readResult);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error is ' + error);
}
```

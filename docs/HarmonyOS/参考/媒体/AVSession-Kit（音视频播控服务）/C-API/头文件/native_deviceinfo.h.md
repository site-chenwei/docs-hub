---
title: "native_deviceinfo.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-deviceinfo-h"
menu_path:
  - "参考"
  - "媒体"
  - "AVSession Kit（音视频播控服务）"
  - "C API"
  - "头文件"
  - "native_deviceinfo.h"
captured_at: "2026-04-17T01:48:38.409Z"
---

# native\_deviceinfo.h

#### 概述

提供播控设备信息的定义。

**引用文件：** <multimedia/av\_session/native\_deviceinfo.h>

**库：** libohavsession.so

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 23

**相关模块：** [OHAVSession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohavsession)

#### 汇总

#### \[h2\]结构体

| 名称 | typedef关键字 | 描述 |
| :-- | :-- | :-- |
| [AVSession\_OutputDeviceInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohavsession-avsession-outputdeviceinfo) | \- | 目标设备信息的定义。 |
| [AVSession\_DeviceInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohavsession-avsession-deviceinfo) | AVSession\_DeviceInfo | 设备信息的声明。该实例用于获取更多的设备信息及其详细属性。 |

#### \[h2\]函数

| 名称 | 描述 |
| :-- | :-- |
| [AVSession\_ErrCode OH\_DeviceInfo\_GetAVCastCategory(AVSession\_DeviceInfo \*deviceInfo, AVSession\_AVCastCategory \*aVCastCategory)](#oh_deviceinfo_getavcastcategory) | 获取目标设备的Cast类别。 |
| [AVSession\_ErrCode OH\_DeviceInfo\_GetDeviceId(AVSession\_DeviceInfo \*deviceInfo, char \*\*deviceId)](#oh_deviceinfo_getdeviceid) | 获取目标设备的设备ID。 |
| [AVSession\_ErrCode OH\_DeviceInfo\_GetDeviceName(AVSession\_DeviceInfo \*deviceInfo, char \*\*deviceName)](#oh_deviceinfo_getdevicename) | 获取目标设备的设备名称。 |
| [AVSession\_ErrCode OH\_DeviceInfo\_GetDeviceType(AVSession\_DeviceInfo \*deviceInfo, AVSession\_DeviceType \*deviceType)](#oh_deviceinfo_getdevicetype) | 获取目标设备的设备类型。 |
| [AVSession\_ErrCode OH\_DeviceInfo\_GetSupportedProtocols(AVSession\_DeviceInfo \*deviceInfo, uint32\_t \*deviceProtocolType)](#oh_deviceinfo_getsupportedprotocols) | 获取目标设备支持的协议。 |

#### 函数说明

#### \[h2\]OH\_DeviceInfo\_GetAVCastCategory()

```c
AVSession_ErrCode OH_DeviceInfo_GetAVCastCategory(AVSession_DeviceInfo *deviceInfo, AVSession_AVCastCategory *aVCastCategory)
```

**描述**

获取目标设备的Cast类别。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [AVSession\_DeviceInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohavsession-avsession-deviceinfo) \*deviceInfo | 表示设备信息实例指针。 |
| [AVSession\_AVCastCategory](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avsession-base-h#avsession_avcastcategory) \*aVCastCategory | 返回aVCastCategory值的指针变量。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [AVSession\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avsession-errors-h#avsession_errcode) | 
AV\_SESSION\_ERR\_SUCCESS：函数执行成功。

AV\_SESSION\_ERR\_INVALID\_PARAMETER：

1\. 参数deviceInfo为nullptr。

2\. 参数aVCastCategory为nullptr。

 |

#### \[h2\]OH\_DeviceInfo\_GetDeviceId()

```c
AVSession_ErrCode OH_DeviceInfo_GetDeviceId(AVSession_DeviceInfo *deviceInfo, char **deviceId)
```

**描述**

获取目标设备的设备ID。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [AVSession\_DeviceInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohavsession-avsession-deviceinfo) \*deviceInfo | 表示设备信息实例指针。 |
| char \*\*deviceId | 返回设备ID值的指针变量。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [AVSession\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avsession-errors-h#avsession_errcode) | 
AV\_SESSION\_ERR\_SUCCESS：函数执行成功。

AV\_SESSION\_ERR\_INVALID\_PARAMETER：

1\. 参数deviceInfo为nullptr。

2\. 参数deviceId为nullptr。

 |

#### \[h2\]OH\_DeviceInfo\_GetDeviceName()

```c
AVSession_ErrCode OH_DeviceInfo_GetDeviceName(AVSession_DeviceInfo *deviceInfo, char **deviceName)
```

**描述**

获取目标设备的设备名称。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [AVSession\_DeviceInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohavsession-avsession-deviceinfo) \*deviceInfo | 表示设备信息实例指针。 |
| char \*\*deviceName | 返回设备名称的指针变量。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [AVSession\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avsession-errors-h#avsession_errcode) | 
AV\_SESSION\_ERR\_SUCCESS：函数执行成功。

AV\_SESSION\_ERR\_INVALID\_PARAMETER：

1\. 参数deviceInfo为nullptr。

2\. 参数deviceName为nullptr。

 |

#### \[h2\]OH\_DeviceInfo\_GetDeviceType()

```c
AVSession_ErrCode OH_DeviceInfo_GetDeviceType(AVSession_DeviceInfo *deviceInfo, AVSession_DeviceType *deviceType)
```

**描述**

获取目标设备的设备类型。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [AVSession\_DeviceInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohavsession-avsession-deviceinfo) \*deviceInfo | 表示设备信息实例指针。 |
| [AVSession\_DeviceType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avsession-base-h#avsession_devicetype) \*deviceType | 返回设备类型的指针变量。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [AVSession\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avsession-errors-h#avsession_errcode) | 
AV\_SESSION\_ERR\_SUCCESS：函数执行成功。

AV\_SESSION\_ERR\_INVALID\_PARAMETER：

1\. 参数deviceInfo为nullptr。

2\. 参数deviceType为nullptr。

 |

#### \[h2\]OH\_DeviceInfo\_GetSupportedProtocols()

```c
AVSession_ErrCode OH_DeviceInfo_GetSupportedProtocols(AVSession_DeviceInfo *deviceInfo, uint32_t *deviceProtocolType)
```

**描述**

获取目标设备支持的协议。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [AVSession\_DeviceInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohavsession-avsession-deviceinfo) \*deviceInfo | 表示设备信息实例指针。 |
| uint32\_t \*deviceProtocolType | 返回设备支持协议的指针变量。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [AVSession\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avsession-errors-h#avsession_errcode) | 
AV\_SESSION\_ERR\_SUCCESS：函数执行成功。

AV\_SESSION\_ERR\_INVALID\_PARAMETER：

1\. 参数deviceInfo为nullptr。

2\. 参数deviceProtocolType为nullptr。

 |

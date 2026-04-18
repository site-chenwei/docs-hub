---
title: "oh_wifi.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-wifi-h"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Connectivity Kit（短距通信服务）"
  - "C API"
  - "头文件"
  - "oh_wifi.h"
captured_at: "2026-04-17T01:48:21.816Z"
---

# oh\_wifi.h

#### 概述

定义查询WIFI开关状态的接口。

**引用文件：** <ConnectivityKit/wifi/oh\_wifi.h>

**库：** libwifi\_ndk.so

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 13

**相关模块：** [Wifi](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-wifi)

#### 汇总

#### \[h2\]枚举

| 名称 | typedef关键字 | 描述 |
| :-- | :-- | :-- |
| [Wifi\_ResultCode](#wifi_resultcode) | Wifi\_ResultCode | 定义WIFI接口返回值的错误码。 |

#### \[h2\]函数

| 名称 | 描述 |
| :-- | :-- |
| [Wifi\_ResultCode OH\_Wifi\_IsWifiEnabled(bool \*enabled)](#oh_wifi_iswifienabled) | 查询WIFI开关是否开启。 |
| [Wifi\_ResultCode OH\_Wifi\_GetDeviceMacAddress(char \*macAddr, unsigned int \*macAddrLen)](#oh_wifi_getdevicemacaddress) | 该接口用于获取设备真实MAC地址。 |

#### 枚举类型说明

#### \[h2\]Wifi\_ResultCode

```c
enum Wifi_ResultCode
```

**描述**

定义WIFI接口返回值的错误码。

**起始版本：** 13

| 枚举项 | 描述 |
| :-- | :-- |
| WIFI\_SUCCESS = 0 | 操作成功。 |
| WIFI\_PERMISSION\_DENIED = 201 | 权限校验失败。 |
| WIFI\_INVALID\_PARAM = 401 | 
参数错误。

可能原因：1.输入参数为空指针；2.参数数值超出定义范围。

 |
| WIFI\_NOT\_SUPPORTED = 801 | 该功能不支持。由于设备能力有限，无法调用该函数。 |
| WIFI\_OPERATION\_FAILED = 2501000 | 

操作失败。

可能原因：服务内部执行失败。

 |
| WIFI\_STA\_DISABLED = 2501001 | 

STA服务未拉起。

可能原因：WiFi未打开。

**起始版本：** 21

 |

#### 函数说明

#### \[h2\]OH\_Wifi\_IsWifiEnabled()

```c
Wifi_ResultCode OH_Wifi_IsWifiEnabled(bool *enabled)
```

**描述**

查询WIFI开关是否开启。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| bool \*enabled | 
\- bool类型的指针，用于接收WIFI开关状态值。

等于true表示WIFI开关开启，false表示WIFI开关关闭。

需要传入非空指针，否则会返回错误。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [Wifi\_ResultCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-wifi-h#wifi_resultcode) | 
返回操作结果，详细定义参见[Wifi\_ResultCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-wifi-h#wifi_resultcode).

[WIFI\_SUCCESS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-wifi-h#wifi_resultcode) 查询WIFI开关状态成功。

[WIFI\_INVALID\_PARAM](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-wifi-h#wifi_resultcode) 入参为空指针。

[WIFI\_OPERATION\_FAILED](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-wifi-h#wifi_resultcode) 服务内部执行错误。

 |

#### \[h2\]OH\_Wifi\_GetDeviceMacAddress()

```c
Wifi_ResultCode OH_Wifi_GetDeviceMacAddress(char *macAddr, unsigned int *macAddrLen)
```

**描述**

该接口用于获取设备真实MAC地址。

**需要权限：** ohos.permission.GET\_WIFI\_LOCAL\_MAC 和 ohos.permission.GET\_WIFI\_INFO

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| char \*macAddr | 设备MAC地址的字符数组，以'\\0'结尾。 |
| unsigned int \*macAddrLen | 为macAddr字符数组分配的内存大小。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [Wifi\_ResultCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-wifi-h#wifi_resultcode) | 
返回操作结果，详细定义参见[Wifi\_ResultCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-wifi-h#wifi_resultcode)。

[WIFI\_SUCCESS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-wifi-h#wifi_resultcode) 成功获取设备MAC地址。

[WIFI\_PERMISSION\_DENIED](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-wifi-h#wifi_resultcode) 权限拒绝。

[WIFI\_NOT\_SUPPORTED](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-wifi-h#wifi_resultcode) 不支持该能力。

[WIFI\_INVALID\_PARAM](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-wifi-h#wifi_resultcode) 输入参数macAddr是空指针。

[WIFI\_OPERATION\_FAILED](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-wifi-h#wifi_resultcode) 内部执行失败。

[WIFI\_STA\_DISABLED](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-wifi-h#wifi_resultcode) Wi-Fi STA模式未启用。

 |

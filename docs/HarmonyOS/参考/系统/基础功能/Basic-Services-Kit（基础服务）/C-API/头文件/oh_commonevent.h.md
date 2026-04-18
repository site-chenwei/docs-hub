---
title: "oh_commonevent.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "Basic Services Kit（基础服务）"
  - "C API"
  - "头文件"
  - "oh_commonevent.h"
captured_at: "2026-04-17T01:48:28.877Z"
---

# oh\_commonevent.h

#### 概述

定义公共事件订阅与退订API接口与枚举错误码。

**库：** libohcommonevent.so

**引用文件：** <BasicServicesKit/oh\_commonevent.h>

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 12

**相关模块：** [OH\_CommonEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent)

#### 汇总

#### \[h2\]结构体

| 名称 | typedef关键字 | 描述 |
| :-- | :-- | :-- |
| [CommonEvent\_SubscribeInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-commonevent-subscribeinfo) | CommonEvent\_SubscribeInfo | 提供CommonEvent\_SubscribeInfo订阅者信息结构体声明。 |
| [CommonEvent\_PublishInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-commonevent-publishinfo) | CommonEvent\_PublishInfo | 发布公共事件时使用的公共事件属性对象。 |
| [CommonEvent\_RcvData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-commonevent-rcvdata) | CommonEvent\_RcvData | 提供CommonEvent\_RcvData公共事件回调数据结构体声明。 |

#### \[h2\]变量

| 名称 | typedef关键字 | 描述 |
| :-- | :-- | :-- |
| void | CommonEvent\_Subscriber | 提供CommonEvent\_Subscriber订阅者结构体声明。 |
| void | CommonEvent\_Parameters | 提供CommonEvent\_RcvData公共事件附加信息结构体声明。 |

#### \[h2\]枚举

| 名称 | typedef关键字 | 描述 |
| :-- | :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | CommonEvent\_ErrCode | 枚举错误码。 |

#### \[h2\]函数

| 名称 | typedef关键字 | 描述 |
| :-- | :-- | :-- |
| [typedef void (\*CommonEvent\_ReceiveCallback)(const CommonEvent\_RcvData \*data)](#commonevent_receivecallback) | CommonEvent\_ReceiveCallback | 提供CommonEvent\_ReceiveCallback回调函数声明。 |
| [CommonEvent\_SubscribeInfo\* OH\_CommonEvent\_CreateSubscribeInfo(const char\* events\[\], int32\_t eventsNum)](#oh_commonevent_createsubscribeinfo) | \- | 创建订阅者信息。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetPublisherPermission(CommonEvent\_SubscribeInfo\* info, const char\* permission)](#oh_commonevent_setpublisherpermission) | \- | 设置订阅者权限。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetPublisherBundleName(CommonEvent\_SubscribeInfo\* info, const char\* bundleName)](#oh_commonevent_setpublisherbundlename) | \- | 设置订阅者包名称。 |
| [void OH\_CommonEvent\_DestroySubscribeInfo(CommonEvent\_SubscribeInfo\* info)](#oh_commonevent_destroysubscribeinfo) | \- | 释放订阅者信息。 |
| [CommonEvent\_Subscriber\* OH\_CommonEvent\_CreateSubscriber(const CommonEvent\_SubscribeInfo\* info,CommonEvent\_ReceiveCallback callback)](#oh_commonevent_createsubscriber) | \- | 创建订阅者。 |
| [void OH\_CommonEvent\_DestroySubscriber(CommonEvent\_Subscriber\* subscriber)](#oh_commonevent_destroysubscriber) | \- | 释放订阅者。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_Subscribe(const CommonEvent\_Subscriber\* subscriber)](#oh_commonevent_subscribe) | \- | 订阅公共事件。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_UnSubscribe(const CommonEvent\_Subscriber\* subscriber)](#oh_commonevent_unsubscribe) | \- | 退订公共事件。 |
| [const char\* OH\_CommonEvent\_GetEventFromRcvData(const CommonEvent\_RcvData\* rcvData)](#oh_commonevent_geteventfromrcvdata) | \- | 获取当前接收的公共事件名称。 |
| [int32\_t OH\_CommonEvent\_GetCodeFromRcvData(const CommonEvent\_RcvData\* rcvData)](#oh_commonevent_getcodefromrcvdata) | \- | 获取接收到的公共事件数据，整数类型。 |
| [const char\* OH\_CommonEvent\_GetDataStrFromRcvData(const CommonEvent\_RcvData\* rcvData)](#oh_commonevent_getdatastrfromrcvdata) | \- | 获取接收到的公共事件数据，字符串类型。 |
| [const char\* OH\_CommonEvent\_GetBundleNameFromRcvData(const CommonEvent\_RcvData\* rcvData)](#oh_commonevent_getbundlenamefromrcvdata) | \- | 获取接收到的公共事件的包名称信息。 |
| [const CommonEvent\_Parameters\* OH\_CommonEvent\_GetParametersFromRcvData(const CommonEvent\_RcvData\* rcvData)](#oh_commonevent_getparametersfromrcvdata) | \- | 获取接收到的公共事件的附加信息。 |
| [CommonEvent\_PublishInfo\* OH\_CommonEvent\_CreatePublishInfo(bool ordered)](#oh_commonevent_createpublishinfo) | \- | 创建公共事件属性对象。 |
| [void OH\_CommonEvent\_DestroyPublishInfo(CommonEvent\_PublishInfo\* info)](#oh_commonevent_destroypublishinfo) | \- | 销毁公共事件属性对象。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetPublishInfoBundleName(CommonEvent\_PublishInfo\* info, const char\* bundleName)](#oh_commonevent_setpublishinfobundlename) | \- | 设置公共事件订阅者包名称。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetPublishInfoPermissions(CommonEvent\_PublishInfo\* info,const char\* permissions\[\], int32\_t num)](#oh_commonevent_setpublishinfopermissions) | \- | 设置公共事件订阅者权限。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetPublishInfoCode(CommonEvent\_PublishInfo\* info, int32\_t code)](#oh_commonevent_setpublishinfocode) | \- | 设置公共事件传递的数据，整数类型。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetPublishInfoData(CommonEvent\_PublishInfo\* info,const char\* data, size\_t length)](#oh_commonevent_setpublishinfodata) | \- | 设置公共事件传递的数据，字符串类型。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetPublishInfoParameters(CommonEvent\_PublishInfo\* info,CommonEvent\_Parameters\* param)](#oh_commonevent_setpublishinfoparameters) | \- | 设置公共事件传递的附加信息。 |
| [CommonEvent\_Parameters\* OH\_CommonEvent\_CreateParameters()](#oh_commonevent_createparameters) | \- | 创建公共事件附加信息对象。 |
| [void OH\_CommonEvent\_DestroyParameters(CommonEvent\_Parameters\* param)](#oh_commonevent_destroyparameters) | \- | 销毁公共事件附加信息对象。 |
| [bool OH\_CommonEvent\_HasKeyInParameters(const CommonEvent\_Parameters\* para, const char\* key)](#oh_commonevent_haskeyinparameters) | \- | 检查附加信息中是否包含键值对信息。 |
| [int OH\_CommonEvent\_GetIntFromParameters(const CommonEvent\_Parameters\* para, const char\* key, const int defaultValue)](#oh_commonevent_getintfromparameters) | \- | 获取公共事件附加信息中键为key的int类型内容。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetIntToParameters(CommonEvent\_Parameters\* param, const char\* key, int value)](#oh_commonevent_setinttoparameters) | \- | 设置公共事件附加信息的int类型内容。 |
| [int32\_t OH\_CommonEvent\_GetIntArrayFromParameters(const CommonEvent\_Parameters\* para, const char\* key, int\*\* array)](#oh_commonevent_getintarrayfromparameters) | \- | 获取公共事件附加信息中键为key的int数组数据。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetIntArrayToParameters(CommonEvent\_Parameters\* param, const char\* key,const int\* value, size\_t num)](#oh_commonevent_setintarraytoparameters) | \- | 设置公共事件附加信息的int数组内容。 |
| [long OH\_CommonEvent\_GetLongFromParameters(const CommonEvent\_Parameters\* para, const char\* key, const long defaultValue)](#oh_commonevent_getlongfromparameters) | \- | 获取公共事件附加信息中键为key的long类型数据。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetLongToParameters(CommonEvent\_Parameters\* param, const char\* key, long value)](#oh_commonevent_setlongtoparameters) | \- | 设置公共事件附加信息的long类型内容。 |
| [int32\_t OH\_CommonEvent\_GetLongArrayFromParameters(const CommonEvent\_Parameters\* para, const char\* key, long\*\* array)](#oh_commonevent_getlongarrayfromparameters) | \- | 获取公共事件附加信息的long数组内容。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetLongArrayToParameters(CommonEvent\_Parameters\* param, const char\* key,const long\* value, size\_t num)](#oh_commonevent_setlongarraytoparameters) | \- | 设置公共事件附加信息的long数组内容。 |
| [bool OH\_CommonEvent\_GetBoolFromParameters(const CommonEvent\_Parameters\* para, const char\* key, const bool defaultValue)](#oh_commonevent_getboolfromparameters) | \- | 获取公共事件附加信息中键为key的布尔类型数据。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetBoolToParameters(CommonEvent\_Parameters\* param, const char\* key, bool value)](#oh_commonevent_setbooltoparameters) | \- | 设置公共事件附加信息的布尔类型内容。 |
| [int32\_t OH\_CommonEvent\_GetBoolArrayFromParameters(const CommonEvent\_Parameters\* para, const char\* key, bool\*\* array)](#oh_commonevent_getboolarrayfromparameters) | \- | 获取公共事件附加信息的布尔数组内容。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetBoolArrayToParameters(CommonEvent\_Parameters\* param, const char\* key,const bool\* value, size\_t num)](#oh_commonevent_setboolarraytoparameters) | \- | 设置公共事件附加信息的布尔数组内容。 |
| [char OH\_CommonEvent\_GetCharFromParameters(const CommonEvent\_Parameters\* para, const char\* key, const char defaultValue)](#oh_commonevent_getcharfromparameters) | \- | 获取公共事件附加信息中键为key的字符类型数据。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetCharToParameters(CommonEvent\_Parameters\* param, const char\* key, char value)](#oh_commonevent_setchartoparameters) | \- | 设置公共事件附加信息的字符类型内容。 |
| [int32\_t OH\_CommonEvent\_GetCharArrayFromParameters(const CommonEvent\_Parameters\* para, const char\* key, char\*\* array)](#oh_commonevent_getchararrayfromparameters) | \- | 获取公共事件附加信息的字符数组内容。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetCharArrayToParameters(CommonEvent\_Parameters\* param, const char\* key,const char\* value, size\_t num)](#oh_commonevent_setchararraytoparameters) | \- | 设置公共事件附加信息的字符数组内容。 |
| [double OH\_CommonEvent\_GetDoubleFromParameters(const CommonEvent\_Parameters\* para, const char\* key,const double defaultValue)](#oh_commonevent_getdoublefromparameters) | \- | 获取公共事件附加信息的double类型内容。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetDoubleToParameters(CommonEvent\_Parameters\* param, const char\* key,double value)](#oh_commonevent_setdoubletoparameters) | \- | 设置公共事件附加信息的double类型内容。 |
| [int32\_t OH\_CommonEvent\_GetDoubleArrayFromParameters(const CommonEvent\_Parameters\* para, const char\* key,double\*\* array)](#oh_commonevent_getdoublearrayfromparameters) | \- | 获取公共事件附加信息中键为key的double数组数据。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetDoubleArrayToParameters(CommonEvent\_Parameters\* param, const char\* key,const double\* value, size\_t num)](#oh_commonevent_setdoublearraytoparameters) | \- | 设置公共事件附加信息的double数组内容。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_Publish(const char\* event)](#oh_commonevent_publish) | \- | 发布公共事件。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_PublishWithInfo(const char\* event, const CommonEvent\_PublishInfo\* info)](#oh_commonevent_publishwithinfo) | \- | 发布带有指定属性的公共事件。 |
| [bool OH\_CommonEvent\_IsOrderedCommonEvent(const CommonEvent\_Subscriber\* subscriber)](#oh_commonevent_isorderedcommonevent) | \- | 查询当前公共事件是否为有序公共事件。 |
| [bool OH\_CommonEvent\_FinishCommonEvent(CommonEvent\_Subscriber\* subscriber)](#oh_commonevent_finishcommonevent) | \- | 用于订阅者结束对当前有序公共事件的处理。 |
| [bool OH\_CommonEvent\_GetAbortCommonEvent(const CommonEvent\_Subscriber\* subscriber)](#oh_commonevent_getabortcommonevent) | \- | 获取当前有序公共事件是否处于中止状态。 |
| [bool OH\_CommonEvent\_AbortCommonEvent(CommonEvent\_Subscriber\* subscriber)](#oh_commonevent_abortcommonevent) | \- | 该接口与[OH\_CommonEvent\_FinishCommonEvent](#oh_commonevent_finishcommonevent)配合使用，可以中止当前的有序公共事件，使该公共事件不再向下一个订阅者传递。 |
| [bool OH\_CommonEvent\_ClearAbortCommonEvent(CommonEvent\_Subscriber\* subscriber)](#oh_commonevent_clearabortcommonevent) | \- | 该接口与[OH\_CommonEvent\_FinishCommonEvent](#oh_commonevent_finishcommonevent)配合使用，可以取消当前有序公共事件的中止状态，使该公共事件继续向下一个订阅者传递。 |
| [int32\_t OH\_CommonEvent\_GetCodeFromSubscriber(const CommonEvent\_Subscriber\* subscriber)](#oh_commonevent_getcodefromsubscriber) | \- | 获取有序公共事件传递的数据，整数类型。 |
| [bool OH\_CommonEvent\_SetCodeToSubscriber(CommonEvent\_Subscriber\* subscriber, int32\_t code)](#oh_commonevent_setcodetosubscriber) | \- | 设置有序公共事件传递的数据，整数类型。 |
| [const char\* OH\_CommonEvent\_GetDataFromSubscriber(const CommonEvent\_Subscriber\* subscriber)](#oh_commonevent_getdatafromsubscriber) | \- | 获取有序公共事件传递的数据，字符串类型。 |
| [bool OH\_CommonEvent\_SetDataToSubscriber(CommonEvent\_Subscriber\* subscriber, const char\* data, size\_t length)](#oh_commonevent_setdatatosubscriber) | \- | 设置有序公共事件传递的数据，字符串类型。 |

#### 枚举类型说明

#### \[h2\]CommonEvent\_ErrCode

```c
enum CommonEvent_ErrCode
```

**描述**

枚举错误码。

**起始版本：** 12

| 枚举项 | 描述 |
| :-- | :-- |
| COMMONEVENT\_ERR\_OK = 0 | 成功。 |
| COMMONEVENT\_ERR\_PERMISSION\_ERROR = 201 | 权限错误。 |
| COMMONEVENT\_ERR\_INVALID\_PARAMETER = 401 | 参数错误。 |
| COMMONEVENT\_ERR\_SENDING\_LIMIT\_EXCEEDED = 1500003 | 
事件发送频率过高。

**起始版本：** 20

 |
| COMMONEVENT\_ERR\_NOT\_SYSTEM\_SERVICE = 1500004 | 三方应用无法发送系统公共事件。 |
| COMMONEVENT\_ERR\_SENDING\_REQUEST\_FAILED = 1500007 | IPC发送失败。 |
| COMMONEVENT\_ERR\_INIT\_UNDONE = 1500008 | 服务未初始化。 |
| COMMONEVENT\_ERR\_OBTAIN\_SYSTEM\_PARAMS = 1500009 | 系统错误。 |
| COMMONEVENT\_ERR\_SUBSCRIBER\_NUM\_EXCEEDED = 1500010 | 订阅者数量超过限制。 |
| COMMONEVENT\_ERR\_ALLOC\_MEMORY\_FAILED = 1500011 | 内存分配失败。 |

#### 函数说明

#### \[h2\]CommonEvent\_ReceiveCallback()

```c
typedef void (*CommonEvent_ReceiveCallback)(const CommonEvent_RcvData *data)
```

**描述**

提供CommonEvent\_ReceiveCallback回调函数声明。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const [CommonEvent\_RcvData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-commonevent-rcvdata) \*data | 公共事件回调数据。 |

#### \[h2\]OH\_CommonEvent\_CreateSubscribeInfo()

```c
CommonEvent_SubscribeInfo* OH_CommonEvent_CreateSubscribeInfo(const char* events[], int32_t eventsNum)
```

**描述**

创建订阅者信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const char\* events\[\] | 订阅的公共事件，实际订阅的公共事件数量为eventsNum与events数组长度的最小值。 |
| int32\_t eventsNum | 订阅的公共事件数量。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [CommonEvent\_SubscribeInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-commonevent-subscribeinfo)\* | 成功则返回订阅者信息,失败则返回NULL。 |

#### \[h2\]OH\_CommonEvent\_SetPublisherPermission()

```c
CommonEvent_ErrCode OH_CommonEvent_SetPublisherPermission(CommonEvent_SubscribeInfo* info, const char* permission)
```

**描述**

设置订阅者权限。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [CommonEvent\_SubscribeInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-commonevent-subscribeinfo)\* info | 订阅者信息。 |
| const char\* permission | 权限名称。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
返回错误码。

返回[COMMONEVENT\_ERR\_OK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示成功。

返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示参数错误。

 |

#### \[h2\]OH\_CommonEvent\_SetPublisherBundleName()

```c
CommonEvent_ErrCode OH_CommonEvent_SetPublisherBundleName(CommonEvent_SubscribeInfo* info, const char* bundleName)
```

**描述**

设置订阅者包名称。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [CommonEvent\_SubscribeInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-commonevent-subscribeinfo)\* info | 订阅者信息。 |
| const char\* bundleName | 包名称。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
返回错误码。

返回[COMMONEVENT\_ERR\_OK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示成功。

返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示参数错误。

 |

#### \[h2\]OH\_CommonEvent\_DestroySubscribeInfo()

```c
void OH_CommonEvent_DestroySubscribeInfo(CommonEvent_SubscribeInfo* info)
```

**描述**

释放订阅者信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [CommonEvent\_SubscribeInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-commonevent-subscribeinfo)\* info | 订阅者信息。 |

#### \[h2\]OH\_CommonEvent\_CreateSubscriber()

```c
CommonEvent_Subscriber* OH_CommonEvent_CreateSubscriber(const CommonEvent_SubscribeInfo* info,CommonEvent_ReceiveCallback callback)
```

**描述**

创建订阅者。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const [CommonEvent\_SubscribeInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-commonevent-subscribeinfo)\* info | 订阅者信息。 |
| [CommonEvent\_ReceiveCallback](#commonevent_receivecallback) callback | 公共事件回调函数 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [CommonEvent\_Subscriber](#变量)\* | 成功则返回订阅者,失败则返回NULL。 |

#### \[h2\]OH\_CommonEvent\_DestroySubscriber()

```c
void OH_CommonEvent_DestroySubscriber(CommonEvent_Subscriber* subscriber)
```

**描述**

释放订阅者。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [CommonEvent\_Subscriber](#变量)\* subscriber | 订阅者。 |

#### \[h2\]OH\_CommonEvent\_Subscribe()

```c
CommonEvent_ErrCode OH_CommonEvent_Subscribe(const CommonEvent_Subscriber* subscriber)
```

**描述**

订阅公共事件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const [CommonEvent\_Subscriber](#变量)\* subscriber | 订阅者。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
返回错误码。

返回[COMMONEVENT\_ERR\_OK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示成功。

返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示参数subscriber无效。

返回[COMMONEVENT\_ERR\_SENDING\_REQUEST\_FAILED](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示IPC请求发送失败。

返回[COMMONEVENT\_ERR\_INIT\_UNDONE](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示公共事件服务未初始化。

返回[COMMONEVENT\_ERR\_SUBSCRIBER\_NUM\_EXCEEDED](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示进程订阅者数量超过200个。

返回[COMMONEVENT\_ERR\_ALLOC\_MEMORY\_FAILED](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)系统分配内存失败。

 |

#### \[h2\]OH\_CommonEvent\_UnSubscribe()

```c
CommonEvent_ErrCode OH_CommonEvent_UnSubscribe(const CommonEvent_Subscriber* subscriber)
```

**描述**

退订公共事件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const [CommonEvent\_Subscriber](#变量)\* subscriber | 订阅者。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
返回错误码。

返回[COMMONEVENT\_ERR\_OK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示成功。

返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示参数subscriber无效。

返回[COMMONEVENT\_ERR\_SENDING\_REQUEST\_FAILED](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示IPC请求发送失败。

返回[COMMONEVENT\_ERR\_INIT\_UNDONE](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示公共事件服务未初始化。

 |

#### \[h2\]OH\_CommonEvent\_GetEventFromRcvData()

```c
const char* OH_CommonEvent_GetEventFromRcvData(const CommonEvent_RcvData* rcvData)
```

**描述**

获取当前接收的公共事件名称。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const [CommonEvent\_RcvData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-commonevent-rcvdata)\* rcvData | 公共事件回调数据。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| const char\* | 返回事件名称。 |

#### \[h2\]OH\_CommonEvent\_GetCodeFromRcvData()

```c
int32_t OH_CommonEvent_GetCodeFromRcvData(const CommonEvent_RcvData* rcvData)
```

**描述**

获取公共事件传递的数据，整数类型。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const [CommonEvent\_RcvData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-commonevent-rcvdata)\* rcvData | 公共事件回调数据。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 返回公共事件传递的数据，整数类型。 |

#### \[h2\]OH\_CommonEvent\_GetDataStrFromRcvData()

```c
const char* OH_CommonEvent_GetDataStrFromRcvData(const CommonEvent_RcvData* rcvData)
```

**描述**

获取公共事件传递的数据，字符串类型。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const [CommonEvent\_RcvData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-commonevent-rcvdata)\* rcvData | 公共事件回调数据。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| const char\* | 返回公共事件传递的数据，字符串类型。 |

#### \[h2\]OH\_CommonEvent\_GetBundleNameFromRcvData()

```c
const char* OH_CommonEvent_GetBundleNameFromRcvData(const CommonEvent_RcvData* rcvData)
```

**描述**

获取接收到的公共事件的包名称信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const [CommonEvent\_RcvData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-commonevent-rcvdata)\* rcvData | 公共事件回调数据。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| const char\* | 返回公共事件的包名称。 |

#### \[h2\]OH\_CommonEvent\_GetParametersFromRcvData()

```c
const CommonEvent_Parameters* OH_CommonEvent_GetParametersFromRcvData(const CommonEvent_RcvData* rcvData)
```

**描述**

获取公共事件附加信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const [CommonEvent\_RcvData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-commonevent-rcvdata)\* rcvData | 公共事件回调数据。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| const [CommonEvent\_Parameters](#变量)\* | 返回公共事件附加信息。 |

#### \[h2\]OH\_CommonEvent\_CreatePublishInfo()

```c
CommonEvent_PublishInfo* OH_CommonEvent_CreatePublishInfo(bool ordered)
```

**描述**

创建公共事件属性对象。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| bool ordered | 
是否为有序公共事件。

\- true：有序公共事件。

\- false：无序公共事件。

 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [CommonEvent\_PublishInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-commonevent-publishinfo)\* | 创建的公共事件属性对象，创建失败时，返回null。 |

#### \[h2\]OH\_CommonEvent\_DestroyPublishInfo()

```c
void OH_CommonEvent_DestroyPublishInfo(CommonEvent_PublishInfo* info)
```

**描述**

销毁公共事件属性对象。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [CommonEvent\_PublishInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-commonevent-publishinfo)\* info | 要销毁的公共事件属性对象。 |

#### \[h2\]OH\_CommonEvent\_SetPublishInfoBundleName()

```c
CommonEvent_ErrCode OH_CommonEvent_SetPublishInfoBundleName(CommonEvent_PublishInfo* info, const char* bundleName)
```

**描述**

设置公共事件订阅者包名称。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [CommonEvent\_PublishInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-commonevent-publishinfo)\* info | 公共事件属性对象。 |
| const char\* bundleName | 设置的订阅者包名称。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
返回错误码。

返回[COMMONEVENT\_ERR\_OK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示成功。

返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示参数错误。

 |

#### \[h2\]OH\_CommonEvent\_SetPublishInfoPermissions()

```c
CommonEvent_ErrCode OH_CommonEvent_SetPublishInfoPermissions(CommonEvent_PublishInfo* info,const char* permissions[], int32_t num)
```

**描述**

设置公共事件订阅者权限。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [CommonEvent\_PublishInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-commonevent-publishinfo)\* info | 公共事件属性对象。 |
| const char\* permissions\[\] | 订阅者权限名称数组，生效数量为num与permissions数组长度的最小值。 |
| int32\_t num | 权限的数量。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
返回错误码。

返回[COMMONEVENT\_ERR\_OK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示成功。

返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示参数错误。

 |

#### \[h2\]OH\_CommonEvent\_SetPublishInfoCode()

```c
CommonEvent_ErrCode OH_CommonEvent_SetPublishInfoCode(CommonEvent_PublishInfo* info, int32_t code)
```

**描述**

设置公共事件传递的数据，整数类型。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [CommonEvent\_PublishInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-commonevent-publishinfo)\* info | 公共事件属性对象。 |
| int32\_t code | 公共事件传递的数据，整数类型。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
返回错误码。

返回[COMMONEVENT\_ERR\_OK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示成功。

返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示参数错误。

 |

#### \[h2\]OH\_CommonEvent\_SetPublishInfoData()

```c
CommonEvent_ErrCode OH_CommonEvent_SetPublishInfoData(CommonEvent_PublishInfo* info,const char* data, size_t length)
```

**描述**

设置公共事件传递的数据，字符串类型。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [CommonEvent\_PublishInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-commonevent-publishinfo)\* info | 公共事件属性对象。 |
| const char\* data | 公共事件传递的数据，字符串类型，实际有效数据长度为length和data字符串长度的最小值。 |
| size\_t length | 结果数据的长度。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
返回错误码。

返回[COMMONEVENT\_ERR\_OK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示成功。

返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示参数错误。

 |

#### \[h2\]OH\_CommonEvent\_SetPublishInfoParameters()

```c
CommonEvent_ErrCode OH_CommonEvent_SetPublishInfoParameters(CommonEvent_PublishInfo* info,CommonEvent_Parameters* param)
```

**描述**

设置公共事件附加信息。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [CommonEvent\_PublishInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-commonevent-publishinfo)\* info | 公共事件属性对象。 |
| CommonEvent\_Parameters\* param | 设置的附加信息。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
返回错误码。

返回[COMMONEVENT\_ERR\_OK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示成功。

返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示参数错误。

 |

#### \[h2\]OH\_CommonEvent\_CreateParameters()

```c
CommonEvent_Parameters* OH_CommonEvent_CreateParameters()
```

**描述**

创建公共事件附加信息对象。

**起始版本：** 18

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [CommonEvent\_Parameters](#变量)\* | 返回公共事件附加信息，创建失败时，返回null。 |

#### \[h2\]OH\_CommonEvent\_DestroyParameters()

```c
void OH_CommonEvent_DestroyParameters(CommonEvent_Parameters* param)
```

**描述**

销毁公共事件附加信息对象。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [CommonEvent\_Parameters](#变量)\* param | 公共事件附加信息。 |

#### \[h2\]OH\_CommonEvent\_HasKeyInParameters()

```c
bool OH_CommonEvent_HasKeyInParameters(const CommonEvent_Parameters* para, const char* key)
```

**描述**

检查附加信息中是否包含键值对信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const [CommonEvent\_Parameters](#变量)\* para | 公共事件附加信息。 |
| const char\* key | 数据键。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| bool | 
返回数据键是否存在。

\- true：存在。

\- false：不存在。

 |

#### \[h2\]OH\_CommonEvent\_GetIntFromParameters()

```c
int OH_CommonEvent_GetIntFromParameters(const CommonEvent_Parameters* para, const char* key, const int defaultValue)
```

**描述**

获取公共事件附加信息中键为key的int类型内容。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const [CommonEvent\_Parameters](#变量)\* para | 公共事件附加信息。 |
| const char\* key | 数据键。 |
| const int defaultValue | 默认值。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int | 返回查询的int类型数据。 |

#### \[h2\]OH\_CommonEvent\_SetIntToParameters()

```c
CommonEvent_ErrCode OH_CommonEvent_SetIntToParameters(CommonEvent_Parameters* param, const char* key, int value)
```

**描述**

设置公共事件附加信息的int类型内容。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [CommonEvent\_Parameters](#变量)\* param | 公共事件附加信息。 |
| const char\* key | 数据键。 |
| int value | 设置的int类型内容。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
返回错误码。

返回[COMMONEVENT\_ERR\_OK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示成功。

返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示参数错误。

 |

#### \[h2\]OH\_CommonEvent\_GetIntArrayFromParameters()

```c
int32_t OH_CommonEvent_GetIntArrayFromParameters(const CommonEvent_Parameters* para, const char* key, int** array)
```

**描述**

获取公共事件附加信息中键为key的int数组数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const [CommonEvent\_Parameters](#变量)\* para | 公共事件附加信息。 |
| const char\* key | 数据键。 |
| int\*\* array | 查询的数组。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 返回查询的数组长度，默认值为0。 |

#### \[h2\]OH\_CommonEvent\_SetIntArrayToParameters()

```c
CommonEvent_ErrCode OH_CommonEvent_SetIntArrayToParameters(CommonEvent_Parameters* param, const char* key,const int* value, size_t num)
```

**描述**

设置公共事件附加信息的int数组内容。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [CommonEvent\_Parameters](#变量)\* param | 公共事件附加信息。 |
| const char\* key | 数据键。 |
| const int\* value | 设置的int数组内容。 |
| size\_t num | 设置的int数组内容中元素的个数。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
返回错误码。

返回[COMMONEVENT\_ERR\_OK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示成功。

返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示参数错误。

返回[COMMONEVENT\_ERR\_ALLOC\_MEMORY\_FAILED](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示内存分配失败。

 |

#### \[h2\]OH\_CommonEvent\_GetLongFromParameters()

```c
long OH_CommonEvent_GetLongFromParameters(const CommonEvent_Parameters* para, const char* key, const long defaultValue)
```

**描述**

获取公共事件附加信息中键为key的long类型数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const [CommonEvent\_Parameters](#变量)\* para | 公共事件附加信息。 |
| const char\* key | 数据键。 |
| const long defaultValue | 默认值。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| long | 返回查询的long类型数据。 |

#### \[h2\]OH\_CommonEvent\_SetLongToParameters()

```c
CommonEvent_ErrCode OH_CommonEvent_SetLongToParameters(CommonEvent_Parameters* param, const char* key, long value)
```

**描述**

设置公共事件附加信息的long类型内容。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [CommonEvent\_Parameters](#变量)\* param | 公共事件附加信息。 |
| const char\* key | 数据键。 |
| long value | 设置的long类型内容。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
返回错误码。

返回[COMMONEVENT\_ERR\_OK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示成功。

返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示参数错误。

 |

#### \[h2\]OH\_CommonEvent\_GetLongArrayFromParameters()

```c
int32_t OH_CommonEvent_GetLongArrayFromParameters(const CommonEvent_Parameters* para, const char* key, long** array)
```

**描述**

获取公共事件附加信息的long数组内容。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const [CommonEvent\_Parameters](#变量)\* para | 公共事件附加信息。 |
| const char\* key | 数据键。 |
| long\*\* array | 查询的数组。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 返回查询的数组长度，默认值为0。 |

#### \[h2\]OH\_CommonEvent\_SetLongArrayToParameters()

```c
CommonEvent_ErrCode OH_CommonEvent_SetLongArrayToParameters(CommonEvent_Parameters* param, const char* key,const long* value, size_t num)
```

**描述**

设置公共事件附加信息的long数组内容。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [CommonEvent\_Parameters](#变量)\* param | 公共事件附加信息。 |
| const char\* key | 数据键。 |
| const long\* value | 设置的long数组内容。 |
| size\_t num | 设置的long数组内容中元素的个数。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
返回错误码。

返回[COMMONEVENT\_ERR\_OK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示成功。

返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示参数错误。

返回[COMMONEVENT\_ERR\_ALLOC\_MEMORY\_FAILED](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示内存分配失败。

 |

#### \[h2\]OH\_CommonEvent\_GetBoolFromParameters()

```c
bool OH_CommonEvent_GetBoolFromParameters(const CommonEvent_Parameters* para, const char* key, const bool defaultValue)
```

**描述**

获取公共事件附加信息中键为key的布尔类型数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const [CommonEvent\_Parameters](#变量)\* para | 公共事件附加信息。 |
| const char\* key | 数据键。 |
| const bool defaultValue | 默认值。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| bool | 返回查询的bool类型数据。 |

#### \[h2\]OH\_CommonEvent\_SetBoolToParameters()

```c
CommonEvent_ErrCode OH_CommonEvent_SetBoolToParameters(CommonEvent_Parameters* param, const char* key, bool value)
```

**描述**

设置公共事件附加信息的布尔类型内容。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [CommonEvent\_Parameters](#变量)\* param | 公共事件附加信息。 |
| const char\* key | 数据键。 |
| bool value | 设置的布尔类型内容。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
返回错误码。

返回[COMMONEVENT\_ERR\_OK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示成功。

返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示参数错误。

 |

#### \[h2\]OH\_CommonEvent\_GetBoolArrayFromParameters()

```c
int32_t OH_CommonEvent_GetBoolArrayFromParameters(const CommonEvent_Parameters* para, const char* key, bool** array)
```

**描述**

获取公共事件附加信息的布尔数组内容。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const [CommonEvent\_Parameters](#变量)\* para | 公共事件附加信息。 |
| const char\* key | 数据键。 |
| bool\*\* array | 查询的数组。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 返回查询的数组长度，默认值为0。 |

#### \[h2\]OH\_CommonEvent\_SetBoolArrayToParameters()

```c
CommonEvent_ErrCode OH_CommonEvent_SetBoolArrayToParameters(CommonEvent_Parameters* param, const char* key,const bool* value, size_t num)
```

**描述**

设置公共事件附加信息的布尔数组内容。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [CommonEvent\_Parameters](#变量)\* param | 公共事件附加信息。 |
| const char\* key | 数据键。 |
| const bool\* value | 设置的布尔数组内容。 |
| size\_t num | 设置的布尔数组内容中元素的个数。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
返回错误码。

返回[COMMONEVENT\_ERR\_OK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示成功。

返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示参数错误。

返回[COMMONEVENT\_ERR\_ALLOC\_MEMORY\_FAILED](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示内存分配失败。

 |

#### \[h2\]OH\_CommonEvent\_GetCharFromParameters()

```c
char OH_CommonEvent_GetCharFromParameters(const CommonEvent_Parameters* para, const char* key, const char defaultValue)
```

**描述**

获取公共事件附加信息中键为key的字符类型数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const [CommonEvent\_Parameters](#变量)\* para | 公共事件附加信息。 |
| const char\* key | 数据键。 |
| const char defaultValue | 默认值。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| char | 返回查询的char类型数据。 |

#### \[h2\]OH\_CommonEvent\_SetCharToParameters()

```c
CommonEvent_ErrCode OH_CommonEvent_SetCharToParameters(CommonEvent_Parameters* param, const char* key, char value)
```

**描述**

设置公共事件附加信息的字符类型内容。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [CommonEvent\_Parameters](#变量)\* param | 公共事件附加信息。 |
| const char\* key | 数据键。 |
| char value | 设置的字符类型内容。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
返回错误码。

返回[COMMONEVENT\_ERR\_OK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示成功。

返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示参数错误。

 |

#### \[h2\]OH\_CommonEvent\_GetCharArrayFromParameters()

```c
int32_t OH_CommonEvent_GetCharArrayFromParameters(const CommonEvent_Parameters* para, const char* key, char** array)
```

**描述**

获取公共事件附加信息的字符数组内容。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const [CommonEvent\_Parameters](#变量)\* para | 公共事件附加信息。 |
| const char\* key | 数据键。 |
| char\*\* array | 查询的数组。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 返回查询的数组长度，默认值为0。 |

#### \[h2\]OH\_CommonEvent\_SetCharArrayToParameters()

```c
CommonEvent_ErrCode OH_CommonEvent_SetCharArrayToParameters(CommonEvent_Parameters* param, const char* key,const char* value, size_t num)
```

**描述**

设置公共事件附加信息的字符数组内容。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [CommonEvent\_Parameters](#变量)\* param | 公共事件附加信息。 |
| const char\* key | 数据键。 |
| const char\* value | 设置的字符数组内容。 |
| size\_t num | 设置的字符数组内容中元素的个数。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
返回错误码。

返回[COMMONEVENT\_ERR\_OK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示成功。

返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示参数错误。

 |

#### \[h2\]OH\_CommonEvent\_GetDoubleFromParameters()

```c
double OH_CommonEvent_GetDoubleFromParameters(const CommonEvent_Parameters* para, const char* key,const double defaultValue)
```

**描述**

获取公共事件附加信息的double类型内容。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const [CommonEvent\_Parameters](#变量)\* para | 公共事件附加信息。 |
| const char\* key | 数据键。 |
| const double defaultValue | 默认值。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| double | 返回查询的double类型数据。 |

#### \[h2\]OH\_CommonEvent\_SetDoubleToParameters()

```c
CommonEvent_ErrCode OH_CommonEvent_SetDoubleToParameters(CommonEvent_Parameters* param, const char* key,double value)
```

**描述**

设置公共事件附加信息的double类型内容。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [CommonEvent\_Parameters](#变量)\* param | 公共事件附加信息。 |
| const char\* key | 数据键。 |
| double value | 设置的double类型内容。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
返回错误码。

返回[COMMONEVENT\_ERR\_OK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示成功。

返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示参数错误。

 |

#### \[h2\]OH\_CommonEvent\_GetDoubleArrayFromParameters()

```c
int32_t OH_CommonEvent_GetDoubleArrayFromParameters(const CommonEvent_Parameters* para, const char* key,double** array)
```

**描述**

获取公共事件附加信息中键为key的double数组数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const [CommonEvent\_Parameters](#变量)\* para | 公共事件附加信息。 |
| const char\* key | 数据键。 |
| double\*\* array | 查询的数组。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 返回查询的数组长度，默认值为0。 |

#### \[h2\]OH\_CommonEvent\_SetDoubleArrayToParameters()

```c
CommonEvent_ErrCode OH_CommonEvent_SetDoubleArrayToParameters(CommonEvent_Parameters* param, const char* key,const double* value, size_t num)
```

**描述**

设置公共事件附加信息的double数组内容。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [CommonEvent\_Parameters](#变量)\* param | 公共事件附加信息。 |
| const char\* key | 数据键。 |
| const double\* value | 设置的double数组内容。 |
| size\_t num | 设置的double数组内容中元素的个数。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
返回错误码。

返回[COMMONEVENT\_ERR\_OK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示成功。

返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示参数错误。

返回[COMMONEVENT\_ERR\_ALLOC\_MEMORY\_FAILED](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示内存分配失败。

 |

#### \[h2\]OH\_CommonEvent\_Publish()

```c
CommonEvent_ErrCode OH_CommonEvent_Publish(const char* event)
```

**描述**

发布公共事件。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const char\* event | 公共事件名称。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
返回错误码。

返回[COMMONEVENT\_ERR\_OK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示成功。

返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示参数错误。

返回[COMMONEVENT\_ERR\_SENDING\_LIMIT\_EXCEEDED](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示事件发送频率过高。

返回[COMMONEVENT\_ERR\_SENDING\_REQUEST\_FAILED](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示IPC请求发送失败。

返回[COMMONEVENT\_ERR\_INIT\_UNDONE](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示公共事件服务未初始化。

 |

#### \[h2\]OH\_CommonEvent\_PublishWithInfo()

```c
CommonEvent_ErrCode OH_CommonEvent_PublishWithInfo(const char* event, const CommonEvent_PublishInfo* info)
```

**描述**

发布带有指定属性的公共事件。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const char\* event | 公共事件名称。 |
| const [CommonEvent\_PublishInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-commonevent-publishinfo)\* info | 设置的公共事件属性。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
返回错误码。

返回[COMMONEVENT\_ERR\_OK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示成功。

返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示参数错误。

返回[COMMONEVENT\_ERR\_SENDING\_LIMIT\_EXCEEDED](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示事件发送频率过高。

返回[COMMONEVENT\_ERR\_SENDING\_REQUEST\_FAILED](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示IPC请求发送失败。

返回[COMMONEVENT\_ERR\_INIT\_UNDONE](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#commonevent_errcode)表示公共事件服务未初始化。

 |

#### \[h2\]OH\_CommonEvent\_IsOrderedCommonEvent()

```c
bool OH_CommonEvent_IsOrderedCommonEvent(const CommonEvent_Subscriber* subscriber)
```

**描述**

查询当前公共事件是否为有序公共事件。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const [CommonEvent\_Subscriber](#变量)\* subscriber | 公共事件的订阅者对象。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| bool | 返回true表示有序公共事件；返回false表示无序公共事件。 |

#### \[h2\]OH\_CommonEvent\_FinishCommonEvent()

```c
bool OH_CommonEvent_FinishCommonEvent(CommonEvent_Subscriber* subscriber)
```

**描述**

用于订阅者结束对当前有序公共事件的处理。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [CommonEvent\_Subscriber](#变量)\* subscriber | 公共事件的订阅者对象。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| bool | 返回true表示操作成功；返回false表示操作失败。 |

#### \[h2\]OH\_CommonEvent\_GetAbortCommonEvent()

```c
bool OH_CommonEvent_GetAbortCommonEvent(const CommonEvent_Subscriber* subscriber)
```

**描述**

获取当前有序公共事件是否处于中止状态。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const [CommonEvent\_Subscriber](#变量)\* subscriber | 公共事件的订阅者对象。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| bool | 返回true表示当前有序公共事件处于中止状态；返回false表示当前有序公共事件没有处于中止状态。 |

#### \[h2\]OH\_CommonEvent\_AbortCommonEvent()

```c
bool OH_CommonEvent_AbortCommonEvent(CommonEvent_Subscriber* subscriber)
```

**描述**

该接口与[OH\_CommonEvent\_FinishCommonEvent](#oh_commonevent_finishcommonevent)配合使用，可以中止当前的有序公共事件，使该公共事件不再向下一个订阅者传递。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [CommonEvent\_Subscriber](#变量)\* subscriber | 公共事件的订阅者对象。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| bool | 返回true表示操作成功；返回false表示操作失败。 |

#### \[h2\]OH\_CommonEvent\_ClearAbortCommonEvent()

```c
bool OH_CommonEvent_ClearAbortCommonEvent(CommonEvent_Subscriber* subscriber)
```

**描述**

该接口与[OH\_CommonEvent\_FinishCommonEvent](#oh_commonevent_finishcommonevent)配合使用，可以取消当前有序公共事件的中止状态，使该公共事件继续向下一个订阅者传递。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [CommonEvent\_Subscriber](#变量)\* subscriber | 公共事件的订阅者对象。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| bool | 返回true表示操作成功；返回false表示操作失败。 |

#### \[h2\]OH\_CommonEvent\_GetCodeFromSubscriber()

```c
int32_t OH_CommonEvent_GetCodeFromSubscriber(const CommonEvent_Subscriber* subscriber)
```

**描述**

获取有序公共事件传递的数据，整数类型。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const [CommonEvent\_Subscriber](#变量)\* subscriber | 公共事件的订阅者对象。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 返回有序公共事件传递的数据，整数类型，无法获取时返回0。 |

#### \[h2\]OH\_CommonEvent\_SetCodeToSubscriber()

```c
bool OH_CommonEvent_SetCodeToSubscriber(CommonEvent_Subscriber* subscriber, int32_t code)
```

**描述**

设置有序公共事件传递的数据，整数类型。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [CommonEvent\_Subscriber](#变量)\* subscriber | 公共事件的订阅者对象。 |
| int32\_t code | 有序公共事件传递的数据，整数类型。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| bool | 返回true表示操作成功；返回false表示操作失败。 |

#### \[h2\]OH\_CommonEvent\_GetDataFromSubscriber()

```c
const char* OH_CommonEvent_GetDataFromSubscriber(const CommonEvent_Subscriber* subscriber)
```

**描述**

获取有序公共事件传递的数据，字符串类型。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const [CommonEvent\_Subscriber](#变量)\* subscriber | 公共事件的订阅者对象。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| const char\* | 返回有序公共事件传递的数据，字符串类型，无法获取时返回null。 |

#### \[h2\]OH\_CommonEvent\_SetDataToSubscriber()

```c
bool OH_CommonEvent_SetDataToSubscriber(CommonEvent_Subscriber* subscriber, const char* data, size_t length)
```

**描述**

设置有序公共事件传递的数据，字符串类型。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [CommonEvent\_Subscriber](#变量)\* subscriber | 公共事件的订阅者对象。 |
| const char\* data | 有序公共事件传递的数据，字符串类型，实际有效数据长度为length与data字符串长度的较小值。 |
| size\_t length | 数据的长度。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| bool | 返回true表示操作成功；返回false表示操作失败。 |

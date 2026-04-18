---
title: "oh_pasteboard.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-pasteboard-h"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "Basic Services Kit（基础服务）"
  - "C API"
  - "头文件"
  - "oh_pasteboard.h"
captured_at: "2026-04-17T01:48:28.902Z"
---

# oh\_pasteboard.h

#### 概述

提供访问系统剪贴板的接口、数据结构、枚举类型。

**引用文件：** <database/pasteboard/oh\_pasteboard.h>

**库：** libpasteboard.so

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 13

**相关模块：** [Pasteboard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard)

#### 汇总

#### \[h2\]结构体

| 名称 | typedef关键字 | 描述 |
| :-- | :-- | :-- |
| [Pasteboard\_ProgressInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-progressinfo) | Pasteboard\_ProgressInfo | 定义进度上报的数据结构。 |
| [Pasteboard\_GetDataParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-getdataparams) | Pasteboard\_GetDataParams | 表示从剪贴板获取粘贴数据和进度时需要写入的参数。 |
| [OH\_PasteboardObserver](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboardobserver) | OH\_PasteboardObserver | 定义剪贴板数据变更观察者。 |
| [OH\_Pasteboard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboard) | OH\_Pasteboard | 定义剪贴板对象，用以操作系统剪贴板。 |

#### \[h2\]宏定义

| 名称 | 描述 |
| :-- | :-- |
| [PASTEBOARD\_MIMETYPE\_TEXT\_PLAIN](#pasteboard_mimetype_text_plain) "text/plain" | 纯文本类型。 |
| [PASTEBOARD\_MIMETYPE\_TEXT\_URI](#pasteboard_mimetype_text_uri) "text/uri" | URI类型。 |
| [PASTEBOARD\_MIMETYPE\_TEXT\_HTML](#pasteboard_mimetype_text_html) "text/html" | HTML类型。 |
| [PASTEBOARD\_MIMETYPE\_PIXELMAP](#pasteboard_mimetype_pixelmap) "pixelMap" | pixelMap类型。 |
| [PASTEBOARD\_MIMETYPE\_TEXT\_WANT](#pasteboard_mimetype_text_want) "text/want" | want类型。 |

#### \[h2\]枚举

| 名称 | typedef关键字 | 描述 |
| :-- | :-- | :-- |
| [Pasteboard\_NotifyType](#pasteboard_notifytype) | Pasteboard\_NotifyType | 剪贴板的数据变更类型。 |
| [Pasteboard\_FileConflictOptions](#pasteboard_fileconflictoptions) | Pasteboard\_FileConflictOptions | 定义文件拷贝冲突时的选项。 |
| [Pasteboard\_ProgressIndicator](#pasteboard_progressindicator) | Pasteboard\_ProgressIndicator | 定义进度条指示选项，可选择是否采用系统默认进度显示。 |

#### \[h2\]函数

| 名称 | typedef关键字 | 描述 |
| :-- | :-- | :-- |
| [typedef void (\*OH\_Pasteboard\_ProgressListener)(Pasteboard\_ProgressInfo\* progressInfo)](#oh_pasteboard_progresslistener) | OH\_Pasteboard\_ProgressListener | 用于在不使用系统默认进度显示时，通知应用拷贝粘贴任务进度。 |
| [typedef void (\*Pasteboard\_Notify)(void\* context, Pasteboard\_NotifyType type)](#pasteboard_notify) | Pasteboard\_Notify | 定义剪贴板内容变更时触发的回调函数。 |
| [typedef void (\*Pasteboard\_Finalize)(void\* context)](#pasteboard_finalize) | Pasteboard\_Finalize | 定义用于释放上下文的回调函数，剪贴板数据变更观察者对象销毁时触发。 |
| [OH\_PasteboardObserver\* OH\_PasteboardObserver\_Create()](#oh_pasteboardobserver_create) | \- | 创建一个剪贴板数据变更观察者[OH\_PasteboardObserver](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboardobserver)指针及实例对象。 |
| [int OH\_PasteboardObserver\_Destroy(OH\_PasteboardObserver\* observer)](#oh_pasteboardobserver_destroy) | \- | 销毁剪贴板数据变更观察者[OH\_PasteboardObserver](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboardobserver)指针指向的实例对象。 |
| [int OH\_PasteboardObserver\_SetData(OH\_PasteboardObserver\* observer, void\* context,const Pasteboard\_Notify callback, const Pasteboard\_Finalize finalize)](#oh_pasteboardobserver_setdata) | \- | 向剪贴板数据变更观察者设置回调函数。 |
| [OH\_Pasteboard\* OH\_Pasteboard\_Create()](#oh_pasteboard_create) | \- | 创建剪贴板[OH\_Pasteboard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboard)指针及实例对象。 |
| [void OH\_Pasteboard\_Destroy(OH\_Pasteboard\* pasteboard)](#oh_pasteboard_destroy) | \- | 销毁剪贴板[OH\_Pasteboard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboard)实例对象。 |
| [int OH\_Pasteboard\_Subscribe(OH\_Pasteboard\* pasteboard, int type, const OH\_PasteboardObserver\* observer)](#oh_pasteboard_subscribe) | \- | 订阅剪贴板的数据变更事件。 |
| [int OH\_Pasteboard\_Unsubscribe(OH\_Pasteboard\* pasteboard, int type, const OH\_PasteboardObserver\* observer)](#oh_pasteboard_unsubscribe) | \- | 取消对剪贴板数据变更事件的订阅。 |
| [bool OH\_Pasteboard\_IsRemoteData(OH\_Pasteboard\* pasteboard)](#oh_pasteboard_isremotedata) | \- | 判断剪贴板中的数据是否来自远端设备。 |
| [int OH\_Pasteboard\_GetDataSource(OH\_Pasteboard\* pasteboard, char\* source, unsigned int len)](#oh_pasteboard_getdatasource) | \- | 获取剪贴板中数据的数据源。 |
| [bool OH\_Pasteboard\_HasType(OH\_Pasteboard\* pasteboard, const char\* type)](#oh_pasteboard_hastype) | \- | 判断剪贴板中是否有指定类型的数据。 |
| [bool OH\_Pasteboard\_HasData(OH\_Pasteboard\* pasteboard)](#oh_pasteboard_hasdata) | \- | 判断剪贴板中是否有数据。 |
| [OH\_UdmfData\* OH\_Pasteboard\_GetData(OH\_Pasteboard\* pasteboard, int\* status)](#oh_pasteboard_getdata) | \- | 获取剪贴板中的数据。 |
| [int OH\_Pasteboard\_SetData(OH\_Pasteboard\* pasteboard, OH\_UdmfData\* data)](#oh_pasteboard_setdata) | \- | 将统一数据对象数据写入剪贴板。 |
| [int OH\_Pasteboard\_ClearData(OH\_Pasteboard\* pasteboard)](#oh_pasteboard_cleardata) | \- | 清空剪贴板中的数据。 |
| [char \*\*OH\_Pasteboard\_GetMimeTypes(OH\_Pasteboard \*pasteboard, unsigned int \*count)](#oh_pasteboard_getmimetypes) | \- | 获取剪贴板中的MIME类型。 |
| [Pasteboard\_GetDataParams \*OH\_Pasteboard\_GetDataParams\_Create(void)](#oh_pasteboard_getdataparams_create) | \- | 创建剪贴板[Pasteboard\_GetDataParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-getdataparams)指针及实例对象。 |
| [void OH\_Pasteboard\_GetDataParams\_Destroy(Pasteboard\_GetDataParams\* params)](#oh_pasteboard_getdataparams_destroy) | \- | 销毁剪贴板[Pasteboard\_GetDataParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-getdataparams)指针指向的实例对象。 |
| [void OH\_Pasteboard\_GetDataParams\_SetProgressIndicator(Pasteboard\_GetDataParams\* params,Pasteboard\_ProgressIndicator progressIndicator)](#oh_pasteboard_getdataparams_setprogressindicator) | \- | 向剪贴板[Pasteboard\_GetDataParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-getdataparams)设置进度条指示选项，可选择是否采用系统默认进度显示。 |
| [void OH\_Pasteboard\_GetDataParams\_SetDestUri(Pasteboard\_GetDataParams\* params, const char\* destUri, uint32\_t destUriLen)](#oh_pasteboard_getdataparams_setdesturi) | \- | 向剪贴板[Pasteboard\_GetDataParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-getdataparams)设置拷贝文件时目标路径。若不支持文件处理，则不需要设置此参数；若应用涉及复杂文件处理策略或需要区分文件多路径存储，建议不设置此参数，由应用自行完成文件copy处理。 |
| [void OH\_Pasteboard\_GetDataParams\_SetFileConflictOptions(Pasteboard\_GetDataParams\* params,Pasteboard\_FileConflictOptions option)](#oh_pasteboard_getdataparams_setfileconflictoptions) | \- | 向剪贴板[Pasteboard\_GetDataParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-getdataparams)设置文件冲突选项。 |
| [void OH\_Pasteboard\_GetDataParams\_SetProgressListener(Pasteboard\_GetDataParams\* params,const OH\_Pasteboard\_ProgressListener listener)](#oh_pasteboard_getdataparams_setprogresslistener) | \- | 向剪贴板[Pasteboard\_GetDataParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-getdataparams)设置进度上报回调函数。 |
| [int OH\_Pasteboard\_ProgressInfo\_GetProgress(Pasteboard\_ProgressInfo\* progressInfo)](#oh_pasteboard_progressinfo_getprogress) | \- | 从[Pasteboard\_ProgressInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-progressinfo)获取粘贴进度。 |
| [void OH\_Pasteboard\_ProgressCancel(Pasteboard\_GetDataParams\* params)](#oh_pasteboard_progresscancel) | \- | 定义取消函数，用于在获取粘贴数据时取消正在进行的粘贴动作。 |
| [OH\_UdmfData\* OH\_Pasteboard\_GetDataWithProgress(OH\_Pasteboard\* pasteboard, Pasteboard\_GetDataParams\* params,int\* status)](#oh_pasteboard_getdatawithprogress) | \- | 获取剪贴板的数据以及粘贴进度，不支持对文件夹的拷贝。 |
| [uint32\_t OH\_Pasteboard\_GetChangeCount(OH\_Pasteboard \*pasteboard)](#oh_pasteboard_getchangecount) | \- | 获取剪贴板内容的变化次数。 |
| [void OH\_Pasteboard\_SyncDelayedDataAsync(OH\_Pasteboard\* pasteboard, void (\*callback)(int errorCode))](#oh_pasteboard_syncdelayeddataasync) | \- | 通知剪贴板从应用同步所有延迟数据，与延迟复制接口[OH\_UdmfRecordProvider\_SetData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-udmf-h#oh_udmfrecordprovider_setdata)搭配使用。当应用使用延迟复制功能复制时，仅将应用支持的数据类型写入剪贴板。应用应在退出时，重新调用[OH\_Pasteboard\_SetData](#oh_pasteboard_setdata)接口主动提交所有复制数据或调用此接口通知剪贴板获取全量数据，等待数据同步完成再继续退出，否则可能导致其他应用粘贴获取不到数据。 |

#### 宏定义说明

#### \[h2\]PASTEBOARD\_MIMETYPE\_TEXT\_PLAIN

```c
#define PASTEBOARD_MIMETYPE_TEXT_PLAIN "text/plain"
```

**描述**

纯文本类型。

**起始版本：** 22

#### \[h2\]PASTEBOARD\_MIMETYPE\_TEXT\_URI

```c
#define PASTEBOARD_MIMETYPE_TEXT_URI "text/uri"
```

**描述**

URI类型。

**起始版本：** 22

#### \[h2\]PASTEBOARD\_MIMETYPE\_TEXT\_HTML

```c
#define PASTEBOARD_MIMETYPE_TEXT_HTML "text/html"
```

**描述**

HTML类型。

**起始版本：** 22

#### \[h2\]PASTEBOARD\_MIMETYPE\_PIXELMAP

```c
#define PASTEBOARD_MIMETYPE_PIXELMAP "pixelMap"
```

**描述**

pixelMap类型。

**起始版本：** 22

#### \[h2\]PASTEBOARD\_MIMETYPE\_TEXT\_WANT

```c
#define PASTEBOARD_MIMETYPE_TEXT_WANT "text/want"
```

**描述**

want类型。

**起始版本：** 22

#### 枚举类型说明

#### \[h2\]Pasteboard\_NotifyType

```c
enum Pasteboard_NotifyType
```

**描述：**

剪贴板的数据变更类型。

**起始版本：** 13

| 枚举项 | 描述 |
| :-- | :-- |
| NOTIFY\_LOCAL\_DATA\_CHANGE = 1 | 本地设备剪贴板数据变更。 |
| NOTIFY\_REMOTE\_DATA\_CHANGE = 2 | 组网内的非本地设备剪贴板数据变更。 |

#### \[h2\]Pasteboard\_FileConflictOptions

```c
enum Pasteboard_FileConflictOptions
```

**描述：**

定义文件拷贝冲突时的选项。

**起始版本：** 15

| 枚举项 | 描述 |
| :-- | :-- |
| PASTEBOARD\_OVERWRITE = 0 | 目标路径存在同文件名时覆盖。 |
| PASTEBOARD\_SKIP = 1 | 目标路径存在同文件名时跳过。 |

#### \[h2\]Pasteboard\_ProgressIndicator

```c
enum Pasteboard_ProgressIndicator
```

**描述：**

定义进度条指示选项，可选择是否采用系统默认进度显示。

**起始版本：** 15

| 枚举项 | 描述 |
| :-- | :-- |
| PASTEBOARD\_NONE = 0 | 不采用系统默认进度显示。 |
| PASTEBOARD\_DEFAULT = 1 | 采用系统默认进度显示。 |

#### 函数说明

#### \[h2\]OH\_Pasteboard\_ProgressListener()

```c
typedef void (*OH_Pasteboard_ProgressListener)(Pasteboard_ProgressInfo* progressInfo)
```

**描述：**

用于在不使用系统默认进度显示时，通知应用拷贝粘贴任务进度。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [Pasteboard\_ProgressInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-progressinfo)\* progressInfo | 定义进度上报的数据结构，且仅当进度指示选项[Pasteboard\_ProgressInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-progressinfo)设置为NONE时才会上报此信息。 |

#### \[h2\]Pasteboard\_Notify()

```c
typedef void (*Pasteboard_Notify)(void* context, Pasteboard_NotifyType type)
```

**描述：**

定义剪贴板内容变更时触发的回调函数。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| void\* context | 上下文信息，由函数[OH\_PasteboardObserver\_SetData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-pasteboard-h#oh_pasteboardobserver_setdata)传入。 |
| [Pasteboard\_NotifyType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-pasteboard-h#pasteboard_notifytype) type | 数据变更的类型。详见：[Pasteboard\_NotifyType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-pasteboard-h#pasteboard_notifytype)。 |

#### \[h2\]Pasteboard\_Finalize()

```c
typedef void (*Pasteboard_Finalize)(void* context)
```

**描述：**

定义用于释放上下文的回调函数，剪贴板数据变更观察者对象销毁时触发。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| void\* context | 要释放的上下文指针。 |

#### \[h2\]OH\_PasteboardObserver\_Create()

```c
OH_PasteboardObserver* OH_PasteboardObserver_Create()
```

**描述：**

创建一个剪贴板数据变更观察者[OH\_PasteboardObserver](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboardobserver)指针及实例对象。

**起始版本：** 13

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [OH\_PasteboardObserver](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboardobserver)\* | 
执行成功时返回一个指向剪贴板数据变更观察者[OH\_PasteboardObserver](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboardobserver)实例对象的指针，否则返回空指针。

当不再需要使用指针时，请使用[OH\_PasteboardObserver\_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-pasteboard-h#oh_pasteboardobserver_destroy)销毁实例对象，否则会导致内存泄漏。

 |

#### \[h2\]OH\_PasteboardObserver\_Destroy()

```c
int OH_PasteboardObserver_Destroy(OH_PasteboardObserver* observer)
```

**描述：**

销毁剪贴板数据变更观察者[OH\_PasteboardObserver](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboardobserver)指针指向的实例对象。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_PasteboardObserver](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboardobserver)\* observer | 表示指向剪贴板数据变更观察者[OH\_PasteboardObserver](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboardobserver)实例的指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int | 
返回执行的错误码。错误码定义详见[PASTEBOARD\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-pasteboard-err-code-h#pasteboard_errcode)。

若返回ERR\_OK，表示执行成功。

若返回ERR\_INVALID\_PARAMETER，表示传入了无效参数。

 |

#### \[h2\]OH\_PasteboardObserver\_SetData()

```c
int OH_PasteboardObserver_SetData(OH_PasteboardObserver* observer, void* context,const Pasteboard_Notify callback, const Pasteboard_Finalize finalize)
```

**描述：**

向剪贴板数据变更观察者设置回调函数。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_PasteboardObserver](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboardobserver)\* observer | 表示指向剪贴板数据变更观察者[OH\_PasteboardObserver](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboardobserver)实例的指针。 |
| void\* context | 表示指向上下文数据的指针，将作为第一个参数传入[Pasteboard\_Notify](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-pasteboard-h#pasteboard_notify)。 |
| const [Pasteboard\_Notify](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-pasteboard-h#pasteboard_notify) callback | 表示数据变更回调函数。详见：[Pasteboard\_Notify](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-pasteboard-h#pasteboard_notify)。 |
| const [Pasteboard\_Finalize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-pasteboard-h#pasteboard_finalize) finalize | 表示可选的回调函数，可以用于剪贴板数据变更观察者销毁时释放上下文数据。详见：[Pasteboard\_Finalize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-pasteboard-h#pasteboard_finalize)。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int | 
返回执行的错误码。错误码定义详见[PASTEBOARD\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-pasteboard-err-code-h#pasteboard_errcode)。

若返回ERR\_OK，表示执行成功。

若返回ERR\_INVALID\_PARAMETER，表示传入了无效参数。

 |

#### \[h2\]OH\_Pasteboard\_Create()

```c
OH_Pasteboard* OH_Pasteboard_Create()
```

**描述：**

创建剪贴板[OH\_Pasteboard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboard)指针及实例对象。

**起始版本：** 13

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [OH\_Pasteboard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboard)\* | 
执行成功则返回一个指向剪贴板[OH\_Pasteboard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboard)实例对象的指针，否则返回nullptr。

当不再需要使用指针时，请使用[OH\_Pasteboard\_Destroy](#oh_pasteboard_destroy)销毁实例对象，否则会导致内存泄漏。

 |

#### \[h2\]OH\_Pasteboard\_Destroy()

```c
void OH_Pasteboard_Destroy(OH_Pasteboard* pasteboard)
```

**描述：**

销毁剪贴板[OH\_Pasteboard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboard)实例对象。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_Pasteboard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboard)\* pasteboard | 表示指向剪贴板[OH\_Pasteboard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboard)实例的指针。 |

#### \[h2\]OH\_Pasteboard\_Subscribe()

```c
int OH_Pasteboard_Subscribe(OH_Pasteboard* pasteboard, int type, const OH_PasteboardObserver* observer)
```

**描述：**

订阅剪贴板的数据变更事件。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_Pasteboard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboard)\* pasteboard | 表示指向剪贴板[OH\_Pasteboard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboard)实例的指针。 |
| int type | 表示订阅的剪贴板数据变更类型，详见：[Pasteboard\_NotifyType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-pasteboard-h#pasteboard_notifytype)。 |
| const [OH\_PasteboardObserver](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboardobserver)\* observer | 表示指向剪贴板数据变更观察者[OH\_PasteboardObserver](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboardobserver)实例的指针。它指定了剪贴板数据变更时触发的回调函数，详见：[OH\_PasteboardObserver](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboardobserver)。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int | 
返回执行的错误码。错误码定义详见[PASTEBOARD\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-pasteboard-err-code-h#pasteboard_errcode)。

若返回ERR\_OK，表示执行成功。

若返回ERR\_INVALID\_PARAMETER，表示传入了无效参数。

 |

#### \[h2\]OH\_Pasteboard\_Unsubscribe()

```c
int OH_Pasteboard_Unsubscribe(OH_Pasteboard* pasteboard, int type, const OH_PasteboardObserver* observer)
```

**描述：**

取消对剪贴板数据变更事件的订阅。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_Pasteboard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboard)\* pasteboard | 表示指向剪贴板[OH\_Pasteboard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboard)实例的指针。 |
| int type | 表示订阅的剪贴板数据变更类型，详见：[Pasteboard\_NotifyType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-pasteboard-h#pasteboard_notifytype)。 |
| const [OH\_PasteboardObserver](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboardobserver)\* observer | 表示指向剪贴板数据变更观察者[OH\_PasteboardObserver](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboardobserver)实例的指针。它指定了剪贴板数据变更时触发的回调函数，详见：[OH\_PasteboardObserver](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboardobserver)。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int | 
返回执行的错误码。错误码定义详见[PASTEBOARD\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-pasteboard-err-code-h#pasteboard_errcode)。

若返回ERR\_OK，表示执行成功。

若返回ERR\_INVALID\_PARAMETER，表示传入了无效参数。

 |

#### \[h2\]OH\_Pasteboard\_IsRemoteData()

```c
bool OH_Pasteboard_IsRemoteData(OH_Pasteboard* pasteboard)
```

**描述：**

判断剪贴板中的数据是否来自远端设备。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_Pasteboard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboard)\* pasteboard | 表示指向剪贴板[OH\_Pasteboard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboard)实例的指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| bool | 返回剪贴板中的数据是否来自远端设备。返回true表示剪贴板中的数据来自远端设备，返回false表示剪贴板中数据来自本端设备。 |

#### \[h2\]OH\_Pasteboard\_GetDataSource()

```c
int OH_Pasteboard_GetDataSource(OH_Pasteboard* pasteboard, char* source, unsigned int len)
```

**描述：**

获取剪贴板中数据的数据源。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_Pasteboard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboard)\* pasteboard | 表示指向剪贴板[OH\_Pasteboard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboard)实例的指针。 |
| char\* source | 表示用于存放剪贴板数据源实例的指针，开发者需在调用接口前申请指针指向的内存。 |
| unsigned int len | 表示source指针对应的内存长度，当内存长度不足时调用接口会失败，建议长度：128字节。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int | 
返回执行的错误码。错误码定义详见[PASTEBOARD\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-pasteboard-err-code-h#pasteboard_errcode)。

若返回ERR\_OK，表示执行成功。

若返回ERR\_INVALID\_PARAMETER，表示传入了无效参数。

 |

#### \[h2\]OH\_Pasteboard\_HasType()

```c
bool OH_Pasteboard_HasType(OH_Pasteboard* pasteboard, const char* type)
```

**描述：**

判断剪贴板中是否有指定类型的数据。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_Pasteboard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboard)\* pasteboard | 表示指向剪贴板[OH\_Pasteboard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboard)实例的指针。 |
| const char\* type | 表示要检查的数据类型。包含剪贴板基础数据类型与自定义数据类型，其中剪贴板基础数据类型有："text/plain"、"text/html"、"text/uri"、"text/want"和"pixelMap"，详见[宏定义](#宏定义)。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| bool | 返回剪贴板中是否有指定类型的数据。返回true表示剪贴板中包含指定类型的数据，返回false表示剪贴板中没有指定类型的数据。 |

#### \[h2\]OH\_Pasteboard\_HasData()

```c
bool OH_Pasteboard_HasData(OH_Pasteboard* pasteboard)
```

**描述：**

判断剪贴板中是否有数据。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_Pasteboard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboard)\* pasteboard | 表示指向剪贴板[OH\_Pasteboard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboard)实例的指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| bool | 返回剪贴板中是否有数据。返回true表示剪贴板中有数据，返回false表示剪贴板中没有数据。 |

#### \[h2\]OH\_Pasteboard\_GetData()

```c
OH_UdmfData* OH_Pasteboard_GetData(OH_Pasteboard* pasteboard, int* status)
```

**描述：**

获取剪贴板中的数据。

**起始版本：** 13

**需要权限**：ohos.permission.READ\_PASTEBOARD，应用访问剪贴板内容需[申请访问剪贴板权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/get-pastedata-permission-guidelines)。[使用粘贴控件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pastebutton)访问剪贴板内容的应用，可以无需申请权限。

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_Pasteboard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboard)\* pasteboard | 表示指向剪贴板[OH\_Pasteboard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboard)实例的指针。 |
| int\* status | 该参数是输出参数，表示执行的错误码。错误码定义详见[PASTEBOARD\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-pasteboard-err-code-h#pasteboard_errcode)。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [OH\_UdmfData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-udmf-oh-udmfdata)\* | 执行成功时返回统一数据对象[OH\_UdmfData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-udmf-oh-udmfdata)实例的指针。否则返回空指针。 |

#### \[h2\]OH\_Pasteboard\_SetData()

```c
int OH_Pasteboard_SetData(OH_Pasteboard* pasteboard, OH_UdmfData* data)
```

**描述：**

将统一数据对象数据写入剪贴板。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_Pasteboard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboard)\* pasteboard | 表示指向剪贴板[OH\_Pasteboard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboard)实例的指针。 |
| [OH\_UdmfData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-udmf-oh-udmfdata)\* data | 表示指向统一数据对象[OH\_UdmfData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-udmf-oh-udmfdata)实例的指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int | 
返回执行的错误码。错误码定义详见[PASTEBOARD\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-pasteboard-err-code-h#pasteboard_errcode)。

若返回ERR\_OK，表示执行成功。

若返回ERR\_INVALID\_PARAMETER，表示传入了无效参数。

 |

#### \[h2\]OH\_Pasteboard\_ClearData()

```c
int OH_Pasteboard_ClearData(OH_Pasteboard* pasteboard)
```

**描述：**

清空剪贴板中的数据。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_Pasteboard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboard)\* pasteboard | 表示指向剪贴板[OH\_Pasteboard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboard)实例的指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int | 
返回执行的错误码。错误码定义详见[PASTEBOARD\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-pasteboard-err-code-h#pasteboard_errcode)。

若返回ERR\_OK，表示执行成功。

若返回ERR\_INVALID\_PARAMETER，表示传入了无效参数。

 |

#### \[h2\]OH\_Pasteboard\_GetMimeTypes()

```c
char **OH_Pasteboard_GetMimeTypes(OH_Pasteboard *pasteboard, unsigned int *count)
```

**描述：**

获取剪贴板中的MIME类型。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_Pasteboard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboard) \*pasteboard | 表示指向剪贴板[OH\_Pasteboard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboard)实例的指针。 |
| unsigned int \*count | 该参数是输出参数，结果集中的类型数量会写入该变量。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| char \*\* | 执行成功时返回剪贴板所有内容的MIME类型，否则返回nullptr。 |

#### \[h2\]OH\_Pasteboard\_GetDataParams\_Create()

```c
Pasteboard_GetDataParams *OH_Pasteboard_GetDataParams_Create(void)
```

**描述：**

创建剪贴板[Pasteboard\_GetDataParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-getdataparams)指针及实例对象。

**起始版本：** 15

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [Pasteboard\_GetDataParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-getdataparams)\* | 
执行成功时返回一个指向剪贴板[Pasteboard\_GetDataParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-getdataparams)实例对象的指针，否则返回空指针。

当不再需要使用指针时，请使用[OH\_Pasteboard\_GetDataParams\_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-pasteboard-h#oh_pasteboard_getdataparams_destroy)销毁实例对象，否则会导致内存泄漏。

 |

#### \[h2\]OH\_Pasteboard\_GetDataParams\_Destroy()

```c
void OH_Pasteboard_GetDataParams_Destroy(Pasteboard_GetDataParams* params)
```

**描述：**

销毁剪贴板[Pasteboard\_GetDataParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-getdataparams)指针指向的实例对象。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [Pasteboard\_GetDataParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-getdataparams) \* params | 表示指向剪贴板OH\_Pasteboard\_GetDataParams的指针。 |

#### \[h2\]OH\_Pasteboard\_GetDataParams\_SetProgressIndicator()

```c
void OH_Pasteboard_GetDataParams_SetProgressIndicator(Pasteboard_GetDataParams* params,Pasteboard_ProgressIndicator progressIndicator)
```

**描述：**

向剪贴板[Pasteboard\_GetDataParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-getdataparams)设置进度条指示选项，可选择是否采用系统默认进度显示。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [Pasteboard\_GetDataParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-getdataparams)\* params | 表示指向剪贴板OH\_Pasteboard\_GetDataParams的指针。 |
| [Pasteboard\_ProgressIndicator](#pasteboard_progressindicator) progressIndicator | 定义进度条指示选项。 |

#### \[h2\]OH\_Pasteboard\_GetDataParams\_SetDestUri()

```c
void OH_Pasteboard_GetDataParams_SetDestUri(Pasteboard_GetDataParams* params, const char* destUri, uint32_t destUriLen)
```

**描述：**

设置拷贝文件时目标路径。若不支持文件处理，则不需要设置此参数；若应用涉及复杂文件处理策略或需要区分文件多路径存储，建议不设置此参数，由应用自行完成文件copy处理。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [Pasteboard\_GetDataParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-getdataparams)\* params | 表示指向剪贴板OH\_Pasteboard\_GetDataParams的指针。 |
| const char\* destUri | 定义拷贝文件目标路径。 |
| uint32\_t destUriLen | 定义拷贝文件目标路径长度。 |

#### \[h2\]OH\_Pasteboard\_GetDataParams\_SetFileConflictOptions()

```c
void OH_Pasteboard_GetDataParams_SetFileConflictOptions(Pasteboard_GetDataParams* params,Pasteboard_FileConflictOptions option)
```

**描述：**

向剪贴板[Pasteboard\_GetDataParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-getdataparams)设置文件冲突选项。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [Pasteboard\_GetDataParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-getdataparams)\* params | 表示指向剪贴板OH\_Pasteboard\_GetDataParams的指针。 |
| [Pasteboard\_FileConflictOptions](#pasteboard_fileconflictoptions) option | 定义文件拷贝冲突时的选项，默认为PASTEBOARD\_OVERWRITE。 |

#### \[h2\]OH\_Pasteboard\_GetDataParams\_SetProgressListener()

```c
void OH_Pasteboard_GetDataParams_SetProgressListener(Pasteboard_GetDataParams* params,const OH_Pasteboard_ProgressListener listener)
```

**描述：**

向剪贴板[Pasteboard\_GetDataParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-getdataparams)设置进度上报回调函数。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [Pasteboard\_GetDataParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-getdataparams)\* params | 表示指向剪贴板OH\_Pasteboard\_GetDataParams的指针。 |
| const [OH\_Pasteboard\_ProgressListener](#oh_pasteboard_progresslistener) listener | 表示进度上报回调函数。 |

#### \[h2\]OH\_Pasteboard\_ProgressInfo\_GetProgress()

```c
int OH_Pasteboard_ProgressInfo_GetProgress(Pasteboard_ProgressInfo* progressInfo)
```

**描述：**

从[Pasteboard\_ProgressInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-progressinfo)获取粘贴进度。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [Pasteboard\_ProgressInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-progressinfo)\* progressInfo | 表示指向剪贴板[Pasteboard\_ProgressInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-progressinfo)的指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int | 返回粘贴进度百分比。 |

#### \[h2\]OH\_Pasteboard\_ProgressCancel()

```c
void OH_Pasteboard_ProgressCancel(Pasteboard_GetDataParams* params)
```

**描述：**

定义取消函数，用于在获取粘贴数据时取消正在进行的粘贴动作。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [Pasteboard\_GetDataParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-getdataparams)\* params | 表示指向剪贴板OH\_Pasteboard\_GetDataParams的指针。 |

#### \[h2\]OH\_Pasteboard\_GetDataWithProgress()

```c
OH_UdmfData* OH_Pasteboard_GetDataWithProgress(OH_Pasteboard* pasteboard, Pasteboard_GetDataParams* params,int* status)
```

**描述：**

获取剪贴板的数据以及粘贴进度，不支持对文件夹的拷贝。

**起始版本：** 15

**需要权限**：ohos.permission.READ\_PASTEBOARD，应用访问剪贴板内容需[申请访问剪贴板权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/get-pastedata-permission-guidelines)。[使用粘贴控件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pastebutton)访问剪贴板内容的应用，可以无需申请权限。

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_Pasteboard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboard)\* pasteboard | 表示指向剪贴板[OH\_Pasteboard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboard)实例的指针。 |
| [Pasteboard\_GetDataParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-getdataparams)\* params | 表示指向剪贴板OH\_Pasteboard\_GetDataParams的指针。 |
| int\* status | 该参数是输出参数，表示执行的错误码。错误码定义详见[PASTEBOARD\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-pasteboard-err-code-h#pasteboard_errcode)。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [OH\_UdmfData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-udmf-oh-udmfdata)\* | 执行成功时返回统一数据对象OH\_UdmfData实例的指针。否则返回空指针。 |

#### \[h2\]OH\_Pasteboard\_GetChangeCount()

```c
uint32_t OH_Pasteboard_GetChangeCount(OH_Pasteboard *pasteboard)
```

**描述：**

获取剪贴板内容的变化次数。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_Pasteboard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboard) \*pasteboard | 表示指向剪贴板[OH\_Pasteboard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboard)实例的指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| uint32\_t | 
执行成功时返回剪贴板内容的变化次数，否则返回0。

当剪贴板内容过期或调用OH\_Pasteboard\_ClearData等接口导致剪贴板内容为空时，内容变化次数不会因此改变。

系统重启或剪贴板服务异常重启时，剪贴板内容变化次数重新从0开始计数。对同一内容连续多次复制会被视作多次更改，每次复制均会导致内容变化次数增加。

 |

#### \[h2\]OH\_Pasteboard\_SyncDelayedDataAsync()

```c
void OH_Pasteboard_SyncDelayedDataAsync(OH_Pasteboard* pasteboard, void (*callback)(int errorCode))
```

**描述：**

通知剪贴板从应用同步所有延迟数据，与延迟复制接口[OH\_UdmfRecordProvider\_SetData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-udmf-h#oh_udmfrecordprovider_setdata)搭配使用。当应用使用延迟复制功能复制时，仅将应用支持的数据类型写入剪贴板。应用应在退出时，重新调用[OH\_Pasteboard\_SetData](#oh_pasteboard_setdata)接口主动提交所有复制数据或调用此接口通知剪贴板获取全量数据，等待数据同步完成再继续退出，否则可能导致其他应用粘贴获取不到数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/Y33UrAsfTCGPkI414W6vqA/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014830Z&HW-CC-Expire=86400&HW-CC-Sign=A5B42B47206CEAD5B9C9D94CC20DBC4D417E572EBD4CA30358A844B09D03DC9C)

-   调用此接口会延长退出过程，建议应用直接设置数据到剪贴板，而不是调用延迟复制接口[OH\_UdmfRecordProvider\_SetData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-udmf-h#oh_udmfrecordprovider_setdata)和此接口。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_Pasteboard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboard) \*pasteboard | 表示指向剪贴板[OH\_Pasteboard](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pasteboard-oh-pasteboard)实例的指针。 |
| void (\*callback)(int errorCode) | 数据同步完成后调用的回调函数指针，errorCode表示同步任务的结果，错误码定义详见[PASTEBOARD\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-pasteboard-err-code-h#pasteboard_errcode)。 |

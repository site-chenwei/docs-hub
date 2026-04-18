---
title: "native_mediakeysession.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-mediakeysession-h"
menu_path:
  - "参考"
  - "媒体"
  - "DRM Kit（数字版权保护服务）"
  - "C API"
  - "头文件"
  - "native_mediakeysession.h"
captured_at: "2026-04-17T01:48:40.497Z"
---

# native\_mediakeysession.h

#### 概述

定义Drm MediaKeySession API。提供以下功能：

生成媒体密钥请求、处理媒体密钥响应、事件监听、获取内容保护级别、检查媒体密钥状态、删除媒体密钥等。

**引用文件：** <multimedia/drm\_framework/native\_mediakeysession.h>

**库：** libnative\_drm.so

**系统能力：** SystemCapability.Multimedia.Drm.Core

**起始版本：** 11

**相关模块：** [Drm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm)

#### 汇总

#### \[h2\]结构体

| 名称 | typedef关键字 | 描述 |
| :-- | :-- | :-- |
| [MediaKeySession\_Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-mediakeysession-callback) | MediaKeySession\_Callback | MediaKeySession\_Callback结构体，用于监听密钥过期、密钥更改等事件，不返回媒体密钥会话实例，适用于单媒体密钥会话解密场景。 |
| [OH\_MediaKeySession\_Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-oh-mediakeysession-callback) | OH\_MediaKeySession\_Callback | OH\_MediaKeySession\_Callback结构体，用于监听密钥过期、密钥更改等事件，返回媒体密钥会话实例，适用多个媒体密钥会话解密场景。 |

#### \[h2\]函数

| 名称 | typedef关键字 | 描述 |
| :-- | :-- | :-- |
| [typedef Drm\_ErrCode (\*MediaKeySession\_EventCallback)(DRM\_EventType eventType, uint8\_t \*info,int32\_t infoLen, char \*extra)](#mediakeysession_eventcallback) | MediaKeySession\_EventCallback | MediaKeySession事件触发时将调用的回调，如密钥过期事件。 |
| [typedef Drm\_ErrCode (\*MediaKeySession\_KeyChangeCallback)(DRM\_KeysInfo \*keysInfo, bool newKeysAvailable)](#mediakeysession_keychangecallback) | MediaKeySession\_KeyChangeCallback | 密钥变更时将调用回调。 |
| [typedef Drm\_ErrCode (\*OH\_MediaKeySession\_EventCallback)(MediaKeySession \*mediaKeySession, DRM\_EventType eventType,uint8\_t \*info, int32\_t infoLen, char \*extra)](#oh_mediakeysession_eventcallback) | OH\_MediaKeySession\_EventCallback | 事件触发时将调用的回调。 |
| [typedef Drm\_ErrCode (\*OH\_MediaKeySession\_KeyChangeCallback)(MediaKeySession \*mediaKeySession, DRM\_KeysInfo \*keysInfo, bool newKeysAvailable)](#oh_mediakeysession_keychangecallback) | OH\_MediaKeySession\_KeyChangeCallback | 密钥变更时将调用的回调。 |
| [Drm\_ErrCode OH\_MediaKeySession\_GenerateMediaKeyRequest(MediaKeySession \*mediaKeySession, DRM\_MediaKeyRequestInfo \*info, DRM\_MediaKeyRequest \*mediaKeyRequest)](#oh_mediakeysession_generatemediakeyrequest) | \- | 生成媒体密钥请求。 |
| [Drm\_ErrCode OH\_MediaKeySession\_ProcessMediaKeyResponse(MediaKeySession \*mediaKeySession, uint8\_t \*response, int32\_t responseLen, uint8\_t \*offlineMediaKeyId, int32\_t \*offlineMediaKeyIdLen)](#oh_mediakeysession_processmediakeyresponse) | \- | 处理媒体密钥请求响应。 |
| [Drm\_ErrCode OH\_MediaKeySession\_CheckMediaKeyStatus(MediaKeySession \*mediaKeySession, DRM\_MediaKeyStatus \*mediaKeyStatus)](#oh_mediakeysession_checkmediakeystatus) | \- | 检查媒体密钥状态。 |
| [Drm\_ErrCode OH\_MediaKeySession\_ClearMediaKeys(MediaKeySession \*mediaKeySession)](#oh_mediakeysession_clearmediakeys) | \- | 清除当前会话的媒体密钥。 |
| [Drm\_ErrCode OH\_MediaKeySession\_GenerateOfflineReleaseRequest(MediaKeySession \*mediaKeySession, uint8\_t \*offlineMediaKeyId, int32\_t offlineMediaKeyIdLen, uint8\_t \*releaseRequest,int32\_t \*releaseRequestLen)](#oh_mediakeysession_generateofflinereleaserequest) | \- | 生成离线媒体密钥释放请求。 |
| [Drm\_ErrCode OH\_MediaKeySession\_ProcessOfflineReleaseResponse(MediaKeySession \*mediaKeySession, uint8\_t \*offlineMediaKeyId, int32\_t offlineMediaKeyIdLen, uint8\_t \*releaseResponse,int32\_t releaseResponseLen)](#oh_mediakeysession_processofflinereleaseresponse) | \- | 处理离线媒体密钥释放请求响应。 |
| [Drm\_ErrCode OH\_MediaKeySession\_RestoreOfflineMediaKeys(MediaKeySession \*mediaKeySession, uint8\_t \*offlineMediaKeyId, int32\_t offlineMediaKeyIdLen)](#oh_mediakeysession_restoreofflinemediakeys) | \- | 恢复离线媒体密钥到当前会话。 |
| [Drm\_ErrCode OH\_MediaKeySession\_GetContentProtectionLevel(MediaKeySession \*mediaKeySession, DRM\_ContentProtectionLevel \*contentProtectionLevel)](#oh_mediakeysession_getcontentprotectionlevel) | \- | 获取会话的内容保护级别。 |
| [Drm\_ErrCode OH\_MediaKeySession\_RequireSecureDecoderModule(MediaKeySession \*mediaKeySession, const char \*mimeType, bool \*status)](#oh_mediakeysession_requiresecuredecodermodule) | \- | 是否需要安全解码。 |
| [Drm\_ErrCode OH\_MediaKeySession\_SetMediaKeySessionCallback(MediaKeySession \*mediaKeySession, MediaKeySession\_Callback \*callback)](#oh_mediakeysession_setmediakeysessioncallback) | \- | 设置MediaKeySession事件回调。 |
| [Drm\_ErrCode OH\_MediaKeySession\_SetCallback(MediaKeySession \*mediaKeySession, OH\_MediaKeySession\_Callback \*callback)](#oh_mediakeysession_setcallback) | \- | 设置MediaKeySession事件回调。 |
| [Drm\_ErrCode OH\_MediaKeySession\_Destroy(MediaKeySession \*mediaKeySession)](#oh_mediakeysession_destroy) | \- | 销毁MediaKeySession实例。 |

#### 函数说明

#### \[h2\]MediaKeySession\_EventCallback()

```c
typedef  Drm_ErrCode (*MediaKeySession_EventCallback)(DRM_EventType eventType, uint8_t *info,int32_t infoLen, char *extra)
```

**描述**

MediaKeySession事件触发时将调用的回调，如密钥过期事件。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [DRM\_EventType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-common-h#drm_eventtype) eventType | 事件类型。 |
| uint8\_t \*info | 从媒体密钥会话获取的事件信息。 |
| int32\_t infoLen | 事件信息长度。 |
| char \*extra | 从媒体密钥会话中获得的额外信息。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [Drm\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-err-h#drm_errcode) | 错误码。 |

#### \[h2\]MediaKeySession\_KeyChangeCallback()

```c
typedef  Drm_ErrCode (*MediaKeySession_KeyChangeCallback)(DRM_KeysInfo *keysInfo, bool newKeysAvailable)
```

**描述**

密钥变更时将调用回调。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [DRM\_KeysInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-keysinfo) \*keysInfo | 密钥信息。 |
| bool newKeysAvailable | 新密钥是否可用，true表示可用，false表示不可用。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [Drm\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-err-h#drm_errcode) | 
DRM\_ERR\_OK：执行成功。

DRM\_ERR\_INVALID\_VAL：参数检查失败。

 |

#### \[h2\]OH\_MediaKeySession\_EventCallback()

```c
typedef Drm_ErrCode (*OH_MediaKeySession_EventCallback)(MediaKeySession *mediaKeySession, DRM_EventType eventType,uint8_t *info, int32_t infoLen, char *extra)
```

**描述**

事件触发时将调用的回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [MediaKeySession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-mediakeysession) \*mediaKeySession | 会话实例。 |
| [DRM\_EventType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-common-h#drm_eventtype) eventType | 事件类型。 |
| uint8\_t \*info | 事件信息。 |
| int32\_t infoLen | 事件信息长度。 |
| char \*extra | 增量信息。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [Drm\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-err-h#drm_errcode) | 错误码。 |

#### \[h2\]OH\_MediaKeySession\_KeyChangeCallback()

```c
typedef Drm_ErrCode (*OH_MediaKeySession_KeyChangeCallback)(MediaKeySession *mediaKeySession, DRM_KeysInfo *keysInfo,bool newKeysAvailable)
```

**描述**

密钥变更时将调用的回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [MediaKeySession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-mediakeysession) \*mediaKeySession | 媒体密钥会话实例。 |
| [DRM\_KeysInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-keysinfo) \*keysInfo | 密钥信息。 |
| bool newKeysAvailable | 新密钥是否可用，true表示可用，false表示不可用。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [Drm\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-err-h#drm_errcode) | 
DRM\_ERR\_OK：执行成功。

DRM\_ERR\_INVALID\_VAL：参数检查失败。

 |

#### \[h2\]OH\_MediaKeySession\_GenerateMediaKeyRequest()

```c
Drm_ErrCode OH_MediaKeySession_GenerateMediaKeyRequest(MediaKeySession *mediaKeySession,DRM_MediaKeyRequestInfo *info, DRM_MediaKeyRequest *mediaKeyRequest)
```

**描述**

生成媒体密钥请求。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [MediaKeySession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-mediakeysession) \*mediaKeySession | MediaKeySession实例。 |
| [DRM\_MediaKeyRequestInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-mediakeyrequestinfo) \*info | 媒体密钥请求信息。 |
| [DRM\_MediaKeyRequest](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-mediakeyrequest) \*mediaKeyRequest | 媒体密钥请求。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [Drm\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-err-h#drm_errcode) | 
DRM\_ERR\_OK：执行成功。

DRM\_ERR\_NO\_MEMORY：内存不足，内存分配失败。

DRM\_ERR\_INVALID\_VAL：输入参数mediaKeySession为空指针或无效，或输入参数info为空指针，或输入参数mediaKeyRequest为空指针。

DRM\_ERR\_UNKNOWN：发生内部错误，请查看日志详细信息。

 |

#### \[h2\]OH\_MediaKeySession\_ProcessMediaKeyResponse()

```c
Drm_ErrCode OH_MediaKeySession_ProcessMediaKeyResponse(MediaKeySession *mediaKeySession,uint8_t *response, int32_t responseLen, uint8_t *offlineMediaKeyId, int32_t *offlineMediaKeyIdLen)
```

**描述**

处理媒体密钥请求响应。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [MediaKeySession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-mediakeysession) \*mediaKeySession | MediaKeySession实例。 |
| uint8\_t \*response | 媒体密钥请求响应。 |
| int32\_t responseLen | 媒体密钥请求响应长度。 |
| uint8\_t \*offlineMediaKeyId | 离线媒体密钥标识。 |
| int32\_t \*offlineMediaKeyIdLen | 离线媒体密钥标识的长度。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [Drm\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-err-h#drm_errcode) | 
DRM\_ERR\_OK：执行成功。

DRM\_ERR\_NO\_MEMORY：内存不足，内存分配失败。

DRM\_ERR\_INVALID\_VAL：输入参数mediaKeySession为空指针或无效，或其它指针类型输入参数为空指针。

DRM\_ERR\_UNKNOWN：发生内部错误，请查看日志详细信息。

 |

#### \[h2\]OH\_MediaKeySession\_CheckMediaKeyStatus()

```c
Drm_ErrCode OH_MediaKeySession_CheckMediaKeyStatus(MediaKeySession *mediaKeySession,DRM_MediaKeyStatus *mediaKeyStatus)
```

**描述**

检查媒体密钥状态。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [MediaKeySession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-mediakeysession) \*mediaKeySession | MediaKeySession实例。 |
| [DRM\_MediaKeyStatus](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-mediakeystatus) \*mediaKeyStatus | 媒体密钥状态。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [Drm\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-err-h#drm_errcode) | 
DRM\_ERR\_OK：执行成功。

DRM\_ERR\_NO\_MEMORY：内存不足，内存分配失败。

DRM\_ERR\_INVALID\_VAL：输入参数mediaKeySession为空指针或无效，或输入参数mediaKeyStatus为空指针。

DRM\_ERR\_UNKNOWN：发生内部错误，请查看日志详细信息。

 |

#### \[h2\]OH\_MediaKeySession\_ClearMediaKeys()

```c
Drm_ErrCode OH_MediaKeySession_ClearMediaKeys(MediaKeySession *mediaKeySession)
```

**描述**

清除当前会话的媒体密钥。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [MediaKeySession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-mediakeysession) \*mediaKeySession | MediaKeySession实例。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [Drm\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-err-h#drm_errcode) | 
DRM\_ERR\_OK：执行成功。

DRM\_ERR\_INVALID\_VAL：输入参数mediaKeySession为空指针或无效。

DRM\_ERR\_UNKNOWN：发生内部错误，请查看日志详细信息。

 |

#### \[h2\]OH\_MediaKeySession\_GenerateOfflineReleaseRequest()

```c
Drm_ErrCode OH_MediaKeySession_GenerateOfflineReleaseRequest(MediaKeySession *mediaKeySession,uint8_t *offlineMediaKeyId, int32_t offlineMediaKeyIdLen, uint8_t *releaseRequest,int32_t *releaseRequestLen)
```

**描述**

生成离线媒体密钥释放请求。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [MediaKeySession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-mediakeysession) \*mediaKeySession | MediaKeySession实例。 |
| uint8\_t \*offlineMediaKeyId | 离线媒体密钥标识。 |
| int32\_t \*releaseRequestLen | 离线媒体密钥标识长度。 |
| uint8\_t \*releaseRequest | 离线媒体密钥释放请求。 |
| int32\_t \*releaseRequestLen | 离线媒体密钥释放请求长度。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [Drm\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-err-h#drm_errcode) | 
DRM\_ERR\_OK：执行成功。

DRM\_ERR\_NO\_MEMORY：内存不足，内存分配失败。

DRM\_ERR\_INVALID\_VAL：输入参数mediaKeySession为空指针或无效，或其它指针类型输入参数为空指针。

DRM\_ERR\_UNKNOWN：发生内部错误或设备上的DRM解决方案不支持离线媒体密钥释放，请查看日志详细信息。

 |

#### \[h2\]OH\_MediaKeySession\_ProcessOfflineReleaseResponse()

```c
Drm_ErrCode OH_MediaKeySession_ProcessOfflineReleaseResponse(MediaKeySession *mediaKeySession,uint8_t *offlineMediaKeyId, int32_t offlineMediaKeyIdLen, uint8_t *releaseResponse,int32_t releaseResponseLen)
```

**描述**

处理离线媒体密钥释放请求响应。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [MediaKeySession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-mediakeysession) \*mediaKeySession | MediaKeySession实例。 |
| uint8\_t \*offlineMediaKeyId | 离线媒体密钥标识。 |
| int32\_t offlineMediaKeyIdLen | 离线媒体密钥标识长度。 |
| uint8\_t \*releaseResponse | 媒体密钥释放请求响应。 |
| int32\_t releaseResponseLen | 媒体密钥释放请求响应长度。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [Drm\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-err-h#drm_errcode) | 
DRM\_ERR\_OK：执行成功。

DRM\_ERR\_INVALID\_VAL：输入参数mediaKeySession为空指针或无效，或其它指针类型输入参数为空指针。

DRM\_ERR\_UNKNOWN：发生内部错误或设备上的DRM解决方案不支持离线媒体密钥释放，请查看日志详细信息。

 |

#### \[h2\]OH\_MediaKeySession\_RestoreOfflineMediaKeys()

```c
Drm_ErrCode OH_MediaKeySession_RestoreOfflineMediaKeys(MediaKeySession *mediaKeySession,uint8_t *offlineMediaKeyId, int32_t offlineMediaKeyIdLen)
```

**描述**

恢复离线媒体密钥到当前会话。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [MediaKeySession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-mediakeysession) \*mediaKeySession | MediaKeySession实例。 |
| uint8\_t \*offlineMediaKeyId | 离线媒体密钥标识。 |
| int32\_t offlineMediaKeyIdLen | 离线媒体密钥标识长度。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [Drm\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-err-h#drm_errcode) | 
DRM\_ERR\_OK：执行成功。

DRM\_ERR\_INVALID\_VAL：输入参数mediaKeySession为空指针或无效，或其它指针类型输入参数为空指针。

DRM\_ERR\_UNKNOWN：发生内部错误，请查看日志详细信息。

 |

#### \[h2\]OH\_MediaKeySession\_GetContentProtectionLevel()

```c
Drm_ErrCode OH_MediaKeySession_GetContentProtectionLevel(MediaKeySession *mediaKeySession,DRM_ContentProtectionLevel *contentProtectionLevel)
```

**描述**

获取会话的内容保护级别。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [MediaKeySession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-mediakeysession) \*mediaKeySession | MediaKeySession实例。 |
| [DRM\_ContentProtectionLevel](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-common-h#drm_contentprotectionlevel) \*contentProtectionLevel | 内容保护级别。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [Drm\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-err-h#drm_errcode) | 
DRM\_ERR\_OK：执行成功。

DRM\_ERR\_INVALID\_VAL：输入参数mediaKeySession为空指针或无效，或输入参数contentProtectionLevel为空指针。

DRM\_ERR\_UNKNOWN：发生内部错误，请查看日志详细信息。

 |

#### \[h2\]OH\_MediaKeySession\_RequireSecureDecoderModule()

```c
Drm_ErrCode OH_MediaKeySession_RequireSecureDecoderModule(MediaKeySession *mediaKeySession,const char *mimeType, bool *status)
```

**描述**

是否需要安全解码。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [MediaKeySession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-mediakeysession) \*mediaKeySession | MediaKeySession实例。 |
| const char \*mimeType | 媒体类型，支持的媒体类型取决于DRM解决方案，如：video/avc、video/hev。 |
| bool \*status | 安全解码模块状态。true表示需要安全解码模块，false表示不需要安全解码模块。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [Drm\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-err-h#drm_errcode) | 
DRM\_ERR\_OK：执行成功。

DRM\_ERR\_INVALID\_VAL：输入参数mediaKeySession为空指针或无效，或其它指针类型输入参数为空指针。

DRM\_ERR\_UNKNOWN：发生内部错误，请查看日志详细信息。

 |

#### \[h2\]OH\_MediaKeySession\_SetMediaKeySessionCallback()

```c
Drm_ErrCode OH_MediaKeySession_SetMediaKeySessionCallback(MediaKeySession *mediaKeySession,MediaKeySession_Callback *callback)
```

**描述**

设置MediaKeySession事件回调。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [MediaKeySession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-mediakeysession) \*mediaKeySession | MediaKeySession实例。 |
| [MediaKeySession\_Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-mediakeysession-callback) \*callback | MediaKeySession的回调。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [Drm\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-err-h#drm_errcode) | 
DRM\_ERR\_OK：执行成功。

DRM\_ERR\_INVALID\_VAL：输入参数mediaKeySession为空指针或无效，或输入参数callback为空指针。

 |

#### \[h2\]OH\_MediaKeySession\_SetCallback()

```c
Drm_ErrCode OH_MediaKeySession_SetCallback(MediaKeySession *mediaKeySession,OH_MediaKeySession_Callback *callback)
```

**描述**

设置MediaKeySession事件回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [MediaKeySession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-mediakeysession) \*mediaKeySession | MediaKeySession实例。 |
| [OH\_MediaKeySession\_Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-oh-mediakeysession-callback) \*callback | MediaKeySession的回调。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [Drm\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-err-h#drm_errcode) | 
DRM\_ERR\_OK：执行成功。

DRM\_ERR\_INVALID\_VAL：输入参数mediaKeySession为空指针或无效，或输入参数callback为空指针。

 |

#### \[h2\]OH\_MediaKeySession\_Destroy()

```c
Drm_ErrCode OH_MediaKeySession_Destroy(MediaKeySession *mediaKeySession)
```

**描述**

销毁MediaKeySession实例。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [MediaKeySession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-mediakeysession) \*mediaKeySession | MediaKeySession实例。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [Drm\_ErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-err-h#drm_errcode) | 
DRM\_ERR\_OK：执行成功。

DRM\_ERR\_INVALID\_VAL：输入参数mediaKeySession为空指针或无效。

DRM\_ERR\_UNKNOWN：发生内部错误，请查看日志详细信息。

 |

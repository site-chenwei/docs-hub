---
title: "moving_photo_capi.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-moving-photo-capi-h"
menu_path:
  - "参考"
  - "媒体"
  - "Media Library Kit（媒体文件管理服务）"
  - "C API"
  - "头文件"
  - "moving_photo_capi.h"
captured_at: "2026-04-17T01:48:45.602Z"
---

# moving\_photo\_capi.h

#### 概述

定义与动态照片相关的API。提供获取动态照片信息的功能。

**库：** libmedia\_asset\_manager.so

**引用文件：** <multimedia/media\_library/moving\_photo\_capi.h>

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 13

**相关模块：** [MediaAssetManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mediaassetmanager)

#### 汇总

#### \[h2\]函数

| 名称 | 描述 |
| :-- | :-- |
| [MediaLibrary\_ErrorCode OH\_MovingPhoto\_GetUri(OH\_MovingPhoto\* movingPhoto, const char\*\* uri)](#oh_movingphoto_geturi) | 获取动态照片的uri。 |
| [MediaLibrary\_ErrorCode OH\_MovingPhoto\_RequestContentWithUris(OH\_MovingPhoto\* movingPhoto, char\* imageUri, char\* videoUri)](#oh_movingphoto_requestcontentwithuris) | 同时请求动态照片的图片内容和视频内容，并写入参数指定的对应的uri中。 |
| [MediaLibrary\_ErrorCode OH\_MovingPhoto\_RequestContentWithUri(OH\_MovingPhoto\* movingPhoto, MediaLibrary\_ResourceType resourceType, char\* uri)](#oh_movingphoto_requestcontentwithuri) | 请求指定资源类型的动态照片内容，并写入参数指定的uri中。 |
| [MediaLibrary\_ErrorCode OH\_MovingPhoto\_RequestContentWithBuffer(OH\_MovingPhoto\* movingPhoto, MediaLibrary\_ResourceType resourceType, const uint8\_t\*\* buffer, uint32\_t\* size)](#oh_movingphoto_requestcontentwithbuffer) | 请求指定资源类型的动态照片内容，以ArrayBuffer的形式返回。 |
| [MediaLibrary\_ErrorCode OH\_MovingPhoto\_Release(OH\_MovingPhoto\* movingPhoto)](#oh_movingphoto_release) | Release [OH\_MovingPhoto](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mediaassetmanager-oh-movingphoto)实例。 |

#### 函数说明

#### \[h2\]OH\_MovingPhoto\_GetUri()

```c
MediaLibrary_ErrorCode OH_MovingPhoto_GetUri(OH_MovingPhoto* movingPhoto, const char** uri)
```

**描述**

获取动态照片的uri。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_MovingPhoto](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mediaassetmanager-oh-movingphoto)\* movingPhoto | [OH\_MovingPhoto](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mediaassetmanager-oh-movingphoto)实例。 |
| const char\*\* uri | 动态照片的uri。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [MediaLibrary\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-media-asset-base-capi-h#medialibrary_errorcode) | 
MEDIA\_LIBRARY\_OK：方法调用成功。

MEDIA\_LIBRARY\_PARAMETER\_ERROR：参数错误。可能的原因：

1\. 未指定强制参数。

2\. 参数类型不正确。

3\. 参数验证失败。

MEDIA\_LIBRARY\_INTERNAL\_SYSTEM\_ERROR：内部系统错误。

 |

#### \[h2\]OH\_MovingPhoto\_RequestContentWithUris()

```c
MediaLibrary_ErrorCode OH_MovingPhoto_RequestContentWithUris(OH_MovingPhoto* movingPhoto, char* imageUri,char* videoUri)
```

**描述**

同时请求动态照片的图片内容和视频内容，并写入参数指定的对应的uri中。

**需要权限：** ohos.permission.READ\_IMAGEVIDEO

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_MovingPhoto](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mediaassetmanager-oh-movingphoto)\* movingPhoto | [OH\_MovingPhoto](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mediaassetmanager-oh-movingphoto)实例。 |
| char\* imageUri | 用于保存图像数据的目标文件uri。 |
| char\* videoUri | 用于保存视频数据的目标文件uri。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [MediaLibrary\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-media-asset-base-capi-h#medialibrary_errorcode) | 
MEDIA\_LIBRARY\_OK：方法调用成功。

MEDIA\_LIBRARY\_PARAMETER\_ERROR：参数错误。可能的原因：

1\. 未指定强制参数。

2\. 参数类型不正确。

3\. 参数验证失败。

MEDIA\_LIBRARY\_PERMISSION\_DENIED：没有权限。

MEDIA\_LIBRARY\_INTERNAL\_SYSTEM\_ERROR：内部系统错误。

 |

#### \[h2\]OH\_MovingPhoto\_RequestContentWithUri()

```c
MediaLibrary_ErrorCode OH_MovingPhoto_RequestContentWithUri(OH_MovingPhoto* movingPhoto,MediaLibrary_ResourceType resourceType, char* uri)
```

**描述**

请求指定资源类型的动态照片内容，并写入参数指定的uri中。

**需要权限：** ohos.permission.READ\_IMAGEVIDEO

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_MovingPhoto](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mediaassetmanager-oh-movingphoto)\* movingPhoto | [OH\_MovingPhoto](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mediaassetmanager-oh-movingphoto)实例。 |
| [MediaLibrary\_ResourceType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-media-asset-base-capi-h#medialibrary_resourcetype) resourceType | 指定的资源类型[MediaLibrary\_ResourceType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-media-asset-base-capi-h#medialibrary_resourcetype)。 |
| char\* uri | 保存数据的目标文件uri。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [MediaLibrary\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-media-asset-base-capi-h#medialibrary_errorcode) | 
MEDIA\_LIBRARY\_OK：方法调用成功。

MEDIA\_LIBRARY\_PARAMETER\_ERROR：参数错误。可能的原因：

1\. 未指定强制参数。

2\. 参数类型不正确。

3\. 参数验证失败。

MEDIA\_LIBRARY\_PERMISSION\_DENIED：没有权限。

MEDIA\_LIBRARY\_INTERNAL\_SYSTEM\_ERROR：内部系统错误。

 |

#### \[h2\]OH\_MovingPhoto\_RequestContentWithBuffer()

```c
MediaLibrary_ErrorCode OH_MovingPhoto_RequestContentWithBuffer(OH_MovingPhoto* movingPhoto,MediaLibrary_ResourceType resourceType, const uint8_t** buffer, uint32_t* size)
```

**描述**

请求指定资源类型的动态照片内容，以ArrayBuffer的形式返回。

**需要权限：** ohos.permission.READ\_IMAGEVIDEO

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_MovingPhoto](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mediaassetmanager-oh-movingphoto)\* movingPhoto | [OH\_MovingPhoto](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mediaassetmanager-oh-movingphoto)实例。 |
| [MediaLibrary\_ResourceType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-media-asset-base-capi-h#medialibrary_resourcetype) resourceType | 指定的资源类型[MediaLibrary\_ResourceType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-media-asset-base-capi-h#medialibrary_resourcetype)。 |
| const uint8\_t\*\* buffer | 保存目标文件数据的缓冲区。 |
| uint32\_t\* size | 缓冲区的大小。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [MediaLibrary\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-media-asset-base-capi-h#medialibrary_errorcode) | 
MEDIA\_LIBRARY\_OK：方法调用成功。

MEDIA\_LIBRARY\_PARAMETER\_ERROR：参数错误。可能的原因：

1\. 未指定强制参数。

2\. 参数类型不正确。

3\. 参数验证失败。

MEDIA\_LIBRARY\_PERMISSION\_DENIED：没有权限。

MEDIA\_LIBRARY\_INTERNAL\_SYSTEM\_ERROR：内部系统错误。

 |

#### \[h2\]OH\_MovingPhoto\_Release()

```c
MediaLibrary_ErrorCode OH_MovingPhoto_Release(OH_MovingPhoto* movingPhoto)
```

**描述**

Release [OH\_MovingPhoto](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mediaassetmanager-oh-movingphoto)实例。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_MovingPhoto](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mediaassetmanager-oh-movingphoto)\* movingPhoto | 要释放的[OH\_MovingPhoto](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mediaassetmanager-oh-movingphoto)实例。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [MediaLibrary\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-media-asset-base-capi-h#medialibrary_errorcode) | 
MEDIA\_LIBRARY\_OK：方法调用成功。

MEDIA\_LIBRARY\_PARAMETER\_ERROR：参数错误。可能的原因：

1\. 未指定强制参数。

2\. 参数类型不正确。

3\. 参数验证失败。

 |

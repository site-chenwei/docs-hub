---
title: "image_receiver_mdk.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-receiver-mdk-h"
menu_path:
  - "参考"
  - "媒体"
  - "Image Kit（图片处理服务）"
  - "C API"
  - "头文件"
  - "image_receiver_mdk.h"
captured_at: "2026-04-17T01:48:41.748Z"
---

# image\_receiver\_mdk.h

#### 概述

声明从native层获取图片数据的方法。

**库：** libimage\_receiver\_ndk.z.so

**引用文件：** <multimedia/image\_framework/image\_receiver\_mdk.h>

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 10

**相关模块：** [Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image)

#### 汇总

#### \[h2\]结构体

| 名称 | typedef关键字 | 描述 |
| :-- | :-- | :-- |
| [OhosImageReceiverInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagereceiverinfo) | \- | 定义ImageReceiver的相关信息。 |
| [ImageReceiverNative\_](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-imagereceivernative-) | ImageReceiverNative | 用于定义ImageReceiverNative数据类型名称。 |

#### \[h2\]函数

| 名称 | typedef关键字 | 描述 |
| :-- | :-- | :-- |
| [typedef void (\*OH\_Image\_Receiver\_On\_Callback)()](#oh_image_receiver_on_callback) | OH\_Image\_Receiver\_On\_Callback | 定义native层图片的回调方法。 |
| [int32\_t OH\_Image\_Receiver\_CreateImageReceiver(napi\_env env, struct OhosImageReceiverInfo info, napi\_value\* res)](#oh_image_receiver_createimagereceiver) | \- | 创建应用层ImageReceiver对象。 |
| [ImageReceiverNative\* OH\_Image\_Receiver\_InitImageReceiverNative(napi\_env env, napi\_value source)](#oh_image_receiver_initimagereceivernative) | \- | 通过应用层ImageReceiver对象初始化native层[ImageReceiverNative](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-imagereceivernative-)对象。 |
| [int32\_t OH\_Image\_Receiver\_GetReceivingSurfaceId(const ImageReceiverNative\* native, char\* id, size\_t len)](#oh_image_receiver_getreceivingsurfaceid) | \- | 通过[ImageReceiverNative](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-imagereceivernative-)获取receiver的id。 |
| [int32\_t OH\_Image\_Receiver\_ReadLatestImage(const ImageReceiverNative\* native, napi\_value\* image)](#oh_image_receiver_readlatestimage) | \- | 通过[ImageReceiverNative](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-imagereceivernative-)获取最新的一张图片。 |
| [int32\_t OH\_Image\_Receiver\_ReadNextImage(const ImageReceiverNative\* native, napi\_value\* image)](#oh_image_receiver_readnextimage) | \- | 通过[ImageReceiverNative](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-imagereceivernative-)获取下一张图片。 |
| [int32\_t OH\_Image\_Receiver\_On(const ImageReceiverNative\* native, OH\_Image\_Receiver\_On\_Callback callback)](#oh_image_receiver_on) | \- | 注册一个[OH\_Image\_Receiver\_On\_Callback](#oh_image_receiver_on_callback)回调事件。每当接收新图片，该回调事件就会响应。 |
| [int32\_t OH\_Image\_Receiver\_GetSize(const ImageReceiverNative\* native, struct OhosImageSize\* size)](#oh_image_receiver_getsize) | \- | 通过[ImageReceiverNative](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-imagereceivernative-)获取ImageReceiver的大小。 |
| [int32\_t OH\_Image\_Receiver\_GetCapacity(const ImageReceiverNative\* native, int32\_t\* capacity)](#oh_image_receiver_getcapacity) | \- | 通过[ImageReceiverNative](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-imagereceivernative-)获取ImageReceiver的容量。 |
| [int32\_t OH\_Image\_Receiver\_GetFormat(const ImageReceiverNative\* native, int32\_t\* format)](#oh_image_receiver_getformat) | \- | 通过[ImageReceiverNative](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-imagereceivernative-)获取ImageReceiver的格式。 |
| [int32\_t OH\_Image\_Receiver\_Release(ImageReceiverNative\* native)](#oh_image_receiver_release) | \- | 
释放native层[ImageReceiverNative](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-imagereceivernative-)对象。

注意，此方法不能释放应用层ImageReceiver对象。

 |

#### 函数说明

#### \[h2\]OH\_Image\_Receiver\_On\_Callback()

```c
typedef void (*OH_Image_Receiver_On_Callback)(void)
```

**描述**

定义native层图片的回调方法。

**起始版本：** 10

#### \[h2\]OH\_Image\_Receiver\_CreateImageReceiver()

```c
int32_t OH_Image_Receiver_CreateImageReceiver(napi_env env, struct OhosImageReceiverInfo info, napi_value* res)
```

**描述**

创建应用层ImageReceiver对象。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| napi\_env env | napi的环境指针。 |
| struct [OhosImageReceiverInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagereceiverinfo) info | ImageReceiver数据设置项。 |
| napi\_value\* res | 应用层的ImageReceiver对象的指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
[IRNdkErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-mdk-common-h#irndkerrcode)：

IMAGE\_RESULT\_SUCCESS：操作成功。

IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。

IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。

IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。

IMAGE\_RESULT\_INVALID\_PARAMETER：从surface获取参数失败。

IMAGE\_RESULT\_CREATE\_SURFACE\_FAILED：创建surface失败。

IMAGE\_RESULT\_SURFACE\_GRALLOC\_BUFFER\_FAILED：surface分配内存失败。

IMAGE\_RESULT\_GET\_SURFACE\_FAILED：获取surface失败。

IMAGE\_RESULT\_MEDIA\_RTSP\_SURFACE\_UNSUPPORT：媒体rtsp surface不支持。

IMAGE\_RESULT\_DATA\_UNSUPPORT：图像类型不支持。

IMAGE\_RESULT\_MEDIA\_DATA\_UNSUPPORT：媒体类型不支持。

 |

#### \[h2\]OH\_Image\_Receiver\_InitImageReceiverNative()

```c
ImageReceiverNative* OH_Image_Receiver_InitImageReceiverNative(napi_env env, napi_value source)
```

**描述**

通过应用层ImageReceiver对象初始化native层[ImageReceiverNative](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-imagereceivernative-)对象。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| napi\_env env | napi的环境指针。 |
| napi\_value source | napi的ImageReceiver对象。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [ImageReceiverNative](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-imagereceivernative-)\* | 操作成功则返回ImageReceiverNative指针；如果操作失败，则返回nullptr。 |

**参考：**

[OH\_Image\_Receiver\_Release](#oh_image_receiver_release)

#### \[h2\]OH\_Image\_Receiver\_GetReceivingSurfaceId()

```c
int32_t OH_Image_Receiver_GetReceivingSurfaceId(const ImageReceiverNative* native, char* id, size_t len)
```

**描述**

通过[ImageReceiverNative](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-imagereceivernative-)获取receiver的id。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const [ImageReceiverNative](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-imagereceivernative-)\* native | native层的ImageReceiverNative指针。 |
| char\* id | 指向字符缓冲区的指针，用于获取字符串的id。 |
| size\_t len | id所对应的字符缓冲区的大小。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
[IRNdkErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-mdk-common-h#irndkerrcode)：

IMAGE\_RESULT\_SUCCESS：操作成功。

IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。

IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。

IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。

IMAGE\_RESULT\_INVALID\_PARAMETER：从surface获取参数失败。

IMAGE\_RESULT\_GET\_SURFACE\_FAILED：获取surface失败。

IMAGE\_RESULT\_DATA\_UNSUPPORT：图像类型不支持。

IMAGE\_RESULT\_MEDIA\_DATA\_UNSUPPORT：媒体类型不支持。

 |

#### \[h2\]OH\_Image\_Receiver\_ReadLatestImage()

```c
int32_t OH_Image_Receiver_ReadLatestImage(const ImageReceiverNative* native, napi_value* image)
```

**描述**

通过[ImageReceiverNative](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-imagereceivernative-)获取最新的一张图片。

注意，此接口需要在[OH\_Image\_Receiver\_On\_Callback](#oh_image_receiver_on_callback)回调后调用，才能正常的接收到数据。并且使用此接口返回Image对象创建的[ImageNative](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-imagenative-)使用完毕后需要调用[OH\_Image\_Release](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-mdk-h#oh_image_release)方法释放，释放后才可以继续接收新的数据。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const [ImageReceiverNative](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-imagereceivernative-)\* native | native层的ImageReceiverNative指针。 |
| napi\_value\* image | 获取到的应用层的Image指针对象。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
[IRNdkErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-mdk-common-h#irndkerrcode)：

IMAGE\_RESULT\_SUCCESS：操作成功。

IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。

IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。

IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。

IMAGE\_RESULT\_INVALID\_PARAMETER：从surface获取参数失败。

IMAGE\_RESULT\_CREATE\_SURFACE\_FAILED：创建surface失败。

IMAGE\_RESULT\_SURFACE\_GRALLOC\_BUFFER\_FAILED：surface分配内存失败。

IMAGE\_RESULT\_GET\_SURFACE\_FAILED：获取surface失败。

IMAGE\_RESULT\_MEDIA\_RTSP\_SURFACE\_UNSUPPORT：媒体rtsp surface不支持。

IMAGE\_RESULT\_DATA\_UNSUPPORT：图像类型不支持。

IMAGE\_RESULT\_MEDIA\_DATA\_UNSUPPORT：媒体类型不支持。

 |

#### \[h2\]OH\_Image\_Receiver\_ReadNextImage()

```c
int32_t OH_Image_Receiver_ReadNextImage(const ImageReceiverNative* native, napi_value* image)
```

**描述**

通过[ImageReceiverNative](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-imagereceivernative-)获取下一张图片。

注意，此接口需要在[OH\_Image\_Receiver\_On\_Callback](#oh_image_receiver_on_callback)回调后调用，才能正常的接收到数据。并且使用此接口返回Image对象创建的[ImageNative](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-imagenative-)使用完毕后需要调用[OH\_Image\_Release](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-mdk-h#oh_image_release)方法释放，释放后才可以继续接收新的数据。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const [ImageReceiverNative](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-imagereceivernative-)\* native | native层的ImageReceiverNative指针。 |
| napi\_value\* image | 读取到的应用层的Image指针对象。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
[IRNdkErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-mdk-common-h#irndkerrcode)：

IMAGE\_RESULT\_SUCCESS：操作成功。

IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。

IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。

IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。

IMAGE\_RESULT\_INVALID\_PARAMETER：从surface获取参数失败。

IMAGE\_RESULT\_CREATE\_SURFACE\_FAILED：创建surface失败。

IMAGE\_RESULT\_SURFACE\_GRALLOC\_BUFFER\_FAILED：surface分配内存失败。

IMAGE\_RESULT\_GET\_SURFACE\_FAILED：获取surface失败。

IMAGE\_RESULT\_MEDIA\_RTSP\_SURFACE\_UNSUPPORT：媒体rtsp surface不支持。

IMAGE\_RESULT\_DATA\_UNSUPPORT：图像类型不支持。

IMAGE\_RESULT\_MEDIA\_DATA\_UNSUPPORT：媒体类型不支持。

 |

#### \[h2\]OH\_Image\_Receiver\_On()

```c
int32_t OH_Image_Receiver_On(const ImageReceiverNative* native, OH_Image_Receiver_On_Callback callback)
```

**描述**

注册一个[OH\_Image\_Receiver\_On\_Callback](#oh_image_receiver_on_callback)回调事件。每当接收新图片，该回调事件就会响应。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const [ImageReceiverNative](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-imagereceivernative-)\* native | native层的ImageReceiverNative指针。 |
| [OH\_Image\_Receiver\_On\_Callback](#oh_image_receiver_on_callback) callback | [OH\_Image\_Receiver\_On\_Callback](#oh_image_receiver_on_callback)事件的回调函数。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
[IRNdkErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-mdk-common-h#irndkerrcode)：

IMAGE\_RESULT\_SUCCESS：操作成功。

IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。

IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。

IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。

IMAGE\_RESULT\_INVALID\_PARAMETER：从surface获取参数失败。

IMAGE\_RESULT\_GET\_SURFACE\_FAILED：获取surface失败。

IMAGE\_RESULT\_DATA\_UNSUPPORT：图像类型不支持。

IMAGE\_RESULT\_MEDIA\_DATA\_UNSUPPORT：媒体类型不支持。

 |

#### \[h2\]OH\_Image\_Receiver\_GetSize()

```c
int32_t OH_Image_Receiver_GetSize(const ImageReceiverNative* native, struct OhosImageSize* size)
```

**描述**

通过[ImageReceiverNative](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-imagereceivernative-)获取ImageReceiver的大小。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const [ImageReceiverNative](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-imagereceivernative-)\* native | native层的ImageReceiverNative指针。 |
| struct [OhosImageSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagesize)\* size | 作为结果的OhosImageSize指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
[IRNdkErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-mdk-common-h#irndkerrcode)：

IMAGE\_RESULT\_SUCCESS：操作成功。

IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。

IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。

IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。

IMAGE\_RESULT\_DATA\_UNSUPPORT：图像类型不支持。

 |

#### \[h2\]OH\_Image\_Receiver\_GetCapacity()

```c
int32_t OH_Image_Receiver_GetCapacity(const ImageReceiverNative* native, int32_t* capacity)
```

**描述**

通过[ImageReceiverNative](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-imagereceivernative-)获取ImageReceiver的容量。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const [ImageReceiverNative](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-imagereceivernative-)\* native | native层的ImageReceiverNative指针。 |
| int32\_t\* capacity | 作为结果的指向容量的指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
[IRNdkErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-mdk-common-h#irndkerrcode)：

IMAGE\_RESULT\_SUCCESS：操作成功。

IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。

IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。

IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。

IMAGE\_RESULT\_DATA\_UNSUPPORT：图像类型不支持。

 |

#### \[h2\]OH\_Image\_Receiver\_GetFormat()

```c
int32_t OH_Image_Receiver_GetFormat(const ImageReceiverNative* native, int32_t* format)
```

**描述**

通过[ImageReceiverNative](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-imagereceivernative-)获取ImageReceiver的格式。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const [ImageReceiverNative](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-imagereceivernative-)\* native | native层的ImageReceiverNative指针。 |
| int32\_t\* format | 作为结果的指向格式的指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
[IRNdkErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-mdk-common-h#irndkerrcode)：

IMAGE\_RESULT\_SUCCESS：操作成功。

IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。

IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL：JNI环境异常。

IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。

IMAGE\_RESULT\_DATA\_UNSUPPORT：图像类型不支持。

 |

#### \[h2\]OH\_Image\_Receiver\_Release()

```c
int32_t OH_Image_Receiver_Release(ImageReceiverNative* native)
```

**描述**

释放native层[ImageReceiverNative](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-imagereceivernative-)对象。

注意，此方法不能释放应用层ImageReceiver对象。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ImageReceiverNative](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-imagereceivernative-)\* native | native层的ImageReceiverNative指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
[IRNdkErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-mdk-common-h#irndkerrcode)：

IMAGE\_RESULT\_SUCCESS：操作成功。

IMAGE\_RESULT\_BAD\_PARAMETER：参数错误。

IMAGE\_RESULT\_INVALID\_PARAMETER：参数无效。

IMAGE\_RESULT\_DATA\_UNSUPPORT：图像类型不支持。

 |

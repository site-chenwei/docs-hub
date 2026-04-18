---
title: "native_avmemory.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avmemory-h"
menu_path:
  - "参考"
  - "媒体"
  - "AVCodec Kit（音视频编解码服务）"
  - "C API"
  - "头文件"
  - "native_avmemory.h"
captured_at: "2026-04-17T01:48:37.254Z"
---

# native\_avmemory.h

#### 概述

声明了媒体数据结构AVMemory的定义。

**引用文件：** <multimedia/player\_framework/native\_avmemory.h>

**库：** libnative\_media\_core.so

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**相关模块：** [Core](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-core)

#### 汇总

#### \[h2\]结构体

| 名称 | typedef关键字 | 描述 |
| :-- | :-- | :-- |
| [OH\_AVMemory](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-core-oh-avmemory) | OH\_AVMemory | 为音视频内存接口定义native层对象。 |

#### \[h2\]函数

| 名称 | 描述 |
| :-- | :-- |
| [OH\_AVMemory \*OH\_AVMemory\_Create(int32\_t size)](#oh_avmemory_create) | 创建OH\_AVMemory实例的指针。 |
| [uint8\_t \*OH\_AVMemory\_GetAddr(struct OH\_AVMemory \*mem)](#oh_avmemory_getaddr) | 获取内存虚拟地址。 |
| [int32\_t OH\_AVMemory\_GetSize(struct OH\_AVMemory \*mem)](#oh_avmemory_getsize) | 获取内存长度。 |
| [OH\_AVErrCode OH\_AVMemory\_Destroy(struct OH\_AVMemory \*mem)](#oh_avmemory_destroy) | 释放OH\_AVMemory实例指针的资源。 |

#### 函数说明

#### \[h2\]OH\_AVMemory\_Create()

```c
OH_AVMemory *OH_AVMemory_Create(int32_t size)
```

**描述**

创建OH\_AVMemory实例的指针。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [OH\_AVBuffer\_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avbuffer-h#oh_avbuffer_create)

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| int32\_t size | 创建内存的大小，单位字节。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [OH\_AVMemory](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-core-oh-avmemory) \* | 
如果创建成功，返回OH\_AVMemory实例的指针，如果失败，返回NULL。

使用结束后需要通过OH\_AVMemory\_Destroy释放内存。

可能的失败原因：

1\. size <= 0。

2\. 创建OH\_AVMemory失败。

3\. OH\_AVMemory内存分配失败。

 |

#### \[h2\]OH\_AVMemory\_GetAddr()

```c
uint8_t *OH_AVMemory_GetAddr(struct OH_AVMemory *mem)
```

**描述**

获取内存虚拟地址。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [OH\_AVBuffer\_GetAddr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avbuffer-h#oh_avbuffer_getaddr)

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [struct OH\_AVMemory](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-core-oh-avmemory) \*mem | 指向OH\_AVMemory实例的指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| uint8\_t \* | 
如果内存有效，返回内存的虚拟地址，如果内存无效，返回NULL。

可能的失败原因：

1\. 输入mem为空指针。

2\. 输入mem参数结构校验失败。

3\. 输入mem中内存为空指针。

 |

#### \[h2\]OH\_AVMemory\_GetSize()

```c
int32_t OH_AVMemory_GetSize(struct OH_AVMemory *mem)
```

**描述**

获取内存长度。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [OH\_AVBuffer\_GetCapacity](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avbuffer-h#oh_avbuffer_getcapacity)

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [struct OH\_AVMemory](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-core-oh-avmemory) \*mem | 指向OH\_AVMemory实例的指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int32\_t | 
如果内存有效，返回内存长度，如果内存无效，返回-1。

可能的失败原因：

1\. 输入mem为空指针。

2\. 输入mem参数结构校验失败。

3\. 输入mem中内存为空指针。

 |

#### \[h2\]OH\_AVMemory\_Destroy()

```c
OH_AVErrCode OH_AVMemory_Destroy(struct OH_AVMemory *mem)
```

**描述**

释放OH\_AVMemory实例指针的资源。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [OH\_AVBuffer\_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avbuffer-h#oh_avbuffer_destroy)

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [struct OH\_AVMemory](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-core-oh-avmemory) \*mem | 指向OH\_AVMemory实例的指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [OH\_AVErrCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-averrors-h#oh_averrcode) | 
AV\_ERR\_OK：释放成功。

AV\_ERR\_INVALID\_VAL：

1\. 输入mem为空指针。

2\. 输入mem参数结构校验失败。

3\. 输入mem不是开发者创建的。

 |

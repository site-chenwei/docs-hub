---
title: "mutex.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mutex-h"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "Function Flow Runtime Kit"
  - "C API"
  - "头文件"
  - "mutex.h"
captured_at: "2026-04-17T01:48:30.105Z"
---

# mutex.h

#### 概述

声明mutex的C接口。

**引用文件：** <ffrt/mutex.h>

**库：** libffrt.z.so

**系统能力：** SystemCapability.Resourceschedule.Ffrt.Core

**起始版本：** 10

**相关模块：** [FFRT](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt)

#### 汇总

#### \[h2\]函数

| 名称 | 描述 |
| :-- | :-- |
| [FFRT\_C\_API int ffrt\_mutexattr\_init(ffrt\_mutexattr\_t\* attr)](#ffrt_mutexattr_init) | 初始化mutex属性。 |
| [FFRT\_C\_API int ffrt\_mutexattr\_settype(ffrt\_mutexattr\_t\* attr, int type)](#ffrt_mutexattr_settype) | 设置mutex属性类型。 |
| [FFRT\_C\_API int ffrt\_mutexattr\_gettype(ffrt\_mutexattr\_t\* attr, int\* type)](#ffrt_mutexattr_gettype) | 获取mutex类型。 |
| [FFRT\_C\_API int ffrt\_mutexattr\_destroy(ffrt\_mutexattr\_t\* attr)](#ffrt_mutexattr_destroy) | 销毁mutex属性，用户需要调用此接口。 |
| [FFRT\_C\_API int ffrt\_mutex\_init(ffrt\_mutex\_t\* mutex, const ffrt\_mutexattr\_t\* attr)](#ffrt_mutex_init) | 初始化mutex。 |
| [FFRT\_C\_API int ffrt\_mutex\_lock(ffrt\_mutex\_t\* mutex)](#ffrt_mutex_lock) | 获取mutex。 |
| [FFRT\_C\_API int ffrt\_mutex\_unlock(ffrt\_mutex\_t\* mutex)](#ffrt_mutex_unlock) | 释放mutex。 |
| [FFRT\_C\_API int ffrt\_mutex\_trylock(ffrt\_mutex\_t\* mutex)](#ffrt_mutex_trylock) | 尝试获取mutex。 |
| [FFRT\_C\_API int ffrt\_mutex\_destroy(ffrt\_mutex\_t\* mutex)](#ffrt_mutex_destroy) | 销毁mutex。 |

#### 函数说明

#### \[h2\]ffrt\_mutexattr\_init()

```c
FFRT_C_API int ffrt_mutexattr_init(ffrt_mutexattr_t* attr)
```

**描述**

初始化mutex属性。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ffrt\_mutexattr\_t](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-mutexattr-t)\* attr | mutex属性指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| FFRT\_C\_API int | 
mutex属性初始化成功返回ffrt\_success，

mutex属性初始化失败返回ffrt\_error\_inval。

 |

#### \[h2\]ffrt\_mutexattr\_settype()

```c
FFRT_C_API int ffrt_mutexattr_settype(ffrt_mutexattr_t* attr, int type)
```

**描述**

设置mutex属性类型。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ffrt\_mutexattr\_t](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-mutexattr-t)\* attr | mutex属性指针。 |
| int type | mutex类型。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| FFRT\_C\_API int | 
mutex属性类型设置成功返回ffrt\_success，

mutex属性指针是空或者

mutex类型不是ffrt\_mutex\_normal或ffrt\_mutex\_recursive返回ffrt\_error\_inval。

 |

#### \[h2\]ffrt\_mutexattr\_gettype()

```c
FFRT_C_API int ffrt_mutexattr_gettype(ffrt_mutexattr_t* attr, int* type)
```

**描述**

获取mutex类型。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ffrt\_mutexattr\_t](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-mutexattr-t)\* attr | mutex属性指针。 |
| int\* type | mutex类型指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| FFRT\_C\_API int | 
mutex类型获取成功返回ffrt\_success，

mutex属性指针或mutex类型指针是空返回ffrt\_error\_inval。

 |

#### \[h2\]ffrt\_mutexattr\_destroy()

```c
FFRT_C_API int ffrt_mutexattr_destroy(ffrt_mutexattr_t* attr)
```

**描述**

销毁mutex属性，用户需要调用此接口。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ffrt\_mutexattr\_t](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-mutexattr-t)\* attr | mutex属性指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| FFRT\_C\_API int | 
mutex属性销毁成功返回ffrt\_success，

mutex属性销毁失败返回ffrt\_error\_inval。

 |

#### \[h2\]ffrt\_mutex\_init()

```c
FFRT_C_API int ffrt_mutex_init(ffrt_mutex_t* mutex, const ffrt_mutexattr_t* attr)
```

**描述**

初始化mutex。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ffrt\_mutex\_t](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-mutex-t)\* mutex | mutex指针。 |
| [const ffrt\_mutexattr\_t](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-mutexattr-t)\* attr | mutex属性指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| FFRT\_C\_API int | 
初始化mutex成功返回ffrt\_success，

初始化mutex失败返回ffrt\_error\_inval。

 |

#### \[h2\]ffrt\_mutex\_lock()

```c
FFRT_C_API int ffrt_mutex_lock(ffrt_mutex_t* mutex)
```

**描述**

获取mutex。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ffrt\_mutex\_t](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-mutex-t)\* mutex | mutex指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| FFRT\_C\_API int | 
获取mutex成功返回ffrt\_success，

获取mutex失败返回ffrt\_error\_inval或者阻塞当前任务。

 |

#### \[h2\]ffrt\_mutex\_unlock()

```c
FFRT_C_API int ffrt_mutex_unlock(ffrt_mutex_t* mutex)
```

**描述**

释放mutex。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ffrt\_mutex\_t](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-mutex-t)\* mutex | mutex指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| FFRT\_C\_API int | 
释放mutex成功返回ffrt\_success，

释放mutex失败返回ffrt\_error\_inval。

 |

#### \[h2\]ffrt\_mutex\_trylock()

```c
FFRT_C_API int ffrt_mutex_trylock(ffrt_mutex_t* mutex)
```

**描述**

尝试获取mutex。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ffrt\_mutex\_t](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-mutex-t)\* mutex | mutex指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| FFRT\_C\_API int | 
获取mutex成功返回ffrt\_success，

获取mutex失败返回ffrt\_error\_inval或ffrt\_error\_busy。

 |

#### \[h2\]ffrt\_mutex\_destroy()

```c
FFRT_C_API int ffrt_mutex_destroy(ffrt_mutex_t* mutex)
```

**描述**

销毁mutex。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [ffrt\_mutex\_t](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-mutex-t)\* mutex | mutex指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| FFRT\_C\_API int | 
销毁mutex成功返回ffrt\_success，

销毁mutex失败返回ffrt\_error\_inval。

 |

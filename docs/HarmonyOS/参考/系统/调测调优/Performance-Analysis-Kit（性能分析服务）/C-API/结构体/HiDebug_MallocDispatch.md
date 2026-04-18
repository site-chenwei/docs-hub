---
title: "HiDebug_MallocDispatch"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-mallocdispatch"
menu_path:
  - "参考"
  - "系统"
  - "调测调优"
  - "Performance Analysis Kit（性能分析服务）"
  - "C API"
  - "结构体"
  - "HiDebug_MallocDispatch"
captured_at: "2026-04-17T01:48:35.212Z"
---

# HiDebug\_MallocDispatch

```c
typedef struct HiDebug_MallocDispatch {...} HiDebug_MallocDispatch
```

#### 概述

应用程序进程可替换/恢复的HiDebug\_MallocDispatch表结构类型定义。

**起始版本：** 20

**相关模块：** [HiDebug](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug)

**所在头文件：** [hidebug\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-type-h)

#### 汇总

#### \[h2\]成员函数

| 名称 | 描述 |
| :-- | :-- |
| [void\* (\*malloc)(size\_t)](#malloc) | 开发者自定义malloc函数指针。 |
| [void\* (\*calloc)(size\_t, size\_t)](#calloc) | 开发者自定义calloc函数指针。 |
| [void\* (\*realloc)(void\*, size\_t)](#realloc) | 开发者自定义realloc函数指针。 |
| [void (\*free)(void\*)](#free) | 开发者自定义free函数指针。 |
| [void\* (\*mmap)(void\*, size\_t, int, int, int, off\_t)](#mmap) | 开发者自定义mmap函数指针。 |
| [int (\*munmap)(void\*, size\_t)](#munmap) | 开发者自定义munmap函数指针。 |

#### 成员函数说明

#### \[h2\]malloc()

```c
void* (*malloc)(size_t)
```

**描述**

开发者自定义malloc函数指针。

#### \[h2\]calloc()

```c
void* (*calloc)(size_t, size_t)
```

**描述**

开发者自定义calloc函数指针。

#### \[h2\]realloc()

```c
void* (*realloc)(void*, size_t)
```

**描述**

开发者自定义realloc函数指针。

#### \[h2\]free()

```c
void (*free)(void*)
```

**描述**

开发者自定义free函数指针。

#### \[h2\]mmap()

```c
void* (*mmap)(void*, size_t, int, int, int, off_t)
```

**描述**

开发者自定义mmap函数指针。

#### \[h2\]munmap()

```c
int (*munmap)(void*, size_t)
```

**描述**

开发者自定义munmap函数指针。

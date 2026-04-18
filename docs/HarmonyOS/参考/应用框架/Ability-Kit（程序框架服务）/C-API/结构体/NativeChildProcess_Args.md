---
title: "NativeChildProcess_Args"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativechildprocess-args"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "C API"
  - "结构体"
  - "NativeChildProcess_Args"
captured_at: "2026-04-17T01:47:48.739Z"
---

# NativeChildProcess\_Args

```c
typedef struct {...} NativeChildProcess_Args
```

#### 概述

传递给子进程的参数。

**起始版本：** 13

**相关模块：** [ChildProcess](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-childprocess)

**所在头文件：** [native\_child\_process.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-child-process-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| char\* entryParams | 入口参数，大小不能超过150KB。 |
| struct [NativeChildProcess\_FdList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativechildprocess-fdlist) fdList | 传递给子进程的文件描述符信息列表。 |

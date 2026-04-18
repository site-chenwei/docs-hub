---
title: "NativeChildProcess_Fd"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativechildprocess-fd"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "C API"
  - "结构体"
  - "NativeChildProcess_Fd"
captured_at: "2026-04-17T01:47:48.787Z"
---

# NativeChildProcess\_Fd

```c
typedef struct {...} NativeChildProcess_Fd
```

#### 概述

传递给子进程的文件描述符信息。

**起始版本：** 13

**相关模块：** [ChildProcess](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-childprocess)

**所在头文件：** [native\_child\_process.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-child-process-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| char\* fdName | 文件描述符的键，最大长度为20字符。 |
| int32\_t fd | 文件描述符的值。 |
| struct [NativeChildProcess\_Fd](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativechildprocess-fd)\* next | 下一个文件描述记录指针。 |

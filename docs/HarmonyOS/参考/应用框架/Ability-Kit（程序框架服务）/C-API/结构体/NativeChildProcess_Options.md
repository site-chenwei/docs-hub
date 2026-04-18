---
title: "NativeChildProcess_Options"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativechildprocess-options"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "C API"
  - "结构体"
  - "NativeChildProcess_Options"
captured_at: "2026-04-17T01:47:48.730Z"
---

# NativeChildProcess\_Options

```c
typedef struct {...} NativeChildProcess_Options
```

#### 概述

启动子进程的配置选项。

**起始版本：** 13

**相关模块：** [ChildProcess](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-childprocess)

**所在头文件：** [native\_child\_process.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-child-process-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [NativeChildProcess\_IsolationMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-child-process-h#nativechildprocess_isolationmode) isolationMode | 子进程所采用的隔离模式。 |
| int64\_t reserved | 预留字段，供未来扩展使用。 |

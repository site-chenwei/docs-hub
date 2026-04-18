---
title: "HiDebug_StackFrame"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-stackframe"
menu_path:
  - "参考"
  - "系统"
  - "调测调优"
  - "Performance Analysis Kit（性能分析服务）"
  - "C API"
  - "结构体"
  - "HiDebug_StackFrame"
captured_at: "2026-04-17T01:48:35.207Z"
---

# HiDebug\_StackFrame

```c
typedef struct HiDebug_StackFrame {...} HiDebug_StackFrame
```

#### 概述

栈帧内容的定义。

**起始版本：** 20

**相关模块：** [HiDebug](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug)

**所在头文件：** [hidebug\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [HiDebug\_StackFrameType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-type-h#hidebug_stackframetype) type | 当前栈的类型。 |
| struct [HiDebug\_JsStackFrame](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-jsstackframe) js | 由[HiDebug\_JsStackFrame](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-jsstackframe)定义的js栈帧内容。 |
| struct [HiDebug\_NativeStackFrame](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-nativestackframe) native | 由[HiDebug\_NativeStackFrame](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-nativestackframe)定义的native栈帧内容。 |

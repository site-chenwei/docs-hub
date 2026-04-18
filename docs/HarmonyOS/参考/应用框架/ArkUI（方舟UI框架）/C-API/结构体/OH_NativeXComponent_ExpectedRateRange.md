---
title: "OH_NativeXComponent_ExpectedRateRange"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/e-xcomponent-oh-nativexcomponent-expectedraterange"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "C API"
  - "结构体"
  - "OH_NativeXComponent_ExpectedRateRange"
captured_at: "2026-04-17T01:48:09.195Z"
---

# OH\_NativeXComponent\_ExpectedRateRange

```c
typedef struct {...} OH_NativeXComponent_ExpectedRateRange
```

#### 概述

定义期望帧率范围。

**起始版本：** 11

**相关模块：** [OH\_NativeXComponent Native XComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent)

**所在头文件：** [native\_interface\_xcomponent.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-xcomponent-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int32\_t min | 期望帧率范围最小值。单位为帧/秒。 |
| int32\_t max | 期望帧率范围最大值。单位为帧/秒。 |
| int32\_t expected | 期望帧率。单位为帧/秒。 |

---
title: "OH_NativeVSync_ExpectedRateRange"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativevsync-oh-nativevsync-expectedraterange"
menu_path:
  - "参考"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "C API"
  - "结构体"
  - "OH_NativeVSync_ExpectedRateRange"
captured_at: "2026-04-17T01:48:50.267Z"
---

# OH\_NativeVSync\_ExpectedRateRange

```c
typedef struct {...} OH_NativeVSync_ExpectedRateRange
```

#### 概述

期望帧率范围结构体。

**起始版本：** 20

**相关模块：** [NativeVsync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativevsync)

**所在头文件：** [native\_vsync.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-vsync-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int32\_t min | 帧率范围的最小帧率。 |
| int32\_t max | 帧率范围的最大帧率。 |
| int32\_t expected | 帧率范围的期望帧率。 |

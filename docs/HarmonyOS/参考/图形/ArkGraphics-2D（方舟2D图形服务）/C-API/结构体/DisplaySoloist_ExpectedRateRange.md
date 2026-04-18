---
title: "DisplaySoloist_ExpectedRateRange"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ivedisplaysoloist-displaysoloist-expectedraterange"
menu_path:
  - "参考"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "C API"
  - "结构体"
  - "DisplaySoloist_ExpectedRateRange"
captured_at: "2026-04-17T01:48:49.894Z"
---

# DisplaySoloist\_ExpectedRateRange

```c
typedef struct {...} DisplaySoloist_ExpectedRateRange
```

#### 概述

提供期望帧率范围结构体。

**起始版本：** 12

**相关模块：** [NativeDisplaySoloist](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaysoloist)

**所在头文件：** [native\_display\_soloist.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-display-soloist-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int32\_t min | 期望帧率范围最小值，取值范围为\[0,120\]。 |
| int32\_t max | 期望帧率范围最大值，取值范围为\[0,120\]。 |
| int32\_t expected | 期望帧率，取值范围为\[0,120\]。 |

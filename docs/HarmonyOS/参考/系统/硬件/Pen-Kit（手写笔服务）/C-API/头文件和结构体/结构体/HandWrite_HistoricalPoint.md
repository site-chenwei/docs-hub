---
title: "HandWrite_HistoricalPoint"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-handwrite-struct-historicalpoint"
menu_path:
  - "参考"
  - "系统"
  - "硬件"
  - "Pen Kit（手写笔服务）"
  - "C API"
  - "头文件和结构体"
  - "结构体"
  - "HandWrite_HistoricalPoint"
captured_at: "2026-04-17T01:48:33.719Z"
---

# HandWrite\_HistoricalPoint

#### 概述

定义历史触摸点信息的结构体。

**系统能力：** SystemCapability.Stylus.HandWrite

**起始版本：** 6.0.0(20)

**相关模块：** [HandWrite](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-handwrite-c)

**所在头文件：** [native\_handwrite\_api.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-handwrite-headerfile-declare)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| float [x](#x) | 历史触摸点的X坐标，相对于被触摸元素左边缘，单位：像素。 |
| float [y](#y) | 历史触摸点的Y坐标，相对于被触摸元素上边缘，单位：像素。 |
| int64\_t [timeStamp](#timestamp) | 当前历史触摸点的时间戳，单位：ns。 |
| float [force](#force) | 当前历史触摸点的压力值。 |

#### 结构体成员变量说明

#### \[h2\]x

```c
float HandWrite_HistoricalPoint::x
```

**描述**

历史触摸点的X坐标，相对于被触摸元素左边缘。

#### \[h2\]y

```c
float HandWrite_HistoricalPoint::y
```

**描述**

历史触摸点的Y坐标，相对于被触摸元素上边缘。

#### \[h2\]timeStamp

```c
int64_t HandWrite_HistoricalPoint::timeStamp
```

**描述**

当前历史触摸点的时间戳，单位为ns。

#### \[h2\]force

```c
float HandWrite_HistoricalPoint::force
```

**描述**

当前历史触摸点的压力值。

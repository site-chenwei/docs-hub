---
title: "Vibrator_FileDescription"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vibrator-vibrator-filedescription"
menu_path:
  - "参考"
  - "系统"
  - "硬件"
  - "Sensor Service Kit（传感器服务）"
  - "C API"
  - "结构体"
  - "Vibrator_FileDescription"
captured_at: "2026-04-17T01:48:34.294Z"
---

# Vibrator\_FileDescription

```c
typedef struct Vibrator_FileDescription { ... } Vibrator_FileDescription
```

#### 概述

振动文件描述。

**起始版本：** 11

**相关模块：** [Vibrator](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vibrator)

**所在头文件：** [vibrator\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vibrator-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int32\_t fd | 自定义振动序列的文件句柄。 |
| int64\_t offset | 自定义振动序列的偏移地址。 |
| int64\_t length | 自定义振动序列的总长度。 |

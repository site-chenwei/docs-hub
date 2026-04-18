---
title: "Hid_MscEventArray"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-msceventarray"
menu_path:
  - "参考"
  - "系统"
  - "硬件"
  - "Driver Development Kit（驱动开发服务）"
  - "C API"
  - "结构体"
  - "Hid_MscEventArray"
captured_at: "2026-04-17T01:48:32.807Z"
---

# Hid\_MscEventArray

```c
typedef struct Hid_MscEventArray {...} Hid_MscEventArray
```

#### 概述

其他特殊事件属性数组。

**起始版本：** 11

**相关模块：** [HidDdk](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk)

**所在头文件：** [hid\_ddk\_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hid-ddk-types-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| Hid\_MscEvent\* hidMscEvent | 其他特殊事件属性编码 |
| uint16\_t length | 数组的有效长度 |

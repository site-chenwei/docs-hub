---
title: "Hid_RelAxesArray"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-relaxesarray"
menu_path:
  - "参考"
  - "系统"
  - "硬件"
  - "Driver Development Kit（驱动开发服务）"
  - "C API"
  - "结构体"
  - "Hid_RelAxesArray"
captured_at: "2026-04-17T01:48:32.816Z"
---

# Hid\_RelAxesArray

```c
typedef struct Hid_RelAxesArray {...} Hid_RelAxesArray
```

#### 概述

相对坐标属性数组。

**起始版本：** 11

**相关模块：** [HidDdk](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk)

**所在头文件：** [hid\_ddk\_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hid-ddk-types-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| Hid\_RelAxes\* hidRelAxes | 相对坐标属性编码 |
| uint16\_t length | 数组的有效长度 |

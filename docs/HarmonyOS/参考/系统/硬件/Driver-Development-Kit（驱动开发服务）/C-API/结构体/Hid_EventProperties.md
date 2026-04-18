---
title: "Hid_EventProperties"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-eventproperties"
menu_path:
  - "参考"
  - "系统"
  - "硬件"
  - "Driver Development Kit（驱动开发服务）"
  - "C API"
  - "结构体"
  - "Hid_EventProperties"
captured_at: "2026-04-17T01:48:32.811Z"
---

# Hid\_EventProperties

```c
typedef struct Hid_EventProperties {...} Hid_EventProperties
```

#### 概述

设备关注事件属性。

**起始版本：** 11

**相关模块：** [HidDdk](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk)

**所在头文件：** [hid\_ddk\_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hid-ddk-types-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| struct Hid\_EventTypeArray hidEventTypes | 事件类型属性编码数组 |
| struct Hid\_KeyCodeArray hidKeys | 键值属性编码数组 |
| struct Hid\_AbsAxesArray hidAbs | 绝对坐标属性编码数组 |
| struct Hid\_RelAxesArray hidRelBits | 相对坐标属性编码数组 |
| struct Hid\_MscEventArray hidMiscellaneous | 其它特殊事件属性编码数组 |
| int32\_t hidAbsMax\[64\] | 绝对坐标属性最大值 |
| int32\_t hidAbsMin\[64\] | 绝对坐标属性最小值 |
| int32\_t hidAbsFuzz\[64\] | 绝对坐标属性模糊值 |
| int32\_t hidAbsFlat\[64\] | 绝对坐标属性固定值 |

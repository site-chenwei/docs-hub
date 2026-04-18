---
title: "Hid_RawDevInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-rawdevinfo"
menu_path:
  - "参考"
  - "系统"
  - "硬件"
  - "Driver Development Kit（驱动开发服务）"
  - "C API"
  - "结构体"
  - "Hid_RawDevInfo"
captured_at: "2026-04-17T01:48:32.805Z"
---

# Hid\_RawDevInfo

```c
typedef struct Hid_RawDevInfo {...} Hid_RawDevInfo
```

#### 概述

原始设备信息定义。

**起始版本：** 18

**相关模块：** [HidDdk](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk)

**所在头文件：** [hid\_ddk\_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hid-ddk-types-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t busType | 总线类型 |
| uint16\_t vendor | 供应商ID |
| uint16\_t product | 产品ID |

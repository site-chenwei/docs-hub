---
title: "Hid_Device"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-device"
menu_path:
  - "参考"
  - "系统"
  - "硬件"
  - "Driver Development Kit（驱动开发服务）"
  - "C API"
  - "结构体"
  - "Hid_Device"
captured_at: "2026-04-17T01:48:32.760Z"
---

# Hid\_Device

```c
typedef struct Hid_Device {...} Hid_Device
```

#### 概述

设备基本信息。

**起始版本：** 11

**相关模块：** [HidDdk](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk)

**所在头文件：** [hid\_ddk\_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hid-ddk-types-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| const char\* deviceName | 设备名称 |
| uint16\_t vendorId | 厂商ID |
| uint16\_t productId | 产品ID |
| uint16\_t version | 版本号 |
| uint16\_t bustype | 总线类型 |
| Hid\_DeviceProp\* properties | 由[Hid\_DeviceProp](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hid-ddk-types-h#hid_deviceprop)表示的设备特性 |
| uint16\_t propLength | 设备特性数量 |

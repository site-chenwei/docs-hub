---
title: "UsbDdkInterface"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk-usbddkinterface"
menu_path:
  - "参考"
  - "系统"
  - "硬件"
  - "Driver Development Kit（驱动开发服务）"
  - "C API"
  - "结构体"
  - "UsbDdkInterface"
captured_at: "2026-04-17T01:48:33.168Z"
---

# UsbDdkInterface

```c
typedef struct UsbDdkInterface {...} UsbDdkInterface
```

#### 概述

USB接口，是特定接口下备用设置的集合。

**起始版本：** 10

**相关模块：** [UsbDdk](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk)

**所在头文件：** [usb\_ddk\_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usb-ddk-types-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint8\_t numAltsetting | 接口的备用设置数量。 |
| struct UsbDdkInterfaceDescriptor\* altsetting | 接口的备用设置。 |

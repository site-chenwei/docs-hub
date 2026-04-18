---
title: "UsbDdkConfigDescriptor"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk-usbddkconfigdescriptor"
menu_path:
  - "参考"
  - "系统"
  - "硬件"
  - "Driver Development Kit（驱动开发服务）"
  - "C API"
  - "结构体"
  - "UsbDdkConfigDescriptor"
captured_at: "2026-04-17T01:48:33.160Z"
---

# UsbDdkConfigDescriptor

```c
typedef struct UsbDdkConfigDescriptor {...} UsbDdkConfigDescriptor
```

#### 概述

配置描述符。

**起始版本：** 10

**相关模块：** [UsbDdk](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk)

**所在头文件：** [usb\_ddk\_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usb-ddk-types-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| struct UsbConfigDescriptor configDescriptor | 标准配置描述符。 |
| struct UsbDdkInterface\* interface | 该配置所包含的接口。 |
| const uint8\_t\* extra | 未做解析的描述符，包含特定于类或供应商的描述符。 |
| uint32\_t extraLength | 未做解析的描述符长度。 |

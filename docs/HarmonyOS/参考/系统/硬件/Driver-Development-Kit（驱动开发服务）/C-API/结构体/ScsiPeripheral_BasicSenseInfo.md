---
title: "ScsiPeripheral_BasicSenseInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pi-scsiperipheralddk-scsiperipheral-basicsenseinfo"
menu_path:
  - "参考"
  - "系统"
  - "硬件"
  - "Driver Development Kit（驱动开发服务）"
  - "C API"
  - "结构体"
  - "ScsiPeripheral_BasicSenseInfo"
captured_at: "2026-04-17T01:48:33.008Z"
---

# ScsiPeripheral\_BasicSenseInfo

```c
typedef struct ScsiPeripheral_BasicSenseInfo {...} ScsiPeripheral_BasicSenseInfo
```

#### 概述

sense data的基本信息。

**起始版本：** 18

**相关模块：** [ScsiPeripheralDDK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk)

**所在头文件：** [scsi\_peripheral\_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsi-peripheral-types-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint8\_t responseCode | 响应码。 |
| bool valid | 信息有效标志位。 |
| uint64\_t information | Information字段。 |
| uint64\_t commandSpecific | Command-specific information字段。 |
| bool sksv | Sense key specific字段的标志位。 |
| uint32\_t senseKeySpecific | Sense key specific字段。 |

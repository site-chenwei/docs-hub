---
title: "ScsiPeripheral_CapacityInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk-scsiperipheral-capacityinfo"
menu_path:
  - "参考"
  - "系统"
  - "硬件"
  - "Driver Development Kit（驱动开发服务）"
  - "C API"
  - "结构体"
  - "ScsiPeripheral_CapacityInfo"
captured_at: "2026-04-17T01:48:33.007Z"
---

# ScsiPeripheral\_CapacityInfo

```c
typedef struct ScsiPeripheral_CapacityInfo {...} ScsiPeripheral_CapacityInfo
```

#### 概述

SCSI read capacity 数据。

**起始版本：** 18

**相关模块：** [ScsiPeripheralDDK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk)

**所在头文件：** [scsi\_peripheral\_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsi-peripheral-types-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t lbAddress | 返回的逻辑单元地址。 |
| uint32\_t lbLength | 单个逻辑单元长度，单位：字节。 |

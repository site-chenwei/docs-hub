---
title: "ScsiPeripheral_InquiryInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk-scsiperipheral-inquiryinfo"
menu_path:
  - "参考"
  - "系统"
  - "硬件"
  - "Driver Development Kit（驱动开发服务）"
  - "C API"
  - "结构体"
  - "ScsiPeripheral_InquiryInfo"
captured_at: "2026-04-17T01:48:32.932Z"
---

# ScsiPeripheral\_InquiryInfo

```c
typedef struct ScsiPeripheral_InquiryInfo {...} ScsiPeripheral_InquiryInfo
```

#### 概述

SCSI inquiry 数据。

**起始版本：** 18

**相关模块：** [ScsiPeripheralDDK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk)

**所在头文件：** [scsi\_peripheral\_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsi-peripheral-types-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint8\_t deviceType | 设备类型。 |
| char idVendor\[[SCSIPERIPHERAL\_VENDOR\_ID\_LEN](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsi-peripheral-types-h) + 1\] | 制造商 id。 |
| char idProduct\[[SCSIPERIPHERAL\_PRODUCT\_ID\_LEN](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsi-peripheral-types-h) + 1\] | 产品 id。 |
| char revProduct\[[SCSIPERIPHERAL\_PRODUCT\_REV\_LEN](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsi-peripheral-types-h) + 1\] | 产品版本。 |
| ScsiPeripheral\_DeviceMemMap\* data | 所有的查询数据。 |

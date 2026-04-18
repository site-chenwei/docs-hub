---
title: "ScsiPeripheral_Request"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk-scsiperipheral-request"
menu_path:
  - "参考"
  - "系统"
  - "硬件"
  - "Driver Development Kit（驱动开发服务）"
  - "C API"
  - "结构体"
  - "ScsiPeripheral_Request"
captured_at: "2026-04-17T01:48:32.920Z"
---

# ScsiPeripheral\_Request

```c
typedef struct ScsiPeripheral_Request {...} ScsiPeripheral_Request
```

#### 概述

请求参数结构体。

**起始版本：** 18

**相关模块：** [ScsiPeripheralDDK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsiperipheralddk)

**所在头文件：** [scsi\_peripheral\_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-scsi-peripheral-types-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint8\_t commandDescriptorBlock\[SCSIPERIPHERAL\_MAX\_CMD\_DESC\_BLOCK\_LEN\] | 命令描述符块。 |
| uint8\_t cdbLength | 命令描述符块的长度。 |
| int8\_t dataTransferDirection | 数据传输方向：-1为无数据传输的命令，-2为从主机到设备的数据传输(写)，-3为从设备到主机的数据传输(读)，-4为双向数据传输。 |
| ScsiPeripheral\_DeviceMemMap\* data | 数据传输的缓冲区。 |
| uint32\_t timeout | 超时时间（单位：毫秒）。 |

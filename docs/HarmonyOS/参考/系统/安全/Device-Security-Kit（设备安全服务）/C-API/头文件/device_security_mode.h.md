---
title: "device_security_mode.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-device-security-mode-8h"
menu_path:
  - "参考"
  - "系统"
  - "安全"
  - "Device Security Kit（设备安全服务）"
  - "C API"
  - "头文件"
  - "device_security_mode.h"
captured_at: "2026-04-17T01:48:19.084Z"
---

# device\_security\_mode.h

#### 概述

文件中定义了与设备安全模式相关的函数。

**引用文件：** <DeviceSecurityKit/device\_security\_mode.h>

**库：** libdevice\_security\_mode.z.so

**系统能力：** SystemCapability.Security.SafetyDetect

**起始版本：** 5.0.1(13)

**相关模块：** [DeviceSecurityMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-devicesecuritymode)

#### 汇总

#### \[h2\]类型定义

| 名称 | 描述 |
| :-- | :-- |
| typedef enum [DSM\_DeviceSecurityMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-devicesecuritymode#dsm_devicesecuritymode-1) [DSM\_DeviceSecurityMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-devicesecuritymode#dsm_devicesecuritymode) | 设备安全模式枚举类型定义。 |

#### \[h2\]枚举

| 名称 | 描述 |
| :-- | :-- |
| 
[DSM\_DeviceSecurityMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-devicesecuritymode#dsm_devicesecuritymode-1) {

DSM\_NORMAL\_MODE = 0,

DSM\_SECURE\_SHIELD\_MODE = 1

}

 | 设备安全模式枚举值。 |

#### \[h2\]函数

| 名称 | 描述 |
| :-- | :-- |
| [DSM\_DeviceSecurityMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-devicesecuritymode#dsm_devicesecuritymode-1) [HMS\_DSM\_GetDeviceSecurityMode()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-devicesecuritymode#hms_dsm_getdevicesecuritymode) | 查询当前设备安全模式。 |

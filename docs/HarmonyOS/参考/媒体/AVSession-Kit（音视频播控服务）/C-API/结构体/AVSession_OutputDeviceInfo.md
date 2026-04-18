---
title: "AVSession_OutputDeviceInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohavsession-avsession-outputdeviceinfo"
menu_path:
  - "参考"
  - "媒体"
  - "AVSession Kit（音视频播控服务）"
  - "C API"
  - "结构体"
  - "AVSession_OutputDeviceInfo"
captured_at: "2026-04-17T01:48:38.569Z"
---

# AVSession\_OutputDeviceInfo

```c
struct AVSession_OutputDeviceInfo {...}
```

#### 概述

目标设备信息的定义。

**起始版本：** 23

**相关模块：** [OHAVSession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohavsession)

**所在头文件：** [native\_deviceinfo.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-deviceinfo-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t size | 设备信息数组的大小。 |
| [AVSession\_DeviceInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohavsession-avsession-deviceinfo) \*\*deviceInfos | 设备信息数组。 |

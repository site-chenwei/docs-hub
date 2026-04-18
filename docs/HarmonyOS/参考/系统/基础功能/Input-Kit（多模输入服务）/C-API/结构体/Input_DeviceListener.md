---
title: "Input_DeviceListener"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-devicelistener"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "Input Kit（多模输入服务）"
  - "C API"
  - "结构体"
  - "Input_DeviceListener"
captured_at: "2026-04-17T01:48:30.820Z"
---

# Input\_DeviceListener

```c
typedef struct Input_DeviceListener {...} Input_DeviceListener
```

#### 概述

定义一个结构体用于监听设备热插拔。

**起始版本：** 13

**相关模块：** [input](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input)

**所在头文件：** [oh\_input\_manager.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-input-manager-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [Input\_DeviceAddedCallback](#input_deviceaddedcallback) deviceAddedCallback | 定义一个回调函数，用于接收设备热插事件。 |
| [Input\_DeviceRemovedCallback](#input_deviceremovedcallback) deviceRemovedCallback | 定义一个回调函数，用于接收设备热拔事件。 |

#### \[h2\]成员函数

| 名称 | typedef关键字 | 描述 |
| :-- | :-- | :-- |
| [typedef void (\*Input\_DeviceAddedCallback)(int32\_t deviceId)](#input_deviceaddedcallback) | Input\_DeviceAddedCallback() | 回调函数，用于接收输入设备的热插事件。 |
| [typedef void (\*Input\_DeviceRemovedCallback)(int32\_t deviceId)](#input_deviceremovedcallback) | Input\_DeviceRemovedCallback() | 回调函数，用于接收输入设备的热拔事件。 |

#### 成员函数说明

#### \[h2\]Input\_DeviceAddedCallback()

```c
typedef void (*Input_DeviceAddedCallback)(int32_t deviceId)
```

**描述**

回调函数，用于接收输入设备的热插事件。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| int32\_t deviceId | 输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。 |

#### \[h2\]Input\_DeviceRemovedCallback()

```c
typedef void (*Input_DeviceRemovedCallback)(int32_t deviceId)
```

**描述**

回调函数，用于接收输入设备的热拔事件。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| int32\_t deviceId | 输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。 |

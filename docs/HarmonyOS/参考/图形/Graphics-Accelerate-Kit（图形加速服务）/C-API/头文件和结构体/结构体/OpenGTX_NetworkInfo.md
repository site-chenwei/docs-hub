---
title: "OpenGTX_NetworkInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_open_g_t_x___network_info"
menu_path:
  - "参考"
  - "图形"
  - "Graphics Accelerate Kit（图形加速服务）"
  - "C API"
  - "头文件和结构体"
  - "结构体"
  - "OpenGTX_NetworkInfo"
captured_at: "2026-04-17T01:48:51.941Z"
---

# OpenGTX\_NetworkInfo

#### 概述

此结构体描述当前设备网络信息，游戏应用获取到网络信息后传递此参数。

**起始版本：** 5.0.0(12)

**相关模块：** [GraphicsAccelerate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate)

**所在头文件：** [opengtx\_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/opengtx__base_8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [OpenGTX\_NetworkLatency](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_open_g_t_x___network_latency) [networkLatency](#networklatency) | 游戏中的网络延迟。 如果没有上下行时延，则设置为total（总时延）的值。将游戏总时延以0ms、50ms、100ms、150ms、200ms分为5个档位，当档位发生变化时，游戏应用通知OpenGTX。 |
| char\* [networkServerIP](#networkserverip) | 游戏服务器的IP地址，字节长度范围\[1,256\]。示例："10.10.10.10"。 |

#### 结构体成员变量说明

#### \[h2\]networkLatency

```c
OpenGTX_NetworkLatency OpenGTX_NetworkInfo::networkLatency
```

**描述**

游戏中的网络延迟。 如果没有上下行时延，则设置为total（总时延）的值。将游戏总时延以0ms、50ms、100ms、150ms、200ms分为5个档位，当档位发生变化时，游戏应用通知OpenGTX。

#### \[h2\]networkServerIP

```c
char* OpenGTX_NetworkInfo::networkServerIP
```

**描述**

游戏服务器的IP地址，字节长度范围\[1,256\]。

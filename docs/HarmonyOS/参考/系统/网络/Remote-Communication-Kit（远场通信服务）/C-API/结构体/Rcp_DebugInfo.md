---
title: "Rcp_DebugInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___debug_info"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Remote Communication Kit（远场通信服务）"
  - "C API"
  - "结构体"
  - "Rcp_DebugInfo"
captured_at: "2026-04-17T01:48:26.174Z"
---

# Rcp\_DebugInfo

#### 概述

描述存储在[Rcp\_Response](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response)中的调试信息的结构。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [Rcp\_DebugEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#rcp_debugevent)[type](#type) | 调试事件类型。 |
| [Rcp\_Buffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___buffer)[data](#data) | 调试信息。 |
| struct [Rcp\_DebugInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___debug_info) \* [next](#next) | 链式存储。指向下一个[Rcp\_DebugInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___debug_info)。 |

#### 结构体成员变量说明

#### \[h2\]data

```cpp
Rcp_Buffer Rcp_DebugInfo::data
```

**描述**

调试信息。

#### \[h2\]next

```cpp
struct Rcp_DebugInfo* Rcp_DebugInfo::next
```

**描述**

链式存储。指向下一个[Rcp\_DebugInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___debug_info)。

#### \[h2\]type

```cpp
Rcp_DebugEvent Rcp_DebugInfo::type
```

**描述**

调试事件类型。

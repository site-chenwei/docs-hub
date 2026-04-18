---
title: "SecurityAudit_Event"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-structs-securityaudit-event"
menu_path:
  - "参考"
  - "系统"
  - "安全"
  - "Device Security Kit（设备安全服务）"
  - "C API"
  - "结构体"
  - "SecurityAudit_Event"
captured_at: "2026-04-17T01:48:19.132Z"
---

# SecurityAudit\_Event

#### 概述

定义审计事件信息。

**起始版本：** 6.0.0(20)

**相关模块：** [SecurityAudit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-securityaudit)

**所在头文件：** [security\_audit.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-security-audit-8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int64\_t [eventId](#eventid) | 审计事件ID。 |
| const char \* [metadata](#metadata) | 
集成了事件版本号、事件接收时间、设备ID和用户ID的json字符串。

 |
| const char \* [content](#content) | 事件内容。 |

#### 结构体成员变量说明

#### \[h2\]content

```cpp
const char* SecurityAudit_Event::content
```

**描述**

事件内容。

#### \[h2\]eventId

```cpp
int64_t SecurityAudit_Event::eventId
```

**描述**

审计事件ID。

#### \[h2\]metadata

```cpp
const char* SecurityAudit_Event::metadata
```

**描述**

集成了事件版本号、事件接收时间、设备ID和用户ID的json字符串。

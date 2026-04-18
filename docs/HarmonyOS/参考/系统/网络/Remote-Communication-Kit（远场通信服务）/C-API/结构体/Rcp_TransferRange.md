---
title: "Rcp_TransferRange"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___transfer_range"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Remote Communication Kit（远场通信服务）"
  - "C API"
  - "结构体"
  - "Rcp_TransferRange"
captured_at: "2026-04-17T01:48:26.866Z"
---

# Rcp\_TransferRange

#### 概述

HTTP传输范围。该设置将转换为HTTP Range标头。具有范围标头的HTTP请求要求服务器仅发送回HTTP响应的一部分。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int64\_t [from](#from) | 传输起始位置。 |
| bool [hasZeroFrom](#haszerofrom) | 是否从零开始。 |
| int64\_t [to](#to) | 传输结束位置。 |
| bool [hasZeroTo](#haszeroto) | 是否以零结束。 |
| struct [Rcp\_TransferRange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___transfer_range) \* [next](#next) | 链式存储。指向下一个[Rcp\_TransferRange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___transfer_range)。 |

#### 结构体成员变量说明

#### \[h2\]from

```cpp
int64_t Rcp_TransferRange::from
```

**描述**

传输起始位置。

#### \[h2\]hasZeroFrom

```cpp
bool Rcp_TransferRange::hasZeroFrom
```

**描述**

请求范围是否从零开始。

#### \[h2\]hasZeroTo

```cpp
bool Rcp_TransferRange::hasZeroTo
```

**描述**

是否以零结束。

#### \[h2\]next

```cpp
struct Rcp_TransferRange* Rcp_TransferRange::next
```

**描述**

链式存储。指向下一个[Rcp\_TransferRange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___transfer_range)。

#### \[h2\]to

```cpp
int64_t Rcp_TransferRange::to
```

**描述**

传输结束位置。

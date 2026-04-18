---
title: "Http_Buffer"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-buffer"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Network Kit（网络服务）"
  - "C API"
  - "结构体"
  - "Http_Buffer"
captured_at: "2026-04-17T01:48:23.473Z"
---

# Http\_Buffer

```c
typedef struct Http_Buffer {...} Http_Buffer
```

#### 概述

HTTP缓存结构体。

**起始版本：** 20

**相关模块：** [netstack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack)

**所在头文件：** [net\_http\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| const char \*buffer | 缓存区数据。 |
| uint32\_t length | 缓存区长度。 |

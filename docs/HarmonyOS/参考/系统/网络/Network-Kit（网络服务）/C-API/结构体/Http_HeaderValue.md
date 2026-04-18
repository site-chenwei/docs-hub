---
title: "Http_HeaderValue"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-headervalue"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Network Kit（网络服务）"
  - "C API"
  - "结构体"
  - "Http_HeaderValue"
captured_at: "2026-04-17T01:48:23.460Z"
---

# Http\_HeaderValue

```c
typedef struct Http_HeaderValue {...} Http_HeaderValue
```

#### 概述

请求或者响应的标头映射的值类型。

**起始版本：** 20

**相关模块：** [netstack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack)

**所在头文件：** [net\_http\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| char \*value | 标头键值对的值。 |
| struct Http\_HeaderValue \*next | 链式存储。指向下一个Http\_HeaderValue。 |

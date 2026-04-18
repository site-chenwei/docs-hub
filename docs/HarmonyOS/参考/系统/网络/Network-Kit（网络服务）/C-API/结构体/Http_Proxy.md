---
title: "Http_Proxy"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-proxy"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Network Kit（网络服务）"
  - "C API"
  - "结构体"
  - "Http_Proxy"
captured_at: "2026-04-17T01:48:23.551Z"
---

# Http\_Proxy

```c
typedef struct Http_Proxy {...} Http_Proxy
```

#### 概述

代理配置结构体。

**起始版本：** 20

**相关模块：** [netstack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack)

**所在头文件：** [net\_http\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [Http\_ProxyType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-type-h#http_proxytype) proxyType | 代理配置类型，参考[Http\_ProxyType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-type-h#http_proxytype)。 |
| [Http\_CustomProxy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-customproxy) customProxy | 自定义代理配置信息，参考[Http\_CustomProxy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-customproxy)。 |

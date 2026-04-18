---
title: "NetConn_ProbeResultInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-proberesultinfo"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Network Kit（网络服务）"
  - "C API"
  - "结构体"
  - "NetConn_ProbeResultInfo"
captured_at: "2026-04-17T01:48:23.310Z"
---

# NetConn\_ProbeResultInfo

```c
typedef struct NetConn_ProbeResultInfo {...} NetConn_ProbeResultInfo
```

#### 概述

定义探测结果信息。

**起始版本：** 20

**相关模块：** [NetConnection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection)

**所在头文件：** [net\_connection\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint8\_t lossRate | 丢包率，百分制，值100表示100%丢包；50表示50%丢包。 |
| uint32\_t rtt[\[NETCONN\_MAX\_RTT\_NUM\]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h#宏定义) | 时延结果，包含最小、最大、平均、标准差。 |

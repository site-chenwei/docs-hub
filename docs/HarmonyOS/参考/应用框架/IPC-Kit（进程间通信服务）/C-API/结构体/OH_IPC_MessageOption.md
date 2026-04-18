---
title: "OH_IPC_MessageOption"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohipcremoteobject-oh-ipc-messageoption"
menu_path:
  - "参考"
  - "应用框架"
  - "IPC Kit（进程间通信服务）"
  - "C API"
  - "结构体"
  - "OH_IPC_MessageOption"
captured_at: "2026-04-17T01:48:16.099Z"
---

# OH\_IPC\_MessageOption

```c
typedef struct {...} OH_IPC_MessageOption
```

#### 概述

IPC消息选项定义。

**起始版本：** 12

**相关模块：** [OHIPCRemoteObject](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohipcremoteobject)

**所在头文件：** [ipc\_cremote\_object.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ipc-cremote-object-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [OH\_IPC\_RequestMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ipc-cremote-object-h#oh_ipc_requestmode) mode | 消息请求模式。 |
| uint32\_t timeout | RPC预留参数，该参数对IPC无效。 |
| void\* reserved | 保留参数，必须为空 |

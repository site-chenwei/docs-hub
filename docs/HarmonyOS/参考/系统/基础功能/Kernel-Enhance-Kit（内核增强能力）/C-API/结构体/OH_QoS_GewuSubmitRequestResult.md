---
title: "OH_QoS_GewuSubmitRequestResult"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-qos-oh-qos-gewusubmitrequestresult"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "Kernel Enhance Kit（内核增强能力）"
  - "C API"
  - "结构体"
  - "OH_QoS_GewuSubmitRequestResult"
captured_at: "2026-04-17T01:48:32.173Z"
---

# OH\_QoS\_GewuSubmitRequestResult

```c
typedef struct { ... } OH_QoS_GewuSubmitRequestResult
```

#### 概述

OH\_QoS\_GewuSubmitRequest()接口的返回结果，成功时返回请求的 request，失败时 error 会置为对应的错误码 。

**起始版本：** 20

**相关模块：** [QoS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-qos)

**所在头文件：** [qos.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-qos-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| OH\_QoS\_GewuRequest request | 创建出来的请求句柄 |
| [OH\_QoS\_GewuErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-qos-h#oh_qos_gewuerrorcode) error | 错误码。- 请求提交成功返回OH\_QOS\_GEWU\_OK。- 由于没有足够的内存而创建会话失败返回OH\_QOS\_GEWU\_NOMEM。 |

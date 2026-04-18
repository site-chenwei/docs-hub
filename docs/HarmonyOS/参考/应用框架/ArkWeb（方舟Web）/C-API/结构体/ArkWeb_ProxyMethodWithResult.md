---
title: "ArkWeb_ProxyMethodWithResult"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-proxymethodwithresult"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkWeb（方舟Web）"
  - "C API"
  - "结构体"
  - "ArkWeb_ProxyMethodWithResult"
captured_at: "2026-04-17T01:48:13.130Z"
---

# ArkWeb\_ProxyMethodWithResult

```c
typedef struct {...} ArkWeb_ProxyMethodWithResult
```

#### 概述

注入的Proxy方法通用结构体。

**起始版本：** 18

**相关模块：** [Web](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web)

**所在头文件：** [arkweb\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| const char\* methodName | 注入的方法名。 |
| [ArkWeb\_OnJavaScriptProxyCallbackWithResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-type-h#arkweb_onjavascriptproxycallbackwithresult) callback | Proxy方法执行的回调。 |
| void\* userData | 需要在回调中携带的自定义数据。 |

---
title: "ArkWeb_ProxyObject"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-proxyobject"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkWeb（方舟Web）"
  - "C API"
  - "结构体"
  - "ArkWeb_ProxyObject"
captured_at: "2026-04-17T01:48:13.159Z"
---

# ArkWeb\_ProxyObject

```c
typedef struct {...} ArkWeb_ProxyObject
```

#### 概述

注入的Proxy对象通用结构体。

**起始版本：** 12

**相关模块：** [Web](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web)

**所在头文件：** [arkweb\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| const char\* objName | 注入的对象名。 |
| const [ArkWeb\_ProxyMethod](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-proxymethod)\* methodList | 注入的对象携带的方法结构体数组。 |
| size\_t size | 方法结构体数组的长度。 |

---
title: "JSVM_EnvScope__*"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-envscope--8h"
menu_path:
  - "参考"
  - "公共基础能力"
  - "C API"
  - "结构体"
  - "JSVM_EnvScope__*"
captured_at: "2026-04-17T01:49:06.727Z"
---

# JSVM\_EnvScope\_\_\*

```c
typedef struct JSVM_EnvScope__* JSVM_EnvScope
```

#### 概述

表示用于控制附加到当前虚拟机实例的环境。只有当线程通过OH\_JSVM\_OpenEnvScope进入该环境的JSVM\_EnvScope后，该环境才对线程的虚拟机实例可用。

**起始版本：** 11

**相关模块：** [JSVM](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm)

**所在头文件：** [jsvm\_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-types-h)

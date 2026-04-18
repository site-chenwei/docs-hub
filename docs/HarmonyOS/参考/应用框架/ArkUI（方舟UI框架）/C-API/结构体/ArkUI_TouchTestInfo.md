---
title: "ArkUI_TouchTestInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-touchtestinfo"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "C API"
  - "结构体"
  - "ArkUI_TouchTestInfo"
captured_at: "2026-04-17T01:48:10.610Z"
---

# ArkUI\_TouchTestInfo

```
typedef struct ArkUI_TouchTestInfo ArkUI_TouchTestInfo
```

#### 概述

定义触摸测试信息。

当用户通过[registerNodeEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#registernodeevent)注册了[NODE\_ON\_CHILD\_TOUCH\_TEST](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h#arkui_nodeeventtype)事件时，才能接收到此事件。触摸测试信息包含触摸测试策略、命中测试过程中需要作用的子组件ID和触摸测试信息项的列表。

**起始版本：** 22

**相关模块：** [ArkUI\_EventModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-eventmodule)

**所在头文件：** [ui\_input\_event.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ui-input-event-h)

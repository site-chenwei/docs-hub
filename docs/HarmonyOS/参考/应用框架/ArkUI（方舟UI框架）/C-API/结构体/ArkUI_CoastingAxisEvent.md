---
title: "ArkUI_CoastingAxisEvent"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-coastingaxisevent"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "C API"
  - "结构体"
  - "ArkUI_CoastingAxisEvent"
captured_at: "2026-04-17T01:48:10.588Z"
---

# ArkUI\_CoastingAxisEvent

```c
typedef struct ArkUI_CoastingAxisEvent ArkUI_CoastingAxisEvent
```

#### 概述

定义惯性滚动轴事件。

当用户在触控板上用双指滑动时，系统会根据手指抬起时的速度，按照一定的衰减曲线构造滑动事件。可以监听此类事件，以便在常规轴事件之后立即处理抛滑效果。

仅当用户在触控板上双指抛滑，且指针位置下存在通过[registerNodeEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#registernodeevent)注册了[NODE\_ON\_COASTING\_AXIS\_EVENT](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h#arkui_nodeeventtype)事件的组件时，才能接收到此事件。

**起始版本：** 22

**相关模块：** [ArkUI\_EventModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-eventmodule)

**所在头文件：** [ui\_input\_event.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ui-input-event-h)

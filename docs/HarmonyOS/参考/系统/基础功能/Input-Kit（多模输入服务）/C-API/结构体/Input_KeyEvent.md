---
title: "Input_KeyEvent"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-keyevent"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "Input Kit（多模输入服务）"
  - "C API"
  - "结构体"
  - "Input_KeyEvent"
captured_at: "2026-04-17T01:48:30.890Z"
---

# Input\_KeyEvent

```c
typedef struct Input_KeyEvent Input_KeyEvent
```

#### 概述

按键事件对象。

**起始版本：** 12

**相关模块：** [input](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input)

**所在头文件：** [oh\_input\_manager.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-input-manager-h)

**相关接口：**

| 名称 | 描述 |
| :-- | :-- |
| [OH\_Input\_CreateKeyEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-input-manager-h#oh_input_createkeyevent) | 创建按键事件对象。通过调用[OH\_Input\_DestroyKeyEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-input-manager-h#oh_input_destroykeyevent)销毁按键事件对象。 |
| [OH\_Input\_DestroyKeyEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-input-manager-h#oh_input_destroykeyevent) | 销毁按键事件对象。 |

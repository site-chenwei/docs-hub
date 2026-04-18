---
title: "Input_KeyState"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-keystate"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "Input Kit（多模输入服务）"
  - "C API"
  - "结构体"
  - "Input_KeyState"
captured_at: "2026-04-17T01:48:30.866Z"
---

# Input\_KeyState

```c
typedef struct Input_KeyState Input_KeyState
```

#### 概述

定义按键信息，用于标识按键行为。例如，“Ctrl”按键信息包含键值和键类型。

**起始版本：** 12

**相关模块：** [input](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input)

**所在头文件：** [oh\_input\_manager.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-input-manager-h)

**相关接口：**

| 名称 | 描述 |
| :-- | :-- |
| [OH\_Input\_CreateKeyState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-input-manager-h#oh_input_createkeystate) | 创建按键状态的枚举对象。通过调用[OH\_Input\_DestroyKeyState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-input-manager-h#oh_input_destroykeystate)销毁按键状态的枚举对象。 |
| [OH\_Input\_DestroyKeyState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-input-manager-h#oh_input_destroykeystate) | 销毁按键状态的枚举对象。 |

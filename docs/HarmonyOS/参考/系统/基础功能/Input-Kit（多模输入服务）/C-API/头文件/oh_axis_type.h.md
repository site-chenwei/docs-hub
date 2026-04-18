---
title: "oh_axis_type.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-axis-type-h"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "Input Kit（多模输入服务）"
  - "C API"
  - "头文件"
  - "oh_axis_type.h"
captured_at: "2026-04-17T01:48:30.759Z"
---

# oh\_axis\_type.h

#### 概述

输入设备的轴事件结构和枚举。

**引用文件：** <multimodalinput/oh\_axis\_type.h>

**库：** libohinput.so

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**相关模块：** [input](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input)

#### 汇总

#### \[h2\]枚举

| 名称 | typedef关键字 | 描述 |
| :-- | :-- | :-- |
| [InputEvent\_AxisType](#inputevent_axistype) | InputEvent\_AxisType | 输入设备的轴类型。 |
| [InputEvent\_AxisEventType](#inputevent_axiseventtype) | InputEvent\_AxisEventType | 输入设备的轴事件类型。 |
| [InputEvent\_AxisAction](#inputevent_axisaction) | InputEvent\_AxisAction | 轴事件动作。 |

#### 枚举类型说明

#### \[h2\]InputEvent\_AxisType

```c
enum InputEvent_AxisType
```

**描述**

输入设备的轴类型。

**起始版本：** 12

| 枚举项 | 描述 |
| :-- | :-- |
| AXIS\_TYPE\_UNKNOWN | 未知轴类型，通常作为初始值。 |
| AXIS\_TYPE\_SCROLL\_VERTICAL | 垂直滚动轴，当您滚动鼠标滚轮或在触控板上进行单指或双指滑动时，垂直滚动轴的状态改变。 |
| AXIS\_TYPE\_SCROLL\_HORIZONTAL | 水平滚动轴，当您滚动鼠标滚轮或在触控板上进行双指滑动时，水平滚动轴的状态发生变化。 |
| AXIS\_TYPE\_PINCH | 捏合轴，用于描述触控板上的双指捏合手势。 |
| AXIS\_TYPE\_ROTATE | 旋转轴，用于描述触控板上的双指旋转手势。 |

#### \[h2\]InputEvent\_AxisEventType

```c
enum InputEvent_AxisEventType
```

**描述**

输入设备的轴事件类型。

**起始版本：** 12

| 枚举项 | 描述 |
| :-- | :-- |
| AXIS\_EVENT\_TYPE\_PINCH = 1 | 
双指捏合事件，包含AXIS\_TYPE\_PINCH和AXIS\_TYPE\_ROTATE两种轴类型。

**起始版本：** 12。

 |
| AXIS\_EVENT\_TYPE\_SCROLL = 2 | 

滚轴事件，包含AXIS\_TYPE\_SCROLL\_VERTICAL和AXIS\_TYPE\_SCROLL\_HORIZONTAL两种轴类型，其中鼠标滚轮事件仅包含AXIS\_TYPE\_SCROLL\_VERTICAL一种轴类型。

**起始版本：** 12。

 |

#### \[h2\]InputEvent\_AxisAction

```c
enum InputEvent_AxisAction
```

**描述**

轴事件动作。

**起始版本：** 12

| 枚举项 | 描述 |
| :-- | :-- |
| AXIS\_ACTION\_CANCEL = 0 | 取消轴输入事件。 |
| AXIS\_ACTION\_BEGIN | 开始轴输入事件。 |
| AXIS\_ACTION\_UPDATE | 轴输入事件中。 |
| AXIS\_ACTION\_END | 结束轴输入事件。 |

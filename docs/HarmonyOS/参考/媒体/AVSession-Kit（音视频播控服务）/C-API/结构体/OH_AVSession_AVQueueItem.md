---
title: "OH_AVSession_AVQueueItem"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohavsession-oh-avsession-avqueueitem"
menu_path:
  - "参考"
  - "媒体"
  - "AVSession Kit（音视频播控服务）"
  - "C API"
  - "结构体"
  - "OH_AVSession_AVQueueItem"
captured_at: "2026-04-17T01:48:38.543Z"
---

# OH\_AVSession\_AVQueueItem

```c
typedef struct {...} OH_AVSession_AVQueueItem
```

#### 概述

音视频队列元素的定义。

**起始版本：** 23

**相关模块：** [OHAVSession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohavsession)

**所在头文件：** [native\_avqueueitem.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avqueueitem-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t itemId | 资源ID。 |
| [OH\_AVSession\_AVMediaDescription](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohavsession-oh-avsession-avmediadescription) \*description | 媒体项信息。 |

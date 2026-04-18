---
title: "AVSession_PlaybackPosition"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohavsession-avsession-playbackposition"
menu_path:
  - "参考"
  - "媒体"
  - "AVSession Kit（音视频播控服务）"
  - "C API"
  - "结构体"
  - "AVSession_PlaybackPosition"
captured_at: "2026-04-17T01:48:38.482Z"
---

# AVSession\_PlaybackPosition

```c
typedef struct AVSession_PlaybackPosition {...} AVSession_PlaybackPosition
```

#### 概述

媒体播放位置的相关属性。

**起始版本：** 13

**相关模块：** [OHAVSession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohavsession)

**所在头文件：** [native\_avplaybackstate.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avplaybackstate-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int64\_t elapsedTime | 已用时间，单位毫秒（ms）。 |
| int64\_t updateTime | 更新时间，单位毫秒（ms）。 |

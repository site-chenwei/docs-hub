---
title: "OH_MediaKeySession_Callback"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-oh-mediakeysession-callback"
menu_path:
  - "参考"
  - "媒体"
  - "DRM Kit（数字版权保护服务）"
  - "C API"
  - "结构体"
  - "OH_MediaKeySession_Callback"
captured_at: "2026-04-17T01:48:40.675Z"
---

# OH\_MediaKeySession\_Callback

```c
typedef struct OH_MediaKeySession_Callback {...} OH_MediaKeySession_Callback
```

#### 概述

OH\_MediaKeySession\_Callback结构体，用于监听密钥过期、密钥更改等事件，返回媒体密钥会话实例，适用多个媒体密钥会话解密场景。

**起始版本：** 12

**相关模块：** [Drm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm)

**所在头文件：** [native\_mediakeysession.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-mediakeysession-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [OH\_MediaKeySession\_EventCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-mediakeysession-h#oh_mediakeysession_eventcallback) eventCallback | 正常事件回调，如密钥过期等。 |
| [OH\_MediaKeySession\_KeyChangeCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-mediakeysession-h#oh_mediakeysession_keychangecallback) keyChangeCallback | 密钥更改事件的密钥更改回调。 |

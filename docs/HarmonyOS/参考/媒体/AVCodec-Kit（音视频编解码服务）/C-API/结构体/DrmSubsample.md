---
title: "DrmSubsample"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-multimedia-drm-drmsubsample"
menu_path:
  - "参考"
  - "媒体"
  - "AVCodec Kit（音视频编解码服务）"
  - "C API"
  - "结构体"
  - "DrmSubsample"
captured_at: "2026-04-17T01:48:37.603Z"
---

# DrmSubsample

```c
typedef struct DrmSubsample {...} DrmSubsample
```

#### 概述

Subsample结构类型定义。

**起始版本：** 12

**相关模块：** [Multimedia\_Drm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-multimedia-drm)

**所在头文件：** [native\_cencinfo.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-cencinfo-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t clearHeaderLen | 头部清流数据的长度。 |
| uint32\_t payLoadLen | 加密数据的长度。 |

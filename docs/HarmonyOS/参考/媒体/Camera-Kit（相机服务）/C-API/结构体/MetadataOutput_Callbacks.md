---
title: "MetadataOutput_Callbacks"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-metadataoutput-callbacks"
menu_path:
  - "参考"
  - "媒体"
  - "Camera Kit（相机服务）"
  - "C API"
  - "结构体"
  - "MetadataOutput_Callbacks"
captured_at: "2026-04-17T01:48:40.058Z"
---

# MetadataOutput\_Callbacks

```c
typedef struct MetadataOutput_Callbacks {...} MetadataOutput_Callbacks
```

#### 概述

元数据输出的回调。

**起始版本：** 11

**相关模块：** [OH\_Camera](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera)

**所在头文件：** [metadata\_output.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-metadata-output-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [OH\_MetadataOutput\_OnMetadataObjectAvailable](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-metadata-output-h#oh_metadataoutput_onmetadataobjectavailable) onMetadataObjectAvailable | 此回调将调用元数据输出结果数据。 |
| [OH\_MetadataOutput\_OnError](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-metadata-output-h#oh_metadataoutput_onerror) onError | 元数据输出错误事件。 |

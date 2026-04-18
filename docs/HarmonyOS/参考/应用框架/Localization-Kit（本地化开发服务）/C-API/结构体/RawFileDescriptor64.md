---
title: "RawFileDescriptor64"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rawfile-rawfiledescriptor64"
menu_path:
  - "参考"
  - "应用框架"
  - "Localization Kit（本地化开发服务）"
  - "C API"
  - "结构体"
  - "RawFileDescriptor64"
captured_at: "2026-04-17T01:48:16.694Z"
---

# RawFileDescriptor64

```c
typedef struct {...} RawFileDescriptor64
```

#### 概述

提供较大rawfile文件描述符信息。RawFileDescriptor64是[OH\_ResourceManager\_GetRawFileDescriptor64](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-raw-file-h#oh_resourcemanager_getrawfiledescriptor64)的输出参数,涵盖了rawfile文件的文件描述符以及在HAP包中的起始位置和长度。

**起始版本：** 11

**相关模块：** [rawfile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rawfile)

**所在头文件：** [raw\_file.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-raw-file-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int fd | rawfile文件描述符，单位为int。 |
| int64\_t start | rawfile在HAP包中的起始位置，单位为int64\_t。 |
| int64\_t length | rawfile在HAP包中的长度，单位为int64\_t。 |

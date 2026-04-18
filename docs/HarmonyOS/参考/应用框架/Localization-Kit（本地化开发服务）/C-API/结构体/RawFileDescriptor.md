---
title: "RawFileDescriptor"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rawfile-rawfiledescriptor"
menu_path:
  - "参考"
  - "应用框架"
  - "Localization Kit（本地化开发服务）"
  - "C API"
  - "结构体"
  - "RawFileDescriptor"
captured_at: "2026-04-17T01:48:16.689Z"
---

# RawFileDescriptor

```c
typedef struct {...} RawFileDescriptor
```

#### 概述

提供rawfile文件描述符信息。RawFileDescriptor是[OH\_ResourceManager\_GetRawFileDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-raw-file-h#oh_resourcemanager_getrawfiledescriptor)的输出参数，涵盖了rawfile文件的文件描述符以及在HAP包中的起始位置和长度。

**起始版本：** 8

**相关模块：** [rawfile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rawfile)

**所在头文件：** [raw\_file.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-raw-file-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int fd | rawfile文件描述符，单位为int。 |
| long start | rawfile在HAP包中的起始位置，单位为long。 |
| long length | rawfile在HAP包中的长度，单位为long。 |

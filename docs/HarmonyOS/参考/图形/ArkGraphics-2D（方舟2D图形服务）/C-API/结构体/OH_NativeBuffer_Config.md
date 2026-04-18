---
title: "OH_NativeBuffer_Config"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativebuffer-oh-nativebuffer-config"
menu_path:
  - "参考"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "C API"
  - "结构体"
  - "OH_NativeBuffer_Config"
captured_at: "2026-04-17T01:48:49.867Z"
---

# OH\_NativeBuffer\_Config

```c
typedef struct {...} OH_NativeBuffer_Config
```

#### 概述

OH\_NativeBuffer的属性配置，用于申请新的OH\_NativeBuffer实例或查询现有实例的相关属性。

**起始版本：** 9

**相关模块：** [OH\_NativeBuffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativebuffer)

**所在头文件：** [native\_buffer.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-buffer-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int32\_t width | 宽度（像素）。 |
| int32\_t height | 高度（像素）。 |
| int32\_t format | 像素格式，具体可参见[OH\_NativeBuffer\_Format](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-buffer-common-h#oh_nativebuffer_format)枚举。 |
| int32\_t usage | buffer的用途说明，具体可参见[OH\_NativeBuffer\_Usage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-buffer-h#oh_nativebuffer_usage)枚举。 |
| int32\_t stride | 
输出参数。本地窗口缓冲区步幅，单位为Byte。

**起始版本：** 10

 |

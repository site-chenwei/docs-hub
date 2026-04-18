---
title: "OH_NativeBuffer_Smpte2086"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativebuffer-oh-nativebuffer-smpte2086"
menu_path:
  - "参考"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "C API"
  - "结构体"
  - "OH_NativeBuffer_Smpte2086"
captured_at: "2026-04-17T01:48:49.749Z"
---

# OH\_NativeBuffer\_Smpte2086

```c
typedef struct OH_NativeBuffer_Smpte2086 {...} OH_NativeBuffer_Smpte2086
```

#### 概述

表示smpte2086静态元数据。

**起始版本：** 12

**相关模块：** [OH\_NativeBuffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativebuffer)

**所在头文件：** [buffer\_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-buffer-common-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [OH\_NativeBuffer\_ColorXY](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativebuffer-oh-nativebuffer-colorxy) displayPrimaryRed | 红基色。 |
| [OH\_NativeBuffer\_ColorXY](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativebuffer-oh-nativebuffer-colorxy) displayPrimaryGreen | 绿基色。 |
| [OH\_NativeBuffer\_ColorXY](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativebuffer-oh-nativebuffer-colorxy) displayPrimaryBlue | 蓝基色。 |
| [OH\_NativeBuffer\_ColorXY](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativebuffer-oh-nativebuffer-colorxy) whitePoint | 白点。 |
| float maxLuminance | 最大的光亮度。 |
| float minLuminance | 最小的光亮度。 |

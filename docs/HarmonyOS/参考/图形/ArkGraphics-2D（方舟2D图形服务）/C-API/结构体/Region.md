---
title: "Region"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativewindow-region"
menu_path:
  - "参考"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "C API"
  - "结构体"
  - "Region"
captured_at: "2026-04-17T01:48:50.342Z"
---

# Region

```c
typedef struct {...} Region
```

#### 概述

表示本地窗口OHNativeWindow需要更新内容的矩形区域（脏区）。

**起始版本：** 8

**相关模块：** [NativeWindow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativewindow)

**所在头文件：** [external\_window.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-external-window-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| \* rects | 如果rects是空指针nullptr，默认Buffer大小为脏区。 |
| int32\_t rectNumber | 如果rectNumber为0，默认Buffer大小为脏区。 |

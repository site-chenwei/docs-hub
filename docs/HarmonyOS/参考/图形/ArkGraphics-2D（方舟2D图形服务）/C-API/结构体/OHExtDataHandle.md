---
title: "OHExtDataHandle"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativewindow-ohextdatahandle"
menu_path:
  - "参考"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "C API"
  - "结构体"
  - "OHExtDataHandle"
captured_at: "2026-04-17T01:48:50.353Z"
---

# OHExtDataHandle

```c
typedef struct OHExtDataHandle {...} OHExtDataHandle
```

#### 概述

扩展数据句柄结构体定义。

**起始版本：** 9

**废弃版本：** 从API version 10开始废弃，不再提供替代接口。

**相关模块：** [NativeWindow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativewindow)

**所在头文件：** [external\_window.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-external-window-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int32\_t fd | 句柄 Fd，-1代表不支持。 |
| uint32\_t reserveInts | Reserve数组的个数。 |
| int32\_t reserve\[0\] | Reserve数组。 |

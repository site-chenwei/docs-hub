---
title: "Print_PrintDocCallback"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-printdoccallback"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "Basic Services Kit（基础服务）"
  - "C API"
  - "结构体"
  - "Print_PrintDocCallback"
captured_at: "2026-04-17T01:48:29.468Z"
---

# Print\_PrintDocCallback

```c
typedef struct {...} Print_PrintDocCallback
```

#### 概述

表示打印文档状态回调结构体。

**起始版本：** 13

**相关模块：** [OH\_Print](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print)

**所在头文件：** [ohprint.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohprint-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [Print\_OnStartLayoutWrite](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohprint-h#print_onstartlayoutwrite) startLayoutWriteCb | 打印开始布局回调。 |
| [Print\_OnJobStateChanged](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohprint-h#print_onjobstatechanged) jobStateChangedCb | 打印任务状态回调。 |

---
title: "JSVM_HeapStatistics"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-heapstatistics"
menu_path:
  - "参考"
  - "公共基础能力"
  - "C API"
  - "结构体"
  - "JSVM_HeapStatistics"
captured_at: "2026-04-17T01:49:06.466Z"
---

# JSVM\_HeapStatistics

```c
typedef struct {...} JSVM_HeapStatistics
```

#### 概述

用于保存有关JavaScript堆内存使用情况的统计信息。

**起始版本：** 12

**相关模块：** [JSVM](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm)

**所在头文件：** [jsvm\_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-types-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| size\_t totalHeapSize | 总堆大小，单位KB。 |
| size\_t totalHeapSizeExecutable | 可执行堆的总大小，单位KB。 |
| size\_t totalPhysicalSize | 总的物理内存大小，单位KB。 |
| size\_t totalAvailableSize | 总的可用内存大小，单位KB。 |
| size\_t usedHeapSize | 已使用的堆大小，单位KB。 |
| size\_t heapSizeLimit | 堆大小限制，单位KB。 |
| size\_t mallocedMemory | 已分配内存的大小，单位KB。 |
| size\_t externalMemory | 外部内存大小，单位KB。 |
| size\_t peakMallocedMemory | 最大可分配内存的大小，单位KB。 |
| size\_t numberOfNativeContexts | 表示当前活跃的native上下文的数量，该数值一直增加可能指示存在内存泄漏。 |
| size\_t numberOfDetachedContexts | 表示已经脱离的上下文数量。 |
| size\_t totalGlobalHandlesSize | 全局Handle的总大小，单位KB。 |
| size\_t usedGlobalHandlesSize | 已经使用的全局Handle的大小，单位KB。 |

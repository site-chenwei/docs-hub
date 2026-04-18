---
title: "fast_solver_rect_partition.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-solver-rect-partition-8h"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "FAST Kit（算法加速服务）"
  - "C API"
  - "头文件和结构体"
  - "头文件"
  - "fast_solver_rect_partition.h"
captured_at: "2026-04-17T01:48:29.960Z"
---

# fast\_solver\_rect\_partition.h

#### 概述

矩形划分求解器相关数据结构及函数定义。

**引用文件：** <FASTKit/fast\_solver\_rect\_partition.h>

**库：** libfast\_solver.so

**系统能力：** SystemCapability.FAST.Core

**起始版本：** 6.0.2(22)

**相关模块：** [FAST](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast)

#### 汇总

#### \[h2\]结构体

| 名称 | 描述 |
| :-- | :-- |
| struct [FAST\_Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-rect) | 定义矩形的数据结构（坐标系说明：X轴从左到右递增，Y轴从上到下递增）。 |

#### \[h2\]类型定义

| 名称 | 描述 |
| :-- | :-- |
| typedef struct [FAST\_Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-rect) [FAST\_Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast#fast_rect) | 定义矩形的数据结构。 |
| typedef struct [FAST\_RectPartitionConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast#fast_rectpartitionconfig) [FAST\_RectPartitionConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast#fast_rectpartitionconfig) | 矩形划分求解器的不透明配置。 |

#### \[h2\]函数

| 名称 | 描述 |
| :-- | :-- |
| FAST\_EXPORT [FAST\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast#fast_errorcode-1) [HMS\_FAST\_RectPartition\_CreateConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast#hms_fast_rectpartition_createconfig) ([FAST\_RectPartitionConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast#fast_rectpartitionconfig) \*\*config) | 创建矩形划分求解器的不透明配置。 |
| FAST\_EXPORT void [HMS\_FAST\_RectPartition\_DestroyConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast#hms_fast_rectpartition_destroyconfig) ([FAST\_RectPartitionConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast#fast_rectpartitionconfig) \*config) | 销毁矩形划分求解器的不透明配置。 |
| FAST\_EXPORT [FAST\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast#fast_errorcode-1) [HMS\_FAST\_RectPartition\_SetAlgo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast#hms_fast_rectpartition_setalgo) ([FAST\_RectPartitionConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast#fast_rectpartitionconfig) \*config, const char \*name) | 设置矩形划分求解器使用的算法。目前仅支持扫描线算法“SweepLineAlgo”，输出数量尽可能少（不保证最优性）的不相交矩形集合，复杂度为![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/ZejvesCrTKmbKd4kYD7V7w/zh-cn_image_0000002538021494.png?HW-CC-KV=V1&HW-CC-Date=20260417T014831Z&HW-CC-Expire=86400&HW-CC-Sign=4D6A6CF2C4F226594FF2A6CD07B2E113199F67FA860890855674F73A38E1908A)。 |
| FAST\_EXPORT [FAST\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast#fast_errorcode-1) [HMS\_FAST\_RectPartition\_Solve](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast#hms_fast_rectpartition_solve) ([FAST\_RectPartitionConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast#fast_rectpartitionconfig) \*config, size\_t size, const [FAST\_Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-rect) \*origin, [FAST\_Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-rect) \*result, size\_t \*resultSize) | 
在指定不透明配置下解决矩形划分问题。函数接收若干个彼此不相交的矩形作为输入，计算出覆盖相同区域的矩形划分方案，并使输出的矩形数量尽可能少。

**说明**：

1\. 输入须保证矩形两两不相交（即任意两个矩形满足：![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/i9G0XkNpQVKwEvrWtr9TRQ/zh-cn_image_0000002538181420.png?HW-CC-KV=V1&HW-CC-Date=20260417T014831Z&HW-CC-Expire=86400&HW-CC-Sign=E22C1A16612B508E0075BF75439B9FD94BC5A088BA6273175FAF99CA20AA7132) 或 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/Pk3y8kdsS2iAmsoVdyPv9w/zh-cn_image_0000002569021207.png?HW-CC-KV=V1&HW-CC-Date=20260417T014831Z&HW-CC-Expire=86400&HW-CC-Sign=165608CCC9329C070D23A506A7922C0C1564C9B42DF01441E0F9C00FD3C48ECE)或![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/0rT0qqcjRq208EYO-ZIUjA/zh-cn_image_0000002568901197.png?HW-CC-KV=V1&HW-CC-Date=20260417T014831Z&HW-CC-Expire=86400&HW-CC-Sign=D547F4F0B9347A3FD64EC2F9C29ACCAC912FA3DEA8EFC886C14F439C7B85B5D6)或 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/d8SYm2ilQeCLxQ7SSa1eZg/zh-cn_image_0000002538021496.png?HW-CC-KV=V1&HW-CC-Date=20260417T014831Z&HW-CC-Expire=86400&HW-CC-Sign=5E0DD9FE9C22F974605EE8A99EE333DE119EA0745BDDEC25E1944B8B3E369A5D)），否则函数返回FAST\_ERROR\_CODE\_ILLEGAL\_INPUT。

2\. 函数保证输出矩形的数量小于等于输入矩形的数量。

 |

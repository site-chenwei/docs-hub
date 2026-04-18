---
title: "FAST"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "FAST Kit（算法加速服务）"
  - "C API"
  - "模块"
  - "FAST"
captured_at: "2026-04-17T01:48:29.958Z"
---

# FAST

#### 概述

提供FAST算法加速能力相关接口，实现应用启动、加载、响应时延等指标的优化。

**起始版本：** 6.0.2(22)

#### 汇总

概述FAST Kit中文件、结构体、宏定义、类型定义、枚举和函数等信息。

#### \[h2\]文件

| 名称 | 描述 |
| :-- | :-- |
| [fast\_ads\_segment\_map.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-ads-segment-map-8h) | 线段表相关数据结构及函数定义。 |
| [fast\_common\_def.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-common-def-8h) | FAST Kit错误码等类型的公共定义。 |
| [fast\_solver\_rect\_partition.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-solver-rect-partition-8h) | 矩形划分求解器相关数据结构及函数定义。 |

#### \[h2\]结构体

| 名称 | 描述 |
| :-- | :-- |
| struct [FAST\_Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-rect) | 定义矩形的数据结构。 |

#### \[h2\]类型定义

| 名称 | 描述 |
| :-- | :-- |
| typedef enum [FAST\_SegmentMapQueryType](#fast_segmentmapquerytype-1) [FAST\_SegmentMapQueryType](#fast_segmentmapquerytype) | 线段表支持的查询操作类型。 |
| typedef enum [FAST\_SegmentMapUpdateType](#fast_segmentmapupdatetype-1) [FAST\_SegmentMapUpdateType](#fast_segmentmapupdatetype) | 线段表支持的更新操作类型。 |
| typedef struct [FAST\_SegmentMapConfig](#fast_segmentmapconfig) [FAST\_SegmentMapConfig](#fast_segmentmapconfig) | 线段表的不透明配置（Opaque Configuration）。 |
| typedef void \* [FAST\_SegmentMapHandle](#fast_segmentmaphandle) | 线段表的句柄。 |
| typedef enum [FAST\_ErrorCode](#fast_errorcode-1) [FAST\_ErrorCode](#fast_errorcode) | FAST Kit的错误码。 |
| typedef struct [FAST\_Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-rect) [FAST\_Rect](#fast_rect) | 定义矩形的数据结构。 |
| typedef struct [FAST\_RectPartitionConfig](#fast_rectpartitionconfig) [FAST\_RectPartitionConfig](#fast_rectpartitionconfig) | 矩形划分求解器的不透明配置。 |

#### \[h2\]枚举

| 名称 | 描述 |
| :-- | :-- |
| [FAST\_SegmentMapQueryType](#fast_segmentmapquerytype-1) { FAST\_SEGMENTMAP\_QUERY\_TYPE\_SUM = 0, FAST\_SEGMENTMAP\_QUERY\_TYPE\_MIN = 1, FAST\_SEGMENTMAP\_QUERY\_TYPE\_MAX = 2 } | 线段表支持的查询操作类型。 |
| [FAST\_SegmentMapUpdateType](#fast_segmentmapupdatetype-1) { FAST\_SEGMENTMAP\_UPDATE\_TYPE\_SET = 0, FAST\_SEGMENTMAP\_UPDATE\_TYPE\_ADD = 1, FAST\_SEGMENTMAP\_UPDATE\_TYPE\_SUB = 2 } | 线段表支持的更新操作类型。 |
| 
[FAST\_ErrorCode](#fast_errorcode-1) {

FAST\_ERROR\_CODE\_SUCCESS = 1023100000, FAST\_ERROR\_CODE\_FAIL = 1023100001, FAST\_ERROR\_CODE\_ILLEGAL\_INPUT = 1023100002, FAST\_ERROR\_CODE\_INVALID\_PTR = 1023100003,

FAST\_ERROR\_CODE\_OOM = 1023199001

}

 | FAST Kit的错误码。 |

#### \[h2\]函数

| 名称 | 描述 |
| :-- | :-- |
| FAST\_EXPORT [FAST\_ErrorCode](#fast_errorcode-1) [HMS\_FAST\_SegmentMap\_CreateConfig](#hms_fast_segmentmap_createconfig) ([FAST\_SegmentMapConfig](#fast_segmentmapconfig) \*\*config) | 创建线段表不透明配置实例。 |
| FAST\_EXPORT void [HMS\_FAST\_SegmentMap\_DestroyConfig](#hms_fast_segmentmap_destroyconfig) ([FAST\_SegmentMapConfig](#fast_segmentmapconfig) \*config) | 销毁线段表的不透明配置实例并释放内存。 |
| FAST\_EXPORT [FAST\_ErrorCode](#fast_errorcode-1) [HMS\_FAST\_SegmentMap\_SetQueryType](#hms_fast_segmentmap_setquerytype) ([FAST\_SegmentMapConfig](#fast_segmentmapconfig) \*config, [FAST\_SegmentMapQueryType](#fast_segmentmapquerytype-1) type) | 设置线段表不透明配置中的查询类型。 |
| FAST\_EXPORT [FAST\_ErrorCode](#fast_errorcode-1) [HMS\_FAST\_SegmentMap\_SetUpdateType](#hms_fast_segmentmap_setupdatetype) ([FAST\_SegmentMapConfig](#fast_segmentmapconfig) \*config, [FAST\_SegmentMapUpdateType](#fast_segmentmapupdatetype-1) type) | 设置线段表不透明配置中的更新类型。 |
| FAST\_EXPORT [FAST\_ErrorCode](#fast_errorcode-1) [HMS\_FAST\_SegmentMap\_Create](#hms_fast_segmentmap_create) ([FAST\_SegmentMapHandle](#fast_segmentmaphandle) \*handle, size\_t size, const int32\_t \*array, [FAST\_SegmentMapConfig](#fast_segmentmapconfig) \*config) | 创建线段表。 |
| FAST\_EXPORT void [HMS\_FAST\_SegmentMap\_Destroy](#hms_fast_segmentmap_destroy) ([FAST\_SegmentMapHandle](#fast_segmentmaphandle) handle) | 销毁线段表实例。 |
| FAST\_EXPORT [FAST\_ErrorCode](#fast_errorcode-1) [HMS\_FAST\_SegmentMap\_Update](#hms_fast_segmentmap_update) ([FAST\_SegmentMapHandle](#fast_segmentmaphandle) handle, size\_t left, size\_t right, int32\_t value) | 更新线段表的区间。 |
| FAST\_EXPORT [FAST\_ErrorCode](#fast_errorcode-1) [HMS\_FAST\_SegmentMap\_Query](#hms_fast_segmentmap_query) ([FAST\_SegmentMapHandle](#fast_segmentmaphandle) handle, size\_t left, size\_t right, int32\_t \*result) | 查询线段表的区间。 |
| FAST\_EXPORT [FAST\_ErrorCode](#fast_errorcode-1) [HMS\_FAST\_RectPartition\_CreateConfig](#hms_fast_rectpartition_createconfig) ([FAST\_RectPartitionConfig](#fast_rectpartitionconfig) \*\*config) | 创建矩形划分求解器的不透明配置。 |
| FAST\_EXPORT void [HMS\_FAST\_RectPartition\_DestroyConfig](#hms_fast_rectpartition_destroyconfig) ([FAST\_RectPartitionConfig](#fast_rectpartitionconfig) \*config) | 销毁矩形划分求解器的不透明配置。 |
| FAST\_EXPORT [FAST\_ErrorCode](#fast_errorcode-1) [HMS\_FAST\_RectPartition\_SetAlgo](#hms_fast_rectpartition_setalgo) ([FAST\_RectPartitionConfig](#fast_rectpartitionconfig) \*config, const char \*name) | 设置矩形划分求解器使用的算法。目前仅支持扫描线算法“SweepLineAlgo”，输出数量尽可能少（不保证最优性）的不相交矩形集合，复杂度为![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/qHgbXdudQJ2mpoFiC7rAyQ/zh-cn_image_0000002569021203.png?HW-CC-KV=V1&HW-CC-Date=20260417T014831Z&HW-CC-Expire=86400&HW-CC-Sign=62DB7714D057E67C52620E8F2AC09180EF72020B56BD3EF1B181C078354F9B69)。 |
| FAST\_EXPORT [FAST\_ErrorCode](#fast_errorcode-1) [HMS\_FAST\_RectPartition\_Solve](#hms_fast_rectpartition_solve) ([FAST\_RectPartitionConfig](#fast_rectpartitionconfig) \*config, size\_t size, const [FAST\_Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-rect) \*origin, [FAST\_Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-rect) \*result, size\_t \*resultSize) | 
在指定不透明配置下解决矩形划分问题。函数接收若干个彼此不相交的矩形作为输入，计算出覆盖相同区域的矩形划分方案，并使输出的矩形数量尽可能少。

**说明**：

1\. 输入须保证矩形两两不相交（即任意两个矩形满足：![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/3AO-wYRxT_Wj-2M1OpCHGw/zh-cn_image_0000002568901193.png?HW-CC-KV=V1&HW-CC-Date=20260417T014831Z&HW-CC-Expire=86400&HW-CC-Sign=BE4E30608574A29842F620FC42AA05B8EE4C6EDCA16576E3D3716C45B2A75F1E) 或 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/sGKT297qS-e3fcBVvxRAKQ/zh-cn_image_0000002538021492.png?HW-CC-KV=V1&HW-CC-Date=20260417T014831Z&HW-CC-Expire=86400&HW-CC-Sign=B95D0D6AEBE8BBA10711F8B86E75299683570BC6B57096937FE3E242B7786FC2)或![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/2pksNvQnRWigKLwop5OhLA/zh-cn_image_0000002538181418.png?HW-CC-KV=V1&HW-CC-Date=20260417T014831Z&HW-CC-Expire=86400&HW-CC-Sign=34504FD615DDF6CA8AA1DFA7016BA6D6DD3D1729F4AD866D0E293B2745538F90)或 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/ey2L_jHMRc-CsOKS9-9tyA/zh-cn_image_0000002569021205.png?HW-CC-KV=V1&HW-CC-Date=20260417T014831Z&HW-CC-Expire=86400&HW-CC-Sign=CB88C2420E0716E16F570A36FC9E669656E16F1CBAB3828054F66BD5DEE33445)），否则函数返回FAST\_ERROR\_CODE\_ILLEGAL\_INPUT。

2\. 函数能保证输出矩形的数量小于等于输入矩形的数量。

 |

#### 类型定义说明

#### \[h2\]FAST\_ErrorCode

```c
typedef enum FAST_ErrorCode FAST_ErrorCode
```

**描述**

FAST Kit的错误码。

**起始版本：** 6.0.2(22)

#### \[h2\]FAST\_Rect

```c
typedef struct FAST_Rect FAST_Rect
```

**描述**

定义矩形的数据结构。

**起始版本：** 6.0.2(22)

#### \[h2\]FAST\_RectPartitionConfig

```c
typedef struct FAST_RectPartitionConfig FAST_RectPartitionConfig
```

**描述**

矩形划分求解器的不透明配置（Opaque Configuration），如果未在配置中设置算法，默认的算法是扫描线算法“SweepLineAlgo”。

**起始版本：** 6.0.2(22)

#### \[h2\]FAST\_SegmentMapConfig

```c
typedef struct FAST_SegmentMapConfig FAST_SegmentMapConfig
```

**描述**

线段表的不透明配置（Opaque Configuration）。

**起始版本：** 6.0.2(22)

#### \[h2\]FAST\_SegmentMapHandle

```c
typedef void* FAST_SegmentMapHandle
```

**描述**

线段表的句柄。

**起始版本：** 6.0.2(22)

#### \[h2\]FAST\_SegmentMapQueryType

```c
typedef enum FAST_SegmentMapQueryType FAST_SegmentMapQueryType
```

**描述**

线段表数据结构支持的区间查询操作类型。

**起始版本：** 6.0.2(22)

#### \[h2\]FAST\_SegmentMapUpdateType

```c
typedef enum FAST_SegmentMapUpdateType FAST_SegmentMapUpdateType
```

**描述**

线段表数据结构支持的区间更新操作类型。

**起始版本：** 6.0.2(22)

#### 枚举类型说明

#### \[h2\]FAST\_ErrorCode

```c
enum FAST_ErrorCode
```

**描述**

FAST Kit的错误码。

**起始版本：** 6.0.2(22)

| 枚举值 | 描述 |
| :-- | :-- |
| FAST\_ERROR\_CODE\_SUCCESS = 1023100000 | 成功。 |
| FAST\_ERROR\_CODE\_FAIL = 1023100001 | 失败。 |
| FAST\_ERROR\_CODE\_ILLEGAL\_INPUT = 1023100002 | 非法输入。 |
| FAST\_ERROR\_CODE\_INVALID\_PTR = 1023100003 | 无效指针（例如 NULL)。 |
| FAST\_ERROR\_CODE\_OOM = 1023199001 | 内存溢出。 |

#### \[h2\]FAST\_SegmentMapQueryType

```c
enum FAST_SegmentMapQueryType
```

**描述**

线段表支持的查询操作类型。

该枚举定义了线段表数据结构能够处理的各种区间查询操作。

**起始版本：** 6.0.2(22)

| 枚举值 | 描述 |
| :-- | :-- |
| FAST\_SEGMENTMAP\_QUERY\_TYPE\_SUM | 区间求和查询。 |
| FAST\_SEGMENTMAP\_QUERY\_TYPE\_MIN | 区间最小值查询。 |
| FAST\_SEGMENTMAP\_QUERY\_TYPE\_MAX | 区间最大值查询。 |

#### \[h2\]FAST\_SegmentMapUpdateType

```c
enum FAST_SegmentMapUpdateType
```

**描述**

线段表支持的更新操作类型。

该枚举定义了线段表数据结构能够处理的各种区间更新操作。

**起始版本：** 6.0.2(22)

| 枚举值 | 描述 |
| :-- | :-- |
| FAST\_SEGMENTMAP\_UPDATE\_TYPE\_SET | 赋值更新，区间内的每一个元素赋同一个值。 |
| FAST\_SEGMENTMAP\_UPDATE\_TYPE\_ADD | 加法更新，区间内的每一个元素加同一个值。 |
| FAST\_SEGMENTMAP\_UPDATE\_TYPE\_SUB | 减法更新，区间内的每一个元素减同一个值。 |

#### 函数说明

#### \[h2\]HMS\_FAST\_RectPartition\_CreateConfig()

```c
FAST_EXPORT FAST_ErrorCode HMS_FAST_RectPartition_CreateConfig (FAST_RectPartitionConfig ** config)
```

**描述**

创建矩形划分求解器的不透明配置。

**起始版本：** 6.0.2(22)

**参数：**

| 名称 | 描述 |
| :-- | :-- |
| config | 指向矩形划分求解器不透明配置[FAST\_RectPartitionConfig](#fast_rectpartitionconfig)的指针。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](#fast_errorcode-1)。

当config为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](#fast_errorcode-1)。

当内存耗尽时，返回[FAST\_ERROR\_CODE\_OOM](#fast_errorcode-1)。

#### \[h2\]HMS\_FAST\_RectPartition\_DestroyConfig()

```c
FAST_EXPORT void HMS_FAST_RectPartition_DestroyConfig (FAST_RectPartitionConfig * config)
```

**描述**

销毁矩形划分求解器的不透明配置，并释放内存，再次访问该不透明配置时为未定义行为。

**起始版本：** 6.0.2(22)

**参数：**

| 名称 | 描述 |
| :-- | :-- |
| config | 待销毁的矩形划分求解器的不透明配置[FAST\_RectPartitionConfig](#fast_rectpartitionconfig)。 |

#### \[h2\]HMS\_FAST\_RectPartition\_SetAlgo()

```c
FAST_EXPORT FAST_ErrorCode HMS_FAST_RectPartition_SetAlgo (FAST_RectPartitionConfig * config, const char * name )
```

**描述**

设置矩形划分求解器使用的算法。目前仅支持扫描线算法“SweepLineAlgo”，输出数量尽可能少（不保证最优性）的不相交矩形集合，复杂度为O(N logN)。

**起始版本：** 6.0.2(22)

**参数：**

| 名称 | 描述 |
| :-- | :-- |
| config | 待设置的矩形划分求解器的不透明配置[FAST\_RectPartitionConfig](#fast_rectpartitionconfig)。 |
| name | 矩形求解器使用的算法名称。目前仅支持扫描线算法“SweepLineAlgo”，输出数量尽可能少（不保证最优性）的不相交矩形集合，复杂度为![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/-Dwx9C1oQEKsbS6Lwhtguw/zh-cn_image_0000002568901195.png?HW-CC-KV=V1&HW-CC-Date=20260417T014831Z&HW-CC-Expire=86400&HW-CC-Sign=5808C37D26D7F0A0A6A02FC58202DCCBC622689CA53E4D02772B141965601CF2)。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](#fast_errorcode-1)。

当config或name为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](#fast_errorcode-1)。

当算法不支持时，返回[FAST\_ERROR\_CODE\_ILLEGAL\_INPUT](#fast_errorcode-1)。

#### \[h2\]HMS\_FAST\_RectPartition\_Solve()

```c
FAST_EXPORT FAST_ErrorCode HMS_FAST_RectPartition_Solve (FAST_RectPartitionConfig * config, size_t size, const FAST_Rect * origin, FAST_Rect * result, size_t * resultSize )
```

**描述**

在指定不透明配置下求解矩形划分问题。在调用函数之前需要先初始化参数中的结果数组result。

**起始版本：** 6.0.2(22)

**参数：**

| 名称 | 描述 |
| :-- | :-- |
| config | 矩形划分求解器的不透明配置。如果参数config中未设置算法，默认的算法是扫描线算法“SweepLineAlgo”。 |
| size | 待划分的矩形[FAST\_Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-rect)数量。 |
| origin | 待划分的矩形[FAST\_Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-rect)源数组。 |
| result | 由矩形划分求解器得到的[FAST\_Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-rect)结果，在调用函数之前需要初始化该结果数组，大小需要和源数组相等，否则可能导致溢出。 |
| resultSize | 划分之后的[FAST\_Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-rect)数量。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](#fast_errorcode-1)。

当入参指针为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](#fast_errorcode-1)。

当输入非法时，返回[FAST\_ERROR\_CODE\_ILLEGAL\_INPUT](#fast_errorcode-1)，如矩形存在相交。

当算法求解失败时，返回[FAST\_ERROR\_CODE\_FAIL](#fast_errorcode-1)。

**注解：**

1.  当选择“SweepLineAlgo”时，不应该返回[FAST\_ERROR\_CODE\_FAIL](#fast_errorcode-1)，此处仅作为预防性设置。

#### \[h2\]HMS\_FAST\_SegmentMap\_Create()

```c
FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_Create (FAST_SegmentMapHandle * handle, size_t size, const int32_t * array, FAST_SegmentMapConfig * config )
```

**描述**

创建线段表。

**起始版本：** 6.0.2(22)

**参数：**

| 名称 | 描述 |
| :-- | :-- |
| handle | 指向线段表句柄[FAST\_SegmentMapHandle](#fast_segmentmaphandle)的指针。 |
| size | 底层数组的大小（元素数量）。 |
| array | 可选；用于初始化线段表的底层数组。如果为NULL，则线段表中的元素均初始化为0，否则数组大小必须与参数size保持一致。 |
| config | 线段表的不透明配置[FAST\_SegmentMapConfig](#fast_segmentmapconfig)，若该参数为NULL或未配置，默认查询类型为[FAST\_SEGMENTMAP\_QUERY\_TYPE\_SUM](#fast_segmentmapquerytype-1)、更新类型为[FAST\_SEGMENTMAP\_UPDATE\_TYPE\_SET](#fast_segmentmapupdatetype-1)。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](#fast_errorcode-1)。

当config或handle为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](#fast_errorcode-1)。

当内存耗尽时，返回[FAST\_ERROR\_CODE\_OOM](#fast_errorcode-1)。

#### \[h2\]HMS\_FAST\_SegmentMap\_CreateConfig()

```c
FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_CreateConfig (FAST_SegmentMapConfig ** config)
```

**描述**

创建线段表的不透明配置。

**起始版本：** 6.0.2(22)

**参数：**

| 名称 | 描述 |
| :-- | :-- |
| config | 指向线段表不透明配置[FAST\_SegmentMapConfig](#fast_segmentmapconfig)的指针。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](#fast_errorcode-1)。

当config为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](#fast_errorcode-1)。

当内存耗尽时，返回[FAST\_ERROR\_CODE\_OOM](#fast_errorcode-1)。

#### \[h2\]HMS\_FAST\_SegmentMap\_Destroy()

```c
FAST_EXPORT void HMS_FAST_SegmentMap_Destroy (FAST_SegmentMapHandle handle)
```

**描述**

销毁线段表实例。

**起始版本：** 6.0.2(22)

**参数：**

| 名称 | 描述 |
| :-- | :-- |
| handle | 待销毁线段表句柄[FAST\_SegmentMapHandle](#fast_segmentmaphandle)。 |

#### \[h2\]HMS\_FAST\_SegmentMap\_DestroyConfig()

```c
FAST_EXPORT void HMS_FAST_SegmentMap_DestroyConfig (FAST_SegmentMapConfig * config)
```

**描述**

销毁线段表的不透明配置。

**起始版本：** 6.0.2(22)

**参数：**

| 名称 | 描述 |
| :-- | :-- |
| config | 待销毁线段表不透明配置[FAST\_SegmentMapConfig](#fast_segmentmapconfig)。 |

#### \[h2\]HMS\_FAST\_SegmentMap\_Query()

```c
FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_Query (FAST_SegmentMapHandle handle, size_t left, size_t right, int32_t * result )
```

**描述**

查询线段表的区间。

**起始版本：** 6.0.2(22)

**参数：**

| 名称 | 描述 |
| :-- | :-- |
| handle | 线段表句柄。 |
| left | 区间左端点 （包含），区间左闭右开。 |
| right | 区间右端点 （不包含），区间左闭右开。 |
| result | 根据区间查询的结果。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](#fast_errorcode-1)。

当handle为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](#fast_errorcode-1)。

当输入非法时，返回[FAST\_ERROR\_CODE\_ILLEGAL\_INPUT](#fast_errorcode-1)，如左端点大于等于右端点。

#### \[h2\]HMS\_FAST\_SegmentMap\_SetQueryType()

```c
FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_SetQueryType (FAST_SegmentMapConfig * config, FAST_SegmentMapQueryType type )
```

**描述**

设置线段表不透明配置中的查询类型。

**起始版本：** 6.0.2(22)

**参数：**

| 名称 | 描述 |
| :-- | :-- |
| config | 待修改的线段表不透明配置。 |
| type | 查询类型。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](#fast_errorcode-1)。

当config为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](#fast_errorcode-1)。

#### \[h2\]HMS\_FAST\_SegmentMap\_SetUpdateType()

```c
FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_SetUpdateType (FAST_SegmentMapConfig * config, FAST_SegmentMapUpdateType type )
```

**描述**

设置线段表不透明配置中的更新类型。

**起始版本：** 6.0.2(22)

**参数：**

| 名称 | 描述 |
| :-- | :-- |
| config | 待修改的线段表不透明配置。 |
| type | 更新类型。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](#fast_errorcode-1)。

当config为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](#fast_errorcode-1)。

#### \[h2\]HMS\_FAST\_SegmentMap\_Update()

```c
FAST_EXPORT FAST_ErrorCode HMS_FAST_SegmentMap_Update (FAST_SegmentMapHandle handle, size_t left, size_t right, int32_t value )
```

**描述**

更新线段表的区间。

**起始版本：** 6.0.2(22)

**参数：**

| 名称 | 描述 |
| :-- | :-- |
| handle | 线段表句柄。 |
| left | 区间左端点 （包含），区间为左闭右开。 |
| right | 区间右端点 （不包含），区间为左闭右开。 |
| value | 待更新的值。 |

**返回：**

当成功时，返回[FAST\_ERROR\_CODE\_SUCCESS](#fast_errorcode-1)。

当handle为NULL时，返回[FAST\_ERROR\_CODE\_INVALID\_PTR](#fast_errorcode-1)。

当输入非法时，返回[FAST\_ERROR\_CODE\_ILLEGAL\_INPUT](#fast_errorcode-1)，如左端点大于等于右端点。

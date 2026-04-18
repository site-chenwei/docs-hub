---
title: "AREngine_ARSemanticDensePointData"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-struct-arsemanticdensepointdata"
menu_path:
  - "参考"
  - "图形"
  - "AR Engine（AR引擎服务）"
  - "C API"
  - "头文件和结构体"
  - "结构体"
  - "AREngine_ARSemanticDensePointData"
captured_at: "2026-04-17T01:48:46.196Z"
---

# AREngine\_ARSemanticDensePointData

#### 概述

高精几何重建对象的稠密点云数据。

作为[HMS\_AREngine\_ARSemanticDense\_AcquirePointData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#hms_arengine_arsemanticdense_acquirepointdata)接口输入。

**起始版本：** 6.0.0(20)

**相关模块：** [AR Engine](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine)

**所在头文件：** [ar\_engine\_core.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-header-file)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int32\_t [id](#id) | 当前点的ID。 |
| float [x](#x) | 当前点的X坐标。 |
| float [y](#y) | 当前点的Y坐标。 |
| float [z](#z) | 当前点的Z坐标。 |
| int32\_t [r](#r) | 当前点的颜色，RGBA表示，这里是R的值。 |
| int32\_t [g](#g) | 当前点的颜色，RGBA表示，这里是G的值。 |
| int32\_t [b](#b) | 当前点的颜色，RGBA表示，这里是B的值。 |
| int32\_t [a](#a) | 当前点的颜色，RGBA表示，这里是A的值。 |
| float [confidence](#confidence) | 当前点的置信度。 |

#### 结构体成员变量说明

#### \[h2\]id

```cpp
int32_t AREngine_ARSemanticDensePointData::id
```

**描述**

当前点的ID。

#### \[h2\]x

```cpp
float AREngine_ARSemanticDensePointData::x
```

**描述**

当前点的X坐标。

#### \[h2\]y

```cpp
float AREngine_ARSemanticDensePointData::y
```

**描述**

当前点的Y坐标。

#### \[h2\]z

```cpp
float AREngine_ARSemanticDensePointData::z
```

**描述**

当前点的Z坐标。

#### \[h2\]r

```cpp
int32_t AREngine_ARSemanticDensePointData::r
```

**描述**

当前点的颜色，RGBA表示，这里是R的值。

#### \[h2\]g

```cpp
int32_t AREngine_ARSemanticDensePointData::g
```

**描述**

当前点的颜色，RGBA表示，这里是G的值。

#### \[h2\]b

```cpp
int32_t AREngine_ARSemanticDensePointData::b
```

**描述**

当前点的颜色，RGBA表示，这里是B的值。

#### \[h2\]a

```cpp
int32_t AREngine_ARSemanticDensePointData::a
```

**描述**

当前点的颜色，RGBA表示，这里是A的值。

#### \[h2\]confidence

```cpp
float AREngine_ARSemanticDensePointData::confidence
```

**描述**

当前点的置信度。

---
title: "AREngine_ARSemanticDenseCubeData"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-struct-arsemanticdensecubedata"
menu_path:
  - "参考"
  - "图形"
  - "AR Engine（AR引擎服务）"
  - "C API"
  - "头文件和结构体"
  - "结构体"
  - "AREngine_ARSemanticDenseCubeData"
captured_at: "2026-04-17T01:48:46.316Z"
---

# AREngine\_ARSemanticDenseCubeData

#### 概述

高精几何重建对象的立方体数据。

作为[HMS\_AREngine\_ARSemanticDense\_AcquireCubeData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#hms_arengine_arsemanticdense_acquirecubedata)接口输入。

**起始版本：** 6.0.0(20)

**相关模块：** [AR Engine](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine)

**所在头文件：** [ar\_engine\_core.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-header-file)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int32\_t [id](#id) | 当前立方体的ID。 |
| int32\_t [vertexSize](#vertexsize) | 当前立方体的顶点大小。 |
| float\* [vertexData](#vertexdata) | 
当前立方体的顶点数据。

对应立方体的8个顶点。索引从立方体后表面开始，按逆时针方向排列。

 |
| float [confidence](#confidence) | 当前立方体的置信度。 |
| AREngine\_ARSemanticPlaneLabel [label](#label) | 

当前立方体的语义标签。

参见[AREngine\_ARSemanticPlaneLabel](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#arengine_arsemanticplanelabel)。

 |

#### 结构体成员变量说明

#### \[h2\]id

```cpp
int32_t AREngine_ARSemanticDenseCubeData::id
```

**描述**

当前立方体的ID。

#### \[h2\]vertexSize

```cpp
int32_t AREngine_ARSemanticDenseCubeData::vertexSize
```

**描述**

当前立方体的顶点大小。

#### \[h2\]vertexData

```cpp
float* AREngine_ARSemanticDenseCubeData::vertexData
```

**描述**

当前立方体的顶点数据。

#### \[h2\]confidence

```cpp
float AREngine_ARSemanticDenseCubeData::confidence
```

**描述**

当前立方体的置信度。

#### \[h2\]label

```cpp
AREngine_ARSemanticPlaneLabel AREngine_ARSemanticDenseCubeData::label
```

**描述**

当前立方体的语义标签。

---
title: "GetRequiredInputShape"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getrequiredinputshape"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "TilingContext"
  - "GetRequiredInputShape"
captured_at: "2026-04-17T01:36:30.940Z"
---

# GetRequiredInputShape

#### 函数功能

根据算子原型定义中的输入索引获取对应的必选输入shape指针。

#### 函数原型

```cpp
const StorageShape *GetRequiredInputShape(const size_t ir_index) const;
```

#### 参数说明

| 参数 | 输入/输出 | 说明 |
| :-- | :-- | :-- |
| ir\_index | 输入 | 必选输入在算子IR原型定义中的索引，从0开始计数。 |

#### 返回值

指定的输入shape指针，shape中包含了原始shape与运行时shape。关于StorageShape类型的定义，请参见[StorageShape](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-storageshape-introduction)。

当输入ir\_index非法时，返回空指针。

#### 约束说明

无

#### 调用示例

```cpp
ge::graphStatus InferShape4ConcatD(TilingContext* context) {
  auto in_shape = context->GetRequiredInputShape(0);
  // ...
}
```

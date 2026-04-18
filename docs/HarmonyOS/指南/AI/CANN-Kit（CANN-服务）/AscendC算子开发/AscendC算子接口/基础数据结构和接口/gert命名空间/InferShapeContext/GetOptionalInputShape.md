---
title: "GetOptionalInputShape"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-infershapecontext-getoptionalinputshape"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "InferShapeContext"
  - "GetOptionalInputShape"
captured_at: "2026-04-17T01:36:29.232Z"
---

# GetOptionalInputShape

#### 函数功能

根据算子原型定义中的输入索引获取对应的可选输入shape指针。

#### 函数原型

```cpp
const Shape *GetOptionalInputShape(const size_t ir_index) const;
```

#### 参数说明

| 参数 | 输入/输出 | 说明 |
| :-- | :-- | :-- |
| ir\_index | 输入 | 算子IR原型定义中的输入索引，从0开始计数。 |

#### 返回值

返回输入shape的指针，输入ir\_index非法，或该输入没有实例化时，返回空指针。

关于Shape类型的定义，请参见[Shape](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-shape-introduction)。

#### 约束说明

无

#### 调用示例

```cpp
ge::graphStatus InferShapeForXXX(InferShapeContext *context) {
  auto in_shape = context->GetOptionalInputShape(2);
  // ...
}
```

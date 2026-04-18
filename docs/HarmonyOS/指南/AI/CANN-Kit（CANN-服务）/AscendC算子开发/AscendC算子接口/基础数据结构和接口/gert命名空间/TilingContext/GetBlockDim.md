---
title: "GetBlockDim"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getblockdim"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "TilingContext"
  - "GetBlockDim"
captured_at: "2026-04-17T01:36:31.062Z"
---

# GetBlockDim

#### 函数功能

获取blockDim，即参与计算的Vector或者Cube核数。blockDim的详细概念和设置方式请参考[SetBlockDim](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setblockdim)。

#### 函数原型

```cpp
uint32_t GetBlockDim() const;
```

#### 参数说明

无

#### 返回值

返回blockDim。

#### 约束说明

无

#### 调用示例

```cpp
ge::graphStatus Tiling4XXX(TilingContext* context) {
  auto block_dim = context->GetBlockDim();
  // ...
}
```

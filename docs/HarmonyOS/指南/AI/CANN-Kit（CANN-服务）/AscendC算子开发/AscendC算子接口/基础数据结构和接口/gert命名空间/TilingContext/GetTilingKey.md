---
title: "GetTilingKey"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-gettilingkey"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "TilingContext"
  - "GetTilingKey"
captured_at: "2026-04-17T01:36:31.012Z"
---

# GetTilingKey

#### 函数功能

获取tiling key。

#### 函数原型

```cpp
uint64_t GetTilingKey() const;
```

#### 参数说明

无

#### 返回值

返回tiling key。

#### 约束说明

无

#### 调用示例

```cpp
ge::graphStatus Tiling4XXX(TilingContext* context) {
  auto tiling_key = context->GetTilingKey();
  // ...
}
```

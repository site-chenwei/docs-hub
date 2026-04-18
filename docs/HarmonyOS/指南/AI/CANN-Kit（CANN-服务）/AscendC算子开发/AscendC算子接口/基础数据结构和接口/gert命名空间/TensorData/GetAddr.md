---
title: "GetAddr"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getaddr"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "TensorData"
  - "GetAddr"
captured_at: "2026-04-17T01:36:30.340Z"
---

# GetAddr

#### 函数功能

获取tensor数据地址。若存在manager函数，则由manager函数给出地址。

#### 函数原型

```cpp
TensorAddress GetAddr() const
```

#### 参数说明

无

#### 返回值

tensor地址。

#### 约束说明

无

#### 调用示例

```cpp
auto addr0 = reinterpret_cast<void *>(0x10);
TensorData td(addr, nullptr);
auto addr1 = td.GetAddr(); // 0x10
```

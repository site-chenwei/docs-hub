---
title: "SetSize"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setsize"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "TensorData"
  - "SetSize"
captured_at: "2026-04-17T01:36:30.384Z"
---

# SetSize

#### 函数功能

设置tensor数据的内存大小。

#### 函数原型

```cpp
void SetSize(const size_t size)
```

#### 参数说明

| 参数 | 输入/输出 | 说明 |
| :-- | :-- | :-- |
| size | 输入 | tensor的内存大小，单位为字节。 |

#### 返回值

无

#### 约束说明

无

#### 调用示例

```cpp
std::vector<int> a = {10};
auto addr = reinterpret_cast<void *>(a.data());
TensorData td(addr, HostAddrManager, 100U, kOnHost);
td.SetSize(10U);
```

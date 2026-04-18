---
title: "Free"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-free"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "TensorData"
  - "Free"
captured_at: "2026-04-17T01:36:30.431Z"
---

# Free

#### 函数功能

释放tensor。

#### 函数原型

```cpp
ge::graphStatus Free()
```

#### 参数说明

无

#### 返回值

成功时返回：ge::GRAPH\_SUCCESS。

失败时返回manager函数返回的状态码。

关于ge::graphStatus类型的定义，请参见[ge::graphStatus](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-gegraphstatus)。

#### 约束说明

无

#### 调用示例

```cpp
std::vector<int> a = {10};
auto addr = reinterpret_cast<void *>(a.data());
TensorData td(addr, nullptr);
td.Free();
```

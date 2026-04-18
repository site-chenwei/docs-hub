---
title: "GetCapacity"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getcapacity"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "TilingData"
  - "GetCapacity"
captured_at: "2026-04-17T01:36:31.157Z"
---

# GetCapacity

#### 函数功能

获取本实例可容纳的最大tiling data长度。

#### 函数原型

```cpp
size_t GetCapacity() const;
```

#### 参数说明

无

#### 返回值

最大tiling data长度。

#### 约束说明

无

#### 调用示例

```cpp
auto td_buf = TilingData::CreateCap(100U);
auto td = reinterpret_cast<TilingData *>(td_buf.get());
size_t cap = td->GetCapacity(); // 100U
```

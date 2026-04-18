---
title: "GetData"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tilingdata-getdata"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "TilingData"
  - "GetData"
captured_at: "2026-04-17T01:36:31.244Z"
---

# GetData

#### 函数功能

获取TilingData的数据指针。

#### 函数原型

```cpp
void *GetData();
const void *GetData() const;
```

#### 参数说明

无

#### 返回值

data指针。

#### 约束说明

无

#### 调用示例

```cpp
auto td_buf = TilingData::CreateCap(100U);
auto td = reinterpret_cast<TilingData *>(td_buf.get());
auto tiling_data_ptr = td->GetData(); // td_buf.get() + sizeof(TilingData)
```

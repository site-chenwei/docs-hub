---
title: "GetChangedResourceKeys"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getchangedresourcekeys"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "InferenceContext"
  - "GetChangedResourceKeys"
captured_at: "2026-04-17T01:36:31.853Z"
---

# GetChangedResourceKeys

#### 函数功能

一般由框架调用。

在结束写类型算子的推导后，可以调用该接口获取变化的资源标识。

#### 函数原型

```cpp
const std::set<ge::AscendString>& GetChangedResourceKeys() const
```

#### 参数说明

无

#### 返回值

| 类型 | 描述 |
| :-- | :-- |
| std::set<ge::AscendString> | 已变化的资源标识集合。 |

#### 约束说明

无

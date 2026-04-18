---
title: "ClearChangedResourceKeys"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-clearchangedresourcekeys"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "InferenceContext"
  - "ClearChangedResourceKeys"
captured_at: "2026-04-17T01:36:34.404Z"
---

# ClearChangedResourceKeys

#### 函数功能

一般由框架调用。

当变化了的资源触发重新推导之后，需要调用该接口清除inference\_context中保存的变化了的资源标识。

#### 函数原型

```cpp
void ClearChangedResourceKeys()
```

#### 参数说明

无

#### 返回值

无

#### 约束说明

无

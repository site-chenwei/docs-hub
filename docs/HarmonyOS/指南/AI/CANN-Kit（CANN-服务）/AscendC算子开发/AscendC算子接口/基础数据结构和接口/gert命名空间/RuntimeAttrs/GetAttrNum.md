---
title: "GetAttrNum"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getattrnum"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "RuntimeAttrs"
  - "GetAttrNum"
captured_at: "2026-04-17T01:36:29.889Z"
---

# GetAttrNum

#### 函数功能

获取属性的数量。

#### 函数原型

```cpp
size_t GetAttrNum() const
```

#### 参数说明

无

#### 返回值

属性的数量。

#### 约束说明

无

#### 调用示例

```cpp
const RuntimeAttrs * runtime_attrs = kernel_context->GetAttrs();
size_t attr_num = runtime_attrs->GetAttrNum();
```

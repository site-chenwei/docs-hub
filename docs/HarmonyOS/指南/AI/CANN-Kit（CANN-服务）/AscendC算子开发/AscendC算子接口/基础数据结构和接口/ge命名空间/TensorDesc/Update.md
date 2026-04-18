---
title: "Update"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-update"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "TensorDesc"
  - "Update"
captured_at: "2026-04-17T01:36:36.496Z"
---

# Update

#### 函数功能

更新TensorDesc的shape、format、datatype属性。

#### 函数原型

```cpp
void Update(const Shape &shape, Format format = FORMAT_ND, DataType dt = DT_FLOAT);
```

#### 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| shape | 输入 | 需刷新的shape对象。 |
| format | 输入 | 需刷新的format对象，默认取值FORMAT\_ND。 |
| dt | 输入 | 需刷新的datatype对象，默认取值DT\_FLOAT。 |

#### 返回值

无

#### 异常处理

无

#### 约束说明

无

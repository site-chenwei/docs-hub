---
title: "GetTensorDesc"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-gettensordesc"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "Tensor"
  - "GetTensorDesc"
captured_at: "2026-04-17T01:36:37.256Z"
---

# GetTensorDesc

#### 函数功能

获取Tensor的描述符。

#### 函数原型

```cpp
TensorDesc GetTensorDesc() const;
```

#### 参数说明

无

#### 返回值

| 类型 | 描述 |
| :-- | :-- |
| [TensorDesc](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensordesc-construction-and-destructor) | 返回当前Tensor的描述符。 |

#### 异常处理

无

#### 约束说明

修改返回的TensorDesc信息，不影响Tensor对象中已有的TensorDesc信息。

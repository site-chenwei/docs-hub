---
title: "SetOriginFormat"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensordesc-setoriginformat"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "TensorDesc"
  - "SetOriginFormat"
captured_at: "2026-04-17T01:36:36.262Z"
---

# SetOriginFormat

#### 函数功能

向TensorDesc中设置Tensor的原始Format。

该Format是指原始网络模型的Format。

#### 函数原型

```cpp
void SetOriginFormat(Format origin_format);
```

#### 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| origin\_format | 输入 | 
需设置的原始Format信息。

关于Format数据类型的定义，请参见[Format](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-ge-format)。

 |

#### 返回值

无

#### 异常处理

无

#### 约束说明

无

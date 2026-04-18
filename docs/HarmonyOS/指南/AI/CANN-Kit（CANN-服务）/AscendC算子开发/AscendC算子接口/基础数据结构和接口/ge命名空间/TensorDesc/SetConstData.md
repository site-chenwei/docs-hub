---
title: "SetConstData"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setconstdata"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "TensorDesc"
  - "SetConstData"
captured_at: "2026-04-17T01:36:36.133Z"
---

# SetConstData

#### 函数功能

如果TensorDesc是常量节点的描述，向TensorDesc中设置权重值。

#### 函数原型

```cpp
void SetConstData(std::unique_ptr<uint8_t[]> const_data_buffer, const size_t &const_data_len);
```

#### 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| const\_data\_buffer | 输入 | 权重地址。 |
| const\_data\_len | 输入 | 权重长度。 |

#### 返回值

无

#### 异常处理

无

#### 约束说明

无

---
title: "ResetData"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-resetdata"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "Tensor"
  - "ResetData"
captured_at: "2026-04-17T01:36:37.946Z"
---

# ResetData

#### 函数功能

释放Tensor中数据内存。

#### 函数原型

```cpp
std::unique_ptr<uint8_t[], Tensor::DeleteFunc> ResetData();
```

#### 参数说明

无

#### 返回值

返回释放后的内存地址和删除器。

#### 异常处理

无

#### 约束说明

无

---
title: "FrameworkType"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-frameworktype"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "OpRegistrationData"
  - "FrameworkType"
captured_at: "2026-04-17T01:36:35.351Z"
---

# FrameworkType

#### 函数功能

设置原始模型的框架类型。

#### 函数原型

```cpp
OpRegistrationData &FrameworkType(const domi::FrameworkType &fmk_type)
```

#### 参数说明

| 参数 | 输入/输出 | 说明 |
| :-- | :-- | :-- |
| fmk\_type | 输入 | 
框架类型。

\- CAFFE

\- TENSORFLOW

\- ONNX

FrameworkType枚举值的如下：CAFFE、MINDSPORE、TENSORFLOW、ANDROID\_NN、ONNX、FRAMEWORK\_RESERVED。

 |

---
title: "GetStorageFormat"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensor-getstorageformat"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "Tensor"
  - "GetStorageFormat"
captured_at: "2026-04-17T01:36:30.700Z"
---

# GetStorageFormat

#### 函数功能

获取运行时Tensor的format。

#### 函数原型

```cpp
ge::Format GetStorageFormat() const
```

#### 参数说明

无

#### 返回值

返回运行时format。

关于ge::Format类型的定义，请参见[Format](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-ge-format)。

#### 约束说明

无

#### 调用示例

```cpp
Tensor t = {{}, {}, {}, {}, nullptr};
t.SetOriginFormat(ge::FORMAT_NHWC);
t.SetStorageFormat(ge::FORMAT_NC1HWC0);
auto fmt = t.GetStorageFormat(); // ge::FORMAT_NC1HWC0
```

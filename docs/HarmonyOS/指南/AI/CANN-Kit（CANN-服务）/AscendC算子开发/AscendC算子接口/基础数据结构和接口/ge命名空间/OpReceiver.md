---
title: "OpReceiver"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-opreceiver"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "OpReceiver"
captured_at: "2026-04-17T01:36:35.273Z"
---

# OpReceiver

#### 函数功能

OpReceiver构造函数，接收自定义算子的注册信息。

#### 函数原型

```cpp
OpReceiver(OpRegistrationData &reg_data);
~OpReceiver();
```

#### 参数说明

| 参数 | 输入/输出 | 说明 |
| :-- | :-- | :-- |
| reg\_data | 输入 | 需要注册的算子信息。 |

#### 返回值

OpReceiver构造函数返回OpReceiver类型的对象。

#### 异常处理

无

#### 约束说明

无

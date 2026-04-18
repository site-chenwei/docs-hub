---
title: "RegisterReliedOnResourceKey"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-registerreliedonresourcekey"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "InferenceContext"
  - "RegisterReliedOnResourceKey"
captured_at: "2026-04-17T01:36:31.805Z"
---

# RegisterReliedOnResourceKey

#### 函数功能

注册依赖的资源。

一般由读类型的算子调用，如stack pop。因读类型算子的shape依赖资源算子，调用该接口注册依赖的资源标识。

若资源算子shape变化可触发读类型算子的重新推导。

#### 函数原型

```cpp
graphStatus RegisterReliedOnResourceKey(const ge::AscendString &key)
```

#### 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| key | 输入 | 资源的唯一标识。 |

#### 返回值

graphStatus：GRAPH\_SUCCESS，代表成功；GRAPH\_FAILED，代表失败。

#### 约束说明

无

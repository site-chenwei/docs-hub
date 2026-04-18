---
title: "AddAutoMappingSubgraphIOIndexFunc"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-addautomappingsubgraphioindexfunc"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "FrameworkRegistry"
  - "AddAutoMappingSubgraphIOIndexFunc"
captured_at: "2026-04-17T01:36:31.674Z"
---

# AddAutoMappingSubgraphIOIndexFunc

#### 函数功能

注册的具体网络类型的自动映射函数。

#### 函数原型

```cpp
void AddAutoMappingSubgraphIOIndexFunc(domi::FrameworkType framework, AutoMappingSubgraphIOIndexFunc fun);
```

#### 参数说明

| 参数 | 输入/输出 | 说明 |
| :-- | :-- | :-- |
| framework | 输入 | 网络类型，FrameworkType类型定义请参考[FrameworkType](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-frameworktype)。 |
| fun | 输入 | 自动映射输入输出函数，函数类型详见[AutoMappingSubgraphIndex](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-automappingsubgraphindex)。 |

#### 返回值

无

#### 异常处理

无

#### 约束说明

无

---
title: "DynamicInputRegisterByIndex"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-dynamicinputregisterbyindex"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "Operator"
  - "DynamicInputRegisterByIndex"
captured_at: "2026-04-17T01:36:35.255Z"
---

# DynamicInputRegisterByIndex

#### 函数功能

指定位置进行算子动态输入注册。

#### 函数原型

```cpp
void DynamicInputRegisterByIndex(const char_t *name, const uint32_t num, size_t index);
```

#### 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| name | 输入 | 算子的动态Input名。 |
| num | 输入 | 添加的动态Input个数。 |
| index | 输入 | 从index位置添加动态输入。 |

#### 返回值

无

#### 异常处理

无

#### 约束说明

无

---
title: "ScalarGetSFFValue"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-scalargetsffvalue"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "AscendC API"
  - "基础API"
  - "标量计算"
  - "ScalarGetSFFValue"
captured_at: "2026-04-17T01:36:25.521Z"
---

# ScalarGetSFFValue

#### 功能说明

获取一个uint64\_t类型数字的二进制中第一个0或1出现的位置，如果没找到则返回-1。

#### 函数原型

```cpp
template <int countValue>  
__aicore__ inline int64_t ScalarGetSFFValue(uint64_t valueIn)
```

#### 参数说明

**表1** 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| valueIn | 输入 | 输入数据，数据类型是uint64\_t。 |
| countValue | 输入 | 获取到第一个0或1的位置。数据类型是int，值为0或1。 |

#### 返回值

int64\_t类型的数，valueIn中第一个0或1出现的位置。

#### 支持的型号

Kirin9020系列处理器

KirinX90系列处理器

#### 约束说明

无。

#### 调用示例

```cpp
uint64_t valueIn = 28;
// 输出数据(oneCount): 2
int64_t oneCount = AscendC::ScalarGetSFFValue<1>(valueIn);
```

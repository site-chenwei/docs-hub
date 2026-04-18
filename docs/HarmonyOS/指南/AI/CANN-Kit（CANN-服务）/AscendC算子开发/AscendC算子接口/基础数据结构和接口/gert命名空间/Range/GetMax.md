---
title: "GetMax"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getmax"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "Range"
  - "GetMax"
captured_at: "2026-04-17T01:36:29.717Z"
---

# GetMax

#### 函数功能

获取最大的T对象指针。

#### 函数原型

```cpp
const T *GetMax() const;
T *GetMax();
```

#### 参数说明

无

#### 返回值

返回最大的T对象指针。

#### 约束说明

无

#### 调用示例

```cpp
int min = -1;
int max = 1024;
Range<int> range(&min,&max);
 
auto ret = range.GetMax(); // ret指针指向max
```

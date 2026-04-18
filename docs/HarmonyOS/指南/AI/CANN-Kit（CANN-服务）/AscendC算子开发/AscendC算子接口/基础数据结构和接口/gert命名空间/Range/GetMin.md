---
title: "GetMin"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getmin"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "Range"
  - "GetMin"
captured_at: "2026-04-17T01:36:29.694Z"
---

# GetMin

#### 函数功能

获取最小的T对象指针。

#### 函数原型

```cpp
const T *GetMin() const;
T *GetMin();
```

#### 参数说明

无

#### 返回值

返回最小的T对象指针。

#### 约束说明

无

#### 调用示例

```cpp
int min = -1;
int max = 1024;
Range<int> range(&min,&max);
 
auto ret = range.GetMin(); // ret指针指向min
```

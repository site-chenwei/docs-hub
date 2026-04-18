---
title: "GetValue"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getvalue"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "AttrValue"
  - "GetValue"
captured_at: "2026-04-17T01:36:31.567Z"
---

# GetValue

#### 函数功能

获取属性key-value键值对中的value值，并将value值从T类型转换为DT类型。

-   支持将INT类型转换为int64\_t类型。
    
-   支持将FLOAT类型转换为float类型。
    
-   支持将STR类型转换为std::string类型。
    

#### 函数原型

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/-n1PlrqLRBuxqHoUHMWlgQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013634Z&HW-CC-Expire=86400&HW-CC-Sign=6219425E2803B130395472903217B8CCF7A6A84C0998186F5EC91D57BDF8B02A)

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
template<typename T, typename DT>
graphStatus GetValue(DT &val) const
graphStatus GetValue(AscendString &val);
```

#### 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| val | 输出 | DT类型的参数。 |

#### 返回值

| 类型 | 描述 |
| :-- | :-- |
| graphStatus | 数据类型转换成功，返回GRAPH\_SUCCESS， 否则，返回GRAPH\_FAILED。 |

#### 异常处理

无

#### 约束说明

无

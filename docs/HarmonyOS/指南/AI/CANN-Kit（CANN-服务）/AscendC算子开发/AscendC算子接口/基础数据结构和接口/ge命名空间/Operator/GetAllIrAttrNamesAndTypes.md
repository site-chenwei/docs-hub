---
title: "GetAllIrAttrNamesAndTypes"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getallirattrnamesandtypes"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "Operator"
  - "GetAllIrAttrNamesAndTypes"
captured_at: "2026-04-17T01:36:34.775Z"
---

# GetAllIrAttrNamesAndTypes

#### 函数功能

获取该算子所有的IR定义的属性名称和属性类型，包含普通和必选属性两种。

#### 函数原型

```cpp
graphStatus GetAllIrAttrNamesAndTypes(std::map<AscendString, AscendString> &attr_name_types) const;
```

#### 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| attr\_name\_types | 输出 | 所有的IR定义的属性名称和属性类型。 |

#### 返回值

| 类型 | 描述 |
| :-- | :-- |
| graphStatus | 
GRAPH\_FAILED：失败。

GRAPH\_SUCCESS：成功。

 |

#### 异常处理

无

#### 约束说明

无

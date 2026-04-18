---
title: "GetAllAttrNamesAndTypes"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getallattrnamesandtypes"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "Operator"
  - "GetAllAttrNamesAndTypes"
captured_at: "2026-04-17T01:36:34.760Z"
---

# GetAllAttrNamesAndTypes

#### 函数功能

获取算子所有已配置的属性名称及类型，包含IR定义的普通属性和开发者自定义属性。

#### 函数原型

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/zttnQLL2RM-f8Htk5bswrA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013634Z&HW-CC-Expire=86400&HW-CC-Sign=371B104B25231984CBADDABD5B950A7A99763AD74C03AF45A0C745FB27A05555)

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
const std::map<std::string, std::string> GetAllAttrNamesAndTypes() const;
graphStatus GetAllAttrNamesAndTypes(std::map<AscendString, AscendString> &attr_name_types) const;
```

#### 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| attr\_name\_types | 输出 | 所有的属性名称和属性类型。 |

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

---
title: "GetDynamicInputNum"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getdynamicinputnum"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "Operator"
  - "GetDynamicInputNum"
captured_at: "2026-04-17T01:36:34.799Z"
---

# GetDynamicInputNum

#### 函数功能

获取算子的动态Input的实际个数。

#### 函数原型

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/LLjd9we1QzCJWI9SwoPo3Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013634Z&HW-CC-Expire=86400&HW-CC-Sign=430B084D3EDE153CF859F129E490E556D211BA721924045E866ED64648AECCEF)

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
int32_t GetDynamicInputNum(const std::string &name) const;
int32_t GetDynamicInputNum(const char_t *name) const;
```

#### 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| name | 输入 | 算子的动态Input名。 |

#### 返回值

| 类型 | 描述 |
| :-- | :-- |
| int | 
实际动态Input的个数。

当name非法，或者算子无动态Input时，返回-1。

 |

#### 约束说明

无

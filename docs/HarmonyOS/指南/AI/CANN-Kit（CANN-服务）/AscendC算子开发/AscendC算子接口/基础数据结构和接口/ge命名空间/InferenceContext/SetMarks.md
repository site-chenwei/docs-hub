---
title: "SetMarks"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setmarks"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "InferenceContext"
  - "SetMarks"
captured_at: "2026-04-17T01:36:31.757Z"
---

# SetMarks

#### 函数功能

在资源类算子推理的上下文中，设置成对资源算子的标记。

#### 函数原型

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/-b9dS0a3Q8mNYORWZazMAg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013634Z&HW-CC-Expire=86400&HW-CC-Sign=635B374D82CED2D174FA129AEDD7CF1E6F7844A4C11CF38A42D2A1E5EB83EE47)

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
void SetMarks(const std::vector<std::string> &marks)
void SetMarks(const std::vector<AscendString> &marks)
```

#### 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| marks | 输入 | 资源类算子的标记。 |

#### 返回值

无

#### 异常处理

无

#### 约束说明

无

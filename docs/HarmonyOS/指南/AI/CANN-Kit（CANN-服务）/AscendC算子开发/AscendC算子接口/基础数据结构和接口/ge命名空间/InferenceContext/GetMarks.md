---
title: "GetMarks"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getmarks"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "InferenceContext"
  - "GetMarks"
captured_at: "2026-04-17T01:36:31.755Z"
---

# GetMarks

#### 函数功能

在资源类算子推理的上下文中，获取成对资源算子的标记。

#### 函数原型

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/PjH1k-dESV6MMPLaba3OSA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013634Z&HW-CC-Expire=86400&HW-CC-Sign=0D999916BA905A59B498F15067DECE92BD15974BE0E36C8348E0D0506904A559)

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
const std::vector<std::string> &GetMarks() const
void GetMarks(std::vector<AscendString> &marks) const
```

#### 参数说明

无

#### 返回值

| 类型 | 描述 |
| :-- | :-- |
| const std::vector<std::string> | 资源类算子的标记。 |

#### 异常处理

无

#### 约束说明

无

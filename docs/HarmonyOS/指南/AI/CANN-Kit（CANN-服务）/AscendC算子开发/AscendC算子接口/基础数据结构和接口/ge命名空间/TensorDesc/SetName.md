---
title: "SetName"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setname"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "TensorDesc"
  - "SetName"
captured_at: "2026-04-17T01:36:36.221Z"
---

# SetName

#### 函数功能

向TensorDesc中设置Tensor的名称。

#### 函数原型

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/7Mkrx7mhQQ6hwsIOk0aB8g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013636Z&HW-CC-Expire=86400&HW-CC-Sign=4A864420E2466150E6BA9283F0F0A50A37010765D5F38C61A660EF4969EA40C9)

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
void SetName(const std::string &name);
void SetName(const char_t *name);
```

#### 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| name | 输入 | 需设置的Tensor的名称。 |

#### 返回值

无

#### 异常处理

无

#### 约束说明

无

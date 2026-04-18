---
title: "SetData"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensor-setdata"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "Tensor"
  - "SetData"
captured_at: "2026-04-17T01:36:37.282Z"
---

# SetData

#### 函数功能

向Tensor中设置数据。

#### 函数原型

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/TvOlZ6TNQGOh_M-1mylmsQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013637Z&HW-CC-Expire=86400&HW-CC-Sign=1096DE14FFE8DB1544D219EC2A47D5D15476E2C46D8AD733C9EAF968F112EB52)

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
graphStatus SetData(std::vector<uint8_t> &&data);
graphStatus SetData(const std::vector<uint8_t> &data);
graphStatus SetData(const uint8_t *data, size_t size);
graphStatus SetData(const std::string &data);
graphStatus SetData(const char_t *data);
graphStatus SetData(const std::vector<std::string> &data);
graphStatus SetData(const std::vector<AscendString> &datas);
graphStatus SetData(uint8_t *data, size_t size, const Tensor::DeleteFunc &deleter_func);
```

#### 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| data/datas | 输入 | 需设置的数据。 |
| size | 输入 | 数据的长度，单位为字节。 |
| deleter\_func | 输入 | 
用于释放data数据。

using DeleteFunc = std::function<void(uint8\_t \*)>;

 |

#### 返回值

| 类型 | 描述 |
| :-- | :-- |
| graphStatus | 设置成功返回GRAPH\_SUCCESS，否则，返回GRAPH\_FAILED。 |

#### 异常处理

无

#### 约束说明

无

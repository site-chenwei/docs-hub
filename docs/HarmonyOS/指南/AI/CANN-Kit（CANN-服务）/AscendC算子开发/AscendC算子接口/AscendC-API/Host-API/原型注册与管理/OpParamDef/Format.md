---
title: "Format"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-format"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "AscendC API"
  - "Host API"
  - "原型注册与管理"
  - "OpParamDef"
  - "Format"
captured_at: "2026-04-17T01:36:27.569Z"
---

# Format

#### 函数功能

定义算子参数数据格式。

#### 函数原型

```cpp
OpParamDef &Format(std::vector<ge::Format> formats);
```

#### 参数说明

| 参数 | 输入/输出 | 说明 |
| :-- | :-- | :-- |
| formats | 输入 | 算子参数数据格式，ge::Format请参考[Format](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-ge-format)。 |

#### 返回值

[OpParamDef](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-paramtype)算子定义。

#### 约束说明

无

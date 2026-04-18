---
title: "HasSubFormat"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-hassubformat"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "HasSubFormat"
captured_at: "2026-04-17T01:36:38.274Z"
---

# HasSubFormat

#### 函数功能

判断实际format中是否包含子format。

#### 函数原型

```cpp
inline bool HasSubFormat(int32_t format)
```

#### 参数说明

| 参数 | 输入/输出 | 说明 |
| :-- | :-- | :-- |
| format | 输入 | 实际format（4字节大小，第1个字节的高四位为预留字段，低四位为c0 format，第2-3字节为子format信息，第4字节为主format信息）。 |

#### 返回值

-   true：实际format中包含子format。
    
-   false：实际format中不包含子format。
    

#### 异常处理

无

#### 约束说明

无

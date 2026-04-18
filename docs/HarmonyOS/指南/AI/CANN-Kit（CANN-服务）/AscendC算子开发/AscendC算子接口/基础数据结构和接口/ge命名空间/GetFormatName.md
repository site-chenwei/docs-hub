---
title: "GetFormatName"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getformatname"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "GetFormatName"
captured_at: "2026-04-17T01:36:38.176Z"
---

# GetFormatName

#### 函数功能

根据传入的format类型，获取format的字符串描述。

#### 函数原型

```cpp
const char_t *GetFormatName(Format format)
```

#### 参数说明

| 参数 | 输入/输出 | 说明 |
| :-- | :-- | :-- |
| format | 输入 | format枚举值。 |

#### 返回值

该format所对应的字符串描述，若format不合法或不被识别，则返回nullptr。

#### 异常处理

无

#### 约束说明

返回的字符串不可被修改。

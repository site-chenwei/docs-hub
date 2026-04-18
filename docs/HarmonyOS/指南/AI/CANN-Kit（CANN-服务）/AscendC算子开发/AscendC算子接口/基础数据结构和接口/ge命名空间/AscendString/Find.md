---
title: "Find"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-find"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "AscendString"
  - "Find"
captured_at: "2026-04-17T01:36:31.534Z"
---

# Find

#### 函数功能

查找子串在当前字符串中的位置。

#### 函数原型

```cpp
size_t Find(const AscendString &ascend_string) const;
```

#### 约束说明

无

#### 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| ascend\_string | 输入 | 要查找的子串。 |

#### 返回值

| 类型 | 描述 |
| :-- | :-- |
| size\_t | 子串的起始位置。 |

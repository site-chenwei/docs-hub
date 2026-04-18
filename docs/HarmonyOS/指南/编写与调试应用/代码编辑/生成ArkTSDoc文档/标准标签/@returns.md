---
title: "@returns"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arktsdoc-returns"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "生成ArkTSDoc文档"
  - "标准标签"
  - "@returns"
captured_at: "2026-04-17T01:36:48.584Z"
---

# @returns

@returns标签用于记录函数返回值。

#### 语法

@returns \[description\]

#### 示例

/\*\*
 \* Returns the sum of a and b
 \* @param a
 \* @param b
 \* @returns Sum of a and b
 \*/
export function sum(a: number, b: number): number{
  return a + b;
}

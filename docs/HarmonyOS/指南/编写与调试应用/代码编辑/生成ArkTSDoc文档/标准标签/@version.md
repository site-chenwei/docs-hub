---
title: "@version"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arktsdoc-version"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "生成ArkTSDoc文档"
  - "标准标签"
  - "@version"
captured_at: "2026-04-17T01:36:48.592Z"
---

# @version

@version标签用于记录项目的版本。

#### 语法

@version <version>

#### 示例

使用 @version 标签：

/\*\*
 \* Calculates the square root of a number.
 \* @version 1.2.3
 \*/
export function sqrt(x: number): number {
  return Math.sqrt(x);
}

---
title: "@todo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arktsdoc-todo"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "生成ArkTSDoc文档"
  - "标准标签"
  - "@todo"
captured_at: "2026-04-17T01:36:48.592Z"
---

# @todo

@todo 标签记录要完成的任务。在一个 ArkTSDoc 注释块中可以包含多个 @todo 标签。

#### 语法

@todo text describing thing to do.

#### 示例

使用 @todo 标签：

/\*\*
 \* @todo Write the documentation.
 \* @todo Implement this function.
 \*/
export function foo() {
  // write me
}

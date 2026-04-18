---
title: "@throws"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arktsdoc-throws"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "生成ArkTSDoc文档"
  - "标准标签"
  - "@throws"
captured_at: "2026-04-17T01:36:48.597Z"
---

# @throws

@throws标签用于函数，记录函数可能引发的错误。可以在一个ArkTSDoc注释中多次使用@throws标记。

#### 语法

@throws description

#### 示例

使用带有描述的 @throws 标记：

/\*\*
 \* @throws Will throw an error if the argument is null.
 \*/
export function bar(x: number) {
  throw new Error();
}

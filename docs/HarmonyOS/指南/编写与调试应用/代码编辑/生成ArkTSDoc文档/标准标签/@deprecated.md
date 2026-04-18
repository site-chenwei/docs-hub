---
title: "@deprecated"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arktsdoc-deprecated"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "生成ArkTSDoc文档"
  - "标准标签"
  - "@deprecated"
captured_at: "2026-04-17T01:36:48.514Z"
---

# @deprecated

@deprecated标签指明一个标识在代码中已经被弃用。

#### 语法

@deprecated \[<some text>\]

#### 示例

可以单独使用@deprecated标记，也可以包含一些描述有关deprecated的详细信息的文本。

例：说明自版本2.0以来旧函数已被弃用

/\*\*
 \* @deprecated since version 2.0
 \*/
export function old() {}

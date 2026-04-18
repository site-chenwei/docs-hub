---
title: "@param"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arktsdoc-param"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "生成ArkTSDoc文档"
  - "标准标签"
  - "@param"
captured_at: "2026-04-17T01:36:48.526Z"
---

# @param

@param标签提供函数参数的描述信息。

可以通过在描述之前插入一个连字符（-），使ArkTSDoc注释更具可读性。连字符前后需使用空格隔开。

#### 语法

@param \[<description>\]

#### 示例

下面的示例演示如何在 @param 标签中包含描述信息。

变量说明：

/\*\*
 \* @param somebody Somebody's name.
 \*/
export function sayHello(somebody: string): void {
  console.log('Hello ' + somebody);
}

可以在变量说明前加个连字符（-），使之更加容易阅读：

/\*\*
 \* @param somebody - Somebody's name.
 \*/
export function sayHello(somebody: string): void {
  console.log('Hello ' + somebody);
}

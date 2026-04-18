---
title: "@performance/hp"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-performance-no-closures"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "性能规则@performance"
  - "@performance/hp-performance-no-closures"
captured_at: "2026-04-17T01:36:47.355Z"
---

# @performance/hp-performance-no-closures

建议函数内部变量尽量使用参数传递。

根据[ArkTS编程规范](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-high-performance-programming)，建议修改。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@performance/hp-performance-no-closures": "suggestion",
  }
}

#### 选项

该规则无需配置额外选项。

#### 正例

let arr = \[0, 1, 2\];
function foo(array: Array<number>): number {
  // arr 尽量通过参数传递
  return array\[0\] + array\[1\];
}
foo(arr);

#### 反例

let arr = \[0, 1, 2\];
function foo() {
  // arr 尽量通过参数传递
  return arr\[0\] + arr\[1\];
}
foo();

#### 规则集

plugin:@performance/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。

---
title: "@typescript"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-extra-parens"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "通用规则@typescript-eslint"
  - "@typescript-eslint/no-extra-parens"
captured_at: "2026-04-17T01:36:45.360Z"
---

# @typescript-eslint/no-extra-parens

禁止使用不必要的括号。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-extra-parens": "error"
  }
}

#### 选项

详情请参考[@typescript-eslint/no-extra-parens选项](https://eslint.nodejs.cn/docs/rules/no-extra-parens#选项)。

#### 正例

// 默认不允许在任何表达式中使用不必要的括号
(0).toString();

const result = (() => {
  console.info('arrow function');
}) ? '1' : '2';

(/^a$/).test(result);

#### 反例

// 默认不允许在任何表达式中使用不必要的括号
const b = 10;
const c = 20;
export const a = (b \* c);

export const d = (a \* b) + c;

export const myType = typeof (a);

#### 规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。

---
title: "@typescript"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-nullish-coalescing"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "通用规则@typescript-eslint"
  - "@typescript-eslint/prefer-nullish-coalescing"
captured_at: "2026-04-17T01:36:45.951Z"
---

# @typescript-eslint/prefer-nullish-coalescing

强制使用空值合并运算符（??）而不是逻辑运算符。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/prefer-nullish-coalescing": "error"
  }
}

#### 选项

详情请参考[@typescript-eslint/prefer-nullish-coalescing选项](https://typescript-eslint.nodejs.cn/rules/prefer-nullish-coalescing/#options)。

#### 正例

function getText1(): string | undefined {
  return 'bar';
}

function getText2(): string | null {
  return 'bar';
}

const foo1: string | undefined = getText1();
export const v1 = foo1 ?? 'a string';

const foo2: string | null = getText2();
export const v2 = foo2 ?? 'a string';

#### 反例

declare const a: string | null;
declare const b: string | null;

export const c = a || b;

#### 规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。

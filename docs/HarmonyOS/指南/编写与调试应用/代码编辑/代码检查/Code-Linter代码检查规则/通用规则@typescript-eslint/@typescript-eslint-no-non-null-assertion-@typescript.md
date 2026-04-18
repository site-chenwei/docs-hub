---
title: "@typescript"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-non-null-assertion"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "通用规则@typescript-eslint"
  - "@typescript-eslint/no-non-null-assertion"
captured_at: "2026-04-17T01:36:45.621Z"
---

# @typescript-eslint/no-non-null-assertion

禁止以感叹号作为后缀的方式使用非空断言。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-non-null-assertion": "error"
  }
}

#### 选项

该规则无需配置额外选项。

#### 正例

interface Example {
  property?: string;
}

declare const example: Example;
export const includesBaz = example.property?.includes('baz') ?? false;

#### 反例

interface Example {
  property?: string;
}

declare const example: Example;
// 禁止使用"example.property!"的方式来进行非空断言
export const includesBaz = example.property!.includes('baz');

#### 规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。

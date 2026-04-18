---
title: "@typescript"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_require-array-sort-compare"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "通用规则@typescript-eslint"
  - "@typescript-eslint/require-array-sort-compare"
captured_at: "2026-04-17T01:36:46.200Z"
---

# @typescript-eslint/require-array-sort-compare

要求调用“Array#sort”时，始终提供“compareFunction”。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/require-array-sort-compare": "error"
  }
}

#### 选项

详情请参考[@typescript-eslint/require-array-sort-compare选项](https://typescript-eslint.nodejs.cn/rules/require-array-sort-compare/#options)。

#### 正例

declare const array: string\[\];

array.sort((a, b) => a.length - b.length);
array.sort((a, b) => a.localeCompare(b));

#### 反例

declare const array: number\[\];
declare const stringArray: object\[\];

array.sort();

// String arrays should be sorted using \`String#localeCompare\`.
stringArray.sort();

#### 规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。

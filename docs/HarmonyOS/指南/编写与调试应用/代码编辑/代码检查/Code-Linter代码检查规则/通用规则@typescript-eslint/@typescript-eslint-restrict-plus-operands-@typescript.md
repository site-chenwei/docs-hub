---
title: "@typescript"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_restrict-plus-operands"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "通用规则@typescript-eslint"
  - "@typescript-eslint/restrict-plus-operands"
captured_at: "2026-04-17T01:36:46.148Z"
---

# @typescript-eslint/restrict-plus-operands

要求加法的两个操作数都是相同的类型，并且是“bigint”、“number”或“string”。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/restrict-plus-operands": "error"
  }
}

#### 选项

详情请参考[@typescript-eslint/restrict-plus-operands选项](https://typescript-eslint.nodejs.cn/rules/restrict-plus-operands/#options)。

#### 正例

const num = 10;
const bigIntNum = 1n;
export const foo1 = parseInt('5.5', num) + num;
export const foo2 = bigIntNum + bigIntNum;

#### 反例

const num = 10;
const bigIntNum = 1n;
export const foo2 = bigIntNum + num;

#### 规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。

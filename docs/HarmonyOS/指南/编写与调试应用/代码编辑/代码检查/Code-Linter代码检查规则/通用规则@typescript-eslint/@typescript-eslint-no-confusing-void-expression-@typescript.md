---
title: "@typescript"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-confusing-void-expression"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "通用规则@typescript-eslint"
  - "@typescript-eslint/no-confusing-void-expression"
captured_at: "2026-04-17T01:36:45.273Z"
---

# @typescript-eslint/no-confusing-void-expression

要求void类型的表达式出现在合适的位置。

void指要被忽略的函数返回，如果将void类型的表达式作为值使用，比如分配给变量、作为函数参数传递或者从函数中返回，容易产生误导。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-confusing-void-expression": "error"
  }
}

#### 选项

详情请参考[@typescript-eslint/no-confusing-void-expression选项](https://typescript-eslint.nodejs.cn/rules/no-confusing-void-expression/#options)。

#### 正例

export function func(): void {
  console.info('no return');
}

#### 反例

export function func(): void {
  return console.info('no return');
}

console.info(func());

#### 规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。

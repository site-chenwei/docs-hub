---
title: "@typescript"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_comma-dangle"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "通用规则@typescript-eslint"
  - "@typescript-eslint/comma-dangle"
captured_at: "2026-04-17T01:36:44.976Z"
---

# @typescript-eslint/comma-dangle

允许或禁止使用尾随逗号。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/comma-dangle": "error"
  }
}

#### 选项

详情请参考[@typescript-eslint/comma-dangle选项](https://eslint.nodejs.cn/docs/rules/comma-dangle#选项)。

#### 正例

// 默认不允许尾随逗号
interface MyType {
  bar: string;
  qux: string;
}

const foo: MyType = {
  bar: 'baz',
  qux: 'qux'
};

const arr = \['1', '2'\];

export { foo, arr };

#### 反例

interface MyType {
  bar: string;
  qux: string;
}

const foo: MyType = {
  bar: 'baz',
  qux: 'qux',
};

const arr = \['1', '2',\];

export { foo, arr, };

#### 规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。

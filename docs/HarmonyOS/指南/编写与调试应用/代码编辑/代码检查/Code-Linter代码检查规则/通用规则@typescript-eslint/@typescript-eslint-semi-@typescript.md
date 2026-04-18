---
title: "@typescript"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_semi"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "通用规则@typescript-eslint"
  - "@typescript-eslint/semi"
captured_at: "2026-04-17T01:36:46.161Z"
---

# @typescript-eslint/semi

要求或不允许使用分号。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/semi": "error"
  }
}

#### 选项

详情请参考[@typescript-eslint/semi选项](https://eslint.nodejs.cn/docs/rules/semi#选项)。

#### 正例

export const name = 'ESLint';

export class Foo {
  public bar = '1';
}

#### 反例

// 默认在语句末尾需要加分号
export const name = 'ESLint'

export class Foo {
  // 默认在语句末尾需要加分号
  public bar = '1'
}

#### 规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。

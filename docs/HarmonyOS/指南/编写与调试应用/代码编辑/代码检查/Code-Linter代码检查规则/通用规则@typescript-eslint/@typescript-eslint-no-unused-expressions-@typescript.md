---
title: "@typescript"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unused-expressions"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "通用规则@typescript-eslint"
  - "@typescript-eslint/no-unused-expressions"
captured_at: "2026-04-17T01:36:45.831Z"
---

# @typescript-eslint/no-unused-expressions

代码中禁止包含未使用的表达式。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-unused-expressions": "error"
  }
}

#### 选项

详情请参考[@typescript-eslint/no-unused-expressions选项](https://eslint.nodejs.cn/docs/rules/no-unused-expressions#选项)。

#### 正例

export const v1 = Number.MAX\_VALUE;

if ('hello'.length === v1) {
  console.info('hello');
}

{
  const v2 = '0';
  console.info(v2);
}

#### 反例

Number.MAX\_VALUE;

if ('0') '0';

{'0';}

#### 规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。

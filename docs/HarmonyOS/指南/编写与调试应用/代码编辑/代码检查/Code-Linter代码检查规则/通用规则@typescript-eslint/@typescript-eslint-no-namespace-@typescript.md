---
title: "@typescript"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-namespace"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "通用规则@typescript-eslint"
  - "@typescript-eslint/no-namespace"
captured_at: "2026-04-17T01:36:45.530Z"
---

# @typescript-eslint/no-namespace

禁止使用 TypeScript语法中的命名空间。

命名空间是一种过时的语法，推荐使用import/export。

该规则仅支持对.js/.ts文件进行检查。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-namespace": "error"
  }
}

#### 选项

详情请参考[@typescript-eslint/no-namespace选项](https://typescript-eslint.nodejs.cn/rules/no-namespace/#options)。

#### 正例

// foo为模块名
declare module 'foo' {}
// anything inside a d.ts file

#### 反例

module foo {}
namespace foo {}

declare module foo {}
declare namespace foo {}

#### 规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。

---
title: "@typescript"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_array-type"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "通用规则@typescript-eslint"
  - "@typescript-eslint/array-type"
captured_at: "2026-04-17T01:36:44.819Z"
---

# @typescript-eslint/array-type

定义数组类型时，建议使用相同的样式。比如都使用T\[\]或者都使用Array<T>。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/array-type": "error"
  }
}

#### 选项

详情请参考[typescript/array-type 选项](https://typescript-eslint.nodejs.cn/rules/array-type#options)。

#### 正例

const x: string\[\] = \['a', 'b'\];
const y: readonly string\[\] = \['a', 'b'\];

export { x, y };

#### 反例

const x: Array<string> = \['a', 'b'\];
const y: ReadonlyArray<string> = \['a', 'b'\];

export { x, y };

#### 规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。

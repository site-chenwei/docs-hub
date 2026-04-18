---
title: "@typescript"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unnecessary-qualifier"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "通用规则@typescript-eslint"
  - "@typescript-eslint/no-unnecessary-qualifier"
captured_at: "2026-04-17T01:36:45.728Z"
---

# @typescript-eslint/no-unnecessary-qualifier

禁止不必要的命名空间限定符。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-unnecessary-qualifier": "error"
  }
}

#### 选项

该规则无需配置额外选项。

#### 正例

export enum A {
  b = 'x',
  c = b
}

export namespace B {
  export type C = number;
  export const x: C = 3;
}

#### 反例

export enum A {
  b = 'x',
  c = A.b
}

export namespace B {
  export type C = number;
  export const x: B.C = 3;
}

#### 规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。

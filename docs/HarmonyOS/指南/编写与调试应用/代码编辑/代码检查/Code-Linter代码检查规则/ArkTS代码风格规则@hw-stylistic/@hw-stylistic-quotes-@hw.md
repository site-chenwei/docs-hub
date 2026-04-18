---
title: "@hw"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-quotes-stylistic"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "ArkTS代码风格规则@hw-stylistic"
  - "@hw-stylistic/quotes"
captured_at: "2026-04-17T01:36:48.215Z"
---

# @hw-stylistic/quotes

强制字符串使用单引号。该规则仅检查.ets文件类型。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@hw-stylistic/quotes": "error"
  }
}

#### 选项

该规则无需配置额外选项。

#### 正例

export {a, b};

const a = 'hello';
const b = \`hello\`;

#### 反例

// Strings must use single quotes.
export const a = "hello";

#### 规则集

"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。

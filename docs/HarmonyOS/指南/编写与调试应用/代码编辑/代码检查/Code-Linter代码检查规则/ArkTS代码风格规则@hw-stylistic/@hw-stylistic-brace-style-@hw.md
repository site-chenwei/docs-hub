---
title: "@hw"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-brace-style-stylistic"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "ArkTS代码风格规则@hw-stylistic"
  - "@hw-stylistic/brace-style"
captured_at: "2026-04-17T01:36:48.007Z"
---

# @hw-stylistic/brace-style

强制大括号和语句位于同一行。该规则仅检查.ets文件类型。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@hw-stylistic/brace-style": "error"
  }
}

#### 选项

该规则无需配置额外选项。

#### 正例

try {
  // doSomething
} catch (e) {
  // doSomething
} finally {
  // doSomething
}

#### 反例

try
// Opening curly brace does not appear on the same line as statement before.
{

// Closing curly brace does not appear on the same line as statement after.
}
catch (e)
// Opening curly brace does not appear on the same line as statement before.
{

// Closing curly brace does not appear on the same line as statement after.
}
finally
// Opening curly brace does not appear on the same line as statement before.
{

}

#### 规则集

"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。

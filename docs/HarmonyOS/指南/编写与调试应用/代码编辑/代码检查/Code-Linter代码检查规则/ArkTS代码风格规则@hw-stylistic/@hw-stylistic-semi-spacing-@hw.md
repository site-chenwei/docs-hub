---
title: "@hw"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_semi-spacing"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "ArkTS代码风格规则@hw-stylistic"
  - "@hw-stylistic/semi-spacing"
captured_at: "2026-04-17T01:36:48.239Z"
---

# @hw-stylistic/semi-spacing

强制分号之前不加空格。该规则仅检查.ets文件类型。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@hw-stylistic/semi-spacing": "error"
  }
}

#### 选项

该规则无需配置额外选项。

#### 正例

export {x, test, C};

const x = 10;

function test(size: number): number {
  let sum = 0;
  for (let a = 0; a < size; a++) {
    sum += a;
  }
  return sum;
}

class C {
  public name: string = 'hello';
}

#### 反例

// Unexpected whitespace before semicolon.
export {x, test, C} ;

// Unexpected whitespace before semicolon.
const x = 10 ;

function test(size: number): number {
  let sum = 0;
  // Unexpected whitespace before semicolon.
  // Unexpected whitespace before semicolon.
  for (let a = 0 ; a < size ; a++) {
    sum += a;
  }
  // Unexpected whitespace before semicolon.
  return sum ;
}

class C {
  // Unexpected whitespace before semicolon.
  public name: string = 'hello' ;
}

#### 规则集

"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。

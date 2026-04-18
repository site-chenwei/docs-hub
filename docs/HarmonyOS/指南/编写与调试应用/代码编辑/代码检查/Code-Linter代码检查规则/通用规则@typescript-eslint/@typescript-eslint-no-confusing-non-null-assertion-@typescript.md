---
title: "@typescript"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-confusing-non-null-assertion"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "通用规则@typescript-eslint"
  - "@typescript-eslint/no-confusing-non-null-assertion"
captured_at: "2026-04-17T01:36:45.194Z"
---

# @typescript-eslint/no-confusing-non-null-assertion

不允许在可能产生混淆的位置使用非空断言。

在赋值或者等于旁边使用非空断言（!）会产生混淆，看起来类似于不等于，不建议这种写法。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-confusing-non-null-assertion": "error"
  }
}

#### 选项

该规则无需配置额外选项。

#### 正例

interface Foo {
  bar?: string;
  num?: number;
}

function getFoo(): Foo {
  return {
    bar: 'bar',
    num: Number.MAX\_VALUE
  };
}
const foo: Foo = getFoo();
export const isEqualsBar = foo.bar === 'hello';
const num = 2;
export const isEqualsNum = num + (foo.num!) === num;

#### 反例

interface Foo {
  bar?: string;
  num?: number;
}

function getFoo(): Foo {
  return {
    bar: 'bar',
    num: Number.MAX\_VALUE
  };
}
const foo: Foo = getFoo();
// 可能会产生混淆，误以为是不等于
export const isEqualsBar = foo.bar! === 'hello';
// 可能会产生混淆，误以为是不等于
const num = 2;
export const isEqualsNum = num + foo.num! === num;

#### 规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。

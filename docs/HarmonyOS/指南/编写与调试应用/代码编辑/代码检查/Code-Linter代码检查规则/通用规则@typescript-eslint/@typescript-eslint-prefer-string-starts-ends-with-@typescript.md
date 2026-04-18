---
title: "@typescript"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-string-starts-ends-with"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "通用规则@typescript-eslint"
  - "@typescript-eslint/prefer-string-starts-ends-with"
captured_at: "2026-04-17T01:36:46.065Z"
---

# @typescript-eslint/prefer-string-starts-ends-with

强制使用“String#startsWith”和“String#endsWith”而不是其他检查子字符串的等效方法。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/prefer-string-starts-ends-with": "error"
  }
}

#### 选项

该规则无需配置额外选项。

#### 正例

declare const foo: string;

// starts with
foo.startsWith('bar');

// ends with
foo.endsWith('bar');

#### 反例

declare const foo: string;
declare const index: number;
// starts with
foo\[index\] === 'b';
foo.charAt(index) === 'b';
foo.indexOf('bar') === index;
foo.slice(index) === 'bar';
foo.substring(index) === 'bar';
foo.match(/^bar/) !== null;
/^bar/.test(foo);

// ends with
foo\[foo.length - index\] === 'b';
foo.charAt(foo.length - index) === 'b';
foo.lastIndexOf('bar') === foo.length - index;
foo.slice(-index) === 'bar';
foo.substring(foo.length - index) === 'bar';
foo.match(/bar$/) !== null;
/bar$/.test(foo);

#### 规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。

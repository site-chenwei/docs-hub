---
title: "@typescript"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_require-await"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "通用规则@typescript-eslint"
  - "@typescript-eslint/require-await"
captured_at: "2026-04-17T01:36:46.195Z"
---

# @typescript-eslint/require-await

异步函数必须包含“await”。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/require-await": "error"
  }
}

#### 选项

该规则无需配置额外选项。

#### 正例

async function doSomething(): Promise<void> {
  return Promise.resolve();
}

export async function foo() {
  await doSomething();
}

export function baz() {
  doSomething().catch(() => {
    console.info('error');
  });
}

#### 反例

async function doSomething(): Promise<void> {
  return Promise.resolve();
}

export async function foo() {
  doSomething();
}

#### 规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。

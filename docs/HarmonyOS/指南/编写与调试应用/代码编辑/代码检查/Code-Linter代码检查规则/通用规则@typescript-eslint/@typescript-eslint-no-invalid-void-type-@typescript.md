---
title: "@typescript"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-invalid-void-type"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "通用规则@typescript-eslint"
  - "@typescript-eslint/no-invalid-void-type"
captured_at: "2026-04-17T01:36:45.520Z"
---

# @typescript-eslint/no-invalid-void-type

禁止在返回类型或者泛型类型之外使用void。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-invalid-void-type": "error"
  }
}

#### 选项

详情请参考[@typescript-eslint/no-invalid-void-type选项](https://typescript-eslint.nodejs.cn/rules/no-invalid-void-type/#options)。

#### 正例

export type NoOp = () => void;
export function noop(): void {
  console.info('noop');
}
export const trulyUndefined = void Number.MAX\_VALUE;
export async function promiseMeSomething(): Promise<void> {
  return Promise.reject('value').catch(() => {
    console.error('error');
  });
}
export type StillVoid = void | never;

#### 反例

// 不允许使用void作为类型
export type PossibleValues = string | number | void;
// 不允许使用void作为类型
export type MorePossibleValues = string | (string | void);

// 不允许使用void作为类型
export function logSomething(thing: void) {
  return thing;
}
export function printArg<T = void>(arg: T) {
  return arg;
}

export interface Interface {
  lambda: () => void;
  // 不允许使用void作为类型
  prop: void;
}

#### 规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。

---
title: "@typescript"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_ban-ts-comment"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "通用规则@typescript-eslint"
  - "@typescript-eslint/ban-ts-comment"
captured_at: "2026-04-17T01:36:44.845Z"
---

# @typescript-eslint/ban-ts-comment

不允许使用\`@ts-<directional>\`格式的注释，或要求在注释后进行补充说明。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/ban-ts-comment": "error"
  }
}

#### 选项

详情请参考[@typescript-eslint/ban-ts-comment选项](https://typescript-eslint.nodejs.cn/rules/ban-ts-comment/#options)。

#### 正例

console.log('hello');

#### 反例

// @ts-expect-error
console.log('hello');

/\* @ts-expect-error \*/
console.log('hello');

#### 规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。

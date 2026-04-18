---
title: "@typescript"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_typedef"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "通用规则@typescript-eslint"
  - "@typescript-eslint/typedef"
captured_at: "2026-04-17T01:36:46.285Z"
---

# @typescript-eslint/typedef

在某些位置需要类型注释。

支持检查的范围从选项中查看。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/typedef": "error"
  }
}

#### 选项

详情请参考[@typescript-eslint/typedef选项](https://typescript-eslint.nodejs.cn/rules/typedef#options)。

#### 正例

export const text = 'text';

#### 反例

// 默认配置下，规则不会告警

#### 规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。

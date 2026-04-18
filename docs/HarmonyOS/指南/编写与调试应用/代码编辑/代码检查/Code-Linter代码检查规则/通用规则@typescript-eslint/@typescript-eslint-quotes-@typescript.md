---
title: "@typescript"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_quotes"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "通用规则@typescript-eslint"
  - "@typescript-eslint/quotes"
captured_at: "2026-04-17T01:36:46.108Z"
---

# @typescript-eslint/quotes

强制使用一致的反引号、双引号或单引号风格。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/XlRijc_lQeSN8Rfh5drj8A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013646Z&HW-CC-Expire=86400&HW-CC-Sign=0D6A6437A62F8904294412BBCF99C071A3F995CCBE63A0454BB89ECF67972C19)

-   该规则默认检查字符串是否正确使用双引号。如需修改请参考[选项](#section182418564158)。
-   该规则建议在对.ts文件进行检查时使用。如需检查.ets文件，建议使用[@hw-stylistic/quotes](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-quotes-stylistic)。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/quotes": "error"
  }
}

#### 选项

详情请参考[@typescript-eslint/quotes选项](https://eslint.nodejs.cn/docs/latest/rules/quotes#选项)。

#### 正例

export const double = "double";
export const foo = \`back
tick\`;  // backticks are allowed due to newline

#### 反例

// 默认推荐使用双引号
export const single = 'single';
export const unescaped = 'a string containing "double" quotes';
export const backtick = \`back\\ntick\`; // you can use \\n in single or double quoted strings

#### 规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。

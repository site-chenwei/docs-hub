---
title: "@typescript"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-require-imports"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "通用规则@typescript-eslint"
  - "@typescript-eslint/no-require-imports"
captured_at: "2026-04-17T01:36:45.634Z"
---

# @typescript-eslint/no-require-imports

禁止使用“require()”语法导入依赖。

该规则仅支持对.js/.ts文件进行检查。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-require-imports": "error"
  }
}

#### 选项

该规则无需配置额外选项。

#### 正例

// lib1 lib2 lib3为.js/.ts文件
import \* as lib1 from './lib1';
import { lib2 } from './lib2';
import \* as lib3 from './lib3';

#### 反例

// lib3为.js/.ts文件
import lib3 = require('./lib3');

#### 规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。

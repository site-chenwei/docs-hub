---
title: "@typescript"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_brace-style"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "通用规则@typescript-eslint"
  - "@typescript-eslint/brace-style"
captured_at: "2026-04-17T01:36:44.963Z"
---

# @typescript-eslint/brace-style

对代码块强制执行一致的括号样式。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/brace-style": "error"
  }
}

#### 选项

详情请参考[@typescript-eslint/brace-style选项](https://eslint.nodejs.cn/docs/rules/brace-style#选项)。

#### 正例

function foo(): boolean {
  return true;
}

class C {
  static {
    foo();
  }

  public meth() {
    foo();
  }
}

export { C };

#### 反例

function foo(): boolean 
{
  return true;
}

class C {
  static 
  {
    foo();
  }

  public meth() 
  {
    foo();
  }
}

export { C };

#### 规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。

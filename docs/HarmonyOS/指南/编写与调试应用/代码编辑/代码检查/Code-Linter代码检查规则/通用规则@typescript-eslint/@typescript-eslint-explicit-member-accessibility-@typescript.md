---
title: "@typescript"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_explicit-member-accessibility"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "通用规则@typescript-eslint"
  - "@typescript-eslint/explicit-member-accessibility"
captured_at: "2026-04-17T01:36:45.064Z"
---

# @typescript-eslint/explicit-member-accessibility

在类属性和方法上需要显式定义访问修饰符。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/explicit-member-accessibility": "error"
  }
}

#### 选项

详情请参考[@typescript-eslint/explicit-member-accessibility选项](https://typescript-eslint.nodejs.cn/rules/explicit-member-accessibility)。

#### 正例

export class Animal {
  private animalName: string; // Property

  public constructor(name: string) {
    // Parameter property and constructor
    this.animalName = name;
  }

  public get name(): string {
    // get accessor
    return this.animalName;
  }

  public set name(value: string) {
    // set accessor
    this.animalName = value;
  }

  public walk() {
    // method
  }
}

#### 反例

export class Animal {
  private animalName: string; // Property

  constructor(name: string) {
    // Parameter property and constructor
    this.animalName = name;
  }

  get name(): string {
    // get accessor
    return this.animalName;
  }

  set name(value: string) {
    // set accessor
    this.animalName = value;
  }

  walk() {
    // method
  }
}

#### 规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。

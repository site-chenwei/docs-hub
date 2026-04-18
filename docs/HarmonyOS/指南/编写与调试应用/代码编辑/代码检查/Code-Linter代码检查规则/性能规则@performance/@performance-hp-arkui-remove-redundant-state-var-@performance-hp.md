---
title: "@performance/hp"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hp-arkui-remove-redundant-state-var"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "性能规则@performance"
  - "@performance/hp-arkui-remove-redundant-state-var"
captured_at: "2026-04-17T01:36:46.995Z"
---

# @performance/hp-arkui-remove-redundant-state-var

建议移除不关联UI组件的状态变量设置。

通用丢帧场景下，建议优先修改。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@performance/hp-arkui-remove-redundant-state-var": "suggestion",
  }
}

#### 选项

该规则无需配置额外选项。

#### 正例

@Entry
@Component
struct MyComponent {
  @State message: string = "";

  appendMsg(newMsg: string): string {
    this.message += newMsg;
    return this.message;
  }

  build() {
    Column() {
      Stack() {
        Text(this.message)
      }
      .backgroundColor("black")
      .width(200)
      .height(400)

      Button("move")
    }
  }
}

#### 反例

@Entry
@Component
struct MyComponent {
  @State message: string = "";

  appendMsg(newMsg: string): string {
    this.message += newMsg;
    return this.message;
  }

  build() {
    Column() {
      Stack() {
      }
      .backgroundColor("black")
      .width(200)
      .height(400)

      Button("move")
    }
  }
}

#### 规则集

plugin:@performance/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。

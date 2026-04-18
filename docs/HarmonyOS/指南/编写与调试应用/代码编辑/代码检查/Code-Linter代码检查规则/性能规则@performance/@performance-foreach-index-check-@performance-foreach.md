---
title: "@performance/foreach"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-foreach-index-check"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "性能规则@performance"
  - "@performance/foreach-index-check"
captured_at: "2026-04-17T01:36:46.746Z"
---

# @performance/foreach-index-check

使用Foreach组件时，不建议在keyGenerator中使用index作为返回值或者返回值的一部分，可能会导致性能问题。

[滑动丢帧场景](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-foreach#渲染性能降低)下，建议优先修改。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@performance/foreach-index-check": "suggestion",
  }
}

#### 选项

该规则无需配置额外选项。

#### 正例

@Entry
@Component
struct ForeachTest {
  private data: string\[\] = \['one', 'two', 'three'\];
  build() {
    RelativeContainer() {
      List() {
        ForEach(this.data, (item: string, index: number) => {
          ListItem() {
            Text(item);
          }
        }, (item: string, index: number) => item)
      }
      .width('100%')
      .height('100%')
    }
    .height('100%')
    .width('100%')
  }
}

#### 反例

@Entry
@Component
struct ForeachTest {
  private data: string\[\] = \['one', 'two', 'three'\];
  build() {
    RelativeContainer() {
      List() {
        // warning line
        ForEach(this.data, (item: string, index: number) => {
          ListItem() {
            Text(item);
          }
        }, (item: string, index: number) => item + index)
      }
      .width('100%')
      .height('100%')
    }
    .height('100%')
    .width('100%')
  }
}

#### 规则集

plugin:@performance/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。

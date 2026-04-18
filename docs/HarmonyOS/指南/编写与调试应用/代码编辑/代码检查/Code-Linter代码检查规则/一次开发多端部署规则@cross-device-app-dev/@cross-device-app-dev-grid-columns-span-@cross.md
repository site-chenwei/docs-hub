---
title: "@cross"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_grid-columns-span"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "一次开发多端部署规则@cross-device-app-dev"
  - "@cross-device-app-dev/grid-columns-span"
captured_at: "2026-04-17T01:36:47.842Z"
---

# @cross-device-app-dev/grid-columns-span

不推荐开发者将栅格中所有的GridCol子组件只设置span属性，且值与父组件的columns属性相等。这等效于子组件宽度始终为父容器的100%，栅格系统没有发挥作用，徒增页面组件树复杂度，影响性能。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@cross-device-app-dev/grid-columns-span": "warn"
  }
}

#### 选项

该规则无需配置额外选项。

#### 正例

@Entry
@Component
struct Index {
  build() {
    Column() {
      GridRow({
        columns: { sm: 4, md: 8, lg: 12 }
      }) {
        GridCol({
          span: { sm: 4, md: 4, lg: 4 }, offset: { sm: 0, md: 2, lg: 4 }
        }) {
          Row().backgroundColor($r('sys.color.ohos\_id\_color\_palette\_aux1'))
        }
      }
    }
  }
}

#### 反例

@Entry
@Component
struct Index {
  build() {
    Column() {
      GridRow({
        columns: { sm: 4, md: 8, lg: 12 }
      }) {
        GridCol({
          span: { sm: 4, md: 8, lg: 12 }
        }) {
          Row().backgroundColor($r('sys.color.ohos\_id\_color\_palette\_aux1'))
        }
      }
    }
  }
}

#### 规则集

plugin:@cross-device-app-dev/recommended
plugin:@cross-device-app-dev/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。

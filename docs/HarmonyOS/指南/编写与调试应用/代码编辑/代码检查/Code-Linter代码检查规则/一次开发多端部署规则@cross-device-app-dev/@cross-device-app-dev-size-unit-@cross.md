---
title: "@cross"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_size-unit"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "一次开发多端部署规则@cross-device-app-dev"
  - "@cross-device-app-dev/size-unit"
captured_at: "2026-04-17T01:36:47.948Z"
---

# @cross-device-app-dev/size-unit

组件通用属性width、height和size，应当使用vp作为单位，以适配不同设备屏幕宽度。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@cross-device-app-dev/size-unit": "warn"
  }
}

#### 选项

该规则无需配置额外选项。

#### 正例

const WIDTH\_SIZE = 100;

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('btn').size({ width: 40, height: '20vp' })
      }.width(WIDTH\_SIZE)
      .height('100vp')
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center)
  }
}

#### 反例

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('btn').size({ width: '40px', height: '20px' })
      }.width('100px')
      .height('100px')
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center)
  }
}

#### 规则集

plugin:@cross-device-app-dev/recommended
plugin:@cross-device-app-dev/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。

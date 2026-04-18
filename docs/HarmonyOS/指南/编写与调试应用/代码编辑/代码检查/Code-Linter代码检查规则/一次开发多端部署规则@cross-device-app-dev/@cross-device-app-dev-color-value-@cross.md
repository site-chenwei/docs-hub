---
title: "@cross"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_color-value"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "代码编辑"
  - "代码检查"
  - "Code Linter代码检查规则"
  - "一次开发多端部署规则@cross-device-app-dev"
  - "@cross-device-app-dev/color-value"
captured_at: "2026-04-17T01:36:47.896Z"
---

# @cross-device-app-dev/color-value

颜色值应当使用“$r”从color.json中引用，以适配不同的系统颜色模式，禁止使用固定的值。

#### 规则配置

// code-linter.json5
{
  "rules": {
    "@cross-device-app-dev/color-value": "warn"
  }
}

#### 选项

该规则无需配置额外选项。

#### 正例

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      // 通过'sys.color.xxx'引用的颜色值，默认支持dark和light颜色模式
      Text()
        .fontColor($r('sys.color.ohos\_id\_color\_activated'));
      // 通过'app.color.xxx'引用的颜色值，需要分别在dark和light颜色模式的color.json中配置
      Text()
        .fontColor($r('app.color.text\_color'));
    }
  }
}

#### 反例

@Entry
@Component
struct Index1 {
  build() {
    RelativeContainer() {
      Text('message').fontColor('#000000')
      Text('message').fontColor('rgb(0, 0, 0)')
      Text('message').fontColor(Color.Black)
    }
  }
}

#### 规则集

plugin:@cross-device-app-dev/recommended
plugin:@cross-device-app-dev/all

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter)。
